---
source: Courtade, T.A., Weissman, T. (2014). Multiterminal Source Coding under Logarithmic Loss. IEEE Transactions on Information Theory, 60(1), 740-761. arXiv:1110.3069
note: Original CEO problem formulation — Berger, T., Zhang, Z., Viswanathan, H. (1996). IEEE Trans. Inf. Theory 42(3), 887-902 — is paywalled. This paper contains complete re-statement and extension of the CEO problem.
author: Thomas A. Courtade, Tsachy Weissman
date: 2012-07-11
type: paper
quality: primary
stance: neutral
---


Multiterminal Source Coding
under Logarithmic Loss

arXiv:1110.3069v3 [cs.IT] 11 Jul 2012

Thomas A. Courtade∗ and Tsachy Weissman†
November 1, 2018

Abstract
We consider the classical two-encoder multiterminal source coding
problem where distortion is measured under logarithmic loss. We provide a single-letter description of the achievable rate distortion region for
arbitrarily correlated sources with finite alphabets. In doing so, we also
give the rate distortion region for the m-encoder CEO problem (also under
logarithmic loss). Several applications and examples are given.

1

Introduction

A complete characterization of the achievable rate distortion region for the twoencoder source coding problem depicted in Figure 1 has remained an open problem for over three decades. Following tradition, we will refer to this two-encoder
source coding network as the multiterminal source coding problem throughout
this paper. Several special cases have been solved for general source alphabets
and distortion measures:
• The lossless case where D1 = 0, D2 = 0. Slepian and Wolf solved this case
in their seminal work [1].
• The case where one source is recovered losslessly: i.e., D1 = 0, D2 =
Dmax . This case corresponds to the source coding with side information
problem of Ahlswede-Körner-Wyner [2], [3].
• The Wyner-Ziv case [4] where Y2 is available to the decoder as side information and Y1 should be recovered with distortion at most D1 .
• The Berger-Yeung case (which subsumes the previous three cases) [5]
where D1 is arbitrary and D2 = 0.
∗ Thomas Courtade is with the Department of Electrical Engineering, University of California, Los Angeles. Email: tacourta@ee.ucla.edu.
† Tsachy Weissman is with the Department of Electrical Engineering, Stanford University.
Email: tsachy@stanford.edu.

1

Y1n

Encoder 1
R1

Y2n

Decoder

Encoder 2

Ŷ1n
Ed(Y1n , Ŷ1n ) ≤ D1

Ŷ2n
Ed(Y2n , Ŷ2n ) ≤ D2

R2

Figure 1: The multiterminal source coding network.

Despite the apparent progress, other seemingly fundamental cases, such as
when D1 is arbitrary and D2 = Dmax , remain unsolved except perhaps in very
special cases.
Recently, the achievable rate distortion region for the quadratic Gaussian
multiterminal source coding problem was given by Wagner, Tavildar, and
Viswanath [6]. Until now, this was the only case for which the entire achievable
rate distortion region was known. While this is a very important result, it is
again a special case from a theoretical point of view: a specific choice of source
distribution, and a specific choice of distortion measure.
In the present paper, we determine the achievable rate distortion region
of the multiterminal source coding problem for arbitrarily correlated sources
with finite alphabets. However, as in [6], we restrict our attention to a specific
distortion measure.
At a high level, the roadmap for our argument is similar to that of [6]. In
particular, both arguments couple the multiterminal source coding problem to a
parametrized family of CEO problems. Then, the parameter in the CEO problem is “tuned” to yield the converse result. Despite this apparent similarity, the
proofs in [6] rely heavily on the previously known Gaussian CEO results [7], the
Gaussian one-helper results [8], and the calculus performed on the closed-form
entropy expressions which arise from the Gaussian source assumption. In our
case we do not have this luxury, and our CEO tuning argument essentially relies
on an existence lemma to yield the converse result. The success of our approach
is largely due to the fact that the distortion measure we consider admits a lower
bound in the form of a conditional entropy, much like the quadratic distortion
measure for Gaussian sources.

1.1

Our Contributions

In this paper, we give a single-letter characterization of the achievable rate distortion region for the multiterminal source coding problem under logarithmic
loss. In the process of accomplishing this, we derive the achievable rate distortion region for the m-encoder CEO problem, also under logarithmic loss. In
both settings, we obtain a stronger converse than is standard for rate distortion problems in the sense that augmenting the reproduction alphabet does not

2

enlarge the rate distortion region. Notably, we make no assumptions on the
source distributions, other than that the sources have finite alphabets. In both
cases, the Berger-Tung inner bound on the rate distortion region is tight. To
our knowledge, this constitutes the first time that the entire achievable rate
distortion region has been described for general finite-alphabet sources under
nontrivial distortion constraints.

1.2

Organization

This paper is organized as follows. In Section 2 we formally define the logarithmic loss function and the multiterminal source coding problem we consider. In
Section 3 we define the CEO problem and give the rate distortion region under logarithmic loss. In Section 4 we return to the multiterminal source coding
problem and derive the rate distortion region for the two-encoder setting. Also
in Sections 3 and 4, applications to estimation, horse racing, and list decoding
are given. In Section 5, we discuss connections between our results and the multiterminal source coding problem with arbitrary distortion measures. Section 6
delivers our concluding remarks and discusses directions for future work.

2

Problem Definition

Throughout this paper, we adopt notational conventions that are standard in
the literature. Specifically, random variables are denoted by capital letters (e.g.,
X) and their corresponding alphabets are denoted by corresponding calligraphic
letters (e.g., X ). We abbreviate a sequence (X1 , X2 , . . . , Xn ) of n random variables by X n , and we denote the interval (Xk , Xk+1 , . . . , Xj ) by Xkj . If the
lower index is equal to 1, it will be omitted when there is no ambiguity (e.g.,
X j , X1j ). Frequently, random variables will appear with two subscripts (e.g.,
Yi,j ). In this case, we are referring to the j th instance of random variable Yi .
j
We overload our notation here slightly in that Yi,1
is often abbreviated as Yij .
However, our meaning will always be clear from context.
n
Let {(Y1,j , Y2,j )}j=1 = (Y1n , Y2n ) be a sequence of n independent, identically
distributed random variables with finite Q
alphabets Y1 and Y2 respectively and
n
joint pmf p(y1 , y2 ). That is, (Y1n , Y2n ) ∼ i=1 p(y1,j , y2,j ).
In this paper, we take the reproduction alphabet Ŷi to be equal to the set
of probability distributions over the source alphabet Yi for i = 1, 2. Thus, for
a vector Ŷin ∈ Ŷin , we will use the notation Ŷi,j (yi ) to mean the j th coordinate
(1 ≤ j ≤ n) of Ŷin (which is a probability distribution on Yi ) evaluated for the
outcome yi ∈ Yi . In other words, the decoder generates ‘soft’ estimates of the
source sequences.
We will consider the logarithmic loss distortion measure defined as follows:


1
= D(1yi (y)kŷi (y)) for i = 1, 2.
d(yi , ŷi ) = log
ŷi (yi )

3

In particular, d(yi , ŷi ) is the relative entropy (i.e., Kullback-Leibler divergence)
between the empirical distribution of the event {Yi = yi } and the estimate
ŷi . Using this definition for symbol-wise distortion, it is standard to define the
distortion between sequences as
n

d(yin , ŷin ) =

1X
d(yi,j , ŷi,j ) for i = 1, 2.
n j=1

We point out that the logarithmic loss function is a widely used penalty
function in the theory of learning and prediction (cf. [9, Chapter 9]). Further,
it is a particularly natural loss criterion in settings where the reconstructions
are allowed to be ‘soft’, rather than deterministic values. Surprisingly, since
distributed learning and estimation problems are some of the most oft-cited applications of lossy multiterminal source coding, it does not appear to have been
studied in this context until the recent work [10]. However, we note that this
connection has been established previously for the single-encoder case in the
study of the information bottleneck problem [11]. Beyond learning and prediction, a similar distortion measure has appeared before in the image processing
literature [12]. As we demonstrate through several examples, the logarithmic
loss distortion measure has a variety of useful applications in the context of
multiterminal source coding.
A rate distortion code (of blocklength n) consists of encoding functions:
n
o
(n)
(n)
gi : Yin → 1, . . . , Mi
for i = 1, 2
and decoding functions
n
o n
o
(n)
(n)
(n)
ψi : 1, . . . , M1
× 1, . . . , M2
→ Ŷin for i = 1, 2.
A rate distortion vector (R1 , R2 , D1 , D2 ) is strict-sense achievable if there
(n) (n)
(n)
(n)
exists a blocklength n, encoding functions g1 , g2 and a decoder (ψ1 , ψ2 )
such that
1
(n)
log Mi for i = 1, 2
n
Di ≥ Ed(Yin , Ŷin ) for i = 1, 2.
Ri ≥

Where
(n)

(n)

(n)

Ŷin = ψi (g1 (Y1n ), g2 (Y2n )) for i = 1, 2.
Definition 1. Let RD? denote the set of strict-sense achievable rate distortion
vectors and define the set of achievable rate distortion vectors to be its closure,
?
RD .
Our ultimate goal in the present paper is to give a single-letter character?
ization of the region RD . However, in order to do this, we first consider an
4

associated CEO problem. In this sense, the roadmap for our argument is similar
to that of [6]. Specifically, both arguments couple the multiterminal source coding problem to a parametrized family of CEO problems. Then, the parameter in
the CEO problem is “tuned” to yield the converse result. Despite this apparent
similarity, the proofs are quite different since the results in [6] depend heavily
on the peculiarities of the Gaussian distribution.

3

The CEO problem

In order to attack the general multiterminal problem, we begin by studying the CEO problem (See [13] for an introduction.). To this end, let
n
{(Xj , Y1,j , Y2,j )}j=1 = (X n , Y1n , Y2n ) be a sequence of n independent, identically distributed random variables distributed according to the joint pmf
p(x, y1 , y2 ) = p(x)p(y1 |x)p(y2 |x). That is, Y1 ↔ X ↔ Y2 form a Markov chain,
in that order.
In this section, we consider the reproduction alphabet X̂ to be equal to the
set of probability distributions over the source alphabet X . As before, for a
vector X̂ n ∈ X̂ n , we will use the notation X̂j (x) to mean the j th coordinate of
X̂ n (which is a probability distribution on X ) evaluated for the outcome x ∈ X .
As in the rest of this paper, d(·, ·) is the logarithmic loss distortion measure.
A rate distortion CEO code (of blocklength n) consists of encoding functions:
n
o
(n)
(n)
gi : Yin → 1, . . . , Mi
for i = 1, 2
and a decoding function
n
o n
o
(n)
(n)
ψ (n) : 1, . . . , M1
× 1, . . . , M2
→ X̂ n .
A rate distortion vector (R1 , R2 , D) is strict-sense achievable for the CEO
(n) (n)
problem if there exists a blocklength n, encoding functions g1 , g2 and a
(n)
decoder ψ
such that
1
(n)
log Mi for i = 1, 2
n
D ≥ Ed(X n , X̂ n ).

Ri ≥

Where
(n)

(n)

X̂ n = ψ (n) (g1 (Y1n ), g2 (Y2n )).
Definition 2. Let RD?CEO denote the set of strict-sense achievable rate distortion vectors and define the set of achievable rate distortion vectors to be its
?
closure, RDCEO .

5

3.1

Inner Bound

Definition 3. Let (R1 , R2 , D) ∈ RDiCEO if and only if there exists a joint
distribution of the form
p(x, y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)p(q)
where |U1 | ≤ |Y1 |, |U2 | ≤ |Y2 |, and |Q| ≤ 4, which satisfies
R1 ≥ I(Y1 ; U1 |U2 , Q)
R2 ≥ I(Y2 ; U2 |U1 , Q)
R1 + R2 ≥ I(U1 , U2 ; Y1 , Y2 |Q)
D ≥ H(X|U1 , U2 , Q).
?

Theorem 1. RDiCEO ⊆ RDCEO .
(R1 , R2 , D) ∈ RDiCEO are achievable.

That is, all rate distortion vectors

Before proceeding with the proof, we cite the following variant of a wellknown inner bound:
Proposition 1 (Berger-Tung Inner Bound [14, 15]). The rate distortion vector
(R1 , R2 , D) is achievable if
R1 ≥ I(U1 ; Y1 |U2 , Q)
R2 ≥ I(U2 ; Y2 |U1 , Q)
R1 + R2 ≥ I(U1 , U2 ; Y1 , Y2 |Q)
D ≥ E [d(X, f (U1 , U2 , Q)]
for a joint distribution
p(x)p(y1 |x)p(y2 |x)p(u1 |y1 , q)p(u2 |y2 , q)p(q)
and reproduction function
f : U1 × U2 × Q → X̂ .
The proof of this proposition is a standard exercise in information theory,
and is therefore omitted. The interested reader is directed to the text [16] for
a modern, detailed treatment. The proposition follows from what is commonly
called the Berger-Tung achievability scheme. In this encoding scheme, each
encoder quantizes its observation Yin to a codeword Uin , such that the empirical distribution of the entries in (Yin , Uin ) is very close to the true distribution
p(yi , ui ). In order to communicate their respective quantizations to the decoder, the encoders essentially perform Slepian-Wolf coding. For this reason,
the Berger-Tung achievability scheme is also referred to as a “quantize-and-bin”
coding scheme.

6

Proof of Theorem 1. Given Proposition 1, the proof of Theorem 1 is immediate.
Indeed, if we apply Proposition 1 with the reproduction function f (U1 , U2 , Q) ,
Pr [X = x|U1 , U2 , Q], we note that
E [d(X, f (U1 , U2 , Q)] = H(X|U1 , U2 , Q),
which yields the desired result.
Thus, from the proof of Theorem 1, we see that our inner bound RDiCEO
simply corresponds to a specialization of the general Berger-Tung inner bound
to the case of logarithmic loss.

3.2

A Matching Outer Bound

A particularly useful property of the logarithmic loss distortion measure is that
the expected distortion is lower-bounded by a conditional entropy. A similar
property is enjoyed by Gaussian random variables under quadratic distortion.
In particular, if G is Gaussian, and Ĝ is such that E(Ĝ − G)2 ≤ D, then
1
2 log(2πe)D ≥ h(G|Ĝ). The case for logarithmic loss is similar, and we state it
formally in the following lemma which is crucial in the proof of the converse.
(n)

(n)

Lemma 1. Let Z = (g1 (Y1n ), g2 (Y2n )) be the argument of the reproduction
function ψ (n) . Then nEd(X n , X̂ n ) ≥ H(X n |Z).
Proof. By definition of the reproduction alphabet, we can consider the reproduction X̂ n to be a probability distribution on X n conditioned
on the argument
Qn
Z. In particular, if x̂n = ψ (n) (z), define s(xn |z) , j=1 x̂j (xj ). It is readily
verified that s is a probability measure on X n . Then, we obtain the following
lower bound on the expected distortion conditioned on Z = z:


n
h
i
1X X
1
E d(X n , X̂ n )|Z = z =
p(xn |z) log
n j=1 n n
x̂j (xj )
x ∈X


n
X
1 X
1
n
=
p(x |z)
log
n n n
x̂j (xj )
j=1
x ∈X


1
1 X
n
p(x |z) log
=
n n n
s(xn |z)
x ∈X


p(xn |z)
1
1 X
n
p(x |z) log
+ H(X n |Z = z)
=
n
n n n
s(x |z)
n
x ∈X

1
1
= D (p(xn |z)ks(xn |z)) + H(X n |Z = z)
n
n
1
≥ H(X n |Z = z),
n
where p(xn |z) = Pr (X n = xn |Z = z) is the true conditional distribution. Averaging both sides over all values of Z, we obtain the desired result.
7

Definition 4. Let (R1 , R2 , D) ∈ RDoCEO if and only if there exists a joint
distribution of the form
p(x)p(y1 |x)p(y2 |x)p(u1 |y1 , q)p(u2 |y2 , q)p(q),
which satisfies
R1
R2
R1 + R2
D


≥ I(Y1 ; U1 |X, Q) + H(X|U2 , Q) − D



≥ I(Y2 ; U2 |X, Q) + H(X|U1 , Q) − D
≥ I(U1 ; Y1 |X, Q) + I(U2 ; Y2 |X, Q) + H(X) − D 


≥ H(X|U1 , U2 , Q).

(1)

Theorem 2. If (R1 , R2 , D) is strict-sense achievable for the CEO problem, then
(R1 , R2 , D) ∈ RDoCEO .
Proof. Suppose the point (R1 , R2 , D) is strict-sense achievable. Let A be a
(n)
nonempty subset of {1, 2}, and let Fi = gi (Yin ) be the message sent by encoder
j−1
n
i ∈ {1, 2}. Define Ui,j , (Fi , Yi ) and Qj , (X j−1 , Xj+1
) = X n \Xj . To
simplify notation, let YA = ∪i∈A Yi (similarly for UA and FA ).
With these notations established, we have the following string of inequalities:
X
X
n
Ri ≥
H(Fi )
i∈A

i∈A

≥ H(FA )
≥ I(YAn ; FA |FAc )
= I(X n , YAn ; FA |FAc )
X
= I(X n ; FA |FAc ) +
I(Fi ; Yin |X n )

(2)
(3)

i∈A

= H(X n |FAc ) − H(X n |F1 , F2 ) +

n
XX

I(Yi,j ; Fi |X n , Yij−1 )

i∈A j=1

≥ H(X n |FAc ) +

X n
X

I(Yi,j ; Fi |X n , Yij−1 ) − nD

(4)

i∈A j=1

=

=

≥

n
X
j=1
n
X
j=1
n
X
j=1

H(Xj |FAc , X j−1 ) +
H(Xj |FAc , X j−1 ) +
H(Xj |UAc ,j , Qj ) +

n
XX
i∈A j=1
n
XX

I(Yi,j ; Fi |X n , Yij−1 ) − nD
I(Yi,j ; Ui,j |Xj , Qj ) − nD

(5)

I(Yi,j ; Ui,j |Xj , Qj ) − nD.

(6)

i∈A j=1
X n
X
i∈A j=1

The nontrivial steps above can be justified as follows:
• (2) follows since FA is a function of YAn .
8

• (3) follows since Fi is a function of Yin and F1 ↔ X n ↔ F2 form a Markov
chain (since Y1n ↔ X n ↔ Y2n form a Markov chain).
• (4) follows since nD ≥ H(X n |F1 , F2 ) by Lemma 1.
• (5) follows from the Markov chain Yi,j ↔ X n ↔ Yij−1 , which follows from
the i.i.d. nature of the source sequences.
• (6) simply follows from the fact that conditioning reduces entropy.
Therefore, dividing both sides by n, we have:
X
i∈A

Ri ≥

n
n
X1X
1X
H(Xj |UAc ,j , Qj ) +
I(Yi,j ; Ui,j |Xj , Qj ) − D.
n j=1
n j=1
i∈A

Also, using Lemma 1 and the fact that conditioning reduces entropy:
D≥

n
1X
1
H(X n |F1 , F2 ) ≥
H(Xj |U1,j , U2,j , Qj ).
n
n j=1

Observe that Qj is independent of (Xj , Y1,j , Y2,j ) and, conditioned on Qj , we
have the long Markov chain U1,j ↔ Y1,j ↔ Xj ↔ Y2,j ↔ U2,j . Finally, by a
standard time-sharing argument, we conclude by saying that if (R1 , R2 , D) is
strict-sense achievable for the CEO problem, then
R1 ≥ I(Y1 ; U1 |X, Q) + H(X|U2 , Q) − D
R2 ≥ I(Y2 ; U2 |X, Q) + H(X|U1 , Q) − D
R1 + R2 ≥ I(U1 ; Y1 |X, Q) + I(U2 ; Y2 |X, Q) + H(X) − D
D ≥ H(X|U1 , U2 , Q).
for some joint distribution p(q)p(x, y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q).
?

Theorem 3. RDoCEO = RDiCEO = RDCEO .
Proof. We first remark that the cardinality bounds on the alphabets in the
definition of RDiCEO can be imposed without any loss of generality. This is a
consequence of [17, Lemma 2.2] and is discussed in detail in Appendix A.
Therefore, it will suffice to show RDoCEO ⊆ RDiCEO without considering
the cardinality bounds. To this end, fix p(q), p(u1 |y1 , q), and p(u2 |y2 , q) and

9

consider the extreme points1 of polytope defined by the inequalities (1):


P1 = 0, 0, I(Y1 ; U1 |X, Q) + I(Y2 ; U2 |X, Q) + H(X)


P2 = I(Y1 ; U1 |Q), 0, I(U2 ; Y2 |X, Q) + H(X|U1 , Q)


P3 = 0, I(Y2 ; U2 |Q), I(U1 ; Y1 |X, Q) + H(X|U2 , Q)


P4 = I(Y1 ; U1 |Q), I(Y2 ; U2 |U1 , Q), H(X|U1 , U2 , Q)


P5 = I(Y1 ; U1 |U2 , Q), I(Y2 ; U2 |Q), H(X|U1 , U2 , Q) ,
(j)

(j)

(j)

(j)

where the point Pj is a triple (R1 , R2 , D(j) ). We say a point (R1 , R2 , D(j) )
is dominated by a point in RDiCEO if there exists some (R1 , R2 , D) ∈ RDiCEO
(j)
(j)
for which R1 ≤ R1 , R2 ≤ R2 , and D ≤ D(j) . Observe that each of the
extreme points P1 , . . . , P5 is dominated by a point in RDiCEO :
• First, observe that P4 and P5 are both in RDiCEO , so these points are not
problematic.
• Next, observe that the point (0, 0, H(X)) is in RDiCEO , which can be
seen by setting all auxiliary random variables to be constant. This point
dominates P1 .
• By using auxiliary random variables (Û1 , Û2 , Q) = (U1 , ∅, Q), the point
(I(Y1 ; U1 |Q), 0, H(X|U1 , Q)) is in RDiCEO , and dominates the point P2 .
By a symmetric argument, the point P3 is also dominated by a point in
RDiCEO .
Since RDoCEO is the convex hull of all such extreme points (i.e., the convex
hull of the union of extreme points over all appropriate joint distributions), the
theorem is proved.
Remark 1. Theorem 3 can be extended to the general case of m-encoders.
Details are provided in Appendix B.

3.3

A stronger converse result for the CEO problem

As defined, our reproduction sequence X̂ n is restricted to be a product distribution on X n . However, for a blocklength n code, we can allow X̂ n to be any
probability distribution on X n and the converse result still holds. In this case,
we define the sequence distortion as follows:


1
1
d(xn , x̂n ) = log
,
n
x̂n (xn )
1 For two encoders, it is easy enough to enumerate the extreme points by inspection. However, this can be formalized by a submodularity argument, which is given in Appendix B.

10

which is compatible with the original definition when X̂ n is a product distribution. The reader can verify that the result of Lemma 1 is still true for this more
general distortion alphabet by setting s(xn |z) = x̂n (xn ) in the corresponding
proof. Since Lemma 1 is the key tool in the CEO converse result, this implies
that the converse holds even if X̂ n is allowed to be any probability distribution
on X n (rather than being restricted to the set of product distributions).
When this stronger converse result is taken together with the achievability
result, we observe that restricting X̂ n to be a product distribution is in fact
?
optimal and can achieve all points in RDCEO .

3.4

An Example: Distributed compression of a posterior
distribution

Suppose two sensors observe sequences Y1n and Y2n respectively, which are conditionally independent given a hidden sequence X n . The sensors communicate
with a fusion center through rate-limited links of capacity R1 and R2 respectively. Given sequences (Y1n , Y2n ) are observed, the sequence X n cannot be
determined in general, so the fusion center would like to estimate the posterior
distribution p(xn |Y1n , Y2n ). Since the communication links are rate-limited, the
fusion center cannot necessarily compute p(xn |Y1n , Y2n ) exactly. In this case, the
(n)
(n)
fusion center would like to generate an estimate p̂(xn |g1 (Y1n ), g2 (Y2n )) that
should approximate p(xn |Y1n , Y2n ) in the sense that, on average:


(n)
(n)
D p(xn |y1n , y2n ) p̂(xn |g1 (y1n ), g2 (y2n )) ≤ nε,
where, consistent with standard notation (e.g.
(n)
(n)
D(p(xn |y1n , y2n )kp̂(xn |g1 (y1n ), g2 (y2n ))) as shorthand for
X

p(xn , y1n , y2n ) log

xn ,y1n ,y2n

[18]),

p(xn |y1n , y2n )
(n)

(n)

p̂(xn |g1 (y1n ), g2 (y2n ))

we

write

.

The relevant question here is the following. What is the minimum distortion ε
that is attainable given R1 and R2 ?
Considering the CEO problem for this setup, we have:


X
1
1
Ed(X̂ n , X n ) =
p(xn , y1n , y2n ) log
n n n n
x̂n (xn )
(x ,y1 ,y2 )
 1
1 
= D p(xn |y1n , y2n ) x̂n (xn ) + H(X n |Y1n , Y2n ).
n
n
(n)

(n)

Identifying p̂(xn |g1 (Y1n ), g2 (Y2n )) ← X̂ n (xn ), we have:


(n)
(n)
D p(xn |y1n , y2n ) p̂(xn |g1 (y1n ), g2 (y2n )) = nEd(X̂ n , X n ) − nH(X|Y1 , Y2 ).

11

BSC(α)

Y1n

Encoder
R

Xn
BSC(α)

Y2n

Decoder

Encoder

X̂ n
Ed(X n , X̂ n ) ≤ D

R
Figure 2: An example CEO problem where X ∼ Bernoulli( 12 ), Pr(Yi = X) =
(1 − α), and both encoders are subject to the same rate constraint.

Thus, finding the minimum possible distortion reduces to an optimization prob?
lem over RDCEO . In particular, the minimum attainable distortion ε∗ is given
by
n
o
?
ε∗ = inf D : (R1 , R2 , D) ∈ RDCEO − H(X|Y1 , Y2 ).
(7)
Moreover, the minimum distortion is obtained by estimating each xj separately. In other words, there exists an optimal (essentially, for large n) estimate
∗(n)
p̂∗ (xn |·, ·) (which is itself a function of optimal encoding functions g1 (·) and
∗(n)
g2 (·)) that can be expressed as a product distribution
∗

n

p̂ (x |·, ·) =

n
Y



∗(n)
∗(n)
p̂∗j xj |g1 (·), g2 (·) .

j=1

For this choice of p̂∗ (xn |·, ·), we have the following relationship:
n


1X 
∗(n)
∗(n)
D p(xj |y1,j , y2,j ) p̂∗j xj |g1 (y1n ), g2 (y2n )
= ε∗ .
n j=1

In light of this fact, one can apply Markov’s inequality to obtain the following
estimate on peak component-wise distortion:
(
)



ε∗
∗(n) n
∗(n) n
∗
# j D p(xj |y1,j , y2,j ) p̂j xj |g1 (y1 ), g2 (y2 )
≥ζ ≤n ,
ζ
where #(·) is the counting measure.
To make this example more concrete, consider the scenario depicted in Figure
2, where X ∼ Bernoulli( 12 ) and Yi is the result of passing X through a binary
symmetric channel with crossover probability α for i = 1, 2. To simplify things,
we constrain the rates of each encoder to be at most R bits per channel use.
By performing a brute-force search over a fine mesh of conditional distributions {p(ui |yi )}2i=1 , we numerically approximate the set of (R, D) pairs such that
?
(R, R, D) is in the achievable region RDCEO corresponding to the network in
Figure 2. The lower convex envelope of these (R, D) pairs is plotted in Figure 3
12

1
0.9

  

0.8
0.7



0.6
0.5

  

0.4
0.3
0.2

  

0.1
0

0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

1

Figure 3: The distortion-rate function of the network in Figure 2 computed for
α ∈ {0.01, 0.1, 0.25}.
for α ∈ {0.01, 0.1, 0.25}. Continuing our example above for this concrete choice
of source parameters, we compute the minimum achievable Kullback-Leibler
distance ε∗ according to (7). The result is given in Figure 4.
These numerical results are intuitively satisfying in the sense that, if Y1 , Y2
are high-quality estimates of X (e.g., α = 0.01), then a small increase in the
allowable rate R results in a large relative improvement of p̂(x|·, ·), the decoder’s
estimate of p(x|Y1 , Y2 ). On the other hand, if Y1 , Y2 are poor-quality estimates
of X (e.g., α = 0.25), then we require a large increase in the allowable rate R
in order to obtain an appreciable improvement of p̂(x|·, ·).
One field where this example is directly applicable is machine learning. In
this case, Xj could represent the class of object j, and Y1,j , Y2,j are observable
attributes. In machine learning, one typically estimates the probability that an
object belongs to a particular class given a set of observable attributes. For this
type of estimation problem, relative entropy is a natural penalty criterion.
Another application is to horse-racing with conditionally independent, ratelimited side informations. In this case, the doubling rate of the gambler’s wealth
can be expressed in terms of the logarithmic loss distortion measure. This
example is consistent with the original interpretation of the CEO problem, where
the CEO makes consecutive business decisions (investments) having outcomes
X n , with the objective of maximizing the wealth of the company. We omit the
details.

13

1

 

0.9
0.8
0.7



0.6

 

0.5
0.4
0.3

 

0.2
0.1
0

0

0.1

0.2

0.3

0.4



0.5

0.6

0.7

0.8

0.9

1

Figure 4: The minimum achievable Kullback-Leibler distance computed according to (7), i.e., the curves here are those of Figure 3, lowered by the constant
H(X|Y1 , Y2 ).

3.5

An Example: Joint estimation of the encoder observations

Suppose one wishes to estimate the encoder observations (Y1 , Y2 ). In this case,
the rate region simplifies considerably. In particular, if we tolerate a distortion
D in our estimate of the pair (Y1 , Y2 ), then the achievable rate region is the
same as the Slepian-Wolf rate region with each rate constraint relaxed by D
bits. Formally:
?

Theorem 4. If X = (Y1 , Y2 ), then RDCEO consists of all vectors (R1 , R2 , D)
satisfying
R1 ≥ H(Y1 |Y2 ) − D
R2 ≥ H(Y2 |Y1 ) − D
R1 + R2 ≥ H(Y1 , Y2 ) − D
D ≥ 0.
?

Proof. First, note that Theorem 3 implies that RDCEO is equivalent to the
the union of (R1 , R2 , D) triples satisfying (1) taken over all joint distributions
p(q)p(x, y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q). Now, since X = (Y1 , Y2 ), each of the in-

14

equalities (1) can be lower bounded as follows:
R1 ≥ I(Y1 ; U1 |Y1 , Y2 , Q) + H(Y1 , Y2 |U2 , Q) − D
= H(Y2 |U2 , Q) + H(Y1 |Y2 ) − D
≥ H(Y1 |Y2 ) − D
R2 ≥ I(Y2 ; U2 |Y1 , Y2 , Q) + H(Y1 , Y2 |U1 , Q) − D
= H(Y1 |U1 , Q) + H(Y2 |Y1 ) − D
≥ H(Y2 |Y1 ) − D
R1 + R2 ≥ I(U1 ; Y1 |Y1 , Y2 , Q) + I(U2 ; Y2 |Y1 , Y2 , Q) + H(Y1 , Y2 ) − D
= H(Y1 , Y2 ) − D
D ≥ H(Y1 , Y2 |U1 , U2 , Q)
≥ 0.
Finally, observe that by setting Ui = Yi for i = 1, 2, we can achieve any point
in this relaxed region (again, a consequence of Theorem 3).
We remark that this result was first proved in [10] by Courtade and Wesel
using a different method.

4

Multiterminal Source Coding

With Theorem 3 in hand, we are now in a position to characterize the achievable
?
rate distortion region RD for the multiterminal source coding problem under
logarithmic loss. As before, we prove an inner bound first.

4.1

Inner Bound

Definition 5. Let (R1 , R2 , D1 , D2 ) ∈ RDi if and only if there exists a joint
distribution of the form
p(y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)p(q)
where |U1 | ≤ |Y1 |, |U2 | ≤ |Y2 |, and |Q| ≤ 5, which satisfies
R1 ≥ I(Y1 ; U1 |U2 , Q)
R2 ≥ I(Y2 ; U2 |U1 , Q)
R1 + R2 ≥ I(U1 , U2 ; Y1 , Y2 |Q)
D1 ≥ H(Y1 |U1 , U2 , Q)
D2 ≥ H(Y2 |U1 , U2 , Q).
?

Theorem 5. RDi ⊆ RD . That is, all rate distortion vectors in RDi are
achievable.
Again, we require an appropriate version of the Berger-Tung inner bound:
15

Proposition 2 (Berger-Tung Inner Bound [14, 15]). The rate distortion vector
(R1 , R2 , D1 , D2 ) is achievable if
R1 ≥ I(U1 ; Y1 |U2 , Q)
R2 ≥ I(U2 ; Y2 |U1 , Q)
R1 + R2 ≥ I(U1 , U2 ; Y1 , Y2 |Q)
D1 ≥ E [d(Y1 , f1 (U1 , U2 , Q)]
D2 ≥ E [d(Y2 , f2 (U1 , U2 , Q)] .
for a joint distribution
p(y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)p(q)
and reproduction functions
fi : U1 × U2 × Q → Ŷi , for i = 1, 2.
Proof of Theorem 5. To prove the theorem, we simply apply Proposition 2 with
the reproduction functions fi (U1 , U2 , Q) := Pr [Yi = yi |U1 , U2 , Q].
?

Hence, we again see that our inner bound RDi ⊆ RD is nothing more
than the Berger-Tung inner bound specialized to the setting when distortion is
measured under logarithmic loss.

4.2

A Matching Outer Bound

The main result of this paper is the following theorem.
?

Theorem 6. RDi = RD .
Proof. As before, we note that the cardinality bounds on the alphabets in the
definition of RDi can be imposed without any loss of generality. This is discussed in detail in Appendix A.
Assume (R1 , R2 , D1 , D2 ) is strict-sense achievable. Observe that proving
?
that (R1 , R2 , D1 , D2 ) ∈ RDi will prove the theorem, since RDi ⊆ RD and
?
RD is closed by definition.
For convenience, define P(R1 , R2 ) to be the set of joint distributions of the
form
p(y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)p(q)
with |U1 | ≤ |Y1 |, |U2 | ≤ |Y2 |, and |Q| ≤ 4 satisfying
R1 ≥ I(U1 ; Y1 |U2 , Q)
R2 ≥ I(U2 ; Y2 |U1 , Q)
R1 + R2 ≥ I(U1 , U2 ; Y1 , Y2 |Q).

16

We remark that P(R1 , R2 ) is compact. We also note that it will suffice to show
the existence of a joint distribution in P(R1 , R2 ) satisfying H(Y1 |U1 , U2 , Q) ≤
D1 and H(Y2 |U1 , U2 , Q) ≤ D2 to prove that (R1 , R2 , D1 , D2 ) ∈ RDi .
With foresight, consider random variable X defined as follows

(Y1 , 1) with probability t
X=
(8)
(Y2 , 2) with probability 1 − t.
In other words, X = (YB , B), where B is a Bernoulli random variable independent of Y1 , Y2 . Observe that Y1 ↔ X ↔ Y2 form a Markov chain, and thus, we
are able to apply Theorem 3.
Since (R1 , R2 , D1 , D2 ) is strict-sense achievable, the decoder can construct
reproductions Ŷ1n , Ŷ2n satisfying
n

1X
Ed(Yi,j , Ŷi,j ) ≤ Di for i = 1, 2.
n j=1
Fix the encoding operations and set X̂j ((y1 , 1)) = tŶ1,j (y1 ) and X̂j ((y2 , 2)) =
(1 − t)Ŷ2,j (y2 ). Then for the CEO problem defined by (X, Y1 , Y2 ):
n

1X
Ed(Xj , X̂j )
n j=1
n

t X
=
E log
n j=1

1
tŶ1,j (Y1,j )

!

n

1−tX
+
E log
n j=1

n

= h2 (t) +

1

!

(1 − t)Ŷ2,j (Y2,j )

n

t X
1−tX
Ed(Y1,j , Ŷ1,j ) +
Ed(Y2,j , Ŷ2,j )
n j=1
n j=1

≤ h2 (t) + tD1 + (1 − t)D2
where h2 (t) is the binary entropy function. Hence, for this CEO problem,
distortion h2 (t) + tD1 + (1 − t)D2 is achievable and Theorem 3 yields a joint
distribution2 Pt ∈ P(R1 , R2 ) satisfying
(t)

(t)

h2 (t) + tD1 + (1 − t)D2 ≥ H(X|U1 , U2 , Q(t) )
(t)

(t)

(t)

(t)

= h2 (t) + tH(Y1 |U1 , U2 , Q(t) )
+ (1 − t)H(Y2 |U1 , U2 , Q(t) ),
where the second equality follows by by definition of X in (8). For convenience,
(t)
(t)
(t)
(t)
define H1 (Pt ) , H(Y1 |U1 , U2 , Q(t) ) and H2 (Pt ) , H(Y2 |U1 , U2 , Q(t) ).
Note the following two facts:
1. By continuity of entropy, the functions H1 (·) and H2 (·) are continuous on
the compact domain P(R1 , R2 ).
2 Henceforth, we use the superscript (t) to explicitly denote the dependence of the auxiliary
random variables on the distribution parametrized by t.

17

2. The above argument proves the existence of a function ϕ : [0, 1] →
P(R1 , R2 ) which satisfies
tH1 (ϕ(t)) + (1 − t)H2 (ϕ(t)) ≤ tD1 + (1 − t)D2 for all t ∈ [0, 1].
These two facts satisfy the requirements of Lemma 7 (see Appendix D), and
hence there exists Pt1 ∈ P(R1 , R2 ), Pt2 ∈ P(R1 , R2 ), and θ ∈ [0, 1] for which
θH1 (Pt1 ) + (1 − θ)H1 (Pt2 ) ≤ D1
θH2 (Pt1 ) + (1 − θ)H2 (Pt2 ) ≤ D2 .
Timesharing3 between distributions Pt1 and Pt2 with probabilities θ and (1−
θ), respectively, yields a distribution P ∗ ∈ P(R1 , R2 ) which satisfies H1 (P ∗ ) ≤
D1 and H2 (P ∗ ) ≤ D2 . This proves the theorem.

4.3

A stronger converse

For the CEO problem, we are able to obtain a stronger converse result as discussed in Section 3.3. We can obtain a similar result for the multiterminal
source coding problem. Indeed, the converse result we just proved continues to
hold even when Ŷin is allowed to be any probability measure on Yin , rather than
a product distribution. The proof of this fact is somewhat involved and can be
found in Appendix E.
We note that the proof of this strengthened converse result (i.e., Theorem
13 in Appendix E) offers a direct proof of the converse of Theorem 6, and
as such we do not require a CEO result (Theorem 3) or a “black box” tuning
argument (Lemma 7). At the heart of this alternative proof lies the Csiszár sum
identity (and a careful choice of auxiliary random variables) which provides a
coupling between the attainable distortions for each source. In the original proof
of Theorem 6, this coupling is accomplished by the tuning argument through
Lemma 7.
Interestingly, the two proofs are similar in spirit, with the key differences being the use of the Csiszár sum identity versus the tuning argument. Intuitively,
the original tuning argument allows a “clumsier” choice of auxiliary random
variables which leads to a more elegant and transparent proof, but appears
incapable of establishing the strengthened converse. On the other hand, applying the Csiszár sum identity requires a very careful choice of auxiliary random
variables which, in turn, affords a finer degree of control over various quantities.

4.4

An Example: The Daily Double

The Daily Double is a single bet that links together wagers on the winners of
two consecutive horse races. Winning the Daily Double is dependent on both
wagers winning together. In general, the outcomes of two consecutive races can
3 The timesharing scheme can be embedded in the timesharing variable Q, increasing the
cardinality of Q by a factor of two.

18

be correlated (e.g. due to track conditions), so a gambler can potentially use
this information to maximize his expected winnings. Let Y1 and Y2 be the set
of horses running in the first and second races respectively. If horses y1 and
y2 win their respective races, then the payoff is o(y1 , y2 ) dollars for each dollar
invested in outcome (Y1 , Y2 ) = (y1 , y2 ).
There are two betting strategies one can follow:
1. The gambler can wager a fraction b1 (y1 ) of his wealth on horse y1 winning
the first race and parlay his winnings by betting a fraction b2 (y2 ) of his
wealth on horse y2 winning the second race. In this case, the gambler’s
wealth relative is b1 (Y1 )b2 (Y2 )o(Y1 , Y2 ) upon learning the outcome of the
Daily Double. We refer to this betting strategy as the product-wager.
2. The gambler can wager a fraction b(y1 , y2 ) of his wealth on horses (y1 , y2 )
winning the first and second races, respectively. In this case, the gambler’s
wealth relative is b(Y1 , Y2 )o(Y1 , Y2 ) upon learning the outcome of the Daily
Double. We refer to this betting strategy as the joint-wager.
Clearly the joint-wager includes the product-wager as a special case. However,
the product-wager requires less effort to place, so the question is: how do the
two betting strategies compare?
To make things interesting, suppose the gamblers have access to rate-limited
information about the first and second race outcomes at rates R1 , R2 respectively. Further, assume that R1 ≤ H(Y1 ), R2 ≤ H(Y2 ), and R1 + R2 ≤
H(Y1 , Y2 ). For (R1 , R2 ) and p(y1 , y2 ) given, let P(R1 , R2 ) denote the set of
joint pmf’s of the form
p(q, y1 , y2 , u1 , u2 ) = p(q)p(y1 , y2 )p(u1 |y1 , q)p(u1 |y1 , q)
which satisfy
R1 ≥ I(Y1 ; U1 |U2 , Q)
R2 ≥ I(Y2 ; U2 |U1 , Q)
R1 + R2 ≥ I(Y1 , Y2 ; U1 , U2 |Q)
for alphabets U1 , U2 , Q satisfying |Ui | ≤ |Yi | and |Q| ≤ 5.
Typically, the quality of a bet is measured by the associated doubling rate
(cf. [18]). Theorem 6 implies that the optimal doubling rate for the productwager is given by:
X
∗
Wp-w
(p(y1 , y2 )) =
p(y1 , y2 ) log b∗1 (y1 )b∗2 (y2 )o(y1 , y2 )
y1 ,y2

= E log o(Y1 , Y2 ) −

inf
p∈P(R1 ,R2 )

{H(Y1 |U1 , U2 , Q) + H(Y2 |U1 , U2 , Q)} .

Likewise, Theorem 4 implies that the optimal doubling rate for the joint-wager

19

is given by:
∗
Wj-w
(p(y1 , y2 )) =

X

p(y1 , y2 ) log b∗ (y1 , y2 )o(y1 , y2 )

y1 ,y2

= E log o(Y1 , Y2 ) + min{R1 − H(Y1 |Y2 ), R2 − H(Y2 |Y1 ),
R1 + R2 − H(Y1 , Y2 )}.
It is important to note that we do not require the side informations to be
the same for each type of wager, rather, the side informations are only provided at the same rates. Thus, the gambler placing the joint-wager receives
side information at rates (R1 , R2 ) that maximizes his doubling rate, while the
gambler placing the product-wager receives (potentially different) side information at rates (R1 , R2 ) that maximizes his doubling rate. However, as we will
see shortly, for any rates (R1 , R2 ), there always exists rate-limited side information which simultaneously allows each type of gambler to attain their maximum
doubling rate.
∗
∗
(p(y1 , y2 )) and Wj-w
(p(y1 , y2 )), we
By combining the expressions for Wp-w
find that the difference in doubling rates is given by:
∗
∗
∆(R1 , R2 ) = Wj-w
(p(y1 , y2 )) − Wp-w
(p(y1 , y2 ))
n
o
= min R1 − H(Y1 |Y2 ), R2 − H(Y2 |Y1 ), R1 + R2 − H(Y1 , Y2 )

+

{H(Y1 |U1 , U2 , Q) + H(Y2 |U1 , U2 , Q)}
(9)
n
min R1 − I(Y1 ; U1 |U2 , Q) + I(Y1 ; Y2 ) − I(Y1 ; U2 , Q) + H(Y2 |U1 , U2 , Q),

inf

p∈P(R1 ,R2 )

= inf

p∈P(R1 ,R2 )

R2 − I(Y2 ; U2 |U1 , Q) + I(Y2 ; Y1 ) − I(Y2 ; U1 , Q) + H(Y1 |U1 , U2 , Q),
o
R1 + R2 − I(Y1 , Y2 ; U1 , U2 |Q) + I(Y1 ; Y2 |U1 , U2 , Q)
= inf
p∈P(R1 ,R2 )

I(Y1 ; Y2 |U1 , U2 , Q).

(10)

The final equality (10) follows since
• R1 ≥ I(Y1 ; U1 |U2 , Q) and R2 ≥ I(Y2 ; U2 |U1 , Q) for any p ∈ P(R1 , R2 ).
• I(Y2 ; Y1 ) ≥ I(Y2 ; U1 , Q) and I(Y1 ; Y2 ) ≥ I(Y1 ; U2 , Q) for any p ∈
P(R1 , R2 ) by the data processing inequality.
• The infimum in (9) is attained by a p ∈ P(R1 , R2 ) satisfying R1 + R2 =
I(Y1 , Y2 ; U1 , U2 |Q). See Lemma 10 in Appendix F for details.
• By definition of conditional mutual information,
H(Yi |U1 , U2 , Q) ≥ I(Y1 ; Y2 |U1 , U2 , Q)
for i = 1, 2.

20

Let p∗ ∈ P(R1 , R2 ) be the distribution that attains the infimum in (9) (such
a p always exists), then (10) yields
∗

∗
∗
Wj-w
(p(y1 , y2 )) − Wp-w
(p(y1 , y2 ))
X
X
=
p∗ (u1 , u2 , q)
p∗ (y1 , y2 |u1 , u2 , q) log
u1 ,u2 ,q

=E

p∗

y1 ,y2

p∗ (y1 , y2 |u1 , u2 , q)
p∗ (y1 |u1 , u2 , q)p∗ (y2 |u1 , u2 , q)

∗

log o(Y1 , Y2 )p (Y1 , Y2 |U1 , U2 , Q)

− Ep∗ log o(Y1 , Y2 )p∗ (Y1 |U1 , U2 , Q)p∗ (Y2 |U1 , U2 , Q).
Hence, we can interpret the auxiliary random variables corresponding to p∗ as
optimal rate-limited side informations for both betting strategies. Moreover,
optimal bets for each strategy are given by
1. b∗ (y1 , y2 ) = p∗ (y1 , y2 |u1 , u2 , q) for the joint-wager, and
2. b∗1 (y1 ) = p∗ (y1 |u1 , u2 , q), b∗2 (y2 ) = p∗ (y2 |u1 , u2 , q) for the product-wager.
Since P(R1 , R2 ) ⊆ P(R10 , R20 ) for R1 ≤ R10 and R2 ≤ R20 , the function
∆(R1 , R2 ) is nonincreasing in R1 and R2 . Thus, the benefits of using the jointwager over the product-wager diminish in the amount of side-information available. It is also not difficult to show that ∆(R1 , R2 ) is jointly convex in (R1 , R2 ).
Furthermore, for rate-pairs (R1 , R2 ) and (R10 , R20 ) satisfying R1 < R10 and
R2 < R20 , there exist corresponding optimal joint- and product-wagers b∗ (y1 , y2 )
0
0
0
and b∗1 (y1 )b∗2 (y2 ), and b∗ (y1 , y2 ) and b∗1 (y1 )b∗2 (y2 ), respectively, satisfying
 0



0
0
D b∗ (y1 , y2 ) b∗1 (y1 )b∗2 (y2 ) < D b∗ (y1 , y2 ) b∗1 (y1 )b∗2 (y2 ) .
(11)
So, roughly speaking, the joint-wager and product-wager look “more alike” as
the amount of side information is increased. The proof of the strict inequality
in (11) can be inferred from the proof of Lemma 10 in Appendix F.
To conclude this example, we note that ∆(R1 , R2 ) enjoys a great deal of
symmetry near the origin in the sense that side information from either encoder
contributes approximately the same amount to the improvement of the productwager. We state this formally as a theorem:
Theorem 7. Define ρm (Y1 , Y2 ) to be the Hirschfeld-Gebelein-Rényi maximal
correlation between random variables Y1 and Y2 . Then, ∆(R1 , R2 ) ≥ I(Y1 ; Y2 )−
ρ2m (Y1 , Y2 ) · (R1 + R2 ). Moreover, this bound is tight as (R1 , R2 ) → (0, 0).
Proof. If R2 = 0, then it is readily verified that ∆(R1 , 0) can be expressed as
follows:
∆(R1 , 0) = I(Y1 ; Y2 ) −

max

I(U1 ; Y2 ).

max

I(U2 ; Y1 ).

p(u1 |y1 ):I(U1 ;Y1 )=R1 ,
U1 →Y1 →Y2 , |U1 |≤|Y1 |+1

By symmetry:
∆(0, R2 ) = I(Y1 ; Y2 ) −

p(u2 |y2 ):I(U2 ;Y2 )=R2 ,
U2 →Y2 →Y1 , |U2 |≤|Y2 |+1

21

Here, we can apply a result of Erkip [19, Theorem 10] to evaluate the gradient
of ∆(R1 , R2 ) at (R1 , R2 ) = (0, 0):
∂
∂
=
= −ρ2m (Y1 , Y2 ).
∆(R1 , R2 )
∆(R1 , R2 )
∂R1
∂R
2
(R1 ,R2 )=(0,0)
(R1 ,R2 )=(0,0)
(12)
Note, since ∆(R1 , 0) and ∆(0, R2 ) are each convex in their respective variable
and ∆(0, 0) = I(Y1 ; Y2 ), we have
∆(R1 , 0) ≥ I(Y1 ; Y2 ) − ρ2m (Y1 , Y2 )R1
∆(0, R2 ) ≥ I(Y1 ; Y2 ) − ρ2m (Y1 , Y2 )R2 .

(13)

Taking this one step further, for ν1 , ν2 > 0, we can evaluate the one-sided
derivative:
lim
λ↓0

∆(λν1 , λν2 ) − ∆(0, 0)
= −ρ2m (Y1 , Y2 ) · (ν1 + ν2 ).
λ

(14)

We remark that (14) does not follow immediately from (12) since the point at
which we are taking the derivatives (i.e., the origin) does not lie in an open
neighborhood of the domain. Nonetheless, the expected result holds.
Since ∆(R1 , R2 ) is convex, we obtain an upper bound on the one-sided
derivative as follows:
1
∆(2λν1 , 0) + 12 ∆(0, 2λν2 ) − ∆(0, 0; p)
∆(λν1 , λν2 ) − ∆(0, 0)
≤ lim 2
λ↓0
λ↓0
λ
λ
1
∆(λ2ν1 , 0) − ∆(0, 0)
= lim
2 λ↓0
λ
1
∆(0, λ2ν2 ) − ∆(0, 0)
+ lim
2 λ↓0
λ
2
= −ρm (Y1 , Y2 ) · (ν1 + ν2 ),

lim

where the final equality follows by (12) and the positive homogeneity of the
directional derivative.
Therefore, to complete the proof of (14), it suffices to prove the lower bound
∆(λν1 , λν2 ) − ∆(0, 0)
≥ −ρ2m (Y1 , Y2 ) · (ν1 + ν2 ).
λ↓0
λ

lim

22

To this end, fix λ, ν1 , ν2 > 0 and observe that
∆(λν1 , λν2 ) − ∆(0, 0)
λ
n
o
1
=
I(Y1 ; Y2 |U1 , U2 |Q) − I(Y1 ; Y2 )
(15)
inf
λ p∈P(λν1 ,λν2 )
n
o
1
=
I(Y1 , Y2 ; U1 , U2 |Q) − I(Y1 ; U1 , U2 |Q) − I(Y2 ; U1 , U2 |Q)
inf
λ p∈P(λν1 ,λν2 )

1
Ip∗ (Y1 ; U1 , U2 |Q) + Ip∗ (Y2 ; U1 , U2 |Q)
(16)
= (ν1 + ν2 ) −
λ

1
Ip∗ (Y1 ; U1 |U2 , Q) + Ip∗ (Y1 ; U2 |Q)
= (ν1 + ν2 ) −
λ

+ Ip∗ (Y2 ; U2 |U1 , Q) + Ip∗ (Y2 ; U1 |Q)

≥ (ν1 + ν2 ) − ρ2m (Y1 , Y2 ) (2ν1 + 2ν2 )
(1 − ρ2m (Y1 , Y2 ))
(Ip∗ (Y1 ; U1 |U2 , Q) + Ip∗ (Y2 ; U2 |U1 , Q))
λ
= −ρ2m (Y1 , Y2 ) (ν1 + ν2 ) + (1 − ρ2m (Y1 , Y2 )) (ν1 + ν2 )
−

(1 − ρ2m (Y1 , Y2 ))
(Ip∗ (Y1 ; U1 |U2 , Q) + Ip∗ (Y2 ; U2 |U1 , Q))
λ
≥ −ρ2m (Y1 , Y2 ) (ν1 + ν2 ) .

(17)

−

(18)

In the above string of inequalities
• (15) follows by definition of ∆(R1 , R2 ).
• Equality (16) follows since Lemma 10 guarantees that the infimum is attained in (15) for some p∗ ∈ P(λν1 , λν2 ) satisfying Ip∗ (Y1 , Y2 ; U1 , U2 |Q) =
λ(ν1 + ν2 ). Here, we write Ip∗ (Y1 , Y2 ; U1 , U2 |Q) to denote the mutual
information I(Y1 , Y2 ; U1 , U2 |Q) evaluated for the distribution p∗ .
• To see that (17) holds, note that
Ip∗ (Y2 ; U2 |Q) = λν1 + λν2 − Ip∗ (Y1 ; U1 |U2 , Q),
and thus
I(Y1 ; Y2 ) − ρ2m (Y1 , Y2 ) (λν1 + λν2 − Ip∗ (Y1 ; U1 |U2 , Q))
≤ ∆(0, λν1 + λν2 − Ip∗ (Y1 ; U1 |U2 , Q))
= I(Y1 ; Y2 ) −

max

(19)
I(Ũ2 ; Y1 )

(20)

p(ũ2 |y2 ):I(Y2 ;Ũ2 )≤λν1 +λν2 −Ip∗ (Y1 ;U1 |U2 ,Q),
Ũ2 ↔Y2 ↔Y1

≤ I(Y1 ; Y2 ) − Ip∗ (Y1 ; U2 |Q),
which implies
−ρ2m (Y1 , Y2 ) (λν1 + λν2 − Ip∗ (Y1 ; U1 |U2 , Q)) ≤ −Ip∗ (Y1 ; U2 |Q).
The above steps are justified as follows:
23

(21)

– (19) follows from (13).
– (20) follows by definition of the function ∆(0, x).
– (21) follows since Q is independent of Y1 , Y2 (by definition of p∗ ), and
thus Ũ2 = (U2 , Q) lies in the set over which we take the maximum in
(20).
By symmetry, we conclude that
− (Ip∗ (Y1 ; U2 |Q) + Ip∗ (Y2 ; U1 |Q))
≥ −ρ2m (Y1 , Y2 ) (2λν1 + 2λν2 − Ip∗ (Y1 ; U1 |U2 , Q) − Ip∗ (Y2 ; U2 |U1 , Q)) ,
and (17) follows.
• (18) follows since λν1 ≥ Ip∗ (Y1 ; U1 |U2 , Q) and λν2 ≥ Ip∗ (Y2 ; U2 |U1 , Q) for
p∗ ∈ P(λν1 , λν2 ).

4.5

An Application: List Decoding

In the previous example, we did not take advantage of the stronger converse
result which we proved in Appendix E (see the discussion in Section 4.3). In
this section, we give an application that requires this strengthened result.
Formally, a 2-list code (of blocklength n consists) of encoding functions:
n
o
(n)
(n)
gi : Yin → 1, . . . , Mi
for i = 1, 2
and list decoding functions
n
o n
o
n
(n)
(n)
(n)
L1 : 1, . . . , M1
× 1, . . . , M2
→ 2Y1
n
o n
o
n
(n)
(n)
(n)
L2 : 1, . . . , M1
× 1, . . . , M2
→ 2Y2 .
A list decoding tuple (R1 , R2 , ∆1 , ∆2 ) is achievable if, for any  > 0, there exists
a 2-list code of blocklength n satisfying the rate constraints
1
(n)
log M1 ≤ R1 + 
n
1
(n)
log M2 ≤ R2 + ,
n
and the probability of list-decoding error constraints
i
h

(n)
(n)
(n)
Pr Y1n ∈
/ L1
g1 (Y1n ), g2 (Y2n ) ≤ ,
h

i
(n)
(n)
(n)
Pr Y2n ∈
/ L2
g1 (Y1n ), g2 (Y2n ) ≤ .

24

with list sizes
1
(n)
log |L1 | ≤ ∆1 + 
n
1
(n)
log |L2 | ≤ ∆2 + .
n
With a 2-list code so defined, the following theorem shows that the 2-list decoding problem and multiterminal source coding problem under logarithmic loss
are equivalent (inasmuch as the achievable regions are identical):
Theorem 8. The list decoding tuple (R1 , R2 , ∆1 , ∆2 ) is achievable if and only
if
R1 ≥ I(U1 ; Y1 |U2 , Q)
R2 ≥ I(U2 ; Y2 |U1 , Q)
R1 + R2 ≥ I(U1 , U2 ; Y1 , Y2 |Q)
∆1 ≥ H(Y1 |U1 , U2 , Q)
∆2 ≥ H(Y2 |U1 , U2 , Q).
for some joint distribution
p(y1 , y2 , u1 , u2 , q) = p(y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)p(q),
where |U1 | ≤ |Y1 |, |U2 | ≤ |Y2 |, and |Q| ≤ 5.
Remark 2. We note that a similar connection to list decoding can be made for
other multiterminal scenarios, in particular the CEO problem.
To prove the theorem, we require a slightly modified version of [20, Lemma
1]:
Lemma 2. If the list decoding tuple (R1 , R2 , ∆1 , ∆2 ) is achieved by a sequence
(n) (n)
(n)
(n)
of 2-list codes {g1 , g2 , L1 , L2 }n→∞ , then
(n)

(n)

(n)

(n)

(n)

(n)

H(Y1n |g1 (Y1n ), g2 (Y2n )) ≤ |L1 | + nn
H(Y2n |g1 (Y1n ), g2 (Y2n )) ≤ |L2 | + nn ,
where n → 0 as n → ∞.
Proof. The proof is virtually identical to that of [20, Lemma 1], and is therefore
omitted.
Proof of Theorem 8. First observe that the direct part is trivial. Indeed, for
a joint distribution p(y1 , y2 , u1 , u2 , q) = p(y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)p(q), apply
(n)
the Berger-Tung achievability scheme and take Li to be the set of yin sequences
which are jointly typical with the decoded quantizations (U1n , U2n ). This set has
cardinality no larger than 2n(H(Yi |U1 ,U2 ,Q)+) , which proves achievability.
25

To see the converse, note that setting
h
i
(n)
(n)
Ŷin = Pr Yin |g1 (Y1n ), g2 (Y2n )
(n)

(n)

achieves a logarithmic loss of n1 H(Yin |g1 (Y1n ), g2 (Y2n )) for source i in the
setting where reproductions are not restricted to product distributions. Applying the strengthened converse of Theorem 6 together with Lemma 2 yields the
desired result.

5

Relationship to the General Multiterminal
Source Coding Problem

In this section, we relate our results for logarithmic loss to multiterminal source
coding problems with arbitrary distortion measures and reproduction alphabets.
n
As before, we let {Y1,j , Y2,j }j=1 be a sequence of n independent, identically
distributed random variables with finite alphabets Y1 and Y2 , respectively, and
joint pmf p(y1 , y2 ).
In this section, the reproduction alphabets Y̆i , i = 1, 2, are arbitrary. We
also consider generic distortion measures:
d˘i : Yi × Y̆i → R+ for i = 1, 2,
where R+ denotes the set of nonnegative real numbers. The sequence distortion
is then defined as follows:
n
1X˘
di (yi,j , y̆i,j ).
d˘i (yin , y̆in ) =
n j=1

We will continue to let d(·, ·) and Ŷ1 , Ŷ2 denote the logarithmic loss distortion
measure and the associated reproduction alphabets, respectively.
A rate distortion code (of blocklength n) consists of encoding functions:
n
o
(n)
(n)
ği : Yin → 1, . . . , Mi
for i = 1, 2
and decoding functions
o n
o
n
(n)
(n)
(n)
→ Y̆in for i = 1, 2.
ψ̆i : 1, . . . , M1
× 1, . . . , M2
A rate distortion vector (R1 , R2 , D1 , D2 ) is strict-sense achievable if there
(n)
(n)
(n) (n)
exists a blocklength n, encoding functions ğ1 , ğ2 and a decoder (ψ̆1 , ψ̆2 )
such that
1
(n)
log Mi for i = 1, 2
n
Di ≥ Ed˘i (Yin , Y̆in ) for i = 1, 2.
Ri ≥

26

(22)
(23)

Where
(n)

(n)

(n)

Y̆in = ψ̆i (ğ1 (Y1n ), ğ2 (Y2n )) for i = 1, 2.
For these functions, we define the quantity


n


X
X
1
˘
(n) (n)
(n)
(n)
2−di (yi ,Y̆i,j )  for i = 1, 2. (24)
βi ğ1 , ğ2 , ψ̆1 , ψ̆2
E log 
:=
n j=1
yi ∈Yi



(n) (n)
(n)
(n)
Now, let βi (R1 , R2 , D1 , D2 ) be the infimum of the βi ğ1 , ğ2 , ψ̆1 , ψ̆2 ’s,
where the infimum is taken over all codes that achieve the rate distortion vector
(R1 , R2 , D1 , D2 ).
At this point it is instructive to pause and consider some examples.
Example 1 (Binary Sources and Hamming Distortion). For i = 1, 2, let Y̆i =
Yi = {0, 1} and let d˘i be the α-scaled Hamming distortion measure:

0 if y̆i = yi ,
˘
di (yi , y̆i ) =
α if y̆i 6= yi .
In this case,
˘

X

2−di (yi ,Y̆i,j ) = 20 + 2−α ,

(25)

yi ∈Yi

so βi (R1 , R2 , D1 , D2 ) = log(1 + 2−α ) for any (R1 , R2 , D1 , D2 ). This notion that
βi (R1 , R2 , D1 , D2 ) is a constant extends to all distortion measures for which the
columns of the |Yi | × |Y̆i | distortion matrix are permutations of one another.
Example 2 (Binary Sources and Erasure Distortion). For i = 1, 2, let Yi =
{0, 1}, Y̆i = {0, 1, e} and let d˘i be the standard erasure distortion measure:

 0 if y̆i = yi
1 if y̆i = e
d˘i (yi , y̆i ) =

∞ if y̆i ∈ {0, 1} and y̆i 6= yi .
In this case,
X
yi ∈Yi

−d˘i (yi ,Y̆i,j )

2


=

2−∞ + 20 = 1 if Y̆i,j ∈ {0, 1}
2−1 + 2−1 = 1 if Y̆i,j = e.

(26)

so βi (R1 , R2 , D1 , D2 ) = 0 for any (R1 , R2 , D1 , D2 ). This result can easily be
extended to erasure distortion on larger alphabets by setting the penalty to log |Yi |
when Y̆i = e.

27

Theorem 9. Suppose (R1 , R2 , D1 , D2 ) is strict-sense achievable for the general
multiterminal source coding problem. Then

R1 ≥ I(U1 ; Y1 |U2 , Q)




R2 ≥ I(U2 ; Y2 |U1 , Q)

R1 + R2 ≥ I(U1 , U2 ; Y1 , Y2 |Q)
(27)

D1 ≥ H(Y1 |U1 , U2 , Q) − β1 (R1 , R2 , D1 , D2 ) 



D2 ≥ H(Y2 |U1 , U2 , Q) − β2 (R1 , R2 , D1 , D2 )
for some joint distribution p(y1 , y2 )p(q)p(u1 |y1 , q)p(u2 |y2 , q) with |Ui | ≤ |Yi | and
|Q| ≤ 5.
Proof. Since (R1 , R2 , D1 , D2 ) is strict-sense achievable, there exists a block(n) (n)
(n)
(n)
length n, encoding functions ğ1 , ğ2 and a decoder (ψ̆1 , ψ̆2 ) satisfying (22)(23). Given these functions, the decoder can generate reproductions Y̆1n , Y̆2n
satisfying the average distortion constraints (23). From the reproduction Y̆in ,
we construct the reproduction Ŷin as follows:
˘

Ŷj (yi ) = P

2−di (yi ,Y̆i,j )

−d˘i (yi0 ,Y̆i,j )
yi0 ∈Yi 2

.

Now, using the logarithmic loss distortion measure, observe that Ŷin satisfies


n

 1 n
X
X
X
0
1
˘
˘
Ed(Yin , Ŷin ) =
E log 2di (Yi,j ,Y̆i,j ) +
E log 
2−di (yi ,Y̆i,j ) 
n j=1
n j=1
0
yi ∈Yi

n
X


1
(n) (n)
(n)
(n)
Ed˘i (Yi,j , Y̆i,j ) + βi ğ1 , ğ2 , ψ̆1 , ψ̆2
n j=1


(n) (n)
(n)
(n)
≤ Di + βi ğ1 , ğ2 , ψ̆1 , ψ̆2
=



:= D̃i .
Thus, (R1 , R2 , D̃1 , D̃2 ) is achievable for the multiterminal source coding problem
with the logarithmic loss distortion measure. Applying Theorem 6 and taking
the infimum over all coding schemes that achieve (R1 , R2 , D1 , D2 ) proves the
theorem.
This outer bound is interesting because the region is defined over the same
set of probability distributions that define the Berger-Tung inner bound. While
the βi ’s can be difficult to compute in general, we have shown that they can be
readily determined for many popular distortion measures. As an application, we
now give a quantitative approximation of the rate distortion region for binary
sources subject to Hamming distortion constraints. Before proceeding, we prove
the following lemma.

28

Lemma 3. Suppose (R1 , R2 , D̃1 , D̃2 ) is strict-sense achievable for the multiterminal source coding problem with binary sources and d˘i equal to the αi -scaled
Hamming distortion measure, for i = 1, 2. Then the Berger-Tung achievability
scheme can achieve a point (R1 , R2 , D1 , D2 ) satisfying
α

i
Di − D̃i ≤
− 1 Hi + log(1 + 2−αi )
2
for some Hi ∈ [0, 1], i = 1, 2.
Proof. By Theorem 9, (R1 , R2 , D̃1 , D̃2 ) satisfy (27) for some joint distribution
p(y1 , y2 )p(q)p(u1 |y1 , q)p(u2 |y2 , q). For this distribution, define the reproduction
functions
Y̆i (U1 , U2 , Q) = arg max p(yi |U1 , U2 , Q) for i = 1, 2.
yi

(28)

Then, observe that for i = 1, 2:
Ed˘i (Yi , Y̆i ) =



p(u1 , u2 , q) αi · min p(yi |u1 , u2 , q) + 0 · max p(yi |u1 , u2 , q)

X

yi

u1 ,u2 ,q

X

= αi

p(u1 , u2 , q) · min p(yi |u1 , u2 , q)
yi

u1 ,u2 ,q

≤

αi X
p(u1 , u2 , q) · H(Yi |U1 , U2 , Q = u1 , u2 , q)
2 u ,u ,q
1

=

yi

(29)

2

αi
H(Yi |U1 , U2 , Q).
2

Where (29) follows from the fact that 2p ≤ h2 (p) for 0 ≤ p ≤ 0.5. Thus,
Di = α2i H(Yi |U1 , U2 , Q) is achievable for rates (R1 , R2 ) using the Berger-Tung
achievability scheme. Combining this with the fact that D̃i ≥ H(Yi |U1 , U2 , Q)−
log(1 + 2−αi ), we see that
Di − D̃i ≤

αi
H(Yi |U1 , U2 , Q) − H(Yi |U1 , U2 , Q) + log(1 + 2−αi ).
2

Lemma 3 allows us to give a quantitative outer bound on the achievable rate
distortion region in terms of the Berger-Tung inner bound.
(1)

(1)

Corollary 1. Suppose (R1 , R2 , D̃1 , D̃2 ) is strict-sense achievable for the multiterminal source coding problem with binary sources and d˘i equal to the standard 1-scaled Hamming distortion measure, for i = 1, 2. Then the Berger-Tung
(1)
(1)
achievability scheme can achieve a point (R1 , R2 , D1 , D2 ), where
 
1
5
(1)
(1)
Di − D̃i ≤ log
< 0.161 for i = 1, 2.
2
4

29

Proof. For rates (R1 , R2 ), note that distortions (D̃1 , D̃2 ) are strict-sense achievable for the αi -scaled Hamming distortion measures if and only if distortions
(1)
(1)
(D̃1 , D̃2 ) = ( α11 D̃1 , α12 D̃2 ) are strict-sense achievable for the 1-scaled Hamming distortion measure. Likewise, the point (R1 , R2 , D1 , D2 ) is achieved by the
Berger-Tung coding scheme for the αi -scaled Hamming distortion measures if
and only if (R1 , R2 , α11 D1 , α12 D2 ) is achieved by the Berger-Tung coding scheme
for the 1-scaled Hamming distortion measure.
Thus, applying Lemma 3, we can use the Berger-Tung achievability scheme
(1)
(1)
to achieve a point (R1 , R2 , D1 , D2 ) satisfying

1 
(1)
(1)
Di − D̃i =
Di − D̃i
αi

1  αi
1
≤
− 1 Hi +
log(1 + 2−αi )
αi 2
αi


1
1
1
−
=
Hi +
log(1 + 2−αi )
(30)
2 αi
αi
for some Hi ∈ [0, 1]. We can optimize (30) over αi to find the minimum gap
for a given Hi . Maximizing over Hi ∈ [0, 1] then gives the worst-case gap.
Straightforward calculus yields the saddle-point:



1
1
1
−αi
−
Hi +
log(1 + 2
)
max inf
2 αi
αi
Hi ∈[0,1] αi >0



1
1
1
−αi
= inf max
−
Hi +
log(1 + 2
)
αi >0 Hi ∈[0,1]
2 αi
αi
 
5
1
< 0.161,
= log
2
4
which is achieved for αi = 2 and any H ∈ [0, 1].
Remark 3. We note briefly that this estimate can potentially be improved if
one knows more about the source distribution.

6

Concluding Remarks

One immediate direction for further work would be to extend our results to
more than two encoders. For the CEO problem, our results can be extended to
an arbitrary number of encoders. This extension is proved in Appendix B.
On the other hand, generalizing the results for the two-encoder source coding
problem with distortion constraints on Y1 and Y2 poses a significant challenge.
The obvious point of difficulty in the proof is extending the interpolation argument to higher dimensions so that it yields a distribution with the desired
properties. In fact, a “quick-fix” to the interpolation argument alone would not
be sufficient since this would imply that the Berger-Tung inner bound is tight for
more than two encoders. This is known to be false (even for the logarithmic loss
distortion measure) since the Berger-Tung achievability scheme is not optimal
for the lossless modulo-sum problem studied by Körner and Marton in [21].
30

Acknowledgement
The authors would like to thank Professors Suhas Diggavi and Aaron Wagner
for the helpful discussions on this topic.

A

Cardinality Bounds on Auxiliary Random
Variables

In order to obtain tight cardinality bounds on the auxiliary random variables
used throughout this paper, we refer to a recent result by Jana. In [17], the
author carefully applies the Caratheodory-Fenchel-Eggleston theorem in order
to obtain tight cardinality bounds on the auxiliary random variables in the
Berger-Tung inner bound. This result extends the results and techniques employed by Gu and Effros for the Wyner-Ahlswede-Körner problem [22], and by
Gu, Jana, and Effros for the Wyner-Ziv problem [23]. We now state Jana’s
result, appropriately modified for our purposes:
Consider an arbitrary joint distribution p(v, y1 , . . . , ym ) with random variables V, Y1 , . . . , Ym coming from alphabets V, Y1 , . . . , Ym respectively.
Let dl : V × V̂l → R, 1 ≤ l ≤ L be arbitrary distortion measures defined for
possibly different reproduction alphabets V̂l .
Definition 6. Define A? to be the set of (m + L)-vectors
(R1 , . . . , Rm , D1 , . . . , DL ) satisfying the following conditions:
1. auxiliary random variables U1 , . . . , Um exist such that
X
Ri ≥ I(YI ; UI |UI c ), for all I ⊆ {1, . . . , m}, and
i∈I

2. mappings ψl : U1 × · · · × Um → V̂l , 1 ≤ l ≤ L exist such that
Edl (V, ψl (U1 , . . . , Um )) ≤ Dl
for some joint distribution
p(v, y1 , . . . , ym )

m
Y

p(uj |yj ).

j=1

Lemma 4 (Lemma 2.2 from [17]). Every extreme point of A? corresponds to
some choice of auxiliary variables U1 , . . . , Um with alphabet sizes |Uj | ≤ |Yj |,
1 ≤ j ≤ m.
In order to obtain the cardinality bounds for the CEO problem, we simply
let L = 1, V = X, and V̂1 = X̂ . Defining


1
,
d1 (x, x̂) = log
x̂(x)
31

?

we see that RDCEO = conv (A? ), where conv (A? ) denotes the convex hull
?
of A? . Therefore, Lemma 4 implies that all extreme points of RDCEO are
achieved with a choice of auxiliary random variables U1 , . . . , Um with alphabet
sizes |Uj | ≤ |Yj |, 1 ≤ j ≤ m. By timesharing between extreme points, any point
?
in RDCEO can be achieved for these alphabet sizes.
Obtaining the cardinality bounds for the multiterminal source coding problem proceeds in a similar fashion. In particular, let L = m = 2, V = (Y1 , Y2 ),
and V̂j = Yˆj , j = 1, 2. Defining


1
for j = 1, 2,
dj ((y1 , y2 ), ŷj ) = log
ŷj (yj )
?

we see that RD = conv (A? ). In this case, Lemma 4 implies that all extreme
?
points of RD are achieved with a choice of auxiliary random variables U1 , U2
with alphabet sizes |Uj | ≤ |Yj |, 1 ≤ j ≤ 2. By timesharing between extreme
?
points, any point in RD can be achieved for these alphabet sizes.
In order to obtain cardinality bounds on the timesharing variable Q, we can
apply Caratheodory’s theorem (cf. [24]). In particular, if C ⊂ Rn is compact,
then any point in conv(C) is a convex combination of at most n + 1 points of
C. Taking C to be the closure of the set of extreme points of A? is sufficient
for our purposes (boundedness of C can be dealt with by a standard truncation
argument).

B

Extension of CEO Results to m Encoders

In this appendix, we prove the generalization of Theorem 3 to m encoders, which
essentially amounts to extending the argument in the proof of Theorem 3 to the
general case. We begin by stating the m-encoder generalizations of Theorems
1 and 2, the proofs of which are trivial extensions of the proofs given for the
two-encoder case and are therefore omitted.
Definition 7. Let RiCEO,m be the set of all (R1 , . . . , Rm , D) satisfying
X
Ri ≥ I(YI ; UI |UI c , Q) for all I ⊆ {1, . . . , m}
i∈I

D ≥ H(X|U1 , . . . , Um , Q).
Qm
for some joint distribution p(q)p(x) i=1 p(yi |x)p(ui |yi , q).
Theorem 10. All rate distortion vectors (R1 , . . . , Rm , D) ∈ RiCEO,m are
achievable.
Definition 8. Let RoCEO,m be the set of (R1 , . . . , Rm , D) satisfying
X
X
Ri ≥
I(Ui ; Yi |X, Q) + H(X|UI c , Q) − D for all I ⊆ {1, . . . , m}
i∈I

(31)

i∈I

D ≥ H(X|U1 , . . . , Um , Q).

(32)
32

for some joint distribution p(q)p(x)

Qm

i=1 p(yi |x)p(ui |yi , q).

Theorem 11. If (R1 , . . . , Rm , D)
(R1 , . . . , Rm , D) ∈ RoCEO,m .

is

strict-sense

achievable,

then

Given the definitions of RiCEO,m and RoCEO,m , the generalization of Theorem
3 to m encoders is an immediate consequence of the following lemma:
Lemma 5. RoCEO,m ⊆ RiCEO,m .
Proof. Suppose (R1 , . . . , Rm , D) ∈ RoCEO,m , then by definition there exists p(q)
and conditional distributions {p(ui |yi , q)}m
i=1 so that (31) and (32) are satisfied.
For the joint distribution corresponding to p(q) and conditional distributions
m
p{(ui |yi , q)}m
to be the polytope defined by the inequalities
i=1 , define PD ⊂ R
(31). Now, to show (R1 , . . . , Rm , D) ∈ RiCEO,m , it suffices to show that each
extreme point of PD is dominated by a point in RiCEO,m that achieves distortion
at most D.
To this end, define the set function f : 2[m] → R as follows:
f (I) := I(YI ; UI |UI c , Q) − (D − H(X|U1 , . . . , Um , Q))
X
=
I(Ui ; Yi |X, Q) + H(X|UI c , Q) − D.
i∈I

It can be verified that the function f and the function f + (I) = max{f (I), 0}
are supermodular functions (see Appendix C). By construction, PD is equal to
the set of (R1 , . . . , Rm ) which satisfy:
X
Ri ≥ f + (I).
i∈I

It follows by basic results in submodular optimization (see Appendix C)
that, for a linear ordering i1 ≺ i2 ≺ · · · ≺ im of {1, . . . , m}, an extreme point of
PD can be greedily computed as follows:
R̃ij = f + ({i1 , . . . , ij }) − f + ({i1 , . . . , ij−1 }) for j = 1, . . . , m.
Furthermore, all extreme points of PD can be enumerated by looking over all
linear orderings i1 ≺ i2 ≺ · · · ≺ im of {1, . . . , m}. Each ordering of {1, . . . , m} is
analyzed in the same manner, hence we assume (for notational simplicity) that
the ordering we consider is the natural ordering ij = j.
Let j be the first index for which R̃j > 0. Then, by construction,
R̃k = I(Uk ; Yk |Uk+1 , . . . , Um , Q) for all k > j.
Furthermore, we must have f ({1, . . . , j 0 }) ≤ 0 for all j 0 < j. Thus, R̃j can be
expressed as
R̃j =

j
X

I(Yi ; Ui |X, Q) + H(X|Uj+1 , . . . , Um , Q) − D

i=1

= I(Yj ; Uj |Uj+1 , . . . , Um , Q) + f ({1, . . . , j − 1})
= (1 − θ)I(Yj ; Uj |Uj+1 , . . . , Um , Q),
33

where θ ∈ [0, 1) is defined as:
−f ({1, . . . , j − 1})
I(Yj ; Uj |Uj+1 , . . . , Um , Q)
D − H(X|U1 , . . . , Um , Q) − I(U1 , . . . , Uj−1 ; Y1 , . . . , Yj−1 |Uj , . . . , Um , Q)
=
.
I(Yj ; Uj |Uj+1 , . . . , Um , Q)

θ=

By the results of Theorem 10, the rates (R̃1 , . . . , R̃m ) permit the following
coding scheme: For a fraction (1 − θ) of the time, a codebook can be used
n
that allows the decoder to recover Ujn , . . . , Um
with high probability. The other
fraction θ of the time, a codebook can be used that allows the decoder to recover
n
n
Uj+1
, . . . , Um
with high probability. As n → ∞, this coding scheme can achieve
distortion
D̃ = (1 − θ)H(X|Uj , . . . , Um , Q) + θH(X|Uj+1 , . . . , Um , Q)
= H(X|Uj , . . . , Um , Q) + θI(X; Uj |Uj+1 , . . . , Um , Q)
= H(X|Uj , . . . , Um , Q) +

I(X; Uj |Uj+1 , . . . , Um , Q)
×
I(Yj ; Uj |Uj+1 , . . . , Um , Q)

[D − H(X|U1 , . . . , Um , Q) − I(U1 , . . . , Uj−1 ; Y1 , . . . , Yj−1 |Uj , . . . , Um , Q)]
≤ H(X|Uj , . . . , Um , Q) + D − H(X|U1 , . . . , Um , Q)
− I(U1 , . . . , Uj−1 ; Y1 , . . . , Yj−1 |Uj , . . . , Um , Q)

(33)

= D + I(X; U1 , . . . Uj−1 |Uj , . . . , Um , Q)
− I(U1 , . . . , Uj−1 ; Y1 , . . . , Yj−1 |Uj , . . . , Um , Q)
= D − I(U1 , . . . , Uj−1 ; Y1 , . . . , Yj−1 |X, Uj , . . . , Um , Q)
≤ D.

(34)

In the preceding string of inequalities (33) follows since Uj is conditionally
independent of everything else given (Yj , Q), and (34) follows from the nonnegativity of mutual information.
Therefore, for every extreme point (R̃1 , . . . , R̃m ) of PD , the point
(R̃1 , . . . , R̃m , D) lies in RiCEO,m . This proves the lemma.
Finally, we remark that the results of Appendix A imply that it suffices to
consider auxiliary random variables U1 , . . . , Um with alphabet sizes |Uj | ≤ |Yj |,
1 ≤ j ≤ m. The timesharing variable Q requires an alphabet size bounded by
|Q| ≤ m + 2.

C

Supermodular Functions

In this appendix, we review some basic results in submodular optimization that
were used in Appendix B to prove Lemma 5. We tailor our statements toward
supermodularity, since this is the property we require in Appendix B.
We begin by defining a supermodular function.

34

Definition 9. Let E = {1, . . . , n} be a finite set. A function s : 2E → R is
supermodular if for all S, T ⊆ E
s(S) + s(T ) ≤ s(S ∩ T ) + s(S ∪ T ).

(35)

One of the fundamental results in submodular optimization is that a greedy
algorithm minimizes a linear function over a supermodular polyhedron. By
varying the linear function to be minimized, all extreme points of the supermodular polyhedron can be enumerated. In particular, define the supermodular
polyhedron P(s) ⊂ Rn to be the set of x ∈ Rn satisfying
X
xi ≥ s(T ) for all T ⊆ E.
i∈T

The following theorem provides an algorithm that enumerates the extreme
points of P(s).
Theorem 12 (See [25–27]). For a linear ordering e1 ≺ e2 ≺ · · · ≺ en of the
elements in E, Algorithm C.1 returns an extreme point v of P(s). Moreover,
all extreme points of P(s) can be enumerated by considering all linear orderings
of the elements of E.
Algorithm C.1: Greedy(s, E, ≺)
comment: Returns extreme point v of P(s) corresponding to the ordering ≺.
for i = 1, . . . n
Set vi = s({e1 , e2 , . . . , ei }) − s({e1 , e2 , . . . , ei−1 })
return (v)

Proof. See [25–27].
Theorem 12 is the key tool we employ to establish Lemma 5. In order to
apply it, we require the following lemma.
Lemma Q 6.
For
any
joint
distribution
of
the
form
m
p(q)p(x) i=1 p(yi |x)p(ui |yi , q) and fixed D ∈ R, define the set function
f : 2[m] → R as:
f (I) := I(YI ; UI |UI c , Q) − (D − H(X|U1 , . . . , Um , Q))
X
=
I(Ui ; Yi |X, Q) + H(X|UI c , Q) − D,

(36)

i∈I

and the corresponding non-negative set function f + : 2[m] → R as f + =
max{f, 0}. The functions f and f + are supermodular.

35

Proof. In order to verify that f is supermodular, it suffices to check that the
function f 0 (I) = I(YI ; UI |UI c , Q) is supermodular since the latter two terms
in (36) are constant. To this end, consider sets T, S ⊆ {1, . . . , m} and observe
that:
f 0 (S) + f 0 (T ) = I(YS ; US |US c , Q) + I(YT ; UT |UT c , Q)
= H(US |US c , Q) − H(US |YS , Q) + H(UT |UT c , Q) − H(UT |YT , Q)
= H(US |US c , Q) + H(UT |UT c , Q)
− H(US∪T |YS∪T , Q) − H(US∩T |YS∩T , Q)

(37)

= H(US\T |US c , Q) + H(US∩T |U(S∩T )c , Q) + H(UT |UT c , Q)
− H(US∪T |YS∪T , Q) − H(US∩T |YS∩T , Q)
= H(US\T |U , Q) + H(UT |U
Sc

Tc

(38)

, Q) − H(US∪T |YS∪T , Q)

+ I(US∩T ; YS∩T |U(S∩T )c , Q)
≤ H(US\T |U(S∪T )c , Q) + H(UT |UT c , Q) − H(US∪T |YS∪T , Q)
+ I(US∩T ; YS∩T |U(S∩T )c , Q)
= I(US∪T ; YS∪T |U

(S∪T )c

(39)

, Q) + I(US∩T ; YS∩T |U

(S∩T )c

, Q)

= f 0 (S ∩ T ) + f 0 (S ∪ T ).
The labeled steps above can be justified as follows:
• (37) follows since Ui is conditionally independent of everything else given
(Yi , Q).
• (38) is simply the chain rule.
• (39) follows since conditioning reduces entropy.
Next, we show that f + = max{f, 0} is supermodular. Observe first that
f is monotone increasing, i.e., if S ⊂ T , then f (S) ≤ f (T ). Thus, fixing
S, T ⊆ {1, . . . , m}, we can assume without loss of generality that
f (S ∩ T ) ≤ f (S) ≤ f (T ) ≤ f (S ∪ T ).
If f (S ∩ T ) ≥ 0, then (35) is satisfied for s = f + by the supermodularity of
f . On the other hand, if f (S ∪ T ) ≤ 0, then (35) is a tautology for s = f + .
Therefore, it suffices to check the following three cases:
• Case 1: f (S ∩ T ) ≤ 0 ≤ f (S) ≤ f (T ) ≤ f (S ∪ T ). In this case, the
supermodularity of f and the fact that f + ≥ f imply:
f + (S ∪ T ) + f + (S ∩ T ) ≥ f (S ∪ T ) + f (S ∩ T )
≥ f (S) + f (T ) = f + (S) + f + (T ).
• Case 2: f (S ∩ T ) ≤ f (S) ≤ 0 ≤ f (T ) ≤ f (S ∪ T ). Since f is monotone
increasing, we have:
f + (S ∪ T ) + f + (S ∩ T ) = f (S ∪ T ) + 0 ≥ f (T ) + 0 = f + (S) + f + (T ).
36

• Case 3: f (S ∩ T ) ≤ f (S) ≤ f (T ) ≤ 0 ≤ f (S ∪ T ). By definition of f + :
f + (S ∪ T ) + f + (S ∩ T ) = f (S ∪ T ) + 0 ≥ 0 + 0 = f + (S) + f + (T ).
Hence, f + = max{f, 0} is supermodular.

D

Amplifying a Pointwise Convexity Constraint

Lemma 7. Let r1 , r2 ∈ R be given, and suppose f1 : K → R and f2 : K → R
are continuous functions defined on a compact domain K ⊂ Rn . If there exists
a function h : [0, 1] → K satisfying
t (f1 ◦ h) (t) + (1 − t) (f2 ◦ h) (t) ≤ tr1 + (1 − t)r2 for all t ∈ [0, 1],

(40)

then there exists x∗1 , x∗2 ∈ K and t∗ ∈ [0, 1] for which
t∗ f1 (x∗1 ) + (1 − t∗ )f1 (x∗2 ) ≤ r1
t∗ f2 (x∗1 ) + (1 − t∗ )f2 (x∗2 ) ≤ r2 .
Before we prove the lemma, we make a few remarks. At first glance, this
lemma appears somewhat bizarre. Indeed, the set K need only be compact
(e.g., connectedness is not required) and h can be an arbitrarily complicated
function, as long as it satisfies (40). The strange nature of the lemma is echoed
by the proof in that we merely prove the existence of the desired x∗1 , x∗2 and
t∗ ; no further information is obtained. Stripped to its core, the existence of the
desired x∗1 , x∗2 and t∗ essentially follows from the pigeonhole principle, which
manifests itself in the sequential compactness of K.
Despite its strange nature, Lemma 7 is crucial in establishing the converse
result for the multiterminal source coding problem under logarithmic loss. In
this application, K is taken to be a closed subset of a finite-dimensional probability simplex and f1 , f2 are conditional entropies evaluated for probability
distributions in K.
Finally, we remark that the Lemma 7 can be generalized to a certain extent.
For example, the function h need only be defined on a dense subset of [0, 1] and
the set K can be a more general sequentially compact space.
Proof of Lemma 7. Since f1 , f2 are continuous4 and K is compact, there exists
M < ∞ such that f1 and f2 are bounded from above and below by M and −M ,
respectively. Fix  > 0, and partition the interval [0, 1] as 0 = t1 < t2 < · · · <

. For convenience define xtj := h(tj ) when tj
tm = 1, such that |tj+1 − tj | < M
is in the partition.
4 Although not required for our purposes, we can assume f and f are defined and contin1
2
uous over all of Rn . This is a consequence of the Tietze extension theorem.

37

Now, for i = 1, 2 define piecewise-linear functions g1 (t), g2 (t) on [0,1] by:

fi (xtj )
if tj is in the partition
gi (t) =
(41)
θfi (xtj ) + (1 − θ)fi (xtj+1 ) if t is in the interval (tj , tj+1 ),
where θ ∈ (0, 1) is chosen so that t = θtj + (1 − θ)tj+1 when t is in the interval
(tj , tj+1 ).
With g1 (t) and g2 (t) defined in this manner, suppose t = θtj + (1 − θ)tj+1
for some j and θ. Then some straightforward algebra yields:

tg1 (t) + (1 − t)g2 (t) = (θtj + (1 − θ)tj+1 ) θf1 (xtj ) + (1 − θ)f1 (xtj+1 )

+ (1 − θtj − (1 − θ)tj+1 ) θf2 (xtj ) + (1 − θ)f2 (xtj+1 )


= θ2 tj f1 (xtj ) + (1 − tj )f2 (xtj )


+ (1 − θ)2 tj+1 f1 (xtj+1 ) + (1 − tj+1 )f2 (xtj+1 )

+ θ(1 − θ) (1 − tj )f2 (xtj+1 ) + (1 − tj+1 )f2 (xtj )

+tj+1 f1 (xtj ) + tj f1 (xtj+1 )


≤ θ2 tj f1 (xtj ) + (1 − tj )f2 (xtj )


+ (1 − θ)2 tj+1 f1 (xtj+1 ) + (1 − tj+1 )f2 (xtj+1 )

+ θ(1 − θ) (1 − tj+1 )f2 (xtj+1 ) + (1 − tj )f2 (xtj )

+tj f1 (xtj ) + tj+1 f1 (xtj+1 ) + 
≤ θ2 [tj r1 + (1 − tj )r2 ]
+ (1 − θ)2 [tj+1 r1 + (1 − tj+1 )r2 ]
+ θ(1 − θ) [(1 − tj+1 )r2 + (1 − tj )r2
+tj r1 + tj+1 r1 ] + 
= (θtj + (1 − θ)tj+1 )r1 + (1 − θtj − (1 − θ)tj+1 )r2 + 
= tr1 + (1 − t)r2 + ,

(42)

where the first inequality follows since |tj+1 − tj | is small, and the second
inequality follows from the the fact that (40) holds for each tj in the partition.
Notably, this implies that it is impossible to have
g1 (t) > r1 +  and g2 (t) > r2 + 
hold simultaneously for any t ∈ [0, 1], else we would obtain a contradiction to
(42). Also, since we included the endpoints t1 = 0 and tm = 1 in the partition,
we have the following two inequalities:
g1 (1) ≤ r1 , and g2 (0) ≤ r2 .
Combining these observations with the fact that g1 (t) and g2 (t) are continuous, there must exist some t∗ ∈ [0, 1] for which
g1 (t∗ ) ≤ r1 + , and g2 (t∗ ) ≤ r2 + 
38

(g1 (1), g2 (1))
r2 + 

(g1 (0), g2 (0))

r1 + 
Figure 5: A parametric plot of the function ϕ : t 7→ (g1 (t), g2 (t)). Since ϕ(t) is
continuous, starts with g2 (0) ≤ r2 + , ends with g1 (1) ≤ r1 + , and doesn’t
intersect the shaded area, ϕ(t) must pass through the lower-left region.

simultaneously. An illustration of this is given in Figure 5, which is a mere
variation on the classical intermediate value theorem.
(n)
(n)
Applying this result, we can find a sequence {x1 , x2 , t(n) }∞
n=1 satisfying
1
n
1
(n)
(n)
t(n) f2 (x1 ) + (1 − t(n) )f2 (x2 ) ≤ r2 +
n
(n)

(n)

t(n) f1 (x1 ) + (1 − t(n) )f1 (x2 ) ≤ r1 +

for each n ≥ 1. Since K × K × [0, 1] is sequentially compact, there exists a
(nj )
(n )
convergent subsequence {nj }∞
, x2 j , t(nj ) ) → (x∗1 , x∗2 , t∗ ) ∈
j=1 such that (x1
K × K × [0, 1]. The continuity of f1 and f2 then apply to yield the desired
result.

E

Strengthening the Converse of Theorem 6

In this appendix, we prove a stronger version of the converse of Theorem 6.
To be precise, let Ŷ1∗n and Ŷ2∗n denote the set of probability measures on Y1n
and Y2n , respectively. Let d∗1 , d∗2 be the (extended)-log loss distortion measures

39

defined as follows:


1
1
log
n
ŷ n (y n )
 1 1 
1
1
d∗2 (y2n , ŷ2n ) = log
,
n
ŷ2n (y2n )
d∗1 (y1n , ŷ1n ) =

where ŷ1n (y1n ) is the probability assigned to outcome y1n ∈ Y1n by the probability
measure ŷ1n ∈ Ŷ1∗n . Similarly for ŷ2n (y2n ). Note that this extends the standard
definition of logarithmic loss to sequence reproductions.
Definition 10. We say that a tuple (R1 , R2 , D1 , D2 ) is sequence-achievable if,
for any  > 0, there exist encoding functions
f1 : Y1n → {1, . . . , 2nR1 }
f2 : Y2n → {1, . . . , 2nR2 },
and decoding functions
φ1 : {1, . . . , 2nR1 } × {1, . . . , 2nR2 } → Ŷ1∗n
φ2 : {1, . . . , 2nR1 } × {1, . . . , 2nR2 } → Ŷ2∗n ,
which satisfy
E d∗1 (Y1n , Ŷ1n ) ≤ D1 + 
E d∗2 (Y2n , Ŷ2n ) ≤ D2 + ,
where
Ŷ1n = φ1 (f1 (Y1n ), f2 (Y2n ))
Ŷ2n = φ2 (f1 (Y1n ), f2 (Y2n )).
Theorem
13. If
(R1 , R2 , D1 , D2 )
?
(R1 , R2 , D1 , D2 ) ∈ RDi = RD .

is

sequence-achievable,

then

Proof. The theorem is an immediate consequence of Theorem 6 and Lemmas 8
and 9, which are given below.
Remark 4. We refer to Theorem 13 as the “strengthened converse” of Theorem
6. Indeed, it states that enlarging the set of possible reproduction sequences to
include non-product distributions cannot attain better performance than when
the decoder is restricted to choosing a reproduction sequence from the set of
product distributions.
Lemma 8. If (R1 , R2 , D̃1 , D2 ) is sequence-achievable, then there exists a joint
distribution
p(y1 , y2 , u1 , u2 , q) = p(q)p(y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)
40

and a D1 ≤ D̃1 which satisfies
D1 ≥ H(Y1 |U1 , U2 , Q)
D2 ≥ D1 + H(Y2 |U1 , U2 , Q) − H(Y1 |U1 , U2 , Q),
and
R1 ≥ H(Y1 |U2 , Q) − D1
R2 ≥ I(Y2 ; U2 |Y1 , Q) + H(Y1 |U1 , Q) − D1
R1 + R2 ≥ I(Y2 ; U2 |Y1 , Q) + H(Y1 ) − D1 .
Proof. For convenience, let F1 = f1 (Y1n ) and F2 = f2 (Y2n ), where f1 , f2 are the
encoding functions corresponding to a scheme which achieves (R1 , R2 , D̃1 , D2 )
(in the sequence-reproduction sense). Define D1 = n1 H(Y1n |F1 , F2 ), so that:
nD1 = H(Y1n |F1 , F2 ).

(43)

Since nD̃1 ≥ H(Y1n |F1 , F2 ) by the strengthened version5 of Lemma 1, we have
D1 ≤ D̃1 as desired. By definition of D1 , we immediately obtain the following
inequality:
nD1 =

n
X

n
H(Y1,i |F1 , F2 , Y1,i+1
)≥

i=1

n
X

n
H(Y1,i |F1 , F2 , Y2i−1 , Y1,i+1
).

(44)

i=1

Next, recall the Csiszár sum identity:
n
X

n
I(Y1,i+1
; Y2,i |Y2i−1 , F1 , F2 ) =

i=1

n
X

n
I(Y2i−1 ; Y1,i |Y1,i+1
, F1 , F2 ).

i=1

This, together with (43), implies the following inequality:
nD2 ≥ nD1 +

n
X

n
n
H(Y2,i |F1 , F2 , Y2i−1 , Y1,i+1
) − H(Y1,i |F1 , F2 , Y2i−1 , Y1,i+1
),

i=1

(45)
5 See the comment in Section 3.3.

41

which we can verifiy as follows:
nD2 ≥ H(Y2n |F1 , F2 ) =

n
X

H(Y2,i |F1 , F2 , Y2i−1 )

i=1

=

n
X

n
n
H(Y2,i |F1 , F2 , Y2i−1 , Y1,i+1
) + I(Y1,i+1
; Y2,i |F1 , F2 , Y2i−1 )

i=1

=

n
X

n
n
H(Y2,i |F1 , F2 , Y2i−1 , Y1,i+1
) + I(Y2i−1 ; Y1,i |Y1,i+1
, F1 , F2 )

i=1

= H(Y1n |F1 , F2 ) +

n
X

n
n
H(Y2,i |F1 , F2 , Y2i−1 , Y1,i+1
) − H(Y1,i |F1 , F2 , Y2i−1 , Y1,i+1
)

i=1

= nD1 +

n
X

n
n
H(Y2,i |F1 , F2 , Y2i−1 , Y1,i+1
) − H(Y1,i |F1 , F2 , Y2i−1 , Y1,i+1
).

i=1

Next, observe that we can lower bound R1 as follows:
nR1 ≥ H(F1 ) ≥ I(Y1n ; F1 |F2 )
n
X
=
H(Y1,i |F2 , Y1i−1 ) − H(Y1n |F1 , F2 )
i=1

≥
=
≥

n
X
i=1
n
X
i=1
n
X

H(Y1,i |F2 , Y1i−1 , Y2i−1 ) − nD1

(46)

H(Y1,i |F2 , Y2i−1 ) − nD1

(47)

n
H(Y1,i |F2 , Y2i−1 , Y1,i+1
) − nD1 .

(48)

i=1

In the above string of inequalities, (46) follows from (43) and the fact that
conditioning reduces entropy. Equality (47) follows since Y1,i ↔ F2 , Y2i−1 ↔
Y1i−1 form a Markov chain (in that order).

42

Next, we can obtain a lower bound on R2 :
nR2 ≥ H(F2 ) ≥ H(F2 |F1 ) = H(F2 |F1 , Y1n ) + I(Y1n ; F2 |F1 )
≥ I(Y2n ; F2 |F1 , Y1n ) + I(Y1n ; F2 |F1 )
= I(Y2n ; F2 |Y1n ) + I(Y1n ; F2 |F1 )
n
X
n
=
I(Y2,i ; F2 |Y1n , Y2i−1 ) + H(Y1,i |F1 , Y1,i+1
) − nD1
≥
=

i=1
n
X
i=1
n
X

(49)
(50)

n
I(Y2,i ; F2 |Y1n , Y2i−1 ) + H(Y1,i |F1 , Y2i−1 , Y1,i+1
) − nD1

n
n
I(Y2,i ; F2 , Y1i−1 , Y2i−1 |Y1,i , Y2i−1 , Y1,i+1
) + H(Y1,i |F1 , Y2i−1 , Y1,i+1
) − nD1

i=1

(51)
≥

n
X

n
n
I(Y2,i ; F2 , Y2i−1 |Y1,i , Y2i−1 , Y1,i+1
) + H(Y1,i |F1 , Y2i−1 , Y1,i+1
) − nD1 .

i=1

(52)
In the above string of inequalities, (50) follows from (43) and the chain rule. (51)
follows from the i.i.d. property of the sources, and (52) follows by monotonicity
of mutual information.
A lower bound on the sum-rate R1 + R2 can be obtained as follows:
n(R1 + R2 ) ≥ H(F1 ) + H(F2 ) ≥ H(F2 ) + H(F1 |F2 )
≥ I(F2 ; Y1n , Y2n ) + I(F1 ; Y1n |F2 )
= I(F2 ; Y1n ) + I(F2 ; Y2n |Y1n ) + I(F1 ; Y1n |F2 )
= I(F2 ; Y2n |Y1n ) + I(F1 , F2 ; Y1n )
n
X
n
≥
I(Y2,i ; F2 , Y2i−1 |Y1,i , Y2i−1 , Y1,i+1
) + H(Y1,i ) − nD1 .

(53)

i=1

Where (53) follows in a manner similar to (49)-(52) in the lower bound on R2 .
n
Now, define U1,i , F1 , U2,i , (F2 , Y2i−1 ), and Qi , (Y2i−1 , Y1,i+1
). Then we
can summarize our results so far as follows. Inequalities (44) and (45) become
n

D1 ≥

1X
H(Y1,i |U1,i , U2,i , Qi )
n i=1
n

1X
H(Y2,i |U1,i , U2,i , Qi ) − H(Y1,i |U1,i , U2,i , Qi ),
D2 ≥ D1 +
n i=1

43

and inequalities (48), (52), and (53) can be written as:
n

R1 ≥

1X
H(Y1,i |U2,i , Qi ) − D1
n i=1
n

1X
I(Y2,i ; U2,i |Y1,i , Qi ) + H(Y1,i |U1,i , Qi ) − D1
R2 ≥
n i=1
n

R1 + R2 ≥

1X
I(Y2,i ; U2,i |Y1,i , Qi ) + H(Y1,i ) − D1 .
n i=1

Next, we note that U1,i ↔ Y1,i ↔ Y2,i ↔ U2,i form a Markov chain (in that
order) conditioned on Qi . Moreover, Qi is independent of Y1,i , Y2,i . Hence, a
standard timesharing argument proves the lemma.
Lemma 9. Fix (R1 , R2 , D1 , D2 ). If there exists a joint distribution of the form
p(y1 , y2 , u1 , u2 , q) = p(q)p(y1 , y2 )p(u1 |y1 , q)p(u2 |y2 , q)
which satisfies
D1 ≥ H(Y1 |U1 , U2 , Q)

(54)

D2 ≥ D1 + H(Y2 |U1 , U2 , Q) − H(Y1 |U1 , U2 , Q),

(55)

and
R1 ≥ H(Y1 |U2 , Q) − D1

(56)

R2 ≥ I(Y2 ; U2 |Y1 , Q) + H(Y1 |U1 , Q) − D1

(57)

R1 + R2 ≥ I(Y2 ; U2 |Y1 , Q) + H(Y1 ) − D1 ,

(58)

then (R1 , R2 , D1 , D2 ) ∈ RDi .
Proof. Let P denote the polytope of rate pairs which satisfy the inequalities (56)-(58). It suffices to show that if (r1 , r2 ) is a vertex of P, then
(r1 , r2 , D1 , D2 ) ∈ RDi . For convenience, let [x]+ = max{x, 0}. There are
only two extreme points of P:

+
(1)
r1 = H(Y1 |U2 , Q) − D1
(1)

(1)

r2 = I(Y2 ; U2 |Y1 , Q) + H(Y1 ) − D1 − r1 ,
and
(2)

(2)

r1 = I(Y2 ; U2 |Y1 , Q) + H(Y1 ) − D1 − r2 ,

+
(2)
r2 = I(Y2 ; U2 |Y1 , Q) + H(Y1 |U1 , Q) − D1 .
(1)

(1)

We first analyze the extreme point (r1 , r2 ):
44

(1)

(1)

• Case 1.1: r1 = 0. In this case, we have r2 = I(Y2 ; U2 |Y1 , Q)+H(Y1 )−
D1 . This can be expressed as:
(1)

r2 = (1 − θ)I(Y2 ; U2 |Q),
where
θ=

D1 − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y2 ; U2 |Q)
.
I(Y2 ; U2 |Q)

(1)

Since r1 = 0, we must have D1 ≥ H(Y1 |U2 , Q). This implies that
θ≥

H(Y1 |U2 , Q) − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y2 ; U2 |Q)
= 0.
I(Y2 ; U2 |Q)

Also, we can assume without loss of generality that D1 ≤ H(Y1 ), hence
θ ∈ [0, 1]. Applying the Berger-Tung achievability scheme, we can achieve
the following distortions:
D1θ = θH(Y1 ) + (1 − θ)H(Y1 |U2 , Q)
= H(Y1 |U2 , Q) + θI(Y1 ; U2 |Q)
≤ H(Y1 |U2 , Q) + D1 − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y2 ; U2 |Q) (59)
= D1 − I(Y2 ; U2 |Y1 , Q) − I(Y1 ; U2 |Q) + I(Y2 ; U2 |Q)
= D1 ,
where (59) follows since I(Y1 ; U2 |Q) ≤ I(Y2 ; U2 |Q) by the data processing
inequality.
D2θ = θH(Y2 ) + (1 − θ)H(Y2 |U2 , Q)
= H(Y2 |U2 , Q) + θI(Y2 ; U2 |Q)
= H(Y2 |U2 , Q) + D1 − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y2 ; U2 |Q)
= H(Y2 ) + D1 − I(Y2 ; U2 |Y1 , Q) − H(Y1 )
= H(Y2 |Y1 , U2 , Q) + D1 − H(Y1 |Y2 )
= H(Y2 |Y1 , U1 , U2 , Q) + D1 − H(Y1 |Y2 )

(60)

≤ H(Y2 |Y1 , U1 , U2 , Q) + D1 − H(Y1 |Y2 , U1 , U2 , Q)
= H(Y2 |U1 , U2 , Q) + D1 − H(Y1 |U1 , U2 , Q)
≤ D2 ,

(61)

where (60) follows since U1 ↔ (Y1 , U2 , Q) ↔ Y2 , and (61) follows from
(55).
•

(1)

(1)

Case 1.2: r1 ≥ 0. In this case, we have r2 = I(Y2 ; U2 |Y1 , Q) +
(1)
I(Y1 ; U2 |Q) = I(Y2 ; U2 |Q). Also, we can write r1 as:
(1)

r1 = (1 − θ)I(Y1 ; U1 |U2 , Q),
45

where
θ=

D1 − H(Y1 |U2 , Q) + I(Y1 ; U1 |U2 , Q)
.
I(Y1 ; U1 |U2 , Q)

(1)

Since r1 ≥ 0, we must have D1 ≤ H(Y1 |U2 , Q). This implies that
θ≤

H(Y1 |U2 , Q) − H(Y1 |U2 , Q) + I(Y1 ; U1 |U2 , Q)
= 1.
I(Y1 ; U1 |U2 , Q)

Also, (54) implies that D1 ≥ H(Y1 |U1 , U2 , Q), hence θ ∈ [0, 1]. Applying the Berger-Tung achievability scheme, we can achieve the following
distortions:
D1θ = θH(Y1 |U2 , Q) + (1 − θ)H(Y1 |U1 , U2 , Q)
= H(Y1 |U1 , U2 , Q) + θI(Y1 ; U1 |U2 , Q)
= H(Y1 |U1 , U2 , Q) + D1 − H(Y1 |U2 , Q) + I(Y1 ; U1 |U2 , Q)
= D1 ,
and
D2θ = θH(Y2 |U2 , Q) + (1 − θ)H(Y2 |U1 , U2 , Q)
= H(Y2 |U1 , U2 , Q) + θI(Y2 ; U1 |U2 , Q)
≤ H(Y2 |U1 , U2 , Q) + D1 − H(Y1 |U2 , Q) + I(Y1 ; U1 |U2 , Q)

(62)

= H(Y2 |U1 , U2 , Q) + D1 − H(Y1 |U1 , U2 , Q)
≤ D2 ,

(63)

where (62) follows since I(Y2 ; U1 |U2 , Q) ≤ I(Y1 ; U1 |U2 , Q) by the data
processing inequality, and (63) follows from (55).
(2)

(2)

In a similar manner, we now analyze the second extreme point (r1 , r2 ):
(2)

(2)

• Case 2.1: r2 = 0. In this case, we have r1 = I(Y2 ; U2 |Y1 , Q)+H(Y1 )−
D1 . This can be expressed as:
(2)

r1 = (1 − θ)I(Y1 ; U1 |Q),
where
θ=

D1 − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y1 ; U1 |Q)
.
I(Y1 ; U1 |Q)

(2)

Since r2 = 0, we must have D1 ≥ H(Y1 |U1 , Q) + I(Y2 ; U2 |Y1 , Q). This
implies that
θ≥

H(Y1 |U1 , Q) + I(Y2 ; U2 |Y1 , Q) − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y1 ; U1 |Q)
= 0.
I(Y1 ; U1 |Q)
46

Also, we can assume without loss of generality that D1 ≤ H(Y1 ), hence
θ≤

H(Y1 ) − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y1 ; U1 |Q)
≤ 1,
I(Y1 ; U1 |Q)

and therefore θ ∈ [0, 1]. Applying the Berger-Tung achievability scheme,
we can achieve the following distortions:
D1θ = θH(Y1 ) + (1 − θ)H(Y1 |U1 , Q)
= H(Y1 |U1 , Q) + θI(Y1 ; U1 |Q)
= H(Y1 |U1 , Q) + D1 − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y1 ; U1 |Q)
= D1 − I(Y2 ; U2 |Y1 , Q)
≤ D1 ,
and
D2θ = θH(Y2 ) + (1 − θ)H(Y2 |U1 , Q)
= H(Y2 |U1 , Q) + θI(Y2 ; U1 |Q)
≤ H(Y2 |U1 , Q) + D1 − I(Y2 ; U2 |Y1 , Q) − H(Y1 ) + I(Y1 ; U1 |Q) (64)
= H(Y2 |Y1 , U2 , Q) + D1 − H(Y1 |Y2 , U1 , Q)
= H(Y2 |Y1 , U1 , U2 , Q) + D1 − H(Y1 |Y2 , U1 , U2 , Q)

(65)

= H(Y2 |U1 , U2 , Q) + D1 − H(Y1 |U1 , U2 , Q)
≤ D2 ,

(66)

where (64) follows since I(Y2 ; U1 |Q) ≤ I(Y1 ; U1 |Q) by the data processing inequality, (65) follows since U1 ↔ (Y1 , U2 , Q) ↔ Y2 and U2 ↔
(Y2 , U1 , Q) ↔ Y1 , and (66) follows from (55).
(2)

(2)

• Case 2.2: r2 ≥ 0. In this case, we have r1
(2)
can write r2 as:

= I(Y1 ; U1 |Q). Also, we

(2)

r2 = (1 − θ)I(Y2 ; U2 |U1 , Q),
where
θ=

D1 − H(Y1 |U1 , Q) − I(Y2 ; U2 |Y1 , Q) + I(Y2 ; U2 |U1 , Q)
.
I(Y2 ; U2 |U1 , Q)

(2)

Since r2 ≥ 0, we must have D1 ≤ H(Y1 |U1 , Q) + I(Y2 ; U2 |Y1 , Q). This
implies that θ ≤ 1. Also, (54) implies that D1 ≥ H(Y1 |U1 , U2 , Q), yielding
θ≥

H(Y1 |U1 , U2 , Q) − H(Y1 |U1 , Q) − I(Y2 ; U2 |Y1 , Q) + I(Y2 ; U2 |U1 , Q)
= 0.
I(Y2 ; U2 |U1 , Q)

47

Therefore, θ ∈ [0, 1]. Applying the Berger-Tung achievability scheme, we
can achieve the following distortions:
D1θ = θH(Y1 |U1 , Q) + (1 − θ)H(Y1 |U1 , U2 , Q)
= H(Y1 |U1 , U2 , Q) + θI(Y1 ; U2 |U1 , Q)
≤ H(Y1 |U1 , U2 , Q) + D1 − H(Y1 |U1 , Q) − I(Y2 ; U2 |Y1 , Q) + I(Y2 ; U2 |U1 , Q)
(67)
= D1 ,
where (67) follows since I(Y1 ; U2 |U1 , Q) ≤ I(Y2 ; U2 |U1 , Q) by the data
processing inequality.
D2θ = θH(Y2 |U1 , Q) + (1 − θ)H(Y2 |U1 , U2 , Q)
= H(Y2 |U1 , U2 , Q) + θI(Y2 ; U2 |U1 , Q)
= H(Y2 |U1 , U2 , Q) + D1 − H(Y1 |U1 , Q) − I(Y2 ; U2 |Y1 , Q) + I(Y2 ; U2 |U1 , Q)
= H(Y2 |U1 , U2 , Q) + D1 − H(Y1 |U1 , U2 , Q)
≤ D2 ,

(68)

where (68) follows from (55).
Thus, this proves that the Berger-Tung compression scheme can achieve any
rate distortion tuple (r1 , r2 , D1 , D2 ) for (r1 , r2 ) ∈ P. Since RDi is, by definition,
the set of rate distortion tuples attainable by the Berger-Tung achievability
scheme, we must have that (R1 , R2 , D1 , D2 ) ∈ RDi . This proves the lemma.

F

A Lemma for the Daily Double

For a given joint distribution p(y1 , y2 ) on the finite alphabet Y1 × Y2 , let
P(R1 , R2 ) denote the set of joint pmf’s of the form
p(q, y1 , y2 , u1 , u2 ) = p(q)p(y1 , y2 )p(u1 |y1 , q)p(u1 |y1 , q)
which satisfy
R1 ≥ I(Y1 ; U1 |U2 , Q)
R2 ≥ I(Y2 ; U2 |U1 , Q)
R1 + R2 ≥ I(Y1 , Y2 ; U1 , U2 |Q)
for given finite alphabets U1 , U2 , Q.
Lemma 10. For R1 , R2 satisfying R1 ≤ H(Y1 ), R2 ≤ H(Y2 ), and R1 + R2 ≤
H(Y1 , Y2 ), the infimum
inf
p∈P(R1 ,R2 )

{H(Y1 |U1 , U2 , Q) + H(Y2 |U1 , U2 , Q)}

is attained by some p∗ ∈ P(R1 , R2 ) which satisfies R1 + R2 =
I(Y1 , Y2 ; U1∗ , U2∗ |Q∗ ), where U1∗ , U2∗ , Q∗ correspond to the auxiliary random variables defined by p∗ .
48

Proof. First, note that the infimum is always attained since P(R1 , R2 ) is compact and the objective function is continuous on P(R1 , R2 ). Therefore, let
U1∗ , U2∗ , Q∗ correspond to the auxiliary random variables which attain the infimum.
If H(Y1 |U1∗ , U2∗ , Q∗ ) + H(Y2 |U1∗ , U2∗ , Q∗ ) = 0, then we must have
I(Y1 , Y2 ; U1∗ , U2∗ |Q∗ ) = H(Y1 , Y2 ). Thus, R1 + R2 = I(Y1 , Y2 ; U1∗ , U2∗ |Q∗ ).
Next, consider the case where H(Y1 |U1∗ , U2∗ , Q∗ ) + H(Y2 |U1∗ , U2∗ , Q∗ ) > 0.
Assume for sake of contradiction that R1 + R2 > I(Y1 , Y2 ; U1∗ , U2∗ |Q∗ ). For any
p ∈ P(R1 , R2 ):
I(Y1 ; U1 |U2 , Q) + I(Y2 ; U2 |U1 , Q) ≤ I(Y1 , Y2 ; U1 , U2 |Q).
Hence, at most one of the remaining rate constraints can be satisfied with equality. If none of the rate constraints are satisfied with equality, then define

(U1∗ , U2∗ ) with probability 1 − 
(Ũ1 , Ũ2 ) =
(Y1 , Y2 ) with probability .
For  > 0 sufficiently small, the distribution p̃ corresponding to the auxiliary
random variables Ũ1 , Ũ2 , Q∗ is still in P(R1 , R2 ). However, p̃ satisfies
H(Y1 |Ũ1 , Ũ2 , Q∗ ) + H(Y2 |Ũ1 , Ũ2 , Q∗ ) < H(Y1 |U1∗ , U2∗ , Q∗ ) + H(Y2 |U1∗ , U2∗ , Q∗ ),
which contradicts the optimality of p∗ .
Therefore, assume without loss of generality that
R1 = I(Y1 ; U1∗ |U2∗ , Q∗ )
R1 + R2 > I(Y1 , Y2 ; U1∗ , U2∗ |Q∗ ).
This implies that R2 > I(Y2 ; U2∗ |Q∗ ). Now, define
 ∗
U2 with probability 1 − 
Ũ2 =
Y2 with probability .
Note that for  > 0 sufficiently small:
I(Y2 ; U2∗ |Q∗ ) < I(Y2 ; Ũ2 |Q∗ ) < R2
I(Y1 , Y2 ; U1∗ , U2∗ |Q∗ ) < I(Y1 , Y2 ; U1∗ , Ũ2 |Q∗ ) < R1 + R2 ,
and for any  ∈ [0, 1]:
R1 = I(Y1 ; U1∗ |U2∗ , Q∗ ) ≥ I(Y1 ; U1∗ |Ũ2 , Q∗ )
H(Y1 |U1∗ , U2∗ , Q∗ ) + H(Y2 |U1∗ , U2∗ , Q∗ ) ≥ H(Y1 |U1∗ , Ũ2 , Q∗ ) + H(Y2 |U1∗ , Ũ2 , Q∗ ).
(69)
Since R2 ≤ H(Y2 ), as  is increased from 0 to 1, at least one of the following
must occur:

49

1. I(Y2 ; Ũ2 |Q∗ ) = R2 .
2. I(Y1 , Y2 ; U1∗ , Ũ2 |Q∗ ) = R1 + R2 .
3. I(Y1 ; U1 |Ũ2 , Q∗ ) < R1 .
If either of events 1 or 2 occur first then the sum-rate constraint is met with
equality (since they are equivalent in this case). If event 3 occurs first, then all
rate constraints are satisfied with strict inequality and we can apply the above
argument to contradict optimality of p∗ . Since (69) shows that the objective is
nonincreasing in , there must exist a p̃ ∈ P(R1 , R2 ) which attains the infimum
and satisfies the sum-rate constraint with equality.

References
[1] D. Slepian and J. Wolf, “Noiseless coding of correlated information
sources,” Information Theory, IEEE Transactions on, vol. 19, pp. 471 –
480, Jul 1973.
[2] R. Ahlswede and J. Korner, “Source coding with side information and
a converse for degraded broadcast channels,” Information Theory, IEEE
Transactions on, vol. 21, pp. 629 – 637, Nov 1975.
[3] A. Wyner, “On source coding with side information at the decoder,” Information Theory, IEEE Transactions on, vol. 21, pp. 294 – 300, May 1975.
[4] A. Wyner and J. Ziv, “The rate-distortion function for source coding with
side information at the decoder,” Information Theory, IEEE Transactions
on, vol. 22, pp. 1 – 10, Jan. 1976.
[5] T. Berger and R. Yeung, “Multiterminal source encoding with one distortion criterion,” Information Theory, IEEE Transactions on, vol. 35, pp. 228
–236, Mar 1989.
[6] A. Wagner, S. Tavildar, and P. Viswanath, “Rate region of the quadratic
gaussian two-encoder source-coding problem,” Information Theory, IEEE
Transactions on, vol. 54, pp. 1938 –1961, May 2008.
[7] V. Prabhakaran, D. Tse, and K. Ramachandran, “Rate region of the
quadratic gaussian ceo problem,” in Information Theory, 2004. ISIT 2004.
Proceedings. International Symposium on, p. 119, june-2 july 2004.
[8] Y. Oohama, “Gaussian multiterminal source coding,” Information Theory,
IEEE Transactions on, vol. 43, pp. 1912 –1923, nov 1997.
[9] N. Cesa-Bianchi and G. Lugosi, Prediction, Learning, and Games. New
York, NY, USA: Cambridge University Press, 2006.

50

[10] T. Courtade and R. Wesel, “Multiterminal source coding with an entropybased distortion measure,” in Information Theory Proceedings (ISIT), 2011
IEEE International Symposium on, pp. 2040 –2044, Aug. 2011.
[11] P. Harremoes and N. Tishby, “The information bottleneck revisited or how
to choose a good distortion measure,” in Information Theory, 2007. ISIT
2007. IEEE International Symposium on, pp. 566 –570, June 2007.
[12] T. Andre, M. Antonini, M. Barlaud, and R. Gray, “Entropy-based distortion measure for image coding,” in Image Processing, 2006 IEEE International Conference on, pp. 1157 –1160, Oct. 2006.
[13] T. Berger, Z. Zhang, and H. Viswanathan, “The ceo problem [multiterminal source coding],” Information Theory, IEEE Transactions on, vol. 42,
pp. 887 –902, may 1996.
[14] T. Berger, Multiterminal Source Coding. In G. Longo (Ed.), The Information Theory Approach to Communications. New York, NY, USA: SpringerVerlag, 1977.
[15] S.-Y. Tung, Multiterminal Source Coding. PhD thesis, Cornell University,
Ithaca, NY, 1978.
[16] A. El Gamal and Y.-H. Kim, Network Information Theory. Cambridge
University Press, 2012.
[17] S. Jana, “Alphabet sizes of auxiliary random variables in canonical inner
bounds,” in Information Sciences and Systems, 2009. CISS 2009. 43rd
Annual Conference on, pp. 67 –71, March 2009.
[18] T. M. Cover and J. A. Thomas, Elements of Information Theory. John
Wiley & Sons, 2nd ed., 2006.
[19] E. Erkip, The Efficiency of Information in Investment. PhD thesis, Stanford University, 1996.
[20] Y.-H. Kim, A. Sutivong, and T. Cover, “State amplification,” Information
Theory, IEEE Transactions on, vol. 54, pp. 1850 –1859, may 2008.
[21] J. Korner and K. Marton, “How to encode the modulo-two sum of binary
sources (corresp.),” Information Theory, IEEE Transactions on, vol. 25,
pp. 219 – 221, Mar 1979.
[22] W. Gu and M. Effros, “On approximating the rate region for source coding
with coded side information,” in Information Theory Workshop, 2007. ITW
’07. IEEE, pp. 432 –435, Sept. 2007.
[23] W. Gu, S. Jana, and M. Effros, “On approximating the rate regions for lossy
source coding with coded and uncoded side information,” in Information
Theory, 2008. ISIT 2008. IEEE International Symposium on, pp. 2162 –
2166, July 2008.
51

[24] H. Witsenhausen, “Some aspects of convexity useful in information theory,”
Information Theory, IEEE Transactions on, vol. 26, pp. 265 – 271, May
1980.
[25] A. Schrijver, Combinatorial Optimization:
Berlin: Springer-Verlag, 2003.

Polyhedra and Efficiency.

[26] S. Fujishige, Submodular Functions and Optimization. Berlin: Elsevier
Science, 2nd ed., 2010.
[27] S. McCormick, Submodular Function Minimization. In Discrete Optimization, K. Aardal, G. Nemhauser, and R. Weismantel, eds. Handbooks in
Operations Research and Management Science, vol. 12. Elsevier, 2005.

52

