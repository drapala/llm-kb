---
title: "Embedding Byzantine Fault Tolerance into Federated Learning via Consistency Scoring"
arxiv: "2411.10212"
year: 2024
type: paper
quality: secondary
note: "Síntese paramétrica — conhecimento de pré-treino, não texto primário recuperado"
---

# Embedding Byzantine Fault Tolerance into Federated Learning via Consistency Scoring

## Metadados

- **Autores**: Não especificado (paramétrico)
- **Ano**: 2024
- **arXiv**: 2411.10212
- **Status**: Síntese paramétrica baseada em conhecimento de treinamento

## Sumário

O paper aborda a vulnerabilidade de Federated Learning (FL) a ataques Byzantine de edge devices comprometidos. Propõe incorporar Byzantine Fault Tolerance (BFT) diretamente no processo de FL via consistency scoring — avaliando a consistência entre updates locais para filtrar participantes maliciosos — de forma que a resiliência se torna transparente e compatível com métodos FL existentes.

## Key Claims

1. **FL é vulnerável a Byzantine attacks**: Dispositivos edge comprometidos podem enviar updates maliciosos que degradam o modelo global. O problema é estrutural ao design de FL: sem verificação centralizada dos dados locais, qualquer participante pode ser um adversário.

2. **Virtual data samples como mecanismo de detecção**: A abordagem gera amostras de dados virtuais e as usa para avaliar consistency scores entre updates locais. Updates que divergem significativamente na resposta a essas amostras virtuais são marcados como suspeitos.

3. **Consistency scoring para filtrar updates comprometidos**: O sistema computa scores de consistência comparando as predições que cada update local produziria nas amostras virtuais. Updates com baixa consistência em relação ao conjunto são filtrados antes da agregação global.

4. **"Seamlessly embeds Byzantine resilience into existing FL methods"**: O design é não-intrusivo — pode ser aplicado sobre métodos FL existentes (FedAvg, FedProx, etc.) sem modificação fundamental da arquitetura. A BFT emerge como camada de validação, não como substituição do protocolo.

5. **Edge devices como vetor de ataque**: O foco em edge devices (vs. servidores intermediários) reflete a realidade de deployments FL em IoT, mobile e computação distribuída onde os participantes são heterogêneos e potencialmente não confiáveis.

## Metodologia (paramétrica)

- Geração de virtual data samples como probe
- Cálculo de consistency scores por update
- Filtro/ponderação de updates baseado em scores
- Avaliação em cenários com diferentes frações de participantes Byzantine

## Conexões com literatura

- Relacionado ao campo clássico de Byzantine Fault Tolerance (Lamport et al. 1982)
- Extensão de FL (McMahan et al. 2017 — FedAvg)
- Alternativa a abordagens baseadas em gradiente (Krum, Bulyan, FLTrust)

---

## Full Text (extracted from PDF, 6 pages)

Embedding Byzantine Fault Tolerance into
Federated Learning via Consistency Scoring
Youngjoon Lee1 , Jinu Gong2 , Joonhyuk Kang1
School of Electrical Engineering, KAIST, South Korea
2
Department of Applied AI, Hansung University, South Korea
Email: yjlee22@kaist.ac.kr, jinugong@hansung.kr, jkang@kaist.ac.kr

arXiv:2411.10212v3 [cs.LG] 17 Sep 2025

1

Abstract—Given sufficient data from multiple edge devices,
federated learning (FL) enables training a shared model without
transmitting private data to the central server. However, FL
is generally vulnerable to Byzantine attacks from compromised
edge devices, which can significantly degrade the model performance. In this work, we propose an intuitive plugin that
seamlessly embeds Byzantine resilience into existing FL methods.
The key idea is to generate virtual data samples and evaluate
model consistency scores across local updates to effectively filter
out compromised updates. By utilizing this scoring mechanism
before the aggregation phase, the proposed plugin enables
existing FL methods to become robust against Byzantine attacks
while maintaining their original benefits. Numerical results on
blood cell classification task demonstrate that the proposed
plugin provides strong Byzantine resilience. In detail, pluginattached FedAvg achieves over 89.6% test accuracy under 30%
targeted attacks (vs. 19.5% w/o plugin) and maintains 65–70%
test accuracy under untargeted attacks (vs. 17–19% w/o plugin).

Index Terms: e-health, federated learning, adversarial fault
tolerance, virtual data, consistency scoring

At edge devices

At central server
Conventional approach:

Edge device 1

Benign update
Poisoned global model

Edge device 2

Edge device 3
Edge device 4

Poisoning

Model aggregation
w/ plugin approach:

Optimal global model

Edge device 5
Poisoned model
Benign model

Proposed plugin

Fig. 1: Comparison of conventional FL and plugin-enhanced
FL under Byzantine attacks. In the conventional approach
(top), malicious edge devices (devices 3 and 4) inject poisoned
model updates that compromise the global model during aggregation. Our proposed plugin (bottom) effectively filters out
these poisoned updates to maintain model integrity, leading to
an optimal global model.

I. I NTRODUCTION
Recent advances in deep learning have transformed healthcare by leveraging large-scale medical datasets [1], [2]. However, strict patient privacy regulations and HIPAA compliance
requirements have created significant barriers to traditional
centralized analysis of healthcare data [3]. Federated learning
(FL) [4] has emerged as a promising framework for healthcare
applications [5]. This method enables collaborative learning of
medical AI models while preserving patient privacy through
secure parameter sharing [6]. For example, clinical diagnosis
and medical imaging analysis have shown significant improvements using this privacy-preserving paradigm [7].
While FL offers privacy benefits, implementing it in realworld healthcare systems faces significant challenges [8].
Healthcare data collected from different medical institutions
naturally exhibits data heterogeneity due to varying patient
populations and clinical protocols [9], [10]. Moreover, Byzantine threats pose a critical concern in federated medical
systems, as malicious participants can compromise the global
model through Byzantine attacks with poisoned updates [11].
This research was partly supported by the Institute of Information & Communications Technology Planning & Evaluation (IITP)-ITRC (Information
Technology Research Center) grant funded by the Korea government (MSIT)
(IITP-2025-RS-2020-II201787, contribution rate: 50%) and (IITP-2025-RS2023-00259991, contribution rate: 50%).

This vulnerability is particularly concerning in clinical applications where model failures could directly impact patient
safety and care outcomes [12]. Therefore, developing Byzantine robust FL against adversarial attacks while maintaining
model performance under heterogeneous conditions remains
an important challenge.
The novel plugin-based architecture proposed in Fig. 1
embeds Byzantine resilience into existing FL methods without
compromising their original benefits. Our plugin generates
virtual data samples to evaluate model behavior patterns,
computing consistency scores across local updates to detect
and filter malicious contributions while preserving the core
functionality of FL methods. Extensive experiments on medical imaging datasets demonstrate that this approach enhances
robustness while maintaining high performance across diverse
FL methods. Main contributions of this paper are as follows:
We propose a novel plugin to embed Byzantine resilience
into FL methods without altering their core principle.
• We propose a virtual data-driven scoring method to detect
and filter compromised local updates.
• We show our plugin’s compatibility and validate its
effectiveness through comprehensive experiments.
•

The remainder of this paper is organized as follows. Section

II provides background on representative FL methods. Section
III presents our novel modular plugin for FL. Section IV
demonstrate how our plugin enhances performance against
Byzantine attacks through extensive numerical evaluations.
II. P RELIMINARIES
To describe FL methods, we consider a federated network
with K edge devices, where each device k holds a local
dataset Dk . The goal of FL is to solve:
min F (w) =
w

1
|Dk |

K
X

Fk (w),

(1)

FedSpeed [18] accelerates convergence through proxcorrection and gradient perturbation:
˜ gke ,le − ∇F
ˆ gke + 1 (wge ,le − wge )),
wkge ,le +1 = wkge ,le − η(∇F
λ k
(6)
˜ ge ,le is a quasiwhere η denotes local learning rate and ∇F
k
ˆ gke is a prox-correction term. This technique
gradient, and ∇F
mitigates client drift while maintaining high generalization
through flat minima search, leading to faster convergence with
larger local intervals.
III. P ROBLEM AND M ODEL

k=1

P

where Fk (w) =
(x,y)∈Dk ℓ(w; x, y) represents the
local objective function of edge device k.
FedProx [13] addresses data heterogeneity by introducing a
proximal term in the local objective function, enforcing local
model updates to remain close to the global model:
µ
FkP rox (w) = Fk (w) + |w − wge |2 ,
(2)
2
where ge denotes global epoch and µ controls the client drift.
This proximal regularization allows FedProx to achieve more
stable convergence even when data across devices is highly
heterogeneous.
FedDyn [14] utilizes dynamic regularization to align local
optimization objectives with the global goal by adapting to
local optimization paths. The local objective in FedDyn is as
follows:
α
FkDyn (w) = Fk (w) + (hge )T (w − wge ) + |w − wge |2 , (3)
2
where α is a scaling factor and hge captures optimization
trajectory differences. Then, the central server aggregates
local updates and adjusts the global model using dynamic
control variates. This adaptive approach allows the model to
dynamically update regularization, ensuring a better fit to each
device’s unique data distribution.
FedRS [15] introduces a restricted softmax method to
tackle label distribution heterogeneity as follows:
exp(αck (wck )T hki )
k
ψi,c
= PC
,
k
k T k
j=1 exp(αj (wj ) hi )

(4)

where hki is the feature vector of the i-th sample and wck is the
classifier weight for class c on edge device k, αck is a scaling
factor to limit updates of missing classes while maintaining
normal softmax behavior for observed classes.
FedSAM [16] incorporates Sharpness-Aware Minimization
(SAM) [17] to enhance model generalization on heterogeneous data. SAM modifies the objective to minimize sharp
local optima by perturbing gradients:
∇Fk (wkge ,le + ϵ)
,
wkSAM = wkge ,le − ρ
|∇Fk (wkge ,le + ϵ)|
ge ,le
∇Fk (wk
)

(5)

where le denotes local epoch and ϵ = ρ |∇F (wge ,le )| is a
k
k
perturbation that stabilizes convergence by directing models
toward flatter minima.

A. Byzantine Attack and Non-IID Setting
We consider an FL environment vulnerable to both targeted
and untargeted model poisoning attacks in medical imaging
task as [19]. Specifically, the FL system comprises K participating edge devices, including B benign and M compromised
nodes, all connected to a central server. Each edge device k
maintains its private patient dataset Dk with varying sizes.
To preserve patient privacy, edge devices collaboratively train
a shared medical image classifier over G global epochs by
sharing only model parameters with the central server.
B. Plugin-based Byzantine-Resilient FL
In this section, we introduce a plugin-based approach
that enhances FedAvg’s resilience against Byzantine attacks
through feature-space analysis. First, benign edge devices
perform local learning, while malicious edge devices craft
Byzantine attacks. For benign edge devices b ∈ B, local
training aims to minimize the empirical loss:
X
1
ℓ(w; x, y),
(7)
Fb (w) =
|Db |
(x,y)∈Db

where ℓ(·) is the cross-entropy loss function. The local updates
are performed via SGD with learning rate η:
wbge ,le +1 = wbge ,le − η∇Fb (wbge ,le ; Bb ),

(8)

where Bb is a randomly sampled mini-batch from Db .
However, compromised edge devices m ∈ M may perform malicious updates through either targeted or untargeted
attacks. In targeted attacks, compromised devices alter their
local updates after L local training epochs, to mislead specific
samples while preserving overall performance.
ge ,L
ge ,L
wm
← wm
+ δm ,

(9)

ge ,L
δm = λ(wm
− wge ),

(10)

attack

where λ is a boosting factor designed to amplify the attack’s
impact. For untargeted attacks, malicious devices inject arbitrary noise to degrade overall performance:
ge
wm

← τ (w′ − wge ),

attack

w′ ∼ N (0, I),
with scaling factor τ and standard Gaussian noise.

(11)
(12)

𝑠 for benign edge device 1:

𝑠 for compromised edge device 3:

other updates as:

cos

𝑓1 − 𝑓𝑔 ,

𝑓2 − 𝑓𝑔

=

cos

𝑓3 − 𝑓𝑔 ,

𝑓1 − 𝑓𝑔

=

cos

𝑓1 − 𝑓𝑔 ,

𝑓3 − 𝑓𝑔

=

cos

𝑓3 − 𝑓𝑔 ,

𝑓2 − 𝑓𝑔

=

cos

𝑓1 − 𝑓𝑔 ,

𝑓4 − 𝑓𝑔

=

cos

𝑓3 − 𝑓𝑔 ,

𝑓4 − 𝑓𝑔

=

+ cos

𝑓1 − 𝑓𝑔 ,

𝑓5 − 𝑓𝑔

=

+ cos

𝑓3 − 𝑓𝑔 ,

𝑓5 − 𝑓𝑔

=

=

High performance AI model

𝑓𝑔 Global feature vector

=

𝑓𝑔 Benign feature vector

s̄k =

1 X
sk,j .
K −1

(17)

j̸=k

The server then sorts these average similarity scores
{s̄k }K
k=1 in ascending order and defines the set S as:

Low performance AI model

S = {k | π(s̄k ) > M },

𝑓𝑔 Poisoned feature vector

Fig. 2: Illustration of the proposed plugin’s scoring principle.
The plugin measures pairwise cosine similarities (denoted as
‘cos’) between feature vectors of model updates (f1 through
f5 ) relative to the global model (fg ). Benign models (blue)
have high cosine similarity with each other, whereas poisoned
models (red) show distinct patterns, enabling effective Byzantine attack filtering.

(18)

where π(s̄k ) denotes the position of s̄k in the sorted scores,
effectively excluding the M model updates with the lowest similarity scores as potential Byzantine attacks. The
Byzantine-resilient global model is then updated by averaging
the remaining model updates:
1 X
wge +1 =
wk .
(19)
|S|
k∈S

To filter these attacks, our plugin performs Byzantine attack
filtering using feature space analysis in three main steps:
deviation analysis, feature mapping, and similarity-based rejection. First, the central server generate N virtual samples
{vn }N
n=1 from a standard normal distribution N (0, I) to serve
as probe points for analyzing model behaviors. For each model
pair (wige , wjge ), the server compute their deviations from the
global model as:
∆wi = wige − wge , ∆wj = wjge − wge .

(13)

These deviation vectors capture how each local model update
differs from the current global model.
Next, the central server maps these deviations to feature
representations using a feature extractor gϕ (·), which is implemented as all layers of the base model except the final
classification layer. For each model pair (wi , wj ) and virtual
sample vn , the server computes:
Fi = {fi1 , fi2 , . . . , fiN } = g1:L−1 (vn ; ∆wi ),

(14)

Fj = {fj1 , fj2 , . . . , fjN } = g1:L−1 (vn ; ∆wj ),

(15)

where g1:L−1 denotes the feature extraction layers of the
model (all layers except the final classification layer), and
each fin , fjn ∈ Rd represents the d-dimensional feature vector
for the n-th virtual sample.
The server then computes the pairwise similarity between
models using the average cosine similarity over the N virtual
samples:
N

si,j =


1 X
cos fin , fjn , fin ∈ Fi , fjn ∈ Fj .
N n=1

(16)

where cos(fin , fjn ) measures the angular similarity between
feature vectors, with higher values indicating more similar
behavior patterns. As shown in Fig. 2, benign models naturally
cluster together with high similarity scores, whereas malicious
model updates exhibit distinct patterns. For each model update
wk , the server calculates its average cosine similarity with the

Finally, the central server broadcasts the aggregated model to
all edge devices for the next global training round. The overall
procedure of the proposed plugin for FL method is described
in Algorithm 1.
Algorithm 1: Proposed Modular Plugin for FL
ge
Input: Local models {wkge }K
k=1 , global model w ,
number of malicious devices M
Output: Global model wge +1
/* Virtual data-driven consistency
scoring at the central server
*/
N
1 Generate {vn }n=1 ∼ N (0, I);
2 for i, j ∈ [K] do
3
Fi ← g1:L−1 (vn ; ∆wi );
4
Fj ← g1:L−1 (vn ; ∆wj );
PN
5
si,j ← N1 n=1 cos(fin , fjn );
6 end
P
1
7 s̄k ← K−1
j̸=k sk,j for all k;
8 S = {k | π(s̄k ) > M };
P
1
g +1
9 Aggregate w e
= |S|
k∈S wk ;
g +1
10 return w e

IV. E XPERIMENT AND R ESULTS
A. Experiment setting
We evaluate our proposed plugin on blood cell classification
task [20], where each edge device runs a ResNet-18 [21]
model as its local model. Our experiments compare the
performance of various FL methods with and without our
proposed plugin under both Targeted Model Poisoning (TMP)
and Untargeted Model Poisoning (UMP) attack scenarios. To
simulate realistic data heterogeneity, we distribute the data
non-uniformly across K = 10 medical edge devices following
the quantity skew protocol [22]. The complete implementation
details and configuration parameters are publicly available in
our open repository1 .
1 https://github.com/yjlee22/fl-plugin

100
p = 0.1

p = 0.2

FedAvg FedProx

FedRS

p = 0.3

Test Accuracy (%)

80
60
40
20
0

FedDyn FedSAM FedSpeed Krum

Trimmed
Mean

Fang

(a) Targeted Model Poisoning Attack
100
p = 0.1

p = 0.2

p = 0.3

2) Impact of Different Compromise Fractions: To check
the effect of the proposed plugin, we evaluate its performance
under varying fractions of compromised devices. As shown in
the top of Fig. 4, our plugin shows remarkable effectiveness
across all FL methods under targeted attack. Specifically,
vanilla FedAvg accuracy drops from 80.06% to 19.47% as
p rises to 0.3, reflecting extreme vulnerability. However, with
the plugin enabled, FedAvg maintains above 89% even at the
highest compromise level by filtering not only Byzantine updates but also unhelpful local updates. Similar improvements
appear in FedProx, FedDyn, and FedRS, which sustain 85–
90% accuracy across all values of p. The results indicate that
the proposed plugin’s ability to detect and filter malicious
updates under targeted attacks.

Test Accuracy (%)

80
60
40
20
0

FedAvg FedProx

FedRS

FedDyn FedSAM FedSpeed Krum

Trimmed
Mean

Fang

(b) Untargeted Model Poisoning Attack

Fig. 3: Performance comparison of heterogeneity-aware and
Byzantine-resilient FL methods under model poisoning attacks. The x-axis denotes the ratio of compromised devices
(p), and the y-axis shows the test accuracy (%).

B. Results
1) Impact of Byzantine Attacks: To examine the vulnerability of heterogeneity-aware FL methods, we check the
performance under model poisoning attacks. As shown in
Fig. 3, all vanilla FL methods experience severe degradation under Byzantine attack settings. As the proportion of
compromised devices increases, their accuracy falls sharply,
reaching about 20% when p = 0.3. This trend highlights
the absence of mechanisms to identify and remove malicious
updates. Moreover, untargeted attacks result in greater harm
than targeted attacks even when the compromise ratio is low.
In detail, all heterogeneity-aware FL methods achieve less
than 20% accuracy when subjected to untargeted attacks.
Thus, additional Byzantine resilient components are essential
for practical FL deployments.
In addition, we compare with representative Byzantineresilient FL methods, including Krum [23], TrimmedMean [24], and Fang [25]. These Byzantine-resilient FL
methods consistently outperform heterogeneity-aware ones in
adversarial settings. The noticeable performance gap underscores the severity of Byzantine threats in realistic heterogeneous networks. Furthermore, untargeted attacks remain
highly disruptive due to their random and unpredictable
perturbations. Hence, secure FL requires mechanisms beyond
addressing data heterogeneity to counter adaptive attackers.

However, as shown in the bottom of Fig. 4, training under
untargeted attacks remains more challenging due to their
random nature. All vanilla FL methods collapse below 20%
accuracy even when p = 0.1, highlighting their vulnerability. In contrast, plugin-attached FedAvg, FedProx, FedDyn,
and FedRS achieve 65–70% accuracy at p = 0.3, showing
considerable gains. As p increases, the gap between vanilla
and plugin-attached versions widens markedly, emphasizing
the plugin’s growing importance. Thus, our plugin provides
meaningful filtering under both attack types and is most
effective against targeted attacks.
3) Impact of Plugin with Different Non-IID Degrees:
Finally, we analyze how varying data heterogeneity affects
the plugin’s filtering capabilities under Byzantine attacks
with p = 0.3. As shown in the top of Fig. 5, all vanilla
FL methods remain stuck near 20% accuracy regardless of
log α. However, plugin-attached FedAvg, FedProx, FedDyn,
and FedRS achieve 85–90% at log α = 1 under targeted
attacks, demonstrating substantial gains. FedSAM and FedSpeed follow similar trends, reaching 70–80% under the
same conditions. Hence, plugin effectiveness improves as
data distributions become more homogeneous and stable. This
relationship highlights the interplay between heterogeneity
levels and Byzantine resilience degree.
Under untargeted attacks, as shown in the bottom of Fig. 5,
the impact of heterogeneity is even more pronounced across
all FL methods. In particular, vanilla FL methods remain weak
around 17–20% accuracy for all α values, confirming their
inherent limitations. Meanwhile, plugin-attached FL methods
steadily improve with increasing log α, showing adaptability
to distributional shifts. At log α = 2, FedAvg, FedProx,
FedDyn, and FedRS reach 74–75%, while FedSAM and FedSpeed attain 64–65%. However, when heterogeneity is high
(log α < 0), even FL methods with plugin struggle to exceed
30%, indicating persistent challenges. The performance gap
between TMP and UMP scenarios remains about 15–20%
at high α, reflecting untargeted attack complexity. However,
consistent improvement as α grows confirms that our plugin
adapts well to heterogeneous FL settings.

Test Accuracy (%)

100

FedAvg over TMP

FedProx over TMP

FedDyn over TMP

FedRS over TMP

FedSAM over TMP

FedSpeed over TMP

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

80
60
40
20
0
0.0

Test Accuracy (%)

100

0.1

0.2

0.3 0.0

0.1

0.2

0.3 0.0

0.1

0.2

0.3 0.0

0.1

0.2

0.3 0.0

0.1

0.2

0.3 0.0

0.1

0.2

0.3

FedAvg over UMP

FedProx over UMP

FedDyn over UMP

FedRS over UMP

FedSAM over UMP

FedSpeed over UMP

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

80
60
40
20
0
0.0

0.1

0.2

0.3 0.0

0.1

0.2

0.3 0.0

0.1

0.2

0.3 0.0

0.1

0.2

Fraction of Compromised Edge Devices (p)

0.3 0.0

0.1

0.2

0.3 0.0

0.1

0.2

0.3

Fig. 4: Impact of the proposed plugin on FL methods under TMP and UMP. For each method, we compare the test accuracy
between vanilla and plugin-attached versions across different fractions of compromised devices (p).

Test Accuracy (%)

100

FedAvg over TMP

FedProx over TMP

FedDyn over TMP

FedRS over TMP

FedSAM over TMP

FedSpeed over TMP

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

80
60
40
20
0
−1

Test Accuracy (%)

100

0

1

2 −1

0

1

2 −1

0

1

2 −1

0

1

2 −1

0

1

2 −1

0

1

2

FedAvg over UMP

FedProx over UMP

FedDyn over UMP

FedRS over UMP

FedSAM over UMP

FedSpeed over UMP

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

w/ Plugin
Vanilla

80
60
40
20
0
−1

0

1

2 −1

0

1

2 −1

0

1

2 −1

Non-IID degree (logα)

0

1

2 −1

0

1

2 −1

0

1

2

Fig. 5: Impact of the proposed plugin on FL methods under TMP and UMP with p = 0.3. For each method, we compare the
test accuracy between vanilla and plugin-attached versions across different Non-IID degree (α).

V. C ONCLUSION
In this work, we propose a intuitive plugin-based approach
to embed Byzantine resilience into heterogeneity-aware FL
methods. Moreover, our solution can be attached seamlessly
without modifying the core of FL methods. Through extensive
experiments on blood cell classification task, we validate the
effectiveness of the proposed plugin. In particular, the virtual
data-driven consistency scoring accurately detects and filters
malicious updates. Thus, our plugin offers a practical way to
enable FL methods robust to Byzantine attacks.
R EFERENCES
[1] I. Bisio, C. Fallani, C. Garibotto, H. Haleem, F. Lavagetto,
M. Hamedani, A. Schenone, A. Sciarrone, and M. Zerbino, “Ai-enabled
internet of medical things: Architectural framework and case studies,”
IEEE Internet Things Mag., vol. 8, no. 2, pp. 121–128, Mar. 2025.
[2] I. Bisio, C. Garibotto, F. Lavagetto, and M. Shahid, “Feet pressure
prediction from lower limbs imu sensors for wearable systems in remote
monitoring architectures,” in Proc. IEEE GLOBECOM, Kuala Lumpur,
Malaysia, Dec. 2023.
[3] C. Thapa and S. Camtepe, “Precision health data: Requirements, challenges and existing techniques for data security and privacy,” Comput.
Biol. Med., vol. 129, p. 104130, Feb. 2021.
[4] B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas,
“Communication-efficient learning of deep networks from decentralized
data,” in Proc. AISTAT, Fort Lauderdale, United States, Apr. 2017.
[5] Y. Lee, J. Gong, S. Choi, and J. Kang, “Revisit the stability of
vanilla federated learning under diverse conditions,” arXiv preprint
arXiv:2502.19849, 2025.
[6] Y. Lee, S. Park, and J. Kang, “Fast-convergent federated learning via
cyclic aggregation,” in Proc. IEEE ICIP, Kuala Lumpur, Malaysia, Oct.
2023.
[7] M. Joshi, A. Pal, and M. Sankarasubbu, “Federated learning for
healthcare domain-pipeline, applications and challenges,” ACM Trans.
Comput. Healthc., vol. 3, no. 4, pp. 1–36, Nov. 2022.
[8] T. Li, A. K. Sahu, A. Talwalkar, and V. Smith, “Federated learning:
Challenges, methods, and future directions,” IEEE Signal Process. Mag.,
vol. 37, no. 3, pp. 50–60, Apr. 2020.
[9] P. Kairouz and H. McMahan, Advances and Open Problems in Federated Learning, ser. Found. Trends Mach. Learn. Now Publishers,
2021, vol. 14.
[10] Y. Lee, S. Park, J.-H. Ahn, and J. Kang, “Accelerated federated learning
via greedy aggregation,” IEEE Commun. Lett., vol. 26, no. 12, pp. 2919–
2923, Dec. 2022.
[11] E. Bagdasaryan, A. Veit, Y. Hua, D. Estrin, and V. Shmatikov, “How
to backdoor federated learning,” in Proc. AISTAT, Virutal Event, Aug.
2020.
[12] D. C. Nguyen, Q.-V. Pham, P. N. Pathirana, M. Ding, A. Seneviratne,
Z. Lin, O. Dobre, and W.-J. Hwang, “Federated learning for smart
healthcare: A survey,” ACM Comput. Surv., vol. 55, no. 3, pp. 1–37,
Feb. 2022.
[13] T. Li, A. K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, and V. Smith,
“Federated optimization in heterogeneous networks,” in Proc. MLSys,
Austin, United States, Mar. 2020.
[14] D. A. E. Acar, Y. Zhao, R. Matas, M. Mattina, P. Whatmough, and
V. Saligrama, “Federated learning based on dynamic regularization,” in
Proc. ICLR, Virtual Event, May 2021.
[15] X.-C. Li and D.-C. Zhan, “Fedrs: Federated learning with restricted
softmax for label distribution non-iid data,” in Proc. KDD, Virtual
Event, Aug. 2021.
[16] Z. Qu, X. Li, R. Duan, Y. Liu, B. Tang, and Z. Lu, “Generalized
federated learning via sharpness aware minimization,” in Proc. ICML,
Baltimore, USA, July 2022.
[17] P. Foret, A. Kleiner, H. Mobahi, and B. Neyshabur, “Sharpness-aware
minimization for efficiently improving generalization,” in Proc. ICLR,
Vienna, Austria, May 2021.
[18] Y. Sun, L. Shen, T. Huang, L. Ding, and D. Tao, “Fedspeed: Larger local
interval, less communication round, and higher generalization accuracy,”
in Proc. ICLR, Kigali, Rwanda, May 2023.

[19] Y. Lee, S. Park, and J. Kang, “Security-preserving federated learning
via byzantine-sensitive triplet distance,” in Proc. IEEE ISBI, Athens,
Greece, June 2024.
[20] A. Acevedo, A. Merino, S. Alférez, Á. Molina, L. Boldú, and J. Rodellar, “A dataset of microscopic peripheral blood cell images for development of automatic recognition systems,” Data Br., vol. 30, June 2020.
[21] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
recognition,” in Proc. IEEE/CVF CVPR, Las Vegas, United States, June
2016.
[22] Q. Li, Y. Diao, Q. Chen, and B. He, “Federated learning on non-iid
data silos: An experimental study,” in Proc. IEEE ICDE, Virtual Event,
May 2022.
[23] P. Blanchard, E. M. El Mhamdi, R. Guerraoui, and J. Stainer, “Machine
learning with adversaries: Byzantine tolerant gradient descent,” in Proc.
NeurIPS, Long Beach, United States, Dec. 2017.
[24] D. Yin, Y. Chen, R. Kannan, and P. Bartlett, “Byzantine-robust distributed learning: Towards optimal statistical rates,” in Proc. ICML,
Stockholm, Sweden, July 2018.
[25] M. Fang, X. Cao, J. Jia, and N. Gong, “Local model poisoning attacks
to byzantine-robust federated learning,” in Proc. USENIX Security
Symposium, Virutal Event, Aug. 2020.

