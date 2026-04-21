# SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling

**arXiv:** 2604.14820  
**Authors:** Hao Han, Jin Xie, Xuehao Ma, Weiquan Zhu, Ziyao Zhang, ZhiLiang Long, Hongkai Chen, Qingwen Ye  
**Published:** 2026-04-16  
**Categories:** cs.SE

## Abstract

SWE-TRACE (Trajectory Reduction and Agentic Criteria Evaluation) addresses 3 bottlenecks in SWE agents: unoptimized demonstration data, sparse execution rewards, computationally prohibitive inference scaling. Three contributions: (1) SFT corpus biased toward shortest-path trajectories; (2) Rubric-Based PRM with dense intermediate step feedback; (3) Heuristic-guided Test-Time Scaling (HG-TTS).

## 3 Contributions

### 1. Data Curation: Shortest-Path SFT Corpus
- LLM multi-task cascading + step-wise oracle verification
- 60K instances biased toward token-efficient, shortest-path trajectories
- Explicitly filters out redundant exploration and repeated tool use
- **Problem**: fine-tuning on noisy agent traces teaches model to imitate inefficient search

### 2. Rubric-Based Process Reward Model (PRM)
- **Auxiliary Rubric-Agent**: provides dense, fine-grained heuristic feedback on INTERMEDIATE steps (not just outcomes)
- Rubric-Agent generates step-specific evaluation criteria (not static rubric)
- Memory-Augmented Agentic RL: rubric feedback guides RL training
- **Problem solved**: sparse outcome rewards (binary pass/fail on final patch) create reward hacking and policy degradation

### 3. Heuristic-Guided Test-Time Scaling (HG-TTS)
- Repurposes the Rubric PRM for inference
- Dynamically evaluates and PRUNES action candidates at each step
- No latency overhead of standard parallel sampling (TTS@16)
- **Problem solved**: computationally prohibitive inference scaling

## Results on SWE-Bench Verified

| Model | Backbone | Training | Resolve Rate |
|---|---|---|---|
| GPT-4o | — | — | 33.2% |
| o3 | — | — | 58.4% |
| Gemini 3 Pro | — | — | 74.2% |
| GLM-4.7 | — | — | 73.1% |
| SWE-TRACE-4B | Qwen3-4B | SFT+RL | 38.9% |
| SWE-TRACE-4B + HG-TTS | Qwen3-4B | SFT+RL | 40.7% |
| SWE-TRACE-30B | Qwen3-30B-A3B | SFT+RL | 63.5% |
| SWE-TRACE-30B + HG-TTS | Qwen3-30B-A3B | SFT+RL | **71.2%** |
| DeepSWE-32B + TTS@16 | Qwen3-32B | RL | 59.0% |
| SWE-Master-32B + TTS@8 | Qwen2.5-Coder-32B | SFT+RL | 70.8% |

SWE-TRACE-30B + HG-TTS reaches 71.2% — competitive with Gemini 3 Pro (74.2%) as open-weight model.

## Key Design Insights

1. **Rubric-as-process-reward**: dynamic per-step rubric generation > static pass/fail outcome reward
2. **Shortest-path bias**: training on efficient trajectories, not just correct ones
3. **PRM dual-use**: same rubric model for training AND inference (HG-TTS)
4. **Heuristic pruning > parallel sampling**: better search efficiency without TTS@16 cost

## Implications for Agentic Pipelines

- Dense step-level feedback (rubric) dramatically stabilizes RL for long-horizon tasks
- Test-time: using process reward model for pruning is more efficient than sampling many full trajectories
- Data quality (shortest-path) matters as much as quantity for SFT

## Relation to KB

- EXTENDS llm-as-judge: Rubric-Agent = dynamic criteria approach (CARMO/SALC) applied to RL training, not just evaluation
- EXTENDS self-improving-agents: ERL heuristics + PRM = convergent finding (structured per-step feedback > sparse outcome reward)
- CONFIRMS agentic-coding-failure-taxonomy: token bloat + policy degradation are concrete manifestations of Phase 2 planning failures
