---
source: Alquier, P. (2024). User-friendly Introduction to PAC-Bayes Bounds. Foundations and Trends in Machine Learning, 17(2), 174-303. arXiv:2110.11216
author: Pierre Alquier
date: 2021-10-21
type: paper
quality: secondary
stance: neutral
---


arXiv:2110.11216v6 [stat.ML] 28 Feb 2025

User-friendly Introduction to
PAC-Bayes Bounds
Suggested Citation: Pierre Alquier (2024), “User-friendly Introduction to PAC-Bayes
Bounds”, : Vol. 17, No. 2, pp 174–303. DOI: 10.1561/2200000100.

Pierre Alquier
ESSEC Business School
pierre.alquier.stat@gmail.com

This article may be used only for the purpose of research, teaching,
and/or private study. Commercial use or systematic downloading (by
robots or other automatic processes) is prohibited without explicit
Publisher approval.

Boston — Delft

Contents

1 Introduction
176
1.1 Machine Learning and PAC Bounds . . . . . . . . . . . . . 177
1.2 What are PAC-Bayes Bounds? . . . . . . . . . . . . . . . 183
1.3 Why this Tutorial? . . . . . . . . . . . . . . . . . . . . . . 186
1.4 Two Types of PAC Bounds, Organization of these Notes . 187
2 First Step in the PAC-Bayes World
190
2.1 A Simple PAC-Bayes Bound . . . . . . . . . . . . . . . . . 190
2.2 PAC-Bayes Bound on Aggregation of Predictors and
Weighted Majority Vote . . . . . . . . . . . . . . . . . . . 204
2.3 PAC-Bayes Bound on a Single Draw from the Posterior . . 205
2.4 Bound in Expectation . . . . . . . . . . . . . . . . . . . . 206
2.5 Applications of Empirical PAC-Bayes Bounds . . . . . . . . 208
3 Tight and Non-vacuous PAC-Bayes Bounds
210
3.1 Why is there a Race to Tighter PAC-Bayes Bound? . . . . 210
3.2 A Few PAC-Bayes Bounds . . . . . . . . . . . . . . . . . . 212
3.3 Tight Generalization Error Bounds for Deep Learning . . . 225
4 PAC-Bayes Oracle Inequalities and Fast Rates
231
4.1 From Empirical Inequalities to Oracle Inequalities . . . . . 231
4.2 Bernstein Assumption and Fast Rates . . . . . . . . . . . 235

4.3 Applications of Theorem 4.3 . . . . . . . . . . . . . . . . 241
4.4 Dimension and Rate of Convergence . . . . . . . . . . . . 244
4.5 Getting Rid of the log Terms: Catoni’s Localization Trick . 247
5 Beyond “Bounded Loss” and “i.i.d. Observations”
253
5.1 “Almost” Bounded Losses (Sub-Gaussian and Sub-gamma) 254
5.2 Heavy-tailed Losses . . . . . . . . . . . . . . . . . . . . . 256
5.3 Dependent Observations . . . . . . . . . . . . . . . . . . 260
5.4 Other Non i.i.d. Settings . . . . . . . . . . . . . . . . . . 262
6 Related Approaches in Statistics and Machine Learning
Theory
264
6.1 Bayesian Inference in Statistics . . . . . . . . . . . . . . . 264
6.2 Empirical Risk Minimization . . . . . . . . . . . . . . . . . 269
6.3 Non-Bayesian Estimators . . . . . . . . . . . . . . . . . . 270
6.4 Online Learning . . . . . . . . . . . . . . . . . . . . . . . 270
6.5 Aggregation of Estimators in Statistics . . . . . . . . . . . 273
6.6 Information Theoretic Approaches . . . . . . . . . . . . . 274
7 Conclusion

279

Acknowledgements

280

References

281

User-friendly Introduction to
PAC-Bayes Bounds
Pierre Alquier
ESSEC Business School, Asia-Pacific Campus, Singapore;
pierre.alquier.stat@gmail.com

ABSTRACT
Aggregated predictors are obtained by making a set of basic
predictors vote according to some weights, that is, to some
probability distribution. Randomized predictors are obtained
by sampling in a set of basic predictors, according to some
prescribed probability distribution.
Thus, aggregated and randomized predictors have in common that their definition rely on a probability distribution on
the set of predictors. In statistical learning theory, there is a
set of tools designed to understand the generalization ability
of such predictors: PAC-Bayesian or PAC-Bayes bounds.
Since the original PAC-Bayes bounds (Shawe-Taylor and
Williamson, 1997; McAllester, 1998), these tools have been
considerably improved in many directions. We will for example describe a simplified version of the localization technique (Catoni, 2003; Catoni, 2007) that was missed by the
community, and later rediscovered as “mutual information
bounds”. Very recently, PAC-Bayes bounds received a considerable attention. There was workshop on PAC-Bayes at
NIPS 2017, (Almost) 50 Shades of Bayesian Learning: PACBayesian trends and insights, organized by B. Guedj, F.
Bach and P. Germain. One of the reasons of this recent interest is the successful application of these bounds to neural
Pierre Alquier (2024), “User-friendly Introduction to PAC-Bayes Bounds”, : Vol. 17,
No. 2, pp 174–303. DOI: 10.1561/2200000100.
©2024 P. Alquier

175
networks (Dziugaite and Roy, 2017). Since then, this is a
recurring topic of workshops in the major machine learning
conferences.
The objective of these notes is to provide an elementary
introduction to PAC-Bayes bounds.

1
Introduction

In a supervised learning problem, such as classification or regression,
we are given a data set, and we 1) fix a set of predictors and 2) find a
good predictor in this set.
For example, when doing linear regression, you 1) chose to consider
only linear predictors and 2) use the least-square method to chose your
linear predictor.
In this tutorial, we will rather focus on “randomized” or “aggregated”
predictors. By this, we mean that we will replace 2) by 2’) define weights
on the predictors and make them vote according to these weights or by 2”)
draw a predictor according to some prescribed probability distribution.
In this first section, we will introduce the main concepts of machine
learning theory, and their mathematical notations. We will briefly introduce PAC bounds, that allow to control the generalization error of
a predictor. These tools will allow to formalize properly the notion of
“randomized” or “aggregated” predictors, and to introduce PAC-Bayes
bounds.

176

1.1. MACHINE LEARNING AND PAC BOUNDS
1.1
1.1.1

177

Machine Learning and PAC Bounds
Machine learning: notations

In a supervised learning problem, the objective is to learn from examples
to assign labels to objects. Objects can be images, videos, e-mails... The
set of all possible objects will be denoted by X . In all the examples
we mentioned, it is possible to encode the objects by (large enough)
vectors, and thus, we will often have X ⊆ Rd , where R is the set of real
numbers. The set of labels will be denoted by Y.
The most classical examples of supervised learning problems are
binary classification and regression. In binary classification, Y = {0, 1}.
Examples includes spam detection: in this case, objects in X are e-mails,
and the label is 1 if the e-mail is a spam, and 0 otherwise. In regression,
labels can be any real number Y = R. This is the case when we try to
predict a numerical quantity such as CO2 emissions, temperature, etc.
A predictor is a function f : X → Y: for each object x, it returns a
label f (x). We are usually interested in parametric sets of predictors.
That is, we consider {fθ , θ ∈ Θ} where Θ is any set, called the parameter
set, and each fθ is a predictor. For example, in linear regression, a
common set of predictors is fθ (x) = ⟨x, θ⟩ ∈ Y = R, with X = Θ = Rd .
In classification, we can define with the same X and Θ,
(

fθ (x) =

1 if ⟨x, θ⟩ ≥ 0,
0 otherwise.

Other examples include neural networks with a fixed architecture, θ
being the weights of the network. Predictors are sometimes refered to
as classifiers in the classification setting, and as regressors in regression.
Assume now that a pair label-object, (x, y) ∈ X × Y, is given. A
predictor f will propose a prediction f (x) of the label y. If f (x) = y, the
predictor f predicts the label correctly, otherwise, it makes a mistake.
In order to quantify how serious a mistake is, we usually measure it
by a loss function. In these notes, a loss function can be any function
ℓ : Y 2 → [0, +∞) such that ℓ(y, y) = 0 for any y ∈ Y; ℓ(f (x), y) will
be interpreted as the cost of the prediction error. In classification, the
most natural loss function is:

178

Introduction
(
′

ℓ(y , y) =

1 if y ′ ̸= y,
0 if y ′ = y.

We will refer to it as the 0-1 loss function, and will use the following
shorter notation: ℓ(y ′ , y) = 1(y ̸= y ′ ). For computational reasons,
it is more convenient to use convex loss functions. For example, in
binary classification: ℓ(y ′ , y) = max(1 − yy ′ , 0) (the hinge loss). In
regression problems, the most popular examples are ℓ(y ′ , y) = (y ′ − y)2
the quadratic loss, or ℓ(y ′ , y) = |y ′ − y| the absolute loss. The original
PAC-Bayes bounds of McAllester (1998) were stated in the special case
of the 0-1 loss, and this is also the case of most bounds published since
then. However, we will see in Section 3 that their extension to any
bounded loss is direct. Some PAC-Bayes bounds for regression with the
quadratic loss were proven for example by Catoni (2004). From now,
and until the end of Section 4, we assume that 0 ≤ ℓ ≤ C. This
is typically the case in classification with the 0-1 loss, or in regression
with quadratic loss under the additional assumption that fθ (x) and
y are bounded. We will discuss how to get rid of this assumption in
Section 5.
Assume we want to build a machine to predict the label of objects
it will encounter in the future. Of course, we don’t know these objects
in advance, nor their labels. A way to model this uncertainty is to
assume that a future pair object-label is a random variable (X, Y )
taking values in X × Y. Let P denote the probability distribution1 of
(X, Y ). The expected prediction mistake is thus E(X,Y )∼P [ℓ(f (X), Y )].
This is usually refered to as the (generalization) risk of f . As it is a
very important notion in machine learning, we introduce the notation
R(f ) = E(X,Y )∼P [ℓ(f (X), Y )].
As we will focus on predictors in {fθ , θ ∈ Θ}, we define
R(θ) := R(fθ )
1

Formally, we can only define a probability distribution on X × Y if it is equipped
with a σ-algebra. Let B be such a σ-algebra. Essentially, the only thing that matters
is that the loss function ℓ and the predictors fθ (·) are measurable functions, which is
satisfied by all classical examples. Note that B will no longer appear explicitly in
this tutorial.

1.1. MACHINE LEARNING AND PAC BOUNDS

179

for short. A good strategy would be to implement in our machine a
predictor fθ such that R(θ) is as small as possible – ideally, we should
implement fθ∗ where R(θ∗ ) = inf θ∈Θ R(θ), if this infimum is reached.
Unfortunately, there is a major difficulty: we don’t know the distribution
P of (X, Y ) in practice. Check the examples above: we are not able to
describe the probability distribution of images we will see in the future,
or of e-mails we will receive.
Instead, we will train our machine based on examples. That is, we
assume that we can access a sample of pairs object-label, that we will call
the data, or the observations: (X1 , Y1 ), . . . , (Xn , Yn ). From now, and
until the end of Section 4, we assume that (X1 , Y1 ), . . . , (Xn , Yn )
are i.i.d. from P . That is, they are “typical examples” of the pairs
object-label the machine will have to deal with in the future. For short,
we put ℓi (θ) := ℓ(fθ (Xi ), Yi ) ≥ 0. We define the empirical risk:
r(θ) =

n
1X
ℓi (θ).
n i=1

Note that it satisfies
E(X1 ,Y1 ),...,(Xn ,Yn ) [r(θ)] = R(θ).
The notation for the previous expectation is cumbersome. From now,
we will write S = [(X1 , Y1 ), . . . , (Xn , Yn )] and ES (for “expectation with
respect to the sample”) instead of E(X1 ,Y1 ),...,(Xn ,Yn ) . In the same way,
we will write PS for probabilities with respect to the sample.
Finally, an estimator is a function that takes a sample of pairs
object-labels of any size and returns a guess for the parameter θ we
should use for future predictions. Formally,2
θ̂ :

∞
[

(X × Y)n → Θ.

n=1

For short, we write θ̂ instead of θ̂((X1 , Y1 ), . . . , (Xn , Yn )). The most
famous example is the Empirical Risk Minimizer, or ERM:
θ̂ERM = argmin r(θ)
θ∈Θ

(when this minimizer exists and is unique).
2

The proper definition also requires θ̂ to be a measurable function of the observations, so that probabilities of events involving θ̂ are well defined. This is not so
important here as we will soon replace the notion of estimator with a new notion.

180

Introduction

1.1.2

PAC bounds

Of course, our objective is to minimize R, not r. So the ERM strategy
is motivated by the hope that these two functions are not so different,
so that the minimizer of r almost minimizes R. Let us now discuss to
what extent this is true. By doing so, we will introduce some tools that
will be also useful for PAC-Bayes bounds.
Proposition 1.1. For any θ ∈ Θ, for any δ ∈ (0, 1),
s



PS R(θ) > r(θ) + C



log 1δ
 ≤ δ.
2n

(1.1)

The proof relies on a result that will be useful in all this tutorial.
Lemma 1.1 (Hoeffding’s inequality). Let U1 , . . . , Un be independent
random variables taking values in an interval [a, b]. Then, for any t > 0,
h Pn

E et

i=1

[Ui −E(Ui )]

i

≤e

nt2 (b−a)2
8

.

Hoeffding’s inequality is proven for example in Chapter 2 of Boucheron et al. (2013), which is a highly recommended reading, but it is
so classical that you can as well find it on Wikipedia.
Proof of Proposition 1.1. Apply Lemma 1.1 to Ui = E[ℓi (θ)] − ℓi (θ):
i

h

ES etn[R(θ)−r(θ)] ≤ e

nt2 C 2
8

(1.2)

.

Now, for any s > 0,


PS (R(θ) − r(θ) > s) = PS ent[R(θ)−r(θ)] > ents
h

≤

ES ent[R(θ)−r(θ)]

≤e

i

ents

nt2 C 2
−nts
8



by Markov’s inequality,

by (1.2).

In other words,
PS (R(θ) > r(θ) + s) ≤ e

nt2 C 2
−nts
8

.

1.1. MACHINE LEARNING AND PAC BOUNDS

181

We can make this bound as tight as possible, by optimizing our choice
for t. Indeed, nt2 C 2 /8 − nts is minimized for t = 4s/C 2 , which gives
−2ns2

PS (R(θ) > r(θ) + s) ≤ e C 2 .

(1.3)

This means that, for a given θ, the empirical risk r(θ) cannot be much
smaller than the risk R(θ). The order of this “much smaller” can be
better understood by introducing
−2ns2

δ = e C2

and substituting δ to s in (1.3), which gives (1.1).
Proposition 1.1 states that R(θ) will usually not exceed r(θ) by more
√
than a term in 1/ n. This is not enough, though, to justify the use of
the ERM. Indeed, (1.1) is only true for the θ that was fixed above, and
we cannot apply it to θ̂ERM that is a function of the data.
The usual approach to control R(θ̂ERM ) is to use the inequality
R(θ̂ERM ) − r(θ̂ERM ) ≤ sup [R(θ) − r(θ)] ,
θ∈Θ

(1.4)

and to prove a version of (1.1) that would hold uniformly on Θ. As an
illustration of this method, we prove the following result.
Theorem 1.2. Assume that card(Θ) = M < +∞. For any δ ∈ (0, 1),
s



PS R(θ̂ERM ) ≤ inf r(θ) + C
θ∈Θ



log M
δ 
≥ 1 − δ.
2n

Proof. As announced before the statement of the theorem, we upper
bound the supremum in (1.4):


PS (sup[R(θ) − r(θ)] > s) = PS 
θ∈Θ


o
[R(θ) − r(θ)] > s 

[n

θ∈Θ

≤

X

PS (R(θ) > r(θ) + s)

θ∈Θ
−2ns2

≤ M e C2

(1.5)

182

Introduction
−2ns2

thanks to (1.3). This time, put δ = M e C 2

s



PS sup[R(θ) − r(θ)] > C
θ∈Θ

and plug into (1.5) to get:


log M
δ 
≤ δ.
2n

Thus, the complementary event satisfies
s



PS sup[R(θ) − r(θ)] ≤ C
θ∈Θ



log M
δ 

≥ 1 − δ.

s



2n

(1.6)

From (1.4),


PS R(θ̂ERM ) ≤ r(θ̂ERM ) + C

log M
δ 
≥1−δ
2n

and note that, as Θ is finite, r(θ̂ERM ) = inf θ∈Θ r(θ).
Bounds in the form of Theorem 1.2 are called Probably Approximately Correct (PAC) bounds, because r(θ̂ERM ) approximates R(θ̂ERM )
p
within C log(M/δ)/2n with probability 1 − δ. This terminology was
introduced by Valiant (1984).
Remark 1.1. The proofs of Proposition 1.1 and Theorem 1.2 used, in
addition to Hoeffding’s inequality, two tricks that we will reuse very
often when we will prove PAC-Bayes bounds:
• given a random variable U and s ∈ R, for any t > 0,






P (U > s) = P etU > ets ≤

E etU



ets

thanks to Markov inequality. The combo “exponential + Markov
inequality” is known as Chernoff’s bounding technique. It is
is of course very useful together with exponential inequalities like
Hoeffding’s inequality.

1.2. WHAT ARE PAC-BAYES BOUNDS?

183

• given a finite number of random variables U1 , . . . , UM ,


!

P

sup Ui > s

1≤i≤M

= P


o
Ui > s 

[ n
1≤i≤M

≤

M
X

P (Ui > s) .

i=1

This argument is called the union-bound argument.
The next step in the study of the ERM would be to go beyond finite
sets Θ. The union bound argument has to be modified in this case, and
things become a little more complicated. We will therefore stop here
the study of the ERM: it is not our objective anyway.
If the reader is interested by the study of the ERM in general:
Vapnik and Chervonenkis (1968) developed the theoretical tools for
this study, see the more recent monograph by Vapnik (1998). We
refer the reader to Devroye et al. (1996) for a beautiful and very
pedagogical introduction to machine learning theory. Chapters 11 and
12 in particular are dedicated to Vapnik and Chervonenkis theory. More
recent references include Giraud (2014) and Wainwright (2019).
1.2

What are PAC-Bayes Bounds?

We are now in better position to explain what are PAC-Bayes bounds.
A simple way to phrase things: PAC-Bayes bounds are generalization of
the union bound argument, that will allow to deal with any parameter
set Θ: finite or infinite, continuous... However, a byproduct of this
technique is that we will have to change the notion of estimator.
Definition 1.1. Let P(Θ) be the set of all probability distributions on
Θ equipped with a σ-algebra T . A data-dependent probability measure
is a function:
∞
ρ̂ :

[

(X × Y)n → P(Θ)

n=1

184

Introduction

with a suitable measurability condition.3 We will write ρ̂ instead of
ρ̂((X1 , Y1 ), . . . , (Xn , Yn )) for short.
In practice, when you have a data-dependent probability measure,
and you want to build a predictor, you can:
• draw a random parameter θ̃ ∼ ρ̂, we will call this procedure
“randomized estimator”.
• use it to average predictors, that is, define a new predictor:
fρ̂ (·) = Eθ∼ρ̂ [fθ (·)]
called the aggregated predictor with weights ρ̂.
So, with PAC-Bayes bounds, we will extend the union bound argument4 to infinite, uncountable sets Θ, but we will obtain bounds on
various risks related to data-dependent probability measures, that is:
• the risk of a randomized estimator, R(θ̃),
• or the average risk of randomized estimators, Eθ∼ρ̂ [R(θ)],
• or the risk of the aggregated estimator, R(fρ̂ ).
From a technical point of view, the analysis shares many similarities
with the analysis of the ERM in the previous section. A key difference
is that the supremum in (1.4) will be replaced by
Eθ∼ρ̂ [R(θ) − r(θ)] ≤ sup Eθ∼ρ [R(θ) − r(θ)].
ρ∈P(Θ)

While this might look unnecessarily complicated at first sight, PACBayes bounds will actually turn out to be extremely convenient for
many reasons that we hope will become clear along the next sections:
3
I don’t want to scare the reader with measurability conditions, as I will not
check them in this tutorial anyway. Here, the exact condition to ensure that what
follows is well defined is that for any A ∈ T , the function

((x1 , y1 ), . . . , (xn , yn )) 7→ [ρ̂((x1 , y1 ), . . . , (xn , yn ))] (A)
is measurable. That is, ρ̂ is a regular conditional probability.
4
See the title of van Erven’s tutorial (van Erven, 2014): “PAC-Bayes mini-tutorial:
a continuous union bound”. Note, however, that it is argued by Catoni (2007) that
PAC-Bayes bounds are actually more than that, we will come back to this in Section 4.

1.2. WHAT ARE PAC-BAYES BOUNDS?

185

• first, they don’t require the set of predictors to be finite, nor
discrete. Of course, it is also possible to prove PAC bounds for
the ERM when Θ ⊂ Rp is not finite, but this leads to technical difficulties or strong restrictions such as the compactness of
Θ. PAC-Bayes bounds do not lead to major difficulties with unbounded parameter spaces, as will be illustrated in Example 3.2.
• randomized estimators are fairly common in machine learning.
This includes Bayesian estimation and related methods such as
variational inference and ensemble methods. Section 2 illustrates
how PAC-Bayes bounds can be applied to such estimators. Moreover, many non-randomized estimators can be derived from randomized ones: aggregation rules, majority vote classifiers, etc. The
PAC-Bayes bounds on the randomized estimator often brings
strong information on the de-randomized version. This will also
be discussed thoroughly and illustrated in Section 2.
• Bayesian estimators incorporate prior knowledge through a prior
distribution π on Θ. Even though PAC-Bayes bounds can be
applied to non-Bayesian estimators, a prior π will still appear in
the bound. The effect of π on the bound will be discussed thoroughly. In particular, PAC-Bayes bounds depend not only on the
minimum of the empirical risk r(θ), but on the prior probability
of the level sets of r: in general, this can be quantified through
the so-called prior-mass condition, as described in Section 4, even
though specific examples such as Example 2.1 will already illustrate this property. A consequence is that flater minima lead to
tigther bounds. This is one of the reasons why PAC-Bayes bounds
can be tight for deep learning (Section 3).
You will of course ask the question: if Θ is infinite, what will the log(M )
term be replaced with? In PAC-Bayes bounds, this term will be replaced
by the Kullback-Leibler divergence between ρ and a fixed π on Θ (the
prior).

186

Introduction

Definition 1.2. Given two probability measures µ and ν in P(Θ), the
Kullback-Leibler (or simply
between µ and ν is

Z KL) divergence
dµ
KL(µ∥ν) = log
(θ) µ(dθ) ∈ [0, +∞]
dν
5
if µ has a density dµ
dν with respect to ν, and KL(µ∥ν) = +∞ otherwise.

Example 1.1. For example, if Θ is finite,
µ(θ)
KL(µ∥ν) =
log
µ(θ).
ν(θ)
θ∈Θ
X





The following result is well known. You can prove it using Jensen’s
inequality.
Proposition 1.2. For any probability measures µ and ν, KL(µ∥ν) ≥ 0
with equality if and only if µ = ν.
1.3

Why this Tutorial?

Since the “PAC analysis of a Bayesian estimator” by Shawe-Taylor
and Williamson (1997) and the first PAC-Bayes bounds proven by McAllester (1998) and McAllester (1999), many new PAC-Bayes bounds
appeared (we will see that some of them can be derived from a bound
due to Seeger, 2002). These bounds were used in various contexts, to
solve a wide range of problems. This led to hundreds of (beautiful!)
papers. The consequence of this is that it’s quite difficult to be aware of
all the existing work on PAC-Bayes bounds. In particular, it seems that
many powerful techniques in Catoni’s book (Catoni, 2007) and earlier
works (Catoni, 2003; 2004) are largely ignored by the community.
On the other hand, it’s not easy to enter into the PAC-Bayes
literature. Most papers already assume some basic knowledge on these
bounds, and Catoni’s book is quite technical to begin with. The objective
5

We recall that if there is a measurable function g such that for any measurable
set A,
Z
µ(A) =

g(θ)ν(dθ),
A

then this function is essentially unique. We put dµ
(θ) = g(θ) and refer to this
dν
function as the density of µ with respect to ν.

1.4. TWO TYPES OF PAC BOUNDS, ORGANIZATION OF THESE
NOTES
187
of these notes is thus to provide a user-friendly introduction, accessible
to PhD students, that could be used as a first approach to PAC-Bayes
bounds. It also provides references for more sophisticated results.
I want to mention existing short introduction to PAC-Bayes bounds,
like the ones by McAllester (2013) and van Erven (2014) and the nice
introductory slides of Fleuret (2011). They are very informative, and
I recommend the reader to check them. However, they are focused on
empirical bounds only. There are also surveys on PAC-Bayes bounds,
such as Chopin et al. (2015, Section 5) or Guedj (2019). These papers
are very useful to navigate in the ocean of publications on PAC-Bayes
bounds, and they helped me a lot when I was writing this document,
but might not provide enough detail for a first reading on the topic.
Finally, in order to highlight the main ideas, I will not necessarily try
to present the bounds with the tightest possible constants. In particular,
many oracle bounds and localized bounds in Section 4 were introduced
in Catoni (2003; 2007) with better constants. Once again, this is an
introduction to PAC-Bayes bounds. I strongly recommend the reader to
check the original publications for more accurate results.
1.4

Two Types of PAC Bounds, Organization of these Notes

It is important to make a distinction between two types of PAC bounds.
Theorem 1.2 is usually refered to as an empirical bound. It means
that, for any θ, R(θ) is upper bounded by an empirical quantity, that
is, by something that we can compute when we observe the data. This
allows to study the ERM as the minimizer of this bound. It also provides
a numerical certificate of the generalization error of the ERM. You will
really end up with something like




PS R(θ̂ERM ) ≤ 0.12 ≥ 0.99.
However, a numerical certificate on the generalization error does
not tell you one thing. Can this 0.12 be improved using a larger sample
size? Or is it the best that can be done with our set of predictors? The
right tools to answer these questions are excess risk bounds, also known
as oracle PAC 
bounds. In these bounds, you have
 a control of the form
PS R(θ̂ERM ) ≤ inf R(θ) + rn (δ) ≥ 1 − δ,
θ∈Θ

188

Introduction

where the remainder rn (δ) should be as small as possible and satisfy
rn (δ) → 0 when n → ∞. Of course, the upper bound on R(θ̂ERM )
cannot be computed because R is unknown in practice, so it doesn’t
lead to a numerical certificate on R(θ̂ERM ). Still, these bounds are very
interesting, because they tell you how close you can expect R(θ̂ERM ) to
be to the smallest possible value of R.
In the same way, there are empirical PAC-Bayes bounds, and oracle
PAC-Bayes bounds (also known as excess-risk PAC-Bayes bounds). The
very first PAC-Bayes bounds by McAllester (1998) and McAllester
(1999) were empirical bounds. The first oracle PAC-Bayes bounds came
later (Catoni, 2003; Catoni, 2004; Zhang, 2006; Catoni, 2007).
In some sense, empirical PAC-Bayes bounds are more useful in
practice, and oracle PAC-Bayes bounds are theoretical objects. But
this might be an oversimplification. We will see that empirical bounds
are tools used to prove some oracle bounds, so they are also useful in
theory. On the other hand, when we design a data-dependent probability
measure, we don’t know if it will lead to large or small empirical bounds.
A preliminary study of its theoretical properties through an oracle
bound is the best way to ensure that it is efficient, and so that it has a
chance to lead to small empirical bounds.
In Section 2, we will study an example of empirical PAC-Bayes
bound, essentially taken from a preprint by Catoni (2003). We will
prove it together, play with it and modify it in many ways. In Section 3,
we cover many empirical PAC-Bayes bounds, and explain the race to
tighter bounds. This led to bounds that are tight enough to provide
good generalization certificates for deep learning, we will discuss this
based on Dziugaite and Roy’s paper (Dziugaite and Roy, 2017) and
a more recent work by Pérez-Ortiz, Rivasplata, Shawe-Taylor, and
Szepesvàri (Pérez-Ortiz et al., 2021).
In Section 4, we will turn to oracle PAC-Bayes bounds. We will see
how to derive these bounds from empirical bounds, and apply them to
some classical set of predictors. We will examine the assumptions leading
to fast rates in these inequalities. Section 5 will be devoted to the various
attempts to extend PAC-Bayes bounds beyond the setting introduced in
this introduction, that is: bounded loss, and i.i.d. observations. Finally,
in Section 6 we will discuss briefly the connection between PAC-Bayes

1.4. TWO TYPES OF PAC BOUNDS, ORGANIZATION OF THESE
NOTES
189
bounds and many other approaches in machine learning and statistics,
including regret bounds and Mutual Information bounds (MI).

2
First Step in the PAC-Bayes World

As mentioned above, there are many PAC-Bayes bounds. This section
covers as a first example a bound proven by Catoni (2003). Why this
choice?
Well, any choice is partly arbitrary: I did my PhD thesis (Alquier,
2006) with Olivier Catoni and thus I know his works well. But, also,
the objective is not to rush immediately to the best bound. Rather,
this Catoni’s result will be useful to illustrate how PAC-Bayes bounds
work, how to use them, and explain the different variants (bounds
on randomized estimators, bounds on aggregated estimators, etc.). It
appears that Catoni’s technique is extremely convenient to prove almost
all the various type of bounds with a unified proof. Later, in Section 3,
we will see many alternative empirical PAC-Bayes bounds, this will
allow you to compare them, and discuss the pros and the cons of each.
2.1
2.1.1

A Simple PAC-Bayes Bound
Catoni’s bound (Catoni, 2003)

From now, and until the end of these notes, let us fix a probability
measure π ∈ P(Θ). The measure π will be called the prior,

190

2.1. A SIMPLE PAC-BAYES BOUND

191

because of a connection with Bayesian statistics that will be discussed
in Section 6. We recall that the loss function is bounded and takes
values in [0, C].
Theorem 2.1. For any λ > 0, for any δ ∈ (0, 1),
PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)]
λC 2 KL(ρ∥π) + log 1δ
+
+
8n
λ

!

≥ 1 − δ.

Let us prove Theorem 2.1. This requires a lemma that will be
extremely useful in all these notes. This lemma has been known since
the 50s (Kullback, 1959, Exercise 8.28) in the case of a finite Θ, but
the general case is due to Donsker and Varadhan (1976).
Lemma 2.2 (Donsker and Varadhan’s variational formula). For any measurable, bounded function h : Θ → R we have:
h

i

h

log Eθ∼π eh(θ) = sup

i

Eθ∼ρ [h(θ)] − KL(ρ∥π) .

ρ∈P(Θ)

Moreover, the supremum with respect to ρ in the right-hand side is
reached for the Gibbs measure πh defined by its density with respect to
π:
dπh
eh(θ)

.
(θ) =
(2.1)
dπ
Eϑ∼π eh(ϑ)
Proof of Lemma 2.2. Using the definition, for any ρ ∈ P(Θ),
dρ
(θ)
KL(ρ∥πh ) = Eθ∼ρ log
dπh





i

h

Eϑ∼π eh(ϑ) dρ


= Eθ∼ρ log
(θ)
dπ
eh(θ)






= −Eθ∼ρ [h(θ)] + Eθ∼ρ log





dρ
(θ)
dπ



h

+ log Eϑ∼π eh(ϑ)
h

i

= −Eθ∼ρ [h(θ)] + KL(ρ∥π) + log Eθ∼π eh(θ) .

i

192

First Step in the PAC-Bayes World

Thanks to Proposition 1.2, the left hand side is nonnegative, and equal
to 0 only for ρ = πh . □
Proof of Theorem 2.1. The beginning of the proof follows closely the
study of the ERM and the proof of Theorem 1.2. Fix θ ∈ Θ and apply
Hoeffding’s inequality with Ui = E[ℓi (θ)] − ℓi (θ): for any t > 0,
h

i

nt2 C 2
8

i

λ2 C 2

ES etn[R(θ)−r(θ)] ≤ e

.

We put t = λ/n, which gives:
h

ES eλ[R(θ)−r(θ)] ≤ e 8n .
This is where the proof diverges from the proof of Theorem 1.2. We will
now integrate this bound with respect to π:
h

i

λ2 C 2

Eθ∼π ES eλ[R(θ)−r(θ)] ≤ e 8n .
Thanks to Tonelli’s theorem, we can exchange the integration with
respect to θ and the one with respect to the sample:
h

i

λ2 C 2

ES Eθ∼π eλ[R(θ)−r(θ)] ≤ e 8n

(2.2)

and we apply Donsker and Varadhan’s variational formula (Lemma 2.2)
to get:
h

i

λ2 C 2

λ2 C 2



ES esupρ∈P(Θ) λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π) ≤ e 8n .
Rearranging terms:


ES esupρ∈P(Θ) λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− 8n

≤ 1.

(2.3)

The end of the proof uses Chernoff bound. Fix s > 0,
"

PS

#

λ2 C 2
sup λEθ∼ρ [R(θ) − r(θ)] − KL(ρ∥π) −
>s
8n
ρ∈P(Θ)


λ2 C 2

≤ ES esupρ∈P(Θ) λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− 8n



e−s

≤ e−s .
Solve e−s = δ, that is, put s = log(1/δ) to get
λ2 C 2
1
sup λEθ∼ρ [R(θ) − r(θ)] − KL(ρ∥π) −
> log
≤ δ.
8n
δ
ρ∈P(Θ)

"

PS

#

2.1. A SIMPLE PAC-BAYES BOUND

193

Rearranging terms gives:
"

PS ∃ρ ∈ P(Θ), Eθ∼ρ [R(θ)] > Eθ∼ρ [r(θ)]
λC 2 KL(ρ∥π) + log 1δ
+
+
8n
λ

#

≤ δ.

Take the complement to end the proof. □
2.1.2

Exact minimization of the bound

We remind that the bound in Theorem 1.2,
s



PS ∀θ ∈ Θ, R(θ) ≤ r(θ) + C



log M
δ 
≥ 1 − δ,
2n

motivated the introduction of θ̂ERM , the minimizer of r.
Exactly in the same way, the bound in Theorem 2.1,
PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)]
λC 2 KL(ρ∥π) + log 1δ
+
+
8n
λ

!

≥ 1 − δ,

motivates the study of a data-dependent probability measure ρ̂λ that
would be defined as:
KL(ρ∥π)
ρ̂λ = argmin Eθ∼ρ [r(θ)] +
.
λ
ρ∈P(Θ)




But does such a minimizer exist? It turns out that the answer is yes,
thanks to Donsker and Varadhan’s variational formula again! Indeed,
to minimize:
KL(ρ∥π)
Eθ∼ρ [r(θ)] +
λ
is equivalent to maximize
−λEθ∼ρ [r(θ)] − KL(ρ∥π)

194

First Step in the PAC-Bayes World

which is exactly what the variational inequality does, with h(θ) =
−λr(θ). We know that the minimum is reached for ρ = π−λr as defined
in (2.1). Let us summarize this in following definition and corollary.
Definition 2.1. In the whole tutorial we will let ρ̂λ denote “the Gibbs
posterior” given by ρˆλ = π−λr , that is:
e−λr(θ) π(dθ)

.
Eϑ∼π e−λr(ϑ)

ρ̂λ (dθ) =

(2.4)

Corollary 2.3. The Gibbs posterior is the minimizer of the right-hand
side of Theorem 2.1:
KL(ρ∥π)
ρ̂λ = argmin Eθ∼ρ [r(θ)] +
.
λ
ρ∈P(Θ)




As a consequence, for any λ > 0, for any δ ∈ (0, 1),
λC 2 KL(ρ∥π) + log 1δ
+
Eθ∼ρ̂λ [R(θ)] ≤ inf
Eθ∼ρ [r(θ)] +
8n
λ
ρ∈P(Θ)
"

PS

#!

≥ 1 − δ.
2.1.3

Some examples, and non-exact minimization of the bound

When you see something like:
λC 2 KL(ρ∥π) + log 1δ
+
,
8n
λ
I’m not sure you immediately see what is the order of magnitude of
the bound. I don’t. In general, when you apply such a general bound
to a set of predictors, I think it is quite important to make the bound
more explicit. Let us process a few examples (I advise you to do the
calculations on your own in these examples, and in other examples).
Eθ∼ρ [r(θ)] +

Example 2.1 (Finite case). Let us start with the special case where
Θ is a finite set, that is, card(Θ) = M < +∞. We begin with the
application of Corollary 2.3. In this case, the Gibbs posterior ρ̂λ of (2.4)
is a probability on the finite set Θ given by
e−λr(θ) π(θ)
.
−λr(ϑ) π(ϑ)
ϑ∈Θ e

ρ̂λ (θ) = P

2.1. A SIMPLE PAC-BAYES BOUND

195

and we have, with probability at least 1 − δ:
λC 2 KL(ρ∥π) + log 1δ
Eθ∼ρ̂λ [R(θ)] ≤ inf
Eθ∼ρ [r(θ)] +
+
. (2.5)
8n
λ
ρ∈P(Θ)
"

#

When we apply Donsker and Varadhan’s variational formula (again!) to
the right-hand side, we obtain:
Eθ∼ρ̂λ [R(θ)] ≤

X
λC 2 log 1δ
−1
log
π(θ)e−λr(θ) +
+
.
λ
8n
λ
θ∈Θ

(2.6)

By using, for any θ ∈ Θ, 0 ≤ exp(−λr(θ)) ≤ exp(−λ inf ϑ∈Θ r(ϑ)), we
show:




log π(θ)
X
−1
.
inf r(θ) ≤
log
π(θ)e−λr(θ) ≤ inf r(θ) +
θ∈Θ
ϑ∈Θ
λ
λ
θ∈Θ
1

(2.7)

So, (2.6) leads to the more explicit (but less tight!) bound:




λC 2 log π(θ)δ 
Eθ∼ρ̂λ [R(θ)] ≤ inf r(θ) +
+
.
θ∈Θ
8n
λ
1

This gives us an intuition on the role of the prior π: the bound will be
tight if there is a θ such that r(θ) and 1/π(θ) are small simulataneously.
However, π cannot be large everywhere: its total mass is constrained to
be 1. The larger Θ is, the more we have to “spread the mass” of π, which
will increase 1/π(θ) in the bound. This is clear if we use a uniform prior:
p
π(θ) = 1/M . In this case, the choice λ = 8n log(M/δ)/C 2 actually
minimizes the right-hand side, and leads to:
s



PS Eθ∼ρ̂λ [R(θ)] ≤ inf r(θ) + C
θ∈Θ



log M
δ 
≥ 1 − δ.
2n

(2.8)

That is, the Gibbs posterior ρ̂λ satisfies the same bound as the ERM
in Theorem 1.2. Note that it does not mean that ρ̂λ and θ̂ERM are
equivalent! The PAC-Bayes bound in (2.6) can actually be tighter, as
shown by a closer examination of (2.7): the term in the middle can
be arbitrarily close to the left-hand side if the empirical risk of all
parameters is close enough to inf θ∈Θ r(θ). We will discuss in Section 4

196

First Step in the PAC-Bayes World

a so-called prior mass condition that relates more generally the mass of
the level sets of r under π to the tightness of PAC-Bayes bounds.
Note that the optimization with respect to λ is a little more problematic when π is not uniform, because the optimal λ would depend on
the data, which is not allowed - at the moment. We will come back to
the choice of λ in the general case soon.
Let us also consider the statement of Theorem 2.1 in this case. With
probability at least 1 − δ, we have:
∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)] +

λC 2 KL(ρ∥π) + log 1δ
+
.
8n
λ

As the bound holds for all ρ ∈ P(Θ), it holds in particular for all ρ in
the set of Dirac masses {δθ , θ ∈ Θ}. Obviously:
Eϑ∼δθ [r(ϑ)] = r(θ)
and

1
δθ (ϑ)
δθ (ϑ) = log
.
KL(δθ ∥π) =
log
π(ϑ)
π(θ)
ϑ∈Θ
X





This gives:
∀θ ∈ Θ, R(θ) ≤ r(θ) +

1
1
λC 2 log π(θ) + log δ
+
8n
λ

and, when π is uniform:
∀θ ∈ Θ, R(θ) ≤ r(θ) +

λC 2 log M
δ
+
.
8n
λ

As this bound holds for any θ, it holds in particular for the ERM, which
gives:
λC 2 log M
δ
R(θ̂ERM ) ≤ inf r(θ) +
+
θ∈Θ
8n
λ
and, once again with the choice λ =
exactly the result of Theorem 1.2:

p

8n log(M/δ)/C 2 , we recover
s

R(θ̂ERM ) ≤ inf r(θ) + C
θ∈Θ

log M
δ
.
2n

2.1. A SIMPLE PAC-BAYES BOUND

197

The previous example leads to important remarks:
• PAC-Bayes bounds can be used to prove generalization bounds for
Gibbs posteriors, but sometimes they can also be used to study
more classical estimators, like the ERM. This actually goes far
beyond the ERM. Many recent papers use PAC-Bayes bounds
to study non-Bayesian robust estimators of the mean and the
covariance matrix of heavy-tailed random vectors. This is discussed
further in Sections 6.2 and 6.3.
• the choice of λ has a different status when you study the Gibbs
posterior ρ̂λ and the ERM. Indeed, in the bound on the ERM, λ
is chosen to minimize the bound, but the estimation procedure
is not affected by λ. The bound for the Gibbs posterior is also
minimized with respect to λ, but ρ̂λ depends on λ. So, if you
make a mistake when choosing λ, this will have bad consequences
not only on the bound, but also on the practical performances
of the method. This means also that if the bound is not tight, it
is likely that the λ obtained by minimizing the bound will not
lead to good performances in practice. (We present in Section 3
bounds that do not depend on a parameter like λ).
Example 2.2 (Lipschitz loss and Gaussian priors). Let us switch to the
continuous case, so that we can derive from PAC-Bayes bounds some
results that could not be obtained only with a union bound argument.
We consider the case where Θ = Rd , the function θ 7→ ℓ(fθ (x), y) is
L-Lipschitz for any x and y, and the prior π is a centered Gaussian:
π = N (0, σ 2 Id ) where Id is the d × d identity matrix.
Let us, as in the previous example, study first the Gibbs posterior,
by an application of Corollary 2.3. With probability at least 1 − δ,
λC 2 KL(ρ∥π) + log 1δ
Eθ∼ρ̂λ [R(θ)] ≤ inf
Eθ∼ρ [r(θ)] +
+
.
8n
λ
ρ∈P(Θ)
"

#

Once again, the right-hand side is an infimum over all possible probability distributions ρ, but it is easier to restrict to Gaussian distributions
here. So:

198

First Step in the PAC-Bayes World
"

Eθ∼ρ̂λ [R(θ)] ≤

inf

ρ = N (m, s2 Id )
m ∈ Rd , s > 0

λC 2 KL(ρ∥π) + log 1δ
Eθ∼ρ [r(θ)] +
+
.
8n
λ
#

(2.9)
Indeed, it is well known that, for ρ = N (m, s2 Id ) and π = N (0, σ 2 Id ),
"

#

σ2
∥m∥2 d s2
+
+
log
−1 .
KL(ρ∥π) =
2σ 2
2 σ2
s2
Moreover, the risk r inherits the Lipschitz property of the loss, that is,
for any (θ, ϑ) ∈ Θ2 , r(θ) ≤ r(ϑ) + L∥ϑ − θ∥. So, for ρ = N (m, s2 Id ),
Eθ∼ρ [r(θ)] ≤ r(m) + LEθ∼ρ [∥θ − m∥]
q

≤ r(m) + L Eθ∼ρ [∥θ − m∥2 ] by Jensen’s inequality
√
= r(m) + Ls d.
Plugging this into (2.9) gives:
√
λC 2
r(m) + Ls d +
8n
m∈Rd ,s>0
"

Eθ∼ρ̂λ [R(θ)] ≤

inf

+

∥m∥2
+ d2
2σ 2

h 2

i

2
s
+ log σs2 − 1
σ2

+ log 1δ

#

λ

.

It is possible to minimize the bound completely in s, but for now, we
√
will just consider the choice s = σ/ n, which gives:
Eθ∼ρ̂λ [R(θ)]


s

≤ inf r(m) + Lσ
m∈Rd

d λC 2
+
+
n
8n



≤ inf r(m) + Lσ
m∈Rd

s

∥m∥2
+ d2
2σ 2

d λC 2
+
+
n
8n

h

i

1
n − 1 + log(n)

+ log 1δ




λ


∥m∥2
+ d2 log(n) + log 1δ
2σ 2


λ

.

It is not possible to optimize the bound with respect to λ as the
optimal value would depend on m... We will show how to get rid of
this limitation soon. However, there is a way to simplify the bound (by
making it worse!): to restrict the infimum on m to ∥m∥ ≤ B for some
B > 0. Then we have:

2.1. A SIMPLE PAC-BAYES BOUND
s

Eθ∼ρ̂λ [R(θ)] ≤

inf

m:∥m∥≤B

r(m) + Lσ

199
2

B
d
1
d λC 2 2σ
2 + 2 log(n) + log δ
+
+
.
n
8n
λ

In this case, we see that the optimal λ is
1
λ=
C

s

8n



B2
d
1
+ log(n) + log
2σ 2 2
δ



which gives:
s

Eθ∼ρ̂λ [R(θ)] ≤

inf

m:∥m∥≤B

r(m) + Lσ

s

d
+C
n

B2
+ d2 log(n) + log 1δ
2σ 2

2n

.

Note that our choice of λ might look a bit weird, as it depends on the
confidence level δ. This can be avoided by taking:
1
λ=
C

s

B2
d
8n
+ log(n)
2
2σ
2




instead (check what bound you obtain by doing so!).
Finally, as in the previous example, we can also start from the
statement of Theorem 2.1: with probability at least 1 − δ,
∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)] +

λC 2 KL(ρ∥π) + log 1δ
+
,
8n
λ

and restrict here ρ to the set of Gaussian distributions N (m, s2 Id ). This
leads to the definition of a new data-dependent probability measure,
ρ̃λ = N (m̃, s̃2 Id ) where
(

(m̃, s̃) = argmin

m∈Rd ,s>0

+

Eθ∼N (m,s2 Id ) [r(θ)]
λC 2
8n

+

∥m∥2
+ d2
2σ 2

h 2

i

2
s
+ log σs2 − 1
σ2

λ

+ log 1δ

)

(2.10)

when this is well defined (we can adapt the definition of ρ̃λ to the
situation when there is no minimum, we postpone this to the next
paragraph). While the Gibbs posterior ρ̂λ can be quite a complicated
object, one simply has to solve this minimization problem to get ρ̃λ . The
probability ρ̃λ is actually a special case of what is called a variational

200

First Step in the PAC-Bayes World

approximation of ρ̂λ . Variational approximations are very popular in
statistics and machine learning, and were indeed analyzed through
PAC-Bayes bounds (Alquier et al., 2016; Alquier and Ridgway, 2020;
Yang et al., 2020). We will come back to this in Section 6. For now,
following the same computations, and using the same choice of λ as for
ρ̂λ , we obtain the same bound:
s

Eθ∼ρ̃λ [R(θ)] ≤

inf

m:∥m∥≤B

r(m) + Lσ

s

d
+C
n

B2
+ d2 log(n) + log 1δ
2σ 2

2n

.

Note that this approach can still be used in the case where the
minimum is not reached in the definition of (m̃, s̃) in (2.10). For any
ϵ > 0, we define (m̃ϵ , s̃ϵ ) as an ϵ-minimizer, that is, it reaches the
infimum in (2.10) up to ϵ. Taking ρ̃λ as ρ̃λ = N (m̃ϵ , s̃2ϵ Id ) with ϵ = 1/n
leads to
Eθ∼ρ̃λ [R(θ)]
s

≤

inf

m:∥m∥≤B

r(m) + Lσ

s

d
+C
n

B2
+ d2 log(n) + log 1δ
2σ 2

2n

+

1
.
n

Example 2.3 (Model aggregation, model selection). In the case where
we have many sets of predictors, say Θ1 , . . . , ΘM , equipped with priors
S
π1 , . . . , πM respectively, it is possible to define a prior on Θ = M
j=1 Θj .
For the sake of simplicity, assume that the Θj ’s are disjoint, and let
p = (p(1), . . . , p(M )) be a probability distribution on {1, . . . , M }. We
simply put:
π=

M
X

p(j)πj .

j=1

The minimization of the bound in Theorem 2.1 leads to the Gibbs
posterior ρ̂λ that will put mass on all the Θj in general, so this is a
model aggregation procedure in the spirit of McAllester (1999). On the
other hand, we can also restrict the minimization in the PAC-Bayes
bound to distributions that would charge only one of the models, that
is, to ρ ∈ P(Θ1 ) ∪ · · · ∪ P(ΘM ). Theorem 2.1 becomes:

2.1. A SIMPLE PAC-BAYES BOUND

201

PS ∀j ∈ {1, . . . , M }, ∀ρ ∈ P(Θj ), Eθ∼ρ [R(θ)]
λC 2 KL(ρ∥π) + log 1δ
≤ Eθ∼ρ [r(θ)] +
+
8n
λ

!

≥ 1 − δ,

that is
PS ∀j ∈ {1, . . . , M }, ∀ρ ∈ P(Θj ), Eθ∼ρ [R(θ)]
λC 2 KL(ρ∥πj ) + log p(j) + log δ
+
≤ Eθ∼ρ [r(θ)] +
8n
λ
1

1!

≥ 1 − δ.

Thus, we can propose the following procedure:
• first, we build the Gibbs posterior for each model j,
e−λr(θ) πj (dθ)
,
−λr(ϑ) π (dϑ)
j
Θj e

(j)

ρ̂λ (dθ) = R
• then, model selection:

(j)




ĵ = argmin Eθ∼ρ̂(j) [r(θ)] +
1≤j≤M 



1 
KL(ρ̂λ ∥πj ) + log p(j)

λ

λ

.



The obtained ĵ satisfies:
(

PS E

(ĵ)

θ∼ρ̂λ

[R(θ)] ≤ min

+

2.1.4

inf

1≤j≤M ρ∈P(Θj )

Eθ∼ρ [r(θ)]

1
KL(ρ∥πj ) + log p(j)
+ log 1δ

λ

)!

≥ 1 − δ.

The choice of λ

As discussed earlier, it is in general not possible to optimize the righthand side of the PAC-Bayes equality with respect to λ. For example,
in (2.5), the optimal value of λ could depend on ρ, which is not allowed

202

First Step in the PAC-Bayes World

by Theorem 2.1. In the previous examples, we have seen that in some
situations, if one is lucky enough, the optimal λ actually does not depend
on ρ, but we still need a procedure for the general case.
A natural idea is to propose a finite grid Λ ⊂ (0, +∞) and to minimize over this grid, which can be justified by a union bound argument.
Theorem 2.4. Let Λ ⊂ (0, +∞) be a finite set. For any δ ∈ (0, 1),
PS ∀ρ ∈ P(Θ), ∀λ ∈ Λ, Eθ∼ρ [R(θ)]
card(Λ)
δ

λC 2 KL(ρ∥π) + log
≤ Eθ∼ρ [r(θ)] +
+
8n
λ

!

≥ 1 − δ.

Proof. Fix λ ∈ Λ, and then follow the proof of Theorem 2.1 until (2.3):


2

C
supρ∈P(Θ) λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− λ 8n

ES e

2



≤ 1.

Sum over λ ∈ Λ to get:
X



ES e



≤ card(Λ)



≤ card(Λ).

2

2

2

2

C
supρ∈P(Θ) λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− λ 8n

λ∈Λ

and so


C
supρ∈P(Θ),λ∈Λ λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− λ 8n

ES e

The end of the proof is as for Theorem 2.1, we start with Chernoff
bound. Fix s > 0,
"

PS

#

λ2 C 2
sup
λEθ∼ρ [R(θ) − r(θ)] − KL(ρ∥π) −
>s
8n
ρ∈P(Θ),λ∈Λ


2

C
supρ∈P(Θ),λ∈Λ λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− λ 8n

≤ ES e

2



e−s

≤ card(Λ)e−s .
Solve card(Λ)e−s = δ, that is, put s = log(card(Λ)/δ) to get
"
PS

#
λ2 C 2
card(Λ)
sup λEθ∼ρ [R(θ) − r(θ)] − KL(ρ∥π) −
> log
≤ δ.
8n
δ
ρ∈P(Θ)

2.1. A SIMPLE PAC-BAYES BOUND

203

Rearranging terms gives:
"

PS ∃ρ ∈ P(Θ), ∃λ ∈ Λ, Eθ∼ρ [R(θ)] > Eθ∼ρ [r(θ)]
λC 2 KL(ρ∥π) + log
+
+
8n
λ

card(Λ)
δ

#

≤ δ.

Take the complement to get the statement of the theorem. □
This leads to the following procedure. First, we remind that, for a
fixed λ, the minimizer of the bound is ρ̂λ = π−λr . Then, we put:
ρ̂ = ρ̂λ̂ where
λC 2 KL(π−λr ∥π) + log
λ̂ = argmin Eθ∼π−λr [r(θ)] +
+
8n
λ
λ∈Λ
(

card(Λ)
δ

)

.
(2.11)

We have immediately the following result.
Corollary 2.5. Define ρ̂ as in (2.11), for any δ ∈ (0, 1) we have
"

PS Eθ∼ρ̂ [R(θ)] ≤

inf

ρ ∈ P(Θ)
λ ∈ Λ

Eθ∼ρ [r(θ)] +

λC 2
8n

KL(ρ∥π) + log card(Λ)
δ
+
λ

#!

≥ 1 − δ.

We could for example propose an arithmetic grid Λ = {1, 2, . . . , n}.
The bound in Corollary 2.5 becomes:
"

Eθ∼ρ̂ [R(θ)] ≤

inf

ρ ∈ P(Θ)
λ = 1, . . . , n

λC 2 KL(ρ∥π) + log nδ
Eθ∼ρ [r(θ)] +
+
8n
λ

#

It is also possible to transform the optimization on a discrete grid by an
optimization on a continuous grid. Indeed, for any λ ∈ [1, n], we simply
apply the bound to the integer part of λ, ⌊λ⌋, and remark that we can
upper bound ⌊λ⌋ ≤ λ and 1/⌊λ⌋ ≤ 1/(λ − 1). So the bound becomes:
λC 2 KL(ρ∥π) + log nδ
Eθ∼ρ [r(θ)] +
+
.
8n
λ−1

"

Eθ∼ρ̂ [R(θ)] ≤

inf

ρ ∈ P(Θ)
λ ∈ [1, n]

#

204

First Step in the PAC-Bayes World

The arithmetic grid is not be the best choice, though: the log(n)
term can be improved. In order to optimize hyperparameters in PACBayes bounds, Langford and Caruana (2002) used a geometric grid
Λ = {ek , k ∈ N} ∩ [1, n], the same choice was used later by Catoni
(2003) and Catoni (2007, Theorem 1.2.8 page 13). Using such a grid in
Corollary 2.5 we get
λC 2 KL(ρ∥π) + log logδ n
Eθ∼ρ [r(θ)] +
+
.
8n
λ/e

"

Eθ∼ρ̂ [R(θ)] ≤

inf

ρ ∈ P(Θ)
λ ∈ [1, n]

#

We conclude this discussion on the choice of λ by mentioning that
there are other PAC-Bayes bounds, as the one by McAllester (1999),
where there is no parameter λ to optimize. We will study these bounds
in Section 3.
2.2

PAC-Bayes Bound on Aggregation of Predictors and Weighted
Majority Vote

In the introduction, right after Definition 1.1, I promised that PACBayes bound would allow to control
• the risk of randomized predictors,
• the expected risk of randomized predictors,
• the risk of averaged predictors.
But so far, we only focused on the expected risk of randomized predictors
(the second bullet point). In this subsection, we provide some bounds
on averaged predictors, and in the next one, we will focus on the risk of
randomized predictors.
We start by a very simple remark. When the loss function u 7→ ℓ(u, y)
is convex for any y, then the risk R(θ) = R(fθ ) is a convex function of
fθ . Thus, Jensen’s inequality ensures:
Eθ∼ρ [R(fθ )] ≥ R(Eθ∼ρ [fθ ]).
Plugging this into Corollary 2.3 gives immediately the following result.

2.3. PAC-BAYES BOUND ON A SINGLE DRAW FROM THE
POSTERIOR

205

Corollary 2.6. Assume that ∀y ∈ Y, u 7→ ℓ(u, y) is convex. Define
fˆρ̂λ (·) = Eθ∼ρ̂λ [fθ (·)].
For any λ > 0, for any δ ∈ (0, 1),
PS


R(fˆρ̂ ) ≤
λ



KL(ρ∥π) + log 1δ
λC 2
Eθ∼ρ [r(θ)] +
+
≥ 1 − δ.
8n
λ
ρ∈P(Θ)
inf

That is, in the case of a convex loss function, like the quadratic loss
or the hinge loss, PAC-Bayes bounds also provide bounds on the risk of
aggregated predictors.
It is also possible to study R(Eθ∼ρ [fθ ]) − Eθ∼ρ [R(fθ )] under other
assumptions. For example, we can use the Lipschitz property as in
Example 2.2. In the case of the quadratic loss, we have R(Eθ∼ρ [fθ ]) −
Eθ∼ρ [R(fθ )] = EX [Varθ∼ρ (fθ (X))], this fact was used to provide tight
bounds on R(Eθ∼ρ [fθ ]) (Audibert, 2004, page 22). A similar idea was
used later beyond regression to control R(Eθ∼ρ [fθ ]) − Eθ∼ρ [R(fθ )] by a
variance term (Germain et al., 2015; Masegosa, 2020).
However, note that in the case of classification, fθ (x) ∈ {0, 1} for
any x and θ, but fˆρ̂λ (x) can be any value in [0, 1]. We can define a new
classifier by fˆρ̂maj
(x) = 1 if fˆρ̂λ (x) ≥ 1/2 and fˆρ̂maj
(x) = 0 otherwise.
λ
λ
This is known as the weighted majority vote classifier. Adaptations
of PAC-Bayes bounds to control the risk of weighted majority vote
classifiers and variants were proven, and this is still an important
research direction (Langford and Shawe-Taylor, 2002; Lacasse et al.,
2006; Laviolette et al., 2011; Lorenzen et al., 2019; Masegosa et al.,
2020; Wu et al., 2021; Wu and Seldin, 2022).
2.3

PAC-Bayes Bound on a Single Draw from the Posterior

Theorem 2.7. For any λ > 0, for any δ ∈ (0, 1), for any data-dependent
probability measure ρ̃,
PS Pθ̃∼ρ̃

dρ
(θ̃) + log 1δ
λC 2 log dπ
+
R(θ̃) ≤ r(θ̃) +
8n
λ

!

≥ 1 − δ.

This bound simply says that if you draw θ̃ from, for example, the
Gibbs posterior ρ̂λ (defined in (2.4)), you have the bound on R(θ̃) that

206

First Step in the PAC-Bayes World

holds with large probability simultaneously on the drawing of the sample
and of θ̃.
Proof. Once again, we follow the proof of Theorem 2.1, until (2.2):
h

λ2 C 2

i

ES Eθ∼π eλ[R(θ)−r(θ)] ≤ e 8n .
Now, for any nonnegative function h,
Eθ∼π [h(θ)] =
≥
=

Z

h(θ)π(dθ)
Z
dρ̃
(θ)>0}
{ dπ

h(θ)π(dθ)

Z

{

dρ̃
(θ)>0
dπ

}

h(θ)

h

dπ
(θ)ρ̃(dθ)
dρ̃
dρ̃

i

i

λ2 C 2

= Eθ∼ρ̃ h(θ)e− log dπ (θ)
and in particular:
h

dρ̃

ES Eθ∼ρ̃ eλ[R(θ)−r(θ)]−log dπ (θ) ≤ e 8n .
We could go through the proof until the end, but you can now guess
that it’s essentially Chernoff bound + rearrangement of the terms. □
Clerico et al. (2022b) proposed a very clever use of such a PAC-Bayes
bound that does not actually require to sample from ρ̃. They study
a sequence (θt )t=0,...,T obtained by gradient descent, with a random
initialization θ0 . The prior π is taken as the distribution of θ0 , and ρ̃ is
defined implicitly as the distribution of θT . They apply a PAC-Bayes
bound similar to Theorem 2.7 and provide an explicit upper bound on
dρ
log dπ
. This analysis gives a bound on R(θT ), that is, a bound on the
risk of a deterministic predictor (up to the initialization). This is related
to information bounds on similar algorithms that will be discussed in
Subsection 6.6.2.
2.4

Bound in Expectation

We end this section by one more variant of the initial PAC-Bayes bound
in Theorem 2.1: a bound in expectation with respect to the sample.

2.4. BOUND IN EXPECTATION

207

Theorem 2.8. For any λ > 0, for any data-dependent probability
measure ρ̃,
"

ES Eθ∼ρ̃ [R(θ)] ≤ ES Eθ∼ρ̃

#

λC 2 KL(ρ̃∥π)
+
.
r(θ) +
8n
λ

In particular, for ρ̃ = ρ̂λ the Gibbs posterior,
"

ES Eθ∼ρ̂λ [R(θ)] ≤ ES

#

λC 2 KL(ρ∥π)
+
.
inf Eθ∼ρ [r(θ)] +
8n
λ
ρ∈P(θ)

These bounds in expectation are very convenient tools from a pedagogical point of view. Indeed, in Section 4, we will study oracle PACBayes inequalities. While it is possible to derive oracle PAC-Bayes
bounds both in expectation and with large probability, the one in expectation are much simpler to derive, and much shorter. Thus, Section 4
will mostly cover PAC-Bayes oracle bounds in expectation, and we refer
the reader to Catoni (2003) and Catoni (2007) for the corresponding
bounds in probability.
Note that as the bound does not hold with large probability, as
the previous bounds, it is no longer a PAC bound in the proper sense:
Probably Approximately Correct. A few years ago, I was attending a
talk by Tsybakov where he presented some results from his paper with
Dalalyan (Dalalyan and Tsybakov, 2008) that can also be interpreted
as a “PAC-Bayes bound in expectation”, and he suggested the more
appropriate EAC-Bayes acronym: Expectedly Approximately Correct
(their paper is briefly discussed in Section 6.5 below). I don’t think this
term was often reused since then. I also found recently the acronym
MAC-Bayes (Grünwald et al., 2021): Mean Approximately Correct. In
order to avoid any confusion I will stick to “PAC-Bayes bound in
expectation”, but I like EAC and MAC! Early examples of PAC-Bayes
bounds in expectation were proven by Alquier (2006), Catoni (2007),
Juditsky et al. (2008), and Dalalyan and Tsybakov (2008).
Proof. Once again, the beginning of the proof is the same as for Theorem 2.1, until (2.3):


2

C
supρ∈P(Θ) λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− λ 8n

ES e

2



≤ 1.

208

First Step in the PAC-Bayes World

This time, use Jensen’s inequality to send the expectation with respect
to the sample inside the exponential function:
h

2

C
ES supρ∈P(Θ) λEθ∼ρ [R(θ)−r(θ)]−KL(ρ∥π)− λ 8n

2

i

e

≤ 1,

that is,
"

ES

#

λ2 C 2
sup λEθ∼ρ [R(θ) − r(θ)] − KL(ρ∥π) −
≤ 0.
8n
ρ∈P(Θ)

In particular,
"

ES

#

λ2 C 2
≤ 0.
λEθ∼ρ̃ [R(θ) − r(θ)] − KL(ρ̃∥π) −
8n

Rearrange terms. □
2.5

Applications of Empirical PAC-Bayes Bounds

The original PAC-Bayes bounds were stated for classification (McAllester, 1998) and it became soon clear that many results could be
extended to any bounded loss, thus covering for example bounded
regression (we discuss in Section 5 how to get rid of the boundedness
assumption). Thus, some papers are written in no specific setting,
with a generic loss, that can cover classification, regression, or density
estimation. For example, the result of Catoni (2007) about classification
are extended to unbounded losses in my PhD thesis (Alquier, 2006,
Chapter 1).
However, some empirical PAC-Bayes bounds were also developped
or applied to specific models, sometimes taking advantage of some
specificities of the model. We mention for example:
• support vector classifiers (Langford and Shawe-Taylor, 2002; Catoni, 2007),
• random forests (Lorenzen et al., 2019),
• ranking/scoring (Ralaivola et al., 2010),

2.5. APPLICATIONS OF EMPIRICAL PAC-BAYES BOUNDS

209

• density estimation (Higgs and Shawe-Taylor, 2010; Seldin and
Tishby, 2010),
• multiple testing (Blanchard and Fleuret, 2007) is tackled with
related techniques,
• deep learning: even though deep networks are trained for classification or regression, the application of PAC-Bayes bounds to
deep learning is not straightforward. We discuss this in Section 3
based on the work by Dziugaite and Roy (2017) and more recent
references,
• generative adversarial networks (Mbacke et al., 2023),
• unsupervised learning, including clustering (Seldin and Tishby,
2010; Appert and Catoni, 2021), representation learning (Nozawa
and Sato, 2019; Nozawa et al., 2020), variational autoencoders
(Chérief-Abdellatif et al., 2022).
This list is of course non-exhaustive. Many more applications are presented in Section 4 (more precisely, in Section 4.3).

3
Tight and Non-vacuous PAC-Bayes Bounds

3.1

Why is there a Race to Tighter PAC-Bayes Bound?

Let us start with a numerical application of the PAC-Bayes bounds we
met in Section 2.
First, assume we are in the classification setting with the 0-1 loss,
so that C = 1. We are given a small set of classifiers, say M = 100,
such that on the test set with size n = 1000, the best of these classifiers
has an empirical risk rn = 0.26. Let us use the bound in (2.8), that is
reminded here:
s



PS Eθ∼ρ̂λ [R(θ)] ≤ inf r(θ) + C
θ∈Θ



log M
δ 
≥ 1 − δ.
2n

With δ = 0.05 this bound is:
s

PS Eθ∼ρ̂λ [R(θ)] ≤ 0.26 + 1.
|

100
log 0.05
2 × 1000

{z

≤0.062

!

≥ 0.95.

}

So the classification risk using the Gibbs posterior is smaller than 0.322
with probability at least 95%.
210

3.1. WHY IS THERE A RACE TO TIGHTER PAC-BAYES BOUND?211
Let us now switch to a more problematic example. We consider a very
simple binary neural network, given by the following formula, for x ∈ Rd ,
and where φ is a nonlinear activation function (e.g φ(x) = max(x, 0)):




M
d
X
X
(2)
(1)
fw (x) = 1  w φ 
w xj  ≥ 0
i

j,i

i=1
(1)

(2)

and the weights wj,i and wi

j=1

are all in {−1, +1} for 1 ≤ j ≤ d and

(1)
(1)
(1)
(2)
(2)
1 ≤ i ≤ M . Define θ = (w1,1 , w1,2 , . . . , wd,M , w1 , . . . , wM ). Note that
the set of all possible such networks has cardinality 2M (d+1) . Consider

inputs that are 100 × 100 greyscale images, that is, x ∈ [0, 1]d with
d = 10, 000, and a sample size n = 10, 000. With neural networks, it
is often the case that a perfect classification of the training sample is
possible, that is, there is a θ such that r(θ) = 0.
Even for a moderate number of units such as M = 100, this leads
to the PAC-Bayes bound (with δ = 0.05):
s

PS Eθ∼ρ̂λ [R(θ)] ≤ 1.
|

1,000,100

log 2 0.05
2 × 10, 000
{z

≃13.58

!

≥ 0.95.

}

So the classification risk using the Gibbs posterior is smaller than 13.58
with probability at least 95%. Which is not informative at all, because
we already know that the classification risk is smaller than 1. Such a
bound is usually refered to as a vacuous bound, because it does not
bring any information at all. You can try to improve the bound by
increasing the dataset. But you can check that even n = 1, 000, 000 still
leads to a vacuous bound with this network.
Various opinions on these vacuous bounds are possible:
• “theory is useless. I don’t know why I would care about generalization guarantees, neural networks work in practice.” This opinion
is lazy: it’s just a good excuse not to have to think about generalization guarantees. I will assume that since you are reading this
tutorial, this is not your opinion.
• “vacuous bounds are certainly better than no bounds at all!” This
opinion is a little cynical, it can be rephrased as “better have a

212

Tight and Non-vacuous PAC-Bayes Bounds
theory that doesn’t work than no theory at all: at least we can
claim we have a theory, and some people might even believe us”.
But the theory just says nothing.

• “let’s get back to work, and improve the bounds”. Since the publication of the first PAC-Bayes bounds already mentioned (ShaweTaylor and Williamson, 1997; McAllester, 1998; McAllester, 1999),
many variants were proven. One can try to test which one is the
best in a given setting, try to improve the priors, try to refine the
bound in many ways... In 2017, Dziugaite and Roy (2017) obtained
non-vacuous (even though not really tight yet) PAC-Bayes bounds
for practical neural networks (since then, tighter bounds were
obtained by these authors and by others). This is a remarkable
achievement, and this also made PAC-Bayes theory immediately
more popular than it was ever before.
Let’s begin this section with a review of some popular PAC-Bayes
bounds: Section 3.2. Some of them are of historical interest, while others
will illustrate various possible improvements. We will prove many of
them thanks to a general bound due to Germain et al. (2009). We will
then focus more specifically on deep learning: we explain which bound,
and which improvements led to tight generalization bounds for deep
learning (Section 3.3). In particular, we will focus on a very important
approach to improve the bounds: data-dependent priors.
3.2

A Few PAC-Bayes Bounds

Note that the original works on PAC-Bayes focused only on classification
with the 0-1 loss (McAllester, 1998). However, they can be directly
extended to any loss taking values in [0, 1] (Maurer, 2004, Lemma 3).
So, we will state all the following bounds for any [0, 1]-valued loss ℓ.
Thus, R and r also take value in [0, 1] and C = 1 in this section. Many
of these bounds can be derived from Theorem 3.6 due to Germain
et al. (2009). So we will postpone the proofs to after the statement of
Theorem 3.6.

3.2. A FEW PAC-BAYES BOUNDS
3.2.1

213

The first PAC-Bayes bounds

The very first paper on PAC-Bayes bounds by McAllester (1998) was
stated for a finite or denumerable set Θ. Let us start with the first
bound for a general Θ, by McAllester (1999).
Theorem 3.1 (Theorem 1, McAllester (1999)). For any δ > 0,
"

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)]
s

+

KL(ρ∥π) + log 1δ + 52 log(n) + 8
≥ 1 − δ.
2n − 1
#

Compared to Theorem 2.1, note that there is no parameter λ here
to optimize. On the other hand, one can no longer use Lemma 2.2 to
minimize the right-hand side. A way to solve this problem
is to make the
√
parameter λ appear artificially using the inequality ab ≤ aλ/2+b/(2λ)
for any λ > 0:
"

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)]
(

≤ Eθ∼ρ [r(θ)] + inf

λ>0

KL(ρ∥π) + log 2δ + 12 log(n)
λ
+
4n − 2
2λ

)#

≥ 1 − δ. (3.1)
On the other hand, the price to pay for an optimization with respect
to λ in Theorem 2.4 was a log(n) term, that is already in McAllester’s
bound, with an arithmetic grid, and a log log(n) term when using a
geometric grid. Of course, the geometric grid leads to an additional
constraint that λ ∈ [1, n], but one can easily check that this is always
the case when (3.1) is nonvacuous anyway. So, asymptotically in n,
Theorem 2.4 with a geometric grid will lead to better results than
Theorem 3.1. On the other hand, the constants in Theorem 3.1 are
smaller, so the bound can be better for small sample sizes (a point that
should not be neglected for tight certificates in practice!).
It is possible to minimize the right-hand side in (3.1) with respect to
ρ, and this will lead to a Gibbs posterior: ρ̂ = π−2λr . It is also possible

214

Tight and Non-vacuous PAC-Bayes Bounds

to minimize it with respect to λ, but the minimization in λ when ρ itself
depends on λ is a bit more tricky (for example, there might be local
minima). We will discuss below a more recent bound due to Thiemann
et al. (2017), that can be minimized efficiently in both λ and ρ.
3.2.2

A key for tigher bounds: kl-PAC-Bayes bounds

Let us now propose a completely different bound. This bound is very
central in the PAC-Bayesian theory: we will see that many other bounds
can be derived from this one. A first version was proven by Langford
and Seeger (2001) and Seeger (2002) and is often refered to as Seeger’s
bound. The bound was slightly improved by Maurer (2004), so we will
here provide Maurer’s version of Seeger’s bound.
Let Be(p) denote the probability distribution of a Bernoulli random
variable V with parameter p, that is, P(V = 1) = p = 1 − P(V = 0).
Then we have:
1−p
p
=: kl(p∥q)
KL(Be(p)∥Be(q)) = p log + (1 − p) log
q
1−q
which is interpreted as a statistical distance between p and q.
Theorem 3.2 (Theorem 5, Maurer (2004)). For any δ > 0,
"



PS ∀ρ ∈ P(Θ), kl Eθ∼ρ [r(θ)] ∥Eθ∼ρ [R(θ)]


√

KL(ρ∥π) + log 2 δ n
≤
n

#

≥ 1 − δ.

Under this form, the bound is not very explicit, so we will derive
more explicit versions. Following Seeger (2002), we define:
kl−1 (p ∥b ) = sup{q ∈ [0, 1] : kl(p∥q) ≤ b}.
Then the bound becomes:
"

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)]


≤ kl−1 Eθ∼ρ [r(θ)]

√ #
2 n
KL(ρ∥π) + log δ


n

≥ 1 − δ.

3.2. A FEW PAC-BAYES BOUNDS

215

We can deduce more explicit bounds from Seeger’s bound simply by
providing explicit bounds on the function kl−1 .
As a first application of this method, Pinsker’s inequality (Boucheron et al., 2013, Theorem 4.19) implies kl(p∥q) ≥ 2(p − q)2 , and thus
p
kl−1 (p∥b) ≤ p + b/2. Thus, Theorem 3.2 implies, for any δ > 0,
"

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)]
s

+

√

KL(ρ∥π) + log 2 δ n
2n

#

≥1−δ

which is essentially McAllester’s bound with improved constants. But
we can do much better.
3.2.3

Explicit tight bounds

Based on an idea due to McAllester (2003), Tolstikhin and Seldin (2013)
derived upper bounded kl−1 using relaxed Pinsker’s inequality to prove
the following result.
Theorem 3.3 ((3), Tolstikhin and Seldin (2013)). For any δ > 0,
"

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)]
s

+

√

KL(ρ∥π) + log 2 δ n
2Eθ∼ρ [r(θ)]
n
√ #
KL(ρ∥π) + log 2 δ n
+2
≥ 1 − δ.
n

Note something amazing: while the dependence of this bound in n
√
is in general in 1/ n, as all the PAC-Bayes bounds seen so far, it drops
to 1/n if Eθ∼ρ [r(θ)] = 0. This was actually not a surprise, because a
similar phenomenon is known for the ERM (Vapnik, 1998).
More generally, we will see in Section 4 a general assumption that
characterizes the best possible learning rate in classification problems.
And as a special case, the noiseless case indeed leads to rates in 1/n.
Let us summarize the important take home message from Theorem 3.3:

216

Tight and Non-vacuous PAC-Bayes Bounds

√
• the empirical PAC-Bayes bounds seen so far were in 1/ n,
• in the noiseless case Eθ∼ρ [r(θ)] = 0, it is possible to have a
bound in 1/n, on the condition that one uses the right PAC-Bayes
inequality, for example Theorem 3.3 or Theorem 3.2.
This is very important for the application of these bounds to neural
networks, as deep networks usually allow to classify the training data
perfectly.
Another example of a theorem derived from Seeger’s bound appears
to be very convenient for a joint minimization in λ and ρ, and is also
extremely tight (see Subsection 3.3 below).
Theorem 3.4 (Theorem 3, Thiemann et al. (2017)). For any δ > 0,
"

(

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤

inf

λ∈(0,2)

Eθ∼ρ [r(θ)] KL(ρ∥π) + log

+
1 − λ2
nλ 1 − λ2

√ )#
2 n
δ

≥ 1−δ.

Here again, we observe the 1/n regime when Eθ∼ρ [r(θ)] = 0 (for
example for λ = 1).
√
Finally, note PAC-Bayes bounds with both 1/n and 1/ n can be
derived without using the kl-PAC-Bayes bound. We provide as an
example this result by Catoni (2007).
Theorem 3.5 (Theorem 1.2.6 page 11, Catoni (2007)). Define, for a > 0,
the function of p ∈ (0, 1)
− log {1 − p [1 − e−a ]}
.
a
Then, for any λ > 0, for any ϵ > 0,
Φa (p) =


PS



KL(ρ∥π) + log 1δ
E
[r(θ)]
+
∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Φ−1
θ∼ρ
λ
n
λ
≥ 1 − δ. (3.2)

Theorem 3.5 can be proven using a bound of Germain et al. (2009),
that is also used to prove the kl-PAC-Bayes bound. Theorem 3.5 can
be made a little more explicit. We have
Φ−1
a (q) =

1 − e−aq
aq
≤
,
−a
1−e
1 − e−a

3.2. A FEW PAC-BAYES BOUNDS

217

and thus:
(

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤

"

λ
−λ

h

n 1−e n

i Eθ∼ρ [r(θ)]

KL(ρ∥π) + log 1δ
+
λ

#)

≥ 1 − δ. (3.3)

Before we prove all these bounds, let us apply them to the same
examples than in Section 2 to highlight the improvements. I will actually
use Theorem 3.4, the application of the other bounds can be done in a
similar way.
Example 3.1 (Finite case). We start with a continuation of Example 2.1:
card(Θ) = M < +∞, and π is a uniform distribution. For any δ > 0,
√






log 2Mδ n 
r(θ)
 ≥ 1 − δ.

PS ∀λ ∈ (0, 2), Eθ∼ρ̂λ [R(θ)] ≤ inf
+

θ∈Θ 1 − λ
nλ 1 − λ 
2
2

If r(θ̂ERM ) = 0, the inequality becomes:
√

Eθ∼ρ̂λ [R(θ)] ≤

log 2Mδ n


nλ 1 − λ2

,

which is exactly minimized for λ = 1. Thus, in this case, we put λ̂ = 1
and we obtain:
√
2 log 2Mδ n
Eθ∼ρ̂λ̂ [R(θ)] ≤
.
n
In the case where r(θ̂ERM ) > 0, we could minimize the right-hand side
exactly in λ. However, even an approximate minimization is enough to
obtain a good bound in this toy example. For example, with
s

λ̂ =

√

log 2Mδ n
,
n

we obtain, for n large enough so that λ̂ < 2,
r

Eθ∼ρ̂λ̂ [R(θ)] ≤

inf θ∈Θ r(θ) +
r

1 − 12

√

log 2Mδ n
n
√

log 2Mδ n
n

218

Tight and Non-vacuous PAC-Bayes Bounds
s



=  inf r(θ) +
θ∈Θ

√



log 2Mδ n
 (1 + o(1)).
n

Thus, Theorem 3.4 allows an empirical definition of λ̂ that leads essentially to the same bound than in Example 2.1, up to the log n term, in
general. Moreover, in the case r(θ̂ERM ) = 0, the rate is much better.
Example 3.2 (Gaussian priors). We come back to the setting of Example 2.2: Θ = Rd , the function θ 7→ ℓ(fθ (x), y) is L-Lipschitz and π
is a Gaussian π = N (0, σ 2 Id ), where Id is the d × d identity matrix.
Plugging the formulas derived in Example 2.2 into Theorem 3.4, we
obtain:
"

PS ∀λ ∈ (0, 2), Eθ∼ρ̂λ [R(θ)] ≤
+

∥m∥2
+ d2
2σ 2

inf

Eθ∼N (m,s2 Id ) [r(θ)]
1 − λ2

m∈Rd ,s>0

h 2

2
s
+ log σs2 − 1
σ2



nλ 1 − λ2

i

√

+ log 2 δ n

#

≥ 1 − δ.



Note that, when compared to Example 2.2, a major advantage here is
that the bound allows to minimize the right-hand side in m, σ and λ
without having to impose an upper bound on ∥m∥.
3.2.4

Some proofs

We start this section with a nice generalization of Theorem 3.2 by
Germain et al. (2009). The first reason why we state this result is that
it can be used to prove all the bounds mentioned since the beginning
of this section, which will be done in this subsection. The other reason
is that it can be used to derive bounds for unbounded losses, and for
non-i.i.d. observations. This point will be discussed in Section 5.
Theorem 3.6 (Theorem 2.1, Germain et al. (2009)). Let D : [0, 1]2 → R
be any convex function. For any δ > 0,
"

PS ∀ρ ∈ P(Θ), D (Eθ∼ρ [r(θ)], Eθ∼ρ [R(θ)])
nD(r(θ),R(θ))

KL(ρ∥π) + log Eθ∼π ES e δ
≤
n

#

≥ 1 − δ.

3.2. A FEW PAC-BAYES BOUNDS

219

Proof of Theorem 3.6. For short, put
M(π) = ES Eθ∼π enD(r(θ),R(θ))
= Eθ∼π ES enD(r(θ),R(θ)) ,
the second inequality being due to Tonelli’s theorem, and observe that
ES esupρ∈P(Θ) [nEθ∼ρ [D(r(θ),R(θ))]−KL(ρ∥π)] = M(π)
(using Donsker and Varadhan’s inequality). Multiply both sides by
δ/M(π) to get:
ES esupρ∈P(Θ) [nEθ∼ρ [D(r(θ),R(θ))]−KL(ρ∥π)]−log

M(π)
δ

= δ.

Thus, with probability at least 1 − δ,
sup

h

i

nEθ∼ρ [D(r(θ), R(θ))] − KL(ρ∥π) − log

ρ∈P(Θ)

M(π)
≤0
δ

and rearranging terms, for all ρ ∈ P(Θ),
Eθ∼ρ [D(r(θ), R(θ))] ≤

KL(ρ∥π) + log M(π)
δ
.
n

Finally, thanks to the convexity of D, this implies
D(Eθ∼ρ [r(θ)], Eθ∼ρ [R(θ)]) ≤

KL(ρ∥π) + log M(π)
δ
.
n

We will now prove Theorem 3.2 from Theorem 3.6. This requires
the following lemma.
Lemma 3.7 (Theorem 1 of Maurer, 2004). For any θ ∈ Θ,
√
ES en.kl(r(θ)∥R(θ)) ≤ 2 n.
We are now in position to prove Theorem 3.2.

220

Tight and Non-vacuous PAC-Bayes Bounds

Proof of Theorem 3.2. We apply Theorem 3.6 to D(x, y) = kl(x∥y). We
obtain, with probability at least 1 − δ, for any ρ ∈ P(Θ),
n.kl(r(θ)∥R(θ))

KL(ρ∥π) + log Eθ∼π ES e δ
n
√
2 n
KL(ρ∥π) + log δ
,
≤
n
we used Lemma 3.7 in the second inequality.
kl (Eθ∼ρ [r(θ)]∥Eθ∼ρ [R(θ)]) ≤

Proof of Theorem 3.3. We recall the relaxed version of Pinkser’s inequality (Boucheron et al., 2013, Lemma 8.4): for any (p, q) ∈ (0, 1)2 ,
(p − q)2
.
2q

kl(p∥q) ≤
This leads to

(p − q)2 ≤ 2qkl(p∥q)
and thus
q ≤p+

q

2qkl(p∥q)

(3.4)

which implies, using q ≤ 1,
q ≤p+

q

2kl(p∥q).

(3.5)

We plug (3.5) into (3.4) to get
q ≤p+

s 

2 p+

q



2kl(p∥q) kl(p∥q) ≤

q

2pkl(p∥q) + 2kl(p∥q)

and
kl−1 (p∥b) ≤ p +

p

2pb + 2b.

Plug this upper bound into Theorem 3.2 to get the stated inequality.
Proof of Theorem 3.4. We follow the previous proof until (3.4). Then,
remark that for any a, b > 0,
√
λa
b
ab = inf
+
,
λ>0 2
2λ
and apply this inequality to a = q and b = 2kl(p∥q). We obtain, for any
λ > 0,
qλ kl(p∥q)
+
q ≤p+
2
λ

3.2. A FEW PAC-BAYES BOUNDS
and thus

221

kl(p∥q)
λ
≤p+
q 1−
.
2
λ
If λ < 2, we can divide both sides by 1 − λ/2 > 0, which gives:




q≤

p
kl(p∥q)
.
+ 
λ
1− 2
λ 1− λ
2

Thus,





b
p
 .
+ 
kl−1 (p∥b) ≤ inf 
λ
λ
0≤λ≤2 1 −
λ
1
−
2
2

Plug this upper bound into Theorem 3.2.
Sketch of the proof of Theorem 3.2. This result can be obtained by an
application of Theorem 3.6 with D(p, q) = − log[1 − p(1 − e−a )] − aq.
The control of the exponential moment
M(π) = ES Eθ∼π enD(r(θ),R(θ))
is provided in Corollary 2.2 of Germain et al. (2009) in the case of the
binary loss, and can be extended to any [0, 1]-valued loss thanks to
Lemma 3 of Maurer (2004).
These derivations lead to a natural question: is there a function D
that will lead to a strict improvement of Theorem 3.2? The question is
investigated by Foong et al. (2021). Overall, it seems that no function
D will lead to a bound that will be smaller in expectation than the one
√
in Theorem 3.2, up to the log(2 n) term.
3.2.5

PAC-Bayes-Bernstein

The first PAC-Bayes bound introduced in Section 2, Theorem 2.1, uses
Hoeffding’s inequality to control the expectation of the exponential
of the generalization error. For this reason, it is sometimes refered
to as PAC-Bayes-Hoeffding bound. Most bounds seen in Section 3 so
far were a consequence of another control of this exponential moment:
Lemma 3.7.

222

Tight and Non-vacuous PAC-Bayes Bounds

We will conclude this necessarily non-exhaustive survey on empirical
PAC-Bayes bounds by covering another family of bounds, known as
PAC-Bayes-Bernstein, because they rely on Bernstein’s inequality to
control the exponential moment. There are actually many versions of
Bernstein’s inequality. For a proof of the one we state here, see Catoni
(2004, Theorem 5.2.1), or McDiarmid (1998).
Lemma 3.8 (Bernstein’s inequality). Let g denote the Bernstein function
defined by g(0) = 1 and, for x ̸= 0,
g(x) =

ex − 1 − x
.
x2

Let U1 , . . . , Un be i.i.d. random variables such that E(Ui ) is well defined
and Ui − E(Ui ) ≤ C almost surely for some C ∈ R. Then
 Pn

E et

i=1

[Ui −E(Ui )]



2

≤ eg(Ct)nt Var(Ui ) .

Before discussing PAC-Bayes bounds based on Lemma 3.8, let us
compare it to our application of Hoeffding’s inequality in Section 1. As
ℓi (θ) ∈ [0, 1] here, an application of Lemma 3.8 to Ui = E[ℓi (θ)] − ℓi (θ)
gives:


2
E etn[R(θ)−r(θ)] ≤ eg(t)nt Var(ℓi (θ)) .
The term Var(ℓi (θ)) is of particular interest, so we introduce a shorter
notation.
Definition 3.1. We put V(θ) = Var(ℓi (θ)).
In order to ease the comparison with the previous section, we also
put λ = nt. Chernoff’s bounding technique leads to
λ2

PS (R(θ) > r(θ) + s) ≤ eg( n ) n V(θ)−λns .
λ

We define δ as the right-hand side and consider the complementary
event:


PS R(θ) ≤ r(θ) +

g

 
λ
n

λV(θ)

n



+

log 1δ

λ

≥ 1 − δ.

The exact optimization of the right-hand side in λ is not straightforward
because of the function g, but an approximate minimization is enough

3.2. A FEW PAC-BAYES BOUNDS

223

to highlight the benefits of Bernstein’s inequality. In the regime λ < n,
g(λ/n) ≤ g(1) < 1 and thus the bound becomes
PS
The choice λ =

λV(θ) log 1δ
R(θ) ≤ r(θ) +
+
n
λ
p

!

≥ 1 − δ.

n/V(θ) would lead to



s

PS R(θ) ≤ r(θ) +



Note however that when V(θ) < 1/n,
propose simply to take λ = n to get:
PS



V(θ)
1 
1 + log
≥ 1 − δ.
n
δ


n/V(θ) > n. In this case, we

p

1 + log 1δ
R(θ) ≤ r(θ) +
n

!

≥ 1 − δ.

Combining both inequalities, we obtain
s



PS R(θ) ≤ r(θ) + min 





V(θ) 1 
1 
,
1 + log
≥ 1 − δ.
n n
δ




(3.6)

It is important to compare (3.6) to bounds obtained by Hoeffding’s
inequality, such as (1.1). Of course, as the loss takes values in [0, 1]
here, we could upper bound V(θ) by 1/4, and in this case we obtain
something comparable to (1.1). However, when V(θ) is small, (3.6) is
much better.
Using the proof technique of Section 2, we obtain the following
PAC-Bayes bound: for any λ > 0, for any δ ∈ (0, 1),
PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)]
≤ Eθ∼ρ [r(θ)] +

λg

 
λ
n

Eθ∼ρ [V(θ)]
n

KL(ρ∥π) + log 1δ
+
λ

!

≥ 1 − δ.

Unfortunately, this bound is useless in practice, as the right-hand side
depends on the unknown distribution of the observations via the variance
term V.

224

Tight and Non-vacuous PAC-Bayes Bounds

It turns out that it is possible to upper bound the term Eθ∼ρ [V(θ)]
by an empirical variance term to obtain a so-called empirical PACBayes-Bernstein bound (Seldin et al., 2012a; Tolstikhin and Seldin,
2013). For example, Tolstikhin and Seldin (2013, Theorem 3) provided
such an upper bound, V(ρ, π, δ) below, to prove the following result.
We will omit the proof here.
Theorem 3.9 (Theorem 4, Tolstikhin and Seldin (2013)). Fix any c1 , c2 >
0. Put, for any θ ∈ Θ,
V̂ (θ) =

n
1 X
(ℓi (θ) − r(θ))2 .
n − 1 i=1

Put
V(ρ, π, δ) = Eθ∼ρ [V̂ (θ)] + 2c2

KL(ρ∥π) + log 2νδ 2
n−1

+ (1 + c2 )
where

1
ν2 =
log
log c2
&

v


u
u Eθ∼ρ [V̂ (θ)] KL(ρ∥π) + log 2ν2
t
δ

1
2

2(n − 1)

s

n−1
1
2 +1+ 2
log δ

!'

.

Then, for any δ ∈ (0, 1),
!

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)] + B(ρ, π, δ)

≥ 1 − δ,

where
v


u
u (e − 2)V(ρ, π, δ) KL(ρ∥π) + log 2ν1
t
δ

B(ρ, π, δ) = (1 + c1 )

n

for all ρ such that
v
u
u KL(ρ∥π) + log 2ν1
√
δ
t
≤ n

(e − 2)Eθ∼ρ [V̂ (θ)]

and
B(ρ, π, δ) = 2

KL(ρ∥π) + log 2νδ 1
n

3.3. TIGHT GENERALIZATION ERROR BOUNDS FOR DEEP
LEARNING

225

for all other ρ, and
1
log
ν1 =
log c1
&

s

(e − 2)n
4 log 2δ

!'

.

Let us compare this bound to Theorems 3.4 and 3.3. If θ is such
that r(θ) = 0, then we also have direclty V̂(θ) = 0. Thus, when there
is a ρ such that ρ-almost surely, r(θ) = 0, then Theorem 3.9 leads
√
to a bound in 1/n rather than in 1/ n. Moreover, as ℓi (θ) ∈ [0, 1]
here, ℓi (θ)2 ≤ ℓi (θ) and thus, we can expect that V̂(θ) ≤ r(θ). Thus,
even when there is no perfect predictor, Theorem 3.9 can lead to
a tighter bound than Theorem 3.3. Empirical PAC-Bayes-Bernstein
bounds became an important research direction, with improvements
of the original bound, and many applications (Tolstikhin and Seldin,
2013; Mhammedi et al., 2019; Wu et al., 2021; Wu and Seldin, 2022;
Jang et al., 2023). Finally, some oracle PAC-Bayes bounds discussed in
Section 4 also rely on Bernstein’s inequality.
More bounds are known, but it’s not possible to mention all, so
I apologize if I didn’t cite a bound you like, or your bound. Many
refinments of the above bounds are discussed in a recent preprint
by Rodrígues-Gálvez et al. (2023). Some other variants will be discussed
later, especially in Section 6: bounds for unbounded losses ℓ, bounds
for non i.i.d. data, and also some bounds where the KL divergence
KL(ρ∥π) is replaced by another divergence.
3.3
3.3.1

Tight Generalization Error Bounds for Deep Learning
A milestone: non vacuous generalization error bounds for
deep networks by Dziugaite and Roy (2017)

PAC-Bayes bounds were applied to (shallow) neural networks as early
as in 2002 by Langford and Caruana (2002). We also applied them with
O. Wintenberger to prove that shallow networks can consistently predict
time series (Alquier and Wintenberger, 2012). McAllester proposed an
application of PAC-Bayes bounds to dropout, a tool used for training
neural networks, in his tutorial (McAllester, 2013). But none of these
techniques seemed to lead to tight empirical bounds for deep networks...

226

Tight and Non-vacuous PAC-Bayes Bounds

until 2017, when Dziugaite and Roy (2017) obtained the first nonvacuous generalization error bounds for deep networks on the MNIST
dataset based on Theorem 3.2 (Seeger’s bound). Since then, there was
a regain of interest in PAC-Bayes bounds to obtain the tightest possible
certificates.
At first sight, Dziugaite and Roy (2017) applied Seeger’s bound to
a deep neural network, but many important ideas and refinements were
used to lead to a non vacuous bound (some being original, and according
to the authors, some based on ideas from Langford and Caruana, 2002).
Let us describe here briefly these ingredients, the reader should of course
read the paper for more details and insightful explanations:
• the posterior is constrained to be Gaussian (similar to the above
“non-exact minimization of the bound” in Section 2.1.3): ρw,s2
= N (w, s2 Id ). Thus, the PAC-Bayes bound only has to be minimized with respect to the parameter (w, s2 ), which allows to use
an optimization algorithm to minimize the bound (the authors
mention that fitting Gaussian distributions to neural networks
was already proposed by Hinton and Van Camp (1993) based on
the MDL principle, which will be discussed in Section 6).
• the choice of an adequate upper bound on kl−1 in Seeger’s bound
in order to make the bound easier to minimize.
• Seeger’s bound holds for the 0 − 1 loss, but Dziugaite and Roy
upper bounded the empirical risk by a convex, Lipschitz upper
bound in order to make the bound easier to minimize (this is a
standard approach in classification):
"

Eθ∼ρ [r(θ)] = Eθ∼ρ

n
1X
1(fθ (Xi ) ̸= Yi )
n i=1

#





n log 1 + e−Yi fθ (Xi )
1X
.
≤ Eθ∼ρ 
n i=1
log 2



• the use of the Stochastic Gradient Algorithm (SGD) to minimize
the bound (up to our knowledge, the first authors to use of SGD

3.3. TIGHT GENERALIZATION ERROR BOUNDS FOR DEEP
LEARNING

227

to minimize a PAC-Bayes bound was Germain et al. (2009) for
linear classification). Of course, this is standard in deep learning,
but there is a crucial observation that SGD tends to converge to
flat minima. This is very important, because around a flat minima
w∗ , we have r(w) ≃ r(w∗ ) and thus Eθ∼ρw,s2 [r(θ)] ≃ r(θ∗ ) even for
quite large values of s2 . On the other hand, for a sharp minimum
w∗ , Eθ∼ρw,s2 [r(θ)] ≃ r(θ∗ ) only for very small values of s2 which
tends to make the PAC-Bayes bound larger (see Example 2.2
above).
• finally, the authors used a data dependent prior: N (w0 , σ 2 I),
where σ 2 is chosen to minimize the bound (this is justified in
theory thanks via a union bound argument as in Subsection 2.1.4).
The mean w0 is not optimized, but the authors point out that the
choice w0 = 0 is not suitable and they actually draw w0 randomly,
as is usually done in non-Bayesian approaches to initialize SGD.
On the MNIST data set, the authors obtain empirical bounds between 0.16 and 0.22, thus, non vacuous. The classification performance
of their posterior is actually around 0.03, so they conclude that there is
still room for improvement. Indeed, since then, a wide range of papers,
from very theoretical to very computational, studied PAC-Bayes bounds
for deep networks (London, 2017; Neyshabur et al., 2017; Zhou et al.,
2018; Letarte et al., 2019; Viallard et al., 2019; Rivasplata et al., 2019;
Lan et al., 2020; Tsuzuku et al., 2020; Biggs and Guedj, 2021; Foret
et al., 2020; Pérez-Ortiz et al., 2021; Suzuki, 2020; Pitas, 2020; Clerico
et al., 2023; Jin et al., 2022; Clerico et al., 2022a; Steffen and Trabs,
2022; Głuch and Urbanke, 2023; Zhang et al., 2023). We discuss recent
results by Pérez-Ortiz et al. (2021) and Clerico et al. (2022a) below,
but first, let us discuss in detail one of the most important ingredients
above: the data-dependent prior.
3.3.2

Bounds with data-dependent priors

To use data in order to improve the prior is actually an old idea: we
found such approaches works by Seeger (2003), Catoni (2003), Catoni
(2004), Zhang (2006), Ambroladze et al. (2006), Catoni (2007), Lever
et al. (2010), Parrado-Hernández et al. (2012), Lever et al. (2013),

228

Tight and Non-vacuous PAC-Bayes Bounds

Dziugaite and Roy (2017), Dziugaite and Roy (2018), and Dziugaite
et al. (2021b). Note that the original PAC-Bayes bounds do not allow
to take a data-dependent prior. Thus, some additional work is required
to make this possible (e.g the union bound on σ 2 by Dziugaite and Roy
(2017) discussed above). The first occurence of this idea is due to Seeger
(2003, Chapter 4). Seeger proposed to split the sample in two parts. The
first part is used to define Θ and the prior π, and the PAC-Bayes bound
is applied on the second part of the sample (that is, conditionally on
the first part). Seeger used this technique to study the generalization of
Gaussian processes. Later Catoni (2003) used it to prove generalization
error bounds on compression schemes. We will here describe in detail
two other approaches: first, Catoni’s “localization” technique, because
it will also be important in Sections 4 and 6, and then a recent bound
by Dziugaite and Roy (2018).
First, let us discuss the intuition leading to Catoni’s method. As
can be seen in the elementary bounds in Section 2, for example in
Example 2.1, the bound is tighter for parameters θ for which π(θ) is
large, and less tight for parameters θ for which π(θ) is small: in the
finite case, we recall that the Kullback-Leibler divergence led to a term
in log(1/π(θ)) in the bound. Based on this idea, we might want to
construct a prior π that gives a large weight to the relevant parameters,
that is, to parameters such that R(θ) is small. A possible prior is π−βR
for some β > 0, where π−βR is given by
dπ−βR
e−βR(θ)
(θ) =
.
dπ
Eϑ∼π [e−βR(ϑ) ]
This priori is often refered to as a localized prior (Catoni, 2003; Catoni,
2007) or as a distribution-dependent prior (Lever et al., 2010; Lever et al.,
2013). This choice is not data-dependent, and thus allowed by theory. But
in practice, it cannot be used, because R(θ) = E(X,Y )∼P [ℓ(fθ (X), Y )] is
of course unknown (still, we use the prior π−βR in Section 4 below, in theoretical bounds that are not meant to be evaluated on the data). For empirical bounds, Catoni proved that KL (ρ∥π−βR ) can be upper bounded,
with large probability, by KL (ρ∥π−ξr ) for ξ = β/(λ + g(λ/n)λ2 /n),
plus some additional terms (g being Bernstein’s function defined in
Lemma 3.8). Plugging this result into Theorem 2.1, he obtained the
following “localized bound” (Catoni, 2003, Lemma 6.2):

3.3. TIGHT GENERALIZATION ERROR BOUNDS FOR DEEP
LEARNING

229

PS ∀ρ, Eθ∼ρ [R(θ)]
≤

(1 − ξ)Eθ∼ρ [r(θ)] + KL (ρ∥π−ξλr ) + (1 + ξ) log 2δ
(1 − ξ)λ + (1 + ξ)g

 
λ
n

!

λ2
n

≥1−δ

which means that we are allowed to use π−ξr , that is data-dependent, as
a prior! This bound is a little scary at first, because it depends on many
parameters. We will provide simpler localized bounds in Section 4 in
order to explain their benefits (in particular, it allows to remove some
log(n) terms in the rates of convergences). For now, simply accept that
the bound is usually tighter than Theorem 2.1, but in practice, we have
to calibrate both λ and β, which makes it a little more difficult to use.
Thus, I am not aware of any application of this technique to neural
networks, but we will show in Section 4 that, used on PAC-Bayes oracle
inequalities, it leads to an improvement of the order of the bound. See
Catoni (2003), Zhang (2006), and Catoni (2007) for more details on the
localization technique.
Dziugaite and Roy (2018) proved that any data-dependent prior
can actually be used in Seeger’s bound, under a differential privacy
condition, at the cost of a small modification of the bound.
Theorem 3.10 (Theorem 4.2, Dziugaite and Roy (2018)). Assume we
have a function Π that maps any sample s = ((x1 , y1 ), . . . , (xn , yn )) into
a prior π = Π(S). Remind that the data is S = ((X1 , Y1 ), . . . , (Xn , Yn ))
and define, for any i ∈ {1, . . . , n}, Si′ a copy of S where (Xi , Yi ) is
replaced by (Xi′ , Yi′ ) ∼ P independent from S. Assume that there is an
η > 0 such that, for any i ∈ {1, . . . , n}, for any measurable set B,
PS (Π(S) ∈ B) ≤ eη PSi′ (Π(Si′ ) ∈ B)
(we say that Π is η-differentially private). Then, for any δ > 0,
√

PS

KL(ρ∥Π(S)) + log 4 δ n
∀ρ, kl (Eθ∼ρ [R(θ)] ∥Eθ∼ρ [r(θ)] ) ≤
n
η2
+
+η
2

s

log 4δ
2n

!

≥ 1 − δ.

230

Tight and Non-vacuous PAC-Bayes Bounds

For more on PAC-Bayes and differential privacy, see Oneto et al.
(2020) and Banerjee and Montúfar (2021).
3.3.3

Comparison of the bounds and tight certificates

Recently, Pérez-Ortiz et al. (2021) trained neural networks by minimizing PAC-Bayes bounds, on the MNIST and CIFAR-10 datasets. They
obtain state of the art test errors (0.02 on MNIST), and improve the
generalization bounds of Dziugaite and Roy (2017): 0.0279 on MNIST,
a very tight bound!. In order to do so, they build on many ideas of
Dziugaite and Roy (2017) but also provide a systematic comparison of
many of the PAC-Bayes bounds listed so far. In all their experiments,
the bound of Thiemann et al. (2017) is the tightest one (Theorem 3.4
above), taking advantage of situations where the empirical risk is very
small. Since then, even tighter results were reported by Clerico et al.
(2022a) with a training based on the Gaussian process approximation
of neural networks.
All these results are obtained by sample splitting, an approach
proposed by Dziugaite et al. (2021b): a large part of the dataset is
used to learn a prior, centered around the weights of a neural network
trained in a non-Bayesian way. The minimization of the PAC-Bayes
bound is done on the second part of the dataset. A recurring criticism
against this approach is that the prior is so good, that the PAC-Bayes
step becomes barely necessary: the posterior learnt is extremely close
to the prior. In other words, we could almost learn the weights using
the first part of the dataset, and use Hoeffding or Bernstein’s inequality
(without a union bound) on the second part of the dataset and still
obtain a reasonnably tight certificate.
I still believe these results are very motivating for PAC-Bayes as they
show that very tight bounds are possible. The numerical comparison of
the various bounds in the context of deep-learning is also of interest.
Other experimental comparisons of the bounds are available, see for
example Foong et al. (2021) in the small-data regime.

4
PAC-Bayes Oracle Inequalities and Fast Rates

As explained in Section 1.4, empirical PAC-Bayes bounds are very useful
as they provide a numerical certificate for randomized estimators or
aggregated predictors. But we also mentioned another type of bounds:
oracle PAC-Bayes bounds. In this section, we provide examples of PACBayes oracle bounds. Interestingly, the first PAC-Bayes oracle inequality
we state below is actually derived from empirical PAC-Bayes inequality.
4.1

From Empirical Inequalities to Oracle Inequalities

As for empirical bounds, we can prove oracle bounds in expectation,
and in probability. We will first present a simple version of each. Later,
we will focus on bounds in expectation for the sake of simplicity: these
bounds are much shorter to prove. But all the results we will prove in
expectation have counterparts in probability, see for example the results
of Catoni (2003) and Catoni (2007).

231

232

PAC-Bayes Oracle Inequalities and Fast Rates

4.1.1

Bound in expectation

We start by a reminder of (the second claim of) Theorem 2.8: for any
λ > 0,
"

ES Eθ∼ρ̂λ [R(θ)] ≤ ES

(

λC 2 KL(ρ∥π)
Eθ∼ρ [r(θ)] +
+
8n
λ

inf

ρ∈P(θ)

)#

,

where we remind that ρ̂λ is the Gibbs posterior defined in (2.4). From
there, we have the following:
"

ES Eθ∼ρ̂λ [R(θ)] ≤ ES

inf

ρ∈P(θ)

"

≤ inf

ES

ρ∈P(θ)

(

)#

(

)#

λC 2 KL(ρ∥π)
Eθ∼ρ [r(θ)] +
+
8n
λ

λC 2 KL(ρ∥π)
+
Eθ∼ρ [r(θ)] +
8n
λ

"

#

"

#

λC 2 KL(ρ∥π)
+
= inf ES {Eθ∼ρ [r(θ)]} +
8n
λ
ρ∈P(θ)
λC 2 KL(ρ∥π)
= inf Eθ∼ρ {ES [r(θ)]} +
+
8n
λ
ρ∈P(θ)

where we used Tonelli’s theorem in the last equality. But, by definition,
ES [r(θ)] = R(θ). Thus, we obtain the following theorem.
Theorem 4.1. For any λ > 0,
(

ES Eθ∼ρ̂λ [R(θ)] ≤ inf

ρ∈P(θ)

λC 2 KL(ρ∥π)
Eθ∼ρ [R(θ)] +
+
8n
λ

)

.

Example 4.1 (Finite case, continued). In the context of Example 2.1, that
p
is, card(Θ) = M < +∞, with λ = 8n/(C 2 log(M )) and π uniform on
Θ we obtain the bound:
s

ES Eθ∼ρ̂λ [R(θ)] ≤ inf R(θ) + C
θ∈Θ

log(M )
.
2n

From this, we don’t have a numerical certificate on ES Eθ∼ρ̂λ [R(θ)].
But on the other hand, we know that our predictions are the best
p
theoretically possible, up to at most C log(M )/2n (such an information
is not provided by an empirical PAC-Bayes inequality).

4.1. FROM EMPIRICAL INEQUALITIES TO ORACLE INEQUALITIES
233
A natural question after Example 4.1 is: is it possible to improve
√
the rate 1/ n? Is it possible to ensure that our predictions are the best
possible up to a smaller term? The answer is “no” in the worst case, but
“yes” quite often. These faster rates will be the object of the following
subsections. But first, as promised, we provide an oracle PAC-Bayes
bound in probability.
4.1.2

Bound in probability

As we derived the oracle inequality in expectation of Theorem 4.1 from
the empirical inequality in expectation of Theorem 2.8, we will now use
the empirical inequality in probability from Theorem 2.1 to prove the
following oracle inequality in probability. Note, however, that the proof
is slightly more complicated, and that this leads to different (and worse)
constants within the bound.
Theorem 4.2. For any λ > 0, for any δ ∈ (0, 1),
PS Eθ∼ρ̂λ [R(θ)]
(

≤

inf

ρ∈P(Θ)

KL(ρ∥π) + log 2δ
λC 2
Eθ∼ρ [R(θ)] +
+2
4n
λ

)!

≥ 1 − δ.
Proof: first, apply Theorem 2.1 to ρ = ρ̂λ , as was done to obtain
Corollary 2.3. This gives:
PS Eθ∼ρ̂λ [R(θ)]
λC 2 KL(ρ∥π) + log 1δ
≤ inf
Eθ∼ρ [r(θ)] +
+
8n
λ
ρ∈P(Θ)
"

#!

≥ 1 − δ. (4.1)

234

PAC-Bayes Oracle Inequalities and Fast Rates

We will now prove the reverse inequality, that is:
PS ∀ρ ∈ P(Θ), Eθ∼ρ [r(θ)]
λC 2 KL(ρ∥π) + log 1δ
≤ Eθ∼ρ [R(θ)] +
+
8n
λ

!

≥ 1 − δ. (4.2)
The proof of (4.2) is exactly similar to the proof of Theorem 2.1, except
that we replace Ui by −Ui . So, the reader who is comfortable enough
with this kind of proof can skip this part, or prove (4.2) as an exercise.
Still, we provide a complete proof for the sake of completeness. Fix
θ ∈ Θ and apply Hoeffding’s inequality with Ui = ℓi (θ) − E[ℓi (θ)], and
t = λ/n:
h

λ2 C 2

i

ES eλ[r(θ)−R(θ)] ≤ e 8n .
Integrate this bound with respect to π:
h

i

λ2 C 2

h

i

λ2 C 2

Eθ∼π ES eλ[r(θ)−R(θ)] ≤ e 8n .
Apply Tonelli:

ES Eθ∼π eλ[r(θ)−R(θ)] ≤ e 8n

and then Donsker and Varadhan’s variational formula (Lemma 2.2):
h

i

λ2 C 2

λ2 C 2



ES esupρ∈P(Θ) λEθ∼ρ [r(θ)−R(θ)]−KL(ρ∥π) ≤ e 8n .
Rearranging terms:


ES esupρ∈P(Θ) λEθ∼ρ [r(θ)−R(θ)]−KL(ρ∥π)− 8n

≤ 1.

Chernoff bound gives:
λ2 C 2
1
sup λEθ∼ρ [r(θ) − R(θ)] − KL(ρ∥π) −
> log
≤ δ.
8n
δ
ρ∈P(Θ)

"

PS

#

4.2. BERNSTEIN ASSUMPTION AND FAST RATES

235

Rearranging terms:
"

PS ∃ρ ∈ P(Θ), Eθ∼ρ [r(θ)] > Eθ∼ρ [R(θ)]
λC 2 KL(ρ∥π) + log 1δ
+
+
8n
λ

#

≤ δ.

Take the complement to get (4.2).
Consider now (4.1) and (4.2). A union bound gives:




2

λC
 Eθ∼ρ̂λ [R(θ)] ≤ inf ρ∈P(Θ) Eθ∼ρ [r(θ)] + 8n +




KL(ρ∥π)+log 1δ
λ

 

and simultaneously

PS 

2

∀ρ ∈ P(Θ), Eθ∼ρ [r(θ)] ≤ Eθ∼ρ [R(θ)] + λC
8n +

KL(ρ∥π)+log 1δ
λ






≥ 1 − 2δ
Plug the upper bound on Eθ∼ρ [r(θ)] from the second line into the first
line to get:
"

PS Eθ∼ρ̂λ [R(θ)] ≤

inf

ρ∈P(Θ)

Eθ∼ρ [r(θ)]

KL(ρ∥π) + log 1δ
λC 2
+2
+2
8n
λ

#!

≥ 1 − 2δ.

Just replace δ by δ/2 to get the statement of the theorem. □
4.2

Bernstein Assumption and Fast Rates

√
As mentioned above, the rate 1/ n that we have obtained in many PACBayes bounds seen so far is not always the tightest possible. Actually,
this can be seen in Tolstikhin and Seldin’s bound (Theorem 3.3): there,
if Eθ∼ρ [r(θ)] = 0 for some ρ, then the bound is actually in 1/n.
It appears that rates in 1/n are possible in a more general setting,
under an assumption often refered to as Bernstein assumption. This is
well known for (“non Bayesian”) PAC bounds (Bartlett et al., 2006),
we will show that this is also true with PAC-Bayes bounds.

236

PAC-Bayes Oracle Inequalities and Fast Rates

Definition 4.1. From now, we will let θ∗ denote a minimizer of R when
it exists:
R(θ∗ ) = min R(θ).

θ∈Θ
∗
When such a θ exists, and when there is a constant K such that, for

any θ ∈ Θ,
n

o

ES [ℓi (θ) − ℓi (θ∗ )]2 ≤ K[R(θ) − R(θ∗ )]
we say that Bernstein assumption is satisfied with constant K.
PAC-Bayes oracle bounds based using explicitly Bernstein’s assumption were proven by Catoni (2003), Zhang (2006), Catoni (2007),
Grünwald and Mehta (2020), and Grünwald et al. (2021). Before we
state such a bound, let us explore situations where this assumption is
satisfied.
Example 4.2 (Classification without noise). Consider classification with
the 0 − 1 loss: ℓi (θ) = 1(Yi ̸= fθ (Xi )). If the optimal classifier does not
make any mistake, that is, if R(θ∗ ) = 0, we have necessarily ℓi (θ∗ ) = 0
almost surely. We refer to this situation as “classification without noise”.
In this case, we have obviously:
n

o

n

ES [ℓi (θ) − ℓi (θ∗ )]2 = ES [1(Yi ̸= fθ (Xi )) − 0]2

o

= ES {1(Yi ̸= fθ (Xi ))}
= R(θ)
= K[R(θ) − R(θ∗ )]
if we put K = 1. So, Bernstein assumption is satisfied with constant
K = 1. Actually, this can be extended beyond the 0 − 1 loss: for any
loss ℓ with values in [0, C], if R(θ∗ ) = 0, then Bernstein assumption is
satisfied with constant K = C.
Example 4.3 (Mammen and Tsybakov margin assumption). More generally, still in classification with the 0 − 1 loss, consider the function
η(x) = ES (Yi |Xi = x).
Mammen and Tsybakov (1999) proved that, if |η(Xi ) − 1/2| ≥ τ almost
surely for some τ > 0, then Bernstein assumption holds for some K that

4.2. BERNSTEIN ASSUMPTION AND FAST RATES

237

depends on τ . The case τ = 1/2 leads back to the previous example
(noiseless classification), but 0 < τ < 1/2 is a more general assumption.
Example 4.4 (Lipschitz and strongly convex loss function). Assume that
Θ is convex. Assume that there are function di : Θ2 → R+ , where each
di might depend of (Xi , Yi ), and assume that ℓi satisfies:
ℓi (θ) + ℓi (θ∗ )
θ + θ∗
∀θ ∈ Θ,
− ℓi
2
2




≥

1 2
d (θ, θ∗ )
8α i

(4.3)

and
∀θ ∈ Θ, |ℓi (θ) − ℓi (θ∗ )| ≤ Ldi (θ, θ∗ ).

(4.4)

In the special case where di (θ, θ′ ) is a metric on Θ, (4.3) will be satisfied if
the loss is α-strongly convex in θ, and (4.4) will be satisfied if the loss is LLipschitz in θ with respect to di . For example, when using the quadratic
loss ℓi (θ) = (Yi − ⟨θ, Xi ⟩)2 , (4.3) holds with di (θ, θ∗ ) = ⟨Xi , θ − θ∗ ⟩2
and α = 1/2 (it is actually an equality in this case, and (4.4) holds if
Xi , Yi and Θ are bounded).
Bartlett et al. (2006) proved that, under these assumptions, Bernstein assumption is satisfied with constant K = 4L2 α. The proof is so
luminous than I cannot resist giving it:
n

ES [ℓi (θ) − ℓi (θ∗ )]2
n

o

≤ L2 ES di (θ, θ∗ )2

o

by (4.4)

ℓi (θ) + ℓi (θ∗ )
θ + θ∗
≤ 8L αES
− ℓi
2
2



∗
∗
R(θ) + R(θ )
θ+θ
2
= 8L α
−R
2
2


∗)
R(θ)
+
R(θ
≤ 8L2 α
− R (θ∗ )
2
2





where in the last equation, we used R(θ∗ ) ≤ R
n





by (4.3)



. Thus:

θ+θ∗
2

o

ES [ℓi (θ) − ℓi (θ∗ )]2 ≤ 4L2 α [R(θ) − R (θ∗ )]
and thus Bernstein assumption is satisfied with constant K = 4L2 α.

238

PAC-Bayes Oracle Inequalities and Fast Rates

Theorem 4.3. Assume Bernstein assumption is satisfied with some
constant K > 0. Take λ = n/ max(2K, C), we have:
ES Eθ∼ρ̂λ [R(θ)] − R(θ∗ )
≤ 2 inf

ρ∈P(Θ)



max(2K, C)KL(ρ∥π)
.
Eθ∼ρ [R(θ)] − R(θ ) +
n
∗



We postpone the proof to the end of this section (page 222), and the
applications to Section 4.3. First, a quick explanation on how we will
use this bound: we only have to find a ρ such that Eθ∼ρ [R(θ)] ≃ R(θ∗ )
to obtain:
2 max(2K, C)KL(ρ∥π)
ES Eθ∼ρ̂λ [R(θ)] ≲ R(θ∗ ) +
,
n
hence the rate in 1/n. We will provide more accurate statements in
Subsection 4.3. The quantity R(θ) − R(θ∗ ) is known as the “excess risk”
of θ. Thus, Theorem 4.3 is often refered to as “excess risk PAC-Bayes
bound”.
Remark 4.1. There is a more general version of Bernstein condition:
where there are constants K > 0 and κ ∈ [1, +∞) such that, for any
θ ∈ Θ,
n
o
1
ES [ℓi (θ) − ℓi (θ∗ )]2 ≤ K[R(θ) − R(θ∗ )] κ
we say that Bernstein assumption is satisfied with constants (K, κ). We
will not study the general case here, but we mention that, in the case of
classification, this can also be interpreted in terms of margin (Mammen
and Tsybakov, 1999). Under such an assumption, some oracle PACBayes inequalities for classification are proven by Catoni (2007, Corollary
1.4.7 page 40) that leads to rates in 1/nκ/(2κ−1) . These results were
later extended to general losses (Alquier, 2008). These rates are known
to be optimal in the minimax sense (Lecué, 2007). Finally, for recent
results and a comparison of all the type of conditions leading to fast
rates in learning theory (including situations with unbounded losses),
see Grünwald and Mehta (2020).
Remark 4.2. All the PAC-Bayes inequalities seen before Section 4 were
√
empirical. Most of them led to the rate 1/ n, except when the empirical
error is close to zero, where we obtained the rate 1/n. In this section,
we built:

4.2. BERNSTEIN ASSUMPTION AND FAST RATES

239

√
• an oracle inequality with rates 1/ n. Note that an empirical
inequality was part of the proof.
• an oracle inequality with rate 1/n. It is important to note that
the proof we will propose does not directly involve any empirical
inequality. (The reader might remark that (4.6) in the proof below is almost an empirical inequality, but the term r(θ∗ ) is not
empirical as it depends on the unknown θ∗ ).
It is thus natural to ask: are there empirical inequalities leading to rates
in 1/n or 1/nκ/(2κ−1) beyond the noiseless case? The answer is “yes” for
“non-Bayesian” PAC bounds (Bartlett and Mendelson, 2006), based on
Rademacher complexity: there are empirical bounds on R(θ̂ERM )−R(θ∗ ).
In the PAC-Bayesian case, it is a little more complicated (unless one
uses the bound to control the risk of a non-Bayesian estimator such as
the ERM). This is discussed by Grünwald et al. (2021).
We will now prove Theorem 4.3. The proof relies on Bernstein’s
inequality (Lemma 3.8).
Proof of Theorem 4.3: We follow the general proof scheme for PAC-Bayes
bounds, with some important differences. Fist, Hoeffding’s inequality
will be replaced by Bernstein’s inequality. But another very important
point is to use the inequality on the “relative losses” ℓi (θ∗ ) − ℓi (θ)
instead of the loss ℓi (θ) (for this reason, excess risk bounds are also
sometimes called “relative bounds”). This is to ensure that we can
use Bernstein condition. So, let us fix θ ∈ Θ and apply Lemma 3.8 to
Ui = ℓi (θ∗ ) − ℓi (θ). As E(Ui ) = R(θ∗ ) − R(θ), we obtain:
∗



∗



2

= ES [ℓi (θ∗ ) − ℓi (θ)]2

o

ES etn[R(θ)−R(θ )−r(θ)+r(θ )] ≤ eg(Ct)nt VarS (Ui ) .
Put λ = tn and note that
VarS (Ui ) ≤ ES (Ui2 )
n

≤ K [R(θ) − R(θ∗ )]
thanks to Bernstein condition. Thus:
λ2

ES eλ[R(θ)−R(θ )−r(θ)+r(θ )] ≤ eg( n ) n K[R(θ)−R(θ )] .


∗

∗



λC

∗

240

PAC-Bayes Oracle Inequalities and Fast Rates

Rearranging terms:


λC λ
∗
∗
E eλ{[1−Kg( n ) n ][R(θ)−R(θ )]−r(θ)+r(θ )} ≤ 1.

(4.5)

S

The next steps are now routine: we integrate θ with respect to π and
apply Tonelli’s theorem and Donsker and Varadhan’s variational formula
to get:


λC λ
∗
∗
E eλ supρ∈P(Θ) (Eθ∼ρ {[1−Kg( n ) n ][R(θ)−R(θ )]−r(θ)+r(θ )}−KL(ρ∥π)) ≤ 1.
S

In particular for ρ = ρ̂λ the Gibbs posterior of (2.4), we have, using
Jensen and rearranging terms:
λC
1 − Kg
n







λ
{ES Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}
n




≤ ES

KL(ρ̂λ ∥π)
Eθ∼ρ̂λ [r(θ)] − r(θ ) +
.
λ


∗

h

From now we assume that λ is such that 1 − Kg



λC
n

 i
λ
n

n

ES Eθ∼ρ̂λ [R(θ)] − R(θ∗ ) ≤

> 0, thus

ES Eθ∼ρ̂λ [r(θ)] − r(θ∗ ) + KL(ρ̂λλ ∥π)
1 − Kg



λC
n



o

λ
n

.

In particular, take λ = n/ max(2K, C). We can check that: λ ≤
n/(2K) ⇒ Kλ/n ≤ 1/2 and λ ≤ n/C ⇒ g(λC/n) ≤ g(1) ≤ 1, so


λC λ
1
Kg
≤
n n
2
and thus


KL(ρ̂λ ∥π)
∗
∗
ES Eθ∼ρ̂λ [R(θ)] − R(θ ) ≤ 2ES Eθ∼ρ̂λ [r(θ)] − r(θ ) +
.
λ
(4.6)
Finally, note that ρ̂λ minimizes the quantity in the expectation in the
right-hand side. Thus, (4.6) can be rewritten as
ES Eθ∼ρ̂λ [R(θ)] − R(θ∗ )
max(2K, C)KL(ρ∥π)
≤ 2ES inf
Eθ∼ρ [r(θ)] − r(θ ) +
n
ρ∈P(Θ)


max(2K, C)KL(ρ∥π)
≤ 2 inf ES Eθ∼ρ [r(θ)] − r(θ∗ ) +
n
ρ∈P(Θ)


max(2K, C)KL(ρ∥π)
∗
= 2 inf
Eθ∼ρ [R(θ)] − R(θ ) +
.□
n
ρ∈P(Θ)


∗



4.3. APPLICATIONS OF THEOREM 4.3
4.3

241

Applications of Theorem 4.3

Example 4.5 (Finite set of predictors). We come back to the setting
of Example 2.1: card(Θ) = M and π is the uniform distribution over
Θ. Assuming Bernstein condition holds with constant K, we apply
Theorem 4.3 and, as was done in Example 2.1, we restrict the supremum
to ρ ∈ {δθ , θ ∈ Θ}. This gives, for λ = n/ max(2K, C),
ES Eθ∼ρ̂λ [R(θ)] − R(θ ) ≤ 2 inf
∗

θ∈Θ



max(2K, C) log(M )
R(θ) − R(θ ) +
n
∗


.

In particular, for θ = θ∗ , this becomes:
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ ) +

2 max(2K, C) log(M )
.
n

Note that the rate log(M )/n from Example 2.1 becomes log(M )/n
under Bernstein assumption.
p

Example 4.6 (Lipschitz loss and Gaussian priors). We now tackle the
setting of Example 2.2 under Bernstein assumption with constant K.
Let us remind that Θ = Rd , θ 7→ ℓ(fθ (x), y) is L-Lipschitz for any (x, y),
and π = N (0, σ 2 Id ). We apply Theorem 4.3, for λ = n/ max(2K, C):
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ )
+2

max(2K, C)KL(ρ∥π)
R(θ) − R(θ ) +
.
n



inf

ρ = N (m, s2 Id )
m ∈ Rd , s > 0



∗

Following the same derivations as in Example 2.2, with m = θ∗ ,
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ )


√

+ 2 inf Ls d +

max(2K, C)

n

∥θ∗ ∥2
+ d2
2σ 2

h 2

2
s
+ log σs2 − 1
σ2

io 

n

s>0

.

Here√again, we would seek for the exact optimizer in s, but for example
s = d/n we obtain:
ES Eθ∼ρ̂λ [R(θ)]


≤ R(θ∗ ) + 2 

Ld
+
n

max(2K, C)

n

∥θ∗ ∥2
+ d2
2σ 2

n

h

d
n2 σ 2

2 2

+ log σ dn

io 


242

PAC-Bayes Oracle Inequalities and Fast Rates

that is
2d max(2K, C)
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ ) +
log
n
2
"

σ 2 n2
d

∗

!

d
+L+
2nσ 2

#

max(2K, C)∥θ∗ ∥2
nσ 2


d log(n)
.
= R(θ∗ ) + O
n
+

Example 4.7 (Lipschitz loss and Uniform priors). We propose a variant of
the previous example, with a different prior. We still assume Bernstein
assumption with constant K, θ 7→ ℓ(fθ (x), y) is L-Lipschitz for any
(x, y), and this time Θ = {θ ∈ Rd : ∥θ∥ ≤ B} and π is uniform on Θ. We
apply Theorem 4.3 with λ = n/ max(2K, C) and restrict the infimum to
ρ = U (θ0 , s) the uniform distribution on {θ : ∥θ − θ0 ∥ ≤ s} = B(θ0 , s).
We obtain:
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ )
+2

max(2K, C)KL(ρ∥π)
R(θ) − R(θ ) +
.
n



inf

ρ = U (θ0 , s)
θ0 ∈ Rd , s > 0



∗

For any s > 0, there exists θ0 ∈ Θ such that θ∗ ∈ B(θ0 , s) ⊂ Θ and we
have:
Eθ∼U (θ0 ,s) [R(θ) − R(θ∗ )] ≤ Ls,
so

∗

ES Eθ∼ρ̂ [R(θ)] ≤ R(θ ) + 2 inf Ls +
λ

max(2K, C)d log

 
B
s

n

s>0

.

The minimum of the right-hand side is exactly reached for s = max(2K,C)d
Ln
and we obtain, for n large enough (in order to ensure that s ≤ B):
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ ) +

2 max(2K, C)d log
n



eBLn
max(2K,C)



.

We will end this section by a (non-exhaustive!) list of more sophisticated models where a rate of convergence was derived thanks to an
oracle PAC-Bayes inequality:

4.3. APPLICATIONS OF THEOREM 4.3

243

• model selection: for classification, see Catoni (2004, Chapter 5),
and Catoni (2007). The minimization procedure in Example 2.3
above is not always optimal. A selection based on Lepski’s procedure (Lepski, 1992) and PAC-Bayes bounds is used by Catoni
(2007) for classification and by Alquier (2008) for general losses.
• density estimation (Catoni, 2004, Chapter 4).
• scoring/ranking (Ridgway et al., 2014).
• least-square regression (Catoni, 2004, Chapter 5) and robust variants (Audibert and Catoni, 2011; Catoni and Giulini, 2017).
• sparse linear regression: Dalalyan and Tsybakov (2008) prove
a rate of convergence similar to the one of the LASSO for the
Gibbs posterior, under more general assumptions. Dalalyan and
Tsybakov (2012), Alquier and Lounici (2011), and Dalalyan et al.
(2018) provided many variants and improvements, see also Luu
et al. (2019) for group-sparsity.
• single-index regression, in small dimension (Gaïffas and Lecué,
2007), and in high-dimension, with sparsity (Alquier and Biau,
2013).
• additive non-parametric regression (Guedj and Alquier, 2013).
• matrix regression (Suzuki, 2012; Alquier, 2013; Dalalyan et al.,
2018; Dalalyan, 2020; Mai, 2023a).
• matrix completion: continuous case (Mai and Alquier, 2015; Mai,
2017; Mai, 2023b) and binary case (Cottet and Alquier, 2018);
more generally tensor completion can be tackled with related
techniques (Suzuki, 2015).
• quantum tomography (Mai and Alquier, 2017).
• deep learning (Chérief-Abdellatif, 2020; Steffen and Trabs, 2022).
• estimation of the Gram matrix for PCA (Catoni and Giulini, 2017;
Zhivotovskiy, 2021) and kernel-PCA (Giulini, 2018; Haddouche
et al., 2020).

244
4.4

PAC-Bayes Oracle Inequalities and Fast Rates
Dimension and Rate of Convergence

Let us recap the examples seen so far (Sections 2 and 4). In each case,
we were able to prove a result of the form:
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ ) + raten (π) where raten (π) −−−→ 0
n→∞

for an adequate choice of λ > 0. The way raten (π) depends on Θ
characterizes the difficulty of learning predictors in Θ when using the
prior π: it is similar to other approaches in learning theory, where the
learning rate depends on the “complexity of Θ”. More precisely (we
remind that all the results seen so far are for a bounded loss function):
• when Θ is finite and π is uniform, raten (π) is in log(M )/n in
general, and in log(M )/n under Bernstein condition.
p

• when Θ = Rd and π = N (0, σ 2 Id ), it is in [∥θ∗ ∥2 + d log(n)]/n
in general, and in [∥θ∗ ∥2 + d log(n)]/n under Bernstein condition.
p

• still when Θ = Rd , Dalalyan and Tsybakov (2008) proposed a
heavy-tailed prior π (multivariate Student). Then, raten (π) is in
p
[log ∥θ∗ ∥ + d log(n)]/n in general, and in [log ∥θ∗ ∥ + d log(n)]/n
under Bernstein condition (this is left as an exercise to the reader).
• when Θ is a compact subset of Rd and π is uniform, raten (π)
p
is in d log(n)/n in general, and in d log(n)/n under Bernstein
condition.
The calculations leading to these results are in Examples 2.2, 4.6 and 4.7.
A closer look at these examples reveals a common strategy: we assumed
conditions ensuring that it is possible to write
inf

ρ∈P(Θ)



Eθ∼ρ [R(θ) − R(θ∗ )] +

d
β
KL(ρ∥π)
≤ log
β
β
c


 

(4.7)

for some constants c and d (d being actually the dimension of the
model). Then, we can plug this inequality into Theorem 4.1, or when
Bernstein assumption is satisfied, into Theorem 4.3, to obtain a rate
of convergence. Let us now turn this into a formal statement under
Bernstein assumption (the case without Bernstein assumption is left as
an exercise to the reader).

4.4. DIMENSION AND RATE OF CONVERGENCE

245

Theorem 4.4. Assume that there are constants β0 , cπ and dπ such that,
for any β ≥ β0 ,
β
KL(ρ∥π)
≤ dπ log
β inf Eθ∼ρ [R(θ) − R(θ )] +
β
cπ
ρ∈P(Θ)




∗





(4.8)

.

Under Bernstein condition with constant K > 0, with λ = n/ max(2K,
C), we have as soon as λ ≥ β0 ,
2dπ max(2K, C) log

ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ ) +



n
cπ max(2K,C)

n



.

The proof is direct, by pluging (4.8) into Theorem 4.3 with λ = β.
Let us finally dicsuss a connection between the assumption in (4.8)
and other classical assumptions in Bayesian statistics and machine
learning. A first direct remark, based on Lemma 2.2, is that (4.8) is
equivalent to
n

−β[R(θ)−R(θ∗ )]

f (β) := − log Eθ∼π e

o

β
≤ dπ log
cπ




.

If the inequality was actually an equality, we would have f ′ (β) = dπ /β,
that is, βf ′ (β) = dπ . Actually, f ′ (β) = Eθ∼π−βR [R(θ) − R(θ∗ )] (this is
proven in the proof of Lemma 4.5 below). This motivated the following
definition (Catoni, 2007, (1.5) page 10).
Definition 4.2. We say that Catoni’s dimension assumption is satisfied
for dimension dπ > 0 if
sup βEθ∼π−βR [R(θ) − R(θ∗ )] = dπ .
β≥0

Lemma 4.5. Under Catoni’s dimension assumption with dimension dπ ,
for any β ≥ β0 = dπ /C,
n

−β[R(θ)−R(θ∗ )]

− log Eθ∼π e

o

eCβ
≤ dπ log
dπ




.

In other words, if Catoni’s dimension assumption is safisfied, then the
assumption of Theorem 4.4 given by (4.8) is satisfied with cπ = dπ /(eC).
Proof: Define

∗

f (ξ) = − log Eθ∼π e−ξ[R(θ)−R(θ )]

246

PAC-Bayes Oracle Inequalities and Fast Rates

for any ξ ≥ 0. First, note that
f (0) = − log Eθ∼π e0 = − log(1) = 0.
Moreover, we can check that f is differentiable and that
n

f ′ (ξ) =

∗

Eθ∼π [R(θ) − R(θ∗ )]e−ξ[R(θ)−R(θ )]

o

Eθ∼π e−ξ[R(θ)−R(θ∗ )]


= Eθ∼π−ξR [R(θ) − R(θ∗ )]
dπ
≤
ξ
where we used Definition 4.2 for the last inequality. This inequality is
quite tight for large ξ, but useless when ξ → 0. In this case, we will
rather use the (simpler) inequality:
n

f ′ (ξ) =

∗

Eθ∼π [R(θ) − R(θ∗ )]e−ξ[R(θ)−R(θ )]
Eθ∼π e−ξ[R(θ)−R(θ∗ )]


n

≤

o

∗

Eθ∼π Ce−ξ[R(θ)−R(θ )]

o

Eθ∼π e−ξ[R(θ)−R(θ∗ )]


= C.
Combining both bounds, f ′ (ξ) ≤ min(C, dπ /ξ). Integrating for 0 ≤ ξ ≤
β gives:
f (β) = f (β) − f (0)
=
≤

Z β
0

f ′ (ξ)dξ

Z dπ
C

0

Cdξ +

Z β
dπ
C

dπ
dξ
ξ

dπ
dπ
=C
+ dπ log(β) − dπ log
C
C


eCβ
= dπ log
.□
dπ


Another classical condition is as follows.



4.5. GETTING RID OF THE log TERMS: CATONI’S LOCALIZATION
TRICK
247
Definition 4.3. We say that the prior mass condition is satisfied with
constants c and dπ if there is r0 > 0 such that, for any r ≤ r0 ,
∗

π({θ ∈ Θ : R(θ) − R(θ ) ≤ r}) ≥

 dπ
r

c

.

This type of condition is classical to analyze the asymptotics of
Bayesian estimators in statistics (Ghosal and Van der Vaart, 2017).
Lemma 4.6. Under the prior mass condition with constants c and dπ ,
(4.8) is satisfied with cπ = dπ /(ec), for any β ≥ β0 = dπ /r0 .
Proof: The proof mimics the strategy of Example 4.7, but in a more
general setting. We define, for any r > 0, ρr as the restriction of π to
{θ ∈ Θ : R(θ) − R(θ∗ ) ≤ r}. Then,
KL(ρ∥π)
f (β) = inf Eθ∼ρ [R(θ) − R(θ )] +
β
ρ∈P(Θ)


KL(ρ
∥π)
r
≤ inf Eθ∼ρ [R(θ) − R(θ∗ )] +
r>0
β




≤ inf r +
r>0

∗

1
log π({θ∈Θ:R(θ)−R(θ
∗ )≤r})

β




.

We put r = dπ /β. Note that as β ≥ dπ /r0 , r ≤ r0 and thus
dπ log rc
dπ
dπ
cβ
=
+
log
f (β) ≤ r +
β
β
β
dπ


4.5



dπ
ecβ
=
log
β
dπ




. □

Getting Rid of the log Terms: Catoni’s Localization Trick

We have seen in Subsection 3.3 Catoni’s idea to replace the prior by
π−βR for some β > 0, where π−βR is given by Definition 4.2. This
technique is called “localization of the bound” by Catoni. Used in
empirical bounds, this trick can lead to tighter bound. We will study
its effect on oracle bounds. Let us start by providing a counterpart of
Theorem 4.3 using this trick (with β = λ/4).
Theorem 4.7. Assume that Bernstein condition holds for some K > 0,
and take λ = n/ max(2K, C). Then

248

PAC-Bayes Oracle Inequalities and Fast Rates

ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}
≤

inf




ρ∈P(Θ) 



3Eθ∼ρ [R(θ) − R(θ∗ )] +



4 max(2K, C)KL ρ∥π− λ R 
4

n

.



Before we give the proof, we will show a striking consequence: the
log(n) terms in the last bullet point in the list of rates of convergence
can be removed:
• when Catoni’s dimension dπ < ∞, raten (π) is in dπ /n in general,
and in dπ /n under Bernstein condition, if we use a localized bound.
p

Indeed, take ρ = π− λ R = π−{n/[4 max(2K,C)]}R in the right-hand side of
4
Theorem 4.7:
0
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )} ≤ 3Eθ∼π λ [R(θ) − R(θ∗ )] + .
−4R
n
Using Definition 4.2 we obtain the following corollary.
Corollary 4.8. Assume that Catoni’s dimension condition is satisfied
with dimension dπ > 0. Assume that Bernstein condition holds for some
K > 0, and take λ = n/ max(2K, C), then:
ES Eθ∼ρ̂λ [R(θ)] ≤ R(θ∗ ) +

12dπ max(2K, C)
.
n

We can also briefly detail the consequence of the bound in the finite
case.
Example 4.8 (The finite case). When card(Θ) = M is finite and π is
uniform on Θ, Theorem 4.7 applied to ρ = δθ∗ gives:
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}


≤

4 max(2K, C)KL δθ∗ ∥π− λ R



4

n
P
λ
∗
4 max(2K, C) log θ∈Θ e− 4 [R(θ)−R(θ )]
=
n
n
P
−
[R(θ)−R(θ∗ )]
4 max(2K, C) log θ∈Θ e 4 max(2K,C)
=
.
n

(4.9)

4.5. GETTING RID OF THE log TERMS: CATONI’S LOCALIZATION
TRICK
249
Of course, we have:
X −
n
[R(θ)−R(θ∗ )]
4 max(2K,C)

e

≤M

θ∈Θ

and thus we recover the rate in log(M )/n:
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )} ≤

4 max(2K, C) log(M )
.
n

On the other hand, in some situations, we can do better from (4.9). Fix
a threshold τ > 0 and define mτ = card({θ ∈ Θ : R(θ) − R(θ∗ ) ≤ τ }) ∈
{1, . . . , M }. Then we obtain the bound:
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}


≤

4 max(2K, C) log mτ + e

nτ
− 4 max(2K,C)



(M − mτ )

n

which will be much smaller for large n. A similar result was obtained
using a different technique by Lecué and Mendelson (2013).
Proof of Theorem 4.7: we follow the proof of Theorem 4.3 until (4.5)
that we remind here:
ES eλ{[1−Kg( n ) n ][R(θ)−R(θ )]−r(θ)+r(θ )} ≤ 1.
λC



λ

∗

∗



Now, we integrate this with respect to π−βR for some β > 0 and use
Fubini:
ES Eθ∼π−βR eλ{[1−Kg( n ) n ][R(θ)−R(θ )]−r(θ)+r(θ )} ≤ 1
λC



λ

∗

∗



and Donsker and Varadhan’s formula:
ES exp

sup
ρ∈P(Θ)

(

λEθ∼ρ

λC
1 − Kg
n




λ
[R(θ) − R(θ∗ )]
n


)

!!

− r(θ) + r(θ∗ ) − KL(ρ∥π−βR )

≤ 1.

250

PAC-Bayes Oracle Inequalities and Fast Rates

At this point, we write explicitly
dρ
(θ)
dπ−βR

"

KL(ρ∥π−βR ) = Eθ∼ρ log

!#

∗

Eϑ∼π [e−β[R(ϑ)−R(θ )] ]
dρ
(θ)
dπ
e−β[R(θ)−R(θ∗ )]

"

= Eθ∼ρ log

!#

= KL(ρ∥π) + βEθ∼ρ [R(θ) − R(θ∗ )]
∗

+ log Eϑ∼π [e−β[R(ϑ)−R(θ )] ]
which, plugged in the last formula, gives:
(

ES exp λ sup

1 − Kg

Eθ∼ρ

ρ∈P(Θ)



λC
n



λ β
−
[R(θ) − R(θ∗ )]
n λ


)

−β[R(ϑ)−R(θ∗ )]

∗

− r(θ) + r(θ ) − KL(ρ∥π) − log Eϑ∼π [e

!!

]

≤ 1.

We apply Jensen and rearrange terms to obtain, for any randomized
estimator ρ̂,


1 − Kg



λC
n

λ β
−
ES {Eθ∼ρ̂ [R(θ)] − R(θ∗ )}
n λ


KL(ρ̂∥π)
∗
≤ ES Eθ∼ρ̂ [r(θ)] − r(θ ) +
λ




h

+

∗

log Eϑ∼π e−β[R(ϑ)−R(θ )]

i

.
λ
Here again, the r.h.s. is minimized for ρ̂ = ρ̂λ the Gibbs posterior, and
we obtain:
"

λC
1−Kg
n




#

λ β
−
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}
n λ

(

≤ ES

KL(ρ∥π)
inf Eθ∼ρ [r(θ)] − r(θ ) +
λ
ρ∈P(Θ)


∗

h

+
≤

inf

ρ∈P(Θ)

∗

log Eϑ∼π e−β[R(ϑ)−R(θ )]



i

λ
KL(ρ∥π)
Eθ∼ρ [r(θ)] − r(θ ) +
λ



ES

)

∗



4.5. GETTING RID OF THE log TERMS: CATONI’S LOCALIZATION
TRICK
251
h

+

∗

log Eϑ∼π e−β[R(ϑ)−R(θ )]

i

λ

KL(ρ∥π)
= inf Eθ∼ρ [R(θ)] − R(θ ) +
λ
ρ∈P(Θ)


∗

h

+
=

inf



ρ∈P(Θ)

∗

log Eϑ∼π e−β[R(ϑ)−R(θ )]

i

λ

β
Eθ∼ρ [R(θ) − R(θ )] 1 −
λ
∗







KL(ρ∥π−βR )
+
λ



where we used again the formula on KL(ρ∥π−βR ) for the last step. So,
for β and λ such that
λC
Kg
n




λ β
− <1
n λ

we have:
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}


≤

inf



1 − βλ Eθ∼ρ [R(θ) − R(θ∗ )] +
1 − Kg

ρ∈P(Θ)



λC
n



KL(ρ∥π−βR )
λ

β
λ
n − λ

.

For example, for λ = n/ max(2K, C) we have already seen that


Kg

λC
n



λ
1
≤
n
2

and taking β = λ/4 leads to
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}


≤

inf

3
∗
4 Eθ∼ρ [R(θ) − R(θ )] +

ρ∈P(Θ)

max(2K,C)KL ρ π− λ R



4

n

1 − 34

that is
ES {Eθ∼ρ̂λ [R(θ)] − R(θ∗ )}
≤

inf




3Eθ∼ρ [R(θ) − R(θ∗ )] +

ρ∈P(Θ) 

which ends the proof. □





4 max(2K, C)KL ρ π− λ R 
4

n



252

PAC-Bayes Oracle Inequalities and Fast Rates

We refer the reader to Mourtada et al. (2023) for more recent results
on localization. We end up this section with the following comment
page 15 in Catoni’s book (Catoni, 2007): “some of the detractors of
the PAC-Bayesian approach (which, as a newcomer, has sometimes
received a suspicious greeting among statisticians) have argued that it
cannot bring anything that elementary union bound arguments could
not essentially provide. We do not share of course this derogatory
opinion, and while we think that allowing for non atomic priors and
posteriors is worthwhile, we also would like to stress that the upcoming
local and relative bounds could hardly be obtained with the only help
of union bounds”.

5
Beyond “Bounded Loss” and “i.i.d. Observations”

If you follow the proof of the PAC-Bayesian inequalities seen so far, you
will see that the “bounded loss” and “i.i.d. observations” assumptions
are used only to apply Lemma 1.1 (Hoeffding’s inequality) or Lemma 3.8
(Bernstein’s inequality). In other words, in order to prove PAC-Bayes
inequalities for unbounded losses or dependent observations, all we need
is a result similar to Hoeffding or Bernstein’s inequalities (also called
exponential moment inequalities) in this context.
In the past 15 years, many variants of PAC-Bayes bounds were
developped for various applications based on this remark. In this section,
we provide some pointers. In the end, some authors now prefer to
assume directly that the data is such that it satisfies a given exponential
inequality. One of the merits of Theorem 3.6 above, from Germain et al.
(2009), is to make it very explicit: the exponential moment appears
in the bound. A similar approach is used by Alquier et al. (2016): a
“Hoeffding assumption” and a “Bernstein assumption” are defined, that
corresponds to data satisfying a Hoeffding type inequality, or a Bernstein
type inequality + the usual Bernstein condition (Definition 4.1). A
similar point of view is used by Rivasplata et al. (2020).

253

254

Beyond “Bounded Loss” and “i.i.d. Observations”

Remark 5.1. It is possible to prove a PAC-Bayes inequality like Theorem 2.1 starting directly from (2.2), that is, assuming that an exponential moment inequality is satisfied in average under the prior π,
rather than uniformly on θ. We will not develop this approach here,
examples are detailed by Alquier et al. (2016), Haddouche et al. (2021),
and Rivasplata et al. (2020).
5.1

“Almost” Bounded Losses (Sub-Gaussian and Sub-gamma)

5.1.1

The sub-Gaussian case

Hoeffding’s inequality for n = 1 variable U1 taking values in [a, b] simply
states that


t2 (b−a)2
E et[U1 −E(U1 )] ≤ e 8 .
Then the general case is obtained by:
 Pn

E e

t

[U −E(Ui )]
i=1 i



=E

n
Y

!
t[Ui −E(Ui )]

e

i=1

=
≤

n
Y
i=1
n
Y



E et[Ui −E(Ui )]
e



(by independence)

t2 (b−a)2
8

i=1

=e

nt2 (b−a)2
8

.

Alternatively, if we simply assume that, for some C > 0,




2

E et[U1 −E(U1 )] ≤ eCt

(5.1)

for some constant C, similar derivations lead to:
 Pn

E et

i=1

[Ui −E(Ui )]



2

≤ enCt ,

on which we can build PAC-Bayes bounds. We can actually rephrase
Hoeffding’s inequality by: “if U1 takes values in [a, b], then (5.1) is
satisfied for C = (b − a)2 /8”.
It appears that (5.1) is satisfied by some unbounded variables. For
example, it is well known that, if Ui ∼ N (m, σ 2 ) then




σ 2 t2

E et[U1 −E(U1 )] = e 2 ,

5.1. “ALMOST” BOUNDED LOSSES (SUB-GAUSSIAN AND
SUB-GAMMA)

255

that is (5.1) with C = σ 2 /2. Actually, it can be proven that a variables
U1 will satisfy (5.1) if and only if its tails P(|U1 | ≥ t) converge to
zero (when t → ∞) as fast as the ones of a Gaussian variable, that is
P(|U1 | ≥ t) ≤ exp(−t2 /C ′ ) for some C ′ > 0, see e.g. Chafaï et al. (2012,
Chapter 1). This is the reason behind the following terminology.
Definition 5.1. A random variable U such that




2

E et[U −E(U )] ≤ eCt

for some finite C is called a sub-Gaussian random variable (with constant
C).
Based on this definition, we can state for example the following
variant of Theorem 2.1 that will be valid for (some!) unbounded losses.
Theorem 5.1. Assume that for any θ the ℓi (θ) are independent and
sub-Gaussian random variables with constant C. Then for any δ ≥ 0,
for any λ > 0,
PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)]
λC 2 KL(ρ∥π) + log 1δ
+
+
n
λ

!

≥ 1 − δ.

(We don’t provide the proof as all the ingredients were explained to
the reader).
For example, the PAC-Bayes bounds of Alquier et al. (2016) were
explicitly stated for sub-Gaussian losses.
5.1.2

The sub-gamma case

We will not provide details, but variables satisfying inequalities similar
to Bernstein’s inequality are called sub-gamma random variables, sometimes sub-exponential random variables. A possible characterization
is: P(|U1 | ≥ t) ≤ exp(−t/C ′ ) for some C ′ > 0. Such variables include:
gamma (and exponential) random variables, Gaussian variables and
bounded variables.

256

Beyond “Bounded Loss” and “i.i.d. Observations”

Boucheron et al. (2013, Chapter 2) provide a very detailed and
pedagogical overview of exponential moment inequalities for independent
random variables, and in particular we refer the reader to their Section
2.4 for more details on sub-gamma variables (but I have to warn you,
this book is so cool you will find difficult to stop at the end of Chapter
2 and will end up reading everything).
In the literature, PAC-Bayes bounds for sub-gamma random variables can be found as early as 2001, see Catoni (2004, Chapter 5). These
are these bounds that are used to prove minimax rates in various parametric and non-parametric problems in the aforementioned (Alquier
and Biau, 2013; Mai and Alquier, 2015; Steffen and Trabs, 2022).
5.1.3

Remarks on exponential moments

Finally, exponential moments inequalities for random variables such
that P(|U1 | ≥ t) ≤ exp(−tα /C ′ ) where α ≥ 1 are studied by Chafaï
et al. (2012, Chapter 1). The set of such variables is called an Orlicz
space.
Still, all these random variables are defined in such a way that
they satisfy more or less the same exponential inequalities as bounded
variables. And indeed, for these variables, P(|U1 | ≥ t) is very small when
t is large – hence the title of this section: almost bounded variables. We
will now discuss briefly how to go beyond this case.
5.2

Heavy-tailed Losses

By heavy-tailed variables, we mean typically random variables U1 such
that P(|U1 | ≥ t) is for example in t−α for some α > 0.
5.2.1

The truncation approach

In my PhD thesis (Alquier, 2006), I studied a truncation technique for
general losses ℓi (θ). That is, write:
ℓi (θ) = ℓi (θ)1(ℓi (θ) ≤ s) + ℓi (θ)1(ℓi (θ) > s)
for some s > 0. The first term is bounded by s, so we can use exponential moments inequalities on it, while I used inequalities on the tails

5.2. HEAVY-TAILED LOSSES

257

P(|ℓi (θ)| ≥ s) to control the second term. For the sake of completeness
I state one of the bounds obtained by this technique (with s = n/λ).
Theorem 5.2 (Corollary 2.5, Alquier (2006)). Define
∆n,λ (θ) = E(X,Y )∼P
and



n
max ℓ(fθ (X), Y ) − , 0
λ


n
n
1X
Ψ λ min ℓ(fθ (Xi ), Yi ),
r̃λ,n (θ) =
n i=1 n
λ









,

where
Ψα (u) :=

− log(1 − uα)
1 − e−αv
and thus Ψ−1
(v)
=
.
α
α
α

Then, for any δ > 0, for any λ > 0,
PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)]
KL(ρ∥π) + log 1δ
Eθ∼ρ [r̃λ,n (θ)] +
λ

(
−1

≤ Ψλ

n

)

!

+ Eθ∼ρ [∆n,λ (θ)]
≥ 1 − δ.

Note that r̃λ,n (θ) is an approximation of r(θ) when λ/n is small
√
enough (usually λ ∼ n in this bound). The function Ψα plays a role
similar to the function Φα in Catoni’s bound (Theorem 3.5), and more
explicit inequalities can be derived by upper-bounding Ψ−1
α . Finally,
∆n,λ (θ) corresponds to the tails of the loss function. Actually, for a
bounded loss, we will have ∆n,λ (θ) = 0 for n/λ large enough. In the subexponential setting, ∆n,λ (θ) > 0 but will usually not be the dominant
term in the right-hand side. However, Alquier (2006) also provided upper
bounds on ∆n,λ (θ) in O((λ/n)s−1 ) where s is such that E(ℓsi ) < +∞,
but this terms is dominant in this case (and thus, it slows down the rate
of convergence). This truncation argument is reused by Alquier (2008)
but only the oracle bounds are provided there. Seldin and Tishby (2010)
used distribution smoothing as an alternative truncation approach to
truncate the unbounded log-loss in density estimation.

258

Beyond “Bounded Loss” and “i.i.d. Observations”

5.2.2

Bounds based on moment inequalities

Based on techniques developped of Honorio and Jaakkola (2014) and
Bégin et al. (2016), Alquier and Guedj (2018) proved inequalities similar
to PAC-Bayes bounds, that hold for heavy-tailed losses (they can also
hold for non i.i.d. losses, we will discuss this point later). Curiously,
these bounds depend no longer on the Kullback-Leibler divergence, but
on other divergences. An example of such an inequality is provided here
and relies only on the assumption that the losses have a variance. We
recall a notation from Section 3: V(θ) = Var(ℓi (θ)).
Theorem 5.3 (Corollary 1, Alquier and Guedj (2018)). Assume that the
ℓi (θ) are independent and such that V(θ) ≤ κ < ∞. Then, for any
δ > 0,


s

PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)] +



κ (1 + χ2 (ρ∥π)) 
nδ
≥ 1 − δ,

where χ2 (ρ∥π) is the chi-square divergence:
χ2 (ρ∥π) =

 




 R dρ (θ) 2 − 1 π(dθ) if ρ ≪ π, and
dπ


 χ2 (ρ∥π) = +∞ otherwise.

Interestingly, the minimization of the bound with respect to ρ
leads to an explicit solution (Alquier and Guedj, 2018). However the
dependence of the rate in δ is much worse than in Theorem 2.1. This
was later dramatically improved by Ohnishi and Honorio (2021). As for
the truncation approach described earlier, this approach leads to slow
rates of convergence for heavy-tailed variables.
5.2.3

Bounds based on robust losses

Catoni (2012) proposed a robust loss function ψ used to estimate the
mean of heavy-tailed random variables (this is based on ideas from an
earlier paper by Audibert and Catoni, 2011). As a result, Catoni (2012)
obtains, for the mean of heavy-tailed variables, confidence intervals very
similar to the ones of estimators of the mean of a Gaussian.

5.2. HEAVY-TAILED LOSSES

259

More recently, Holland (2019) derives a full PAC-Bayesian theory
for possibly heavy-tailed losses based on Catoni’s technique. The idea
is as follows. Put

√
√
−2 2


if u < − 2,

3
√
√
3
ψ(u) =
u√− u6 if − 2 ≤ u ≤ 2,


 2 2 otherwise
3
and, for any s > 0,
X
ℓi (θ)
s n
ψ
.
rψ,s (θ) =
n i=1
s




The idea is that, even when ℓi (θ) is unbounded, the new version of the
risk, rψ,s (θ), is bounded. Thus, the study of the deviations of rψ,s (θ)
can be done with the standard tools for bounded losses. There is some
additional work to connect ES [rψ,s (θ)] to R(θ) for a well chosen s, and
Holland (2019) obtains the following result.
Theorem 5.4 (Theorem 9, Holland (2019)). Let δ > 0. Assume that the
ℓi (θ) are independent and
• E(ℓi (θ)2 ) ≤ M2 < +∞ and E(ℓi (θ)3 ) ≤ M3 < +∞,
• for any θ ∈ Θ, R(θ) ≤

p

nM2 /(4 log(1/δ)),

• δ ≤ e−1/9 ≃ 0.89,
and put

h √

∗
πn,s
(Θ) =

Eθ∼π e n[R(θ)−rψ,s (θ)]
h

Eθ∼π eR(θ)−rψ,s (θ)

i

i

then, for s := nM2 /[2 log(1/δ)],
PS ∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)]

≤ Eθ∼ρ [rψ,s (θ)] +

KL(ρ∥π) + M2 +

log

√

8πM2
δ2

2



∗ (Θ) − 1
+ πn,s

!

n
≥ 1 − δ.

260

Beyond “Bounded Loss” and “i.i.d. Observations”

On the contrary to Theorem 5.3 above, the bound is very similar
to the one in the bounded case (heavy-tailed variables do not lead to
slower rates). In particular, we have a good dependence of the bound
in δ, and the presence of KL(ρ∥π) that is much smaller than χ2 (ρ∥π).
The only notable difference is the restriction in the range of δ (which
is of no consequence in practice), and the term πn∗ (Θ). Unfortunately,
as discussed by Holland (2019, Remark 10), this term will deterioriate
the rate of convergence when the ℓi (θ) are not sub-Gaussian (to my
knowledge, it is not known if it will lead to better or worse rates than
the ones obtained through truncation).
5.3
5.3.1

Dependent Observations
Inequalities for dependent variables

There are versions of Hoeffding and Bernstein’s inequalities for dependent random variables, under various assumptions on this dependence.
This can be used in the case where the observations are actually a time
series, or a random field.
For example, we learnt auto-regressive predictors of the form X̂t =
fθ (Xt−1 , . . . , Xt−k ) for weakly dependent time series with a PAC-Bayes
bound (Alquier and Wintenberger, 2012). The proof relies on Rio’s
version of Hoeffding’s inequality (Rio, 2000). In our work, only slow
√
rates in 1/ n are provided. Fast rates in 1/n were proven in a subsequent
paper (Alquier et al., 2013) for (less general) mixing time series thanks
to Samson’s version of Bernstein’s inequality (Samson, 2000).
More exponential moment inequalities (and moment inequalities) for
dependent variables can be found in the survey by Wintenberger (2010)
and in monographs dedicated to weak dependence (Dedecker et al.,
2007). Other time series models where PAC-Bayes bounds were used
include martingales (Seldin et al., 2012b), Markov chains (Banerjee et
al., 2021a), continuous dynamical systems (Haußmann et al., 2021), LTI
systems (Eringis et al., 2021). Concentration inequalities on martingales
are a very important tool to derive PAC-Bayes bounds in this context.
Interestingly, they also allow to derive bounds that can hold when the
sample size n is not deterministic but instead might be chosen based on

5.3. DEPENDENT OBSERVATIONS

261

the observations seen so far (that is, n is a stopping time), as observed
by Chugg et al. (2023).
5.3.2

An example

The weak-dependence conditions are quite general but they are also quite
difficult to understand and the definitions are sometimes cumbersome.
We only provide a much simpler example based on a more restrictive
assumption, α-mixing. This result is due to Alquier and Guedj (2018)
and extends Theorem 5.3 to time series.
Definition 5.2. Given two σ-algebras F and G, we define
α(F, G) = sup{Cov(U, V ); 0 ≤ U ≤ 1, U is F-measurable,
0 ≤ V ≤ 1, V is G-measurable}.
Observe that if F and G are independent, α(F, G) = 0.
Definition 5.3. Given a time series U = (Ut )t∈Z we define its α-mixing
coefficients by
∀h ∈ Z, αh (U ) = sup α(σ(Ut ), σ(Ut+h )).
t∈N

Theorem 5.5 (Corollary 2, Alquier and Guedj (2018)). Let X = (Xt )t∈Z
be a real-valued stationary time series. Define, for θ = (θ1 , θ2 ) ∈ R2 ,
ℓt (θ) = (Xt − θ1 − θ2 Xt−1 )2 and R(θ) = EX [ℓt (θ)] (it does not depend
on t as the series is stationary). Define
r(θ) =

n
X

ℓt (θ)

t=1

the empirical risk based on the observation of (X0 , . . . , Xn ). Assume
the prior π is chosen such that
Z

∥θ∥6 π(dθ) ≤ M6 < +∞

(for example a Gaussian prior). Assume that X the α-mixing coefficients
of X satisfy:
X
1
[αt (X)] 3 ≤ A < +∞.
t∈Z

262

Beyond “Bounded Loss” and “i.i.d. Observations”
2

Assume that E(Xt6 ) ≤ C < +∞. Define ν = 32C 3 A(1 + 4M6 ). Then,
for any δ > 0,
r
PS

5.4
5.4.1

∀ρ ∈ P(Θ), Eθ∼ρ [R(θ)] ≤ Eθ∼ρ [r(θ)] +

ν (1 + χ2 (ρ∥π))
nδ

!
≥ 1 − δ.

Other Non i.i.d. Settings
Non identically distributed observations

When the data is independent, but non-identically distributed, that is,
(Xi , Yi ) ∼ Pi , we can still introduce
r(θ) =

n
n
1X
1X
ℓi (θ) =
ℓ(fθ (Xi ), Yi )
n i=1
n i=1

and
R(θ) = E[r(θ)] =

1X
E
[ℓ(fθ (Xi ), Yi )].
n i=1 (Xi ,Yi )∼Pi

The proofs of most exponential inequalities still hold in this setting (for
example, Hoeffding inequality when the losses are bounded). Based on
this remark, all the results of Catoni (2007) are written for independent,
but not necessarily identically distributed observations. Of course, if
we actually have Pi = P for any i, we recover the usual case R(θ) =
E(X,Y )∼P [ℓ(fθ (X), Y )].
5.4.2

Shift in the distribution

A common problem in machine learning practice is the shift in distribution: one learns a classifier based on i.i.d. observations (Xi , Yi ) ∼ P . But
in practice, the data to be predicted are drawn from another distribution Q, that is: R(θ) = E(X,Y )∼Q [ℓ(fθ (X), Y )] ̸= E(X,Y )∼P [ℓ(fθ (X), Y )].
There is still a lot of work to do to address this practical problem, but
an interesting approach is proposed by Germain et al. (2016b): the
authors use a technique called domain adaptation to allow the use of
PAC-Bayes bounds in this context.

5.4. OTHER NON I.I.D. SETTINGS
5.4.3

263

Meta-learning

Meta-learning is a scenario when one solves many machine learning
tasks simulataneously, and the objective is to improve this learning
process for yet-to-come tasks. A popular formalization (but not the
only one possible) is:
• each task t ∈ {1, . . . , T } corresponds to a probability distribution
Pt . The Pt ’s are i.i.d. from some P.
• for each task t, an i.i.d. sample (X1t , Y1t ), . . . , (Xnt , Ynt ) is drawn
from Pt . Thus, we observe the empirical risk of task t:
n
1X
rt (θ) =
ℓ(fθ (Xit ), Yit )
n i=1

and use PAC-Bayes bounds to learn a good θt for this task.
• based on the data of tasks {1, . . . , T }, we want to improve the
learning process for a yet non-observed task PT +1 ∼ P.
This improvement differs from one application to the other, for example:
learn a better parameter space ΘT +1 ⊂ Θ, learn a better prior, learn
better hyperparameters like λ... PAC-Bayes bounds for meta-learning
were studied by Pentina and Lampert (2014), Amit and Meir (2018),
Jose and Simeone (2021), Rothfuss et al. (2021), Liu et al. (2021a),
Meunier and Alquier (2021), Liu et al. (2021b), Foong et al. (2021),
Rezazadeh (2022), Riou et al. (2023), and Sucker and Ochs (2023). I
believe PAC-Bayes bound are particularly convenient for meta-learning
problems, and thus that this direction of research is very promising.

6
Related Approaches in Statistics and Machine
Learning Theory

In this section, we list some connections between PAC-Bayes theory
and other approaches in statistics and machine learning. We will mostly
provide references, and will use mathematics more heuristically than in
the previous sections. Note that these connections are well-known and
were discussed in the literature, see for example Banerjee (2006).
6.1

Bayesian Inference in Statistics

In Bayesian statistics, we are given a sample X1 , . . . , Xn assumed to
be i.i.d. from some Pθ∗ in a model {Pθ , θ ∈ Θ}. A prior π is given on
the parameter set Θ. When each Pθ has a density pθ with respect to a
given measure, the likelihood function is defined by
L(θ; X1 , . . . , Xn ) :=

n
Y

pθ (Xi ).

i=1

According to the Bayesian paradigm, all the information on the parameter that can be inferred from the sample is in the posterior distribution
π(dθ|X1 , . . . , Xn ) = R

L(θ; X1 , . . . , Xn )π(dθ)
.
L(ϑ; X1 , . . . , Xn )π(dϑ)

264

6.1. BAYESIAN INFERENCE IN STATISTICS

265

A direct remark is that π(dθ|X1 , . . . , Xn ) can be seen as a Gibbs
posterior. Indeed, as
" n
Y

#

Pn

pθ (Xi ) π(dθ) = e

i=1

log pθ (Xi )

π(dθ)

i=1

we can define the loss ℓi (θ) = − log pθ (Xi ) and the corresponding
empirical risk is the negative log-likelihood:
r(θ) =

n
1X
[− log pθ (Xi )],
n i=1

and we have
π(·|X1 , . . . , Xn ) = π−nr
(

= argmin Eθ∼ρ
ρ∈P(Θ)

"

n
1X
KL(ρ∥π)
[− log pθ (Xi )] +
n i=1
n

#

)

.

(6.1)
This connection is for example discussed by Audibert (2004) and Germain et al. (2016a). Note, however, that log-likelihoods are rarely
bounded, which prevents to use the simplest PAC-Bayes bounds to
study the consistency of π(dθ|X1 , . . . , Xn ).
6.1.1

Gibbs posteriors, generalized posteriors

Independently from the PAC-Bayes community, the Bayesian statistics
community proposed to generalize the posterior, by replacing the loglikelihood by minus a risk function. Often, the resulting generalised
posterior is called a Gibbs posterior. This is done for example by Jiang
and Tanner (2008) and Syring and Martin (2019) in order to estimate
some parameters of the distributions of the data without having to
model the whole distribution. Another instance of such generalized
posteriors are fractional, or tempered posteriors, π−αnr , where r is the
negative log-likelihood and α < 1. Grünwald and Van Ommen (2017)
proved that in some contexts where the posterior π(dθ|X1 , . . . , Xn )
is not consistent, a tempered posterior for α small enough will be.
Gibbs posteriors are discussed in a decision theoretic framework by
Bissiri et al. (2016). An asymptotic study of Gibbs posteriors, using

266

Related Approaches in Statistics and Machine Learning Theory

different arguments than PAC-Bayes bounds (but related), is provided
by Syring and Martin (2023) and some the references therein. Finally,
Bhattacharya et al. (2019, Theorem 3.4) proved a PAC-Bayes bound
for tempered posteriors.
6.1.2

Contraction of the posterior in Bayes nonparametrics

A very active field of research is the study of the contraction of the posterior in Bayesian statistics: the objective is to prove that π(dθ|X1 , . . . , Xn )
concentrates around the true parameter θ∗ when n → ∞. We refer the
reader to Rousseau (2016) and Ghosal and Van der Vaart (2017) on
this topic, see also Banerjee et al. (2021b) on high-dimensional models
specifically. Usually, such results require two assumptions:
• a technical condition, the existence of tests to discriminate between
members of the model {Pθ , θ ∈ Θ},
• and the prior mass condition, which states that enough mass
is given by the prior to a neighborhood of θ∗ . In other words,
π({θ : d(θ, θ∗ ) ≤ r}) does not converge too fast to 0 when r → 0,
for some distance or risk measure d. For example, we can assume
that there is a sequence rn → 0 when n → ∞ such that
π({θ : d(θ, θ∗ ) ≤ rn }) ≥ e−nrn .

(6.2)

The prior mass condition is to be compared to Definition 4.3 above.
We can actually use the prior mass condition in conjunction with PACBayes bounds, instead of Definition 4.3, to show that the bound is small.
For example consider the PAC-Bayes inequality of Theorem 4.3: under
a Bernstein condition with constant K and for a well chosen λ,
(
∗

ES Eθ∼ρ̂λ [R(θ)] − R(θ ) ≤ 2 inf

ρ∈P(Θ)

Eθ∼ρ [R(θ)] − R(θ∗ )
max(2K, C)KL(ρ, π)
+
.
n
)

Assume that the prior mass condition holds with d(θ, θ∗ ) = R(θ)−R(θ∗ )
and take
π(dθ)1({d(θ, θ∗ ) ≤ rn })
ρ(dθ) =
.
π({θ : d(θ, θ∗ ) ≤ rn })

6.1. BAYESIAN INFERENCE IN STATISTICS

267

We obviously have:
Eθ∼ρ [R(θ)] − R(θ∗ ) ≤ rn
and a direct calculation gives
KL(ρ∥π) = − log π({θ : d(θ, θ∗ ) ≤ rn }) ≤ nrn
so the bound becomes:
ES Eθ∼ρ̂λ [R(θ)] − R(θ∗ ) ≤ 2[1 + max(2K, C)]rn −−−→ 0.
n→∞

Bhattacharya et al. (2019, Theorem 3.1) proved the contraction of
tempered posteriors their PAC-Bayes bound for tempered posteriors
together with a prior mass condition.
6.1.3

Variational approximations

In many applications where the dimension of Θ is large, sampling from
π(dθ|X1 , . . . , Xn ) becomes a very difficult task. In order to overcome this
difficulty, a recent trend is to approximate this probability distribution
by a tractable approximation. Formally, we would chose a set F of
probability distributions (for example, Gaussian distributions with
diagonal covariance matrix) and define the following approximation of
the posterior:
ρ̂ = argmin KL(ρ∥π(·|X1 , . . . , Xn )).
ρ∈F

This is called a variational approximation in Bayesian statistics, we
refer the reader to Blei et al. (2017) for recent survey on the topic. Note
that, by definition of π(dθ|X1 , . . . , Xn ) we also have
(

ρ̂ = argmin Eθ∼ρ
ρ∈F

"

X
1 n
KL(ρ∥π)
[− log pθ (Xi )] +
n i=1
n
#

)

that is, a restricted version of (6.1).
This leads to two remarks:
• non-exact minimization of PAC-Bayes bounds, as in Subsection 2.1.3, can be interpreted as variational approximations of

268

Related Approaches in Statistics and Machine Learning Theory
Gibbs posteriors. Note that this is also the case of the Gaussian
approximation that was used for neural networks in (Dziugaite
and Roy, 2017). This led to a systematic study of the consistency
of variational approximation via PAC-Bayes bounds (Alquier et
al., 2016; Sheth and Khardon, 2017).

• on the other hand, little was known at that time on the theoretical
properties of variational approximations of the posterior in statistics. Using the fact that variational approximations of tempered
posteriors are constrained minimizers of the PAC-Bayes bound
of Bhattacharya et al. (2019), we studied the consistency of such
approximations (Alquier and Ridgway, 2020). As a byproduct we
have a generalization of the prior mass condition for variational
inference (Alquier and Ridgway, 2020, (2.1) and (2.2)). These
results were extended to the standard posterior π(dθ|X1 , . . . , Xn )
by Yang et al. (2020) and Zhang and Gao (2020).
More theoretical studies on variational inference (using PAC-Bayes, or
not) appeared at the same time or since (Chérief-Abdellatif and Alquier,
2018; Huggins et al., 2018; Masegosa, 2020; Cherief-Abdellatif, 2019;
Plummer et al., 2020; Chérief-Abdellatif et al., 2019; Banerjee et al.,
2021a; Avena Medina et al., 2021; Ohn and Lin, 2021; Frazier et al.,
2021).
The most general version of (6.1) we are aware of is:
D(ρ∥π)
ρ̂ = argmin Eθ∼ρ [r(θ)] +
n
ρ∈F




(6.3)

where D is any distance or divergence between probability distributions.
Here, the Bayesian point of view is generalized in three directions:
1. the negative log-likelihood is replaced by a more general notion
of risk r(θ), as in PAC-Bayes bounds and in Gibbs posteriors,
2. the minimization over P(Θ) is replaced by the minimization over
F, in order to keep things tractable, as in variational inference,
3. finally, the KL divergence is replaced by a general D. Note that
this already happened in Theorem 5.3 above.

6.2. EMPIRICAL RISK MINIMIZATION

269

This triple generalization, and the optimization point of view on Bayesian statistics is strongly advocated in Knoblauch et al. (2022) (in
particular reasons to replace KL by D are given in this paper that seem
to me more relevant in practice than Theorem 5.3).
In this spirit, Rodríguez-Gálvez et al. (2021) and Chee and Loustau
(2021) provided PAC-Bayes type bounds where D is the Wasserstein
distance.
Remark 6.1. When D ̸= KL, (6.3) is no longer necessarily equivalent
to
ρ̂ = argmin D (ρ∥π(·|X1 , . . . , Xn )) .
(6.4)
ρ∈F

Knoblauch et al. (2022) discusses why (6.3) is a more natural generalization, and Geffner and Domke (2020) shows that (6.4) leads to
difficult minimization problems. Note however that there are also some
theoretical results on (6.4) by Jaiswal et al. (2020).
6.2

Empirical Risk Minimization

We already pointed out in the introduction the link between empirical
risk minimization (based on PAC bounds) and PAC-Bayes.
When the parameter space Θ is not finite as in Theorem 1.2 above,
the log(M ) term is replaced by a measure of the complexity of Θ called
the Vapnik-Chervonenkis dimension (VC-dim). We simply mention that
Catoni (2003, Section 2) and Catoni (2007, Chapter 3, page 115–130)
builds a well-chosen data dependent prior such that the VC-dim of
Θ appears explicitly in the PAC-Bayes bound. However, Livni and
Moran (2020) provide an example where the VC dimension is finite,
yet the PAC-Bayes approach fails. This problem was solved recently
by Grünwald et al. (2021) thanks to “conditional PAC-Bayes bounds”.
This is discussed below together with Mutual Information bounds.
Similarly, generalization bounds for Support Vectors Machines are
based on a quantity called the margin. This quantity can also appear
in PAC-Bayes bounds (Langford and Shawe-Taylor, 2002; Herbrich and
Graepel, 2002; Catoni, 2007; Biggs and Guedj, 2022).
Audibert and Bousquet studied a PAC-Bayes version of the chaining
argument (Audibert and Bousquet, 2007). See also versions based on
Mutual Information bounds (Asadi et al., 2018; Clerico et al., 2022c).

270

Related Approaches in Statistics and Machine Learning Theory

Finally, Kakade et al. (2008) and Yang et al. (2019) proved PACBayes bounds using Rademacher complexity.
6.3

Non-Bayesian Estimators

More generally, Catoni developped recently a technique to prove upper
bound on the risk of non-Bayesian estimators that relies on PACBayes bounds. Given an estimator m̂ of some vector m∗ ∈ Rd , put
Bd = {v ∈ Rd : ∥v∥ ≤ 1}, then
∥m̂ − m∗ ∥ = sup ⟨v, m̂ − m∗ ⟩
v∈Bd

=

sup ⟨Ev∼ρ [v], m̂ − m∗ ⟩
ρ∈P(Bd )

=

sup

n

o

Ev∼ρ [⟨v, m̂⟩] − Ev∼ρ [⟨v, m∗ ⟩] .

ρ∈P(Bd )

Thus, we can work with PAC-Bayes bound to control ∥m̂ − m∗ ∥. The
technique is detailed by Catoni and Giulini (2017) to provide robust
estimation of the Gram matrix (for PCA), an infinite-dimensional
version for kernel-PCA was then provided by Giulini (2018). This builds
on earlier work on robust estimation Audibert and Catoni (2011) and
Catoni (2012). More results on the estimation of the covariance matrix
were proven since using this technique (Zhivotovskiy, 2021; Nakakita
et al., 2022).
6.4
6.4.1

Online Learning
Sequential prediction

Sequential classification focuses on the following problem. At each time
step t,
• a new object xt is revealed,
• the forecaster must propose a prediction ŷt of the label of yt ,
• the true label yt ∈ {0, 1} is revealed and the forecaster incurs a
loss ℓ(ŷt , yt ), and updates his/her knowledge.

6.4. ONLINE LEARNING

271

Similarly, online regression and other online prediction problems are
studied.
Prediction strategies are often evaluated through upper bounds on
the regret Reg(T ) given by:
Reg(T ) :=

T
X

ℓ(ŷt , yt ) − inf ℓ(fθ (xt ), yt )
θ

t=1

where {fθ , θ ∈ Θ} is a family of predictors as in Section 1 above.
However, a striking point is that most regret bounds hold without any
stochastic assumption on the data (xt , yt )t=1,...,T : they are not assumed
to be independent nor to have any link whatsoever with any statistical
model. On the other hand, assumptions on the function θ 7→ ℓ(fθ (xt ), yt )
are unavoidable (depending on the strategies: boundedness, Lipschitz
condition, convexity, strong convexity, etc.).
A popular strategy, strongly related to the PAC-Bayesian approach,
is the exponentially weighted average (EWA) forecaster, also known as
weighted majority algorithm or multiplicate update rule (Littlestone
and Warmuth, 1989; Vovk, 1990; Cesa-Bianchi et al., 1997; Kivinen and
Warmuth, 1999) (we also refer to Barzdinš and Freivalds (1974) on the
halving algorithm that can be seen as an ancestor of this method). This
strategy is defined as follows. First, let ρ1 = π be a prior distribution
on Θ, and fix a learning rate η > 0. Then, at each time step t:
• the prediction is given by
ŷt = Eθ∼ρt [fθ (x)],
• when yt is revealed, we update
ρt+1 (dθ) = R

e−ηℓ(fθ (x),yt ) ρt (dθ)
.
−ηℓ(fϑ (x),yt ) ρ (dϑ)
t
Θe

We provide here a simple regret bound from Cesa-Bianchi and Lugosi
(2006) (stated for a finite Θ but the extension is direct). Note the formal
analogy with PAC-Bayes bounds.

272

Related Approaches in Statistics and Machine Learning Theory

Theorem 6.1. Assume that, for any t, 0 ≤ ℓ(fθ (xt ), yt ) ≤ C (bounded
loss assumption) and θ 7→ ℓ(fθ (xt ), yt ) is a convex function. Then, for
any T > 0,
T
X

(

ℓ(ŷt , yt ) ≤

t=1

inf

ρ∈P(Θ)

ηC 2 T
KL(ρ∥π)
Eθ∼ρ [ℓ(fθ (xt ), yt )] +
+
8
η

)

.

In particular, when Θ is finite with card(Θ) = M and π is uniform, the
restriction of the infimum to Dirac masses leads to
T
X

ℓ(ŷt , yt ) ≤ inf ℓ(fθ (xt ), yt ) +
θ∈Θ

t=1

and thus with η = C2

q

log(M )
ηC 2 T
+
8
η

2 log(M )
,
T

s

Reg(T ) ≤ C

T log(M )
.
2

Choices of η that do not depend on the time horizon T are possible (Cesa-Bianchi and Lugosi, 2006). Smaller regret bounds, up to log(T )
or even constants, are known under stronger assumptions (Cesa-Bianchi
and Lugosi, 2006; Audibert, 2009). We refer the reader to Shalev-Shwartz
(2011) and Orabona (2019) for more up to date introductions to online
learning.
While there is no stochastic assumption on the data in Theorem 6.1,
it is possible to deduce inequalities in probability or in expectation from
it under an additional assumption (for example, the assumption that
the data is i.i.d.). This is described for example in Shalev-Shwartz (2011,
Chapter 5), but does not always lead to optimal rates. For more up-todate discussion on this topic with more general results, see Bilodeau
et al. (2021). It is also possible to use tools from sequential predictions
to derive PAC-Bayes bounds (Jang et al., 2023).
Finally, we mention that many other strategies than EWA are
studied: online gradient algorithm, follow-the-regularized-leader (FTRL),
online mirror descent (OMD)... EWA is actually derived as a special
case of FTRL and OMD in many references (Shalev-Shwartz, 2011)
and conversely, Hoeven et al. (2018) and Khan and Rue (2021) derive
OMD and online gradient as approximations of EWA. Regret bounds for

6.5. AGGREGATION OF ESTIMATORS IN STATISTICS

273

variational approximations of EWA were proved by Chérief-Abdellatif
et al. (2019). More generally, Haddouche and Guedj (2022) and Lugosi
and Neu (2021) proved PAC-Bayes regret bounds, that allow to recover
regret bounds for EWA, variational approximations and potentially more
methods. Here, we point out a similarity to Section 2: we remarked
that one can use PAC-Bayes inequalities to provide generalization error
bounds on non-Bayesian methods like the ERM. Haddouche and Guedj
(2023) and Rodrígues-Gálvez et al. (2023) recently used this approach
to prove PAC-Bayes bounds with heavy-tailed losses.
6.4.2

Bandits and reinforcement learning (RL)

Other online problems received considerable attention in the past few
years. In bandits, the forecaster only receives feedback on the loss
of his/her prediction, but not on the losses what he/she would have
incurred under other predictions. We refer the reader to Bubeck and
Cesa-Bianchi (2012) for an introduction to bandits. Note that some
strategies used for bandits are derived from EWA. Some authors derived
strategies or regret bounds directly from PAC-Bayes bounds (Seldin
et al., 2011; Seldin et al., 2012a). There are also PAC-Bayes bounds for
offline bandits (London and Sandler, 2019; Sakhi et al., 2023; Aouali et
al., 2023). Bandits themself are a subclass of a larger family of learning
problems: reinforcement learning (RL). PAC-Bayes bounds or related
generalization bounds for RL were derived by Wang et al. (2019) and
Tasdighi et al. (2023).
6.5

Aggregation of Estimators in Statistics

Given a set E of statistical estimators, the aggregation problem consists
of finding a new estimator, called the aggregate, that would perform
as well as the best estimator in E, see Nemirovski (2000) for a formal
definition and variants of the problem. The optimal rates are derived by
Tsybakov (2003). Many aggregates share a formal similarity with the
EWA of online learning and with the Gibbs posterior of the PAC-Bayes
approach (Nemirovski, 2000; Juditsky and Nemirovski, 2000; Yang,
2001; Meir and Zhang, 2003; Yang, 2004; Catoni, 2004; Zhang, 2006;

274

Related Approaches in Statistics and Machine Learning Theory

Leung and Barron, 2006; Lecué, 2007; Dalalyan and Tsybakov, 2008;
Bunea and Nobel, 2008; Suzuki, 2012; Dalalyan and Tsybakov, 2012;
Dai et al., 2012; Dalalyan and Salmon, 2012; Dai et al., 2014; Dalalyan
et al., 2018; Luu et al., 2019; Dalalyan, 2020). In some of these papers,
the connection to PAC-Bayes bounds is explicit, for example Dalalyan
and Tsybakov (2008, Theorem 1), which is actually an oracle PAC-Bayes
bound in expectation. It leads to fast rates in the spirit of Theorem 4.3,
but with different assumptions (in particular, the Xi ’s are not random
there).
6.6

Information Theoretic Approaches

A note on the terminology: a huge number of statistical and machine
learning results mentioned above rely on tools from information theory:
Zhang (2006) actually proves beautiful PAC-Bayesian bounds under
the name “information theoretic bounds” (maybe for this reason, it’s
not always listed with the other PAC-Bayes bounds in the publications
on the topic). My goal here is not to classify what should be called
“PAC-Bayes” and what should not, I’m certainly not qualified for that.
I simply want to point out the connection to two families of methods
inspired directly from information theory.
6.6.1

Minimum description length

In Rissanen’s Minimum Description Length (MDL) principle, the idea
is to penalize the empirical error of a classifier by its shortest description (Rissanen, 1978). We refer the reader to Barron et al. (1998) and
Grünwald (2007) for more recent presentations of this very fruitful
approach. Note that given a prefix-free code on a finite alphabet Θ, it
is possible to build a probability distribution π(θ) ≃ 2−L(θ) where L(θ)
is the length of the code of θ, so codes provide a way to define priors in
PAC-Bayes bounds, see for example Catoni (2004, Chapter 1).
6.6.2

Mutual information bounds (MI)

Recently, some generalization error bounds appeared where the complexity is measured in terms of the mutual information between the
sample and the estimator.

6.6. INFORMATION THEORETIC APPROACHES

275

Definition 6.1. Let U and V be two random variables with joint probability distribution PU,V . Let PU and PV denote the marginal distribution
of U and V respectively. The mutual information (MI) between U and
V is defined as:
I(U, V ) := KL(PU,V ∥PU ⊗ PV ).
Russo and Zou (2019) introduced generalization error bounds (in
expectation) that depend on the mutual information between the predictors and the labels. In particular, when fˆ is obtained by empirical
risk minimization, they recover bounds depending of the VC-dimension
of Θ.
Russo and Zou’s result was improved and extended by Raginsky et
al. (2016) and Xu and Raginsky (2017). In particular, Xu and Raginsky
(2017, Subsection 4.3) proved a powerful MI inequality, from which
many existing and new results can be derived. Unfortunately, it is not
pointed out that the results on Gibbs posteriors could also be obtained
directly from a PAC-Bayes bound in expectation such as Theorem 2.8
above. Thus, the connection between information bounds and PACBayes bounds might have been missed by part of the information bounds
community (in the same way that part of the PAC-Bayes community
might have missed the “information theoretic bounds” of Zhang (2006)).
It turns out that Langford and Blum (2003) discussed the minimization of a PAC-Bayes bound in expectation (such as Theorem 2.8
above) with respect to the prior π. We will see below that the optimal
prior turns out to be π−λR (which is the prior that appears in Catoni’s
localized bounds such as Theorem 4.7 above). This idea also appears
in Catoni (2007, page 14 and 51), where it is also noticed that the
optimized KL term boils down to the mutual information between the
sample and the parameter. All these derivations will be detailed below,
and essentially lead to an inequality similar to the one of Russo and
Zou (2019).
More recent work on MI bounds mention explicitly the connection
to PAC-Bayes bounds (Negrea et al., 2019; Dziugaite et al., 2021a;
Banerjee and Montúfar, 2021). Let us for example cite a result state
by Negrea et al. (2019), or rather, a simplified version (by setting their
parameter m to 0).

276

Related Approaches in Statistics and Machine Learning Theory

Theorem 6.2 (Theorem 2.3, Negrea et al. (2019), with m = 0). Using
the notations and assumptions of Section 1, assume that the losses ℓi (θ)
are sub-Gaussian with parameter C, then, for any data-dependent ρ̃,
s
n

o

ES Eθ∼ρ̃ [R(θ)] − Eθ∼ρ̃ [r(θ)] ≤

2CI(θ, S)
≤
n

s

2CES [KL(ρ̃∥π)]
.
n

A few comments on this result:
• the first inequality is from Xu and Raginsky (2017, Theorem 1).
Note however that Theorem 2.3 of Negrea et al. (2019) contains
more information, as setting their parameter m ̸= 0 allows to
get a data-dependent prior. The paper contains more new results,
and a beautiful application to derive empirical bounds on the
performance of stochastic gradient descent (SGD). On this topic,
see also the recent works by Bu et al. (2020), Haghifam et al.
(2020), Wang et al. (2021), Neu et al. (2021), and Haghifam et al.
(2023).
• we can see here that the MI bound
s
n

o

ES Eθ∼ρ̃ [R(θ)] − Eθ∼ρ̃ [r(θ)] ≤

2CI(θ, S)
n

(6.5)

is tighter than the the PAC-Bayes bound in expectation
s
n

o

ES Eθ∼ρ̃ [R(θ)] − Eθ∼ρ̃ [r(θ)] ≤

2CES [KL(ρ̃∥π)]
.
n

(6.6)

However, an MI bound cannot be used as is in practice. Indeed,
I(θ, S) depends on the distribution of the sample S that is unknown in practice. In order to use (6.5), one must upper bound
I(θ, S) by a quantity that does not depend on the sample.
• Catoni (2007, page 14 and 51) discuss the optimization of PACBayes bounds with respect to
√ the prior. In order to explain the
discussion done there, apply ab ≤ a/(2λ) + bλ/2 to (6.6) to get
a “Catoni style” bound:
n

o

ES Eθ∼ρ̃ [R(θ)] − Eθ∼ρ̃ [r(θ)] ≤

Cλ ES [KL(ρ̃∥π)]
+
2n
λ

6.6. INFORMATION THEORETIC APPROACHES

277

and thus
ES Eθ∼ρ̃ [R(θ)] ≤ ES



Cλ KL(ρ̃∥π)
Eθ∼ρ̃ [r(θ)] +
+
2n
λ



(compare to Theorem 2.8 above). Let ρ̃ be any data-dependent
measure that is absolutely continuous with respect to π almostsurely, thus
dρ̃
(θ)
dπ
is well-defined. Catoni defines ES (ρ̃) the probability measure
defined by


dES (ρ̃)
dρ̃
(θ) = ES
(θ) .
dπ
dπ
Direct calculations show that ES [KL(ρ̃∥π)] = ES [KL(ρ̃∥ES (ρ̃))] +
KL(ES (ρ̃)∥π) = I(θ, S) + KL(ES (ρ̃)∥π) and thus:
ES Eθ∼ρ̃ [R(θ)] ≤ ES {Eθ∼ρ̃ [r(θ)]}+

Cλ I(θ, S) + KL(ES (ρ̃)∥π)
+
.
2n
λ

So the choice to replace π by ES (ρ̃) gives the MI bound:
ES Eθ∼ρ̃ [R(θ)] ≤ ES {Eθ∼ρ̃ [r(θ)]} +
The choice λ =

Cλ I(θ, S)
+
.
2n
λ

2nI(θ, S)/C leads to

p

s

ES Eθ∼ρ̃ [R(θ)] ≤ ES {Eθ∼ρ̃ [r(θ)]} +

2CI(θ, S)
.
n

In other words, MI bounds can be seen as PAC-Bayes bounds
optimized with respect to the prior. Of course, as we said above,
MI bound cannot be computed in practice. Catoni proposes an
interpretation of his localization technique as taking the prior π−βR
to approximate ES (π−λr ), and then to upper bound KL(ρ∥π−βR )
via empirical bounds. As we have seen in Section 3, this leads to
empirical bounds with data-dependent priors, and in Section 4, this
leads to improved PAC-Bayes oracle bounds. All this is pointed
out by Grünwald et al. (2021): “Catoni already mentions that the
prior that minimizes a MAC-Bayesian bound is the prior that
turns the KL term into the mutual information”.

278

Related Approaches in Statistics and Machine Learning Theory

Similarly to PAC-Bayesian bounds, MI bounds can be stated with
other divergences than KL (Lugosi and Neu, 2022).
Thanks to MI bounds, it is also possible to provide an exact formula
(not an upper bound) for the generalization error of the Gibbs posterior
in terms of the symmetrized version of the KL bound (Aminian et al.,
2021).
Since Bassily et al. (2018) and Nachum et al. (2018), it is known
that MI bounds can fail in some situations where the VC dimension
is finite: thus, they suffer the same limitation as PAC-Bayes bounds
proven by Livni and Moran (2020). Recently, expanding on ideas from
the PAC-Bayes literature (Audibert, 2004; Catoni, 2007; Mhammedi
et al., 2019) and in the MI literature (Steinke and Zakynthinou, 2020;
Hellström and Durisi, 2020), Grünwald et al. (2021) unified MI bounds
and PAC-Bayes bounds, an they developped “conditional” MI and PACBayes bounds. Note in particular that conditional PAC-Bayes bounds
are based on the notion of “exchangeable priors” introduced by Catoni
(2003, Chapter 2 page 31), see also Audibert (2004, page 105) and
developped by Catoni (2007, Definition 3.1.1 page 11) under the name
“exchangeable posteriors” (to highlight the fact that these distributions
can be data-dependent).
The bounds of Grünwald et al. (2021) are proven to be small for
any set of classifiers with finite VC dimension. Thus, they don’t suffer
the limitations of PAC-Bayes and MI bounds of Bassily et al. (2018),
Nachum et al. (2018), and Livni and Moran (2020). To cite the results
of Grünwald et al. (2021) would go beyond the framework of this “easy
introduction”, but one of the main point of this tutorial is to prepare
the reader not familiar with PAC-Bayes bounds, Bernstein assumption
etc. to read this work. Recent work on sharp mutual information bounds
and their connection to minimax rates in classification include Haghifam
et al. (2021) and Haghifam et al. (2022).

7
Conclusion

We hope that the reader:
• has a better view of what a PAC-Bayes bound is, and what can
be done with such a bound,
• is at least a little convinced that these bounds are quite flexible,
that they can be used in a wide range of contexts, and for different
objectives in ML,
• wants to read many of the references listed above, that provide
tighter bounds and clever applications.
I believe that PAC-Bayes bounds (and all the related approaches, including mutual information bounds, etc.) will play an important role in
the study of deep learning, in the wake of Dziugaite and Roy (2017),
in RL (Wang et al., 2019) and in meta-learning (Pentina and Lampert,
2014; Amit and Meir, 2018; Rothfuss et al., 2021).

279

Acknowledgements

First, a huge “thank you” to both anonymous referees for their careful
reading of this manuscript. Their insightful comments helped a lot to
improve it.
My PhD advisor Olivier Catoni taught me PAC-Bayes bounds, and
so much more.
Of course I learn also about PAC-Bayes and related topics from all
my co-authors, friends, students and twitter pals... that I will not even
try to make a list. Thanks to all of you, you know who you are!
Still, I would like to thank specifically, for motivating, providing
valuable feedback and helping to improve the manuscript (since the
very first draft of Section 2): Mathieu Alain, Pradeep Banerjee, Wessel
Bruinsma, David Burt, Badr-Eddine Chérief-Abdellatif, Nicolas Chopin,
Arnak Dalalyan, Andrew Foong, Natalie Frank, Avrajit Ghosh, Avetik
Karagulyan, Aryeh Kontorovich, The Tien Mai, Thomas Möllenhoff,
Peter Nickl, Donlapark Ponnoprat, Charles Riou, and Alexandre Tsybakov. A very first draft of Section 2 was started in September-October
2008 as I was invited at ENSAE by Alexandre Tsybakov to give talks
on PAC-Bayes bounds. I taught a course on PAC-Bayes bounds and
online learning at ENSAE Paris from 2014 to 2019, partially based on
this preliminary version. I should thank all students for enduring this.
Most of the document was written when I was working at RIKEN AIP
(Tokyo) in the Approximate Bayesian Inference team led by Emtiyaz
Khan: I thank Emti and the whole team for their support.
280

References

Alquier, P. (2006). “Transductive and inductive adaptative inference for
regression and density estimation”. PhD thesis, University Paris 6.
Alquier, P. (2008). “PAC-Bayesian bounds for randomized empirical risk
minimizers”. Mathematical Methods of Statistics. 17(4): 279–304.
Alquier, P. (2013). “Bayesian methods for low-rank matrix estimation:
short survey and theoretical study”. In: International Conference
on Algorithmic Learning Theory. Springer. 309–323.
Alquier, P. and G. Biau. (2013). “Sparse single-index model.” Journal
of Machine Learning Research. 14(1).
Alquier, P. and B. Guedj. (2018). “Simpler PAC-Bayesian bounds for
hostile data”. Machine Learning. 107(5): 887–902.
Alquier, P., X. Li, and O. Wintenberger. (2013). “Prediction of time series by statistical learning: general losses and fast rates”. Dependence
Modeling. 1(2013): 65–93.
Alquier, P. and K. Lounici. (2011). “PAC-Bayesian bounds for sparse
regression estimation with exponential weights”. Electronic Journal
of Statistics. 5: 127–145.
Alquier, P. and J. Ridgway. (2020). “Concentration of tempered posteriors and of their variational approximations”. Annals of Statistics.
48(3): 1475–1497.

281

282

REFERENCES

Alquier, P., J. Ridgway, and N. Chopin. (2016). “On the properties of
variational approximations of Gibbs posteriors”. Journal of Machine
Learning Research. 17(239): 1–41.
Alquier, P. and O. Wintenberger. (2012). “Model selection for weakly
dependent time series forecasting”. Bernoulli. 18(3): 883–913.
Ambroladze, A., E. Parrado-hernández, and J. Shawe-taylor. (2006).
“Tighter PAC-Bayes bounds”. In: Advances in Neural Information
Processing Systems. Ed. by B. Schölkopf, J. Platt, and T. Hoffman.
Vol. 19. MIT Press.
Aminian, G., Y. Bu, L. Toni, M. R. D. Rodrigues, and G. Wornell. (2021).
“Characterizing the deneralization error of Gibbs algorithm with
symmetrized KL information”. arXiv preprint arXiv:2107.13656.
Amit, R. and R. Meir. (2018). “Meta-learning by adjusting priors based
on extended PAC-Bayes theory”. In: International Conference on
Machine Learning. PMLR. 205–214.
Aouali, I., V.-E. Brunel, D. Rohde, and A. Korba. (2023). “Exponential
Smoothing for Off-Policy Learning”. In: Proceedings of the 40th
International Conference on Machine Learning. Ed. by A. Krause,
E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett.
Vol. 202. Proceedings of Machine Learning Research. PMLR. 984–
1017.
Appert, G. and O. Catoni. (2021). “New bounds for k-means and
information k-means”. arXiv preprint arXiv:2101.05728.
Asadi, A., E. Abbe, and S. Verdu. (2018). “Chaining mutual information and tightening generalization bounds”. In: Advances in Neural
Information Processing Systems. Ed. by S. Bengio, H. Wallach, H.
Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett. Vol. 31.
Curran Associates, Inc.
Audibert, J.-Y. (2004). “PAC-Bayesian statistical learning theory”. PhD
thesis, Université Paris VI.
Audibert, J.-Y. (2009). “Fast learning rates in statistical inference
through aggregation”. The Annals of Statistics. 37(4): 1591–1646.
Audibert, J.-Y. and O. Bousquet. (2007). “Combining PAC-Bayesian
and generic chaining bounds”. Journal of Machine Learning Research.
8(4).

REFERENCES

283

Audibert, J.-Y. and O. Catoni. (2011). “Robust linear least squares
regression”. The Annals of Statistics. 39(5): 2766–2794.
Avena Medina, M., J. L. Montiel Olea, C. Rush, and A. Velez. (2021).
“On the robustness to misspecification of α-posteriors and their
variational approximations”. arXiv preprint arXiv:2104.08324.
Banerjee, A. (2006). “On Bayesian bounds”. In: Proceedings of ICML.
ACM. 81–88.
Banerjee, I., V. A. Rao, and H. Honnappa. (2021a). “PAC-Bayes bounds
on variational tempered posteriors for Markov models”. Entropy.
23(3): 313.
Banerjee, P. K. and G. Montúfar. (2021). “Information complexity and
generalization bounds”. In: 2021 IEEE International Symposium on
Information Theory (ISIT). IEEE. 676–681.
Banerjee, S., I. Castillo, and S. Ghosal. (2021b). “Bayesian inference in
high-dimensional models”. arXiv preprint arXiv:2101.04491.
Barron, A., J. Rissanen, and B. Yu. (1998). “The minimum description
length principle in coding and modeling”. IEEE Transactions on
Information Theory. 44(6): 2743–2760.
Bartlett, P. L., M. I. Jordan, and J. D. McAuliffe. (2006). “Convexity,
classification, and risk bounds”. Journal of the American Statistical
Association. 101(473): 138–156.
Bartlett, P. L. and S. Mendelson. (2006). “Empirical minimization”.
Probability theory and related fields. 135(3): 311–334.
Barzdinš, J. and R. Freivalds. (1974). “Prediction and limiting synthesis
of recursively enumerable classes of functions”. Latvijas Valsts Univ.
Zimatm. Raksti. 210: 101–111.
Bassily, R., S. Moran, I. Nachum, J. Shafer, and A. Yehudayoff. (2018).
“Learners that use little information”. In: Proceedings of Algorithmic
Learning Theory. Ed. by F. Janoos, M. Mohri, and K. Sridharan.
Vol. 83. Proceedings of Machine Learning Research. PMLR. 25–55.
Bégin, L., P. Germain, F. Laviolette, and J.-F. Roy. (2016). “PACBayesian bounds based on the Rényi divergence”. In: Artificial
Intelligence and Statistics. PMLR. 435–444.
Bhattacharya, A., D. Pati, and Y. Yang. (2019). “Bayesian fractional
posteriors”. The Annals of Statistics. 47(1): 39–66.

284

REFERENCES

Biggs, F. and B. Guedj. (2021). “Differentiable PAC–Bayes objectives
with partially aggregated neural networks”. Entropy. 23(10).
Biggs, F. and B. Guedj. (2022). “On margins and derandomisation in
PAC-Bayes”. In: International Conference on Artificial Intelligence
and Statistics. PMLR. 3709–3731.
Bilodeau, B., D. J. Foster, and D. M. Roy. (2021). “Minimax rates for
conditional density estimation via empirical entropy”. arXiv preprint
arXiv:2109.10461, to appear in the Annals of Statistics.
Bissiri, P. G., C. C. Holmes, and S. G. Walker. (2016). “A general
framework for updating belief distributions”. Journal of the Royal
Statistical Society: Series B (Statistical Methodology). 78(5): 1103–
1130.
Blanchard, G. and F. Fleuret. (2007). “Occam’s hammer”. In: International Conference on Computational Learning Theory. Springer.
112–126.
Blei, D. M., A. Kucukelbir, and J. D. McAuliffe. (2017). “Variational
inference: A review for statisticians”. Journal of the American statistical Association. 112(518): 859–877.
Boucheron, S., G. Lugosi, and P. Massart. (2013). Concentration inequalities. Oxford University Press.
Bu, Y., S. Zou, and V. V. Veeravalli. (2020). “Tightening mutual
information-based bounds on generalization error”. IEEE Journal
on Selected Areas in Information Theory. 1(1): 121–130.
Bubeck, S. and N. Cesa-Bianchi. (2012). “Regret analysis of stochastic
and nonstochastic multi-armed bandit problems”. Foundations and
Trends® in Machine Learning. 5(1): 1–122. doi: 10.1561/2200000024.
Bunea, F. and A. Nobel. (2008). “Sequential procedures for aggregating
arbitrary estimators of a conditional mean”. IEEE Transactions on
Information Theory. 54(4): 1725–1735.
Catoni, O. (2007). PAC-Bayesian supervised classification: The thermodynamics of statistical learning. Institute of Mathematical Statistics
Lecture Notes – Monograph Series, 56. Institute of Mathematical
Statistics, Beachwood, OH.
Catoni, O. (2003). “A PAC-Bayesian approach to adaptive classification”.
preprint LPMA 840.

REFERENCES

285

Catoni, O. (2004). Statistical learning theory and stochastic optimization.
Saint-Flour Summer School on Probability Theory 2001 (Jean Picard
ed.), Lecture Notes in Mathematics. Springer. 1–269.
Catoni, O. (2012). “Challenging the empirical mean and empirical
variance: a deviation study”. In: Annales de l’IHP Probabilités et
statistiques. Vol. 48. No. 4. 1148–1185.
Catoni, O. and I. Giulini. (2017). “Dimension free PAC-Bayesian bounds
for the estimation of the mean of a random vector”. In: NIPS-2017
Workshop (Almost) 50 Shades of Bayesian Learning: PAC-Bayesian
trends and insights.
Cesa-Bianchi, N., Y. Freund, D. Haussler, D. P. Helmbold, R. E.
Schapire, and M. K. Warmuth. (1997). “How to use expert advice”.
Journal of the ACM. 44(3): 427–485.
Cesa-Bianchi, N. and G. Lugosi. (2006). Prediction, learning, and games.
Cambridge university press.
Chafaï, D., O. Guédon, G. Lecué, and A. Pajor. (2012). Interactions
between compressed sensing random matrices and high dimensional
geometry. Société Mathématique de France (SMF).
Chee, A. and S. Loustau. (2021). “Learning with BOT-Bregman and
Optimal Transport divergences”. Preprint hal-03262687.
Cherief-Abdellatif, B.-E. (2019). “Consistency of ELBO maximization
for model selection”. In: Proceedings of The 1st Symposium on
Advances in Approximate Bayesian Inference. Ed. by F. Ruiz, C.
Zhang, D. Liang, and T. Bui. Vol. 96. Proceedings of Machine
Learning Research. PMLR. 11–31.
Chérief-Abdellatif, B.-E. (2020). “Convergence rates of variational inference in sparse deep learning”. In: International Conference on
Machine Learning. PMLR. 1831–1842.
Chérief-Abdellatif, B.-E. and P. Alquier. (2018). “Consistency of variational Bayes inference for estimation and model selection in mixtures”. Electronic Journal of Statistics. 12(2): 2995–3035.
Chérief-Abdellatif, B.-E., P. Alquier, and M. E. Khan. (2019). “A
generalization bound for online variational inference”. In: Proceedings
of The Eleventh Asian Conference on Machine Learning. Ed. by
W. S. Lee and T. Suzuki. Vol. 101. Proceedings of Machine Learning
Research. Nagoya, Japan. 662–677.

286

REFERENCES

Chérief-Abdellatif, B.-E., Y. Shi, A. Doucet, and B. Guedj. (2022). “On
PAC-Bayesian reconstruction guarantees for VAEs”. In: International Conference on Artificial Intelligence and Statistics. PMLR.
3066–3079.
Chopin, N., S. Gadat, B. Guedj, A. Guyader, and E. Vernet. (2015).
“On some recent advances on high dimensional Bayesian statistics”.
ESAIM: Proceedings and Surveys. 51: 293–319.
Chugg, B., H. Wang, and A. Ramdas. (2023). “A unified recipe for deriving (time-uniform) PAC-Bayes bounds”. arXiv preprint arXiv:2302.
03421.
Clerico, E., G. Deligiannidis, and A. Doucet. (2022a). “Conditionally
Gaussian PAC-Bayes”. In: International Conference on Artificial
Intelligence and Statistics. PMLR. 2311–2329.
Clerico, E., G. Deligiannidis, B. Guedj, and A. Doucet. (2022b). “A PACBayes bound for deterministic classifiers”. arXiv preprint arXiv:2209.
02525.
Clerico, E., A. Shidani, G. Deligiannidis, and A. Doucet. (2022c).
“Chained generalisation bounds”. In: Conference on Learning Theory.
PMLR. 4212–4257.
Clerico, E., A. Shidani, G. Deligiannidis, and A. Doucet. (2023). “Wide
stochastic networks: Gaussian limit and PAC-Bayesian training”. In:
International Conference on Algorithmic Learning Theory. PMLR.
447–470.
Cottet, V. and P. Alquier. (2018). “1-bit matrix completion: PACBayesian analysis of a variational approximation”. Machine Learning.
107(3): 579–603.
Dai, D., P. Rigollet, L. Xia, and T. Zhang. (2014). “Aggregation of
affine estimators”. Electronic Journal of Statistics. 8(1): 302–327.
Dai, D., P. Rigollet, and T. Zhang. (2012). “Deviation optimal learning
using greedy Q-aggregation”. The Annals of Statistics. 40(3): 1878–
1905.
Dalalyan, A. S., E. Grappin, and Q. Paris. (2018). “On the exponentially
weighted aggregate with the Laplace prior”. Annals of Statistics.
46(5): 2452–2478.

REFERENCES

287

Dalalyan, A. S. and J. Salmon. (2012). “Sharp oracle inequalities for
aggregation of affine estimators”. The Annals of Statistics. 40(4):
2327–2355.
Dalalyan, A. S. and A. B. Tsybakov. (2008). “Aggregation by exponential
weighting, sharp PAC-Bayesian bounds and sparsity”. Machine
Learning. 72(1-2): 39–61.
Dalalyan, A. S. and A. B. Tsybakov. (2012). “Sparse regression learning
by aggregation and Langevin Monte-Carlo”. Journal of Computer
and System Sciences. 78(5): 1423–1443.
Dalalyan, A. S. (2020). “Exponential weights in multivariate regression
and a low-rankness favoring prior”. Ann. Inst. H. Poincaré Probab.
Statist. 56(2): 1465–1483.
Dedecker, J., P. Doukhan, G. Lang, L. R. J. Rafael, S. Louhichi, and
C. Prieur. (2007). “Weak dependence”. In: Weak dependence: With
examples and applications. Springer. 9–20.
Devroye, L., L. Györfi, and G. Lugosi. (1996). A probabilistic theory of
pattern recognition. Springer Science & Business Media.
Donsker, M. D. and S. S. Varadhan. (1976). “Asymptotic evaluation of
certain Markov process expectations for large time. III.” Communications on Pure and Applied Mathematics. 28: 389–461.
Dziugaite, G. K., K. Hsu, W. Gharbieh, G. Arpino, and D. Roy. (2021a).
“On the role of data in PAC-Bayes bounds”. In: International Conference on Artificial Intelligence and Statistics. PMLR. 604–612.
Dziugaite, G. K. and D. M. Roy. (2017). “Computing nonvacuous
generalization bounds for deep (stochastic) neural networks with
many more parameters than training data”. In: Proceedings of the
Conference on Uncertainty in Artificial Intelligence.
Dziugaite, G. K. and D. M. Roy. (2018). “Data-dependent PAC-Bayes
priors via differential privacy”. In: Advances in Neural Information
Processing Systems. 8430–8441.
Dziugaite, G. K., K. Hsu, W. Gharbieh, G. Arpino, and D. Roy. (2021b).
“On the role of data in PAC-Bayes”. In: Proceedings of The 24th
International Conference on Artificial Intelligence and Statistics. Ed.
by A. Banerjee and K. Fukumizu. Vol. 130. Proceedings of Machine
Learning Research. PMLR. 604–612.

288

REFERENCES

Eringis, D., J. Leth, Z.-H. Tan, R. Wisniewski, and M. Petreczky. (2021).
“PAC-Bayesian theory for stochastic LTI systems”. In: IEEE. 6626–
6633.
Fleuret, F. (2011). “Machine learning, PAC-learning”. Slides available on
the author’s website. url: https://fleuret.org/public/EN_20110511pac/pac-fleuret-2011.pdf.
Foong, A. Y. K., W. P. Bruinsma, D. R. Burt, and R. E. Turner.
(2021). “How tight can PAC-Bayes be in the small data regime?”
In: Advances in Neural Information Processing Systems. Ed. by M.
Ranzato, A. Beygelzimer, Y. Dauphin, P. Liang, and J. W. Vaughan.
Vol. 34. Curran Associates, Inc. 4093–4105.
Foret, P., A. Kleiner, H. Mobahi, and B. Neyshabur. (2020). “Sharpnessaware minimization for efficiently improving generalization”. arXiv
preprint arXiv:2010.01412.
Frazier, D. T., R. Loaiza-Maya, G. M. Martin, and B. Koo.
(2021). “Loss-based variational Bayes prediction”. arXiv preprint
arXiv:2104.14054.
Gaïffas, S. and G. Lecué. (2007). “Optimal rates and adaptation in
the single-index model using aggregation”. Electronic journal of
statistics. 1: 538–573.
Geffner, T. and J. Domke. (2020). “On the difficulty of unbiased alpha
divergence minimization”. arXiv preprint arXiv:2010.09541.
Germain, P., F. Bach, A. Lacoste, and S. Lacoste-Julien. (2016a). “PACBayesian theory meets Bayesian inference”. In: Proceedings of the
30th International Conference on Neural Information Processing
Systems. 1884–1892.
Germain, P., A. Habrard, F. Laviolette, and E. Morvant. (2016b). “A new
PAC-Bayesian perspective on domain adaptation”. In: International
conference on machine learning. PMLR. 859–868.
Germain, P., A. Lacasse, F. Laviolette, and M. Marchand. (2009). “PACBayesian learning of linear classifiers”. In: Proceedings of the 26th
Annual International Conference on Machine Learning. 353–360.
Germain, P., A. Lacasse, F. Laviolette, M. Marchand, and J.-F. Roy.
(2015). “Risk bounds for the majority vote: from a PAC-Bayesian
analysis to a learning algorithm”. Journal of Machine Learning
Research. 16(26): 787–860.

REFERENCES

289

Ghosal, S. and A. Van der Vaart. (2017). Fundamentals of nonparametric
Bayesian inference. Vol. 44. Cambridge University Press.
Giraud, C. (2014). Introduction to high-dimensional statistics. CRC
Press.
Giulini, I. (2018). “Robust dimension-free Gram operator estimates”.
Bernoulli. 24(4B): 3864–3923.
Głuch, G. and R. Urbanke. (2023). “Bayes complexity of learners vs
overfitting”. arXiv preprint arXiv:2303.07874.
Grünwald, P., T. Steinke, and L. Zakynthinou. (2021). “PAC-Bayes,
MAC-Bayes and conditional mutual information: fast rate bounds
that handle general VC classes”. In: Conference on Learning Theory.
PMLR. 2217–2247.
Grünwald, P. and T. Van Ommen. (2017). “Inconsistency of Bayesian
inference for misspecified linear models, and a proposal for repairing
it”. Bayesian Analysis. 12(4): 1069–1103.
Grünwald, P. D. (2007). The minimum description length principle.
MIT press.
Grünwald, P. D. and N. A. Mehta. (2020). “Fast rates for general unbounded loss functions: From ERM to Generalized Bayes”. Journal
of Machine Learning Research. 21(56): 1–80.
Guedj, B. (2019). “A primer on PAC-Bayesian learning”. In: Proceedings
of the second congress of the French Mathematical Society.
Guedj, B. and P. Alquier. (2013). “PAC-Bayesian estimation and prediction in sparse additive models”. Electronic Journal of Statistics.
7: 264–291.
Haddouche, M. and B. Guedj. (2022). “Online PAC-Bayes Learning”.
In: Advances in Neural Information Processing Systems. Ed. by S.
Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh.
Vol. 35. Curran Associates, Inc. 25725–25738.
Haddouche, M. and B. Guedj. (2023). “PAC-Bayes generalisation bounds
for heavy-tailed losses through supermartingales”. Transactions on
Machine Learning Research.
Haddouche, M., B. Guedj, O. Rivasplata, and J. Shawe-Taylor. (2020).
“Upper and lower bounds on the performance of kernel PCA”. arXiv
preprint arXiv:2012.10369.

290

REFERENCES

Haddouche, M., B. Guedj, O. Rivasplata, and J. Shawe-Taylor. (2021).
“PAC-Bayes unleashed: generalisation bounds with unbounded
losses”. Entropy. 23(10).
Haghifam, M., G. K. Dziugaite, S. Moran, and D. Roy. (2021). “Towards
a unified information-theoretic framework for generalization”. In:
Advances in Neural Information Processing Systems. Ed. by M.
Ranzato, A. Beygelzimer, Y. Dauphin, P. Liang, and J. W. Vaughan.
Vol. 34. Curran Associates, Inc. 26370–26381.
Haghifam, M., S. Moran, D. M. Roy, and G. K. Dziugiate. (2022).
“Understanding generalization via leave-one-out conditional mutual
information”. In: 2022 IEEE International Symposium on Information Theory (ISIT). IEEE. 2487–2492.
Haghifam, M., J. Negrea, A. Khisti, D. M. Roy, and G. K. Dziugaite.
(2020). “Sharpened generalization bounds based on conditional mutual information and anapplication to noisy, iterative algorithms”.
In: Advances in Neural Information Processing Systems. Ed. by
H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin.
Vol. 33. Curran Associates, Inc. 9925–9935.
Haghifam, M., B. Rodríguez-Gálvez, R. Thobaben, M. Skoglund, D. M.
Roy, and G. K. Dziugaite. (2023). “Limitations of informationtheoretic generalization bounds for gradient descent methods in
stochastic convex optimization”. In: International Conference on
Algorithmic Learning Theory. PMLR. 663–706.
Haußmann, M., S. Gerwinn, A. Look, B. Rakitsch, and M. Kandemir.
(2021). “Learning partially known stochastic dynamics with empirical
PAC-Bayes”. In: International Conference on Artificial Intelligence
and Statistics. PMLR. 478–486.
Hellström, F. and G. Durisi. (2020). “Generalization bounds via information density and conditional information density”. IEEE Journal
on Selected Areas in Information Theory. 1(3): 824–839.
Herbrich, R. and T. Graepel. (2002). “A PAC-Bayesian margin bound
for linear classifiers”. IEEE Transactions on Information Theory.
48(12): 3140–3150.
Higgs, M. and J. Shawe-Taylor. (2010). “A PAC-Bayes bound for tailored
density estimation”. In: International Conference on Algorithmic
Learning Theory. Springer. 148–162.

REFERENCES

291

Hinton, G. E. and D. Van Camp. (1993). “Keeping the neural networks
simple by minimizing the description length of the weights”. In:
Proceedings of the sixth annual conference on Computational learning
theory. 5–13.
Hoeven, D., T. Erven, and W. Kotłowski. (2018). “The many faces of
exponential weights in online learning”. In: Conference On Learning
Theory. PMLR. 2067–2092.
Holland, M. (2019). “PAC-Bayes under potentially heavy tails”. Advances in Neural Information Processing Systems. 32: 2715–2724.
Honorio, J. and T. Jaakkola. (2014). “Tight bounds for the expected
risk of linear classifiers and PAC-Bayes finite-sample guarantees”.
In: Proceedings of the 17th International Conference on Artificial
Intelligence and Statistics. 384–392.
Huggins, J. H., T. Campbell, M. Kasprzak, and T. Broderick. (2018).
“Practical bounds on the error of Bayesian posterior approximations:
A nonasymptotic approach”. arXiv preprint arXiv:1809.09505.
Jaiswal, P., V. Rao, and H. Honnappa. (2020). “Asymptotic consistency
of α-Rényi-approximate posteriors”. Journal of Machine Learning
Research. 21(156): 1–42.
Jang, K., K.-S. Jun, I. Kuzborskij, and F. Orabona. (2023). “Tighter
PAC-Bayes Bounds Through Coin-Betting”. In: Proceedings of
Thirty Sixth Conference on Learning Theory. Ed. by G. Neu and
L. Rosasco. Vol. 195. Proceedings of Machine Learning Research.
PMLR. 2240–2264.
Jiang, W. and M. A. Tanner. (2008). “Gibbs posterior for variable
selection in high-dimensional classification and data mining”. The
Annals of Statistics: 2207–2231.
Jin, G., Y. X., P. Yang, L. Zhang, S. Schewe, and X. Huang. (2022).
“Weight expansion: a new perspective on dropout and generalization”.
arXiv preprint arXiv:2201.09209.
Jose, S. T. and O. Simeone. (2021). “Transfer meta-learning:
Information-theoretic bounds and information meta-risk minimization”. IEEE Transactions on Information Theory. 68(1): 474–501.
Juditsky, A. and A. Nemirovski. (2000). “Functional aggregation for
nonparametric regression”. Annals of Statistics: 681–712.

292

REFERENCES

Juditsky, A., P. Rigollet, and A. B. Tsybakov. (2008). “Learning by
mirror averaging”. The Annals of Statistics. 36(5): 2183–2206.
Kakade, S. M., K. Sridharan, and A. Tewari. (2008). “On the complexity
of linear prediction: Risk bounds, margin bounds, and regularization”. In: Advances in Neural Information Processing Systems. Ed.
by D. Koller, D. Schuurmans, Y. Bengio, and L. Bottou. Vol. 21.
Curran Associates, Inc.
Khan, M. E. and H. Rue. (2021). “The Bayesian Learning Rule”. arXiv
preprint arXiv:2107.04562.
Kivinen, J. and M. K. Warmuth. (1999). “Averaging expert predictions”. In: European Conference on Computational Learning Theory.
Springer, Berlin. 153–167.
Knoblauch, J., J. Jewson, and T. Damoulas. (2022). “An optimizationcentric view on Bayes’ rule: Reviewing and generalizing variational
inference”. Journal of Machine Learning Research. 23(132): 1–109.
Kullback, S. (1959). Information theory and statistics. John Wiley &
Sons.
Lacasse, A., F. Laviolette, M. Marchand, P. Germain, and N. Usunier.
(2006). “PAC-Bayes bounds for the risk of the majority vote and the
variance of the Gibbs classifier”. In: Advances in Neural Information
Processing Systems. Ed. by B. Schölkopf, J. Platt, and T. Hoffman.
Vol. 19. MIT Press.
Lan, X., X. Guo, and K. E. Barner. (2020). “PAC-Bayesian generalization bounds for multiLayer perceptrons”. Preprint arXiv:2006.08888.
Langford, J. and A. Blum. (2003). “Microchoice bounds and selfbounding learning algorithms”. Machine Learning. 51(2): 165–179.
Langford, J. and R. Caruana. (2002). “(Not) bounding the true error”.
Advances in Neural Information Processing Systems. 2: 809–816.
Langford, J. and M. Seeger. (2001). “Bounds for averaging classifiers”.
Technical Report CMU-CS-01-102, Carnegie Mellon University.
Langford, J. and J. Shawe-Taylor. (2002). “PAC-Bayes & margins”.
In: Proceedings of the 15th International Conference on Neural
Information Processing Systems. MIT Press. 439–446.
Laviolette, F., M. Marchand, and J.-F. Roy. (2011). “From PAC-Bayes
bounds to quadratic programs for majority votes”. In: Proceedings
of International Conference on Machine Learning. Citeseer. 5–59.

REFERENCES

293

Lecué, G. (2007). “Aggregation procedures: optimality and fast rates”.
PhD thesis. Université Pierre et Marie Curie-Paris VI.
Lecué, G. and S. Mendelson. (2013). “On the optimality of the aggregate
with exponential weights for low temperatures”. Bernoulli. 19(2):
646–675.
Lepski, O. (1992). “Asymptotically minimax adaptive estimation I:
upper bounds”. Theory of Probability and its Applications. 36(4):
682–697.
Letarte, G., P. Germain, B. Guedj, and F. Laviolette. (2019). “Dichotomize and generalize: PAC-Bayesian binary activated deep
neural networks”. In: Advances in Neural Information Processing
Systems. 6872–6882.
Leung, G. and A. R. Barron. (2006). “Information theory and mixing
least-squares regressions”. IEEE Trans. Inform. Theory. 52(8): 3396–
3410.
Lever, G., F. Laviolette, and J. Shawe-Taylor. (2010). “Distributiondependent PAC-Bayes Priors”. In: Proceedings of the 15th International Conference on Algorithmic Learning Theory. Berlin, Heidelberg: Springer. 119–133.
Lever, G., F. Laviolette, and J. Shawe-Taylor. (2013). “Tighter PACBayes bounds through distribution-dependent priors”. Theoretical
Computer Science. 473: 4–28.
Littlestone, N. and M. K. Warmuth. (1989). “The weighted majority
algorithm”. In: Proceedings of the 30th Annual Symposium on the
Foundations of Computer Science. IEEE. 256–261.
Liu, T., J. Lu, Z. Yan, and G. Zhang. (2021a). “PAC-Bayes bounds
for meta-learning with data-dependent prior”. arXiv preprint
arXiv:2102. 03748.
Liu, T., J. Lu, Z. Yan, and G. Zhang. (2021b). “Statistical generalization
performance guarantee for meta-learning with data dependent prior”.
Neurocomputing. 465: 391–405.
Livni, R. and S. Moran. (2020). “A limitation of the PAC-Bayes framework”. In: Advances in Neural Information Processing Systems. Ed.
by H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin.
Vol. 33. Curran Associates, Inc. 20543–20553.

294

REFERENCES

London, B. (2017). “A PAC-Bayesian analysis of randomized learning
with application to stochastic gradient descent”. In: Advances in
Neural Information Processing Systems. 2931–2940.
London, B. and T. Sandler. (2019). “Bayesian counterfactual risk minimization”. In: Proceedings of the 36th International Conference
on Machine Learning. Ed. by K. Chaudhuri and R. Salakhutdinov.
Vol. 97. Proceedings of Machine Learning Research. PMLR. 4125–
4133.
Lorenzen, S. S., C. Igel, and Y. Seldin. (2019). “On PAC-Bayesian
bounds for random forests”. Machine Learning. 108(8-9): 1503–
1522.
Lugosi, G. and G. Neu. (2021). “Online-to-PAC conversions: Generalization bounds via regret analysis”. arXiv preprint arXiv:2305.19674.
Lugosi, G. and G. Neu. (2022). “Generalization bounds via convex
analysis”. In: Proceedings of Thirty Fifth Conference on Learning
Theory. Ed. by P.-L. Loh and M. Raginsky. Vol. 178. Proceedings of
Machine Learning Research. PMLR. 3524–3546.
Luu, T. D., J. Fadili, and C. Chesneau. (2019). “PAC-Bayesian risk
bounds for group-analysis sparse regression by exponential weighting”. Journal of Multivariate Analysis. 171: 209–233.
Mai, T. T. (2017). “PAC-Bayesian estimation of low-rank matrices”.
PhD thesis, Université Paris Saclay.
Mai, T. T. (2023a). “From bilinear regression to inductive matrix
completion: a quasi-Bayesian analysis”. Entropy. 25(2): 333.
Mai, T. T. (2023b). “Simulation comparisons between Bayesian and
de-biased estimators in low-rank matrix completion”. METRON :
1–22.
Mai, T. T. and P. Alquier. (2015). “A Bayesian approach for noisy matrix completion: Optimal rate under general sampling distribution”.
Electronic Journal of Statistics. 9(1): 823–841.
Mai, T. T. and P. Alquier. (2017). “Pseudo-Bayesian quantum tomography with rank-adaptation”. Journal of Statistical Planning and
Inference. 184: 62–76.
Mammen, E. and A. B. Tsybakov. (1999). “Smooth discrimination
analysis”. The Annals of Statistics. 27(6): 1808–1829.

REFERENCES

295

Masegosa, A., S. Lorenzen, C. Igel, and Y. Seldin. (2020). “Second order
PAC-Bayesian bounds for the weighted majority vote”. In: Advances
in Neural Information Processing Systems. Ed. by H. Larochelle,
M. Ranzato, R. Hadsell, M. Balcan, and H. Lin. Vol. 33. Curran
Associates, Inc. 5263–5273.
Masegosa, A. R. (2020). “Learning under model misspecification: Applications to variational and ensemble methods”. In: Advances in
Neural Information Processing Systems. Ed. by H. Larochelle, M.
Ranzato, R. Hadsell, M. Balcan, and H. Lin. Vol. 33. Curran Associates, Inc. 5479–5491.
Maurer, A. (2004). “A note on the PAC Bayesian theorem”. arXiv
preprint cs/0411099.
Mbacke, S. D., F. Clerc, and P. Germain. (2023). “PAC-Bayesian generalization bounds for adversarial generative models”. arXiv preprint
arXiv:2302.08942.
McAllester, D. A. (1998). “Some PAC-Bayesian theorems”. In: Proceedings of the Eleventh Annual Conference on Computational Learning
Theory. New York: ACM. 230–234.
McAllester, D. A. (1999). “PAC-Bayesian model averaging”. In: Proceedings of the twelfth annual conference on Computational learning
theory. 164–170.
McAllester, D. A. (2003). “PAC-Bayesian stochastic model selection”.
Machine Learning. 51(1): 5–21.
McAllester, D. A. (2013). “A PAC-Bayesian tutorial with a dropout
bound”. arXiv preprint arXiv:1307.2118.
McDiarmid, C. (1998). “Concentration”. In: Probabilistic methods for
algorithmic discrete mathematics. Ed. by M. Habib, C. McDiarmid,
and B. Reed. Springer. 195–248.
Meir, R. and T. Zhang. (2003). “Generalization error bounds for
Bayesian mixture algorithms”. Journal of Machine Learning Research. 4(Oct): 839–860.
Meunier, D. and P. Alquier. (2021). “Meta-strategy for learning tuning
parameters with guarantees”. Entropy. 23(10).

296

REFERENCES

Mhammedi, Z., P. D. Grünwald, and B. Guedj. (2019). “PAC-Bayes unexpected Bernstein inequality”. In: Advances in Neural Information
Processing Systems. Ed. by H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alché-Buc, E. Fox, and R. Garnett. Vol. 32. Curran
Associates, Inc.
Mourtada, J., T. Vaškevičius, and N. Zhivotovskiy. (2023). “Local Risk Bounds for Statistical Aggregation”. arXiv preprint
arXiv:2306.17151.
Nachum, I., J. Shafer, and A. Yehudayoff. (2018). “A direct sum result
for the information complexity of learning”. In: Proceedings of the
31st Conference On Learning Theory. Ed. by S. Bubeck, V. Perchet,
and P. Rigollet. Vol. 75. Proceedings of Machine Learning Research.
PMLR. 1547–1568.
Nakakita, S., P. Alquier, and M. Imaizumi. (2022). “Dimension-free
bounds for sum of dependent matrices and operators with heavytailed distribution”. arXiv preprint arXiv:2210.09756.
Negrea, J., M. Haghifam, G. K. Dziugaite, A. Khisti, and D. M. Roy.
(2019). “Information-theoretic generalization bounds for SGLD via
data-dependent estimates”. Advances in Neural Information Processing Systems. 32: 11015–11025.
Nemirovski, A. (2000). “Topics in non-parametric statistics”. Ecole
d’Eté de Probabilités de Saint-Flour. 28: 85.
Neu, G., G. K. Dziugaite, M. Haghifam, and D. M. Roy. (2021).
“Information-theoretic generalization bounds for stochastic gradient
descent”. In: Conference on Learning Theory. PMLR. 3526–3545.
Neyshabur, B., S. Bhojanapalli, D. McAllester, and N. Srebro. (2017).
“A PAC-Bayesian approach to spectrally-normalized margin bounds
for neural networks”. NIPS 2017 Workshop: (Almost) 50 Shades of
Bayesian Learning: PAC-Bayesian trends and insights.
Nozawa, K., P. Germain, and B. Guedj. (2020). “PAC-Bayesian contrastive unsupervised representation learning”. In: Proceedings of
the 36th Conference on Uncertainty in Artificial Intelligence (UAI).
Ed. by J. Peters and D. Sontag. Vol. 124. Proceedings of Machine
Learning Research. PMLR. 21–30.
Nozawa, K. and I. Sato. (2019). “PAC-Bayes analysis of sentence representation”. arXiv preprint arXiv:1902.04247.

REFERENCES

297

Ohn, I. and L. Lin. (2021). “Adaptive variational Bayes: Optimality,
computation and applications”. arXiv preprint arXiv:2109.03204.
Ohnishi, Y. and J. Honorio. (2021). “Novel change of measure inequalities with applications to PAC-Bayesian bounds and Monte Carlo
estimation”. In: International Conference on Artificial Intelligence
and Statistics. PMLR. 1711–1719.
Oneto, L., M. Donini, M. Pontil, and J. Shawe-Taylor. (2020). “Randomized learning and generalization of fair and private classifiers: From
PAC-Bayes to stability and differential privacy”. Neurocomputing.
416: 231–243.
Orabona, F. (2019). “A modern introduction to online learning”. arXiv
preprint arXiv:1912.13213.
Parrado-Hernández, E., A. Ambroladze, J. Shawe-Taylor, and S. Sun.
(2012). “PAC-Bayes bounds with data dependent priors”. The Journal of Machine Learning Research. 13(1): 3507–3531.
Pentina, A. and C. Lampert. (2014). “A PAC-Bayesian bound for lifelong
learning”. In: International Conference on Machine Learning. PMLR.
991–999.
Pérez-Ortiz, M., O. Rivasplata, J. Shawe-Taylor, and C. Szepesvári.
(2021). “Tighter risk certificates for neural networks”. The Journal
of Machine Learning Research. 22(1): 10326–10365.
Pitas, K. (2020). “Dissecting non-vacuous generalization bounds based
on the mean-field approximation”. In: Proceedings of the 37th International Conference on Machine Learning. Ed. by H. D. III and A.
Singh. Vol. 119. Proceedings of Machine Learning Research. PMLR.
7739–7749.
Plummer, S., D. Pati, and A. Bhattacharya. (2020). “Dynamics of
coordinate ascent variational inference: A case study in 2D Ising
models”. Entropy. 22(11).
Raginsky, M., A. Rakhlin, M. Tsao, Y. Wu, and A. Xu. (2016). “Information-theoretic analysis of stability and bias of learning algorithms”.
In: 2016 IEEE Information Theory Workshop (ITW). IEEE. 26–30.
Ralaivola, L., M. Szafranski, and G. Stempfel. (2010). “Chromatic
PAC-Bayes bounds for non-i.i.d. data: Applications to ranking and
stationary β-mixing processes”. Journal of Machine Learning Research. 11(Jul): 1927–1956.

298

REFERENCES

Rezazadeh, A. (2022). “A general framework for PAC-Bayes bounds for
meta-learning”. arXiv preprint arXiv:2206.05454.
Ridgway, J., P. Alquier, N. Chopin, and F. Liang. (2014). “PAC-Bayesian
AUC classification and scoring”. Advances in Neural Information
Processing Systems. 1(January): 658–666.
Rio, E. (2000). “Inégalités de Hoeffding pour les fonctions lipschitziennes
de suites dépendantes”. Comptes Rendus de l’Académie des SciencesSeries I-Mathematics. 330(10): 905–908.
Riou, C., P. Alquier, and B.-E. Chérief-Abdellatif. (2023). “Bayes meets
Bernstein at the meta level: an analysis of fast rates in meta-learning
with PAC-Bayes”. arXiv preprint arXiv:2302.11709.
Rissanen, J. (1978). “Modeling by shortest data description”. Automatica. 14(5): 465–471.
Rivasplata, O., I. Kuzborskij, C. Szepesvári, and J. Shawe-Taylor. (2020).
“PAC-Bayes analysis beyond the usual bounds”. In: Advances in
Neural Information Processing Systems.
Rivasplata, O., V. M. Tankasali, and C. Szepesvari. (2019). “PAC-Bayes
with backprop”. arXiv preprint arXiv:1908.07380.
Rodrígues-Gálvez, B., R. Thobaden, and M. Skoglund. (2023). “More
PAC-Bayes bounds: From bounded losses, to losses with general tail
behaviors, to anytime-validity”. arXiv preprint arXiv:2306.12214.
Rodríguez-Gálvez, B., G. Bassi, R. Thobaben, and M. Skoglund. (2021).
“Tighter expected generalization error bounds via Wasserstein distance”. In: Advances in Neural Information Processing Systems.
Ed. by M. Ranzato, A. Beygelzimer, Y. Dauphin, P. Liang, and
J. W. Vaughan. Vol. 34. Curran Associates, Inc. 19109–19121.
Rothfuss, J., V. Fortuin, M. Josifoski, and A. Krause. (2021). “PACOH:
Bayes-optimal meta-learning with PAC-guarantees”. In: International Conference on Machine Learning. PMLR. 9116–9126.
Rousseau, J. (2016). “On the frequentist properties of Bayesian nonparametric methods”. Annual Review of Statistics and Its Application.
3: 211–231.
Russo, D. and J. Zou. (2019). “How much does your data exploration
overfit? Controlling bias via information usage”. IEEE Transactions
on Information Theory. 66(1): 302–323.

REFERENCES

299

Sakhi, O., P. Alquier, and N. Chopin. (2023). “PAC-Bayesian Offline
Contextual Bandits With Guarantees”. In: Proceedings of the 40th
International Conference on Machine Learning. Ed. by A. Krause,
E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett.
Vol. 202. Proceedings of Machine Learning Research. PMLR. 29777–
29799.
Samson, P.-M. (2000). “Concentration of measure inequalities for
Markov chains and Φ-mixing processes”. The Annals of Probability.
28(1): 416–461.
Seeger, M. (2002). “PAC-Bayesian generalisation error bounds for Gaussian process classification”. Journal of machine learning research.
3(Oct): 233–269.
Seeger, M. (2003). “Bayesian Gaussian process models: PAC-Bayesian
generalisation error bounds and sparse approximations”. Tech. rep.
University of Edinburgh.
Seldin, Y., P. Auer, J. Shawe-Taylor, R. Ortner, and F. Laviolette.
(2011). “PAC-Bayesian analysis of contextual bandits”. In: Advances
in Neural Information Processing Systems. 1683–1691.
Seldin, Y., N. Cesa-Bianchi, P. Auer, F. Laviolette, and J. Shawe-Taylor.
(2012a). “PAC-Bayes-Bernstein inequality for martingales and its
application to multiarmed bandits”. In: Proceedings of the Workshop
on On-line Trading of Exploration and Exploitation 2. Ed. by D.
Glowacka, L. Dorard, and J. Shawe-Taylor. Vol. 26. Proceedings of
Machine Learning Research. Bellevue, Washington, USA: PMLR.
98–111.
Seldin, Y., F. Laviolette, N. Cesa-Bianchi, J. Shawe-Taylor, and P.
Auer. (2012b). “PAC-Bayesian inequalities for martingales”. IEEE
Transactions on Information Theory. 58(12): 7086–7093.
Seldin, Y. and N. Tishby. (2010). “PAC-Bayesian analysis of coclustering and beyond.” Journal of Machine Learning Research.
11(12).
Shalev-Shwartz, S. (2011). “Online learning and online convex optimization”. Foundations and Trends® in Machine Learning. 4(2):
107–194.

300

REFERENCES

Shawe-Taylor, J. and R. Williamson. (1997). “A PAC analysis of a
Bayes estimator”. In: Proceedings of the Tenth Annual Conference
on Computational Learning Theory. New York: ACM. 2–9.
Sheth, R. and R. Khardon. (2017). “Excess risk bounds for the Bayes risk
using variational inference in latent Gaussian models”. In: Advances
in Neural Information Processing Systems. 5151–5161.
Steffen, M. F. and M. Trabs. (2022). “PAC-Bayes training for neural
networks: sparsity and uncertainty quantification”. arXiv preprint
arXiv:2204.12392.
Steinke, T. and L. Zakynthinou. (2020). “Reasoning about generalization
via conditional mutual information”. In: Conference on Learning
Theory. PMLR. 3437–3452.
Sucker, M. and P. Ochs. (2023). “PAC-Bayesian learning of optimization
algorithms”. In: International Conference on Artificial Intelligence
and Statistics. PMLR. 8145–8164.
Suzuki, T. (2012). “PAC-Bayesian bound for Gaussian process regression
and multiple kernel additive model”. In: Conference on Learning
Theory. JMLR Workshop and Conference Proceedings. 8–1.
Suzuki, T. (2015). “Convergence rate of Bayesian tensor estimator and
its minimax optimality”. In: Proceedings of the 32nd International
Conference on Machine Learning. Ed. by F. Bach and D. Blei. Vol. 37.
Proceedings of Machine Learning Research. Lille, France: PMLR.
1273–1282.
Suzuki, T. (2020). “Generalization bound of globally optimal nonconvex neural network training: Transportation map estimation by
infinite dimensional Langevin dynamics”. In: Advances in Neural
Information Processing Systems. Ed. by H. Larochelle, M. Ranzato,
R. Hadsell, M. Balcan, and H. Lin. Vol. 33. Curran Associates, Inc.
19224–19237.
Syring, N. and R. Martin. (2019). “Calibrating general posterior credible
regions”. Biometrika. 106(2): 479–486.
Syring, N. and R. Martin. (2023). “Gibbs posterior concentration rates
under sub-exponential type losses”. Bernoulli. 29(2): 1080–1108.
Tasdighi, B., A. Akgül, K. K. Brink, and M. Kandemir.
(2023). “PAC-Bayesian soft actor-critic learning”. arXiv preprint
arXiv:2301.12776.

REFERENCES

301

Thiemann, N., C. Igel, O. Wintenberger, and Y. Seldin. (2017). “A
strongly quasiconvex PAC-Bayesian bound”. In: International Conference on Algorithmic Learning Theory. 466–492.
Tolstikhin, I. and Y. Seldin. (2013). “PAC-Bayes-empirical-Bernstein
inequality”. Advances in Neural Information Processing Systems 26
(NIPS 2013): 1–9.
Tsuzuku, Y., I. Sato, and M. Sugiyama. (2020). “Normalized flat minima:
Exploring scale invariant definition of flat minima for neural networks using PAC-Bayesian analysis”. In: International Conference
on Machine Learning. PMLR. 9636–9647.
Tsybakov, A. B. (2003). “Optimal rates of aggregation”. In: Computational Learning Theory and Kernel Machines. Proc. 16th Annual
Conference on Learning Theory (COLT) and 7th Annual Workshop
on Kernel Machines. Ed. by B. Schölkopf and M. Warmuth. Springer
Lecture Notes in Artificial Intelligence. 303–313.
Valiant, L. (1984). “A theory of the learnable”. Communications of the
ACM. 27(11): 1134–1142.
van Erven, T. (2014). “PAC-Bayes mini-tutorial: a continuous union
bound”. arXiv preprint arXiv:1405.1580.
Vapnik, V. (1998). Statistical learning theory. Wiley–Blackwell.
Vapnik, V. N. and A. Y. Chervonenkis. (1968). “The uniform convergence of frequencies of the appearance of events to their probabilities”. Doklady Akademii Nauk. 181(4): 781–783.
Viallard, P., R. Emonet, P. Germain, A. Habrard, and E. Morvant.
(2019). “ Interpreting neural networks as majority votes through
the PAC-Bayesian theory”. NeurIPS 2019 Workshop on Machine
Learning with Guarantees.
Vovk, V. G. (1990). “Aggregating strategies”. Proceedings of Computational Learning Theory, 1990.
Wainwright, M. J. (2019). High-dimensional statistics: A non-asymptotic
viewpoint. Vol. 48. Cambridge university press.
Wang, H., S. Zheng, C. Xiong, and R. Socher. (2019). “On the generalization gap inreparameterizable reinforcement learning”. In: Proceedings
of the 36th International Conference on Machine Learning. Ed. by K.
Chaudhuri and R. Salakhutdinov. Vol. 97. Proceedings of Machine
Learning Research. PMLR. 6648–6658.

302

REFERENCES

Wang, Z., S.-L. Huang, E. E. Kuruoglu, J. Sun, X. Chen, and Y.
Zheng. (2021). “PAC-Bayes information bottleneck”. arXiv preprint
arXiv:2109.14509.
Wintenberger, O. (2010). “Deviation inequalities for sums of weakly
dependent time series”. Electronic Communications in Probability.
(15): 489–503.
Wu, Y.-S., A. Masegosa, S. Lorenzen, C. Igel, and Y. Seldin. (2021).
“Chebyshev-Cantelli PAC-Bayes-Bennett inequality for the weighted
majority vote”. In: Advances in Neural Information Processing Systems. Ed. by M. Ranzato, A. Beygelzimer, Y. Dauphin, P. Liang,
and J. W. Vaughan. Vol. 34. Curran Associates, Inc. 12625–12636.
Wu, Y.-S. and Y. Seldin. (2022). “Split-kl and PAC-Bayes-split-kl
inequalities for ternary random variables”. In: Advances in Neural
Information Processing Systems. Ed. by S. Koyejo, S. Mohamed,
A. Agarwal, D. Belgrave, K. Cho, and A. Oh. Vol. 35. Curran
Associates, Inc. 11369–11381.
Xu, A. and M. Raginsky. (2017). “Information-theoretic analysis of
generalization capability of learning algorithms”. In: Proceedings of
the 31st International Conference on Neural Information Processing
Systems. NIPS’17. Long Beach, California, USA: Curran Associates
Inc. 2521–2530.
Yang, J., S. Sun, and D. M. Roy. (2019). “Fast-rate PAC-Bayes generalization bounds via shifted Rademacher processes”. Advances in
Neural Information Processing Systems. 32: 10803–10813.
Yang, Y. (2001). “Adaptive regression by mixing”. Journal of the American Statistical Association. 96(454): 574–588.
Yang, Y. (2004). “Aggregating regression procedures to improve performance”. Bernoulli. 10(1): 25–47.
Yang, Y., D. Pati, and A. Bhattacharya. (2020). “α-variational inference
with statistical guarantees”. Annals of Statistics. 48(2): 886–905.
Zhang, F. and C. Gao. (2020). “Convergence rates of variational posterior distributions”. Annals of Statistics. 48(4): 2180–2207.
Zhang, T. (2006). “Information-theoretic upper and lower bounds for
statistical estimation”. IEEE Transactions on Information Theory.
52(4): 1307–1321.

REFERENCES

303

Zhang, X., A. Ghosh, G. Liu, and R. Wang. (2023). “Auto-tune: PACBayes optimization over prior and posterior for neural networks”.
arXiv preprint arXiv:2305.19243.
Zhivotovskiy, N. (2021). “Dimension-free bounds for sums of independent
matrices and simple tensors via the variational principle”. arXiv
preprint arXiv:2108.08198.
Zhou, W., V. Veitch, M. Austern, R. P. Adams, and P. Orbanz. (2018).
“Non-vacuous generalization bounds at the imagenet scale: a PACBayesian compression approach”. arXiv preprint arXiv:1804.05862.

