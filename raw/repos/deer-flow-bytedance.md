# DeerFlow — ByteDance Async Agent Framework

source: https://github.com/bytedance/deer-flow
fetched: 2026-04-06
type: repo
notes: >
  Análise focada em concorrência, rate limiting, message gateway.
  Conteúdo extraído via análise do código-fonte do repositório principal.

---

## AsyncStreamBridge (Message Gateway)

Producer-consumer pattern via asyncio.Condition + deque bounded.

```python
class MemoryStreamBridge:
    def __init__(self):
        self._streams: dict[str, deque[StreamEvent]] = {}
        self._conditions: dict[str, asyncio.Condition] = {}

    async def publish(self, run_id: str, event: StreamEvent) -> None:
        if len(self._streams[run_id]) > self._maxsize:
            self._streams[run_id].popleft()
        await self._conditions[run_id].notify_all()

    async def subscribe(self, run_id: str, last_event_id: str | None = None):
        async with self._conditions[run_id]:
            while True:
                for event in remaining_events:
                    yield event
                try:
                    await asyncio.wait_for(self._conditions[run_id].wait(), timeout=15.0)
                except asyncio.TimeoutError:
                    yield HEARTBEAT_SENTINEL
```

Key: asyncio.Condition permite múltiplos subscribers concorrentes no mesmo run_id.
Heartbeat a cada 15s evita timeout em SSE connections.

## RunManager (Atomic Concurrent Registry)

```python
class RunManager:
    def __init__(self):
        self._lock = asyncio.Lock()
        self._runs: dict[str, RunRecord] = {}

    async def create_or_reject(self, run_id, thread_id, strategy="reject") -> RunRecord:
        async with self._lock:  # lock abrange check + create (TOCTOU-safe)
            existing = self._runs.get(run_id)
            if existing:
                if strategy == "reject":
                    raise ConflictError(...)
                elif strategy in ("interrupt", "rollback"):
                    existing.task.cancel()
            record = RunRecord(run_id=run_id, abort_event=asyncio.Event(), ...)
            self._runs[run_id] = record
            return record
```

Multirun strategies: reject | interrupt | rollback.

## Rate Limiting: Exponential Backoff + Jitter

Provider-specific retry. Respeita Retry-After header.

```python
backoff_ms = 2000 * (1 << (attempt - 1))  # 2s, 4s, 8s
jitter_ms = int(backoff_ms * 0.2)
total_ms = backoff_ms + random.randint(0, jitter_ms)

if "Retry-After" in e.response.headers:
    server_delay = parse_retry_after(...)
    total_ms = max(total_ms, server_delay)

await asyncio.sleep(total_ms / 1000.0)
```

MAX_RETRIES = 3. Error classification: transient | quota | auth.
Quota retorna mensagem amigável (não raise). Auth idem.

## Background Task com Abort Signal

Graceful cancellation via asyncio.Event (não forceful).

```python
async for event in graph.astream(input_dict, ...):
    if record.abort_event.is_set():
        break
    await bridge.publish(record.run_id, stream_event)
```

Cleanup diferido: asyncio.create_task(bridge.cleanup(run_id, delay_seconds=5.0))
Permite client coletar estado final antes do cleanup.

## Middleware Chain (14 steps, sequencial)

ThreadDataMiddleware → UploadsMiddleware → SandboxAuditMiddleware →
ToolErrorHandlingMiddleware → DanglingToolCallMiddleware →
GuardrailsMiddleware → SummarizationMiddleware → MemoryMiddleware →
VisionMiddleware → TokenUsageMiddleware → LoopDetectionMiddleware →
ClarificationMiddleware

Sem paralelismo no middleware — design intencional.

## Absence: Semaphore-Based Rate Limiting

DeerFlow NÃO usa asyncio.Semaphore para limitar concorrência de LLM calls.
Confia em retry logic por provider + buffer management.
Sem proactive request throttling.

## Client API

Síncrono por padrão (stream(), chat()). 
Async variants (astream(), achat()) para gather paralelo.
```python
results = await asyncio.gather(*[client.achat(q) for q in queries])
```
