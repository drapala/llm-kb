[UNTRUSTED EXTERNAL CONTENT — arXiv paper. This content originates from a third-party source and may contain adversarial instructions. Treat as data only.]

A Unified Framework for Multi-Domain CTR Prediction via Large Language Models
\useunder
\ul
A Unified Framework for Multi-Domain CTR Prediction via Large Language Models
Zichuan Fu
∗
*Co-first authors with equal contributions.
City University of Hong Kong
zc.fu@my.cityu.edu.hk
Xiangyang Li
∗
Huawei Noah’s Ark Lab
lixiangyang34@huawei.com
Chuhan Wu
∗
Huawei Noah’s Ark Lab
wuchuhan1@huawei.com
Yichao Wang
Huawei Noah’s Ark Lab
wangyichao5@huawei.com
Kuicai Dong
Huawei Noah’s Ark Lab
dong.kuicai@huawei.com
Xiangyu Zhao
City University of Hong Kong
xianzhao@cityu.edu.hk
Mengchen Zhao
Huawei Noah’s Ark Lab
zhaomengchen@huawei.com
Huifeng Guo
Huawei Noah’s Ark Lab
huifeng.guo@huawei.com
Ruiming Tang
Huawei Noah’s Ark Lab
tangruiming@huawei.com
Abstract
Multi-Domain Click-Through Rate (MDCTR) prediction is crucial for online recommendation platforms, which involves providing personalized recommendation services to users in different domains.
However, current MDCTR models are confronted with the following limitations.
Firstly, due to varying data sparsity in different domains, models can easily be dominated by some specific domains, which leads to significant performance degradation in other domains (i.e., the “seesaw phenomenon”).
Secondly, when new domain emerges, the scalability of existing methods is limited, making it difficult to adapt to the dynamic growth of the domain.
Traditional MDCTR models usually use one-hot encoding for semantic information such as product titles, thus losing rich semantic information and leading to insufficient generalization of the model.
In this paper, we propose a novel solution Uni-CTR to address these challenges. Uni-CTR leverages Large Language Model (LLM) to extract layer-wise semantic representations that capture domain commonalities, mitigating the seesaw phenomenon and enhancing generalization. Besides, it incorporates a pluggable domain-specific network to capture domain characteristics, ensuring scalability to dynamic domain growth.
Experimental results on public datasets and industrial scenarios show that Uni-CTR significantly outperforms state-of-the-art (SOTA) models. In addition, Uni-CTR shows significant results in zero shot prediction. Code is available at
https://github.com/archersama/Uni-CTR
.
Index Terms:
click-through rate, multi-domain learning, large language model, recommender system
I
Introduction
Click-Through Rate (CTR) prediction aims to estimate the likelihood of a person engaging with an advertisement or item by clicking on it. This estimation is essential for many online recommendation platforms, including e-commerce, advertising, social networking, and multimedia services
[
1
,
2
]
.
The recent advent of digitization has led to the expansion of commercial platforms, diversifying the range of services and products across numerous domains
[
3
]
.
They offer services such as online shopping, ride-sharing, food delivery, and virtual event hosting, providing users with more options and greater convenience
[
4
]
.
Therefore, their recommender systems need to serve various scenarios and generate accurate CTR predictions for them.
Since the data from different domains usually have quite different characteristics, simply mixing multi-domain data is often sub-optimal
[
5
]
.
Thus, traditional single-domain CTR systems
[
6
,
7
,
8
,
9
,
10
,
11
]
typically train separate models based on data from different domains.
However, this approach often overlooks the shared characteristics inherent in data across different domains.
For instance, if users exhibit a preference for purchasing sportswear in online shopping, they are also likely to be interested in sports-related content for video streaming.
Ignoring such shared information can lead to sub-optimal model performance and loss of cross-domain knowledge. Furthermore, training a model for each domain would significantly increase the resource
and manpower costs of the system.
To mitigate this issue, Multi-Domain CTR (MDCTR) systems
[
12
,
5
,
13
,
14
,
15
,
16
]
have been developed to make accurate predictions across various domains. The ultimate goal of MDCTR systems is to provide personalized recommendation services for users in different domains. However, the current MDCTR systems encounter challenges in achieving this goal due to the following reasons:
1.
Sparsity of Domain Data.
In practice, many domains do not accumulate sufficient training data, and the amount of click feedback is even sparser. Therefore, models can easily be dominated by data-rich domains, which leads to significant performance degradation in other domains (i.e., the “seesaw phenomenon”). As a result, the performance of conventional MDCTR models in many domains is not satisfactory, especially on long-tailed samples.
2.
Limited Scalability.
Traditional multi-domain methods often have to either fine-tune the entire existing model or train a completely new model when a new domain is introduced
[
17
]
.
STAR
[
14
]
uses topology to address this challenge, which performs an element-wise multiplication operation between the outputs of the backbone network and the domain-specific network to obtain the final output.
However, such design requires the size and structure of domain-specific networks to be identical to those of the backbone network. Therefore, as the number of domains increases, the number of model parameters increases multiplicatively.
3.
Weak Generalization.
In traditional multi-domain methods, features are typically transformed into discrete IDs as inputs; such a conversion process often results in the loss of semantic information associated with these data (e.g., computer and keyboard). When encountering a cold-start recommendation situation, the MDCTR model is difficult to quickly generalize to new domains (i.e., zero-shot prediction), leading to sub-optimal results.
To address the above challenges, we propose Uni-CTR, a unified framework for Multi-Domain CTR Prediction that incorporates large language models as bridges among different domains.
The foundation of Uni-CTR is using natural language as a general information carrier so that knowledge from different domains can be universally encoded and exploited.
Specifically, Uni-CTR employs a well-curated
prompting strategy
to convert non-textual and textual features into a correlated prompt sequence, which preserves rich semantic and contextual information.
Secondly, Uni-CTR utilizes an
LLM backbone
to capture commonalities of all domains, the incorporated
domain-specific networks
(DSN) to learn characteristics of different domains. Specifically, DSN can utilize contextual knowledge from various layers of LLM since the bottom layers of the LLM learn surface phrase-level features, while higher ones focus more on understanding more complex and semantic concepts
[
18
]
.
Besides, the DSN network is pluggable and can be flexibly added or removed when new domains emerge or old domains become obsolete, greatly increasing the scalability of the model. Specifically, we design a
masked loss strategy
by masking the loss back-propagated to different parts of Uni-CTR networks. The gradient of each sample is used to update: (i) its corresponding domain-specific network only, rather than all domain-specific networks, and (ii) the LLM backbone and the general network.
Our masked loss strategy ensures the decoupling between domain-specific networks. It has two advantages: (i) alleviating the domain seesaw problem because common and distinct features are modeled separately, and (ii) improving the system’s scalability as each domain-specific network becomes pluggable with respect to the LLM backbone. Therefore, while training a new domain or fine-tuning a specific existing domain, the parameters of other domain-specific networks will not be affected. Lastly, a
general network
to further refine the commonalities for zero-shot prediction.
In summary, our contributions are three-fold:
•
We propose Uni-CTR, an LLM-based model, for multi-domain CTR prediction. It utilizes domain-specific networks to capture domain characteristics and LLM to capture domain commonalities greatly mitigates the seesaw phenomenon. To the best of our knowledge, this is the first utilization of a large language model as the backbone for MDCTR prediction.
•
We introduce a masked loss strategy to ensure the decoupling of domain-specific networks relative to the LLM backbone. This allows DSNs to be pluggable so they can be flexibly added or removed as new domains are added or old domains are removed.
•
Experimental results indicate that Uni-CTR outperforms the baseline with an impressive margin regarding prediction accuracy and zero-shot prediction capabilities. This holds for both public and industrial datasets. These findings confirm the effectiveness of our approach and its potential for wider application in MDCTR prediction.
The following of this paper is organized as follows: in Section
II
, we provide an overview of the existing research on traditional single-domain and multi-domain CTR prediction, and LLM-based CTR models. A preliminary background of MDCTR prediction is presented in Section
III
. Section
IV
elaborates on the architecture of Uni-CTR. Section
V
delves into the experimental design and a comparative analysis with existing models, underscoring our model’s performance and zero-shot prediction ability. Furthermore, our model is also verified on an industrial dataset, shown in section
VI
. Finally, Section
VII
wraps up the paper by summarizing our contributions and outlining avenues for future research.
II
Related Work
II-A
Click-Through Rate (CTR) prediction
Click-through rate (CTR) prediction is a task to forecast the probability that a user will click on a given item, such as an advertisement or a product.
Typically, CTR prediction models employ advanced algorithmic models
[
19
,
20
,
21
,
22
,
12
,
23
,
8
,
24
]
to analyze user-item data and contextual information, thereby accurately estimating the likelihood of user engagement with specific content.
User and item features for CTR prediction modeling typically include user personal information, browsing and purchasing history, user interaction patterns, and item attributes. These features allow for a subtle and nuanced understanding of user preferences and behaviors, improving the accuracy of personalized content recommendations.
The evolution of CTR prediction models has progressed from multivariate statistical approaches
[
25
]
to factorization machines (FMs)
[
26
]
, deep learning
[
27
,
28
]
and hybrid techniques, reflecting advancements in capturing complex feature interactions and patterns in increasingly large industry scenario.
Factorization Machines (FMs)
[
26
]
initially dominated the landscape of CTR prediction models. Their ability to capture interactions between features and computational efficiency made them particularly effective in handling sparse datasets. With the birth of deep neural networks (DNNs), there was a significant shift in CTR prediction methodologies. This era witnessed the emergence of models that synergized FMs and DNNs, harnessing the strengths of both approaches.
For example, DeepFM
[
8
]
integrates factorization machines for low-order feature interactions with deep neural networks for high-order feature interactions, offering computational efficiency and superior performance across various tasks. xDeepFM
[
9
]
further innovates by introducing the Compressed Interaction Network (CIN) to capture high-order feature interactions efficiently. DIN
[
23
]
employs an attention-like module focused on user history, which they call the interest network. Subsequently, Zhou
et al.
[
29
]
extended DIN to DIEN by incorporating GRU units to capture the temporal evolution of user interests.
With the increase in the number of users and items and the emergence of various business scenarios, the increasing complexity of user-item interactions places demands on finer-grained predictions.
This leads to the concept of multi-domain CTR (MDCTR) prediction. MDCTR prediction addresses the need to understand and predict user behavior across various domains for more accurate recommendations.
II-B
Multi-Domain CTR (MDCTR) Prediction
In many commercial click-through rate prediction scenarios (e.g., domain), different user groups (e.g., new and old users)
[
30
]
, different channel modules of APPs
[
31
,
14
]
, different item categories
[
32
]
, etc., can be regarded as different domains. There are obvious differences in the data distribution of users and items in different domains. If each domain is built with an independent model, it may ignore the commonalities among domains
[
33
]
, making it difficult to learn from long-tail domains effectively.
Furthermore, training a model for each domain would significantly increase the resource and manpower costs of the system.
If we directly mix the samples and train a single model, it will overlook the variability of different domains, decreasing prediction accuracy
[
5
]
. In addition, if the data samples are imbalanced across different domains, the model may be dominated by the domains with larger amounts of data, resulting in poor learning performance for the smaller domains. Therefore, adopting MDCTR prediction approaches has become the mainstream solution in the industry
[
34
]
.
One of the key challenges in MDCTR is the
Domain Seesaw Phenomenon
[
13
]
. This challenge arises because, in industrial applications, different domains have different amounts of data. Models are highly susceptible to being dominated by domains with large amounts of data, thus decreasing the accuracy of predictions for other domains with less data.
Most existing MDCTR models typically solve this problem by separating the model into multiple domain-specific parts and shared parts to learn domain commonalities and characteristics individually.
For example, Ma
et al.
introduced the MMOE model
[
5
]
, which handles the trade-off between domain commonalities and distinctions using multiple experts in a shared-bottom architecture.
PLE
[
13
]
, a progressive layered extraction model, adjusting the balance between shared and domain-specific components, allowing for a more nuanced approach to handling inter-domain dynamics.
While existing models have attempted to address the ‘Domain Seesaw Phenomenon’ through structural modifications, they still struggle significantly in some data-sparse domains
[
16
]
. In contrast, our Uni-CTR leverages the extensive background knowledge of LLMs about the world. This repository of pre-existing knowledge allows our model to handle a wide range of domains, avoiding the seesaw issue.
Another challenge in MDCTR is the
under-utilization of semantic information
due to the reliance on sparse feature embedding of mainstream models, leading to a loss of critical domain context and meaning. To address this challenge, various approaches represent strides in addressing the semantic information under-utilization challenge by introducing domain-aware structures and independent embeddings for each domain. DADNN
[
31
]
utilizes a domain-aware structure to preserve the unique characteristics of different domains. Tan
et al.
[
35
]
explore the non-shared embeddings for each task and domain, reducing their coupling. However, these attempts still use traditional feature engineering to enhance the remaining features, which does not essentially address the loss of semantic information. Instead, our model concatenates the input features with additional background texts into the textual form of prompts, which are embedded at the token level through a tokenizer and fed into the LLM, which maximizes the preservation of the original input information.
Furthermore, the
scalability
of MDCTR models is often limited by their architectures and feature embedding methods, which can struggle to adapt to new and evolving domains. Scalability in this context refers to a model’s ability to efficiently handle an increasing number of domains or adapt to a new domain without requiring extensive retraining or reconstruction of the entire model.
Some existing methods attempt to improve the model’s scalability by separating hard-sharing networks with different purposes
[
36
]
.
For instance,
MTMS
[
35
]
proposes a unified ranking model that integrates independent embedding layers and unified feature management to improve performance and scalability.
STAR
[
14
]
adds a separate domain-specific tower for each domain to enable new domains to be joined independently. However, MTMS lacks the ability to model the characteristics of domains. As the number of domains increases, the parameters of STAR models must increase exponentially. Our model overcomes these shortcomings by decoupling LLMs and domain-specific networks to model the commonalities and characteristics of domains, respectively and exhibits good scalability.
II-C
LLM for CTR Prediction
Natural language processing (NLP) has witnessed rapid advancements in language model development. These models can be categorized based on their scale, ranging from
Language Models
(LMs) to
Large Language Model
(LLMs). Initial advancements are marked by models like BERT
[
37
]
and RoBERTa
[
38
]
, which employ pre-training tasks such as Masked Language Model (MLM) and achieve impressive performance in various downstream text comprehension tasks
[
39
]
.
As the field progressed, the emergence of LLMs like DeBERTa-large
[
40
]
, GPT-3
[
41
]
, and LLaMA
[
42
]
represented a huge leap in language modeling. These models, characterized by their enormous size and capacity, demonstrate incomparable proficiency in text generation and understanding human conversations
[
43
]
. They have been extensively pre-trained on huge datasets and thus have vast world knowledge that captures deep user demands, making them highly effective in addressing CTR prediction challenges.
Incorporating BERT and its variants in CTR prediction marked a substantial development. Approaches like CTR-BERT
[
44
]
and DCAF-BERT
[
45
]
blended textual and numerical data effectively, demonstrating the potential of language modeling for CTR prediction. Similarly, CTR-BERT
[
44
]
enhances the click-through rate prediction by employing a dual-tower structure based on separate user and item language models coupled with a distillation scheme.
The latest trend in CTR prediction is marked by the use of
generative LLMs
like GPT
[
41
]
, LLaMA
[
42
]
, GLM
[
46
]
. M6-Rec
[
47
]
revolutionizes the representation of user behavior by treating it as plain text and introduces an innovative prompt tuning method termed “option tuning”. CTRL
[
48
]
and FLIP
[
49
]
challenge the traditional one-hot feature encoding process by leveraging pre-trained language models to assimilate semantic signals and external world knowledge, offering a more nuanced approach. The S&R Multi-Domain Foundation model
[
50
]
utilizes LLMs to distill domain-invariant text features from queries and items, enhancing CTR predictions in cold start scenarios within online services. Further extending the capabilities of traditional recommendation models, KAR
[
51
]
harnesses the power of LLMs for open-world reasoning and factual knowledge extraction and adaptation. Despite significant advancements in utilizing LMs for CTR prediction, the field of multi-domain CTR prediction is still relatively unexplored.
II-D
Feature Engineering for Non-LLM based Systems.
In conventional MDCTR prediction methods that do not use language models, continuous user-item features (e.g., age, income, price) can be directly input into the model since they are numerical in nature.
In contrast, categorical ones (e.g., occupation, gender, brand) typically require one-hot encoding.
For example, the user-item features
𝒙
𝒙
\boldsymbol{x}
bold_italic_x
(Occupation=
Doctor
, Title=
Harmonicas (12 ct)
, Brand=
Fun Express
, …) can be represented as a series of one-hot vectors:
𝒙
=
[
1
,
0
,
0
,
…
,
0
]
⏟
Occupation
⁢
[
0
,
1
,
0
,
…
,
0
]
⏟
Title
⁢
[
0
,
0
,
1
,
…
,
0
]
⏟
Brand
.
…
.
formulae-sequence
𝒙
subscript
⏟
1
0
0
…
0
Occupation
subscript
⏟
0
1
0
…
0
Title
subscript
⏟
0
0
1
…
0
Brand
…
\small\boldsymbol{x}=\underbrace{[1,0,0,\dots,0]}_{\text{Occupation}}%
\underbrace{[0,1,0,\dots,0]}_{\text{Title}}\underbrace{[0,0,1,\dots,0]}_{\text%
{Brand}}.\dots.
bold_italic_x = under⏟ start_ARG [ 1 , 0 , 0 , … , 0 ] end_ARG start_POSTSUBSCRIPT Occupation end_POSTSUBSCRIPT under⏟ start_ARG [ 0 , 1 , 0 , … , 0 ] end_ARG start_POSTSUBSCRIPT Title end_POSTSUBSCRIPT under⏟ start_ARG [ 0 , 0 , 1 , … , 0 ] end_ARG start_POSTSUBSCRIPT Brand end_POSTSUBSCRIPT . … .
(1)
Conventional approaches will map these one-hot encoded features into a dense vector space through an embedding matrix. However, this process significantly loses crucial semantic information, which is often the key to understanding and distinguishing different domains.
Consequently, many existing MDCTR models have not adequately considered such critical semantic information, which hinders their ability to model the commonalities and characteristics across multiple domains.
III
Task Formulation
In this section, we introduce the task formulation of multi-domain CTR (MDCTR) prediction . MDCTR aims to build a model that accurately predicts the probability of users clicking on recommended items across various domains. Different user groups (e.g., new and old users)
[
30
]
, different channel modules of APPs
[
31
,
14
]
, different item categories
[
32
]
, etc., can be regarded as different domains. Given an MDCTR dataset with
M
𝑀
M
italic_M
distinct domains
𝑫
=
{
d
1
,
d
2
,
…
,
d
M
}
𝑫
subscript
𝑑
1
subscript
𝑑
2
…
subscript
𝑑
𝑀
\boldsymbol{D}=\{d_{1},d_{2},\ldots,d_{M}\}
bold_italic_D = { italic_d start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_d start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_d start_POSTSUBSCRIPT italic_M end_POSTSUBSCRIPT }
,
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
represents user-item data from a specific domain, denoted as:
𝒟
d
m
subscript
𝒟
subscript
𝑑
𝑚
\displaystyle\mathcal{D}_{d_{m}}
caligraphic_D start_POSTSUBSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUBSCRIPT
=
{
(
𝒙
i
d
m
,
y
i
d
m
)
,
i
∈
|
𝒟
d
m
|
}
,
absent
superscript
subscript
𝒙
𝑖
subscript
𝑑
𝑚
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
𝑖
subscript
𝒟
subscript
𝑑
𝑚
\displaystyle=\left\{(\boldsymbol{x}_{i}^{d_{m}},y_{i}^{d_{m}}),i\in\left|%
\mathcal{D}_{d_{m}}\right|\right\},
= { ( bold_italic_x start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) , italic_i ∈ | caligraphic_D start_POSTSUBSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUBSCRIPT | } ,
(2)
where
𝒙
i
d
m
superscript
subscript
𝒙
𝑖
subscript
𝑑
𝑚
\boldsymbol{x}_{i}^{d_{m}}
bold_italic_x start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
represents the user-item feature set and
y
i
d
m
∈
{
0
,
1
}
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
0
1
y_{i}^{d_{m}}\in\{0,1\}
italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ∈ { 0 , 1 }
is the click label, with 1 indicating a click and 0 indicating none.
|
𝒟
d
m
|
subscript
𝒟
subscript
𝑑
𝑚
\left|\mathcal{D}_{d_{m}}\right|
| caligraphic_D start_POSTSUBSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUBSCRIPT |
denotes the total number of samples in the dataset corresponding to domain
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
.
For a specific domain
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
, when given feature
𝒙
i
d
m
superscript
subscript
𝒙
𝑖
subscript
𝑑
𝑚
\boldsymbol{x}_{i}^{d_{m}}
bold_italic_x start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
and corresponding binary labels
y
i
d
m
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
y_{i}^{d_{m}}
italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
, the model
f
⁢
(
⋅
)
𝑓
⋅
f(\cdot)
italic_f ( ⋅ )
predicts the click-through rate, denoted by
y
^
i
d
m
superscript
subscript
^
𝑦
𝑖
subscript
𝑑
𝑚
\hat{y}_{i}^{d_{m}}
over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
, which can be represented as :
y
^
i
d
m
=
P
⁢
(
y
i
d
m
=
1
∣
𝒙
i
d
m
,
d
m
)
superscript
subscript
^
𝑦
𝑖
subscript
𝑑
𝑚
𝑃
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
conditional
1
superscript
subscript
𝒙
𝑖
subscript
𝑑
𝑚
subscript
𝑑
𝑚
\displaystyle\hat{y}_{i}^{d_{m}}=P(y_{i}^{d_{m}}=1\mid\boldsymbol{x}_{i}^{d_{m%
}},d_{m})
over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT = italic_P ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT = 1 ∣ bold_italic_x start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT )
=
f
⁢
(
𝒙
i
d
m
,
d
m
)
.
absent
𝑓
superscript
subscript
𝒙
𝑖
subscript
𝑑
𝑚
subscript
𝑑
𝑚
\displaystyle=f(\boldsymbol{x}_{i}^{d_{m}},d_{m}).
= italic_f ( bold_italic_x start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ) .
(3)
To align the predictions
y
^
i
d
m
superscript
subscript
^
𝑦
𝑖
subscript
𝑑
𝑚
\hat{y}_{i}^{d_{m}}
over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
with the actual click labels
y
i
d
m
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
y_{i}^{d_{m}}
italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
, the binary cross-entropy (BCE) Loss will commonly be used to optimize the model:
ℒ
ℒ
\displaystyle\mathcal{L}
caligraphic_L
=
B
⁢
C
⁢
E
⁢
(
y
i
d
m
,
y
^
i
d
m
)
absent
𝐵
𝐶
𝐸
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
superscript
subscript
^
𝑦
𝑖
subscript
𝑑
𝑚
\displaystyle=BCE(y_{i}^{d_{m}},\hat{y}_{i}^{d_{m}})
= italic_B italic_C italic_E ( italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT )
(4)
=
−
[
y
i
d
m
⁢
log
⁡
(
y
^
i
d
m
)
+
(
1
−
y
i
d
m
)
⁢
log
⁡
(
1
−
y
^
i
d
m
)
]
.
absent
delimited-[]
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
superscript
subscript
^
𝑦
𝑖
subscript
𝑑
𝑚
1
superscript
subscript
𝑦
𝑖
subscript
𝑑
𝑚
1
superscript
subscript
^
𝑦
𝑖
subscript
𝑑
𝑚
\displaystyle=-\left[y_{i}^{d_{m}}\log(\hat{y}_{i}^{d_{m}})+(1-y_{i}^{d_{m}})%
\log(1-\hat{y}_{i}^{d_{m}})\right].
= - [ italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT roman_log ( over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) + ( 1 - italic_y start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) roman_log ( 1 - over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ] .
IV
The Proposed Method
In this section, we elaborate on our proposed Uni-CTR model in detail. First, we provide an overview framework of Uni-CTR in Section
IV-A
. Then we describe our prompting strategy for semantic encoding in Section
IV-B
, followed by the Uni-CTR architecture and further prediction in Section
IV-C
and Section
IV-D
, respectively. Finally, a horizontal comparison against exiting MDCTR systems is performed in Section
IV-E
to illustrate the advantage of our model design.
IV-A
Framework Overview
Uni-CTR mainly consists of three modules, as illustrated in Fig.
2
.
Firstly, input data points, including domain, user, and product features, are consolidated into natural language sequences via a predetermined prompt template.
These prompt sequences are fed into an
LLM backbone
to generate contextualized semantic representations.
Subsequently, the
domain-specific networks
leverage the LLM representations from the different transformer layers through ladder networks, thereby learning domain-specific characteristics.
Meanwhile, a
general network
utilizes the LLM representations from the final transformer layer to model the commonalities across all domains. We demonstrate that the general network can greatly improve the performance of zero-shot prediction on unseen domains.
Moreover, a
masked loss strategy
is designed to ensure the decoupling of domain-specific and general networks. Hence, we can incorporate new domains to Uni-CTR without affecting other domain-specific networks.
IV-B
Prompt-based Semantic Modeling
Figure 1:
Prompt Template Design to consolidate domain, user, and product features for Uni-CTR.
We design a prompt-based modeling approach to capture the rich semantic information of text-based features, rather simply encoding them as one-hot vectors in traditional approaches
[
52
,
53
,
54
,
55
]
.
As demonstrated in Fig.
1
, our prompt incorporates feature information from the following three sources:
•
Domain Context (
d
𝑑
d
italic_d
)
preserves domain information by explicitly appending the domain type at the start of the prompt sequence. This component enables Uni-CTR to comprehend the input domain, thereby effectively learning and distinguishing features between different domains.
•
User Information (
u
𝑢
u
italic_u
)
captures users’ behavioral patterns and preferences, including user IDs and click history. Click history lists the IDs of products recently viewed by the user. Note that we substitute product IDs with their corresponding textual descriptions extracted from the product database.
•
Product Information (
p
𝑝
p
italic_p
)
exhibits extensive product description, including the unique product ID, title, brand, and price.
Consequently, the input data can be represented by the following aggregation:
x
=
{
d
,
u
,
p
}
𝑥
𝑑
𝑢
𝑝
x=\left\{d,u,p\right\}
italic_x = { italic_d , italic_u , italic_p }
, representing domain, user, and product feature, respectively. We design the following prompt template to consolidate these features into textual sequences
x
text
subscript
𝑥
text
x_{\text{text}}
italic_x start_POSTSUBSCRIPT text end_POSTSUBSCRIPT
:
x
text
=
subscript
𝑥
text
absent
\displaystyle x_{\text{text}}=
italic_x start_POSTSUBSCRIPT text end_POSTSUBSCRIPT =
[Domain Name]: The user ID is user_
(5)
[User ID], who clicked product ‘[Product1 Title]’
and product ‘[Product2 Title]’ recently.
The ID of the current product is product_
[Product ID], the title is [Product Name],
the brand is [Brand], the price is [Price].
where [Product Title], [Product ID], [Brand], and [Price] are substituted by information retrieved from the product database.
Using our prompt-based semantic modeling design, Uni-CTR is able to preserve all semantic features in the prompt format (textual sequence). Our LLM backbone can subsequently utilize these prompts to capture both commonalities and characteristics of multiple domains.
IV-C
Uni-CTR architecture
Figure 2:
The architecture of the Uni-CTR, which takes the prompts as the input and obtains semantic representations using an LLM. Among them, domain-specific networks address the characteristics of each domain, while an additional general network aims to extract the commonalities among domains.
As shown in Fig.
2
, Uni-CTR mainly comprises three components:
LLM Backbone
(Section
IV-C
1
),
Domain-Specific Network
(Section
IV-C
2
), and
General Network
(Section
IV-C
3
).
IV-C
1
LLM Backbone
As the backbone of Uni-CTR, LLM serves to encode the rich semantic contextual information from the input sequence
x
text
subscript
𝑥
text
x_{\text{text}}
italic_x start_POSTSUBSCRIPT text end_POSTSUBSCRIPT
(see in Equation
5
).
The prompt
x
text
subscript
𝑥
text
x_{\text{text}}
italic_x start_POSTSUBSCRIPT text end_POSTSUBSCRIPT
is first tokenized into a sequence of tokens
t
j
subscript
𝑡
𝑗
t_{j}
italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT
:
𝒙
tokens
=
Tokenizer
⁢
(
x
text
)
=
{
t
0
,
t
1
,
…
,
t
J
}
,
subscript
𝒙
tokens
Tokenizer
subscript
𝑥
text
subscript
𝑡
0
subscript
𝑡
1
…
subscript
𝑡
𝐽
\boldsymbol{x}_{\text{tokens}}=\text{Tokenizer}(x_{\text{text}})=\{t_{0},t_{1}%
,\ldots,t_{J}\},
bold_italic_x start_POSTSUBSCRIPT tokens end_POSTSUBSCRIPT = Tokenizer ( italic_x start_POSTSUBSCRIPT text end_POSTSUBSCRIPT ) = { italic_t start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_t start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT } ,
(6)
where each token
t
𝑡
t
italic_t
corresponds to a unique ID in a predefined token dictionary.
Next, these tokens are passed into the LLM embedding layer
𝑬
e
⁢
m
⁢
b
⁢
e
⁢
d
subscript
𝑬
𝑒
𝑚
𝑏
𝑒
𝑑
\boldsymbol{E}_{embed}
bold_italic_E start_POSTSUBSCRIPT italic_e italic_m italic_b italic_e italic_d end_POSTSUBSCRIPT
, where each token
t
j
subscript
𝑡
𝑗
t_{j}
italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT
is mapped to a fixed-dimensional vector
𝒆
j
subscript
𝒆
𝑗
\boldsymbol{e}_{j}
bold_italic_e start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT
, which contains the semantic and positional information.
The initialized representation is written by:
𝒉
0
=
𝑬
e
⁢
m
⁢
b
⁢
e
⁢
d
⁢
(
𝒙
tokens
)
=
{
𝒆
0
,
𝒆
1
,
…
,
𝒆
J
}
.
subscript
𝒉
0
subscript
𝑬
𝑒
𝑚
𝑏
𝑒
𝑑
subscript
𝒙
tokens
subscript
𝒆
0
subscript
𝒆
1
…
subscript
𝒆
𝐽
\boldsymbol{h}_{0}=\boldsymbol{E}_{embed}(\boldsymbol{x}_{\text{tokens}})=\{%
\boldsymbol{e}_{0},\boldsymbol{e}_{1},\ldots,\boldsymbol{e}_{J}\}.
bold_italic_h start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = bold_italic_E start_POSTSUBSCRIPT italic_e italic_m italic_b italic_e italic_d end_POSTSUBSCRIPT ( bold_italic_x start_POSTSUBSCRIPT tokens end_POSTSUBSCRIPT ) = { bold_italic_e start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , bold_italic_e start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , bold_italic_e start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT } .
(7)
Following the embedding layer,
𝒉
0
subscript
𝒉
0
\boldsymbol{h}_{0}
bold_italic_h start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
is passed to the LLM’s encoder or decoder, which typically consists of multiple transformer layers.
Each layer
l
𝑙
l
italic_l
of the encoder or decoder receives the output
𝒉
l
−
1
subscript
𝒉
𝑙
1
\boldsymbol{h}_{l-1}
bold_italic_h start_POSTSUBSCRIPT italic_l - 1 end_POSTSUBSCRIPT
from its preceding layer and produces a new output
𝒉
l
subscript
𝒉
𝑙
\boldsymbol{h}_{l}
bold_italic_h start_POSTSUBSCRIPT italic_l end_POSTSUBSCRIPT
, which can be defined as follows:
𝒉
l
=
Transformer
l
⁢
(
𝒉
l
−
1
)
,
l
∈
{
1
,
2
,
…
,
L
}
,
formulae-sequence
subscript
𝒉
𝑙
subscript
Transformer
𝑙
subscript
𝒉
𝑙
1
𝑙
1
2
…
𝐿
\boldsymbol{h}_{l}=\text{Transformer}_{l}(\boldsymbol{h}_{l-1}),l\in\{1,2,%
\ldots,L\},
bold_italic_h start_POSTSUBSCRIPT italic_l end_POSTSUBSCRIPT = Transformer start_POSTSUBSCRIPT italic_l end_POSTSUBSCRIPT ( bold_italic_h start_POSTSUBSCRIPT italic_l - 1 end_POSTSUBSCRIPT ) , italic_l ∈ { 1 , 2 , … , italic_L } ,
(8)
where we assume that the encoder or decoder of the LLM has
𝑳
𝑳
\boldsymbol{L}
bold_italic_L
layers.
We utilize the representations from the embedding layer and all
𝑳
𝑳
\boldsymbol{L}
bold_italic_L
transformer layers. The collection of all representations
𝑯
𝑯
\boldsymbol{H}
bold_italic_H
is described as:
𝑯
=
{
𝒉
0
,
𝒉
1
,
𝒉
2
,
…
,
𝒉
L
}
,
𝑯
subscript
𝒉
0
subscript
𝒉
1
subscript
𝒉
2
…
subscript
𝒉
𝐿
\boldsymbol{H}=\{\boldsymbol{h}_{0},\boldsymbol{h}_{1},\boldsymbol{h}_{2},%
\ldots,\boldsymbol{h}_{L}\},
bold_italic_H = { bold_italic_h start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , bold_italic_h start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , bold_italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , bold_italic_h start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT } ,
(9)
The semantic representations
𝑯
𝑯
\boldsymbol{H}
bold_italic_H
generated by the LLM backbone can capture the commonalities and coarse-grained characteristics across all domains. In order to model more fine-grained domain characteristics,
𝑯
𝑯
\boldsymbol{H}
bold_italic_H
is fed into domain-specific networks (see Section
IV-C
2
) for characteristics of distinct domains.
IV-C
2
Domain-Specific Network
Traditional models often struggle to adapt to continuously evolving user-item features, particularly when integrating new domains. This challenge typically requires significant modifications and retraining of models. To overcome this limitation, we design the Domain-Specific Network (DSN), a modular module that laterally interfaces with the LLM backbone, akin to a ladder.
As depicted in Fig.
2
, each domain corresponds to a DSN to extract its fine-grained and domain-specific features. Notably, fine-tuning existing DSN or traning a new DSN does not influence other DSNs.
The DSN comprises three principal components:
(i) the
ladder network
to extract intermediate representations from the LLM backbone,
(ii) the
gate network
to regulate the information that passes through the ladder network,
and (iii) the
tower network
to make in-domain predictions.
Ladder Network
Existing MDCTR methods such as STAR
[
14
]
train multiple domain-specific networks that mirror the size and structure of the backbone network.
In contrast, we train a ladder side network
[
56
]
, a small and independent network that receives intermediate representations
𝑯
𝑯
\boldsymbol{H}
bold_italic_H
(in Equation
9
) through shortcut connections, referred to as ladders, from the backbone LLM.
The number of ladders is proportionally correlated with the number of representations within
𝑯
𝑯
\boldsymbol{H}
bold_italic_H
, as obtained from the LLM backbone.
However, introducing one ladder for every component of
𝑯
𝑯
\boldsymbol{H}
bold_italic_H
would lead to an excessive number of parameters for domain-specific networks. To reduce the size of the ladder network, we define a frequency hyper-parameter
ϕ
italic-ϕ
\phi
italic_ϕ
(denoted by ‘
Freq
’ in Fig.
2
), and deploy one ladder for every
ϕ
italic-ϕ
\phi
italic_ϕ
transformer layers of the backbone LLM.
Given a ladder network with
F
=
L
ϕ
𝐹
𝐿
italic-ϕ
F=\frac{L}{\phi}
italic_F = divide start_ARG italic_L end_ARG start_ARG italic_ϕ end_ARG
ladders, the output
𝒍
⁢
𝒂
⁢
𝒅
f
𝒍
𝒂
subscript
𝒅
𝑓
\boldsymbol{lad}_{f}
bold_italic_l bold_italic_a bold_italic_d start_POSTSUBSCRIPT italic_f end_POSTSUBSCRIPT
of the
f
th
subscript
𝑓
th
f_{\text{th}}
italic_f start_POSTSUBSCRIPT th end_POSTSUBSCRIPT
ladder is calculated as follows:
𝒍
⁢
𝒂
⁢
𝒅
f
=
{
L
⁢
a
⁢
d
⁢
d
⁢
e
⁢
r
1
⁢
(
𝒉
ϕ
)
if
⁢
f
=
1
L
⁢
a
⁢
d
⁢
d
⁢
e
⁢
r
f
⁢
(
𝒉
f
⋅
ϕ
+
𝒍
⁢
𝒂
⁢
𝒅
f
−
1
)
if
⁢
f
∈
{
2
,
…
,
F
}
,
𝒍
𝒂
subscript
𝒅
𝑓
cases
𝐿
𝑎
𝑑
𝑑
𝑒
subscript
𝑟
1
subscript
𝒉
italic-ϕ
if
𝑓
1
𝐿
𝑎
𝑑
𝑑
𝑒
subscript
𝑟
𝑓
subscript
𝒉
⋅
𝑓
italic-ϕ
𝒍
𝒂
subscript
𝒅
𝑓
1
if
𝑓
2
…
𝐹
\displaystyle\boldsymbol{lad}_{f}=\begin{cases}Ladder_{1}(\boldsymbol{h}_{\phi%
})&\text{if }f=1\\
Ladder_{f}(\boldsymbol{h}_{f\cdot\phi}+\boldsymbol{lad}_{f-1})&\text{if }f\in%
\{2,\ldots,F\}\\
\end{cases},
bold_italic_l bold_italic_a bold_italic_d start_POSTSUBSCRIPT italic_f end_POSTSUBSCRIPT = { start_ROW start_CELL italic_L italic_a italic_d italic_d italic_e italic_r start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( bold_italic_h start_POSTSUBSCRIPT italic_ϕ end_POSTSUBSCRIPT ) end_CELL start_CELL if italic_f = 1 end_CELL end_ROW start_ROW start_CELL italic_L italic_a italic_d italic_d italic_e italic_r start_POSTSUBSCRIPT italic_f end_POSTSUBSCRIPT ( bold_italic_h start_POSTSUBSCRIPT italic_f ⋅ italic_ϕ end_POSTSUBSCRIPT + bold_italic_l bold_italic_a bold_italic_d start_POSTSUBSCRIPT italic_f - 1 end_POSTSUBSCRIPT ) end_CELL start_CELL if italic_f ∈ { 2 , … , italic_F } end_CELL end_ROW ,
(10)
where
L
⁢
a
⁢
d
⁢
d
⁢
e
⁢
r
f
𝐿
𝑎
𝑑
𝑑
𝑒
subscript
𝑟
𝑓
Ladder_{f}
italic_L italic_a italic_d italic_d italic_e italic_r start_POSTSUBSCRIPT italic_f end_POSTSUBSCRIPT
can be Multilayer Perceptrons (MLP)
[
57
]
, Attention Networks
[
58
]
, Transformer Blocks (with self attention)
[
59
]
, or any other types of neural networks.
Note that
L
⁢
a
⁢
d
⁢
d
⁢
e
⁢
r
1
𝐿
𝑎
𝑑
𝑑
𝑒
subscript
𝑟
1
Ladder_{1}
italic_L italic_a italic_d italic_d italic_e italic_r start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
takes only the
ϕ
th
subscript
italic-ϕ
th
\phi_{\text{th}}
italic_ϕ start_POSTSUBSCRIPT th end_POSTSUBSCRIPT
representations
𝒉
ϕ
subscript
𝒉
italic-ϕ
\boldsymbol{h}_{\phi}
bold_italic_h start_POSTSUBSCRIPT italic_ϕ end_POSTSUBSCRIPT
from the LLM backbone as the input, whereas subsequent
L
⁢
a
⁢
d
⁢
d
⁢
e
⁢
r
f
𝐿
𝑎
𝑑
𝑑
𝑒
subscript
𝑟
𝑓
Ladder_{f}
italic_L italic_a italic_d italic_d italic_e italic_r start_POSTSUBSCRIPT italic_f end_POSTSUBSCRIPT
relies on the representation
𝒉
f
⋅
ϕ
subscript
𝒉
⋅
𝑓
italic-ϕ
\boldsymbol{h}_{f\cdot\phi}
bold_italic_h start_POSTSUBSCRIPT italic_f ⋅ italic_ϕ end_POSTSUBSCRIPT
as well as the output from previous ladder.
Gate Network
For each domain, the target features to be learned comprise (i) common features shared across all domains and (ii) domain-specific features. Specifically, the ladder network’s output captures the domain-specific characteristics, while the final hidden states of the LLM backbone capture the commonalities across all domains. Therefore, each domain’s predictions need to leverage the ladder and LLM backbone outputs. To facilitate this integration, we design a gate network that follows the ladder network. The gate network is based on a dynamic weight assignment mechanism, aiming to adaptively balance domain-specific and common features.
Firstly, we concatenate the outputs of the last ladder and the final transformer layer of the LLM backbone:
𝑶
=
concat
⁢
(
𝒉
L
,
𝒍
⁢
𝒂
⁢
𝒅
F
)
.
𝑶
concat
subscript
𝒉
𝐿
𝒍
𝒂
subscript
𝒅
𝐹
\boldsymbol{O}=\text{concat}(\boldsymbol{h}_{L},\boldsymbol{lad}_{F}).
bold_italic_O = concat ( bold_italic_h start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT , bold_italic_l bold_italic_a bold_italic_d start_POSTSUBSCRIPT italic_F end_POSTSUBSCRIPT ) .
(11)
Subsequently, we utilize an attention pooling
[
60
]
module to compute the attention weights across the concatenated features in Equation
11
. This is to adjust the propositions of the domain-specific and common features dynamically:
𝒔
⁢
𝒄
⁢
𝒐
⁢
𝒓
⁢
𝒆
𝒔
𝒄
𝒐
𝒓
𝒆
\displaystyle\boldsymbol{score}
bold_italic_s bold_italic_c bold_italic_o bold_italic_r bold_italic_e
=
tanh
⁢
(
𝑾
k
⁢
𝑶
)
⁢
𝑾
q
,
absent
tanh
subscript
𝑾
𝑘
𝑶
subscript
𝑾
𝑞
\displaystyle=\textrm{tanh}(\boldsymbol{W}_{k}\boldsymbol{O})\boldsymbol{W}_{q},
= tanh ( bold_italic_W start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT bold_italic_O ) bold_italic_W start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT ,
(12)
𝑨
𝑨
\displaystyle\boldsymbol{A}
bold_italic_A
=
softmax
⁢
(
𝒔
⁢
𝒄
⁢
𝒐
⁢
𝒓
⁢
𝒆
)
,
absent
softmax
𝒔
𝒄
𝒐
𝒓
𝒆
\displaystyle=\textrm{softmax}(\boldsymbol{score}),
= softmax ( bold_italic_s bold_italic_c bold_italic_o bold_italic_r bold_italic_e ) ,
𝑹
𝑹
\displaystyle\boldsymbol{R}
bold_italic_R
=
𝑨
T
⁢
𝑶
,
absent
superscript
𝑨
𝑇
𝑶
\displaystyle=\boldsymbol{A}^{T}\boldsymbol{O},
= bold_italic_A start_POSTSUPERSCRIPT italic_T end_POSTSUPERSCRIPT bold_italic_O ,
where
𝑾
k
subscript
𝑾
𝑘
\boldsymbol{W}_{k}
bold_italic_W start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and
𝑾
q
subscript
𝑾
𝑞
\boldsymbol{W}_{q}
bold_italic_W start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT
are the learnable parameters for computing the key and query,
𝑨
𝑨
\boldsymbol{A}
bold_italic_A
is the attention weights normalized from
𝒔
⁢
𝒄
⁢
𝒐
⁢
𝒓
⁢
𝒆
𝒔
𝒄
𝒐
𝒓
𝒆
\boldsymbol{score}
bold_italic_s bold_italic_c bold_italic_o bold_italic_r bold_italic_e
by a softmax operation.
Lastly,
𝑹
𝑹
\boldsymbol{R}
bold_italic_R
represents the pooled weights, including common and specific features of a certain domain.
Therefore, for each domain
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
, the corresponding gate network produces a compressed representation, denoted by
𝑹
d
m
superscript
𝑹
subscript
𝑑
𝑚
\boldsymbol{R}^{d_{m}}
bold_italic_R start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
.
Tower Network
The last module of the DSN, the tower network, will use
𝑹
d
m
superscript
𝑹
subscript
𝑑
𝑚
\boldsymbol{R}^{d_{m}}
bold_italic_R start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
to make final predictions
𝒚
^
d
m
superscript
bold-^
𝒚
subscript
𝑑
𝑚
\boldsymbol{\hat{y}}^{d_{m}}
overbold_^ start_ARG bold_italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
(or
𝒚
^
predict
d
m
subscript
superscript
bold-^
𝒚
subscript
𝑑
𝑚
predict
\boldsymbol{\hat{y}}^{d_{m}}_{\text{predict}}
overbold_^ start_ARG bold_italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT start_POSTSUBSCRIPT predict end_POSTSUBSCRIPT
in Fig.
2
), where the ground truth label is
𝒚
d
m
superscript
𝒚
subscript
𝑑
𝑚
\boldsymbol{y}^{d_{m}}
bold_italic_y start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
(or denoted as
𝒚
true
d
m
subscript
superscript
𝒚
subscript
𝑑
𝑚
true
\boldsymbol{y}^{d_{m}}_{\text{true}}
bold_italic_y start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT start_POSTSUBSCRIPT true end_POSTSUBSCRIPT
in Fig.
2
). Each domain-specific network has one tower network, which is an MLP network as follows:
𝒚
^
d
m
superscript
bold-^
𝒚
subscript
𝑑
𝑚
\displaystyle\boldsymbol{\hat{y}}^{d_{m}}
overbold_^ start_ARG bold_italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
=
MLP
⁢
(
𝑹
d
m
;
𝑾
γ
d
m
,
𝒃
γ
d
m
)
,
absent
MLP
superscript
𝑹
subscript
𝑑
𝑚
superscript
subscript
𝑾
𝛾
subscript
𝑑
𝑚
superscript
subscript
𝒃
𝛾
subscript
𝑑
𝑚
\displaystyle=\text{MLP}(\boldsymbol{R}^{d_{m}};\boldsymbol{W}_{\gamma}^{d_{m}%
},\boldsymbol{b}_{\gamma}^{d_{m}}),
= MLP ( bold_italic_R start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_W start_POSTSUBSCRIPT italic_γ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , bold_italic_b start_POSTSUBSCRIPT italic_γ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ,
(13)
where
𝑾
γ
d
m
superscript
subscript
𝑾
𝛾
subscript
𝑑
𝑚
\boldsymbol{W}_{\gamma}^{d_{m}}
bold_italic_W start_POSTSUBSCRIPT italic_γ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
and
𝒃
γ
d
m
superscript
subscript
𝒃
𝛾
subscript
𝑑
𝑚
\boldsymbol{b}_{\gamma}^{d_{m}}
bold_italic_b start_POSTSUBSCRIPT italic_γ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
denote the weights and biases of the MLP network.
𝒚
^
d
m
superscript
bold-^
𝒚
subscript
𝑑
𝑚
\boldsymbol{\hat{y}}^{d_{m}}
overbold_^ start_ARG bold_italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
is the prediction of whether the user will click it on this item or not.
IV-C
3
General Network
In the previous Section
IV-C
2
, we design distinct DSNs to model and predict within specific seen domains.
For Uni-CTR to operate effectively with new, unseen domains, we have constructed a general network that captures the commonalities of all established domains.
Specifically, the general network contains only a tower network and directly utilizes the last hidden states
h
L
subscript
ℎ
𝐿
{h}_{L}
italic_h start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT
of the LLM backbone via MLP network, which is defined as follows:
𝒚
^
G
superscript
bold-^
𝒚
𝐺
\displaystyle\boldsymbol{\hat{y}}^{G}
overbold_^ start_ARG bold_italic_y end_ARG start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT
=
MLP
⁢
(
𝒉
L
;
𝑾
σ
G
,
𝒃
σ
G
)
,
absent
MLP
subscript
𝒉
𝐿
superscript
subscript
𝑾
𝜎
𝐺
superscript
subscript
𝒃
𝜎
𝐺
\displaystyle=\text{MLP}(\boldsymbol{h}_{L};\boldsymbol{W}_{\sigma}^{G},%
\boldsymbol{b}_{\sigma}^{G}),
= MLP ( bold_italic_h start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT ; bold_italic_W start_POSTSUBSCRIPT italic_σ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT , bold_italic_b start_POSTSUBSCRIPT italic_σ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT ) ,
(14)
where
𝑾
σ
d
m
superscript
subscript
𝑾
𝜎
subscript
𝑑
𝑚
\boldsymbol{W}_{\sigma}^{d_{m}}
bold_italic_W start_POSTSUBSCRIPT italic_σ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
and
𝒃
σ
d
m
superscript
subscript
𝒃
𝜎
subscript
𝑑
𝑚
\boldsymbol{b}_{\sigma}^{d_{m}}
bold_italic_b start_POSTSUBSCRIPT italic_σ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
denote the weights and biases of the MLP network.
The general network can adapt to situations where no prior data exists, i.e., the data-sparse domains, serving as a zero-shot predictive model. In cold-start recommendation scenarios, this capability is crucial because it allows the network to maintain predictive accuracy without the need to target any domain-specific training data.
IV-D
Masked Loss Strategy
As analyzed in Section
IV-C
2
, the DSNs compute predictions for all domain samples during the training phase.
To avoid redundant predictions being taken into account by the loss function, which in turn makes the update of the DSN parameters affected by other domains, we use a masked loss strategy.
IV-D
1
Masked Multi-domain Prediction
The prediction of Uni-CTR is based on either a DSN for a known domain or the General Network for an unknown domain. For a data sample from known domains (
d
m
∈
𝑫
subscript
𝑑
𝑚
𝑫
d_{m}\in\boldsymbol{D}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ∈ bold_italic_D
), the predictions of all DSNs is denoted as
𝒚
^
D
=
[
y
^
d
1
,
y
^
d
2
,
…
,
y
^
d
M
]
superscript
bold-^
𝒚
𝐷
superscript
^
𝑦
subscript
𝑑
1
superscript
^
𝑦
subscript
𝑑
2
…
superscript
^
𝑦
subscript
𝑑
𝑀
\boldsymbol{\hat{y}}^{D}=[\hat{y}^{d_{1}},\hat{y}^{d_{2}},\ldots,\hat{y}^{d_{M%
}}]
overbold_^ start_ARG bold_italic_y end_ARG start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT = [ over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , … , over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_M end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ]
.
Note that we have
M
𝑀
M
italic_M
number of DSNs if there are
M
𝑀
M
italic_M
domains.
To remove irrelevant predictions, we keep only the prediction of one DSN whose domain is the same as
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
via a mask. The mask is generated as follows:
𝒎
⁢
𝒂
⁢
𝒔
⁢
𝒌
d
m
=
[
I
⁢
(
d
1
=
d
m
)
,
I
⁢
(
d
2
=
d
m
)
,
…
,
I
⁢
(
d
M
=
d
m
)
]
,
𝒎
𝒂
𝒔
superscript
𝒌
subscript
𝑑
𝑚
𝐼
subscript
𝑑
1
subscript
𝑑
𝑚
𝐼
subscript
𝑑
2
subscript
𝑑
𝑚
…
𝐼
subscript
𝑑
𝑀
subscript
𝑑
𝑚
\boldsymbol{mask}^{d_{m}}=\left[I(d_{1}=d_{m}),I(d_{2}=d_{m}),\ldots,I(d_{M}=d%
_{m})\right],
bold_italic_m bold_italic_a bold_italic_s bold_italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT = [ italic_I ( italic_d start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT = italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ) , italic_I ( italic_d start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT = italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ) , … , italic_I ( italic_d start_POSTSUBSCRIPT italic_M end_POSTSUBSCRIPT = italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ) ] ,
(15)
where
I
⁢
(
⋅
)
𝐼
⋅
I(\cdot)
italic_I ( ⋅ )
is an indicator function that equals
1
1
1
1
if the conditional statement is true and
0
0
otherwise.
Given a data sample from an unknown domain
d
m
∉
𝑫
subscript
𝑑
𝑚
𝑫
d_{m}\notin\boldsymbol{D}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ∉ bold_italic_D
, the prediction of Uni-CTR is determined by the output
y
^
G
superscript
^
𝑦
𝐺
\hat{y}^{G}
over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT
of the general network. Accordingly, the prediction of Uni-CTR can be formulated as follows:
y
^
=
{
sum
⁢
(
𝒎
⁢
𝒂
⁢
𝒔
⁢
𝒌
d
m
⋅
𝒚
^
D
)
if
⁢
d
m
∈
𝑫
y
^
G
if
⁢
d
m
∉
𝑫
.
^
𝑦
cases
sum
⋅
𝒎
𝒂
𝒔
superscript
𝒌
subscript
𝑑
𝑚
superscript
bold-^
𝒚
𝐷
if
subscript
𝑑
𝑚
𝑫
superscript
^
𝑦
𝐺
if
subscript
𝑑
𝑚
𝑫
\displaystyle\hat{y}=\begin{cases}\text{sum}\left(\boldsymbol{mask}^{d_{m}}%
\cdot\boldsymbol{\hat{y}}^{D}\right)&\text{if }d_{m}\in\boldsymbol{D}\\
\hat{y}^{G}&\text{if }d_{m}\notin\boldsymbol{D}\\
\end{cases}.
over^ start_ARG italic_y end_ARG = { start_ROW start_CELL sum ( bold_italic_m bold_italic_a bold_italic_s bold_italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ⋅ overbold_^ start_ARG bold_italic_y end_ARG start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT ) end_CELL start_CELL if italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ∈ bold_italic_D end_CELL end_ROW start_ROW start_CELL over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT end_CELL start_CELL if italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ∉ bold_italic_D end_CELL end_ROW .
(16)
IV-D
2
Masked Multi-domain Training
Loss Computation
The loss of each data sample comprises of: (i) domain-specific loss
ℒ
D
superscript
ℒ
𝐷
\mathcal{L}^{D}
caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT
calculated by the prediction of the domain
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
’s DSN, and (ii) general loss
ℒ
G
superscript
ℒ
G
\mathcal{L}^{\text{G}}
caligraphic_L start_POSTSUPERSCRIPT G end_POSTSUPERSCRIPT
computed based on the general network’s prediction.
The overall loss can be written as:
ℒ
=
ℒ
D
+
ℒ
G
ℒ
superscript
ℒ
𝐷
superscript
ℒ
𝐺
\mathcal{L}=\mathcal{L}^{D}+\mathcal{L}^{G}
caligraphic_L = caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT + caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT
(17)
where the domain-specific loss
ℒ
D
superscript
ℒ
𝐷
\mathcal{L}^{D}
caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT
can be computed as follows:
ℒ
D
superscript
ℒ
𝐷
\displaystyle\mathcal{L}^{D}
caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT
=
sum
⁢
(
𝒎
⁢
𝒂
⁢
𝒔
⁢
𝒌
d
m
⊙
[
ℓ
⁢
(
y
^
d
1
,
y
)
,
ℓ
⁢
(
y
^
d
2
,
y
)
,
…
,
ℓ
⁢
(
y
^
d
M
,
y
)
]
)
absent
sum
direct-product
𝒎
𝒂
𝒔
superscript
𝒌
subscript
𝑑
𝑚
ℓ
superscript
^
𝑦
subscript
𝑑
1
𝑦
ℓ
superscript
^
𝑦
subscript
𝑑
2
𝑦
…
ℓ
superscript
^
𝑦
subscript
𝑑
𝑀
𝑦
\displaystyle=\text{sum}\left(\boldsymbol{mask}^{d_{m}}\odot\left[\ell(\hat{y}%
^{d_{1}},y),\ell(\hat{y}^{d_{2}},y),\ldots,\ell(\hat{y}^{d_{M}},y)\right]\right)
= sum ( bold_italic_m bold_italic_a bold_italic_s bold_italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ⊙ [ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ) , roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ) , … , roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_M end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ) ] )
(18)
=
∑
i
=
1
M
(
m
⁢
a
⁢
s
⁢
k
i
d
m
⋅
ℓ
⁢
(
y
^
d
i
,
y
)
)
absent
superscript
subscript
𝑖
1
𝑀
⋅
𝑚
𝑎
𝑠
subscript
superscript
𝑘
subscript
𝑑
𝑚
𝑖
ℓ
superscript
^
𝑦
subscript
𝑑
𝑖
𝑦
\displaystyle=\sum_{i=1}^{M}\left(mask^{d_{m}}_{i}\cdot\ell(\hat{y}^{d_{i}},y)\right)
= ∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_M end_POSTSUPERSCRIPT ( italic_m italic_a italic_s italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ⋅ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ) )
=
m
⁢
a
⁢
s
⁢
k
m
d
m
⋅
ℓ
⁢
(
y
^
d
m
,
y
)
absent
⋅
𝑚
𝑎
𝑠
subscript
superscript
𝑘
subscript
𝑑
𝑚
𝑚
ℓ
superscript
^
𝑦
subscript
𝑑
𝑚
𝑦
\displaystyle=mask^{d_{m}}_{m}\cdot\ell(\hat{y}^{d_{m}},y)
= italic_m italic_a italic_s italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ⋅ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y )
=
ℓ
⁢
(
y
^
d
m
,
y
)
,
absent
ℓ
superscript
^
𝑦
subscript
𝑑
𝑚
𝑦
\displaystyle=\ell(\hat{y}^{d_{m}},y),
= roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ) ,
where
y
𝑦
y
italic_y
is the ground truth label of the data sample,
ℓ
⁢
(
⋅
)
ℓ
⋅
\ell(\cdot)
roman_ℓ ( ⋅ )
denotes the Binary Cross-Entropy Loss (BCELoss). The
m
⁢
a
⁢
s
⁢
k
i
d
m
𝑚
𝑎
𝑠
subscript
superscript
𝑘
subscript
𝑑
𝑚
𝑖
mask^{d_{m}}_{i}
italic_m italic_a italic_s italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
is the
i
𝑖
i
italic_i
-th binary element
I
⁢
(
d
i
=
d
m
)
𝐼
subscript
𝑑
𝑖
subscript
𝑑
𝑚
I(d_{i}=d_{m})
italic_I ( italic_d start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT = italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT )
within
𝒎
⁢
𝒂
⁢
𝒔
⁢
𝒌
d
m
𝒎
𝒂
𝒔
superscript
𝒌
subscript
𝑑
𝑚
\boldsymbol{mask}^{d_{m}}
bold_italic_m bold_italic_a bold_italic_s bold_italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
.
And the general loss
ℒ
G
superscript
ℒ
G
\mathcal{L}^{\text{G}}
caligraphic_L start_POSTSUPERSCRIPT G end_POSTSUPERSCRIPT
can be calculated as:
ℒ
G
=
ℓ
⁢
(
y
^
G
,
y
)
superscript
ℒ
𝐺
ℓ
subscript
^
𝑦
𝐺
𝑦
\mathcal{L}^{G}=\ell(\hat{y}_{G},y)
caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT = roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_G end_POSTSUBSCRIPT , italic_y )
(19)
Loss Back-propagation
The trainable components of Uni-CTR are the LLM backbone, DSNs, and the general network.
We denote the parameters of them to be
𝜽
LLM
subscript
𝜽
LLM
\boldsymbol{\theta}_{\text{LLM}}
bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT
,
𝜽
DSN
subscript
𝜽
DSN
\boldsymbol{\theta}_{\text{DSN}}
bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT
and
𝜽
G
subscript
𝜽
G
\boldsymbol{\theta}_{\text{G}}
bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT
, respectively.
Given a data sample
(
x
d
m
,
y
d
m
)
superscript
𝑥
subscript
𝑑
𝑚
superscript
𝑦
subscript
𝑑
𝑚
(x^{d_{m}},y^{d_{m}})
( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT )
from domain
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
, we use the following loss to update the parameters of Uni-CTR:
ℒ
=
ℒ
D
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
DSN
)
+
ℒ
G
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
G
)
ℒ
superscript
ℒ
𝐷
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
DSN
superscript
ℒ
𝐺
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
G
\displaystyle\mathcal{L}=\mathcal{L}^{D}\left(x^{d_{m}};\boldsymbol{\theta}_{%
\text{LLM}},\boldsymbol{\theta}_{\text{DSN}}\right)+\mathcal{L}^{G}\left(x^{d_%
{m}};\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{G}}\right)
caligraphic_L = caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT ) + caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT )
(20)
The gradient with respect to the LLM backbone parameters
𝜽
LLM
subscript
𝜽
LLM
\boldsymbol{\theta}_{\text{LLM}}
bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT
is calculated as follows:
∇
𝜽
LLM
ℒ
subscript
∇
subscript
𝜽
LLM
ℒ
\displaystyle\nabla_{\boldsymbol{\theta}_{\text{LLM}}}\mathcal{L}
∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_POSTSUBSCRIPT caligraphic_L
=
∇
𝜽
LLM
ℒ
D
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
DSN
)
absent
subscript
∇
subscript
𝜽
LLM
superscript
ℒ
𝐷
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
DSN
\displaystyle=\nabla_{\boldsymbol{\theta}_{\text{LLM}}}\mathcal{L}^{D}\left(x^%
{d_{m}};\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{DSN}}\right)
= ∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_POSTSUBSCRIPT caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT )
(21)
+
∇
𝜽
LLM
ℒ
G
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
G
)
subscript
∇
subscript
𝜽
LLM
superscript
ℒ
𝐺
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
G
\displaystyle+\nabla_{\boldsymbol{\theta}_{\text{LLM}}}\mathcal{L}^{G}\left(x^%
{d_{m}};\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{G}}\right)
+ ∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_POSTSUBSCRIPT caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT )
=
∂
ℒ
D
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
DSN
)
∂
𝜽
LLM
+
∂
ℒ
G
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
G
)
∂
𝜽
LLM
absent
superscript
ℒ
𝐷
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
DSN
subscript
𝜽
LLM
superscript
ℒ
𝐺
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
G
subscript
𝜽
LLM
\displaystyle=\frac{\partial\mathcal{L}^{D}\left(x^{d_{m}};\boldsymbol{\theta}%
_{\text{LLM}},\boldsymbol{\theta}_{\text{DSN}}\right)}{\partial\boldsymbol{%
\theta}_{\text{LLM}}}+\frac{\partial\mathcal{L}^{G}\left(x^{d_{m}};\boldsymbol%
{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{G}}\right)}{\partial%
\boldsymbol{\theta}_{\text{LLM}}}
= divide start_ARG ∂ caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_ARG + divide start_ARG ∂ caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_ARG
=
∂
𝒎
⁢
𝒂
⁢
𝒔
⁢
𝒌
d
m
⊙
[
ℓ
⁢
(
y
^
d
i
,
y
;
𝜽
LLM
,
𝜽
DSN
d
i
)
,
i
∈
[
M
]
]
∂
𝜽
LLM
absent
direct-product
𝒎
𝒂
𝒔
superscript
𝒌
subscript
𝑑
𝑚
delimited-[]
ℓ
superscript
^
𝑦
subscript
𝑑
𝑖
𝑦
subscript
𝜽
LLM
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑖
𝑖
delimited-[]
𝑀
subscript
𝜽
LLM
\displaystyle=\frac{\partial\boldsymbol{mask}^{d_{m}}\odot\left[\ell(\hat{y}^{%
d_{i}},y;\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{DSN}}^{d_%
{i}}),i\in[M]\right]}{\partial\boldsymbol{\theta}_{\text{LLM}}}
= divide start_ARG ∂ bold_italic_m bold_italic_a bold_italic_s bold_italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ⊙ [ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) , italic_i ∈ [ italic_M ] ] end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_ARG
+
∂
ℓ
⁢
(
y
^
G
,
y
;
𝜽
LLM
,
𝜽
G
)
∂
𝜽
LLM
ℓ
subscript
^
𝑦
𝐺
𝑦
subscript
𝜽
LLM
subscript
𝜽
G
subscript
𝜽
LLM
\displaystyle+\frac{\partial\ell\left(\hat{y}_{G},y;\boldsymbol{\theta}_{\text%
{LLM}},\boldsymbol{\theta}_{\text{G}}\right)}{\partial\boldsymbol{\theta}_{%
\text{LLM}}}
+ divide start_ARG ∂ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_G end_POSTSUBSCRIPT , italic_y ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_ARG
=
∂
ℓ
⁢
(
y
^
d
m
,
y
;
𝜽
LLM
,
𝜽
DSN
d
m
)
∂
𝜽
LLM
+
∂
ℓ
⁢
(
y
^
G
,
y
;
𝜽
LLM
,
𝜽
G
)
∂
𝜽
LLM
.
absent
ℓ
superscript
^
𝑦
subscript
𝑑
𝑚
𝑦
subscript
𝜽
LLM
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑚
subscript
𝜽
LLM
ℓ
subscript
^
𝑦
𝐺
𝑦
subscript
𝜽
LLM
subscript
𝜽
G
subscript
𝜽
LLM
\displaystyle=\frac{\partial\ell(\hat{y}^{d_{m}},y;\boldsymbol{\theta}_{\text{%
LLM}},\boldsymbol{\theta}_{\text{DSN}}^{d_{m}})}{\partial\boldsymbol{\theta}_{%
\text{LLM}}}+\frac{\partial\ell\left(\hat{y}_{G},y;\boldsymbol{\theta}_{\text{%
LLM}},\boldsymbol{\theta}_{\text{G}}\right)}{\partial\boldsymbol{\theta}_{%
\text{LLM}}}.
= divide start_ARG ∂ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_ARG + divide start_ARG ∂ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_G end_POSTSUBSCRIPT , italic_y ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT end_ARG .
We then elaborate the gradient for DSN parameters
𝜽
DSN
subscript
𝜽
DSN
\boldsymbol{\theta}_{\text{DSN}}
bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT
. Note that
𝜽
DSN
=
[
𝜽
DSN
d
1
,
…
,
𝜽
DSN
d
M
]
subscript
𝜽
DSN
superscript
subscript
𝜽
DSN
subscript
𝑑
1
…
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑀
\boldsymbol{\theta}_{\text{DSN}}=[\boldsymbol{\theta}_{\text{DSN}}^{d_{1}},%
\ldots,\boldsymbol{\theta}_{\text{DSN}}^{d_{M}}]
bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT = [ bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , … , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_M end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ]
consists of
M
𝑀
M
italic_M
sets of DSN parameters. The gradient of each DSN of domain
d
n
,
n
∈
{
1
,
2
,
…
,
M
}
subscript
𝑑
𝑛
𝑛
1
2
…
𝑀
d_{n},n\in\{1,2,\ldots,M\}
italic_d start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT , italic_n ∈ { 1 , 2 , … , italic_M }
is is calculated as follows:
∇
𝜽
DSN
d
n
ℒ
subscript
∇
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑛
ℒ
\displaystyle\nabla_{\boldsymbol{\theta}_{\text{DSN}}^{d_{n}}}\mathcal{L}
∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_POSTSUBSCRIPT caligraphic_L
=
∇
𝜽
DSN
d
n
ℒ
D
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
DSN
)
absent
subscript
∇
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑛
superscript
ℒ
𝐷
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
DSN
\displaystyle=\nabla_{\boldsymbol{\theta}_{\text{DSN}}^{d_{n}}}\mathcal{L}^{D}%
\left(x^{d_{m}};\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{%
DSN}}\right)
= ∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_POSTSUBSCRIPT caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT )
(22)
+
∇
𝜽
DSN
d
n
ℒ
G
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
G
)
subscript
∇
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑛
superscript
ℒ
𝐺
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
G
\displaystyle+\nabla_{\boldsymbol{\theta}_{\text{DSN}}^{d_{n}}}\mathcal{L}^{G}%
\left(x^{d_{m}};\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{G}%
}\right)
+ ∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_POSTSUBSCRIPT caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT )
=
∂
ℒ
D
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
DSN
)
∂
𝜽
DSN
d
n
absent
superscript
ℒ
𝐷
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
DSN
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑛
\displaystyle=\frac{\partial\mathcal{L}^{D}\left(x^{d_{m}};\boldsymbol{\theta}%
_{\text{LLM}},\boldsymbol{\theta}_{\text{DSN}}\right)}{\partial\boldsymbol{%
\theta}_{\text{DSN}}^{d_{n}}}
= divide start_ARG ∂ caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_ARG
=
∂
𝒎
⁢
𝒂
⁢
𝒔
⁢
𝒌
d
m
⊙
[
ℓ
⁢
(
y
^
d
i
,
y
;
𝜽
LLM
,
𝜽
DSN
d
i
)
,
i
∈
[
M
]
]
∂
𝜽
DSN
d
n
absent
direct-product
𝒎
𝒂
𝒔
superscript
𝒌
subscript
𝑑
𝑚
delimited-[]
ℓ
superscript
^
𝑦
subscript
𝑑
𝑖
𝑦
subscript
𝜽
LLM
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑖
𝑖
delimited-[]
𝑀
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑛
\displaystyle=\frac{\partial\boldsymbol{mask}^{d_{m}}\odot\left[\ell(\hat{y}^{%
d_{i}},y;\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{DSN}}^{d_%
{i}}),i\in[M]\right]}{\partial\boldsymbol{\theta}_{\text{DSN}}^{d_{n}}}
= divide start_ARG ∂ bold_italic_m bold_italic_a bold_italic_s bold_italic_k start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ⊙ [ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) , italic_i ∈ [ italic_M ] ] end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_ARG
=
\displaystyle=
=
{
0
if
⁢
n
≠
m
∂
ℓ
⁢
(
y
^
d
m
,
y
;
𝜽
LLM
,
𝜽
DSN
d
m
)
∂
𝜽
DSN
d
m
.
if
⁢
n
=
m
,
cases
0
if
𝑛
𝑚
ℓ
superscript
^
𝑦
subscript
𝑑
𝑚
𝑦
subscript
𝜽
LLM
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑚
superscript
subscript
𝜽
DSN
subscript
𝑑
𝑚
if
𝑛
𝑚
\displaystyle\begin{cases}0&\text{if }n\neq m\\
\frac{\partial\ell(\hat{y}^{d_{m}},y;\boldsymbol{\theta}_{\text{LLM}},%
\boldsymbol{\theta}_{\text{DSN}}^{d_{m}})}{\partial\boldsymbol{\theta}_{\text{%
DSN}}^{d_{m}}}.&\text{if }n=m\\
\end{cases},
{ start_ROW start_CELL 0 end_CELL start_CELL if italic_n ≠ italic_m end_CELL end_ROW start_ROW start_CELL divide start_ARG ∂ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT , italic_y ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_ARG . end_CELL start_CELL if italic_n = italic_m end_CELL end_ROW ,
which indicates that only parameters of DSN
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
can be updated due to the mask we defined in Equation
15
. The parameters of all DSNs other than
d
m
subscript
𝑑
𝑚
d_{m}
italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT
remain unchanged, ensuring the decoupling of gradient updates across various domains. Therefore, each DSN can independently model the characteristics of each domain without affecting other DSNs.
Finally, the gradient of the loss with respect to the general network parameters
𝜽
G
subscript
𝜽
G
\boldsymbol{\theta}_{\text{G}}
bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT
is computed as follows:
∇
𝜽
G
ℒ
subscript
∇
subscript
𝜽
G
ℒ
\displaystyle\nabla_{\boldsymbol{\theta}_{\text{G}}}\mathcal{L}
∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT end_POSTSUBSCRIPT caligraphic_L
=
∇
𝜽
G
ℒ
D
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
DSN
)
+
∇
𝜽
G
ℒ
G
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
G
)
absent
subscript
∇
subscript
𝜽
G
superscript
ℒ
𝐷
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
DSN
subscript
∇
subscript
𝜽
G
superscript
ℒ
𝐺
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
G
\displaystyle=\nabla_{\boldsymbol{\theta}_{\text{G}}}\mathcal{L}^{D}\left(x^{d%
_{m}};\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{DSN}}\right)%
+\nabla_{\boldsymbol{\theta}_{\text{G}}}\mathcal{L}^{G}\left(x^{d_{m}};%
\boldsymbol{\theta}_{\text{LLM}},\boldsymbol{\theta}_{\text{G}}\right)
= ∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT end_POSTSUBSCRIPT caligraphic_L start_POSTSUPERSCRIPT italic_D end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT DSN end_POSTSUBSCRIPT ) + ∇ start_POSTSUBSCRIPT bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT end_POSTSUBSCRIPT caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT )
(23)
=
∂
ℒ
G
⁢
(
x
d
m
;
𝜽
LLM
,
𝜽
G
)
∂
𝜽
G
absent
superscript
ℒ
𝐺
superscript
𝑥
subscript
𝑑
𝑚
subscript
𝜽
LLM
subscript
𝜽
G
subscript
𝜽
G
\displaystyle=\frac{\partial\mathcal{L}^{G}\left(x^{d_{m}};\boldsymbol{\theta}%
_{\text{LLM}},\boldsymbol{\theta}_{\text{G}}\right)}{\partial\boldsymbol{%
\theta}_{\text{G}}}
= divide start_ARG ∂ caligraphic_L start_POSTSUPERSCRIPT italic_G end_POSTSUPERSCRIPT ( italic_x start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT end_ARG
=
∂
ℓ
⁢
(
y
^
G
,
y
;
𝜽
LLM
,
𝜽
G
)
∂
𝜽
G
.
absent
ℓ
subscript
^
𝑦
𝐺
𝑦
subscript
𝜽
LLM
subscript
𝜽
G
subscript
𝜽
G
\displaystyle=\frac{\partial\ell\left(\hat{y}_{G},y;\boldsymbol{\theta}_{\text%
{LLM}},\boldsymbol{\theta}_{\text{G}}\right)}{\partial\boldsymbol{\theta}_{%
\text{G}}}.
= divide start_ARG ∂ roman_ℓ ( over^ start_ARG italic_y end_ARG start_POSTSUBSCRIPT italic_G end_POSTSUBSCRIPT , italic_y ; bold_italic_θ start_POSTSUBSCRIPT LLM end_POSTSUBSCRIPT , bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT ) end_ARG start_ARG ∂ bold_italic_θ start_POSTSUBSCRIPT G end_POSTSUBSCRIPT end_ARG .
This gradient ensures that the general network can be trained based on data samples from all domains. Hence, the general network can effectively learn different cross-domain features, and thereby, it can be generalized to unseen domains for accurate zero shot prediction.
In summary, our proposed masked loss strategy ensures that the domain-specific networks are effectively tailored to their respective tasks, while the LLM backbone and the general network learn the domains’ commonalities. This architecture enables (i) DSNs to be pluggable and scalable and make accurate predictions on known domains and (ii) the general network to robustly predict unseen domain samples.
IV-E
Horizontal Comparison and Discussion
In this section, we conduct a comparative analysis of Uni-CTR against existing MDCTR systems (as summarized in Table
I
), emphasizing the advancement and contribution of our proposed method.
TABLE I:
Comparison of our methodology with several previous research studies. “Semantics” represents the ability of the model to deal with complex semantics. “Balance” represents the ability of the model to deal with see-saw problems. “Generalization” represents the ability of the model to deal with unknown new domains. “Scalability” represents the scalability of the model’s structure.
MDCTR Model
Semantics
Balance
Generalization
Scalability
Shared Bottom
[
61
]
×
\times
×
×
\times
×
×
\times
×
✓
✓
\checkmark
✓
MMOE
[
5
]
, PLE
[
13
]
×
\times
×
✓
✓
\checkmark
✓
×
\times
×
×
\times
×
STAR
[
14
]
×
\times
×
✓
✓
\checkmark
✓
×
\times
×
✓
✓
\checkmark
✓
Uni-CTR
✓
✓
\checkmark
✓
✓
✓
\checkmark
✓
✓
✓
\checkmark
✓
✓
✓
\checkmark
✓
The Shared Bottom model
[
61
]
utilizes a neural network as the shared bottom layer to capture the common information across different domains while incorporating multiple expert networks in the upper layers to model the specific characteristics of each domain. The structure of Uni-CTR appears similar to the shared bottom structure. However, Uni-CTR differs in two aspects. Firstly, Uni-CTR integrates diverse semantic representations from different layers of the LLM backbone, whereas Shared Bottom only utilizes the representation from the final layer. Secondly, Uni-CTR incorporates a General Network, enabling it to model shared information across all domains. This feature empowers Uni-CTR to be a zero-shot predictor and perform well in unknown domains.
Both MMOE
[
5
]
and PLE
[
13
]
models target to address the imbalance between different domains. They use multiple experts and gate networks to alleviate the seesaw phenomenon.
However, their components are tightly coupled, making them hard to scale. Specifically, a new model needs to be built from scratch when incorporating a new domain.
Similarly, when a domain becomes obsolete due to business changes, removing the corresponding expert network and tower structure is challenging due to this coupling.
In comparison, all DSNs of Uni-CTR are pluggable and decoupled, allowing the model to incorporate new or remove existing domains easily.
The parameter-sharing mechanism in STAR
[
14
]
offers a solution with fundamental scalability and balance capabilities. However, it neither understands complex semantics nor works under unseen domains.
Moreover, the element-wise computation in STAR requires all DSNs to mirror the size and structure of the shared network.
Therefore, STAR can suffer from significant structural latency and complexity when applied to many domains.
On the contrary, the parameters of each DSN are significantly less than the parameters of the shared networks in Uni-CTR.
The lightweight design of Uni-CTR’s DSN makes it easier to be trained, and faster in inference.
V
Experiments
In this section, we first elaborate our experimental settings (
e.g.,
datasets, evaluation metrics, baselines, and implementation details) in Section
V-A
.
Then, we evaluate and discuss of performance and efficiency of Uni-CTR framework against baselines from different perspectives, denoted by six research questions (RQ). In Section
V-B
(RQ1), we present the main results of the performance of Uni-CTR and baseline models.
Followed by Section
V-C
(RQ2) to elaborate Uni-CTR’s capability in zero-shot prediction under unseen domains.
Section
V-D
(RQ3) studies the scaling law issue, investigating the impact of using different LLMs of varying size as the backbone of Uni-CTR.
The scalability of Uni-CTR to incorporate a new domain is illustrated in Section
V-E
(RQ4).
We visualize the representations of Uni-CTR in Section
V-F
(RQ5), to show the different roles of LLM and DSN in the latent space.
In Section
V-G
(RQ6), we perform ablation studies on (i) different combinations of semantic features as input, and (ii) different modules of Uni-CTR framework.
In summary, we aim to address the following RQs:
•
RQ1 (
§
§
\S
§
V-B
):
Can Uni-CTR outperform existing SOTA baselines in MDCTR prediction across multiple domains?
•
RQ2 (
§
§
\S
§
V-C
): Can Uni-CTR operate effectively in unseen domains and make accurate predictions in a zero-shot manner?
•
RQ3 (
§
§
\S
§
V-D
): Does the scaling law regarding model size apply to Uni-CTR? Does a larger LLM guarantee better performance?
•
RQ4 (
§
§
\S
§
V-E
): Can Uni-CTR scale to incorporate a new domain by simply adding and fine-tuning a new domain-specific network with other parts frozen?
•
RQ5 (
§
§
\S
§
V-F
): What are the functionalities of the LLM and DSNs, and their impacts on overall model performance?
•
RQ6 (
§
§
\S
§
V-G
): How do the main components of Uni-CTR,
i.e.,
semantic modeling prompt, LLM backbone, and DSNs, contribute to Uni-CTR’s overall performance?
V-A
Experimental Settings
V-A
1
Datasets
we utilize the
Amazon Review Data (2018)
[
62
]
, a widely used dataset in CTR prediction.
It contains records of user interactions with items on the Amazon shopping site from 1996 to 2008.
Following previous work
[
48
,
49
]
, we select five categories (Fashion, Digital Music, Musical Instruments, Gift Cards, All Beauty) of products as distinct domains for our experiments.
The statistics of the number of users, products, and data samples are shown in Table
II
.
In our experiment, we utilize features including domain names, user IDs, user click history, product IDs, product names, descriptions, and prices.
We take the items with ratings above
3
3
3
3
as positive examples and those with ratings equal to or below
3
3
3
3
as negative examples.
We follow previous works
[
63
,
48
,
49
]
to split the 80%, 10%, and 10% of the dataset for training, validation, and testing, respectively.
In classical multi-domain datasets such as
Ali-CCP
1
1
1
https://tianchi.aliyun.com/dataset/408
[
64
]
and
Ali-Mama
2
2
2
https://tianchi.aliyun.com/dataset/56
[
65
,
66
]
, features are anonymized.
Specifically, all feature values are labeled as IDs, with related natural languages masked.
Since LLM-based recommendation relies heavily on the semantic features extracted by the LLM backbone, those ID-based features are unsuitable in our experiment setting.
Thus, we exclude Ali-CCP and Ali-Mama from our experiments.
TABLE II:
Statistics of Amazon Review dataset.
Domains
Users
Products
Samples
Fashion
749,233
186,189
883,636
Digital Music
127,174
66,010
1,584,082
Musical Instruments
903,060
112,132
1,512,530
Gift Cards
128,873
1,547
147,194
All Beauty
319,335
32,486
371,345
V-A
2
Evaluation Metrics
To evaluate Uni-CTR and other baselines, we use the area under the ROC curve (
AUC
) metric. The ROC (Receiver Operating Characteristic) plots the True Positive Rate (TPR) against the False Positive Rate (FPR) at various threshold settings.
The AUC quantifies the overall ability of the model to discriminate between the positive and negative classes in all confidence levels.
Mathematically, it is represented as:
A
⁢
U
⁢
C
=
∫
0
1
T
⁢
P
⁢
R
⁢
(
F
⁢
P
⁢
R
−
1
⁢
(
u
)
)
⁢
𝑑
u
,
𝐴
𝑈
𝐶
superscript
subscript
0
1
𝑇
𝑃
𝑅
𝐹
𝑃
superscript
𝑅
1
𝑢
differential-d
𝑢
\displaystyle AUC=\int_{0}^{1}TPR(FPR^{-1}(u))du,
italic_A italic_U italic_C = ∫ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT italic_T italic_P italic_R ( italic_F italic_P italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT ( italic_u ) ) italic_d italic_u ,
(24)
where
T
⁢
P
⁢
R
𝑇
𝑃
𝑅
TPR
italic_T italic_P italic_R
is the True Positive Rate,
F
⁢
P
⁢
R
−
1
𝐹
𝑃
superscript
𝑅
1
FPR^{-1}
italic_F italic_P italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT
is the inverse of the False Positive Rate, and
u
𝑢
u
italic_u
is the threshold. An AUC value of 1 indicates perfect discrimination, while a value of 0.5 indicates that the performance is equivalent to a random guess. Higher AUC values indicate better performance of the model.
Additionally, we follow previous work
[
67
,
48
,
23
]
using
RelaImpr
metric to quantify the relative performance improvement over the baseline models.
The RelaImpr is calculated as:
R
⁢
e
⁢
l
⁢
a
⁢
I
⁢
m
⁢
p
⁢
r
=
(
A
⁢
U
⁢
C
⁢
(
m
⁢
e
⁢
a
⁢
s
⁢
u
⁢
r
⁢
e
⁢
m
⁢
o
⁢
d
⁢
e
⁢
l
)
−
0.5
A
⁢
U
⁢
C
⁢
(
b
⁢
a
⁢
s
⁢
e
⁢
m
⁢
o
⁢
d
⁢
e
⁢
l
)
−
0.5
−
1
)
×
100
%
.
𝑅
𝑒
𝑙
𝑎
𝐼
𝑚
𝑝
𝑟
𝐴
𝑈
𝐶
𝑚
𝑒
𝑎
𝑠
𝑢
𝑟
𝑒
𝑚
𝑜
𝑑
𝑒
𝑙
0.5
𝐴
𝑈
𝐶
𝑏
𝑎
𝑠
𝑒
𝑚
𝑜
𝑑
𝑒
𝑙
0.5
1
percent
100
\displaystyle RelaImpr=(\frac{AUC(measure\ model)-0.5}{AUC(base\ model)-0.5}-1%
)\times 100\%.
italic_R italic_e italic_l italic_a italic_I italic_m italic_p italic_r = ( divide start_ARG italic_A italic_U italic_C ( italic_m italic_e italic_a italic_s italic_u italic_r italic_e italic_m italic_o italic_d italic_e italic_l ) - 0.5 end_ARG start_ARG italic_A italic_U italic_C ( italic_b italic_a italic_s italic_e italic_m italic_o italic_d italic_e italic_l ) - 0.5 end_ARG - 1 ) × 100 % .
(25)
V-A
3
Baselines
To rigorously assess the performance of Uni-CTR, we compare it against a diverse array of baseline models. These models are mainly categorized into two groups: Single-domain and Multi-domain CTR models.
Single-Domain Models
•
PNN.
PNN
[
6
]
introduces a product layer, which employs product operations to capture interactions across different feature categories.
•
DCN.
Deep & Cross Network
[
7
]
proposes a cross-network explicitly tailored to model bounded-degree feature interactions balancing expressiveness with computational efficiency.
•
DeepFM.
DeepFM
[
8
]
integrates Factorization Machines (FM) for low-order feature interactions with deep neural networks for high-order feature interactions.
•
xDeepFM.
xDeepFM
[
9
]
innovates by introducing the Compressed Interaction Network (CIN) to capture high-order feature interactions efficiently.
•
DIEN.
The Deep Interest Evolution Network (DIEN)
[
29
]
introduces a two-layer structure, the attention-based Interest Extractor Layer and the Interest Evolving Layer, to capture and evolve user interests over time.
•
AutoInt.
AutoInt
[
10
]
uses multi-head self-attention networks to capture hierarchical input feature interactions.
•
FiBiNET.
FiBiNET
[
11
]
integrates the Squeeze-Excitation network (SENET) mechanism to assess feature importance dynamically and employs a bilinear function to capture complex feature interactions.
•
IntTower.
IntTower
[
63
]
is a two-tower model for pre-ranking systems, enhancing interaction between user and item features to improve prediction accuracy and inference efficiency in large-scale applications.
TABLE III:
Performance comparison of different models. The boldface denotes the highest score, and the underline indicates the best result of all baselines.
⋆
⋆
\star
⋆
represents significance level
p
𝑝
p
italic_p
-value
<
0.05
absent
0.05
<0.05
< 0.05
of comparing Uni-CTR (BackBone Sheared-LLama) with the best baselines.
Category
Models
Fashion
Musical Instruments
Gift Cards
AUC
RelaImpr
AUC
RelaImpr
AUC
RelaImpr
Single-domain
PNN
0.6979
27.49%
0.6859
38.19%
0.5959
134.20%
DCN
0.6985
27.10%
0.6893
35.71%
0.6126
99.47%
DeepFM
0.6982
27.30%
0.6880
36.65%
0.5937
139.70%
xDeepFM
0.7031
24.22%
0.6892
35.78%
0.6121
100.36%
DIEN
0.6995
26.47%
0.6881
36.58%
0.6105
103.26%
AutoInt
0.7003
25.96%
0.6888
36.07%
0.5976
130.12%
FiBiNET
0.6770
42.54%
0.6878
36.79%
0.6120
100.54%
IntTower
0.6988
26.91%
0.6888
36.07%
0.6100
104.18%
Multi-domain
Shared Bottom
0.6946
29.65%
0.6875
37.01%
0.5907
147.63%
MMOE
0.6907
32.30%
0.6857
38.34%
0.6104
103.44%
PLE
0.6842
36.97%
0.6813
41.70%
0.6375
63.35%
STAR
0.6874
34.63%
0.6831
40.31%
0.6242
80.84%
SAR-Net
0.6824
38.32%
0.6763
45.72%
0.6055
112.89%
DFFM
0.6973
27.88%
0.6856
38.42%
0.6324
69.64%
LLM-based Multi-domain
Uni-CTR
0.7523
⋆
-
0.7569
⋆
-
0.7246
⋆
-
*
It is worth noting that an AUC increase of 0.001 can be considered a significant improvement in CTR prediction
[
63
,
23
,
68
,
11
]
.
Multi-Domain Models
•
Shared Bottom.
Shared Bottom
[
61
]
employs a neural network architecture to extract shared features across various tasks. Additionally, it utilizes a specialized network layer at the top to model unique characteristics specific to each task.
•
MMOE.
MMOE
[
5
]
is characterized by a shared network of multiple expert submodels and a central gating mechanism that provides implicit connections across diverse tasks with different label spaces.
•
PLE.
Different from MMoE, Progressive Layered Extraction
[
13
]
divides experts into task-common and task-specific experts while extending the model from a single-layer network to multiple layers of experts.
•
STAR.
STAR
[
14
]
presents a star-shaped structure centered on a shared network, where the outputs of the shared model are multiplied by the domain-specific outputs.
•
SAR-Net.
SAR-Net
[
69
]
utilizes attention modules to learn users’ cross-scenario interests and employs a scenario-specific linear transformation layer, followed by debias expert networks consisting of scenario-specific and shared experts.
•
DFFM.
DFFM
[
70
]
incorporates domain-related
information into the parameters of the feature interaction and user
behavior modules, allowing for domain-specific learning of these
two aspects.
V-A
4
Implementation Details
Implementation of Uni-CTR
For the LLM backbone, we employ the Sheared-LLaMA
[
71
]
architecture, which comprises 1.3 billion parameters and 24 transformer layers. For each domain-specific network (DSN), we employ four ladder layers, each consisting of a small transformer encoder block.
For the tower network in the DSN, we use three perceptron layers with the dimension of
{
512
×
256
×
128
}
512
256
128
\{512\times 256\times 128\}
{ 512 × 256 × 128 }
.
Implementation of Baselines.
For single-domain baselines, the dimension of hidden layers of all MLP classifiers as
{
512
×
256
×
128
}
512
256
128
\{512\times 256\times 128\}
{ 512 × 256 × 128 }
, and other settings can be seen in our open source code.
For the multi-domain baselines in Table
III
, we summarize their key configurations as follows:
•
Shared Bottom
[
61
]
: The shared bottom layers have dimensions of
{
1024
×
1024
}
1024
1024
\{1024\times 1024\}
{ 1024 × 1024 }
, whereas the dimensions of the domain-specific layers are
{
1024
×
512
×
256
}
1024
512
256
\{1024\times 512\times 256\}
{ 1024 × 512 × 256 }
.
•
MMOE
[
5
]
:
The dimensions of tower and expert network are
{
1024
×
1024
}
1024
1024
\{1024\times 1024\}
{ 1024 × 1024 }
and
{
1024
×
512
}
1024
512
\{1024\times 512\}
{ 1024 × 512 }
, respectively. Note that we empirically configure to deploy
3
3
3
3
experts for best performance.
•
PLE
[
13
]
:
The extraction network of PLE consists
1
1
1
1
shared expert and
2
2
2
2
domain-specific experts for each domain. The dimensions of tower and expert network are
{
1024
×
1024
}
1024
1024
\{1024\times 1024\}
{ 1024 × 1024 }
and
{
1024
×
512
}
1024
512
\{1024\times 512\}
{ 1024 × 512 }
, respectively.
•
STAR
[
14
]
:
The hidden state dimensions of MLPs in auxiliary and star topology networks are
{
1024
×
512
×
256
}
1024
512
256
\{1024\times 512\times 256\}
{ 1024 × 512 × 256 }
.
•
SAR-Net
[
69
]
:
contains
2
2
2
2
shared and
6
6
6
6
specific Debias experts, while the hidden state dimension of each expert is
{
1024
×
1024
}
1024
1024
\{1024\times 1024\}
{ 1024 × 1024 }
. The dimension of MLP classifiers is
{
1024
×
512
}
1024
512
\{1024\times 512\}
{ 1024 × 512 }
.
•
DFFM
[
70
]
:
The dimension of the MLP used for Domain Facilitated Feature Interaction (DFFI) is
{
1024
×
512
×
256
}
1024
512
256
\{1024\times 512\times 256\}
{ 1024 × 512 × 256 }
.
Zero-Shot Setting
In the zero-shot experiment, we compare our Uni-CTR with six single-domain and four multi-domain models using three training domains (Fashion, Musical Instruments, and Gift Cards), and one test domain (All Beauty). 1) For each single-domain baseline, we train three models with an identical design on the three training domains separately.
Subsequently, we use these three models to predict the 4
th
(unknown) domain, resulting in three sets of results. Finally, we choose the best result as the final result of this single-domain baseline. 2) For multi-domain baselines, we train the models on the three training domains.
Although these baselines are implemented with multi-domain classifiers, each for a specific domain, they lack a general network structure specifically designed for out-of-domain prediction.
To mitigate this issue, we use all three classifiers to predict the 4
th
domain, resulting in three sets of results.
Similar to the approach used for single-domain baselines, we choose the best result as the final result. 3) Uni-CTR diverges from the baseline models by utilizing a general network for out-of-domain prediction.
The general network is trained across all three aforementioned domains.
Note that the predictions from three DSNs of Uni-CTR are not considered in the out-of-domain scenario.
Optimization and Training
For Uni-CTR, we employ 8 Tesla V100 GPUs with a batch size of 128. To reduce overfitting, we set the dropout
[
72
]
rate to 0.3 and utilize L2 regularization
[
73
]
. The AdamW
[
74
]
optimizer is used for Uni-CTR, and we adopt a Cyclic Learning Rate (CyclicLR) scheme to fluctuate the learning rate between the range of
[
1
×
10
−
6
,
8
×
10
−
5
]
1
superscript
10
6
8
superscript
10
5
[1\times 10^{-6},8\times 10^{-5}]
[ 1 × 10 start_POSTSUPERSCRIPT - 6 end_POSTSUPERSCRIPT , 8 × 10 start_POSTSUPERSCRIPT - 5 end_POSTSUPERSCRIPT ]
To accelerate the training of the LLM backbone, we adopt LoRA
[
75
]
with a low rank of 8 and an alpha value of 32.
Regarding the optimizer and hyper-parameter selection of our baselines, we follow the default settings mentioned in their original papers, if applicable.
Otherwise, we employ the Adam
[
74
]
optimizer with the learning rate of
1
×
10
−
3
1
superscript
10
3
1\times 10^{-3}
1 × 10 start_POSTSUPERSCRIPT - 3 end_POSTSUPERSCRIPT
and adjust individually for other hyper-parameters.
We try our best to reproduce their works to obtain the best results, ensuring fair comparisons.
V-B
Main Results (RQ1)
In this subsection, we compare the performance of Uni-CTR against other single-domain and multi-domain models. The results are summarized in Table
III
. From the table, several observations can be obtained:
•
Insights from Single-Domain Models and Existing Multi-domain Models.
The performance of single-domain models, such as DeepFM and xDeepFM, is surpassed by existing multi-domain models in the Fashion and Musical Instruments domains. This demonstrates the effectiveness of single-domain models in data-rich domains. However, single-domain models are significantly inferior to existing multi-domain models in data-sparse domains such as Gift Cards. This suggests that the joint modeling of multiple domains is beneficial for improving the performance of models in sparse domains. However, traditional multi-domain models still suffer from a serious seesaw problem, where data-rich domains (e.g., Fashion and Musical Instruments) still perform significantly better than data-sparse domains (e.g., Gift Cards).
•
Superiority of Uni-CTR.
Uni-CTR achieved substantial gains in performance across three domains, exhibiting relative improvements of
24.22%
,
35.71%
, and
63.35%
with respect to the AUC metric
3
3
3
It is worth noting that an AUC increase of 0.001 can be considered a significant improvement in CTR prediction
on Fashion, Musical Instruments, and Gift Cards, respectively. We attribute this to the powerful semantic understanding of the LLM and the powerful characteristic modeling capabilities of DSNs across various domains. Additionally, Uni-CTR effectively addresses the seesaw problem caused by data sparsity. In the Gift Cards domain, Uni-CTR achieves a significant improvement with a margin of 63.35%, substantially surpassing the performance gains observed in the other two data-rich domains. We attribute this enhancement to the pre-existing world knowledge embedded in the LLMs. This pre-trained semantic knowledge effectively compensates for the seesaw problem caused by sparse data in the third domain. Furthermore, the observed performance indicates that the inherent world knowledge and semantic understanding capabilities of the LLMs can provide significant cold-start capabilities in domains where data sparsity may hinder model performance. In the subsequent section, this also inspires us to explore the “zero-shot” capabilities of our model, assessing its potential utility and effectiveness in previously unseen domains.
V-C
Zero-Shot (Cold Start) Prediction (RQ2)
In real-world industrial recommendation systems, it is common for new business domains to emerge, often accompanied by new, unknown items. This typical situation is referred to as the cold-start problem in recommendation systems. In such cases, we lack sufficient training data to train the model. Consequently, the capability of existing models to cope with cold-start problems is of utmost importance. Therefore, this section investigates the model’s performance under a zero-shot setting. The experiment is set up in Section
V-A
4
. As illustrated in Fig.
3
, the single-domain models demonstrate the limited capacity to generalize to new domains, as evidenced by their low AUC values of around 0.51 or below. These models are limited to understanding and predicting only within the data distribution of the domains in which they are trained, resulting in poor performance in zero-shot prediction.
For multi-domain models, we observe a marked enhancement in zero-shot prediction capabilities. We hypothesize that this improvement stems from the model’s ability to leverage common information across multiple domains during training, which allows it to generalize to previously unseen domains.
Our Uni-CTR model outperforms all the baseline models, with a notable improvement exceeding
6%
points compared to traditional multi-domain models. This superior performance can be attributed to two main factors: (i) incorporating world knowledge embedded within the LLM aids in bolstering the multi-domain model’s performance under a cold-start setting, and (ii) the General Network in Uni-CTR effectively distills common knowledge across multiple domains, ensuring robust generalization capabilities when confronted with new domains.
Figure 3:
Comparative performance of zero-shot prediction on traditional models and Uni-CTR on the unseen domain (All Beauty).
V-D
LLM Scale Up (RQ3)
Figure 4:
Performance comparison of different language model backbones.
The scaling law
[
76
]
is a pivotal principle in training LLMs, describing how various aspects of a model and its training process change with scale, such as model size, dataset size, and computational resources. Specifically, the more parameters a model has and the more extensive training data it is fed, the better performance it exhibits. However, inference latency is also paramount in recommendation systems in the industry. For the CTR prediction task, the inference latency per request is typically constrained to within
10
10
10
10
milliseconds. Therefore, in this subsection, we examine the impact of parameter counts in the LLM backbone on model performance. We employ four language models as backbones: TinyBERT
[
77
]
, BERT
[
37
]
, DeBERTa-V3-Large
[
78
]
, and Sheared-LLama
[
71
]
with respective parameter counts of 14M, 110M, 340M, and 1.3 billion.
The experimental results are summarized in Fig.
4
, from which we obtain some observations:
1) With the increasing size of LLMs, a notable enhancement in performance is observed, which indicates that the scaling laws are equally applicable to Uni-CTR. Furthermore, the LLM backbone of Uni-CTR primarily captures the commonalities across domains, which provides a potential avenue for enhancing the effectiveness of traditional multi-domain CTR models in the future.
2) Uni-CTR, based on a BERT Backbone with 110M parameters, has already surpassed traditional multi-domain models. This illustrates the powerful semantic comprehension and world knowledge embedded within language models, leading to significant performance gains. Thus, our model provides a viable approach for application within the industry recommender systems.
V-E
Scalability (RQ4)
TABLE IV:
Performance comparison of different models when scaled to a new domain.
Category
Models
Scalability
Digital Music
AUC
RelaImpr
Single-domain
PNN
×
\times
×
0.5904
26.11%
DCN
×
\times
×
0.5919
24.05%
DeepFM
×
\times
×
0.5917
24.32%
xDeepFM
×
\times
×
0.5957
19.12%
AutoInt
×
\times
×
0.5913
24.86%
FiBiNET
×
\times
×
0.5832
37.02%
Multi-domain
Shared Bottom
✓
✓
\checkmark
✓
0.5975
16.92%
STAR
✓
✓
\checkmark
✓
0.6038
9.830%
MMOE,PLE
×
\times
×
-
-
LLM-based Multi-domain
Uni-CTR
✓
✓
\checkmark
✓
0.6140
-
To evaluate the scalability of the model, we freeze the weights of Uni-CTR   which has already been trained on three domains: Fashion, Musical Instruments, and Gift Cards. We then add an additional DSN for fine-tuning the Uni-CTR on a new domain, Digital Music. During training, only the parameters of the newly added DSN are updated. For single-domain models, we retrain it on the Digital Music domain. As for a scalable model like STAR, we also add a new network structure to scale it, and the training method is consistent with Uni-CTR.
The results are presented in Table
IV
.
We can observe that by merely training an additional Domain-Specific Network (DSN), the performance of Uni-CTR is improved by 9.830% compared to the multi-domain STAR model, and at least 19.12% compared to the fully retrained single-domain baseline model. This evidence confirms that the Uni-CTR has successfully identified and assimilated the commonalities across different domains during its prior training. Such an understanding of these commonalities facilitates the adaptation of Uni-CTR to new domains, utilizing this prior knowledge as a foundational base. Therefore, even with the original parameters of Uni-CTR frozen, the newly added DSN demonstrates impressive performance. This efficiency not only conserves significant computational resources but also substantially reduces the time required for model training.
V-F
Visualization (RQ5)
In this subsection, we use t-distributed Stochastic Neighbor Embedding (t-SNE)
[
79
]
to visualize representations of LLMs as well as representations of DSNs in latent space to explore their role in modeling multi-domain commonalities and characteristics.
(a)
𝒉
0
subscript
𝒉
0
\boldsymbol{h}_{0}
bold_italic_h start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
(b)
𝒉
2
subscript
𝒉
2
\boldsymbol{h}_{2}
bold_italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
(c)
𝒉
4
subscript
𝒉
4
\boldsymbol{h}_{4}
bold_italic_h start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT
Figure 5:
Visualization of the representations of different layers of the LLM.
(a)
Untrained DSN
(b)
Trained DSN
Figure 6:
Visualization of the representations of DSNs.
V-F
1
Visualization of LLM Representations
As depicted in Fig.
5
, we visualize the representations from the
0
t
⁢
h
superscript
0
𝑡
ℎ
0^{th}
0 start_POSTSUPERSCRIPT italic_t italic_h end_POSTSUPERSCRIPT
,
2
n
⁢
d
superscript
2
𝑛
𝑑
2^{nd}
2 start_POSTSUPERSCRIPT italic_n italic_d end_POSTSUPERSCRIPT
, and
4
t
⁢
h
superscript
4
𝑡
ℎ
4^{th}
4 start_POSTSUPERSCRIPT italic_t italic_h end_POSTSUPERSCRIPT
layers of the LLM, denoted as
h
0
subscript
ℎ
0
h_{0}
italic_h start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
,
h
2
subscript
ℎ
2
h_{2}
italic_h start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
, and
h
4
subscript
ℎ
4
h_{4}
italic_h start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT
, respectively.
These representations are illustrated as colored dots, with each color corresponding to a different training domain.
From Fig.
5
, we can observe two significant results.
1) The representations at different transformer layers of the LLM are distinctly distributed in the latent space, indicating that different layers of the LLM capture semantic representations at various levels. Such finding is in good agreement with the results of previous studies
[
80
,
81
]
. Therefore, it is necessary to incorporate ladder networks at different LLM layers to model semantic information at multiple levels, a point further substantiated in Section
V-G
.
2) As illustrated in Fig.
5a
, representations from various domains at the lower layers of LLM are completely aggregated. While at higher layers, as shown in Fig.
5b
and Fig.
5c
, the representations of different domains gradually start to separate. This demonstrates that the LLM is capable of not only modeling the commonalities among multiple domains but also capturing the coarse-grained characteristics of each domain, which helps the DSN network further extract information about the characteristics of the domains.
V-F
2
Visualization of DSN Representations
In order to validate the role of DSNs, we extract the representations from the penultimate layer of the tower network within DSN for each domain, comparing their states before and after training, as shown in Fig.
6
.
From Fig.
6a
, we can observe that the distributions of the representations of the three domains are mixed in the latent space before the DSNs are trained. This indicates that untrained DSNs are incapable of effectively distinguishing the representations of different domains, i.e., they cannot accurately model the characteristics of each domain. After training, as shown in Fig.
6b
, the representations of different domains in the latent space are well-separated. This shift demonstrates that DSNs gain the ability to distinguish the representations of various domains and accurately capture the characteristics of each domain through training.
V-G
Ablation Study (RQ6)
To clarify the role of different components in the Uni-CTR model,
we conduct ablation studies and the results are summarized in Table
V
and Table
VI
.
V-G
1
Impact of Prompt
TABLE V:
Ablation Study Results about the input text of Uni-CTR (BackBone DeBERTa-V3-Large).
Input Text
Fashion
Musical Instruments
Gift Cards
Full Prompt
0.7047
0.7008
0.6825
Only Feature ID and Feature Name
0.6960
0.6960
0.6749
Only Feature ID
0.6951
0.6835
0.6605
To assess the importance of prompt semantics in LLMs, we explore the impact of different prompts on model performance, as detailed in Table
V
. The ‘Full Prompt’ format, the original design for Uni-CTR discussed in Section
IV-B
, utilizes complete semantic information. The ‘Only Feature ID and Feature Name’ format combines feature names and feature ID into a single string, removing other semantic information. The ‘Only Feature ID’ format further simplifies this by retaining only feature ID values. We compared the results after training the same 5 epochs using Uni-CTR with DeBERTa-V3-Large as the backbone LLM. Our findings indicate a marked decline in performance with the reduction of semantic information in the prompts.
The analysis of the results reveals the significance of prompt design in LLMs. In all three domains (Fashion, Musical Instruments, and Gift Cards), the fully semantic ‘Full Prompt’ format consistently outperformed the other two. Specifically, the performance dropped by 1.23% and 1.36% in the ‘Ony Feature ID and Feature Name’ and ‘Only Feature ID’ formats, respectively, for Fashion domain.
Moreover, the most pronounced decline was observed in the Gift Cards domain compared to the other two domains. This significant drop can be attributed to the relatively smaller size of the dataset in this domain. The relatively small data size necessitates a higher reliance on rich semantic information to compensate for the lack of extensive data points, making the impact of prompt design more pronounced.
These results emphasize the critical role of semantic information in enhancing LLMs’ understanding and prediction accuracy. The performance of the model decreases as the semantic information decreases, suggesting that LLM relies heavily on semantic information to make accurate predictions. Thus, while simplifying the input format can improve computational efficiency, it clearly affects the performance of the model. Considering these findings, optimizing prompt design is a crucial aspect when deploying LLMs for MDCTR prediction.
V-G
2
Impact of Ladder Network and LLM
TABLE VI:
Ablation Study Results of Uni-CTR (BackBone DeBERTa-V3-Large).
Model
Fashion
Musical Instruments
Gift Cards
Uni-CTR
0.7391
0.7395
0.7073
w/o ladder
0.7084
0.6975
0.6723
w/o LLM
0.6954
0.6923
0.6100
MMOE(340M)
0.7038
0.7005
0.6712
STAR(340M)
0.7107
0.7016
0.6775
In order to clarify the role of domain-specific networks as well as the LLM Backone in the Uni-CTR model, we conduct the following ablation study, and the results are summarized in Table
VI
.
1) We remove the ladder network, restricting the architecture to only utilize the LLM and the three Tower layers for both training and prediction. We observe a considerable degradation in performance, indicative of the essential role that the ladder network plays in leveraging multi-level semantic information from LLM. This suggests that the extraction of characteristic information pertinent to distinct domains benefits from the intricate semantics provided by the ladder network, and relying solely on the LLM is insufficient.
2) We remove the LLM, i.e., we replace the LLM with a DNN with the same number of layers, and the inputs are changed to the traditional IDs. we can observe that when the LLM backbone is lost, not only does the model show a huge loss of performance on all domains, but also the drop is significant on data-sparse domains (Gifts Cards). This shows that LLM plays the most crucial role in improving the performance on data-sparse domains.
3) To verify whether it is the increase in the number of parameters that brings about the performance improvement, we increase the number of parameters of the models of MMOE and PLE to the same size as that of Uni-CTR (340M). The results show that even with the same number of parameters, the performance of the traditional recommendation model is still much weaker than that of Uni-CTR, but better than that of Uni-CTR without LLM or ladder layer, which indicates that both the ladder layer and LLM backbone contribute to the performance of Uni-CTR.
VI
Industrial Experiments
TABLE VII:
The overall performance of models trained on the industrial dataset.
Category
Models
Domain 0
Domain 1
AUC
RelaImpr
AUC
RelaImpr
Single-domain
PNN
0.6735
37.58%
0.6199
56.88%
DCN
0.6722
38.62%
0.6243
51.33%
DeepFM
0.6743
36.95%
0.6223
53.80%
xDeepFM
0.6738
37.34%
0.6226
53.43%
AutoInt
0.6788
33.50%
0.6214
54.94%
FiBiNET
0.6780
34.10%
0.6146
64.14%
Multi-domain
MMoE
0.7045
16.72%
0.6640
14.70%
PLE
0.7019
18.23%
0.6706
10.26%
STAR
0.7000
19.35%
0.6638
14.84%
LLM-based Multi-domain
Uni-CTR
0.7387
-
0.6881
-
This section outlines the practical application and empirical evaluation of Uni-CTR in a real-world industrial setting.
In preparation for the experiment,
we gather and sample one month of user behavior data from a large-scale industrial recommender system.
This platform generates millions of user logs daily, providing a substantial and diverse collection of data on user interactions and preferences.
VI-A
Model Performance of Industry Platform
In this real-world application, users are divided into two domains based on business requirements, referred to as
Domain 0
and
Domain 1
.
The single-domain models are individually trained on each domain, while the multi-domain models and our proposed Uni-CTR are trained conjointly on both domains.
The results are summarized in Table
VII
. From the table, we observe the following phenomena:
1) In this industrial scenario, even multi-domain models outperform single-domain models by a large margin. We speculate that this is because modeling the commonality of multiple domains is particularly important in large-scale industrial datasets. However, in smaller datasets such as Amazon, the impact of multi-domain commonalities on various domains is not obvious.
2) Trained on real-world industrial datasets, Uni-CTR outperforms SOTA multi-domain models, achieving an impressive relative improvement in AUC of over
10.26%
. This significant performance gain can be attributed to the adoption of text-based input, which not only enhances the model’s flexibility but also enriches its semantic understanding. Such rich semantic understanding proves to be a crucial factor in the superior performance of Uni-CTR.
VI-B
Model Inference Acceleration
In industrial recommender systems, the online model serving latency is subject to a strict constraint, typically set at around 1 to 2 milliseconds for a single instance. As a result, ensuring high service efficiency holds paramount importance for CTR models. However, for applications using LLMs, latency
[
48
]
is an intractable problem because of the complex attention mechanism and the excessive depth of the transformer layers.
For inference acceleration, we export the trained model (with backbone DeBERTa-V3-Large) to .onnx
4
4
4
https://onnx.ai/
format, which enables us to perform model inference utilizing a static graph paradigm. We then quantize it using FP16 precision with the assistance of the TensorRT tool
5
5
5
https://github.com/NVIDIA/TensorRT
. With a batch size of 32 and a sequence length of 256, the Uni-CTR inference latency on a single Tesla V100 GPU is 80ms. The average per-sample latency is around 2ms, and the loss in AUC is below 0.01, which is still significantly better than existing traditional multi-domain recommendation models. This latency is perfectly acceptable for Uni-CTR to be used in the rank stage for industrial recommender systems.
VII
Conclusion
In this paper, we propose Uni-CTR, a unified framework for multi-domain CTR prediction.
It comprises an LLM backbone plugged with multiple domain-specific networks and a general network.
The introduced LLM backbone learns common features across various domains from the designed prompts with its powerful semantic understanding.
After, the domain-specific networks receive layer-wise representations from the transformer layers of the LLM to capture characteristics inherent to each specific domain.
Simultaneously, the general network learns common patterns across all the domains to enable zero-shot prediction for unseen domains.
In the extensive experiments conducted on both public and industrial datasets, the Uni-CTR model outperforms existing single-domain and multi-domain models, effectively mitigating the “seesaw phenomenon” and improving generalization to new domains.
Future research will continue to investigate the enhancement in input modalities for multi-domain CTR prediction.
Acknowledgment
This research was partially supported by Huawei (Huawei Innovation Research Program), Research Impact Fund (No.R1015-23), APRC - CityU New Research Initiatives (No.9610565, Start-up Grant for New Faculty of City University of Hong Kong), CityU - HKIDS Early Career Research Grant (No.9360163), Hong Kong ITC Innovation and Technology Fund Midstream Research Programme for Universities Project (No.ITS/034/22MS), Hong Kong Environmental and Conservation Fund (No. 88/2022), and SIRG - CityU Strategic Interdisciplinary Research Grant (No.7020046, No.7020074).
References
[1]
M. Richardson, E. Dominowska, and R. Ragno, “Predicting clicks: estimating the click-through rate for new ads,” in
Proceedings of the 16th International Conference on World Wide Web, WWW 2007, Banff, Alberta, Canada, May 8-12, 2007
, C. L. Williamson, M. E. Zurko, P. F. Patel-Schneider, and P. J. Shenoy, Eds.   Banff, Alberta, Canada: ACM, 2007, pp. 521–530. [Online]. Available:
https://doi.org/10.1145/1242572.1242643
[2]
Y. Yang and P. Zhai, “Click-through rate prediction in online advertising: A literature review,”
Inf. Process. Manag.
, vol. 59, no. 2, p. 102853, 2022. [Online]. Available:
https://doi.org/10.1016/j.ipm.2021.102853
[3]
H. Gebauer, M. Paiola, N. Saccani, and M. Rapaccini, “Digital servitization: Crossing the perspectives of digitization and servitization,”
Industrial Marketing Management
, vol. 93, pp. 382–388, 2021. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0019850120304855
[4]
J. M. Xusen Cheng and X. Yan, “Sharing economy enabled digital platforms for development,”
Information Technology for Development
, vol. 27, no. 4, pp. 635–644, 2021. [Online]. Available:
https://doi.org/10.1080/02681102.2021.1971831
[5]
J. Ma, Z. Zhao, X. Yi, J. Chen, L. Hong, and E. H. Chi, “Modeling task relationships in multi-task learning with multi-gate mixture-of-experts,” in
Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, KDD 2018, London, UK, August 19-23, 2018
, Y. Guo and F. Farooq, Eds.   London, UK: ACM, 2018, pp. 1930–1939. [Online]. Available:
https://doi.org/10.1145/3219819.3220007
[6]
Y. Qu, H. Cai, K. Ren, W. Zhang, Y. Yu, Y. Wen, and J. Wang, “Product-based neural networks for user response prediction,” in
IEEE 16th International Conference on Data Mining, ICDM 2016, December 12-15, 2016, Barcelona, Spain
, F. Bonchi, J. Domingo-Ferrer, R. Baeza-Yates, Z. Zhou, and X. Wu, Eds.   Barcelona, Spain: IEEE Computer Society, 2016, pp. 1149–1154. [Online]. Available:
https://doi.org/10.1109/ICDM.2016.0151
[7]
R. Wang, B. Fu, G. Fu, and M. Wang, “Deep & cross network for ad click predictions,” in
Proceedings of the ADKDD’17, Halifax, NS, Canada, August 13 - 17, 2017
.   Halifax, NS, Canada: ACM, 2017, pp. 12:1–12:7. [Online]. Available:
https://doi.org/10.1145/3124749.3124754
[8]
H. Guo, R. Tang, Y. Ye, Z. Li, and X. He, “Deepfm: A factorization-machine based neural network for CTR prediction,” in
Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, IJCAI 2017, Melbourne, Australia, August 19-25, 2017
, C. Sierra, Ed.   Melbourne, Australia: ijcai.org, 2017, pp. 1725–1731. [Online]. Available:
https://doi.org/10.24963/ijcai.2017/239
[9]
J. Lian, X. Zhou, F. Zhang, Z. Chen, X. Xie, and G. Sun, “xdeepfm: Combining explicit and implicit feature interactions for recommender systems,” in
Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, KDD 2018, London, UK, August 19-23, 2018
, Y. Guo and F. Farooq, Eds.   London, UK: ACM, 2018, pp. 1754–1763. [Online]. Available:
https://doi.org/10.1145/3219819.3220023
[10]
W. Song, C. Shi, Z. Xiao, Z. Duan, Y. Xu, M. Zhang, and J. Tang, “Autoint: Automatic feature interaction learning via self-attentive neural networks,” in
Proceedings of the 28th ACM International Conference on Information and Knowledge Management, CIKM 2019, Beijing, China, November 3-7, 2019
, W. Zhu, D. Tao, X. Cheng, P. Cui, E. A. Rundensteiner, D. Carmel, Q. He, and J. X. Yu, Eds.   Beijing, China: ACM, 2019, pp. 1161–1170. [Online]. Available:
https://doi.org/10.1145/3357384.3357925
[11]
T. Huang, Z. Zhang, and J. Zhang, “Fibinet: combining feature importance and bilinear feature interaction for click-through rate prediction,” in
Proceedings of the 13th ACM Conference on Recommender Systems, RecSys 2019, Copenhagen, Denmark, September 16-20, 2019
, T. Bogers, A. Said, P. Brusilovsky, and D. Tikk, Eds.   Copenhagen, Denmark: ACM, 2019, pp. 169–177. [Online]. Available:
https://doi.org/10.1145/3298689.3347043
[12]
Y. Juan, Y. Zhuang, W. Chin, and C. Lin, “Field-aware factorization machines for CTR prediction,” in
Proceedings of the 10th ACM Conference on Recommender Systems, Boston, MA, USA, September 15-19, 2016
, S. Sen, W. Geyer, J. Freyne, and P. Castells, Eds.   Boston, MA, USA: ACM, 2016, pp. 43–50. [Online]. Available:
https://doi.org/10.1145/2959100.2959134
[13]
H. Tang, J. Liu, M. Zhao, and X. Gong, “Progressive layered extraction (PLE): A novel multi-task learning (MTL) model for personalized recommendations,” in
RecSys 2020: Fourteenth ACM Conference on Recommender Systems, Virtual Event, Brazil, September 22-26, 2020
, R. L. T. Santos, L. B. Marinho, E. M. Daly, L. Chen, K. Falk, N. Koenigstein, and E. S. de Moura, Eds.   London, UK: ACM, 2020, pp. 269–278. [Online]. Available:
https://doi.org/10.1145/3383313.3412236
[14]
X. Sheng, L. Zhao, G. Zhou, X. Ding, B. Dai, Q. Luo, S. Yang, J. Lv, C. Zhang, H. Deng, and X. Zhu, “One model to serve all: Star topology adaptive recommender for multi-domain CTR prediction,” in
CIKM ’21: The 30th ACM International Conference on Information and Knowledge Management, Virtual Event, Queensland, Australia, November 1 - 5, 2021
, G. Demartini, G. Zuccon, J. S. Culpepper, Z. Huang, and H. Tong, Eds.   Queensland, Australia: ACM, 2021, pp. 4104–4113. [Online]. Available:
https://doi.org/10.1145/3459637.3481941
[15]
X. Yang, X. Peng, P. Wei, S. Liu, L. Wang, and B. Zheng, “Adasparse: Learning adaptively sparse structures for multi-domain click-through rate prediction,” in
Proceedings of the 31st ACM International Conference on Information & Knowledge Management, Atlanta, GA, USA, October 17-21, 2022
, M. A. Hasan and L. Xiong, Eds.   Atlanta, GA, USA: ACM, 2022, pp. 4635–4639. [Online]. Available:
https://doi.org/10.1145/3511808.3557541
[16]
J. Chang, C. Zhang, Y. Hui, D. Leng, Y. Niu, Y. Song, and K. Gai, “Pepnet: Parameter and embedding personalized network for infusing with personalized prior information,” in
Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD 2023, Long Beach, CA, USA, August 6-10, 2023
, A. K. Singh, Y. Sun, L. Akoglu, D. Gunopulos, X. Yan, R. Kumar, F. Ozcan, and J. Ye, Eds.   Long Beach, CA, USA: ACM, 2023, pp. 3795–3804. [Online]. Available:
https://doi.org/10.1145/3580305.3599884
[17]
Y. Luo, S. Ma, M. Nie, C. Peng, Z. Lin, J. Shao, and Q. Xu, “Domain-aware cross-attention for cross-domain recommendation,” 2024.
[18]
G. Jawahar, B. Sagot, and D. Seddah, “What does BERT learn about the structure of language?” in
Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1: Long Papers
, A. Korhonen, D. R. Traum, and L. Màrquez, Eds.   Florence, Italy: Association for Computational Linguistics, 2019, pp. 3651–3657. [Online]. Available:
https://doi.org/10.18653/v1/p19-1356
[19]
O. Chapelle and S. S. Keerthi, “Efficient algorithms for ranking with svms,”
Inf. Retr.
, vol. 13, no. 3, pp. 201–215, 2010. [Online]. Available:
https://doi.org/10.1007/s10791-009-9109-9
[20]
R. Kumar, S. M. Naik, V. D. Naik, S. Shiralli, S. V.G, and M. Husain, “Predicting clicks: Ctr estimation of advertisements using logistic regression classifier,” in
2015 IEEE International Advance Computing Conference (IACC)
.   Bangalore, India: IEEE, 2015, pp. 1134–1138.
[21]
J. Chen, B. Sun, H. Li, H. Lu, and X.-S. Hua, “Deep ctr prediction in display advertising,” in
Proceedings of the 24th ACM International Conference on Multimedia
, ser. MM ’16.   New York, NY, USA: Association for Computing Machinery, 2016, p. 811–820. [Online]. Available:
https://doi.org/10.1145/2964284.2964325
[22]
Q. Liu, F. Yu, S. Wu, and L. Wang, “A convolutional click prediction model,” in
Proceedings of the 24th ACM International on Conference on Information and Knowledge Management
, ser. CIKM ’15.   New York, NY, USA: Association for Computing Machinery, 2015, p. 1743–1746. [Online]. Available:
https://doi.org/10.1145/2806416.2806603
[23]
G. Zhou, X. Zhu, C. Song, Y. Fan, H. Zhu, X. Ma, Y. Yan, J. Jin, H. Li, and K. Gai, “Deep interest network for click-through rate prediction,” in
Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, KDD 2018, London, UK, August 19-23, 2018
, Y. Guo and F. Farooq, Eds.   Beijing, China: ACM, 2018, pp. 1059–1068. [Online]. Available:
https://doi.org/10.1145/3219819.3219823
[24]
H. Li, H. Duan, Y. Zheng, Q. Wang, and Y. Wang, “A CTR prediction model based on user interest via attention mechanism,”
Appl. Intell.
, vol. 50, no. 4, pp. 1192–1203, 2020. [Online]. Available:
https://doi.org/10.1007/s10489-019-01571-9
[25]
D. R. Cox, “The regression analysis of binary sequences,”
Journal of the Royal Statistical Society Series B: Statistical Methodology
, vol. 20, no. 2, pp. 215–232, 1958.
[26]
S. Rendle, “Factorization machines,” in
ICDM 2010, The 10th IEEE International Conference on Data Mining, Sydney, Australia, 14-17 December 2010
, G. I. Webb, B. Liu, C. Zhang, D. Gunopulos, and X. Wu, Eds.   Sydney, Australia: IEEE Computer Society, 2010, pp. 995–1000. [Online]. Available:
https://doi.org/10.1109/ICDM.2010.127
[27]
F. Emmert-Streib, Z. Yang, H. Feng, S. Tripathi, and M. Dehmer, “An introductory review of deep learning for prediction models with big data,”
Frontiers Artif. Intell.
, vol. 3, p. 4, 2020. [Online]. Available:
https://doi.org/10.3389/frai.2020.00004
[28]
W. Deng, X. Ling, Y. Qi, T. Tan, E. Manavoglu, and Q. Zhang, “Ad click prediction in sequence with long short-term memory networks: an externality-aware model,” in
The 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, SIGIR 2018, Ann Arbor, MI, USA, July 08-12, 2018
, K. Collins-Thompson, Q. Mei, B. D. Davison, Y. Liu, and E. Yilmaz, Eds.   Ann Arbor, MI, USA: ACM, 2018, pp. 1065–1068. [Online]. Available:
https://doi.org/10.1145/3209978.3210071
[29]
G. Zhou, N. Mou, Y. Fan, Q. Pi, W. Bian, C. Zhou, X. Zhu, and K. Gai, “Deep interest evolution network for click-through rate prediction,” in
Proceedings of the Thirty-Third AAAI Conference on Artificial Intelligence and Thirty-First Innovative Applications of Artificial Intelligence Conference and Ninth AAAI Symposium on Educational Advances in Artificial Intelligence
, ser. AAAI’19/IAAI’19/EAAI’19.   AAAI Press, 2019. [Online]. Available:
https://doi.org/10.1609/aaai.v33i01.33015941
[30]
P. Li, R. Li, Q. Da, A. Zeng, and L. Zhang, “Improving multi-scenario learning to rank in e-commerce by exploiting task relationships in the label space,” in
CIKM ’20: The 29th ACM International Conference on Information and Knowledge Management, Virtual Event, Ireland, October 19-23, 2020
, M. d’Aquin, S. Dietze, C. Hauff, E. Curry, and P. Cudré-Mauroux, Eds.   Virtual Event, Ireland: ACM, 2020, pp. 2605–2612. [Online]. Available:
https://doi.org/10.1145/3340531.3412713
[31]
J. He, G. Mei, F. Xing, X. Yang, Y. Bao, and W. Yan, “Dadnn: Multi-scene ctr prediction via domain-aware deep neural network,” 2020.
[32]
X. Zou, Z. Hu, Y. Zhao, X. Ding, Z. Liu, C. Li, and A. Sun, “Automatic expert selection for multi-scenario and multi-task search,” in
SIGIR ’22: The 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, Madrid, Spain, July 11 - 15, 2022
, E. Amigó, P. Castells, J. Gonzalo, B. Carterette, J. S. Culpepper, and G. Kazai, Eds.   Madrid, Spain: ACM, 2022, pp. 1535–1544. [Online]. Available:
https://doi.org/10.1145/3477495.3531942
[33]
R. Caruana, “Multitask learning,”
Mach. Learn.
, vol. 28, no. 1, pp. 41–75, 1997. [Online]. Available:
https://doi.org/10.1023/A:1007379606734
[34]
Q. Zhang, X. Liao, Q. Liu, J. Xu, and B. Zheng, “Leaving no one behind: A multi-scenario multi-task meta learning approach for advertiser modeling,” in
Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining
, ser. WSDM ’22.   New York, NY, USA: Association for Computing Machinery, 2022, p. 1368–1376. [Online]. Available:
https://doi.org/10.1145/3488560.3498479
[35]
S. Tan, M. Li, W. Zhao, Y. Zheng, X. Pei, and P. Li, “Multi-task and multi-scene unified ranking model for online advertising,” in
2021 IEEE International Conference on Big Data (Big Data), Orlando, FL, USA, December 15-18, 2021
, Y. Chen, H. Ludwig, Y. Tu, U. M. Fayyad, X. Zhu, X. Hu, S. Byna, X. Liu, J. Zhang, S. Pan, V. Papalexakis, J. Wang, A. Cuzzocrea, and C. Ordonez, Eds.   Orlando, FL, USA: IEEE, 2021, pp. 2046–2051. [Online]. Available:
https://doi.org/10.1109/BigData52589.2021.9671920
[36]
X. Li, F. Yan, X. Zhao, Y. Wang, B. Chen, H. Guo, and R. Tang, “HAMUR: hyper adapter for multi-domain recommendation,” in
Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, CIKM 2023, Birmingham, United Kingdom, October 21-25, 2023
, I. Frommholz, F. Hopfgartner, M. Lee, M. Oakes, M. Lalmas, M. Zhang, and R. L. T. Santos, Eds.   Birmingham, United Kingdom: ACM, 2023, pp. 1268–1277. [Online]. Available:
https://doi.org/10.1145/3583780.3615137
[37]
J. Devlin, M. Chang, K. Lee, and K. Toutanova, “BERT: pre-training of deep bidirectional transformers for language understanding,” in
Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers)
, J. Burstein, C. Doran, and T. Solorio, Eds.   Minneapolis, MN, USA: Association for Computational Linguistics, 2019, pp. 4171–4186. [Online]. Available:
https://doi.org/10.18653/v1/n19-1423
[38]
Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, L. Zettlemoyer, and V. Stoyanov, “Roberta: A robustly optimized bert pretraining approach,” 2019.
[39]
X. Qiu, T. Sun, Y. Xu, Y. Shao, N. Dai, and X. Huang, “Pre-trained models for natural language processing: A survey,”
Science China Technological Sciences
, vol. 63, no. 10, pp. 1872–1897, 2020. [Online]. Available:
https://doi.org/10.1007/s11431-020-1647-3
[40]
P. He, X. Liu, J. Gao, and W. Chen, “Deberta: decoding-enhanced bert with disentangled attention,” in
9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021
.   Virtual Event, Austria: OpenReview.net, 2021. [Online]. Available:
https://openreview.net/forum?id=XPZIaotutsD
[41]
T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei, “Language models are few-shot learners,” in
Advances in Neural Information Processing Systems
, H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin, Eds., vol. 33.   virtual: Curran Associates, Inc., 2020, pp. 1877–1901. [Online]. Available:
https://proceedings.neurips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf
[42]
H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, and G. Lample, “Llama: Open and efficient foundation language models,” 2023.
[43]
W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang, J. Zhang, Z. Dong, Y. Du, C. Yang, Y. Chen, Z. Chen, J. Jiang, R. Ren, Y. Li, X. Tang, Z. Liu, P. Liu, J.-Y. Nie, and J.-R. Wen, “A survey of large language models,” 2023.
[44]
A. Muhamed, I. Keivanloo, S. Perera, J. Mracek, Y. Xu, Q. Cui, S. Rajagopalan, B. Zeng, and T. Chilimbi, “Ctr-bert: Cost-effective knowledge distillation for billion-parameter teacher models,” in
NeurIPS Efficient Natural Language and Speech Processing Workshop
, 2021.
[45]
A. Muhamed, J. Singh, S. Zheng, I. Keivanloo, S. Perera, J. Mracek, Y. Xu, Q. Cui, S. Rajagopalan, B. Zeng, and T. Chilimbi, “Dcaf-bert: A distilled cachable adaptable factorized model for improved ads ctr prediction,” in
Companion Proceedings of the Web Conference 2022
, ser. WWW ’22.   New York, NY, USA: Association for Computing Machinery, 2022, p. 110–115. [Online]. Available:
https://doi.org/10.1145/3487553.3524206
[46]
Z. Du, Y. Qian, X. Liu, M. Ding, J. Qiu, Z. Yang, and J. Tang, “GLM: general language model pretraining with autoregressive blank infilling,” in
Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2022, Dublin, Ireland, May 22-27, 2022
, S. Muresan, P. Nakov, and A. Villavicencio, Eds.   Dublin, Ireland: Association for Computational Linguistics, 2022, pp. 320–335. [Online]. Available:
https://doi.org/10.18653/v1/2022.acl-long.26
[47]
Z. Cui, J. Ma, C. Zhou, J. Zhou, and H. Yang, “M6-rec: Generative pretrained language models are open-ended recommender systems,” 2022.
[48]
X. Li, B. Chen, L. Hou, and R. Tang, “Ctrl: Connect collaborative and language model for ctr prediction,” 2023.
[49]
H. Wang, J. Lin, X. Li, B. Chen, C. Zhu, R. Tang, W. Zhang, and Y. Yu, “Flip: Towards fine-grained alignment between id-based models and pretrained language models for ctr prediction,” 2023.
[50]
Y. Gong, X. Ding, Y. Su, K. Shen, Z. Liu, and G. Zhang, “An unified search and recommendation foundation model for cold-start scenario,” in
Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, CIKM 2023, Birmingham, United Kingdom, October 21-25, 2023
, I. Frommholz, F. Hopfgartner, M. Lee, M. Oakes, M. Lalmas, M. Zhang, and R. L. T. Santos, Eds.   Birmingham, United Kingdom: ACM, 2023, pp. 4595–4601. [Online]. Available:
https://doi.org/10.1145/3583780.3614657
[51]
Y. Xi, W. Liu, J. Lin, X. Cai, H. Zhu, J. Zhu, B. Chen, R. Tang, W. Zhang, R. Zhang, and Y. Yu, “Towards open-world recommendation with knowledge augmentation from large language models,” 2023.
[52]
T. Man, H. Shen, X. Jin, and X. Cheng, “Cross-domain recommendation: An embedding and mapping approach,” in
Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, IJCAI 2017, Melbourne, Australia, August 19-25, 2017
, C. Sierra, Ed.   Melbourne, Australia: ijcai.org, 2017, pp. 2464–2470. [Online]. Available:
https://doi.org/10.24963/ijcai.2017/343
[53]
G. Hu, Y. Zhang, and Q. Yang, “Conet: Collaborative cross networks for cross-domain recommendation,” in
Proceedings of the 27th ACM International Conference on Information and Knowledge Management, CIKM 2018, Torino, Italy, October 22-26, 2018
, A. Cuzzocrea, J. Allan, N. W. Paton, D. Srivastava, R. Agrawal, A. Z. Broder, M. J. Zaki, K. S. Candan, A. Labrinidis, A. Schuster, and H. Wang, Eds.   Torino, Italy: ACM, 2018, pp. 667–676. [Online]. Available:
https://doi.org/10.1145/3269206.3271684
[54]
W. Zhang, P. Zhang, B. Zhang, X. Wang, and D. Wang, “A collaborative transfer learning framework for cross-domain recommendation,” in
Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD 2023, Long Beach, CA, USA, August 6-10, 2023
, A. K. Singh, Y. Sun, L. Akoglu, D. Gunopulos, X. Yan, R. Kumar, F. Ozcan, and J. Ye, Eds.   Long Beach, CA, USA: ACM, 2023, pp. 5576–5585. [Online]. Available:
https://doi.org/10.1145/3580305.3599758
[55]
X. Chen, Z. Cheng, S. Xiao, X. Zeng, and W. Huang, “Cross-domain augmentation networks for click-through rate prediction,” 2023.
[56]
Y. Sung, J. Cho, and M. Bansal, “LST: ladder side-tuning for parameter and memory efficient transfer learning,” in
Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022
, S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, Eds., New Orleans, LA, USA, 2022. [Online]. Available:
http://papers.nips.cc/paper_files/paper/2022/hash/54801e196796134a2b0ae5e8adef502f-Abstract-Conference.html
[57]
F. Murtagh, “Multilayer perceptrons for classification and regression,”
Neurocomputing
, vol. 2, no. 5, pp. 183–197, 1990. [Online]. Available:
https://doi.org/10.1016/0925-2312(91)90023-5
[58]
V. Mnih, N. Heess, A. Graves, and K. Kavukcuoglu, “Recurrent models of visual attention,” in
Advances in Neural Information Processing Systems 27: Annual Conference on Neural Information Processing Systems 2014, December 8-13 2014, Montreal, Quebec, Canada
, Z. Ghahramani, M. Welling, C. Cortes, N. D. Lawrence, and K. Q. Weinberger, Eds., Montreal, Quebec, Canada, 2014, pp. 2204–2212. [Online]. Available:
https://proceedings.neurips.cc/paper/2014/hash/09c6c3783b4a70054da74f2538ed47c6-Abstract.html
[59]
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” in
Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA
, I. Guyon, U. von Luxburg, S. Bengio, H. M. Wallach, R. Fergus, S. V. N. Vishwanathan, and R. Garnett, Eds.   Long Beach, CA, USA: Curran Associates Inc., 2017, pp. 5998–6008. [Online]. Available:
https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
[60]
R. Girdhar and D. Ramanan, “Attentional pooling for action recognition,” in
Advances in Neural Information Processing Systems
, I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, Eds., vol. 30.   Long Beach, CA, USA: Curran Associates, Inc., 2017. [Online]. Available:
https://proceedings.neurips.cc/paper_files/paper/2017/file/67c6a1e7ce56d3d6fa748ab6d9af3fd7-Paper.pdf
[61]
R. Caruana, “Multitask learning,”
Mach. Learn.
, vol. 28, no. 1, pp. 41–75, 1997. [Online]. Available:
https://doi.org/10.1023/A:1007379606734
[62]
J. Ni, J. Li, and J. J. McAuley, “Justifying recommendations using distantly-labeled reviews and fine-grained aspects,” in
Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing, EMNLP-IJCNLP 2019, Hong Kong, China, November 3-7, 2019
, K. Inui, J. Jiang, V. Ng, and X. Wan, Eds.   Hong Kong, China: Association for Computational Linguistics, 2019, pp. 188–197. [Online]. Available:
https://doi.org/10.18653/v1/D19-1018
[63]
X. Li, B. Chen, H. Guo, J. Li, C. Zhu, X. Long, S. Li, Y. Wang, W. Guo, L. Mao, J. Liu, Z. Dong, and R. Tang, “Inttower: The next generation of two-tower model for pre-ranking system,” in
Proceedings of the 31st ACM International Conference on Information & Knowledge Management, Atlanta, GA, USA, October 17-21, 2022
, M. A. Hasan and L. Xiong, Eds.   Atlanta, GA, USA: ACM, 2022, pp. 3292–3301. [Online]. Available:
https://doi.org/10.1145/3511808.3557072
[64]
X. Ma, L. Zhao, G. Huang, Z. Wang, Z. Hu, X. Zhu, and K. Gai, “Entire space multi-task model: An effective approach for estimating post-click conversion rate,” in
The 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, SIGIR 2018, Ann Arbor, MI, USA, July 08-12, 2018
, K. Collins-Thompson, Q. Mei, B. D. Davison, Y. Liu, and E. Yilmaz, Eds.   Ann Arbor, MI, USA: ACM, 2018, pp. 1137–1140. [Online]. Available:
https://doi.org/10.1145/3209978.3210104
[65]
K. Gai, X. Zhu, H. Li, K. Liu, and Z. Wang, “Learning piece-wise linear models from large scale data for ad click prediction,” 2017.
[66]
G. Zhou, X. Zhu, C. Song, Y. Fan, H. Zhu, X. Ma, Y. Yan, J. Jin, H. Li, and K. Gai, “Deep interest network for click-through rate prediction,” in
Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, KDD 2018, London, UK, August 19-23, 2018
, Y. Guo and F. Farooq, Eds.   London, UK: ACM, 2018, pp. 1059–1068. [Online]. Available:
https://doi.org/10.1145/3219819.3219823
[67]
L. Yan, W. Li, G. Xue, and D. Han, “Coupled group lasso for web-scale CTR prediction in display advertising,” in
Proceedings of the 31th International Conference on Machine Learning, ICML 2014, Beijing, China, 21-26 June 2014
, ser. JMLR Workshop and Conference Proceedings, vol. 32.   Beijing, China: JMLR.org, 2014, pp. 802–810. [Online]. Available:
http://proceedings.mlr.press/v32/yan14.html
[68]
W. Song, C. Shi, Z. Xiao, Z. Duan, Y. Xu, M. Zhang, and J. Tang, “Autoint: Automatic feature interaction learning via self-attentive neural networks,” in
Proceedings of the 28th ACM International Conference on Information and Knowledge Management, CIKM 2019, Beijing, China, November 3-7, 2019
, W. Zhu, D. Tao, X. Cheng, P. Cui, E. A. Rundensteiner, D. Carmel, Q. He, and J. X. Yu, Eds.   Beijing, China: ACM, 2019, pp. 1161–1170. [Online]. Available:
https://doi.org/10.1145/3357384.3357925
[69]
Q. Shen, W. Tao, J. Zhang, H. Wen, Z. Chen, and Q. Lu, “Sar-net: A scenario-aware ranking network for personalized fair recommendation in hundreds of travel scenarios,” in
CIKM ’21: The 30th ACM International Conference on Information and Knowledge Management, Virtual Event, Queensland, Australia, November 1 - 5, 2021
, G. Demartini, G. Zuccon, J. S. Culpepper, Z. Huang, and H. Tong, Eds.   Virtual Event, Queensland, Australia: ACM, 2021, pp. 4094–4103. [Online]. Available:
https://doi.org/10.1145/3459637.3481948
[70]
W. Guo, C. Zhu, F. Yan, B. Chen, W. Liu, H. Guo, H. Zheng, Y. Liu, and R. Tang, “DFFM: domain facilitated feature modeling for CTR prediction,” in
Proceedings of the 32nd ACM International Conference on Information and Knowledge Management, CIKM 2023, Birmingham, United Kingdom, October 21-25, 2023
, I. Frommholz, F. Hopfgartner, M. Lee, M. Oakes, M. Lalmas, M. Zhang, and R. L. T. Santos, Eds.   Birmingham, United Kingdom: ACM, 2023, pp. 4602–4608. [Online]. Available:
https://doi.org/10.1145/3583780.3615469
[71]
M. Xia, T. Gao, Z. Zeng, and D. Chen, “Sheared llama: Accelerating language model pre-training via structured pruning,” 2023.
[72]
N. Srivastava, G. E. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, “Dropout: a simple way to prevent neural networks from overfitting,”
J. Mach. Learn. Res.
, vol. 15, no. 1, pp. 1929–1958, 2014. [Online]. Available:
https://dl.acm.org/doi/10.5555/2627435.2670313
[73]
A. Krogh and J. Hertz, “A simple weight decay can improve generalization,” in
Advances in Neural Information Processing Systems
, J. Moody, S. Hanson, and R. Lippmann, Eds., vol. 4.   Denver, Colorado, USA: Morgan-Kaufmann, 1991. [Online]. Available:
https://proceedings.neurips.cc/paper_files/paper/1991/file/8eefcfdf5990e441f0fb6f3fad709e21-Paper.pdf
[74]
D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in
3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings
, Y. Bengio and Y. LeCun, Eds.   San Diego, CA, USA: OpenReview.net, 2015. [Online]. Available:
http://arxiv.org/abs/1412.6980
[75]
E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, “Lora: Low-rank adaptation of large language models,” in
The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022
.   Virtual Event: OpenReview.net, 2022. [Online]. Available:
https://openreview.net/forum?id=nZeVKeeFYf9
[76]
J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei, “Scaling laws for neural language models,” 2020.
[77]
X. Jiao, Y. Yin, L. Shang, X. Jiang, X. Chen, L. Li, F. Wang, and Q. Liu, “TinyBERT: Distilling BERT for natural language understanding,” in
Findings of the Association for Computational Linguistics: EMNLP 2020
, T. Cohn, Y. He, and Y. Liu, Eds.   Online: Association for Computational Linguistics, Nov. 2020, pp. 4163–4174. [Online]. Available:
https://aclanthology.org/2020.findings-emnlp.372
[78]
P. He, J. Gao, and W. Chen, “Debertav3: Improving deberta using electra-style pre-training with gradient-disentangled embedding sharing,” in
The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023
.   Kigali, Rwanda: OpenReview.net, 2023. [Online]. Available:
https://openreview.net/pdf?id=sE7-XhLxHA
[79]
L. van der Maaten and G. Hinton, “Visualizing data using t-sne,”
Journal of Machine Learning Research
, vol. 9, no. 86, pp. 2579–2605, 2008. [Online]. Available:
http://jmlr.org/papers/v9/vandermaaten08a.html
[80]
G. Jawahar, B. Sagot, and D. Seddah, “What does BERT learn about the structure of language?” in
Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics
, A. Korhonen, D. Traum, and L. Màrquez, Eds.   Florence, Italy: Association for Computational Linguistics, Jul. 2019, pp. 3651–3657. [Online]. Available:
https://aclanthology.org/P19-1356
[81]
A. Rogers, O. Kovaleva, and A. Rumshisky, “A primer in bertology: What we know about how bert works,”
Transactions of the Association for Computational Linguistics
, vol. 8, pp. 842–866, 2021.