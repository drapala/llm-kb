---
source: "Elements of Information Theory"
author: "Thomas M. Cover, Joy A. Thomas"
year: 1991
edition: "1st"
publisher: "John Wiley & Sons (Wiley Series in Telecommunications)"
isbn: "0-471-06259-6"
type: textbook
url: "https://cs-114.org/wp-content/uploads/2015/01/Elements_of_Information_Theory_Elements.pdf"
access: open-pdf
chapters_extracted: [2, 8, 13, 14]
note: "Ch2 and Ch8 as summaries (definitions covered by Shannon 1948). Ch13 Rate Distortion and Ch14 Network Information Theory in full — CEO problem foundations + Slepian-Wolf."
---

# Elements of Information Theory — Cover & Thomas (1991)

## Scope of this extract

- **Chapter 2 Summary**: formal definitions (entropy, mutual information, properties)
- **Chapter 8 Summary**: channel capacity theorem
- **Chapter 13 (full)**: Rate Distortion Theory
- **Chapter 14 (full)**: Network Information Theory (Slepian-Wolf, MAC, broadcast, relay, Wyner-Ziv)

CEO problem (Berger 1996) not in 1st edition. Foundations in Ch13 (R(D)) and Ch14 (multi-terminal source coding). See raw/papers/courtade-ceo-problem.md for CEO problem.

---

## Chapter 2 Summary: Entropy, Relative Entropy, and Mutual Information


summary

SUMMARY
Definition:

(2.152)

H(P,)+P,log(m-l)rH(X).
mass function

(2.154)

- Yz p(x) log p(x). +E9

of H:

1. H(X)rO.
2. H,(X) = (log, a) H,(X).
3. (Conditioning
reduces entropy) For any two random variables, X and Y,

we have
H(XIY)

(2.155)

I H(X)

with equality if and only if X and Y are independent.
4. H(XI, X2, . . . , X, ) I Cy= 1 H(X, ), with equality if and only if the random
variables Xi are independent.
5. H(X) I log (%‘I with equality

if and only if X is uniformly

distributed

over 8.
6. H(p) is concave in p.
Definition:

The relative entropy D(pllq)

with respect to the probability

of the probability

mass diction

mass function p

Q is defined by

SUMMARY OF

CHAPTER

41

2

(2.156)
Definition:
The mutual information
is defined as

between two random variables X and Y

p(=c, Y)
z(x; Y) = 2 2 Pk Y) log pop(y)
*
ZEaTYEW
Alternative

expressions:

(2.157)

1
H(x) = E, log p(x)

(2.158)

1
H(x, n = E, log p(x, y)

(2.159)

1
= E, log p(X(Y)

(2.160)

H(XIY)

z(x;n =E,log

PK
p(x)p(y)

Y)

(2.161)

Pcx)

(2.162)

D(Plld = E, h3 m
Properties

of D and I:

1. Z(X, Y) = H(X) - ZZ(XIY) = H(Y) - H(YIX) = H(X) + H(Y) - NX, Y).
2. D(p 11q) L 0 with equality if and only if p(x) = q(x), for all x E kf’ .
3. Z(X, Y) = D( p(x, y)II p(x)p(y)) 2 0, with equality if and only if p(x, y) =
p(x)p(y), i.e., X and Y are independent.
over 8, then D(plJu) =
4. of I%pI= m, and u is the uniform distribution
log m - H(p).
5. D( p 114) is convex in the pair (p, q).
Chain

rules

Entropy:
H(x,,X,,
. . .v X,1= Cy=l HVr,(Xi-1, *a * ,X1)*
Mutual
information:
ZcX,,X,, . . . ,X,; Y)= Cy-,, Z(Xi; YJxl,X2, +* * ,Xi-1).
Relative entropy: D(p(x, y)IIqCx, yN = D(p(n)l(q(xN + D(p(y(x)((q(y(x)h
Jensen’s

If f is a convex function,

inequality:

Log sum inequality:
b 2, ***, b p&P

For n positive

$
i=l

I

with equality

Ui10gz2($

then EflX) 1 f(EX).

numbers,

a,, a,, . . . , a,, and b,,

(2.163)

U,)lOgw
8

i=l

if and only if a&b, = constant.

r=l

i

I

42

ENTROPY, RELATZVE ENTROPY AND MUTUAL

Data processing
Z(X, Y) 2 Z(x; 2)

inequality:

If X+

Second law of thermodynamics:

lNFORh4ATZON

Y+ 2 forms a Markov

For a Markov

chain, then

chain,

1. Relative entropy D( p, 11CL;) decreases with time.
2. Relative entropy D( ~~11CL) between a distribution
and the stationary
distribution
decreases with time.
3. Entropy H(X,) increases if the stationary distribution
is uniform.
4. The conditional entropy H(X, IX, ) increases with time for a stationary
Markov chain.
5. The conditional entropy H(X,jX,)
of the initial condition X0 increases
for any Markov chain.
Suffkient
statistic:
T(X) is sticient
1(0; X) = I(@; Z’(X)) for all distributions
Fano’s
Then

inequality:

relative
on 8.

Let P, = Fr{ g(Y) #X},

to {f,(z)}

if and only if

where g is any function

H(P,)+P,log(l~“(-l)rH(XIY).

of Y.
(2.164)

PROBLEMS FOR CHAPTER 2
1.

---

## Chapter 8 Summary: Channel Capacity


channel: C = log13 1- H(row of transition

matrix).

SUMMARY

OF CHAPTER

219

8

Properties
of C:
1. 0 5 C 5 min{loglWPj, logl%I}.
2. 1(X, Y) is a continuous concave function of p(x).
Definition:
The set A:’ of jointly typical sequences {(x”, y” )} with respect to
the distribution
p(x, y) is given by
4

(n) = w, y”)E
{

x c!P:

(8.158)

- ~logp(x”)-HO(cr,

(8.159)

lr

- i logp(y”HrRY)~
-~logp(x”,y”)-H(X,Y)

(8.160)

CE,
I

CC

I

,

(8.161)

where PW, yn I= l-l:= 1 phi 9yi )*
Joint AEP: Let (X”, Y”) be sequences of length n drawn i.i.d. according to
pW, y” ) = lly= 1 phi, yi 1. Then
1. Pr((X: Y”)EA~‘)+
1 as n-m.
2. (A:“‘1 I ‘-~d’,(x. Y)+C!
3. If (2: ?)

-p(d’)p(

y”), then Pr&‘,

?“) E A:‘)

I 2-“c’cx’ y)-3c!

The channel coding theorem:
AI1 rates below capacity C are achievable,
that is, for every E > 0 and rate R < C, there exists a sequence of (2”q n)
codes with maximum probability of error
A(“) I c ,
for n sufficiently

large. Conversely,

(8.162)

if hen’+ 0, then R I C.

Feedback
capacity:
Feedback does not increase capacity for discrete memoryless channels, i.e., CFB = C.
Source channel theorem:
A stochastic process with entropy rate H(V)
cannot be sent reliably over a discrete memoryless channel if H(V) > C.
Conversely, if the process satisfies the AEP, then the source can be transmitted reliably if H( ‘V ) < C.

220

CHANNEL

PROBLEMS

FOR CHAPTER

CAPACl-I’Y

8

1. Preprocessing the output. One is given a communication channel with
probabilities
p( y(x)
and channel
capacity
C=
transition
1(X;
Y).
A
helpful
statistician
preprocesses
the
output
by
max,,z )
forming Y = g(Y). He claims that this will strictly improve the
capacity.
(a) Show that he is wrong.
(b) Under what conditions does he not strictly decrease the capacity?
2.

Maximum likelihood decoding. A source produces independent, equally
probable symbols from an alphabet (a,, a,) at a rate of one symbol
every 3 seconds. These symbols are transmitted over a binary symmetric channel which is used once each second by encoding the source
symbol a 1 as 000 and the source symbol a, as 111. If in the
corresponding 3 second interval of the channel output, any of the
sequences 000,001,010,100 is received, a, is decoded; otherwise, a2 is
decoded. Let E < t be the channel crossover probability.
(a) For each possible received 3-bit sequence in the interval corresponding to a given source letter, find the probability that a,
came out of the source given that received sequence.
(b) Using part (a), show that the above decoding rule minimizes the
probability of an incorrect decision.
(c) Find the probability of an incorrect decision (using part (a) is not
the easy way here).
(d) If the source is slowed down to produce one letter every 2n + 1
seconds, a, being encoded by 2n + 1 O’s and a, being encoded by
2n + 1 1’s. What decision rule minimizes the probability of error
at the decoder? Find the probability of error as n+ 00.

3.

An additive noise channel. Find the channel capacity of the following
discrete memoryless channel:

z

X- --L

+

Y

where Pr{Z = 0) = Pr{Z = a} = 3. The alphabet for x is E = (0, 1).
Assume that 2 is independent of X.
Observe that the channel capacity depends on the value of a.
4.

Channels with memory have higher capacity. Consider a binary symmetric channel with Yi = Xi $ Zi, where $ is mod 2 addition, and
Xi, Yi E {O,l}.
Suppose that {Zi} has constant marginal probabilities ~{Zi = 1)
= p = 1 - Pr{ Zi = 0}, but that Z,, Z,, . . , , 2, are not necessarily in-

PROBLEMS

FOR

CHAPTER

221

8

dependent. Assume that 2” is independent of the input X”. Let
C=l-Wp,l-p).
Show that mq,~xl,x2 ,..., x,j I<X,,X, ,..., X,;
Y,,Y, ,..* ,Y,)rnC.
5.

Channel capacity. Consider
X + 2 (mod ll), where

the discrete

memoryless

1,
l/3,

3
l/3 )

(

z=

2,
l/3,

, lo}. Assume that 2 is independent
andXE{O,l,...
(a) Find the capacity.
(b) What is the maximizing p*(x)?

channel

Y=

of X.

6.

Using two channels at once. Consider two discrete memoryless
channels (gl, p(yllx,),
?V1) and Wz, p(yzlxz), 9~~) with capacities C,
and C, respectively. A new channel (gl x 5!&, p(y,lx,)
xp(y,lx,),
5, x 9z) is formed in which x, E %‘1and x, E Tz, are simultaneously
sent, resulting in yl, y2. Find the capacity of this channel.

7.

Noisy typewriter. Consider a 26-key typewriter.
(a) If pushing a key results in printing the associated letter, what is
the capacity C in bits?
(b) Now suppose that pushing a key results in printing that letter or
the next (with equal probability). Thus A+ A or B, . . . , Z+ 2 or
A. What is the capacity?
(c) What is the highest rate code with block length one that you can
find that achieves zero probability of error for the channel in part
09.

8.

Cascade of binary symmetric

cal binary symmetric
BSC#l

channels.

Show that a cascade of n identi-

channels,
jX1+...+Xn-l+

each with raw error probability p, is equivalent to a single BSC with
error probability $ (1 - (1 - 2~)” ) and hence that lim,,,
1(X,; Xn ) = 0
if p # 0,l. No encoding or decoding takes place at the intermediate
terminals X1, . . . , Xn- 1. Thus the capacity of the cascade tends to
zero.
9.

The Z channel.

and transition

The 2 channel has binary input and output alphabets
probabilities p( y lx) given by the following matrix:
1

Q= [ l/2

0
l/2

11
1 x,YE{O,

Find the capacity of the Z channel and the maximizing
ability distribution.

input prob-

10. Suboptimal codes. For the Z channel of the previous problem, assume
that we choose a (2”“, n) code at random, where each codeword is a

CHANNEL

CAPACU’Y

sequence of fair coin tosses. This will not achieve capacity. Find the
maximum rate R such that the probability
of error Pp’, averaged
over the randomly generated codes, tends to zero as the block length
n tends to infinity.
11.

Zero-error capacity. A channel with alphabet (0, 1,2,3,4}
tion probabilities of the form
P(~,xI={~/2

has transi-

ify=x+lmod5
otherwise.

(a) Compute the capacity of this channel in bits.
(b) The zero-error capacity of a channel is the number of bits per
channel use that can be transmitted
with zero probability
of
error. Clearly, the zero-error capacity of this pentagonal channel
is at least 1 bit (transmit 0 or 1 with probability l/2). Find a
block code that shows that the zero-error capacity is greater than
1 bit. Can you estimate the exact value of the zero-error
capacity?
(Hint: Consider codes of length 2 for this channel.)
The zero-error capacity of this channel was found by Lovasz [182].
12.

Time-vu ying channels. Consider a time-varying
channel. Let YI , Y2, . . . , Y, be conditionally
with conditional
distribution
Xl&,
* * * J,,
nycl pityi Ixi )*

discrete memoryless
independent
given
given by p( ~1x1 =

0

1 -Pi

Let X = (X1, Xz, . . . ,X,, ), Y = <Y,, Y2, . . . , Y, 1. Find max,,,, 1(X; Y).

HISTORICAL

NOTES

The idea of mutual information and its relationship to channel capacity was first
developed by Shannon in his original paper (2381. In this paper, he stated the
channel capacity theorem and outlined the proof using typical sequences in an
argument similar to the one described here. The first rigorous proof was due to
Feinstein [107], who used a painstaking “cookie-cutting”
argument to find the
number of codewords that can be sent with a low probability of error. A simpler
proof using a random coding exponent was developed by Gallager [118]. Our
proof is based on Cover [62] and on Fomey’s unpublished
course notes [115].

HISTORICAL

NOTES

223

The converse was proved by Fano [105], who used the inequality bearing his
name. The strong converse was first proved by Wolfowitz [276], using techniques
that are closely related to typical sequences. An iterative algorithm to calculate
the channel capacity was developed independently by Arimoto [ll] and Blahut
[371.

The idea of the zero-error capacity was developed by Shannon [239]; in the
same paper, he also proved that feedback does not increase the capacity of a
discrete memoryless channel. The problem of finding the zero-error capacity is
essentially combinatorial;
the first important result in this area is due to Lovasz
[182].

Elements of Information Theory
Thomas M. Cover, Joy A. Thomas
Copyright  1991 John Wiley & Sons, Inc.
Print ISBN 0-471-06259-6 Online ISBN 0-471-20061-1

Chapter 9

Differential

Entropy

We now introduce the concept of differential entropy, which is the
entropy of a continuous random variable. Differential entropy is also
related to the shortest description length, and is similar in many ways
to the entropy of a discrete random variable. But there are some
important differences, and there is need for some care in using the
concept.
9.1


---

## Chapter 13: Rate Distortion Theory (full)

ChaDter 13

Rate Distortion

Theory

The description of an arbitrary real number requires an infinite number
of bits, so a finite representation of a continuous random variable can
never be perfect. How well can we do? To frame the question
appropriately,
it is necessary to define the “goodness” of a
representation of a source. This is accomplished by defining a distortion
measure which is a measure of distance between the random variable
and its representation. The basic problem in rate distortion theory can
then be stated as follows: given a source distribution and a distortion
measure, what is the minimum expected distortion achievable at a
particular rate? Or, equivalently, what is the minimum rate description
required to achieve a particular distortion?
One of the most intriguing aspects of this theory is that joint
descriptions are more efficient than individual descriptions. It is simpler
to describe an elephant and a chicken with one description than to
describe each alone. This is true even for independent random variables.
It is simpler to describe X1 and X2 together (at a given distortion for
each) than to describe each by itself. Why don’t independent problems
have independent solutions? The answer is found in the geometry.
Apparently rectangular grid points (arising from independent descriptions) do not fill up the space efficiently.
Rate distortion theory can be applied to both discrete and continuous
random variables. The zero-error data compression theory of Chapter 5
is an important special case of rate distortion theory applied to a
discrete source with zero distortion.
We will begin by considering the simple problem of representing a
single continuous random variable by a finite number of bits.
336

13.1 QUANTIZATION

13.1

337

QUANTIZATION

This section on quantization motivates the elegant theory of rate distortion by showing how complicated it is to solve the quantization problem
exactly for a single random variable.
Since a continuous random source requires infinite precision to represent exactly, we cannot reproduce it exactly using a finite rate code. The
question is then to find the best possible representation for any given
data rate.
We first consider the problem of representing a single sample from
the source. Let the random variable to be represented be X and let the
representation of X be denoted as X(X). If we are given R bits to
represent X, then the function X can take on 2R values. The problem is
to find the optimum set of values for X (called the reproduction points or
codepoints) and the regions that are associated with each value X.
For example, let X - NO, (T’), and assume a square-d error distortion
measure. In this case, we wish to find the function X(X) such that X
takes on at most 2R values and minimizes E(X - X(XN2. If we are given
1 bit to represent X, it is clear that the bit should distinguish whether
X > 0 or not. To minimize squared error, each reproduced symbol should
be at the conditional mean of its region. This is illustrated in Figure
13.1. Thus
ifxr0,
ifx<O.
nI - d%,
0.4
0.35
0.3
0.25

2

0.2
0.15

-0.7979

0.7979
Figure 13.1. One bit quantization of a Gaussian random variable.

(13.1)

338

RATE DlSTORTlON

THEORY

If we are given 2 bits to represent the sample, the situation is not as
simple. Clearly, we want to divide the real line into four regions and use
a point within each region to represent the sample. But it is no longer
immediately obvious what the representation regions and the reconstruction points should be.
We can however state two simple properties of optimal regions and
reconstruction points for the quantization of a single random variable:
l

l

Given a set of reconstruction points, the distortion is minimized by
mapping a source random variable X to the representation X(w)
that is closest to it. The set of regions of %’defined by this mapping
is called a Voronoi or Dirichlet partition defined by the reconstruction points.
The reconstruction points should minimize the conditional expected
distortion over their respective assignment regions.

These two properties enable us to construct a simple algorithm to find
a “good” quantizer: we start with a set of reconstruction points, find the
optimal set of reconstruction regions (which are the nearest neighbor
regions with respect to the distortion measure), then find the optimal
reconstruction points for these regions (the centroids of these regions if
the distortion is squared error), and then repeat the iteration for this
new set of reconstruction points. The expected distortion is decreased at
each stage in the algorithm, so the algorithm will converge to a local
minimum of the distortion. This algorithm is called the Lloyd algorithm
[ 1811 (for real-valued random variables) or the generaked Lloyd aZgorithm [80] (for vector-valued random variables) and is frequently used
to design quantization systems.
Instead of quantizing a single random variable, let us assume that we
are given a set of n i.i.d. random variables drawn according to a
Gaussian distribution. These random variables are to be represented
using nR bits. Since the source is i.i.d., the symbols are independent,
and it may appear that the representation of each element is an
independent problem to be treated separately. But this is not true, as
the results on rate distortion theory will show. We will represent the
entire sequence by a single index taking ZnR values. This treatment of
entire sequences at once achieves a lower distortion for the same rate
than independent quantization of the individual samples.

13.2

DEFINITIONS

Assume that we have a source that produces asequenceX,,X,,...,X,
i.i.d. -p(x), x E 35 We will assume that the alphabet is finite for the

13.2

339

DEFlNlTlONS

proofs in this chapter; but most of the proofs can be extended to
continuous random variables.
The encoder describes the source sequence X” by an index f,(X”> E
{1,2,. . . , ZnR}. The decoder represents X” by an estimate p E @, as
illustrated in Figure 13.2.
Definition:

A distortion function or distortion measure is a mapping
(13.2)

d:%‘x&-R+

from the set of source alphabet-reproduction alphabet pairs into the set
of non-negative real numbers. The distortion d(x, i) is a measure of the
cost of representing the symbol x by the symbol i.
Definition:
A distortion measure is said to be bounded if the maximum
value of the distortion is finite, i.e.,
def

d max = max d(x,i)<m.
XEBe”,
i&t

(13.3)

In most cases, the reproduction alphabet k is the same as the source
alphabet %‘. Examples of common distortion functions are
Hamming (probability of error) distortion. The Hamming distortion
is given by

l

d&i)

=

0 ifx=i
1 ifx#?

(13.4)

which results in a probability of error distortion, since Ed(X, @ =
Pr(X #X).
Squared error distortion. The squared error distortion,

l

d(x, i) = (3~- i>2 ,

(13.5)

is the most popular distortion measure used for continuous alphabets. Its advantages are its simplicity and its relationship to
least squares prediction. But in applications such as image and

P

>

Encoder

fnw9 E (1,2,...Pl

>

Decoder

Figure 13.2. Rate distortion encoder and decoder.

,‘- &

340

RATE DlSTORTlON

THEORY

speech coding, various authors have pointed out that the mean
squared error is not an appropriate measure of distortion as observed by a human observer. For example, there is a large squared
error distortion between a speech waveform and another version of
the same waveform slightly shifted in time, even though both would
sound very similar to a human observer.
Many alternatives have been proposed; a popular measure of distortion in speech coding is the Itakura-Saito distance, which is the relative
entropy between multivariate normal processes. In image coding, however, there is at present no real alternative to using the mean squared
error as the distortion measure.
The distortion measure is defined on a symbol-by-symbol basis. We
extend the definition to sequences by using the following definition:
Definition:

The distortion

between sequences xn and in is defined by

d(x”,P)

= ; $ d(xi, &) .

(13.6)

11

So the distortion for a sequence is the average of i;he per symbol
distortion of the elements of the sequence. This is not the only reasonable definition. For example, one may want to measure distortion
between two sequences by the maximum of the per symbol distortions.
The theory derived below does not apply directly to this case.
Definition:

A (2nR,n) rate distortion

code consists of an encoding

function,

f, : Z”+ {1,2,. . . , 2nR} ,

(13.7)

and a decoding (reproduction) function,
g,:{1,2 ,...,

znR}+P.

(13.8)

The distortion associated with the (2nR,n) code is defined as
D = Ed(X”, g,( f, (x” 1))3

(13.9)

where the expectation is with respect to the probability distribution on
X, i.e.,
D = c p(x”) dtx”, g,( f,b” ))) .

xn

(13.10)

13.2

341

DEFiNITIONS

The set of n-tuples g,(l), g,(2), . . . , g,(2’?, denoted bY e(l),
. -3
p~2”~), constitutes the codebook, and f,‘(l), . . . , f,‘<2’?
are the
associated assignment regions.
l

Many terms are used to describe the replacement of X” by its
quantized version p(w). It is common to refer to * as the vector
quantization, reproduction, reconstruction, representation, source code,
or estimate of X”.
Definition:
A rate distortion pair (R, D) is said to be achievable if there
exists a sequence of (2”R, n) rate distortion codes ( f,, g, 1 with
lim,,, E&X”, g,( fn,cx” ))I 5 D.
Definition:
The rate distortion region for a source is the closure of the
set of achievable rate distortion pairs (R, D).
Definition:
The rate distortion function R(D) is the infimum of rates R
such that (R,D) is in the rate distortion region of the source for a given
distortion D.
Definition:
The distortion rate function D(R) is the inflmum of all
distortions D such that (R,D) is in the rate distortion region of the
source for a given rate R.
The distortion rate function defines another way of looking at the
boundary of the rate distortion region, which is the set of achievable
rate distortion pairs. We will in general use the rate distortion function
rather than the distortion rate function to describe this boundary,
though the two approaches are equivalent.
We now define a mathematical function of the source, which we call
the information rate distortion function. The main result of this chapter
is the proof that the information rate distortion function is equal to the
rate distortion function defined above, i.e., it is the infimum of rates that
achieve a particular distortion.
Definition:
The information rate distortion function
source X with distortion measure d(x, LC)is defined as

R"'(D) for a

I(X, 2)
min
i&D
pWp(ilx)d(x,

(13.11)

R"'(D) =

p(ilx) :

where the minimization is over all conditional distributions p(i)x) for
which the joint distribution p(x, i) = p(x)p(ilz) satisfies the expected
distortion constraint.

342

RATE DlSTORTION

THEORY

Paralleling the discussion of channel capacity in Chapter 8, we
initially consider the properties of the information rate distortion function and calculate it for some simple sources and distortion measures.
Later we prove that we can actually achieve this function, i.e., there
exist codes with rate R”‘(D) with distortion D. We also prove a converse
establishing that R 1 R”‘(D) for any code that achieves distortion D.
The main theorem of rate distortion theory can now be stated as
follows:
Theorem 13.2.1: The rate distortion function for an i.i.d. source X with
distribution p(x) and bounded distortion function d(x, i) is equal to the
associated information rate distortion function. Thus
I(X, 2)
(13.12)
min
R(D) = R”‘(D) -p(i(x):C(,,i)p(x)pdi.lzMz,
?ED
is the minimum achievable rate at distortion D.
This theorem shows that the operational definition of the rate distortion function is equal to the information definition. Hence we will use
R(D) from now on to denote both definitions of the rate distortion
function. Before coming to the proof of the theorem, we calculate the
information rate distortion function for some simple sources and distortions.
13.3

CALCULATION

13.3.1 Binary

OF THE RATE DISTORTION

FUNCTION

Source

We now find the description rate R(D) required to describe a
Bernoulli(p) source with an expected proportion of errors less than or
equal to D.
Theorem 13.3.1: The rate distortion function for a Bernoulli( p> source
with Hamming distortion is given by
O~D~min{p,l-p},
D>min{p,l-p}.

(13.13)

Proof: Consider a binary source X - Bernoulli(p) with a Hamming
distortion measure. Without loss of generality, we may assume that
p < fr. We wish to calculate the rate distortion function,
R(D) =

Icx;&.
min
p(ilr) : cc,,ij p(le)p(ilx)m,
i)=D

Let 69 denote modulo 2 addition. Thus X$X

(13.14)

= 1 is equivalent to X # X.

13.3

CALCULATlON

OF THE RATE DlSTORTlON

343

FUNCTION

We cannot minimize 1(X, X) directly; instead, we find a lower bound and
then show that this lower bound is achievable. For any joint distribution
satisfying the distortion constraint, we have

WC
a =H(X)
- H(X@)
= H(p) - H(XcBX(2)

(13.16)

H(p)-H(Xa32)

(13.17)

IH(p)--H(D),

(13.18)

since Pr(X #X) I D and H(D) increases with D for D 5 f . Thus
(13.19)

R(D)zH(p)-H(D).

We will now show that the lower bound is actually the rate distortion
function by finding a joint distribution that meets the distortion constraint and has 1(X, X) = R(D). For 0 I D 5 p, we can achieve the value
of the rate distortion function in (13.19) by choosing (X, X) to have the
joint distribution given by the binary symmetric channel shown in
Figure 13.3.
We choose the distribution of X at the input of the channel so that the
output distribution of X is the specified distribution. Let r = Pr(X = 1).
Then choose r so that
(13.20)

r(l-D)+(l-r)D=p,
or

(13.21)

0

1-D

0 l-p

X

P-D
1-W

1

1-D

Figure 13.3. Joint distribution

1

P

for binary source.

344

RATE DISTORTlON

I(x;~=HGX)-H(XI~=H(p)-H(D),

THEORY

(13.22)

and the expected distortion is RX # X) = D.
If D 2 p, then we can-achieve R(D) = 0 by letting X = 0 with probability 1. In this case, Z(X, X) = O-and D = p. Similarly, if D 2 1 - p, we cm
achieve R(D I= 0 by setting X = 1 with probability 1.
Hence the rate distortion function for a binary source is
OrD= min{p,l-p},
D> min{p,l-p}.

(13.23)

This function is illustrated in Figure 13.4. Cl
The above calculations may seem entirely unmotivated. Why should
minimizing mutual information have anything to do with quantization?
The answer to this question must wait until we prove Theorem 13.2.1.
13.3.2 Gaussian Source
Although Theorem 13.2.1 is proved only for discrete sources with a
bounded distortion measure, it can also be proved for well-behaved
continuous sources and unbounded distortion measures. Assuming this
general theorem, we calculate the rate distortion function for a Gaussian source with squared error distortion:
Theorem 13.3.2: The rate distortion function for a N(0, u2) source with
squared error distortion is
1
+%,

2

OsDsg2,

0,

I

0

(13.24)

D>U2.

I

I

I

0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
D

Figure 13.4. Rate distortion function for a binary source.

13.3 CALCULATZON OF THE RATE DlSTORTlON FUNCTION

345

proof= Let X be -N(O, a’). By the rate distortion theorem, we have
R(D) =

min
I(X, 2) .
(13.25)
flilx) :E(2-m2sD
As in the previous example, we first 6nd a lower bound for the rate
distortion function and then prove that this is achievable. Since
E(X - a2 5 D, we observe
Z(X, 2) = h(X) - h(X(X)

(13.26)

1
= 2 log(27re)(r2 - h(X - XIX)

(13.27)

2 f log(27re)cr2 - h(X - X)

(13.28)

1
2 2 log(27re)02 - h(N(0, E(X - 2)“))

(13.29)

1
= 5 log(27re)(r2 - f log(2ne)E(X - X)”

(13.30)

1
1
2 2 log(2?re)(r2 - 2 log(2we)D

(13.31)

1
= 2 log $ ,

(13.32)

where (13.28) follows from the fact that conditioning reduces entropy
and (13.29) follows from the fact that the normal distribution maximizes
the entropy for a given second moment (Theorem 9.6.5). Hence
R(D)? f log;.

(13.33)

To find the conditional density fliI%) that achieves this lower bound,
it is usually more convenient to look at the conditional density fix Ii>,
which is sometimes called the test channel (thus emphasizing the
duality of rate distortion with channel capacity). As in the binary case,
we construct flx)i) to achieve equality in the bound. We choose the joint
distribution as shown in Figure 13.5. If D I cr2,we choose
(13.34)
x=x+2,
k-N(0,a2-D),
Z-yNtO,D),

i-,V(0,a2-

D)+~+-X-N(0,02)

Figure 13.5. Joint distribution

for Gaussian source.

RATE DlSTORTlON

346

where X and 2 are independent. For this joint distribution,
I(X,k)=

THEORY

we calculate

flog;,

(13.35)

and E(X-X)2 = D, thus achieving the bound in (13.33). If D > a2, we
choose X = 0 with probability 1, achieving R(D) = 0.
Hence the rate distortion function for the Gaussian source with squared
error distortion is
R(D) =

1
z log ;

,

OsDscr2,
D>a2,

0,
as illustrated

(13.36)

in Figure 13.6. Cl

We can rewrite (13.36) to express the distortion in terms of the rate,
(13.37)

D(R) = a22-2R.

Each bit of description reduces the expected distortion by a factor of 4.
With a 1 bit description, the best expected square error is a2/4. We can
compare this with the result of simple 1 bit quantization of a N(0, a2)
random variable as described in Section 13.1. In this case, using the two
regions corresponding to the positive and negative real lines and reproduction points as the centroids of the respective regions, the expected
distortion is r-2 a2 = 0.3633~~. (See Problem 1.) As we prove later, the
rate distortion=limit R(D) is achieved by considering long block lengths.
This example shows that we can achieve a lower distortion by considering several distortion problems in succession (long block lengths) than
can be achieved by considering each problem separately. This is somewhat surprising because we are quantizing independent random variables.
3
2.5

-0

0.2

0.4

0.6

0.8

1

1.2

1.4

1.6

1.8

2

D

Figure 13.6. Rate distortion function for a Gaussian source.

13.3

CALCULATlON

347

OF THE RATE DZSTORTION FUNCTION

13.3.3 Simultaneous
Random Variables

Description

of Independent

Gaussian

Consider the case of representing m independent (but not identically
distributed)
normal random sources XI, . . . , Xm, where Xi are
-JV(O, CT:>,with squared error distortion. Assume that we are given R
bits with which to represent this random vector. The question naturally
arises as to how we should allot these bits to the different components to
minimize the total distortion. Extending the definition of the information rate distortion function to the vector case, we have
R(D) =

min

f(imlxm) :EdtXm,~m,zsD

I(X”; 2”))

(13.38)

where d(xm, irn ) = Cr!, (xi - &>2. Now using the arguments in the previous example, we have

I(X”;X”) = h(X”) - h(X”IX”)

(13.39)

= 2 h(Xi)- 2 h(xiIXi-1,2m)
1

(13.40)

i=l

i=l

h(Xi)-

~
i=l

=E

~
i=l

(13.41)

h(Xi(~i)

I(Xi;X) i

(13.42)

R(D i )

(13.43)

i=l

12
i=l

(13.44)

=~l(;log$+,

where Di = E(Xi - pi)’ and (13.41) follows from the fact that conditioning reduces entropy. We can achieve equality in (13.41) by choosing
f(36mI~m)= ~~=l f(Xil~i) an d in (13.43) by choosing the distribution of
each pi - &(O, 0; - Di >, as in the previous example. Hence the problem
of finding the rate distortion function can be reduced to the following
optimization (using nats for convenience):
R(D)=EA~D
1
Using Lagrange multipliers,
J(D)=2

gmax

.

(13.45)

i-l

we construct the functional
‘ln’+h$
i=l2
Di

Di,
i=l

(13.46)

RATE DZSTORTZON THEORY

348

and differentiating

with respect to Di and setting equal to 0, we have
aJ
-=
aDi

or

11
-gE+A=O,

(13.47)

i

(13.48)

Di = A’ .

Hence the optimum allotment of the bits to the various descriptions
results in an equal distortion for each random variable. This is possible
if the constant A’ in (13.48) is less than a; for all i. As the total
allowable distortion D is increased, the constant A’ increases until it
exceeds C: for some i. At this point the solution (13.48) is on the
boundary of the allowable region of distortions. If we increase the total
distortion, we must use the Kuhn-Tucker conditions to find the minimum in (13.46). In this case the Kuhn-Tucker conditions yield
aJ
a=

1 1
-2D,+A,

(13.49)

where A is chosen so that
ifDi<uB,
(13.50)
ifDi?uP.
It is easy to check that the solution to the Kuhn-Tucker equations is
given by the following theorem:
Theorem 13.3.3 (Rate distortion for a parallel Gaussian source): Let
Xi - N(0, Uf), i = 1,2, . . . , m be independent Gaussian random variables
and let the distortion measure be d(xm, irn) = Cr=, (Xi - 3;i)2.Then the rate
distortion function is given by
R(D)=2

m 1
zlog$
i=l

(13.51)
i

where
if ACuB,
if Aru$,

(13.52)

where A is chosen SO that Ill=, Di = D.
This gives rise to a kind of reverse “water-filling” as illustrated in
Figure 13.7. We choose a constant A and only describe those random

13.4

349

CONVERSE TO THE RATE DZSTORTZON THEOREM
2
'i

4

7

04
D3

O6

D,
Ds

xi

x2

Figure! 13.7. Reverse water-filling

x3

x4

x5

x6

for independent Gaussian random variables.

variables with variances greater than A. No bits are used to describe
random variables with variance less than A.
More generally, the rate distortion function for a multivariate normal
vector can be obtained by reverse water-filling on the eigenvalues. We
can also apply the same arguments to a Gaussian stochastic process. By
the spectral representation theorem, a Gaussian stochastic process can
be represented as an integral of independent Gaussian processes in the
different frequency bands. Reverse water-filling on the spectrum yields
the rate distortion function.
13.4

CONVERSE

TO THE RATE DISTORTION

THEOREM

In this section, we prove the converse to Theorem 13.2.1 by showing that
we cannot achieve a distortion less than D if we describe X at a rate less
than R(D), where
R(D) =

min
I(X, 2) .
p(ilx): c p(x)p(iIrkz(x,
i)sD
dr,i)

(13.53)

The minimization is over all conditional distributions p(;ls) for which
the joint distribution p(x, i) = p(x)& 1~)satisfies the expected distortion
constraint. Before proving the converse, we establish some simple
properties of the information rate distortion function.

Lemma 13.4.1 (Convexity of R(D)): The rate distortion function R(D)
given in (13.53) is a non-increasing convex function of D.
Proof: R(D) is the minimum of the mutual information over increasingly larger sets as D increases. Thus R(D) is non-increasing in D.
To prove that R(D) is convex, consider two rate distortion pairs
(R,, D, ) and (R2, D,) which lie on the rate-distortion curve. Let the joint

350

RATE DISTORTION

THEORY

distributions that achieve these pairs be pl(x, i) =p(x)p,(ilx)
and
p&, i) = p(z)&lx).
Consider the distribution pA = Ap, + (1 - A)JQ.
Since the distortion is a linear function of the distribution, we have
D( p,) = AD, + (1 - A)D,. Mutual information, on the other hand, is a
convex function of the conditional distribution (Theorem 2.7.4) and
hence
IJX; 2) 5 AIJX; k) + ( 1 - A)I,.JX; X) .

(13.54)

Hence by the definition of the rate distortion function,
ND, 11 IJZ

(13.55)

ti

5 AI&

%) + (1 - A)l,$X; X)

= AR(D,) + (1 - A)R(D,),
which proves that R(D) is a convex function of D.

(13.56)
(13.57)

Cl

The converse can now be proved.
Proof: (Converse in Theorem 13.2.1): We must show, for any source
X drawn i.i.d. -p(x) with distortion measure d(x, i), and any (2RR,n)
rate distortion code with distortion ID, that the rate R of the code
satisfies R 2 R(D).
Consider any (2”“, n) rate distortion code defined by functions f, and
g,. Let P = &X”) = g,( &(X”)) be the reproduced sequence corresponding to X”. Then we have the following chain of inequalities:
(13.58)
(13.59)
(13.60)
(13.61)

‘2 i H(Xi) - H(X”IP)

(13.62)

i=l

~ ~ H(xi) - ~ H(XiI~,Xi-l,
i=l

~

~

i=l

9x1)

(13.63)

i=l

H(x,)-

~

i=l

H(XiI$)

(13.64)

13.5

351

ACHZEVABZLZTY OF THE RATE DZSTORTZON FUNCTZON

=

i:
i=l

I(xi;s>

(13.65)

i

(13.66)

~ ~ R(Ed(Xi, ~ i ))
i=l

=n~

’
n

i=l

R(Ed(Xi,ff

i ))

(h)

2 nR(x

~ Ed(Xi,~i))

(13.67)
(13.68)

rl

‘2 nR(Ed(X”,

p)>

= nR(D),

(13.69)
(13.70)

where
(a) follows from the fact that there are at most 2nRp’s in the range
of the encoding function,
(b) from the fact that p is a function of X” and thus H(* IX” ) = 0,
(c) from the definition of mutual information,
(d) from the fact that the Xi are independent,
(e) from the chain rule for entropy,
(f) from the fact that conditioning reduces entropy,
(g) from the definition of the rate distortion function,
(h) from the convexity of the rate distortion function (Lemma 13.4.1)
and Jensen’s inequality, and
(i) from the definition of distortion for blocks of length n.
This shows that the rate R of any rate distortion code exceeds the rate
distortion function R(D) evaluated at the distortion level D = Ed(X”, p)
achieved by that code. 0
13.5

ACHIEVABILITY

OF THE RATE DISTORTION

FUNCTION

We now prove the achievability of the rate distortion function. We begin
with a modified version of the joint AIZP in which we add the condition
that the pair of sequences be typical with respect to the distortion
measure.
Definitions Let p(x, i) be a joint probability distribution on E x & and
let d(x, i) be a distortion measure on aPx %, For any E > 0, a pair of
sequences (x”, in) is said to be distortion e-typical or simply distortion
typical if

RATE DlSTORTZON THEORY

352

-;

1

1
--; log&?)-H(X)

<E

(13.71)

1
-;logp(?)-H(X)

<E

(13.72)

logp(x”,i”)-H(X,&

<e

(13.73)

]dW, i”) - Ed(X, %)I < E

(13.74)

The set of distortion typical sequences is called the distortion typical set
and is denoted A:‘,.
Note that this is the definition of the jointly typical set (Section 8.6)
with the additional constraint that the distortion be close to the expected value. Hence, the distortion typical set is a subset of the jointly
typical set, i.e., At;f’, CA:‘. If <xi, pi> are drawn i.i.d -p(x, 12),then the
distortion between two random sequences
d(X”,P)=

i $l d(Xi,*i)

(13.75)

i

is an average of i.i.d. random variables, and the law of large numbers
implies that it is close to its expected value with high probability. Hence
we have the following lemma.
Lemma

13.5.1: Let (Xi, pi) be drawn i.i.d. - p(x, i). Then Pr(Al;f’, )+ 1

us n-*a.
Proof: The sums in the four conditions in the definition of Agjc are
all normalized sums of i.i.d random variables and hence, by the law of
large numbers, tend to their respective expected values with probability
1. Hence the set of sequences satisfying all four conditions has probability tending to 1 as n- 00. Cl
The following lemma is a direct consequence of the definition of the
distortion typical set.
Lemma

13.5.2: For all (x”, i”) E A:‘,,

p($t) ~p~~~I~n)2-“(z(X;t)+3~)

.

(13.76)

Proof: Using the definition of A:‘,, we can bound the probabilities

p(x”), p(P) and ~(2, i”) for all (2, P) E A:‘,, and hence

13.5

ACHlEVABILZTY

OF THE RATE DISTORTION

FUNCTION

i”)
Jwp3 = pw,
&?a)

(13.77)

pw, 3)
=Pop(x”)p(~n)

(13.78)

2- n(H(X,a,-,,
n(H(X)+c)
2 -nvzUE)+E)
tj+3rj
= p(? )2n(Z(X;
2

ql(a2-

and the lemma follows immediately.

353

(13.79)
(13.80)

Cl

We also need the following interesting inequality.
Lemma 13.5.3: For 0 5 x, y 5 1, n > 0,
(13.81)
Proof: Let f(y) = e-’ - l+y. Thenf(O)=O andf’(y)=
-eeY+l>O
for y > 0, and hence fly) > 0 for y > 0. Hence for 0 I y I 1, we have
1- ySemY, and raising this to the nth power, we obtain
(1 -y)” IemY”.

(13.82)

Thus the lemma is satisfied for x = 1. By examination, it is clear that the
inequality is also satisfied for x = 0. By differentiation, it is easy to see
that g,(jc) = (1 - my)” is a convex function of x and hence for 0 5 x 5 1, we
have

(1- xy>”=gym

(13.83)

5 Cl- x)g,(O) + 3cg,w

(13.84)

= (1 - X)1 + x(1 -y)”

(13.85)

51 --x +xemyn

(13.86)

51 -x+ee-yn.

Cl

(13.87)

We use this to prove the achievability of Theorem 13.2.1.
Proof (Achievability in Theorem 13.2.1): Let XI, X,, . . . , Xn be
drawn i.i.d. - p(x) and let d(x, i) be a bounded distortion measure for
this source. Let the rate distortion function for this source be R(D).

354

RATE DISTORTION

THEORY

Then for any D, and any R > R(D), we will show that the rate distortion
pair (R, D) is achievable, by proving the existence a sequence of rate
distortion codes with rate R and asymptotic distortion D.
Fix p(i Ix), where p(ilx) achieves equality in (13.53). Thus 1(X; X) =
R(D). Calculate p(i) = C, p(x)p(i)x). Choose S > 0. We will prove the
existence of a rate distortion code with rate R and distortion less than or
equal to D + 6.
Generation of codebook. Randomly generate a rate distortion
codebook % consisting of 2nR sequences p drawn i.i.d. - lly=, ~(32~).
Index these codewords by w E { 1,2, . . . , 2nR}. Reveal this codebook
to the encoder and decoder.
Encoding. Encode X” by w if there exists a w such that (X”, p(w)) E
Al;f’,, the distortion typical set. If there is more than one such w,
send the least. If there is no such w, let w = 1. Thus nR bits suffice
to describe the index w of the jointly typical codeword.
Decoding. The reproduced sequence is x”(w).
Calculation of distortion. As in the case of the channel coding
theorem, we calculate the expected distortion over the random
choice of codebooks %’as
fi = Exn,.d(X”, p)
where the expectation is over the random choice of codebooks and
over X”.
For a tied codebook %’and choice of E > 0, we divide the sequences
xn E 8” into two categories:
l

l

Sequences xn such that there exists a codeword p(w) that is
distortion typical with xn, i.e., d(x”, Z(w)) <D + E. Since the total
probability of these sequences is at most 1, these sequences contribute at most D + E to the expected distortion.
Sequences xn such that there does not exist a codeword e(w) that
is distortion typical with xn. Let P, be the total probability of these
sequences. Since the distortion for any individual sequence is
bounded by d,,,, these sequences contribute at most P,d,,, to the
expected distortion.

Hence we can bound the total distortion by
Ed(X”, *(X”>> 5 D + E + P,d,,,

,

(13.89)

which can be made less than D + S for an appropriate choice of E if P, is
small enough. Hence, if we show that P, is small, then the expected
distortion is close to D and the theorem is proved.

13.5

ACHIEVABILITY

OF THE RATE DISTORTION

355

FUNCTION

Cchhtion
of P,. We must bound the probability that, for a random
choice of codebook % and a randomly chosen source sequence, there is no
codeword that is distortion typical with the source sequence. Let J( %)
denote the set of source sequences xn such that at least one codeword in
%’is distortion typical with xn.

Then

This is the probability of all sequences not well represented by a code,
averaged over the randomly chosen code. By changing the order of
summation, we can also interpret this as the probability of choosing a
codebook that does not well represent sequence xn, averaged with
respect to p(x”). Thus
(13.91)
Let us define
1 if (x”, i”) EA~‘~ ,

K(x”, in) =

0

(13.92)

if (x”, i”) $ZAg’, .

The probability that a single randomly chosen codeword x” does not
well represent a fixed xn is
p~(x:*>$@;)

= Pr(K(x:p)

= o) = I - &(in)~xn,

in),

(13.93)

and therefore the probability that 2”R independently chosen codewords
do not represent xn, averaged over p(x”), is
P,=&(x”)

c

PM)

(13.94)

v :x” $JC%,

Xn

= c po[
xn

1 - c p(?)K(xn, ??I”“.
P

(13.95)

We now use Lemma 13.5.2 to bound the sum within the brackets. From
Lemma 13.5.2, it follows that

2 p(.p)K(=zn,
in)2 c p(~n(Xn)2-n(z(x;a)+3.)~(x~, i”) ,
i”
and hence

in

(13.96)

356

RATE DlSTORTlON

THEORY

anR

P, 5 c $I&“)( 1 - 2-“(z(X;t)+3’) c p@yx”)K~x”, in))
x”
2”

. (13.97)

We now use Lemma 135.3 to bound the term on the right hand side of
(13.97) and obtain
2”R

(

1-2-

n(ZLY; A)+3c)

2 p(,plx~)K(;r:~,p)
>
i”
( 1 - c

p(.pIxn)&~,

p)

+ e-(2-n"(x;9)+3e)2nR)

.

(13.98)

in

Substituting this inequality in (13.971, we obtain
p, 5 1 - 2 &“)p(i”Ixn)K((xn,

i”) + e-2-n(z(X;k)+3t)2nR.

(13.99)

The last term in the bound is equal to
-cp(R-ZW,bP-Se)
e

9

(13.100)

which goes to zero exponentially fast with n if R > 1(X, a + 3~. Hence if
we choose p@(r) to be the conditional distribution that achieves the
minimum in the rate distortion function, then R > R(D) implies R >
1(X, X) and we can choose E small enough so that the last term in (13.99)
goes to 0.
The first two terms in (13.99) give the probability under the joint
distribution p(x”, P) that the pair of sequences is not distortion typical.
Hence using Lemma 13.5.1,

I - c c p(xR,
in)IC(X”,
in)=PI-W”,
p )@;‘, 1
Xn

12n

<E

(13.101)
(13.102)

for n sufficiently large. Therefore, by an appropriate choice of l and n,
we can make P, as small as we like.
So for any choice of 6 > 0 there exists an c and n such that over all
randomly chosen rate R codes of block length n, the expected distortion
is less than D + S. Hence there must exist at least one code %* with this
rate and block length with average distortion less than D + 8. Since 6
was arbitrary, we have shown that (R, 0) is achievable if R > R(D). Cl
We have proved the existence of a rate distortion code with an
expected distortion close to D and a rate close to R(D). The similarities
between the random coding proof of the rate distortion theorem and the
random coding proof of the channel coding theorem are now evident. We

13.5

ACHlEVABKITY

OF THE RATE DlSTORTlON

FUNCTION

357

will explore the parallels further by considering the Gaussian example,
which provides some geometric insight into the problem. It turns out
that channel coding is sphere packing and rate distortion coding is
sphere covering.
Channel coding for the Gaussian channel. Consider a Gaussian channel, Yi = Xi + Zi, where the Zi are i.i.d. - N(0, N) and there is a
power constraint P on the power per symbol of the transmitted
codeword. Consider a sequence of n transmissions. The power
constraint implies that the transmitted sequence lies within a
sphere of radius a
in W. The coding problem is equivalent to
finding a set of ZnR sequences within this sphere such that the
probability of any of them being mistaken for any other is smallthe spheres of radius a
around each of them are almost
disjoint. This corresponds to filling a sphere of radius vm
with spheres of radius a.
One would expect that the largest
number of spheres that could be fit would be the ratio of their
volumes, or, equivalently, the nth power of the ratio of their radii.
Thus if M is the number of codewords that can be transmitted
efficiently, we have
(13.103)
The results of the channel coding theorem show that it is possible
to do this efficiently for large n; it is possible to find approximately

codewords such that the noise spheres around them are almost
disjoint (the total volume of their intersection is arbitrarily small).
Rate distortion for the Gaussian source. Consider a Gaussian source
of variance a2. A (2nR,n) rate distortion code for this source with
distortion D is a set of 2nR sequences in W such that most source
sequences of length n (all those that lie within a sphere of radius
w)
are within a distance m
of some codeword. Again, by the
sphere packing argument, it is clear that the minimum number of
codewords required is

The rate distortion theorem shows that this minimum rate is
asymptotically achievable, i.e., that there exists a collection of

358

RATE DISTORTION

THEORY

spheres of radius m
that cover the space except for a set of
arbitrarily small probability.
The above geometric arguments also enable us to transform a good code
for channel transmission into a good code for rate distortion. In both
cases, the essential idea is to fll the space of source sequences: in
channel transmission, we want to find the largest set of codewords
which have a large minimum distance between codewords, while in rate
distortion, we wish to find the smallest set of codewords that covers the
entire space. If we have any set that meets the sphere packing bound for
one, it will meet the sphere packing bound for the other. In the
Gaussian case, choosing the codewords to be Gaussian with the appropriate variance is asymptotically optimal for both rate distortion and
channel coding.
13.6 STRONGLY TYPICAL SEQUENCES AND RATE DISTORTION
In the last section, we proved the existence of a rate distortion code of
rate R(D) with average distortion close to D. But a stronger statement is
true-not
only is the average distortion close to D, but the total
probability that the distortion is greater than D + S is close to 0. The
proof of this stronger result is more involved; we will only give an
outline of the proof. The method of proof is similar to the proof in the
previous section; the main difference is that we will use strongly typical
sequences rather than weakly typical sequences. This will enable us to
give a lower bound to the probability that a typical source sequence is
not well represented by a randomly chosen codeword in (13.93). This
will give a more intuitive proof of the rate distortion theorem.
We will begin by defining strong typicality and quoting a basic
theorem bounding the probability that two sequences are jointly typical.
The properties of strong typicality were introduced by Berger [281 and
were explored in detail in the book by Csiszar and Kiirner [83]. We will
define strong typicality (as in Chapter 12) and state a fundamental
lemma. The proof of the lemma will be left as a problem at the end of
the chapter.
Definition:
A sequence xn E SE’”is said to be c-strongly typical with
respect to a distribution p(x) on Z!Yif
1. For all a E S?with p(a) > 0, we have
(13.106)
2. For all a E % with p(a) = 0, N(alxn) = 0.

13.6

359

STRONGLY TYPlCAL SEQUENCES AND RATE DISTORTION

N(alxn) is the number of occurrences of the symbol a in the sequence
X”.

The set of sequences xn E Z’” such that xn is strongly typical is called
the strongly typical set and is denoted Afn’(X) or AT’“’ when the random
variable is understood from the context.
Definition:
A pair of sequences (x”, y” ) E Z” x 9” is said to be Estrongly typical with respect to a distribution p(x, y) on %’ X ??Iif
1. For all (a, b) E 2 x 3 with p(a, b) > 0, we have
iN(a,

bIxn, y”)-pb,W

<-

l&l

(13.107)

?

2. For all (a, b) E 8? x 9 with p(a, b) = 0, N(a, bIxn, y”) = 0.
N(o, bIxn, Y”) is the number of occurrences of the pair (a, b) in the
pair of sequences (xn, y”).
The set of sequences (x”, y” ) E %? x ?V such that (xn, yn ) is strongly
typical is called the strongly typical set and is denoted AT’“‘(X, Y) or
A*(n).
‘From the definition, it follows that if (x”, y” >E AT’“‘(X, Y), then
xn E Af’(X).
From the strong law of large numbers, the following lemma is
immediate.
Lemma 13.6.1: Let (Xi, Yi) be drawn i.i.d. - p(x, y). Then Pr(Af”‘)+
as n+m.

1

We will use one basic result, which bounds the probability that an
independently drawn sequence will be seen as jointly strongly typical
with a given sequence. Theorem 8.6.1 shows that if we choose X” and Y”
independently, the probability that they will be weakly jointly typical is
4- nzcx;Y) . The following lemma extends the result to strongly typical
sequences. This is stronger than the earlier result in that it gives a
lower bound on the probability that a randomly chosen sequence is
jointly typical with a fixed typical xn.
Lemma 13.6.2: Let Yl, Y2, . . . , Y, be drawn i.i.d. -II p(y). For xn E
A z(“‘, the probability that (x”, Y”) E AT’“’ is bounded by
2- n(Z(X; Y)+E,) I

pdcxn,

yn)

EA;(n))

where E, goes to 0 as E--, 0 and n+ 00.

I

g-n(ZcX;

Y)-El)

,

(13.108)

360

RATE DlSTORTlON

THEORY

Proof: We will not prove this lemma, but instead outline the proof in
a problem at the end of the chapter. In essence, the proof involves
finding a lower bound on the size of the conditionally typical set. Cl
We will proceed directly to the achievability of the rate distortion
function. We will only give an outline to illustrate the main ideas. The
construction of the codebook and the encoding and decoding are similar
to the proof in the last section.
Proof: Fix p(iIx). Calculate p(i) = C, p($p(~?I;1~).Fix E > 0. Later we
will choose E appropriately to achieve an expected distortion less than
D + 6.
Generation of codeboolz. Generate a rate distortion codebook % consisting of ZnR sequences p drawn i.i.d. -llip(lZi). Denote the
sequences P(l), . . . , P(anR).
Encoding. Given a sequence X”, index it by w if there exists a w such
that (X”, x”(w)) E Afn), the strongly jointly typical set. If there is
more than one such w, send the first in lexicographic order. If there
is no such w, let w = 1.
Decoding. Let the reproduced sequence be k(w).
Calculation of distortion. As in the case of the proof in the last
section, we calculate the expected distortion over the random
choice of codebook as
D = Ex,,, ,d(X”, p)
= E, c p(x” )d(xn, %‘Yxn)I

(13.110)

= 2 p;n)E,d(x:*l,
xn

(13.111)

where the expectation is over the random choice of codebook.
For a fixed codebook %, we divide the sequences xn E 8?” into three
categories as shown in Figure 13.8.
l

l

The non-typical sequences xnFAe I(n). The total probability of these
sequences can be made less than E by choosing n large enough.
Since the individual distortion between any two sequences is bounded by d,,,, the non-typical sequences can contribute at most Ed,,,
to the expected distortion.
Typical sequences xn E AT’“’ such that there exists a codeword &’
that is jointly typical with x”. In this case, since the source sequence
and the codeword are strongly jointly typical, the continuity of the

13.6

STRONGLY TYHCAL

SEQUENCES AND RATE DISTORTlON

361

Figure 13.8. Classes of source sequences in rate distortion theorem.

l

distortion as a function of the joint distribution ensures that they
are also distortion typical. Hence the distortion between these xn
and their codewords is bounded by D + Ed,,,, and since the total
probability of these sequences is at most 1, these sequences contribute at most D + ~d,,.,~~to the expected distortion.
Typical sequences xn E AT’“’ such that there does not exist a
codeword p that is jointly typical with x”. Let P, be the total
probability of these sequences. Since the distortion for any individual sequence is bounded by d,,,, these sequences contribute at most
P,4nax to the expected distortion.

The sequences in the first and third categories are the sequences that
may not be well represented by this rate distortion code. The probability
of the first category of sequences is less than E for sufficiently large n.
The probability of the last category is P,, which we will show can be
made small. This will prove the theorem that the total probability of
sequences that are not well represented is small. In turn, we use this to
show that the average distortion is close to D.
Cakulation of P,. We must bound the probability that there is no
codeword that is jointly typical with the given sequence X”. From
the joint AEP, we know that the probability that X” and any x” are
jointly typical is A 2-nz(x’ “!- Hence the expected number of jointly
typical x”(w) is 2nR2-nz’x’x’, which is exponentially large if R >
I(X, X).
But this is not sufficient to show that P, + 0. We must show that the
probability that there is no codeword that is jointly typical with X” goes
to zero. The fact that the expected number of jointly typical codewords is

362

RATE DISTORTION

THEORY

exponentially large does not ensure that there will at least one with
high probability.
Just as in (13.93), we can expand the probability of error as
I’, =

c

p(xn)[l - Pr((x”, ?,

E Afn))12”R.

(13.112)

xn EAT(~)

From Lemma 13.6.2, we have

Substituting this in (13.112) and using the inequality (1 - x)” 5 eVnx,we
have
(13.114)
which goes to 0 as n + a if R > 1(X, & + Ed. Hence for an appropriate
choice of E and n, we can get the total probability of all badly represented sequences to be as small as we want. Not only is the expected
distortion close to D, but with probability going to 1, we will find a
codeword whose distortion with respect to the given sequence is less
than D+6. Cl
13.7 CHARACTERIZATION
FUNCTION

OF THE RATE DISTORTION

We have defined the information rate distortion function as

R(D)=

min
Polx):q+)P Wq(ildd(z,

i&D

m

a ,

(13.115)

where the minimization is over all conditional distributions @Ix) for
which the joint distribution p(~)&?Ix) satisfies the expected distortion
constraint. This is a standard minimization problem of a convex function over the convex set of all q(i 1~)I 0 satisfying C, &IX) = 1 for all x
and CQ(~~X)JI(X)C&X,
i) 5 D.
We can use the method of Lagrange multipliers to find the solution.
We set up the functional

qGIx>

J(q) = c c p(x)q(iIx) log c p(x)q(iIx) + A T c PWW~k

x i

X

32

a
(13.116)

(13.117)

13.7

CHARACTERIZATlON

OF THE RATE DISTORTION

363

FUNCTlON

where the last term corresponds to the constraint that @Ix) is a
conditional probability mass function. If we let q(i) = C, p(x)q(iIx) be
the distribution on X induced by &C lx), we can rewrite J(a) as

J(q)=cx ci pWqG
Ix>
log$
+cx dx>C
qelx)
i

+ AC c p(x)q(iIx)&x,
2 i

i)

(13.118)
(13.119)

DifYerentiating with respect to &fix), we have

+pw - c p(r’)q(~lx’)--&p~x)
x’

+ Ap(xMx, i)

+ v(x) = 0 .

(13.120)

Setting log p(x) = ~(x>/p(x>, we obtain

1

+ h&x, i> + log /&L(x) = 0

p(x)[ log s

(13.121)

(13.122)
Since C, q(i(x)

= 1, we must have
p(x) = 2 q(i)e-*d’“, i,
P

qcqx) =

Multiplying

q@e
c,

-Ad(x,

(13.123)

i)

q(i)e-Wd

(13.124)

l

this by p(x) and summing over all x, we obtain
-hd(x,

q(i)

= q(i)

2r

i)

c;, p(x)e
q(~t)e-kW”

’

(13.125)

If q(i) > 0, we can divide both sides by q(i) and obtain
p&k

c

-I\d(r,

i)

z c,, q(~/)e-WW

=1

(13.126)

for all i E &‘. We can combine these @‘I equations with the equation

RATE DISTORTION

364

THEORY

defining the distortion and calculate h and the I@ unknowns q(i). We
can use this and (13.124) to find the optimum conditional distribution.
The above analysis is valid if all the output symbols are active, i.e.,
q(i) > 0 for all i. But this is not necessarily the case. We would then
have to apply the Kuhn-Tucker conditions to characterize the minimum.
The inequality condition a(i) > 0 is covered by the Kuhn-Tucker conditions, which reduce to
aJ

aq(ild

=0

if q(iJz)>O,

20

if q(iJx)=O.

(13.127)

Substituting the value of the derivative, we obtain the conditions for the
minimum as
cx

p(de

-A&x, i)

& q(~‘)e-Ad’“, i’) =1

-h&x, if)
p We
cx c;, q(Jl’)e-“d’“’ i’) sl

if q(i)>O,

(13.128)

if q(i) = 0 .

(13.129)

This characterization will enable us to check if a given q(i) is a solution
to the minimization problem. However, it is not easy to solve for the
optimum output distribution from these equations. In the next section,
we provide an iterative algorithm for computing the rate distortion
function. This algorithm is a special case of a general algorithm for
finding the minimum relative entropy distance between two convex sets
of probability densities.

13.8 COMPUTATION OF CHANNEL CAPACITY AND THE RATE
DISTORTION FUNCTION
Consider the following problem: Given two convex sets A and B in .%n as
shown in Figure 13.9, we would like to the find the minimum distance
between them
d min = aEyipE,
,

&a,

b)

,

(13.130)

where d(a, b) is the Euclidean distance between a and b. An intuitively
obvious algorithm to do this would be to take any point x E A, and find
the y E B that is closest to it. Then fix this y and find the closest point in
A. Repeating this process, it is clear that the distance decreases at each
stage. Does it converge to the minimum distance between the two sets?
Csiszhr and Tusnady [85] have shown that if the sets are convex and if
the distance satisfies certain conditions, then this alternating minimiza-

13.8

COMPUTATION

OF CHANNEL

365

CAPACITY

Figure 13.9. Distance between convex sets.

tion algorithm will indeed converge to the minimum. In particular, if the
sets are sets of probability distributions and the distance measure is the
relative entropy, then the algorithm does converge to the the minimum
relative entropy between the two sets of distributions.
To apply this algorithm to rate distortion, we have to rewrite the rate
distortion function as a minimum of the relative entropy between two
sets. We begin with a simple lemma:
Lemma X3.8.1: Let p(x)p( ylx) be a given joint distribution. Then the
distribution r(y) that minimizes the relative entropy D( p(x)p( yIx)ll p(x)
r(y)) is the marginal distribution r*(y) corresponding to p( ~1x1, i.e.,

D(p(x)p(y(x)l(p(x)r*(y))

= 7% D(p(dp( yIdIIpW-( yN ,
(13.131)

where r*(y) = C, p(x)p( y lx). Also
ZE

Fy
, PWP(Y

Id log$$

= x9
c p(x)p( ylx) log $$
Y

pWp( y Id
r*(3cly) = c, p(x)p( y Jx) *

, (13.132)

(13.133)

proof:
D( pWp( yldJI pWr( yN - D(pWp( yIx)ll pWr*( yN
= c PCX)P(Ylx>log$g;;jy
x9Y

(13.134)

366

RATE DISTORTION

THEORY

(13.136)
(13.137)

(13.139)

10.

The proof of the second part of the lemma is left as an exercise. cl
We can use this lemma to rewrite the minimization in the definition
of the rate distortion function as a double minimization,
R(D) = min

min

2 2 p(3G)q(32~x)log
$i!$

r(i) q(iJx):c p(x)q(iIx)d(x,3iMD z p

l

(13.140)
If A is the set of all joint distributions with marginal p(x) that satisfy
the distortion constraints and if B the set of product distributions
p(~)r($ with arbitrary r(i), then we can write

We now apply the process of alternating minimization, which is called
the Blahut-Arimoto algorithm in this case. We begin with a choice of A
and an initial output distribution r(i) and calculate the q(ilx) that
minimizes the mutual information subject to a distortion constraint. We
can use the method of Lagrange multipliers for this minimization to
obtain
q(qx)

-h&x, i)
r(i)e
= c; r(.$e-wG)

(13.142)

.

For this conditional distribution q(ilx), we calculate the output distribution r(32)that minimizes the mutual information, which by Lemma
13.31 is
(13.143)
We use this output distribution as the starting point of the next
iteration. Each step in the iteration, minimizing over q( I ) and then
minimizing over r( >reduces the right hand side of (13.140). Thus there
is a limit, and the limit has been shown to be R(D) by Csiszar [791,
l

l

l

SUMMARY

367

OF CHAPTER 13

where the value of D and R(D1 depends on h. Thus choosing A appropriately sweeps out the R(D)curve.
A similar procedure can be applied to the calculation of channel
capacity. Again we rewrite the definition of channel capacity,

(13.144)
as a double maximization using Lemma 13.8.1,
c = Fx$YF

c c r(jc)p(yld
32 Y

&lY)
log r(x)

(13.145)

.

In this case, the Csiszar-Tusnady algorithm becomes one of alternating
maximization-we
start with a guess of the maximizing distribution r(x)
and find the best conditional distribution, which is, by Lemma 13.8.1,
(13.146)
For this conditional distribution, we find the best input distribution r(x)
by solving the constrained maximization problem with Lagrange multipliers. The optimum input distribution is

n,cq(x1y))p’y’x)

(13.147)

r(X) = c, rl,( q(xJy))p’y’x) ’

which we can use as the basis for the next iteration.
These algorithms for the computation of the channel capacity and the
rate distortion function were established by Blahut [37] and Arimoto
[ll] and the convergence for the rate distortion computation was proved
by Csiszar [79]. The alternating minimization procedure of Csiszar and
Tusnady can be specialized to many other situations as well, including
the EM algorithm [88], and the algorithm for finding the log-optimal
portfolio for a stock market 1641.

SUMMARY

OF CHAPTER

13

Rate distortion:
The rate distortion function for a source X-p(r)
distortion measure d(x, i) is
R(D) =

min
1(x; a ,
p(Xlx):C(,,i)p(x)p(iIx)d(x,
i)SD

and

(13.148)

368

RATE DZSTORTZON THEORY

where the minimization is over all conditional distributions p(i]x) for which
the joint distribution p(r, i) = p(x)p(~~;lx>satisfies the expected distortion
constraint.
Rate distortion
theorem: If R > R(D), there exists a sequence of codes
&X”)
with number of codewords IXY )I I 2”R with E&X”, X’YX”))-, D. If
R <R(D), no such codes exist.
l

Bernoulli

source: For a Bernoulli source with Hamming distortion,
(13.149)

R(D)=H(p)-H(D).

Gaussian source: For a Gaussian source with squared error distortion,
(13.150)

R(D)=;log$.

Multivariate
Gaussian source: The rate distortion function for a multivariate normal vector with Euclidean mean squared error distortion is
given by reverse water-filling on the eigenvalues.

PROBLEMS
1.

FOR CHAPTER

13

One bit quantization of a single Gaussian random variable. Let XJw, a21 and let the distortion measure be squared error. Here we do

not allow block descriptions. Show that the optimum reproduction
points for 1 bit quantization are -+flu,
and that the expected
distortion for 1 bit quantization is %? a”.
Compare this with the distortion rate bound D = a22 -2R for R = 1.
2.

Rate distortion function wit? infinite distortion. Find the rate distortion
function R(D) = min 1(X, X) for X - Bernoulli ( i ) and distortion

0, x=i,
d(Q)=

1,

x=l,i=O,

100, x=0$=1.
3.

Rate distortion for binary source with asymmetric distortion.

Fix p(xli)

and evaluate 1(X,X) and D for
X- Bern(l/2),
d(x,c,)=

[ I
0
b

a
o .

(R(D) cannot be expressed in closed form.)

4. Properties of R(D). Consider a discrete source X E %’= { 1,2, . . . , m}
with distribution pl, p2, . . . , p, and a distortion measure d(i, j). Let
R(D) be the rate distortion function for this source and distortion
measure. Let d’(i, j) = d(i, j) - wi be a new distortion measure and

369

PROBLEMS FOR CHAPTER 33

let R’(D) be the corresponding rate distortion function. Show that
R’(D) = R(D + W), where ti = C piwi, and use this to show that there
is no essential loss of generality in assuming that min, c&i, i) = 0, i.e.,
for each x E 8, there is one symbol 2 which reproduces the source
with zero distortion.
This result is due to Pinkston [209].
5. Rate distortion for uniform source with Hamming distortion. Consider a
source X uniformly distributed on the set { 1,2, . . . , m}. Find the rate
distortion function for this source with Hamming distortion, i.e.,
d(x, i) =
6.

0 ifx=i,
{ 1 ifx#i.

Shannon lower bound for the rate distortion function. Consider a source
X with a distortion measure d(x, i) that satisfies the following property: all columns of the distortion matrix are permutations of the set
W,, 4,. . . , d,}. Define the function
4(D)=

glax
P’Cizl

(13.151)

H(p).

PidisD

The Shannon lower bound on the rate distortion function [245] is
proved by the following steps:
(a) Show that 4(D) is a concave function of D.
(b) Justify th e following series of inequalities for 1(X; X) if
Ed(X, k) 5 D,
1(x; % = H(X) - H(X@)
= H(X) - 2 p(i)H(X@
i
1 H(X) - c p(i)+(D,)
i

(13.152)
= i)

(13.153)
(13.154)
(13.155)

rH(X)-

4(D),

(13.156)

R(DkH(X)-4(D),

(13.157)

where Di = C, p(x]i)d(x, i).
(c) Argue that

which is the Shannon lower bound on the rate distortion function.
(d) If in add i t ion, we assume that the source has a uniform distribution and that the rows of the distortion matrix are permutations of each other, then R(D) = H(X) - 4(D), i.e., the lower
bound is tight.

RATE DlSTORTlON THEORY

370

7. Erasure distortion. Consider X- Bernoulli( i ), and let the distortion
measure be given by the matrix

Calculate the rate distortion function for this source. Can you suggest
a simple scheme to achieve any value of the rate distortion function
for this source?
8. Bounds on the rate distortion function for squared error distortion.
For the case of a continuous random variable X with mean zero and
variance a2 and squared error distortion, show that
h(X) - i log(2?re)D I R(D) I f log $ .

(13.159)

For the upper bound, consider the joint distribution shown in Figure
13.10. Are Gaussian random variables harder or easier to describe
than other random variables with the same variance?

Figure 13.10. Joint distribution

for upper bound on rate distortion function.

9. Properties of optimal rate distortion code. A good (R, D) rate distortion
code with R = R(D) puts severe constraints on the relationship of the
source X” and the representations x”. Examine the chain of
inequalities (13.58-13.70) considering the conditions for equality and
interpret as properties of a good code. For example, equality in
(13.59) implies that p is a deterministic function of X”.
10. Probability of conditionally typical sequences.In Chapter 8, we calculated the probability that two independently drawn sequencesX” and
Y” will be weakly jointly typical. To prove the rate distortion
theorem, however, we need to calculate this probability when one of
the sequences is fixed and the other is random.
The techniques of weak typicality allow us only to calculate the
average set size of the conditionally typical set. Using the ideas of
strong typicality on the other hand provides us with stronger bounds
which work for all typical X” sequences. We will outline the proof that
Pr{(x”, Y”) E AT’“‘} = 2-nz(X’ y, for all typical x~. This approach was
introduced by Berger [28] and is fully developed in the book by
Csiszar and Korner [83].

371

PROBLEMS FOR CHAPTER 13

Let (Xi, Yi> be drawn i.i.d. -p(z, y). Let the marginals of X and Y
be p(x) and p(y) respectively.
(a) Let A*(“)
c be the strongly typical set for X. Show that
IA;‘“‘I

& 2nH(X)

(13.160)

Hint: Theorem 12.1.1 and 12.1.3.
(b) The joint type of a pair of sequences W, y” ) is the proportion of
times (xi, yi) = (a, b) in the pair of sequences, i.e.,
b(x”, y”) = i &$,I(xi = a, yi = b) * (13.161)

pxn,Yn(a,b) = $(a,

The conditional type of a sequence y” given xR is a stochastic
matrix that gives the proportion of times a particular element of
9 occurred with each element of 8 in the pair of sequences.
Specifically, the conditional type V,,,,,(b Icz)is defined as
V,~,,dbb) =

Nb, blx”, Y”)
jQlxn)
*

(13.162)

Show that the number of conditional types is bounded by (n +
l)l”lPl .
(c) The set of sequences y” E 9” with conditional type V with respect
to a sequence zn is called the conditional type class Tv(x” ). Show
that
(13.163)

(n + ~),*,,~, 2nH(Y’X)5 IT”(X”>I 5 2nH(Y’X).

(d) The sequence yn E W is said to be e-strongly conditionally typical
with the sequence xn with respect to the conditional distribution
V( - I . ) if the conditional type is close to V. The conditional type
should satisfy the following two conditions:
i. For all (a, b) E aPx 91with V(bla)> 0,
; IN(a, blx: y”) - V(bla)N(alx”)l~

6

. (13.164)

ii. N(a, blx”, y”) = 0 for all (a, b) such that V(bla) = 0.
The set of such sequences is called the conditionally typical set
and is denoted AT’“’ (Ylx”). Show that the number of sequences y”
that are conditionally typical with a given xn E ZP is bounded by
?t(W(Y(X)-cl)

I

IA;‘“‘(ylx”)l

5

(n

+

l)1~11~Y12n(N(Y1X)+cl)

,

(13.165)
where E~--,O as E+O.

372

RATE DZSTORTION THEORY

(e) For a pair of random variables (X, Y) with joint distribution
p(x, y), the e-strongly typical set AT’“’ is the set of sequences
(x”, y”) E En X ??/” satisfying
i.

/iN(a,blx”,Y”) --da,

WI<

(13.166)

&

for every pair (a, b) E %’ x 3 with p(a, b) > 0.
ii. N(a,b~x~,y”)=Oforall(a,b)~%‘~~withp(a,b)=O.
The set of E-strongly jointly typical sequences is called the Estrongly jointly typical set and is denoted Af”‘(X, Y).
Let (X, Y) be drawn i.i.d. -p(x, y). For any xn such that there
exists at least one pair (x”, y”) E AT’“‘(X, Y), the set of sequences
y” such that (x”, y”) EAT(~) satisfies
(n + ;),%,,%,2n(H(YIX)-G(c))
I I{ yR: (x”, y”) E AT’“‘} 1
,
(13.167)

I(n + 1) I~11912n(H(YlX)+S(s))
where US+ 0 as E+ 0. In particular, we can write
2n(ff(YIX)-+ I I{yn:(xn, y”) eAT(

5 24H(Y1X)+4,
(13.168)

where we can make Q. arbitrarily small with an appropriate
choice of E and n.
(f) Let Y1, Y2,. . . , Y, be drawn i.i.d. -np(yi>. For xn EA:(~‘, the
probability that (x”, Y”) E AT’“’ is bounded by
2- nU(X;Y)+e3)

5 I+((~“, y”) E AT’“‘) 5 2-n(z(X;

y)-s3)

, (13.169)

where Edgoes to 0 as E+ 0 and n+a.

HISTORICAL

NOTES

The idea of rate distortion was introduced by Shannon in his original paper
[238]. He returned to it and dealt with it exhaustively in his 1959 paper [245],
which proved the first rate distortion theorem. Meanwhile, Kolmogorov and his
school in the Soviet Union began to develop rate distortion theory in 1956.
Stronger versions of the rate-distortion theorem have been proved for more
general sources in the comprehensive book by Berger [27].

HISTORXAL

NOTES

373

The inverse water-filling solution for the rate-distortion function for parallel
Gaussian sources was established by McDonald and Schultheiss [190]. An iterative algorithm for the calculation of the rate distortion function for a general i.i.d.
source and arbitrary distortion measure was described by Blahut [37] and
Arimoto [ll] and Csiszar [79]. This algorithm is a special case of general
alternating minimization algorithm due to Csiszar and Tusnady [85].

Elements of Information Theory
Thomas M. Cover, Joy A. Thomas
Copyright  1991 John Wiley & Sons, Inc.
Print ISBN 0-471-06259-6 Online ISBN 0-471-20061-1

Chapter 14

---

## Chapter 14: Network Information Theory (full)

Chapter 14

Network

Information

Theory

A system with many senders and receivers contains many new elements
in the communication
problem: interference,
cooperation and feedback.
These are the issues that are the domain of network information
theory.
The general problem is easy to state. Given many senders and receivers
and a channel transition
matrix which describes the effects of the
interference
and the noise in the network, decide whether or not the
sources can be transmitted
over the channel. This problem involves
distributed
source coding (data compression)
as well as distributed
communication
(finding the capacity region of the network). This general problem has not yet been solved, so we consider various special cases
in this chapter.
Examples of large communication
networks include computer networks, satellite networks and the phone system. Even within a single
computer,
there are various components
that talk to each other. A
complete theory of network information
would have wide implications
for the design of communication
and computer networks.
with a common satelSuppose that m stations wish to communicate
lite over a common channel, as shown in Figure 14.1. This is known as a
multiple
access channel. How do the various senders cooperate with
each other to send information
to the receiver? What rates of communication are simultaneously
achievable? What limitations
does interference among the senders put on the total rate of communication?
This is
the best understood multi-user
channel, and the above questions have
satisfying answers.
In contrast, we can reverse the network and consider one TV station
sending information
to m TV receivers, as in Figure 14.2. How does the
sender encode information
meant for different receivers in a common
374

NETWORK

lNFORh4ATION

375

THEORY

Figure 14.1. A multiple

access channel.

signal? What are the rates at which information
can be sent to the
different receivers? For this channel, the answers are known only in
special cases.
There are other channels such as the relay channel (where there is
one source and one destination,
but one or more intermediate
senderreceiver pairs that act as relays to facilitate the communication
between
the source and the destination),
the interference channel (two senders
and two receivers with crosstalk) or the two-way channel (two senderreceiver pairs sending information
to each other). For all these channels,
we only have some of the answers to questions about achievable communication
rates and the appropriate
coding strategies.
All these channels can be considered special cases of a general
communication
network that consists of m nodes trying to communicate
with each other, as shown in Figure 14.3. At each instant of time, the
ith node sends a symbol xi that depends on the messages that it wants
to send and on past received symbols at the node. The simultaneous
transmission
of the symbols (xl, x2, . . . , X, ) results in random received
symbols (Y, , Yz, . . . , Y, ) drawn according to the conditional
probability
distribution
p( y”’ yt2’
y’“‘lP,
d2), . . . , xcm)). Here p( - 1. ) expresses
the effects of the noise and interference present in the network. If p( 1. )
takes on only the values 0 and 1, the network is deterministic.
Associated with some of the nodes in the network are stochastic data
sources, which are to be communicated
to some of the other nodes in the
network. If the sources are independent,
the messages sent by the nodes
l

Figure 14.2. A broadcast channel.

NETWORK

376

Figure 14.3. A communication

ZNFORMATION

THEORY

network.

are also independent.
However, for full generality,
we must allow the
sources to be dependent. How does one take advantage of the dependence to reduce the amount of information
transmitted?
Given the
probability
distribution
of the sources and the channel transition
function, can one transmit these sources over the channel and recover the
sources at the destinations
with the appropriate
distortion?
We consider various special cases of network communication.
We
consider the problem of source coding when the channels are noiseless
and without interference. In such cases, the problem reduces to finding
the set of rates associated with each source such that the required
sources can be decoded at the destination
with low probability
of error
(or appropriate
distortion).
The simplest case for distributed
source
coding is the Slepian-Wolf
source coding problem, where we have two
sources which must be encoded separately, but decoded together at a
common node. We consider extensions to this theory when only one of
the two sources needs to be recovered at the destination.
The theory of flow in networks has satisfying answers in domains like
circuit theory and the flow of water in pipes. For example, for the
single-source
single-sink
network of pipes shown in Figure 14.4, the
maximum
flow from A to B can be easily computed from the FordFulkerson theorem. Assume that the edges have capacities Ci as shown.
Clearly, the maximum
flow across any cut-set cannot be greater than

<=D
Cl

A

B

c3

c2

C = min(C1

c4

c5

+ C,, C2 + C, + C,, C, + C,, C, + C, + C,)

Figure 14.4. Network

of water pipes.

14.1

GAUSSIAN MULTPLE

USER CHANNELS

377

the sum of the capacities of the cut edges. Thus minimizing
the
maximum
flow across cut-sets yields an upper bound on the capacity of
the network. The Ford-Fulkerson
[113] theorem shows that this capacity can be achieved.
The theory of information
flow in networks does not have the same
simple answers as the theory of flow of water in pipes. Although we
prove an upper bound on the rate of information
flow across any cut-set,
these bounds are not achievable in general. However, it is gratifying
that some problems like the relay channel and the cascade channel
admit a simple max flow min cut interpretation.
Another subtle problem
in the search for a general theory is the absence of a source-channel
separation theorem, which we will touch on briefly in the last section of
this chapter. A complete theory combining distributed
source coding and
network channel coding is still a distant goal.
In the next section, we consider Gaussian examples of some of the
basic channels of network information
theory. The physically motivated
Gaussian channel lends itself to concrete and easily interpreted
answers. Later we prove some of the basic results about joint typicality
that we use to prove the theorems of multiuser
information
theory. We
then consider various problems in detail-the
multiple
access channel,
the coding of correlated sources (Slepian-Wolf
data compression), the
broadcast channel, the relay channel, the coding of a random variable
with side information
and the rate distortion problem with side information. We end with an introduction
to the general theory of information
flow in networks. There are a number of open problems in the area, and
there does not yet exist a comprehensive
theory of information
networks. Even if such a theory is found, it may be too complex for easy
implementation.
But the theory will be able to tell communication
designers how close they are to optimality
and perhaps suggest some
means of improving
the communication
rates.

14.1

GAUSSIAN

MULTIPLE

USER CHANNELS

Gaussian multiple
user channels illustrate
some of the important
features of network information
theory. The intuition
gained in Chapter 10
on the Gaussian channel should make this section a useful introduction.
Here the key ideas for establishing
the capacity regions of the Gaussian
multiple
access, broadcast, relay and two-way channels will be given
without proof. The proofs of the coding theorems for the discrete
memoryless
counterparts
to these theorems will be given in later
sections of this chapter.
The basic discrete time additive white Gaussian noise channel with
input power P and noise variance N is modeled by

NETWORK

378

Yi=Xi

1NFORMATlON

i-1,2,...

+Zi,

THEORY

(14.1)

where the Zi are i.i.d. Gaussian random variables with mean 0 and
variance N. The signal X = (X1, X,, . . . , Xn) has a power constraint
(14.2)
The Shannon capacity C is obtained by maximizing
1(X, Y) over all
random variables X such that EX2 5 P, and is given (Chapter 10) by
1
C = 2 log

(14.3)

In this chapter we will restrict our attention to discrete-time
memoryless channels; the results can be extended to continuous time Gaussian
channels.
14.1.1 Single

User Gaussian

Channel

We first review the single user Gaussian channel studied in Chapter 10.
Here Y = X + 2. Choose a rate R < $ log(l + 5 ). Fix a good ( 2nR, n)
codebook of power P. Choose an index i in the set 2nR. Send the ith
codeword X(i) from the codebook generated above. The receiver observes
Y = X( i ) + Z and then finds the index i of the closest codeword to Y. If n
is sufficiently large, the probability
of error Pr(i # i> will be arbitrarily
small. As can be seen from the definition
of joint typicality,
this
minimum
distance decoding scheme is essentially equivalent to finding
the codeword in the codebook that is jointly typical with the received
vector Y.
14.1.2 The Gaussian
We consider

Multiple

Access Channel

m transmitters,

with m Users

each with a power P. Let
Y=~X,+z.

(14.4)

i=l

Let

C(N)
-P

P
1
= z log 1 + N
(
>

(14.5)

denote the capacity of a single user Gaussian channel with signal to
noise ratio PIN. The achievable rate region for the Gaussian channel
takes on the simple form given in the following equations:

14.1

GAUSSIAN

MULTIPLE

USER

379

CHANNELS

(14.7)
(14.8)
.
.

(14.9)
(14.10)

Note that when all the rates are the same, the last inequality dominates
the others.
Here we need m codebooks, the ith codebook having 2nRi codewords of
power P. Transmission
is simple. Each of the independent
transmitters
chooses an arbitrary codeword from its own codebook. The users simultaneously send these vectors. The receiver sees these codewords added
together with the Gaussian noise 2.
Optimal
decoding consists of looking for the m codewords, one from
each codebook, such that the vector sum is closest to Y in Euclidean
distance. If (R,, R,, . . . , R,) is in the capacity region given above, then
the probability
of error goes to 0 as n tends to infinity.
Remarks:
It is exciting to see in this problem that the sum of the
rates of the users C(mPIN)
goes to infinity with m. Thus in a cocktail
party with m celebrants of power P in the presence of ambient noise N,
the intended listener receives an unbounded amount of information
as
the number of people grows to infinity. A similar conclusion holds, of
course, for ground communications
to a satellite.
It is also interesting
to note that the optimal transmission
scheme
here does not involve time division multiplexing.
In fact, each of the
transmitters
uses all of the bandwidth all of the time.
14.1.3 The Gaussian

Broadcast

Channel

Here we assume that we have a sender of power P and two distant
receivers, one with Gaussian noise power & and the other with Gaussian noise power N2. Without loss of generality,
assume N1 < N,. Thus
receiver Y1 is less noisy than receiver Yz. The model for the channel is
Y1 = X + 2, and YZ = X + Z,, where 2, and 2, are arbitrarily
correlated
Gaussian random variables with variances & and N,, respectively. The
sender wishes to send independent
messages at rates R, and R, to
receivers Y1 and YZ, respectively.
Fortunately,
all Gaussian broadcast channels belong to the class of
degraded broadcast channels discussed in Section 14.6.2. Specializing
that work, we find that the capacity region of the Gaussian broadcast
channel is

380

NETWORK

INFORMATION

THEORY

(14.11)
(14.12)
where a! may be arbitrarily
chosen (0 5 a! 5 1) to trade off rate R, for
wishes.
rate R, as the transmitter
To encode the messages, the transmitter
generates two codebooks,
at
one with power aP at rate R,, and another codebook with power CUP
rate R,, where R, and R, lie in the capacity region above. Then to send
an index i E {1,2, . . . , 2nR1} andj E {1,2, . . . , 2nR2} to YI and Y2, respectively, the transmitter
takes the codeword X( i ) from the first codebook
and codeword X(j) from the second codebook and computes the sum. He
sends the sum over the channel.
The receivers must now decode their messages. First consider the bad
receiver YZ. He merely looks through the second codebook to find the
closest codeword to the received vector Y,. His effective signal to noise
CUP+ IV,), since YI’s message acts as noise to YZ. (This can
ratio is CUP/(
be proved.)
The good receiver YI first decodes Yz’s codeword, which he can
accomplish because of his lower noise NI. He subtracts this codeword X,
from HI. He then looks for the codeword in the first codebook closest to
Y 1 - X,. The resulting
probability
of error can be made as low as
desired.
A nice dividend of optimal encoding for degraded broadcast channels
is that the better receiver YI always knows the message intended for
receiver YZ in addition to the message intended for himself.
14.1.4 The Gaussian

Relay Channel

For the relay channel, we have a sender X and an ultimate
intended
receiver Y. Also present is the relay channel intended solely to help the
receiver. The Gaussian relay channel (Figure 14.30) is given by
Y,=X+Z,,

(14.13)

Y=X+Z,+X,+Z,,

(14.14)

where 2, and 2, are independent
zero mean Gaussian random variables
with variance A$ and N,, respectively.
The allowed encoding by the
relay is the causal sequence

The sender X has power P and sender XI has power P,. The capacity

is

14.1

GAUSSIAN

MULTIPLE

USER

C = gyyc min

381

CHANNELS

’ + ;l+;NF),

C(g)}

,

(14.16)

where Z = 1 - CL Note that if
(14.17)
it can be seen that C = C(P/N,),which
is achieved by a! = 1. The channel
appears to be noise-free after the relay, and the capacity C(P/N, ) from X
to the relay can be achieved. Thus the rate C(PI(N, + N,)) without the relay is increased by the presence of the relay to C(P/N,).
For
large N2, and for PI/N, 2 PIN,, we see that the increment
in rate is
from C(P/(N, + N,)) = 0 to C(P/N, ).
Let R, < C(aP/N,).
Two codebooks are needed. The first codebook has
ZnR1 words of power aP The second has 2nRo codewords of power CUP We
shall use codewords from these codebooks successively in order to create
the opportunity
for cooperation
by the relay. We start by sending a
codeword from the first codebook. The relay now knows the index of this
codeword since R, < C( aPIN,),
but the intended receiver has a list of
possible codewords of size 2n(R1-C((UP’(N1+N2? This list calculation
involves a result on list codes.
In the next block, the transmitter
and the relay wish to cooperate to
resolve the receiver’s uncertainty
about the previously sent codeword on
the receiver’s list. Unfortunately,
they cannot be sure what this list is
because they do not know the received signal Y. Thus they randomly
partition
the first codebook into 2nRo cells with an equal number of
codewords in each cell. The relay, the receiver, and the transmitter
agree on this partition.
The relay and the transmitter
find the cell of the
partition in which the codeword from the first codebook lies and cooperatively send the codeword from the second codebook with that index.
That is, both X and X1 send the same designated codeword. The relay, of
course, must scale this codeword so that it meets his power constraint
P,. They now simultaneously
transmit
their codewords. An important
point to note here is that the cooperative information
sent by the relay
and the transmitter
is sent coherently. So the power of the sum as seen
by the receiver Y is <V% + fl)‘.
However, this does not exhaust what the transmitter
does in the
second block. He also chooses a fresh codeword from the first codebook,
adds it “on paper” to the cooperative
codeword from the second
codebook, and sends the sum over the channel.
The reception by the ultimate
receiver Y in the second block involves
first finding the cooperative index from the second codebook by looking
for the closest codeword in the second codebook. He subtracts the
codeword from the received sequence, and then calculates a list of

382

NETWORK

INFORMATION

THEORY

indices of size ZnRo corresponding
to all codewords of the first codebook
that might have been sent in the second block.
Now it is time for the intended receiver to complete computing the
codeword from the first codebook sent in the first block. He takes his list
of possible codewords that might have been sent in the first block and
intersects it with the cell of the partition that he has learned from the
cooperative
relay transmission
in the second block, The rates and
powers have been chosen so that it is highly probable that there is only
one codeword in the intersection. This is Y’s guess about the information
sent in the first block.
We are now in steady state. In each new block, the transmitter
and
the relay cooperate to resolve the list uncertainty
from the previous
block. In addition, the transmitter
superimposes some fresh information
from his first codebook to this transmission
from the second codebook
and transmits
the sum.
The receiver is always one block behind, but for sufficiently many
blocks, this does not affect his overall rate of reception.
14.1.5 The Gaussian

Interference

Channel

The interference channel has two senders and two receivers. Sender 1
wishes to send information
to receiver 1. He does not care what receiver
2 receives or understands.
Similarly
with sender 2 and receiver 2. Each
channel interferes with the other. This channel is illustrated
in Figure
14.5. It is not quite a broadcast channel since there is only one intended
receiver for each sender, nor is it a multiple access channel because each
receiver is only interested in what is being sent by the corresponding
transmitter.
For symmetric interference, we have
Y~=x,+ax~+z,

(14.18)

Yz=x,+ax~+z,,

(14.19)

where Z,, 2, are independent

J(O, N) random

Figure 14.5. The Gaussian interference

variables.

channel.

This channel

14.1

GAUSSIAN

MULTIPLE

USER

CHANNELS

383

has not been solved in general even in the Gaussian case. But remarkably, in the case of high interference, it can be shown that the capacity
region of this channel is the same as if there were no interference
whatsoever.
To achieve this, generate two codebooks, each with power P and rate
WIN).
Each sender independently
chooses a word from his book and
sends it. Now, if the interference a satisfies C(a2P/(P + N)) > C(P/N),
the first transmitter
perfectly understands
the index of the second
transmitter.
He finds it by the usual technique of looking for the closest
codeword to his received signal. Once he finds this signal, he subtracts it
from his received waveform. Now there is a clean channel between him
and his sender. He then searches the sender’s codebook to find the
closest codeword and declares that codeword to be the one sent.
14.1.6. The Gaussian

Two-Way

Channel

The two-way channel is very similar to the interference channel, with
the additional
provision that sender 1 is attached to receiver 2 and
sender 2 is attached to receiver 1 as shown in Figure 14.6. Hence,
sender 1 can use information
from previous received symbols of receiver
2 to decide what to send next. This channel introduces another fundamental aspect of network information
theory, namely, feedback. Feedback enables the senders to use the partial information
that each has
about the other’s message to cooperate with each other.
The capacity region of the two-way channel is not known in general.
This channel was first considered by Shannon 12461, who derived upper
and lower bounds on the region. (See Problem 15 at the end of this
chapter.) For Gaussian channels, these two bounds coincide and the
capacity region is known; in fact, the Gaussian two-way channel decomposes into two independent
channels.
Let P, and P2 be the powers of transmitters
1 and 2 respectively and
let N1 and N, be the noise variances of the two channels. Then the rates
R, c C(P,IN,)
and R, < C(P,IN,)
can be achieved by the techniques
described for the interference
channel. In this case, we generate two
codebooks of rates R, and R,. Sender 1 sends a codeword from the first
codebook. Receiver 2 receives the sum of the codewords sent by the two
senders plus some noise. He simply subtracts out the codeword of sender

Figure 14.6. The two-way channel.

NETWORK

384

INFORMATION

THEORY

2 and he has a clean channel from sender 1 (with only the noise of
variance NJ Hence the two-way Gaussian channel decomposes into two
independent
Gaussian channels. But this is not the case for the general
two-way channel; in general there is a trade-off between the two senders
so that both of them cannot send at the optimal rate at the same
time.

14.2 JOINTLY

TYPICAL

SEQUENCES

We have previewed the capacity results for networks by considering
multi-user
Gaussian channels. We will begin a more detailed analysis in
this section, where we extend the joint AEP proved in Chapter 8 to a
form that we will use to prove the theorems of network information
theory. The joint AEP will enable us to calculate the probability
of error
for jointly typical decoding for the various coding schemes considered in
this chapter.
Let (X1,X,, . . . , X, ) denote a finite collection of discrete random
distribution,
p(x,, x2, . . . , xk ),
variables
with
some fixed joint
Xk)
E
2rl
x
2iti2
x
*
*
x
zt$.
Let
5’
denote
an
ordered sub(Xl, x2, ’ * * 9
set of these random variables and consider n independent
copies of S.
Thus
Pr{S = s} = fi Pr{S,

= si},

SET.

(14.20)

xl)}

(14.21)

i=l

For example,

if S = (Xj, X, ), then
Pr{S = S} = Pr((Xj,

Xi) = txj9

=

(14.22)
i=l

To be explicit, we will sometimes use X(S) for S. By the law of large
numbers, for any subset S of random variables,
1

- ; log p(S,, s,, * * * , s,)=

-;

8 logp(S,)-+H(S),
i

where the convergence takes place simultaneously
all 2K subsets, S c {X,, X2, . . . , X,}.
Definition:
defined by

The

set A:’

of E-typical

(14.23)

1

with probability

n-sequences

1 for

(x1, x2,. . . , xK) is

14.2

JOlNTLY

AI”‘(X,,X,,

385

TYPICAL SEQUENCES

. . . ,X,>

= A’:’
= (x1, x2,
{

.

*

l

,

x,1:

- ; logp(s)-H(S)

<E,

VSc{x,,&,...,

Let A:‘(S) denote the restriction
if S = (X,, X2>, we have
A:‘(X,,

xd &

(14.24)

’

of A:’ to the coordinates

of S. Thus

X2> = {(xl, x2):
- ;logP(x,,x,)-M&X,)

<E,

1

(14.25)

- ~logp(x,)-H(x,)
Definition:

We will use the notation
1
Floga,-b

a, 6 2n(b &a) to mean

for n sufficiently

large.

Theorem

For any E > 0, for suffkiently

1.

14.2.1:

VSc{X,,X,

P(A’,“‘(S))~~-E,

2.

s E A:)(S)

3.

IAl”’

4. Let s,, s, c {X1,X2,.

large n,
,...,

X,}.

(14.27)

+, &) & 2-n(H(S)-ce),

(14.28)

& 2dH(S)-C24.

(14.29)

. . ,x,}.
&I

(14.26)

<E

If (s,, s2EA:)(S1,

I*,> & 2-~(~(S&wd

S,), then

.

(14.30)

Proof:
1. This follows from the law of large numbers
ables in the definition of A’“‘(S)
.
c

for the random

vari-

NETWORK lNFORMA7’ZON

386

2. This follows directly
3. This follows from

from the definition

THEORY

of A:‘(S).

(14.31)

I

2 -n(H(S)+c)

c
BEA:’

= IA~‘(S)(2-“‘H’S””

If n is sufficiently

(14.32)

(S 1

.

(14.33)

large, we can argue that
l-ES

c

p(s)

(14.34)

yam-c)

(14.35)

IWEA~‘(S)
I

c
wzA~‘(S)

= (@‘($)(2-“‘H’S’-”

.

(14.36)

Combining
(14.33) and (14.36), we have IAy’(S>l A 2n(H(S)r2c) for
sufficiently large n.
4. For (sl, s2) E A:‘(&,
S,), we have p(sl)k 2-ncHcs1)f’) and p(s,, s,)
-‘2- nwq, S2kB). Hence
P(S2lSl)

=

P(Sl9
p(s

82)
)
1

&2-n(H(SzlS1)k2E)

The next theorem bounds the number
quences for a given typical sequence.

.

r-J

of conditionally

(14.37)
typical

se-

Theorem
14.2.2: Let S,, S, be two subsets of Xl, X2,. . . ,X,. For any
to be the set of s, sequences that are jointly
E > 0, define Ar’(S,Is,)
e-typical with a particular
s, sequence. If s, E A:‘@,),
then for sufficiently large n, we have
IAl”‘(Sl(s2)l

5

2n(H(S11S2)+2e)

,

(14.38)

and
(l-

E)2 nwc3~JS+-2c)
5 2 pb3,)~4%,

Is4 .

82

Proof:

As in part 3 of the previous

theorem, we have

(14.39)

14.2

JOINTLY

7YPZCAL

387

SEQUENCES

12

c

(14.40)

P(SIb2)

a,~A~+S,ls~)

= IA~)(Slls2)12-~'H'S11S2'+2~'.

If n is sufficiently

(14.42)

large, then we can argue from (14.27) that

1 - E 5 c p(s2)
82

c

P(SIlS2)

(14.43)

2-~(5wl~2)-2~)

(14.44)

q~Af%~l~~)

Ic

p(s2)
82

c
q~Af%~le,)

= 2 p(s2)lA33,

ls2)12-n’n’S1(S2’-2” .

0

(14.45)

82

To calculate the probability
of decoding error, we need to know the
probability
that conditionally
independent
sequences are jointly typical.
Let S,, S, and S, be three subsets of {X1,X2,. . . ,X,). If S; and Sg are
conditionally
independent
given SA but otherwise share the same pairwise marginals
of (S,, S,, S,), we have the following probability
of joint
typicality.
Theorem
14.2.3: Let A:’ denote the typical
function p(sl, s,, sg), and let

set for the probability

mass

P(& = s,, s; = 82, s;
i=l

(14.46)

Then
p{(s;

, s;, s;> E A:)}

f @@1;

SzIS3)*6e)

.

(14.47)

Proof: We use the f notation from (14.26) to avoid calculating
upper and lower bounds separately. We have
P{(S;,

S;, S;>EA~‘}

= c
(q I s2,

P(~3)P(~11~3)P(~21~3)

(14.48)

e3EAy)

A

the

,@Z’(S,,

s,,

s3)12-“(H(S~)~~)2-n(Htslls3)‘2.)2-n(H(SalS3)’2.) (14.49)

388

NETWORK

22 -n(Z(Sl;

S2IS3)*6a)

.

ZNFORMATION

THEORY

(14.51)

Cl

We will specialize this theorem to particular
choices of S,, S, and S,
for the various achievability
proofs in this chapter.

14.3

THE MULTIPLE

ACCESS CHANNEL

The first channel that we examine in detail is the multiple
access
channel, in which two (or more) senders send information
to a common
receiver. The channel is illustrated
in Figure 14.7.
A common example of this channel is a satellite receiver with many
independent
ground stations. We see that the senders must contend not
only with the receiver noise but with interference from each other as
well.
A discrete memoryless multiple
access channel consists of
transition
matrix
alphabets,
&, E2 and 91, and a probability

Definition:

three
P(Yh

x2).

access channel
A ((2nR1, 2nR2 ), n) code for the multiple
consists of two sets of integers
w/; = {1,2, . . . , 2nR1} and ‘IV2 =
(1, 2,. . . , 2nR2) called the message sets, two encoding functions,

Definition:

X/wl-+~~,
x2 : w2+

and a decoding

(14.52)

CY;

(14.53)

function
g:w44”,x

Figure

14.7.

The

multiple

w2.

access channel.

(14.54)

14.3

THE MULTlPLE

ACCESS

389

CHANNEL

There are two senders and one receiver for this channel. Sender 1
chooses an index WI uniformly
from the set { 1,2, . . . , 2nRl} and sends
the corresponding
codeword over the channel. Sender 2 does likewise.
Assuming that the distribution
of messages over the product set W; x
‘I& is uniform, i.e., the messages are independent
and equally likely, we
define the average probability
of error for the ((2nRl, 2”R2), n) code as
follows:
p(n)
e

=

1
2 n(RI+R2)

c

Pr{gW”) + b,, w,$w,, Q> sent} .

(WI, W2EWlXW2

(14.55)
Definition:
A rate pair (RI, R,) is said to be achievable for the multiple
access channel if there exists a sequence of ((2”R1, ZnR2), n) codes with
P%’ + 0.
Definition:
The capacity region of the multiple
access channel
closure of the set of achievable (RI, R,) rate pairs.

is the

An example of the capacity region for a multiple
access channel
illustrated
in Figure 14.8.
We first state the capacity region in the form of a theorem.

is

14.3.1 (Multiple
access channel capacity): The capacity of a
multiple
access channel (SE”,x 2&, p( yIxl, x2), 3) is the closure of the
convex hull of all (RI, R,) satisfying
Theorem

R, < I(x,; YIX,) ,

(14.56)

R,<I(X,;

(14.57)

YIX,),

Figure 14.8. Capacity region for a multiple

access channel.

390

NETWORK

R, +R,<I(X,,X,;
for some product

distribution

ZNFORMATlON

Y)

p1(x1)p2(x2)

THEORY

(14.58)
on %I X E’..

Before we prove that this is the capacity region of the multiple
access
channel, let us consider a few examples of multiple
access channels:
14.3.1 (Independent
binary symmetric
channels): Assume
that we have two independent
binary symmetric
channels, one from
sender 1 and the other from sender 2, as shown in Figure 14.9.
In this case, it is obvious from the results of Chapter 8 that we can
send at rate 1 - H( pJ over the first channel and at rate 1 - H( pz ) over
the second channel. Since the channels are independent,
there is no
interference
between the senders. The capacity region in this case is
shown in Figure 14.10.

Example

Example

(Binary multiplier
channel):
with binary inputs and output

Consider

14.3.2

cess channel

Y=X,X,.

a multiple

ac-

(14.59)

Such a channel is called a binary multiplier
channel. It is easy to see
that by setting X2 = 1, we can send at a rate of 1 bit per transmission
from sender 1 to the receiver. Similarly,
setting X1 = 1, we can achieve
R, = 1. Clearly, since the output is binary, the combined rates R, + R, of

0
Xl

1

0

1
Y
0’

0

1’

x2

1

Figure 14.9. Independent

binary symmetric channels.

14.3

THE MULTIPLE

ACCESS

391

CHANNEL

A

R2

C,=l-H(p3

0

R,

C, = 1 -H@,)

Figure 14.10. Capacity region for independent

BSC’s.

sender 1 and sender 2 cannot be more than 1 bit. By timesharing,
we
can achieve any combination
of rates such that R, + R, = 1. Hence the
capacity region is as shown in Figure 14.11.
14.3.3 (Binary erasure multiple
access channel ): This multiple access channel has binary inputs, EI = %s = (0, 1) and a ternary
output Y = XI + X,. There is no ambiguity in (XI, Xz> if Y = 0 or Y = 2 is
received; but Y = 1 can result from either (0,l) or (1,O).
We now examine the achievable rates on the axes. Setting X, = 0, we
can send at a rate of 1 bit per transmission
from sender 1. Similarly,
setting XI = 0, we can send at a rate R, = 1. This gives us two extreme
points of the capacity region.
Can we do better? Let us assume that R, = 1, so that the codewords of
XI must include all possible binary sequences; XI would look like a
Example

c,=

1

0

C,=l

Figure 14.11. Capacity region for binary multiplier

/
R,

channel.

NETWORK lNFORh4ATlON

392

Figure 14.12.
channel.

Equivalent

THEORY

single user channel for user 2 of a binary erasure multiple access

Bernoulli( fr ) process. This acts like noise for the transmission
from X,.
For X,, the channel looks like the channel in Figure 14.12.
This is the binary erasure channel of Chapter 8. Recalling the results,
the capacity of this channel is & bit per transmission.
Hence when sending at maximum
rate 1 for sender 1, we can send an
additional
8 bit from sender 2. Later on, after deriving the capacity
region, we can verify that these rates are the best that can be achieved.
The capacity region for a binary erasure channel is illustrated
in
Figure 14.13.

0

I
1

z
Figure 14.13.

C,=l

R,

Capacity region for binary erasure multiple

access channel.

14.3

THE MULTlPLE

ACCESS

14.3.1 Achievability
Channel

393

CHANNEL

of the Capacity

Region

for the Multiple

Access

We now prove the achievability
of the rate region in Theorem 14.3.1; the
proof of the converse will be left until the next section. The proof of
achievability
is very similar to the proof for the single user channel. We
will therefore only emphasize the points at which the proof differs from
the single user case. We will begin by proving the achievability
of rate
pairs that satisfy (14.58) for some fixed product distribution
p(Q(x&
In Section 14.3.3, we will extend this to prove that all points in the
convex hull of (14.58) are achievable.
Proof

(Achievability

in Theorem

14.3.1):

Fixp(z,,

x,) =pl(x,)p&).

Codebook generation.
Generate 2nR1 independent
codewords X,(i 1,
i E {1,2,. . . , 2nR1}, of length n, generating
each element
i.i.d.
- Ily= 1 p1 (Eli ). Similarly,
generate 2nR2 independent
codewords
X,(j),
j E { 1,2, . . . , 2nR2}, generating
each
element
i.i.d.
- IlyE, p2(~2i). These codewords form the codebook, which is revealed to the senders and the receiver.
Encoding.
To send index i, sender 1 sends the codeword X,(i).
Similarly,
to send j, sender 2 sends X,(j).
Decoding. Let A:’ denote the set of typical (x1, x,, y) sequences. The
receiver Y” chooses the pair (i, j) such that

(q(i 1,x2(j), y) E A:’

(14.60)

if such a pair (6 j) exists and is unique; otherwise, an error is
declared.
Analysis of the probability
of error. By the symmetry of the random
code construction,
the conditional
probability
of error does not
depend on which pair of indices is sent. Thus the conditional
probability
of error is the same as the unconditional
probability
of
error. So, without loss of generality,
we can assume that (i, j) =
(1,l) was sent.
We have an error if either the correct codewords are not typical with
the received sequence or there is a pair of incorrect codewords that are
typical with the received sequence. Define the events
E, = {O&G ), X2( j>, Y) E A:'}
Then by the union

of events bound,

.

394

NETWORK

sP(E”,,)

+

C
iZ1,

p(E,l)

+

j=l

2
i=l,

P(Elj)

ZNFORMATlON

+

j#l

C
i#l,

P(E,)

THEORY

9 (14.63)

j#l

where P is the conditional
probability
given that (1, 1) was sent. From
the AEP, P(E",,)+O.
By Theorem 14.2.1 and Theorem 14.2.3, for i # 1, we have

RE,,) = R(X,W, X,(l), W EA:‘)

= c
(Xl , x2,

(14.64)

P(X,
)P(x,,
Y)

(14.65)

s IAS"' -nu-z(X,)-c)
2- nmx2, Y)-cl

(14.66)

52 -n(H(X1)+H(X,,YbH(Xp

(14.67)

y)eA:)

x2, Y)-SC)

=2- n(Z(X1; x2,Y)-36)
=2-

n(Z(X,;

since Xl and Xz are independent,
ml; YIX,) = 1(X1; YIX,).
Similarly,
for j # 1,

(14.68)

Y’1X2)-3613

(14.69)

9

and therefore 1(X1 ; X,, Y) = 1(X1; X,) +

(14.70)
and for i f 1, j # 1,

P(E,)12-

n(Z(X1,

x2; Y)-4c)

.

(14.71)

It follows that
pp’

I

p(E;,)

+

2”Rq-d1(x~; yIx2)-3C) c-J”+J-““‘~~; YiXl)-3e)

+2 n(R1+R2,pzwl,X2;

+

Y)-4e)

.

(14.72)

Since E > 0 is arbitrary, the conditions of the theorem imply that each
term tends to 0 as n + 00.
The above bound shows that the average probability
of error, averaged over all choices of codebooks in the random code construction,
is
arbitrarily
small. Hence there exists at least one code %* with arbitrarily small probability
of error.
This completes the proof of achievability
of the region in (14.58) for a
fixed input distribution.
Later, in Section 14.3.3, we will show that

14.3

THE MULTZPLE

timesharing
completing

ACCESS

395

CHANNEL

allows any (R,, R,) in the convex hull to be achieved,
the proof of the forward part of the theorem.
0

14.3.2 Comments
Channel

on the Capacity

Region

for the Multiple

Access

We have now proved the achievability
of the capacity region of the
multiple
access channel, which is the closure of the convex hull of the
set of points (R,, R2) satisfying

R, < I(x,; YIX,) ,

(14.73)

R, < I(&; Y(x,) ,

(14.74)

R, + R,<I(X,,X,;

Y)

(14.75)

for some distribution
pI(xI)p2(x2)
on ZEI x ZQ.
For a particularp,(x,)p,(~),
the region is illustrated
in Figure 14.14.
Let us now interpret
the corner points in the region. The point A
corresponds to the maximum
rate achievable from sender 1 to the
receiver when sender 2 is not sending any information.
This is

Now for any distribution

p&

)p2&),

I(X1;Y(X,) = ; p&M&;

YIX,= x2)

5 rnzy 1(X1; YIX, = xa 1,

A

I
0

Figure 14.14.Achievable

4x,;

region of multiple

r)

4x,;

Y/X2)

(14.77)
(14.78)

/
R,

access channel for a fixed input distribution.

NETWORK

396

INFORMATION

THEORY

since the average is less than the maximum.
Therefore, the maximum
in
(14.76) is attained when we set X, =x2, where x, is the value that
maximizes
the conditional
mutual information
between X1 and Y. The
distribution
of X1 is chosen to maximize this mutual information.
Thus
X, must facilitate the transmission
of X, by setting X, = x2.
The point B corresponds to the maximum
rate at which sender 2 can
send as long as sender 1 sends at his maximum
rate. This is the rate
that is obtained if X1 is considered as noise for the channel from X, to Y.
In this case, using the results from single user channels, X, can send at
a rate I(x,; Y). The receiver now knows which X, codeword was used
and can “subtract” its effect from the channel. We can consider the
channel now to be an indexed set of single user channels, where the
index is the X, symbol used. The X1 rate achieved in this case is the
average mutual information,
where the average is over these channels,
and each channel occurs as many times as the corresponding X, symbol
appears in the codewords. Hence the rate achieved is
(14.79)
The points C and D correspond to B and A respectively with the roles of
the senders reversed.
The non-corner points can be achieved by timesharing.
Thus, we have
given a single user interpretation
and justification
for the capacity
region of a multiple
access channel.
The idea of considering other signals as part of the noise, decoding
one signal and then “subtracting”
it from the received signal is a very
useful one. We will come across the same concept again in the capacity
calculations
for the degraded broadcast channel.
14.3.3 Convexity
Channel

of the Capacity

Region

of the Multiple

Access

We now recast the capacity region of the multiple
access channel in
order to take into account the operation of taking the convex hull by
introducing
a new random variable. We begin by proving that the
capacity region is convex.
Theorem
14.3.2: The capacity region % of a multiple
convex, i.e., if (R,,R,)E%
and (R;,Ri)E%,
then
hR,+(l-h)R;)EceforOsA~l.

access channel
(hR,+(l-A)R;,

is

Proof: The idea is timesharing.
Given two sequences of codes at
different rates R = (RI, R,) and R’ = (R; , R;1), we can construct a third
codebook at a rate AR + (1 - h)R’ by using the first codebook for the first
An symbols and using the second codebook for the last (1 - A)n symbols.
The number of X1 codewords in the new code is

14.3

THE MULTlPLE

ACCESS

397

CHANNEL

2 n%2

n(l-h)R{

= 2n(AR1+(1-h)Ri)

(14.80)

and hence the rate of the new code is AR + (1 - A)R’. Since the overall
probability
of error is less than the sum of the probabilities
of error for
each of the segments, the probability
of error of the new code goes to 0
q
and the rate is achievable.
We will now recast the statement
of the capacity region for the
multiple
access channel using a timesharing
random variable Q.
Theorem
14.3.3: The set of achievable rates of a discrete memoryless
multiple
access channel is given by the closure of the set of all (R,, R,)
pairs satisfying

R,<I(X,;

YIX,, &I,

R, +R,-W&,X,;

Y)&)

for some choice of the joint
with IS I 5 4.

distribution

p(~)p(~~~q)p(~~lq)p(yl.r:,,

(14.81)
x2)

Proof: We will show that every rate pair lying in the region in the
theorem is achievable, i.e., it lies in the convex closure of the rate pairs
satisfying Theorem 14.3.1. We will also show that every point in the
convex closure of the region in Theorem 14.3.1 is also in the region
defined in (14.81).
Consider a rate point R satisfying the inequalities
(14.81) of the
theorem. We can rewrite the right hand side of the first inequality
as

ml; YIX,, &I = it p(q)l(x,;

YIX,, Q = d

(14.82)

k=l

(14.83)
k=l

where m is the cardinality
of the support set of Q. We can similarly
expand the other mutual informations
in the same way.
For simplicity in notation, we will consider a rate pair as a vector and
denote a pair satisfying the inequalities
in (14.58) for a specific input
product distributionp19(~,)p,,(x,)
as R,. Specifically, let R, = CR,,, Rz,)
be a rate pair satisfying
(14.84)
(14.85)

NETWORK

398

ZNFORMATZON

THEORY

Then by Theorem 14.3.1, R, = (RIP, R,,) is achievable,
Then since R satisfies (14.81), and we can expand the right hand
sides as in (14.83), there exists a set of pairs R, satisfying (14.86) such
that

R =qtl p(q)R,.

(14.87)

Since a convex combination
of achievable rates is achievable, so is R.
Hence we have proved the achievability
of the region in the theorem.
The same argument can be used to show that every point in the convex
closure of the region in (14.58) can be written as the mixture of points
satisfying (14.86) and hence can be written in the form (14.81).
The converse will be proved in the next section. The converse shows
that all achievable
rate pairs are of the form (14.81), and hence
establishes
that this is the capacity region of the multiple
access
channel.
The cardinality
bound on the time-sharing
random variable Q is a
consequence of Caratheodory’s
theorem on convex sets. See the discussion below. 0
The proof of the convexity of the capacity region shows that any
convex combination
of achievable rate pairs is also achievable. We can
continue this process, taking convex combinations
of more points. Do we
need to use an arbitrary number of points ? Will the capacity region be
increased? The following theorem says no.
Theorem
14.3.4 (Carattiodory):
Any point in the convex closure of a
connected compact set A in a d dimensional
Euclidean
space can be
represented as a convex combination
of d + 1 or fewer points in the
original set A.
Proof: The proof can be found
[127], and is omitted here. Cl

in Eggleston

[95] and Grunbaum

This theorem allows us to restrict attention to a certain finite convex
combination
when calculating the capacity region. This is an important
property because without it we would not be able to compute the
capacity region in (14.81), since we would never know whether using a
larger alphabet 2 would increase the region.
In the multiple
access channel, the bounds define a connected compact set in three dimensions.
Therefore all points in its closure can be

14.3

THE MULTIPLE

ACCESS

399

CHANNEL

defined as the convex combination
of four points. Hence, we can restrict
the cardinality
of Q to at most 4 in the above definition of the capacity
region.

14.3.4 Converse for the Multiple

Access Channel

We have so far proved the achievability
section, we will prove the converse.

of the capacity

region.

In this

Proof (Converse to Theorem 14.3.1 and Theorem 14.3.3): We must
show that given any sequence of ((2”Rl, 2nR2), n) codes with Pr’+
0, that
the rates must satisfy

R, 5 I(&; YIX,, Q),

R, +R,G&,X,;
for some choice of random
distrhtion

variable

p(q>p(xllq)p(x21q)p(yJ;lc,,

YIQ)
Q defined

(14.88)
on { 1,2,3,4}

and joint

x2)’

Fix n. Consider the given code of block length n. The joint distribution
on W; x ‘Wz x S!?yx S?t x 3” is well defined. The only randomness is due
to the random uniform choice of indices W1 and W, and the randomness
induced by the channel. The joint distribution
is

P(W1,%rX~,x;,Yn)=

72

1

-

1

1 p2

P(3GqlWI)P(X~IW2)
4 P(YiIXli, X2i)

9

(14.89)
where p(xI; I w,) is either 1 or 0 depending on whether x; = x,(w 1), the
p(xi I w2) = 1 or 0
codeword corresponding
to w 1, or not, and similarly,
according to whether xi = x2(w2) or not. The mutual informations
that
follow are calculated with respect to this distribution.
By the code construction,
it is possible to estimate ( W,, W2) from the
received sequence Y” with a low probability
of error. Hence the conditional entropy of ( W,, W2) given Y” must be small. By Fano’s inequality,
H(W,,W21Yn)an(R,+R2)PSI”‘+H(P~‘)~n~n.

(14.90)

It is clear that E + 0 as Pen’
e + 0.
Then we have”
H(W,JY”)sH(W,,

W,IY”)Qzc~,

(14.91)

NETWORK

400

H(W,lY")~H(W,,

INFORh4ATlON

w~IYn)s2En.

THEORY

(14.92)

We can now bound the rate R, as

4

= H(W,)

(14.93)

Y”)+

H(Wl(Yn)

(14.94)

Y”)+

7x,

(14.95)

5 I(Xrf(W,);

Y”) + ne,

(14.96)

= H(Xy(W,))

- H(Xq(W,)IY”)

=I(W,;
(a)

5 I(W,;
(b)

(14.97)

+ m,,

= Icx;C Wl ); Y” IX:< W,)) + nc,

(14.99)

=H(YnlX~(W,))-H(Yn(X~(Wl),X~(W,))+n~n

(14.100)

'2 H(Y"IXi(W,))-

$ H(YiIYiel,X~(Wl),X~(W,))+

ne,,

(14.101)

i=l

' H(Y"IXi( Wz))- i

H(YiIX,i,

Xzi) + ne,

(14.102)

i=l

2 i

H(YiIX”,(

Wg)) - i

i=l

' i H(YiIX,i) - i

Xzi) + ne,

(14.103)

H(YiIXli,

Xzi) + nc,

(14.104)

i=l

i=l

= i

H(Y,IX,i,

i=l

I(Xli;

yilX,i)

+ nr;, 9

(14.105)

i=l

(a) follows from Fano’s inequality,
(b) from the data processing inequality,
(c) from the fact that since WI and W, are independent,
so are Xy( Wl)
and X",(W,>, and hence H(X~(W,)~X~(W,)>= H(XI(W,)), and
H(XT( Wl)I Y", XiC W,)) 5 H(Xy( WI )I Y”) by conditioning,
(d) follows from the chain rule,
(e) from the fact that Yi depends only on Xii and Xzi by the memoryless property of the channel,
(f) from the chain rule and removing conditioning,
and
(g) follows from removing conditioning.

14.3

THE MULTZPLE

ACCESS

401

CHANNEL

Hence, we have

Similarly,

R, I L i I(xli;
n i=l

qx,i)

+ En.

(14.106)

R, I ’ ~ I(X,i;
n i=l

Yi IX~i) + ~~ .

(14.107)

we have

To bound the sum of the rates, we have
n(R, + R,) = H(W,,

(14.108)

W,>

= I(W,, wz; Y”) + H(W,, wJYn)

(14.109)

(a)
5 I(W,, Wz; Y”) + ne,

(14.110)

(b)

(14.111)

5 I(Xy( W,), Xt( W, 1; Y”) + ne,
= H(Y”) - H(Yn~X~(W,),X~(W,N
2 H(Y”)-

i

(14.112)

+ nen

H(YiIY’-l,X~(W,),X~(W,))+

ne,

(14.113)

i=l

(:’ H(Y”)

- i

H(YiIX,i,

(14.114)

Xzi) + ne,

i=l

2 i

H(Yi) - i

i=l

i=l

=

2
i=l

I(Xli,Xzi;

H(YiIXli,

(14.115)

X,i) + ne,

(14.116)

Yi) + nE ny

where
(a) follows from Fano’s inequality,
(b) from the data processing inequality,
(c) from the chain rule,
(d) from the fact that Yi depends only on Xii and X,i and is conditionally independent
of everything else, and
(e) follows from the chain rule and removing conditioning.
Hence we have
n’

(14.117)

402

NETWORK

ZNFORhdATlON

THEORY

The expressions in (14.106), (14.107) and (14.117) are the averages of
the mutual
informations
calculated at the empirical
distributions
in
column i of the codebook. We can rewrite these equations with the new
variable Q, where Q = i E { 1,2, . . . , n} with probability
A. The equations become
1 n

=

i

$
It&,;
i 1

= I&,;

Q= 9 + E n

y,Ix,,,

ySIx,,,

(14.119)
(14.120)

Q) + E,

=I(x,;yIx,,&)+~,,

(14.121)

where X1 L Xla, X, iXza and Y 2 Ye are new random variables whose
distributions
depend on Q in the same way as the distributions
of X~i,
X,i and Yi depend on i. Since W, and W, are independent,
so are X,i( W,)
and Xzi( W,), and hence

A Pr{X,,

=x,1&

= i} Pr{X,,

= LC~IQ = i} .
(14.122)

Hence, taking
converse:

the limit

as n + a, Pr’+

0, we have the following

R, 5 I&;

YIX,,

&I,

Ra’I(X,;

YIX,,

&I,

R, +R,~I(X,,X,;

YlQ>

(14.123)

for some choice of joint distribution
p( Q)J& I Q)J& I q)p( y 1x1, IX&
As in the previous section, the region is unchanged if we limit
cardinality
of 2 to 4.
This completes the proof of the converse. Cl

the

Thus the achievability
of the region of Theorem 14.3.1 was proved in
Section 14.3.1. In Section 14.3.3, we showed that every point in the
region defined by (14.88) was also achievable.
In the converse, we
showed that the region in (14.88) was the best we can do, establishing
that this is indeed the capacity region of the channel. Thus the region in

14.3

THE MULTIPLE

ACCESS

403

CHANNEL

(14.58) cannot be any larger than the region in (14.88), and this is the
capacity region of the multiple
access channel.
14.3.5 m-User

Multiple

Access Channels

We will now generalize the result derived for two senders to m senders,
m 2 2. The multiple
access channel in this case is shown in Figure
14.15.
We send independent
indices w 1, wa, . . . , w, over the channel from
the senders 1,2, . . . , m respectively. The codes, rates and achievability
are all defined in exactly the same way as the two sender case.
Let S G {1,2, . . . , m} . Let SC denote the complement
of S. Let R(S ) =
c iEs Ri, and let X(S) = {Xi : i E S}. Then we have the following theorem.
Theorem
14.35: The capacity region of the m-user multiple
access
channel is the closure of the convex hull of the rate vectors satisfying
R(S) I 1(X(S); YIX(S”))
for some product

distribution

p&,

for all S C {1,2, . . . , m}
>p&,>

(14.124)

. . . P,,&)~

Proof: The proof contains no new ideas. There are now 2” - 1 terms
in the probability
of error in the achievability
proof and an equal
number of inequalities
in the proof of the converse. Details are left to
the reader.
0
In general,

the region in (14.124)

14.3.6 Gaussian Multiple

is a beveled box.

Access Channels

We now discuss the Gaussian
in somewhat more detail.

Figure 14.15.

multiple

access channel

m-user multiple

access channel.

of Section 14.1.2

NETWORK

INFORMATION

THEORY

There are two senders, XI and X,, sending
The received signal at time i is

to the single receiver Y.

Yi = Xii + X,i + Zi )

(14.125)

where {Zi} is a sequence of independent,
identically
distributed,
zero
mean Gaussian random variables with variance N (Figure 14.16). We
will assume that there is a power constraint Pj on sender j, i.e., for each
sender, for all messages, we must have
WjE{l,2

,...,

2nR’},j=l,2.

(14.126)

Just as the proof of achievability
of channel capacity for the discrete
case (Chapter 8) was extended to the Gaussian channel (Chapter lo),
we can extend the proof the discrete multiple
access channel to the
Gaussian multiple
access channel. The converse can also be extended
similarly,
so we expect the capacity region to be the convex hull of the
set of rate pairs satisfying

R, 5 I&;

Y(&) ,

(14.127)

R, 5 I(&?; YIX,) ,

(14.128)

R, + R,s

Icx,,X,;

Y)

(14.129)

for some input distribution
f,(~, >f,(x, > satisfying
5.
Now, we can expand the mutual information
entropy, and thus

EXf 5 P, and EX: 5
in terms

ml; YJX,) = WIX,) - hW)X,,X,)

(14.130)

=h(xl+x~+Z~x~)-h(x~+x~+z~x~,x~)

Figure 14.16. Gaussian multiple

of relative

access channel.

(14.131)

14.3

THE MULTlPLE

405

ACCESS CHANNEL

=h(X,+zlx,>- h(Z(X,,x,>

(14.132)

= h(X, + zlx,> - W)

(14.133)

= h(X, + 2) - h(Z)

(14.134)

1
= h(X, + 2) - z log(271-e)N

(14.135)

1
5 2 log(2ne)(P,

+ N) - f log(27re)N

(14.136)

,

(14.137)

1
=$og

(

1+w PI

>

where (14.133) follows from the fact that 2 is independent
of XI and X,,
(14.134) from the independence of XI and X,, and (14.136) from the fact
that the normal maximizes
entropy for a given second moment. Thus
the maximizing
distribution
is XI - JV(0, P, ) and X, - A’( 0, P,) with XI
and X, independent.
This distribution
simultaneously
maximizes
the
mutual information
bounds in (14.127)-(14.129).
Definition:

We define the channel
A

C(x) =

1
z

capacity function
log(1 + x) ,

corresponding to the channel capacity of a Gaussian
with signal to noise ratio x.
Then -we write the bound on R, as

(14.138)
white noise channel

RI&).

(14.139)

R@(2),

(14.140)

Similarly,

and
R,+R,sC(v).

(14.141)

These upper bounds are achieved when XI - A’(O, PI) and X, = MO, P,>
and define the capacity region.
The surprising
fact abopt+$hese inequalities
is that the sum of the
rates can be as large as C( ++
), which is that rate achieved by a single
transmitter
sending with a power equal to the sum of the powers.

406

NETWORK

1NFORMATlON

THEORY

The interpretation
of the corner points is very similar to the interpretation of the achievable rate pairs for a discrete multiple access channel
for a fixed input distribution.
In the case of the Gaussian channel, we
can consider decoding as a two-stage process: in the first stage, the
receiver decodes the second sender, considering the first sender as part
of t$e noise. This decoding will have low probability
of error if R, <
C(LP, + N ). After the second sender has been successfully decoded, it can
be subtpracted out and the first sender can be decoded correctly if
R, < C( +). Hence, this argument shows that we can achieve the rate
pairs at the corner points of the capacity region.
If we generalize this to m senders with equal power, the total rate is
C( s ), which goes to 00 as m + 00. The average rate per sender, kC( F)
goes to 0. Thus when the total number of senders is very large, so that
there is a lot of interference,
we can still send a total amount of
information
which is arbitrarily
large even though the rate per individual sender goes to 0.
The capacity region described above corresponds to Code Division
Multiple
Access (CDMA), where orthogonal
codes are used for the
different senders, and the receiver decodes them one by one. In many
practical situations, though, simpler schemes like time division multiplexing or frequency division multiplexing
are used.
With frequency division multiplexing,
the rates depend on the bandwidth allotted to each sender. Consider the case of two senders with
powers P, and P2 and using bandwidths
non-intersecting
frequency
bands W, and W,, where W, + W, = W (the total bandwidth). Using the
formula for the capacity of a single user bandlimited
channel, the
following rate pair is achievable:

o “(&) c(.)R1
Figure 14.17.Gaussian multiple

access channel capacity.

14.4

ENCODZNG

OF CORRELATED

407

SOURCES

RI =~log(l+&),

(14.142)
(14.143)

As we vary WI and Wz, we trace out the curve as shown in Figure 14.17.
This curve touches the boundary of the capacity region at one point,
which corresponds to allotting bandwidth to each channel proportional
to the power in that channel. We conclude that no allocation of frequency bands to radio stations can be optimal
unless the allocated
powers are proportional
to the bandwidths.
As Figure 14.17 illustrates,
in general the capacity region is larger
than that achieved by time division or frequency division multiplexing.
But note that the multiple
access capacity region derived above is
achieved by use of a common decoder for all the senders. However in
many practical systems, simplicity of design is an important
consideration, and the improvement
in capacity due to the multiple
access ideas
presented earlier may not be sufficient to warrant the increased complexity.
For a Gaussian multiple
access system with m sources with powers
PI, p,, * * *, Pmand ambient noise of power N, we can state the equivalent of Gauss’s law for any set S in the form
C Ri = Total

rate of information

flow across boundary

of S

(14.144)

iES

(14.145)

14.4

ENCODING

OF CORRELATED

SOURCES

We now turn to distributed
data compression. This problem is in many
ways the data compression dual to the multiple access channel problem.
We know how to encode a source X. A rate R > H(X) is sufficient. Now
suppose that there are two sources (X, Y) - p(x, y). A rate H(X, Y) is
sufficient if we are encoding them together. But what if the X-source
and the Y-source must be separately described for some user who wishes
to reconstruct both X and Y? Clearly, by separate encoding X and Y, it is
seen that a rate R = R, + R, > H(X) + H(Y) is sufficient. However, in a
surprising
and fundamental
paper by Slepian and Wolf [255], it is
shown that a total rate R = H(X, Y) is sufficient even for separate
encoding of correlated sources.
be a sequence of jointly distributed
random
Let <X,,Y,),(x,,Y2),...
variables i.i.d. - p(x, y). Assume that the X sequence is available at a

NETWORK

INFORMATION

THEORY

location A and the Y sequence is available at a location B. The situation
is illustrated
in Figure 14.18.
Before we proceed to the proof of this result, we will give a few
definitions.
Definition:
A ((2nR1, 2nR2 ), n) distributed
(X, Y) consists of two encoder maps,

f,:i??Y”+{1,2,.

source code for the joint

source

. . ,2nR1},

(14.146)

fi : 9P+ { 1,2, . . . , 2nR2}

(14.147)

and a decoder map,
g:{l,2,.

. . , 2nR’} x {1,2, . . . , 2nR2} -+ Z” x 3” .

(14.148)

Here fl(Xn ) is the index corresponding
to X”, f,( Y” ) is the index
corresponding
to Y” and (RI, R,) is the rate pair of the code.
Definition:
defined as

The probability

of error for a distributed

Pp’ = P(g( f,W

1, f,W” N # w,

Y” 1) *

source code is

(14.149)

Definition:
A rate pair (R,, R,) is said to be achievable for a distributed source if there exists a sequence of ((znR1, 2nR2), n) distributed
source
codes with probability
of error PF’ + 0. The achievable rate region is the
closure of the set of achievable rates.

X
=

Encoder

4

Decoder
Y
*

Encoder

R2

Figure 14.18.Slepian-Wolf

coding.

14.4

ENCODlNG

OF CORRELATED

409

SOURCES

Theorem
14.4.1 (Slepian-Wolf
): For the distributed source codingproblem for the source (X, Y) drawn i.i.d - p(x, y), the achievable rate region
is given by

R, ~H(XIY),

(14.150)

R, 2 H(yIX) ,

(14.151)
(14.152)

R,+R+H(X,Y).
Let us illustrate

the result with some examples.

14.4.1: Consider the weather in Gotham and Metropolis.
For
the purposes of our example, we will assume that Gotham is sunny with
probability
0.5 and that the weather in Metropolis
is the same as in
Gotham with probability
0.89. The joint distribution
of the weather is
given as follows:

Example

Pk

Y)

Gotham
Rain
Shine

Metropolis
Rain
Shine
0.445
0.055

0.055
0.445

Assume that we wish to transmit 100 days of weather information
to the
National Weather Service Headquarters
in Washington.
We could send
all the 100 bits of the weather in both places, making 200 bits in all. If
we decided to compress the information
independently,
then we would
still need lOOH(O.5) = 100 bits of information
from each place for a total
of 200 bits.
If instead we use Slepian-Wolf
encoding, we need only H(X) +
H(YIX) = lOOH(O.5) + lOOH(O.89) = 100 + 50 = 150 bits total.
Example

14.43:

Consider

the following

joint

distribution:

In this case, the total rate required for the transmission
of this source is
H(U) + H(V] U) = log 3 = 1.58 bits, rather than the 2 bits which would

410

NETWORK

be needed if the sources were transmitted
pian-Wolf encoding.
14.4.1 Achievability

of the Slepian-Wolf

ZNFORMATZON

independently

THEORY

without

Sle-

Theorem

We now prove the achievability
of the rates in the Slepian-Wolf theorem.
Before we proceed to the proof, we will first introduce a new coding
procedure using random bins.
The essential idea of random bins is very similar to hash functions:
we choose a large random index for each source sequence. If the set of
typical source sequences is small enough (or equivalently,
the range of
the hash function is large enough), then with high probability,
different
source sequences have different indices, and we can recover the source
sequence from the index.
Let us consider the application
of this idea to the encoding of a single
source. In Chapter 3, the method that we considered was to index all
elements of the typical set and not bother about elements outside the
typical set. We will now describe the random binning procedure, which
indexes all sequences, but rejects untypical sequences at a later stage.
Consider the following procedure: For each sequence X”, draw an
index at random from { 1,2, . . . , 2”R}. The set of sequences X” which
have the same index are said to form a bin, since this can be viewed as
first laying down a row of bins and then throwing the Xn’s at random
into the bins. For decoding the source from the bin index, we look for a
typical X” sequence in the bin. If there is one and only one typical X”
sequence in the bin, we declare it to be the estimate x” of the source
sequence; otherwise, an error is declared.
The above procedure defines a source code. To analyze the probability
of error for this code, we will now divide the X” sequences into two
types, the typical sequences and the non-typical
sequences.
If the source sequence is typical, then the bin corresponding
to this
source sequence will contain at least one typical sequence (the source
sequence itself). Hence there will be an error only if there is more than
one typical sequence in this bin. If the source sequence is non-typical,
then there will always be an error. But if the number of bins is much
larger than the number of typical sequences, the probability
that there
is more than one typical sequence in a bin is very small, and hence the
probability
that a typical sequence will result in an error is very small.
Formally,
let RX”) be the bin index corresponding
to X”. Call the
decoding function g. The probability
of error (averaged over the random
choice of codes f) is
P( g( f(X)) #X) zs P(XflAy’
5 E+ c
X

) + 2 P( 3x’ # x:x’ E A:‘,
c
X’EA(“)
x’z:

P;fo

= f(x>>p(x)

f-(x’, = f(x))p(x)
(14.153)

14.4

ENCODING

OF CORRELATED

5 E+ 2

c

X

=E+

se+

SOURCES

2-5(x)

411

(14.154)

x’EAT)

c

2-“R 2 p(x)

x’EA~)

x

2

2-nR

(14.156)

x’EA~)

SE+2
126

nw(X)+E)2-nR

(14.157)
(14.158)

if R > H(X) + E and n is sufficiently large. Hence if the rate of the code is
greater than the entropy, the probability
of error is arbitrarily
small and
the code achieves the same results as the code described in Chapter 3.
The above example illustrates
the fact that there are many ways to
construct codes with low probabilities
of error at rates above the entropy
of the source; the universal source code is another example of such a
code. Note that the binning scheme does not require an explicit characterization
of the typical set at the encoder; it is only needed at the
decoder. It is this property that enables this code to continue to work in
the case of a distributed
source, as will be illustrated
in the proof of the
theorem.
We now return to the consideration
of the distributed
source coding
and prove the achievability
of the rate region in the Slepian-Wolf
theorem.
Proof (Achievability
in Theorem 14.4.1): The basic idea of the proof
is to partition the space of E’” into 2nR1 bins and the space of ?V into 2nR2
bins.
Random code generation.
Independently
assign every x E 2” to one of
2nR1 bins according to a uniform distribution
on { 1,2, . . . , 2nR1}.
Similarly,
randomly assign every y E 9” to one of 2nR2 bins. Reveal
the assignments f, and f, to both the encoder and decoder.
Encoding.
Sender 1 sends the index of the bin to which X belongs.
Sender 2 sends the index of the bin to which Y belongs.
Decoding. Given the received index pair (iO, j,), declare (&, 4) = (x, y),
if there is one and only one pair of sequences (x, y) such that
f,(x) = i,, f,(y) = j0 and (x, y) E A:‘. Otherwise declare an error.
The scheme is illustrated
in Figure 14.19. The set of X sequences and the set of Y sequences are divided into bins in such a
way that the pair of indices specifies a product bin.

NETWORK

412

ZNFORhIATlON

2nHW,

THEORY

Y)

jointly typical pairs
W,Y”)

Figure 14.19. Slepian-Wolf
bins.

ProbabiZity

encoding: the jointly

typical pairs are isolated by the product

of error. Let (Xi, Yi> -p(x,

y). Define the events

4, = {(X, W&4:‘}

,

(14.159)

E, = (3x’ #X: f,(x’> = f,(X) and (x’,Y)EA~)}

,

(14.160)

E, = {3y’#Y:

,

(14.161)

fJy’)

=f,(Y)

and (X, y’)EAr’}

and

El2 = {3(x’,y’):x’#X,y’ZY,

f,w)=fim,

f,(YWf,(Y)

and (x’, y’) E A:‘}

. (14.162)

Here X, Y, f, and f, are random. We have an error if (X, Y) is not in
A:’ or if there is another typical pair in the same bin. Hence by the
union of events bound,
P~‘=P(E,uE,UE,UE,,)
I P(E,)

+ P(E,) + RE, I+ P(E,,)

First consider E,. By the AISP, P(E,>+
ly large, P(E,) < e.
To bound P(EI), we have
P(E1)=

P{3x’#X:

(14.163)

f,(x’>=

f,(X),

l

(14.164)

0 and hence for n sufficient-

and (x’,Y)EA~)}

(14.165)

14.4

ENCODING

OF CORRELATED

= c p(x, y)P{3x’
(x9Y)
5 c p(x, y)
(x, Y)

113

SOURCES

#x: fi(x’) = f,(x), (x’ , y) E A;‘}

c
x’fx

(14.166)
(14.167)

P( fi(X’) = f,(x)>

(x’ , yEA:’
=

2

k Y)

(14.168)

p(x~P-"~'IA,(Xly)l

52 412 n(H(XIY)+r) (by Theorem

14.2.2))

(14.169)

which goes to 0 if R, > H(XIY).
Hence for sufficiently
large n,
P(E, ) < E. Similarly,
for sufficiently
large n, P(E, ) < E if R, >
H(YIX) and P(E12) < E if R, + R, > H(X, Y).
Since the average probability
code ( fT, f $, g*) with probability
sequence of codes with Pr’+
complete.
0

of error is < 4e, there exists at least one
of error < 4~. Thus, we can construct a
0 and the proof of achievability
is

14.4.2 Converse for the Slepian-Wolf

Theorem

The converse for the Slepian-Wolf
theorem follows obviously from from
the results for single source, but we will provide it for completeness.
Proof (Converse to Theorem 14.4.1): As usual, we begin with Fano’s
inequality.
Let fi , f,, g be fixed. Let I0 = f,<x” ) and J, = f,(Y” ). Then
H(X”, Y” I&, Jo) 5 Pr’n(
where E, -+ 0 as n + 00. Now adding

loglE(

+ log1 3 ) + 1 = nen , (14.170)

conditioning,

we also have

H(X” 1Y”, I,, JO) 5 Pf%2ca ,

(14.171)

H(Y” IXn, I,, JO) 5 Pr&

(14.172)

and

We can write

.

a chain of inequalities
(a)
(14.173)
= I(X”, Y”; I,, Jo) + H(I,,
(2 I(X”, Y”; I,, JO)

J,(X”,

Y”)

(14.174)
(14.175)

NETWORK

414

ZNFORMATION

THEORY

= H(X", Y") - H(X", Y" II,, Jo)

(14.176)

2 H(X”, Y”) - m,

(14.177)

Cd)

= nH(X, Y) - ne, ,

(14.178)

where
(a) follo;fR f””
the fact that I,, E {1,2, . . . , 2nR1} and J, E { 1,2,
2
- *- ?
(b) from the iact the I, is a function of X” and J, is a function of Y”,
(c) from Fano’s inequality
(14.170), and
(d) from the ch ain rule and the fact that <xi, Yi> are i.i.d.
Similarly,

using (14.171), we have
kc)
nR, 2 H(I,,)

(14.179)

1 H(I,IY”)

(14.180)

= 1(x”; I, 1Y” ) + H(I, IX”, y” )

(14.181)

(2 I(X”; I,IY")

(14.182)
- H(X”II,,

g H(X”IY”)

- nc,

(14.184)

- nc, ,

(14.185)

Cd)

= nH(XIY)

Jo, Y”)

R2

H(Y)

M

YIX)

oj HWI
Y) H(X)
R,
!

Figure 14.20.

(14.183)

= H(X”IY”)

’

Rate region for Slepian-Wolf encoding.

14.4

ENCODING

OF CORRELATED

425

SOURCES

where the reasons are the same as for the equations
we can show that
nR, L nH(Y(X)
Dividing these inequalities
the desired converse.
0
The region
Figure 14.20.

described

14.4.3 Slepian-Wolf

(14.186)

- TM,.

by n and taking

the limit

in the Slepian-Wolf

theorem

Theorem

above. Similarly,

for Many

as n + 00, we have

is illustrated

in

Sources

The results of the previous section can easily be generalized
sources. The proof follows exactly the same lines.

to many

Theorem
14.4.2: Let (XIi,Xzi, . . . ,X,,J be i.i.d. - p(xI,xz,.
. . ,x,).
source coding with
Then the set of rate vectors achievable for distributed
separate encoders and a common decoder is defined by
(14.187)
for all S c {1,2,.

. . , m> where

RW=C,&
iES
and X(S)=

{Xj:jES}.

Proof:
omitted.

The proof is identical
Cl

to the case of two variables

(14.188)

and is

The achievability
of Slepian-Wolf
encoding has been proved for an
i.i.d. correlated source, but the proof can easily be extended to the case
of an arbitrary joint source that satisfies the AEP; in particular,
it can
be extended to the case of any jointly ergodic source [63]. In these cases
the entropies in the definition
of the rate region are replaced by the
corresponding
entropy rates.
14.4.4 Interpretation

of Slepian-Wolf

Coding

We will consider an interpretation
of the corner points of the rate region
in Slepian-Wolf
encoding in terms of graph coloring. Consider the point
with rate R, = H(X), R, = H(YIX). Using nH(X) bits, we can encode X”
efficiently, so that the decoder can reconstruct X” with arbitrarily
low
probability
of error. But how do we code Y” with nH(Y(X) bits?
Looking at the picture in terms of typical sets, we see that associated
with every X” is a typical “fan” of Y” sequences that are jointly typical
with the given X” as shown in Figure 14.21.

416

NETWORK

Figure

14.21.

Jointly

typical

ZNFORMATZON

THEORY

fans.

If the Y encoder knows X”, the encoder can send the index of the Y”
within this typical fan. The decoder, also knowing X”, can then construct
this typical fan and hence reconstruct Y”. But the Y encoder does not
know X”. So instead of trying to determine the typical fan, he randomly
colors all Y” sequences with ZnR2 colors. If the number of colors is high
enough, then with high probability,
all the colors in a particular fan will
be different and the color of the Y” sequence will uniquely define the Y”
the number of
sequence within the X” fan. If the rate R, > H(YIX),
colors is exponentially
larger than the number of elements in the fan
and we can show that the scheme will have exponentially
small probability of error.

14.5 DUALITY BETWEEN SLEPIAN-WOLF
MULTIPLE ACCESS CHANNELS

ENCODING

AND

With multiple
access channels, we considered the problem of sending
independent
messages over a channel with two inputs and only one
output. With Slepian-Wolf
encoding, we considered the problem of
sending a correlated source over a noiseless channel, with a common
decoder for recovery of both sources. In this section, we will explore the
duality between the two systems.
In Figure 14.22, two independent
messages are to be sent over the
channel as X; and Xi sequences. The receiver estimates the messages
from the received sequence. In Figure 14.23, the correlated sources are
encoded as “independent”
messages i and j. The receiver tries to
estimate the source sequences from knowledge of i and j.
In the proof of the achievability
of the capacity region for the multiple
access channel, we used a random map from the set of messages to the
sequences X; and Xi. In the proof for Slepian-Wolf
coding, we used a
random map from the set of sequences X” and Y” to a set of messages.

14.5

DUALI2-Y

Wl

-x1

w2

-x2

BETWEEN

SLEPZAN-WOLF

417

ENCODZNG

P(YlX*J2)

>Y

-(lQkz,

-

Figure 14.22. Multiple

access channels.

In the proof of the coding theorem for the multiple
probability
of error was bounded by
Prkr+

P(r co d eword jointly

c

typical

codewords

= E+

c
2

nR1

2-“”

+

c

2-“‘2 +

terms

the

with received sequence)
(14.189)
2-“‘3,

c
2 n(Rl

2 nRz terms

access channel,

+W

(14.190)

terms

where E is the probability
the sequences are not typical, Ri are the rates
corresponding
to the number of codewords that can contribute
to the
probability
of error, and Ii is the corresponding mutual information
that
corresponds to the probability
that the codeword is jointly typical with
the received sequence.
In the case of Slepian-Wolf encoding, the corresponding expression for
the probability
of error is

X
=

Encoder

’

RI

(X9 v)

Decoder

Y
,‘

Encoder

t

Figure 14.23. Correlated

R2

source encoding.

+td

A

NETWORK

418

Puke+

Jointly

= E +

c

typical

2

2

nH1

Pr(have

same codeword)

THEORY

(14.191)

sequences

2-n%+

terms

INFORMATION

c

2 nH!2 terms

242

+

c

2 nH3

2-n(%+R2)

terms

(14.192)

where again the probability
that the constraints of the AEP are not
satisfied is bounded by E, and the other terms refer to the various ways
in which another pair of sequences could be jointly typical and in the
same bin as the given source pair.
The duality of the multiple
access channel and correlated
source
encoding is now obvious. It is rather surprising that these two systems
are duals of each other; one would have expected a duality between the
broadcast channel and the multiple
access channel.

14.6

THE BROADCAST

CHANNEL

The broadcast channel is a communication
channel in which there is one
sender and two or more receivers. It is illustrated
in Figure 14.24. The
basic problem is to find the set of simultaneously
achievable rates for
communication
in a broadcast channel.
Before we begin the analysis, let us consider some examples:
Example
14.6.1 (TV station): The simplest example of the broadcast
channel is a radio or TV station. But this example is slightly degenerate
in the sense that normally the station wants to send the same information to everybody who is tuned in; the capacity is essentially maxpCX,
min, 1(X, Yi ), which may be less than the capacity of the worst receiver.

Figure 14.24.

Broadcast channel.

14.6

THE BROADCAST

CHANNEL

419

But we may wish to arrange the information
in such a way that the
better receivers receive extra information,
which produces a better
picture or sound, while the worst receivers continue to receive more
basic information.
As TV stations introduce High Definition TV (HDTV),
it may be necessary to encode the information
so that bad receivers will
receive the regular TV signal, while good receivers will receive the extra
information
for the high definition
signal. The methods to accomplish
this will be explained in the discussion of the broadcast channel.
14.6.2 (Lecturer in classroom): A lecturer in a classroom is
communicating
information
to the students in the class. Due to difYerences among the students, they receive various amounts of information.
Some of the students receive most of the information;
others receive only
a little. In the ideal situation, the lecturer would be able to tailor his or
her lecture in such a way that the good students receive more information and the poor students receive at least the minimum
amount of
information.
However, a poorly prepared lecture proceeds at the pace of
the weakest student. This situation is another example of a broadcast
channel.
Example

14.6.3 (Orthogonal
broadcast channels): The simplest broadcast channel consists of two independent
channels to the two receivers.
Here we can send independent
information
over both channels, and we
can achieve rate R, to receiver 1 and rate R, to receiver 2, if R, < C!, and
R, < C,. The capacity region is the rectangle shown in Figure 14.25.
Example

14.6.4 (Spanish and Dutch speaker): To illustrate
the idea of
superposition,
we will consider a simplified
example of a speaker who
can speak both Spanish and Dutch. There are two listeners:
one
understands
only Spanish and the other understands
only Dutch. Assume for simplicity
that the vocabulary of each language is 220 words

Example

Figure 14.25. Capacity region for two orthogonal

broad&t

channels.

NETWORK

420

INFORMATION

THEORY

and that the speaker speaks at the rate of 1 word per second in either
language. Then he can transmit
20 bits of information
per second to
receiver 1 by speaking to him all the time; in this case, he sends no
information
to receiver 2. Similarly,
he can send 20 bits per second to
to receiver 1. Thus he can
receiver 2 without sending any information
achieve any rate pair with R, + R, = 20 by simple timesharing.
But can
he do better?
Recall that the Dutch listener, even though he does not understand
Spanish, can recognize when the word is Spanish. Similarly,
the Spanish listener can recognize when Dutch occurs. The speaker can use this
to convey information;
for example, if the proportion
of time he uses
each language is 50%, then of a sequence of 100 words, about 50 will be
Dutch and about 50 will be Spanish. But there are many ways to order
the Spanish and Dutch words; in fact, there are about ( !&’ ) = 2100H(t)
ways to order the words. Choosing one of these orderings conveys
information
to both listeners. This method enables the speaker to send
information
at a rate of 10 bits per second to the Dutch receiver, 10 bits
per second to the Spanish receiver, and 1 bit per second of common
information
to both receivers, for a total rate of 21 bits per second,
which is more than that achievable by simple time sharing. This is an
example of superposition
of information.
The results of the broadcast channel can also be applied to the case of
a single user channel with an unknown distribution.
In this case, the
objective is to get at least the minimum
information
through when the
channel is bad and to get some extra information
through when the
channel is good. We can use the same superposition
arguments as in the
case of the broadcast channel to find the rates at which we can send
information.
14.6.1 Definitions

for a Broadcast Channel

A broadcast channel consists of an input alphabet Z and
two output alphabets q1 and 5V2 and a probability
transition
function
p( yl, y2 IX). The broadcast channel will be said to be memoryless
if
pbfq, Y;lx”) = J$L, P(Yli, Y&i).
Definition:

We define codes, probability
of error, achievability
and capacity
regions for the broadcast channel as we did for the multiple
access
channel.
A ((2nR1, 211R2),n) code for a broadcast channel with independent
information
consists of an encoder,
X:({l,
and two decoders,

2,. . . , 2nR1} x { 1,2, . . . , 2nR2})+

2” ,

(14.193)

14.6

THE BROADCAST

421

CHANNEL

g,:%+-+(1,2,.

. . ,2nR1}

(14.194)

2nRz}.

(14.195)

and
g,:C?+{1,2

,...,

We define the average probability
of error
decoded message is not equal to the transmitted

where (WI, W,) are assumed to be uniformly

as the probability
message, i.e.,

distributed

the

over 2nR1 x 2”R2.

Definition:
A rate pair (R,, Rz) is said to be achievable for the broadcast channel if there exists a sequence of ((ZnR1, 2nR2), n> codes with
P%’ + 0.
We will now define the rates for the case where we have common
information
to be sent to both receivers.
A ((2nR9 2nR1, 2nR21, n) code for a broadcast channel with common
information
consists of an encoder,
X:({l,

2, * . . , 2nRo} x { 1,2, . . . , 2nR1} x { 1,2, . . . , 2nR2} I)-, ap” ,
(14.197)

and two decoders,
g, : 37 --j {1,2, . . . , 2nR0) x { 1,2, . . . , FR1}

(14.198)

g,:CK+{1,2

(14.199)

,...,

2nR0}X{1,2

,...,

2nR2}.

Assuming that the distribution
on ( W,, WI, Wz ) is uniform, we can define
the probability
of error as the probability
the decoded message is not
equal to the transmitted
message, i.e.,

Pr) = P(gJYy)

# (W,, WI> or gJz"> # CW,,W,)) -

(14.200)

Definition:
A rate triple (RO, R,, R,) is said to be achievable for the
broadcast channel with common information
if there exists a sequence
of ((2nRo, 2nR1,2nR2), n) codes with PF’-, 0.
Definition:
The capacity region of the broadcast
of the set of achievable rates.

channel

is the closure

422

NETWORK

INFORMATION

THEORY

Theorem
14.6.1: The capacity region of a broadcast channel depends
only on the conditional
marginal
distributions
p( y,lx) and p( y21x).
Proof:

See exercises.

14.6.2 Degraded
Definition:

Cl

Broadcast

A broadcast

Channels
channel

is said to be physically

degraded

if

P(Y1, Yzl”) = P(Yh)P(Y,IYd*
A broadcast channel is said to be stochastically
degraded if
its conditional
marginal
distributions
are the same as that of a physically degraded broadcast channel, i.e., if there exists a distribution
p’(y21yI) such that
Definition:

p(y&)

= c P(YIIdP’(Y2lYd

’

(14.201)

Yl

Note that since the capacity of a broadcast channel depends only on
the conditional
marginals,
the capacity region of the stochastically
degraded broadcast channel is the same as that of the corresponding
physically degraded channel. In much of the following, we will therefore
assume that the channel is physically degraded.
14.6.3 Capacity

Region

We now consider
broadcast channel

for the Degraded

Broadcast Channel

sending independent
information
over a degraded
at rate R, to Y1 and rate R, to Yz.

Theorem
14.6.2: The capacity region for sending independent information over the degraded broadcast channel X-, Y1+ Y2 is the convex hull
of the closure of all (R,, R2) satisfying
y,> ,

(14.202)

R, 5 I(X, Y@>

(14.203)

R, 5 NJ;

for some joint distribution
p(u)p(x I u>p( y, z lx>, where the auxiliary rano?om variable U has cardinality
bounded by I % 11 min{ 1%I, I CV1I, I %2I}.

Proof: The cardinality
bounds for the auxiliary
random variable U
are derived using standard methods from convex set theory and will not
be dealt with here.
We first give an outline of the basic idea of superposition
coding for
the broadcast channel. The auxiliary random variable U will serve as a
cloud center that can be distinguished
by both receivers Y1 and Yz. Each

14.6

THE BROADCAST

423

CHANNEL

by the receiver Y1.
cloud consists of ZP1 codewords X” distinguishable
The worst receiver can only see the clouds, while the better receiver can
see the individual
codewords within the clouds.
The formal proof of the achievability
of this region uses a random
coding argument:
Fix p(u) and p(xlu).
Random codebook generation.
Generate 2nR2 independent
codewords
of length n, U(w,), w1 E { 1,2, . . . , 2nR2}, according to lIysl p(ui ).
For each codeword U(w2), generate 2nR1 independent
codewords
X(wl, w,) according to l-l:=, ~(~G~IzQ(w~)).
Here u(i) plays the role of the cloud center understandable
to
both Y1 and Yz, while x( i, j ) is the jth satellite codeword in the i th
cloud.
Encoding. To send the pair (W,, W,>, send the corresponding
codeword X( W1, Wz).
1
Decodiyg. Receiver
2 determines
the unique
Ws such that
NJW,), Y2> E A:‘. If there are none such or more than one such,
an error is declared.
Receiver
l_ looks for the unique
( W1, W-J such that
If there are none such or more than
<vCw,>, Xcw,, W,>, Y1) EA:‘.
one such, an error is declared.
Analysis of the probability
of error. By the symmetry
of the code
generation,
the probability
of error does not depend on which
codeword was sent. Hence, without loss of generality,
we can
assume that the message pair ( W,, Wz> = (1,l) was sent. Let P( - )
denote the conditional probability
of an event given that (1,l) was
sent.
Since we have essentially a single user channel from U to Yz, we
will be able to decode the U codewords with low probability
of error
if R, < I(U; Y2>. To prove this, we define the events
E,
Then the probability

= {(U(i), Y2) E A:‘}

.

(14.204)

of error at receiver 2 is
(14.205)

(14.206)
(14.207)
r2E

(14.208)

NETWORK

424

INFORMATION

THEORY

if n is large enough and R, < I(U; Y,), where (14.207) follows from
the AEF’.
Similarly,
for decoding for receiver 1, we define the following
events
&

= {(U(i),

Y1) E Al")} ,

iyi

= {(U(i),

X(i, j), Yr) E A:'}

(14.209)

,

(14.210)

where the tilde refers to events defined at receiver 1. Then, we can
bound the probability
of error as
P:‘(l)

(14.211)

= P(ZZcy1 LJ U j?*i LJ U ‘rlj)
if1

j#l

~ P(~"y,) + C P(~,) + C P(~yu).
if1

(14.212)

j#l

Bynhi$e ys~-~~ arguments as for receiver 2, we can bound P(~~i) I
; 1
. Hence the second term
goes to 0 if R, < I(U; YI ). But
2by the data processing inequality
and the degraded nature of the
channel, I(U; YI ) 2 I( U; Y,), and hence the conditions
of the
theorem imply that the second term goes to 0. We can also bound
the third term in the probability
of error as
p(iyv)

X(1, j), Y1) E A;‘)

= P((U(l),

= c
= c
(u,

(14.213)

P((U(l), X(1, j), Y,))

(14.214)

PWWP(X(1,

(14.215)

X, Y, EA:’

j)(uu))Pw,(uw

W, X, Y, IEAr’

5

c

2-n(H(U)-c)2-n(H(xIU)-~)2-~(~(y~t~)-E)

(14.216)

NJ, X, Y, EAr)

52 n(HW,
=2-

X, Y1)+c)

n(Z(X;

2- n(H(U)-c)2-n(H(XI(I)-a)2-n(H(YIIU)-~)

(14.217)

YIJU)-46)

(14.218)

Hence, if R, < 1(X, YI 1U ), the third term in the probability
goes to 0. Thus we can bound the probability
of error
p:)(1)

I

E +

13E

2nR22-nUW;

Y1)-3r)

+

@2-n(Z(X;

YlIU)-4r)

of error
(14.219)

(14.220)

14.6

THE BROADCAST

4725

CHANNEL

if n is large enough and R, < Z(U; YI ) and R, < Z(X, YI 1U). The
above bounds show that we can decode the messages with total
probability
of error that goes to 0. Hence theres exists a sequence
of error going to 0.
of good ((znR1, 2”R2), n) codes %‘E with probability
With this, we complete the proof of the achievability
of the capacity
region for the degraded broadcast channel. The proof of the converse is
outlined in the exercises.
Cl
So far we have considered sending independent
information
to both
receivers. But in certain situations, we wish to send common information to both the receivers. Let the rate at which we send common
information
be R,. Then we have the following obvious theorem:
Theorem
14.6.3: Zf the rate pair (RI, R,) is achievable for a broadcast
channel with independent
information,
then the rate triple (R,, R, R,, R, - R,) with a common rate R, is achievable, provided that R, 5
min(R,, R,).
In the case of a degraded broadcast channel, we can do even better.
Since by our coding scheme the better receiver always decodes all the
information
that is sent to the worst receiver, one need not reduce the
amount of information
sent to the better receiver when we have common
information.
Hence we have the following theorem:
Theorem
14.6.4: If the rate pair (R,, R,) is achievable for a degraded
broadcast channel, the rate triple (R,,, R,, R, - R,) is achievable for the
channel with common information,
provided that R, CR,.
We will end this section by considering
symmetric broadcast channel.

the example

of the binary

Example
14.6.6: Consider a pair of binary symmetric
channels with
parameters p1 and p2 that form a broadcast channel as shown in Figure
14.26.
Without loss of generality in the capacity calculation,
we can recast
this channel as a physically
degraded channel. We will assume that
pr <p2 < 8. Then we can express a binary symmetric
channel with
parameter pz as a cascade of a binary symmetric channel with parameter p1 with another binary symmetric channel. Let the crossover probability of the new channel be (Y. Then we must have
pl(l-a)+(l-P,)~=P2*

or

(14.221)

426

NETWORK

ZNFORMATZON

THEORY

y2

Figure 14.26. Binary symmetric broadcast channel.

a-p2-p1

l-zp,

(14.222)

*

We now consider the auxiliary random variable in the definition of the
capacity region. In this case, the cardinality
of U is binary from the
bound of the theorem. By symmetry,
we connect U to X by another
binary symmetric
channel with parameter
p9 as illustrated
in Figure
14.27.
We can now calculate the rates in the capacity region. It is clear by
symmetry
that the distribution
on U that maximizes
the rates is the
uniform distribution
on (0, l}, so that

w; Yz> =WY,) - WY,IU)

(14.223)

=l--wp*p,),

(14.224)

where
p *p2 = PC1 -p2)

Figure 14.27. Physically

+ (1 -

PIP2

-

(14.225)

degraded binary symmetric broadcast channel.

14.6

THE BROADCAST

427

CHANNEL

Similarly,

m YJU)=H(Y,lU)

- H(Y,IX,

U)

(14.226)

= H(Y,lU) - H(Y#)

(14.227)

= H(P “PII - MP,),

(14.228)

where
p*pl=P(l-p,)+(l-P)P,.

(14.229)

Plotting these points as a function of p, we obtain the capacity region in
Figure 14.28.
When p = 0, we have maximum
information
transfer to Y2, i.e.,
R, = 1 - H(p,) and R, = 0. When p = i, we have maximum
information
transfer to YI , i.e., R, = 1 - H( p1 ), and no information
transfer to Yz.
These values of p give us the corner points of the rate region.
14.6.6 (Gaussian broadcast channel):
The Gaussian broadcast channel is illustrated
in Figure 14.29. We have shown it in the case
where one output is a degraded version of the other output. Later, we
will show that all Gaussian broadcast channels are equivalent
to this
type of degraded channel.
Example

Y,=X+Z,,

(14.230)

Yz=x+z,=Y,+z;,

(14.231)

where 2, - NO, N,) and Z$ - NO, N, - NJ
Extending
the results of this section to the Gaussian case, we can
show that the capacity region of this channel is given by

R2h

Figure 14.28.

Capacity region of binary symmetric broadcast channel.

428

NETWORK

INFORMATZON

THEORY

Figure 14.29. Gaussian broadcast channel.

(14.232)
(14.233)

where cy may be arbitrarily
chosen (0 5 cy5 1). The coding scheme that
achieves this capacity region is outlined in Section 14.1.3.

14.7 THE RELAY CHANNEL

The relay channel is a channel in which there is one sender and one
receiver with a number of intermediate
nodes which act as relays to
help the communication
from the sender to the receiver. The simplest
relay channel has only one intermediate
or relay node. In this case the
channel consists of four finite sets %, E1, 9 and CV1and a collection of
probability
mass functions p( - , - Ix, x1) on 9 x ?!$, one for each (x, s, >E
is that x is the input to the channel and y is
2 x Z&. The interpretation
the output of the channel, y1 is the relay’s observation and x, is the
input symbol chosen by the relay, as shown in Figure 14.30. The
problem is to find the capacity of the channel between the sender X and
the receiver Y.
The relay channel combines a broadcast channel (X to Y and YJ and
a multiple
access channel (X and X1 to Y). The capacity is known for the
special case of the physically degraded relay channel. We will first prove
an outer bound on the capacity of a general relay channel and later
establish an achievable region for the degraded relay channel.
Definition:
A (2”R, n) code for a relay
integers W = { 1,2, . . . , 2”R}, an encoding

channel
function

Figwe 14.30. The relay channel.

consists

of a set of

14.7

THE RELAY

429

CHANNEL

X:(1,2,.
a set of relay functions

and a decoding

(14.234)

. . ,2nR}+%n,

{ fi}r+

such that

function,
g:%“-,{l,2

,...,

(14.236)

2nR}.

Note that the definition of the encoding functions includes the nonanticipatory
condition on the relay. The relay channel input is allowed
to depend only on the past observations y 11, y12, . . . , y li _ 1. The channel
is memoryless
in the sense that (Y,, Yli) depends on the past only
through the current transmitted
symbols <x,,X,J
Thus for any choice
p(w), w E W; and code choice X: { 1,2, . . . , 2”R} + Ey and relay functions
{ fi} T=1, the joint probability
mass function on ‘W x %‘” x S?y x 3” x 9 9
is given by
Pb9 x, Xl,
= p(w)

Y, Yl)
l-7 P(36iIW)PblilYI19

Y129

- ’

* , y&po$,

Y&i,

Xii)

l

(14*237)

i=l

If the message w E [l, 2nR] is sent, let
h(w) = F+{ g(Y) # w 1w sent}
denote the conditional
probability
probability
of error of the code as

of error.

(14.238)

We define

p$’=$ c h(w).

the average

(14.239)

W

The probability
of error is calculated under the uniform distribution
over the codewords w E { 1, 2nR}. The rate R is said to be achievable by
the relay channel if there exists a sequence of <2”“, n) codes with
P%’ * 0. The capacity C of a relay channel is the supremum of the set of
achievable rates.
We first give an upper bound on the capacity of the relay channel.
Theorem

the capacity

For any relay channel
C is bounded above by

14.7.1:

C 5 p;uFl) min{l(X,
,

(3? x 2&, p( y, yr(x, x1), 9 x 9I>

Xl; Y), 1(x, Y, YJX,)}

.

(14.240)

430

NETWORK

lNFORh4ATIOiV

THEORY

Proof: The proof is a direct consequence of a more general
min cut theorem to be given in Section 14.10. Cl

max flow

This upper bound has a nice max flow min cut interpretation.
The
first term in (14.240) upper bounds the maximum
rate of information
transfer from senders X and XI to receiver Y. The second terms bound
the rate from X to Y and YI.
We now consider a family of relay channels in which the relay
receiver is better than the ultimate
receiver Y in the sense defined
below. Here the max flow min cut upper bound in the (14.240) is
achieved.
Definition:
be physically

The relay channel (% x ZI, p(y, yllx, x1), 9 X %$) is said to
degraded if p(y, y&, x,) can be written in the form

p(y, Y11~,~1)=P(Y11~,~1)P(YIY1,~1). (14.241)
Thus Y is a random

degradation

of the relay signal YI.

For the physically degraded
the following theorem.

relay channel,

the capacity

Theorem
14.7.2:
is given by

C of a physically

degraded

relay channel

XI; Y), 1(X; YI IX, )} ,

(14.242)

The capacity

C = sup min{l(X,
P(& Xl)
where the supremum

is over all joint

distributions

is given bY

on S?’x 2&

Proof (Converse): The proof follows from Theorem
14.7.1 and by
degradedness,
since for the degraded relay channel, 1(X, Y, YI 1X1) =
1(x; Yl Ix, ).
Achievability.
The proof of achievability
involves a combination
of the
following basic techniques:
(1) random coding, (2) list codes, (3)
Slepian-Wolf
partitioning,
(4) coding for the cooperative multiple
access channel, (5) superposition
coding, and (6) block Markov
encoding at the relay and transmitter.
We provide only an outline of the proof.
Outline of achievability.
We consider B blocks of transmission,
each
of n symbols. A sequence of B - 1 indices, Wi E { 1, . . . , 2nR}, i =
1,2,. . . , B - 1 will be sent over the channel in nB transmissions.
(Note that as B + 00, for a fixed n, the rate R(B - 1)/B is arbitrarily
close to R.)

14.7

THE RELAY

431

CHANNEL

We define a doubly-indexed
z = {dwls),

set of codewords:

XI(S)} : w E (1, 2nR}, s E (1, 2nRO}, XE 8?“, x, E %I .
(14.243)

We will also need a partition

~={S1,S2,...,

S2dzo} of “u’= {1,2,.

. . , 2nR)

(14.244)

into 2nRo cells, with Si fl Sj = 4, i #j, and U Si = ‘K The partition
will enable us to send side information
to the receiver in the
manner of Slepian and Wolf [2551.
Generation of random code. Fix p(=z&(~)x, ).
First generate at random 2nRo i.i.d. n-sequences in Zzpy, each
drawn according to p(xl) = lly=, p(X,i). Index them as x1(s), s E
indepen{1,2,. . . , 2”Ro}. For each x1(s), generate 2nR conditionally
dent n-sequences x(w Is), w E { 1,2, . . . ,2”},
drawn independently
according to p(xlx,(s)) = l-l:=, p(3Gi(;Xli(S)). This defines the random
codebook Ce= {x(wls), x1(s)}.
The random partition
9’ = {S,, S,, . . . , SznRO} of { 1,2, . . . , 2nR}
is defined as follows. Let each integer w E { 1,2, . . . , 2nR} be assigned independently,
according to a uniform distribution
over the
indices s = 1,2, . . . , anRo, to cells S,.
Encoding. Let wi E {1,2, . . . , 2nR} be the new index to be sent in
block i, and let Si be defined as the partition corresponding to wi_ 1,
i.e., wi-l f s*i* The encoder sends X( Wi IS~). The relay has an
estimate
pi _ 1 of the previous index Wi _ 1. (This will be made
precise in the decoding section.) Assume that S,_1 E Sii. The relay
encoder sends xl(~i) in block i.
Decoding. We assume that at the end of block i - 1, the receiver
LOWS (We, w,, . . . , Wi-0) and (So, s2,. . . , Si-1) and the relay ~IIOWS
(sl, s2, . . . , Si).
(WI, w2, * * - 3 Wi-r) and consequently
The decoding

procedures

at the end of block i are as follows:

1. Knowing Si and upon receiving yl( i), the relay receiver estimates
the message of the transmitter
pi = w if and only if there exists a
E-typical.
unique w such that (X(W ISi), X1(Si), y&i)) are jointly
Using Theorem
14.2.3, it can be shown that Si = Wi with an
arbitrarily
small probability
of error if

R<W
and n is sufficiently

large.

Yl Ix, 1

(14.245)

432

NETWORK

INFORMATZON

THEORY

2. The receiver declares that ii = s was sent iff there exists one and
only one s such that (x1(s), y(i)) are jointly
E-typical. From
Theorem 14.2.1, we know that Si can be decoded with arbitrarily
small probability
of error if

R, < I(&; Y)

(14.246)

and n is sufficiently large.
3. Assuming that Si is decoded correctly at the receiver, the receiver
constructs a list LZ(y(i - 1)) of indices that the receiver considers to
be jointly typical with y(i - 1) in the (i - 1)th block. The receiver
then declares pi _ 1 = w as the index sent in block i - 1 if there is a
unique w in SSi n JZ(y(i - 1)). If n is sticiently
large and if
Rd(X;YIX,)+R,,

(14.247)

then pi_, = wi -1 with arbitrarily
small probability
bining the two constraints
(14.246) and (14.247),
leaving

of error. ComR, drops out,

R<I@;YJX,)+I(&; Y)=I(x,xl; Y) .

(14.248)

For a detailed analysis of the probability
of error, the reader is
referred to Cover and El Gamal [671. Cl
Theorem 14.7.2 can also shown to be the capacity
classes of relay channels.
(i) Reversely

degraded

relay channel,

for the following

i.e.,

P(Y~Yll~~~l)=P(Yl~~~l)P(YllY~~l). (14.249)
(ii) Relay channel with feedback.
(iii) Deterministic
relay channel,
Yl=flGQ,

14.8

SOURCE CODING

WITH

y =gkx,).

(14.250)

SIDE INFORMATION

We now consider the distributed
source coding problem where two
random variables X and Y are encoded separately but only X is to be
recovered. We now ask how many bits R, are required to describe X if
we are allowed R, bits to describe Y.

14.8

SOURCE

CODING

WITH

433

SZDE INFORMATION

If R, > H(Y), then Y can be described perfectly, and by the results of
Slepian-Wolf coding, R 1 = H(XIY) bits suffice to describe X. At the other
extreme, if R, = 0, we must describe X without any help, and R, = H(X)
bits are then necessary to describe X. In general, we will use R, =
I(Y, i’> bits to describe an approximate
version of Y. This will allow us to
describe X using H(X1 Y) bits in the presence of side information
Y. The
following theorem is consistent with this intuition.
Theorem
14.8.1: Let (X, Y) -p(x, y). If Y is encoded at rate R, and X is
encoded at rate R,, we can recover X with an arbitrarily
small probability of error if and only if

for some joint

probability

R, zH(XIU),

(14.251)

R, L I(y; U)

(14.252)

mass function

p(x, y)p(ul y), where 1% 15

191+2.
We prove this theorem in two parts. We begin with the converse, in
which we show that for any encoding scheme that has a small probability of error, we can find a random variable U with a joint probability
mass function as in the theorem.
Proof (Converse): Consider any source code for Figure 14.31. The
source code consists of mappings f,(X” ) and g, (Y” ) such that the rates of
f, and g, are less than R, and R,, respectively, and a decoding mapping
h, such that
P:’

= Pr{h,(

f,<X”),

g,W”))

+Xnl

< E

l

(14.253)

Define new random variables S = f,(X”> and 2’ = g,(Y” ). Then since we
can recover X” from S and T with low probability
of error, we have, by
Fano’s inequality,
H(x”IS,

Figure 14.31.

T)s

ne, .

Encoding with side information.

(14.254)

NETWORK

434

ZNFORMATZON

THEORY

Then

nR,2 H(T)
(b)
z

=

I(Y”;
i

I(Yi;

(14.255)
(14.256)

T)

TIY,,

.

.

l

,

(14.257)

Y&l)

i=l

= i I(y,;T,Y l,"',

yi-l)

i=l

(~’~ I(Y,; Ui)

(14.259)

i=l

where
(a) follows from the fact that the range of g, is { 1,2, . . . , 2”2},
(b) follows from the properties of mutual information,
(c) follows from the chain rule and the fact that Yi is independent
YIP * ’ * 9 Yi-l and hence I(Yi; YI, . . . , Yi_l) = 0, and
(d) follows if we define Vi = (T, Yl , . . . , Yi _1).

of

chain for R, ,

We also have another

(a)
nR, 1 H(S)

(14.260)

(b 1

2 H(SlT)
= H(SlT) + H(X”Is,

(14.261)

T) - H(XnJS, T)

(14.262)

2 HW, SIT) - nc,

(14.263)

(E)H(X” 1T) - nen

(14.264)

g ~ H(XiIT,X,, -*'9 X-i 1)--a n

(14.265)

i=l

%) 2 H(XiIT,Ximl >Y"-'>-- nen

(14.266)

14.8

SOURCE

CODZNG

WlTH

SIDE

435

INFORMATION

(2)i H(XJT,Yi-l)

(14.267)

- TlEn

i=l

”

i

(14.268)

H(xiI Vi) - ne,

i-l

where
(a) follows from the fact that the range of S is { 1,2, . . . , 2nR1},
(b) follows from the fact that conditioning
reduces entropy,
(c) from Fano’s inequality,
(d) from the chain rule and the fact that S is a function of X”,
(e) from the chain rule for entropy,
(f) from the fact that conditioning
reduces entropy,
(g) from the (subtle) fact that Xi-;,(T, Yi-l)+X’-l
forms a Markov
chain since Xi does not contain any information
about Xi-l that is
not there in Y’-’ and T, and
(h) follows from the definition of U.
Also, since Xi contains no more information
about Vi than is present in
Yi, it follows that Xi + Yi + Vi forms a Markov chain. Thus we have the
following inequalities:
RI 2 L i k?(XJU) i
n i=l

(14.269)

R, 1 ~ ~ I(Yi; Vi).

(14.270)

c 1

We now introduce an timesharing
rewrite these equations as
R,d

&3(X
n i=l

i

random

Vi, Q=i)=H(XQIUQ,

R, 2 i 3 I(Yi
i

Now since Q is independent
on i), we have

variable

Ui(Q=i)=I(YQ;

Q, so that we can

&I

(14.271)

V,lQ>

(14.272)

1

of Ys (the distribution

I(Y,;U,IQ)=I(Y,;U,,Q)-I(Y,;Q)=I(Y,;U,,Q).
Now Xs and YQ have the joint

distribution

of Yi does not depend

(14.273)
p(x, y) in the theorem.

436

NETWORK

1NFORMATlON

THEORY

Defining U = (Uo, Q), X = Xo, and Y = Ye, we have shown the existence
of a random variable U such that

R, ~WXJU),

(14.274)

R,rI(Y;U)

(14.275)

for any encoding scheme that has a low probability
converse is proved.
Cl

of error. Thus the

Before we proceed to the proof of the achievability
of this pair of
rates, we will need a new lemma about strong typicality
and Markov
chains. Recall the definition
of strong typicality
for a triple of random
variables X, Y and 2. A triplet of sequences xn, yn, zn is said to be
e-strongly typical if
1
n Ma,

b, cIxn, y: z”) - p(a, b, c> <

,2&p,

’

(14s276)

In particular,
this implies that (x”, y” ) are jointly strongly typical and
that ( y”, z”) are also jointly strongly typical. But the converse is not
true: the fact that (x”, y”) E AT’“‘(X, Y) and (y”, x”) E AT’“‘(Y, 2) does
not in general imply that (xn, yn, z”) E AT’“‘(X, Y, 2). But if X+ Y+ 2
forms a Markov chain, this implication
is true. We state this as a lemma
without proof [28,83].
Lemma
14.8.1: Let (X, Y, 2) form a Markov chain X-+ Y+ 2, i.e.,
p(x, y, x) =p(x, y)p(zly>. If for a given (y”, z”) EAT’“‘(Y, Z), X” is drawn
- IlyE p(xilyi), then Pr{(X”, y”, z”) E AT’“‘(X, Y, 2)) > 1 - E for n suficiently large.
Remark:
The theorem is true from the strong law of large numbers
if X” - llyzl p(xi 1yi, ZJ The Markovity
of X-, Y+ 2 is used to show
that X” - p(xi 1yi) is sufficient for the same conclusion.
We now outline

the proof of achievability

Proof (Achievability
p(u) = c, PCy)p(ul y).

in

Theorem

in Theorem

14.8.1):

Fix

14.8.1.

p(u 1y).

Calculate

Generation
of codebooks. Generate ZnR2 independent
codewords of
length n, U(w,), wo, E { 1,2, . . . , 2nR2} according to llyzl p(ui).
Randomly
bin all the X” sequences into 2” 1 bins by independently
generating
an index
b uniformly
distributed
on
{1,2,. . . , 2nR1} for each X”. Let B(i) denote the set of X” sequences
allotted to bin i.

14.8

SOURCE

CODING

WITH

SIDE

437

INFORMATION

Encoding. The X sender sends the index i of the bin in which X” falls.
The Y sender looks for an index s such that (Y”, U”(s)) E
AT’“‘(Y, U). If there is more than one such s, it sends the least. If
there is no such U”(s) in the codebook, it sends s = 1.
Decoding. The receiver looks for a unique X” E B(i) such that
(X”, U”(s)) E Af”‘(X, U). If there is none or more than one, it
declares an error.
Analysis of the probability
of error. The various sources of error are
as follows:
1. The

pair (X”, Y” ) generated by the source is not typical. The
probability
of this is small if n is large. Hence, without loss of
generality, we can condition on the event that the source produces
a particular
typical sequence (cF, y”) E A$‘“!
2. The sequence Y” is typical, but there does not exist a U”(s) in the
codebook which is jointly typical with it. The probability
of this is
small from the arguments of Section 13.6, where we showed that if
there are enough codewords, i.e., if

R,>I(Y;U),

(14.277)

then we are very likely to find a codeword that is jointly strongly
typical with the given source sequence.
3. The codeword V(S) is jointly typical with y” but not with x”. But
by Lemma 14.8.1, the probability
of this is small since X+ Y+ U
forms a Markov chain.
4. We also have an error if there exists another typical X” E B(i)
which is jointly typical with U”(s). The probability
that any other
X” is jointly
typical with U”(s) is less than 2-n(z(U’X)-3r\ and
therefore the probability
of this kind of error is bounded above by

IB(i)

nAT(n)(x)J2-n(l(X;

u)-3C)

5

2n(H(x)+r)2-nR12-n(z(x;

U)-3~)

,

(14.278)

which goes to 0 if R, > H(Xl U).
Hence it is likely that the actual source sequence X” is jointly typical
with U”(s) and that no other typical source sequence in the same bin is
also jointly
typical with U”(s). We can achieve an arbitrarily
low
probability
of error with an appropriate
choice of n and E, and this
completes the proof of achievability.
Cl

438

14.9

NETWORK

RATE DISTORTION

WITH

ZNFORMATZON

THEORY

SIDE INFORMATION

We know that R(D) bits are sufficient to describe X within distortion D.
We now ask how many bits are required given side information
Y.
We will begin with a few definitions. Let (Xi, Yi> be i.i.d. - p(x, y) and
encoded as shown in Figure 14.32.
Definition:
The rate distortion function with side information
R,(D) is
defined as the minimum
rate required to achieve distortion D if the side
information
Y is available
to the decoder. Precisely, R,(D)
is the
infimum
of rates R such that there exist maps i, : Z” + { 1, . . . , 2nR},
g,:w
x (1,. . . , 2nR} + gn such that
lim sup Ed(X”,

n-bm

g,(Y”, i,vr” ))I 5 D .

(14.279)

Clearly, since the side information
can only help, we have R.(D) 5
R(D). For the case of zero distortion, this is the Slepian-Wolf
problem
and we will need H(XIY)
bits. Hence R,(O) = H(XIY).
We wish to
determine
the entire curve R,(D). The result can be expressed in the
following theorem:
Theorem
14.9.1 (Rate distortion with side information):
drawn Cd. - p(x, y) and Let d(P, P) = A I& d(q, ii)
rate distortion function with side information
is
R,(D)

= Prnj;j mjnU(X,

W) - I(Y; W))

Let (X, Y) be
be given. The

(14.280)

where the minimization
is over all functions f : 9 x ?V+ % and conditional probability
mass functions p(w(x), 1?V~S I%‘( + 1, such that
c

2 c

x w Y

pb,

y)p(wId

db,

fly,

w)) -( D .

(14.281)

The function f in the theorem corresponds to the decoding map that
maps the encoded version of the X symbols and the side information
Y to

Figure 14.32. Rate distortion

with side information.

14.9

RATE

DlSTORTZON

WZTH

SIDE

439

lNFORh4ATlON

the output alphabet. We minimize
over all conditional
distributions
on
W and functions f such that the expected distortion
for the joint
distribution
is less than D.
We first prove the converse after considering some of the properties of
the function R,(D) defined in (14.280).
Lemma
14.9.1: The rate distortion
function
with side information
R.(D) defined in (14.280) is a non-increasing
convex function of D.
Proof: The monotonicity
of R.(D) follows immediately
from the fact
that the domain of minimization
in the definition
of R,(D) increases
with D.
As in the case of rate distortion without side information,
we expect
R,(D) to be convex. However, the proof of convexity is more involved
because of the double rather than single minimization
in the definition
of R.(D) in (14.280). We outline the proof here.
Let D, and D, be two values of the distortion and let WI, fi and Wz, fi
be the corresponding
random variables and functions that achieve the
minima in the definitions of Ry(D1) and R.(D,), respectively. Let Q be a
random variable independent
of X, Y, WI and W, which takes on the
value 1 with probability
A and the value 2 with probability
1 - A.
Define W = (Q, Ws) and let f( W, Y) = fQ( Wo, Y). Specifically fl W, Y) =
f,< WI, Y) with probability
A and fl W, Y) = f,( W,, Y) with probability
1 - A. Then the distortion becomes
D = Ed(X, Jt)

(14.282)

= AEd(X, f,<W,, Y)) + Cl- NE&X,

f,(w,,

Y))

=AD,+(l-A)D,,
and (14.280)
I(W,X)

(14.283)
(14.284)

becomes

- I(W, Y) = H(X) - H(XJW)

-H(Y)

+ H(Y(W)

H(YIW,,Q)

=H(X)-H(XlW,,Q)-H(Y)+

(14.285)

(14.286)

= H(X) - AH(XI WI) - (1 - A)H(X( Wz>
-H(Y)

+ AH(YIW,)

+ (I-

NH(YIW,)

(14.287)

= MI(W,, X) - WV,; y))

+Cl- A)(I(W,,X)
- I<&; Y)),
and hence

(14.288)

440

NETWORK
R,(D)

lNFORh4ATlON

min (I(U;X)-I(U;Y))

=

(14.289)

U :EdsD

(14.290)

Y)

IZ(W,X)-Z(W,

= h(l(W~,X) - WV,; Y)) + (1 - AU~WJ)

- Icw,; YN

= AR.@,) + (1 - W&U&),
proving

the convexity

of R,(D).

We are now in a position
distortion theorem.

THEORY

(14.291)

Cl

to prove the converse to the conditional

rate

Proof (Converse to Theorem 14.9.1): Consider any rate distortion
code with side information.
Let the encoding function be f, : Zn+
(132 , . . . , 2nR}. Let the decoding function be g, : T!P x { 1,2, . . . , 2"R} +
k” and let gni: qn x {1,2, . . . , 2nR} + k denote the ith symbol produced
by the decoding function. Let 2’ = f,<x”) denote the encoded version of
X”. We must show that if E&(X”, g,(Y”,
f,(X”)))
I D, then R 2 R,(D).
- ._
._
We have the following chain of inequalities:

r&z

(a)

H(T)

(14.292)

(2 H(TIY”)

(14.293)

21(X”; TIY”)

(14.294)

~ ~ Z(Xi; TIY”,X’-‘)

(14.295)

i=l

i=l

(14.296)

-

(~’ ~ H(Xi)Yi) - H(X i T, Y’-‘, Yip Yy+l, Xi-‘)

(14.297)

i-l

~ ~ H(Xi)Yi)i==l

H(X i T, Y’-‘, Yip Yy+l)

‘~’ ~ H(Xi(Yi) - H(XiIwi, yi)

(14.298)
(14.299)

i=l

‘~ ~ Z(Xi; Wily)i
i=l

(14.300)

14.9

RATE DISTORTION
= i

441

WITH SIDE 1NFORMATlON
H(W,(y,)

- H(W,(Xi,

Yi>

(14.301)

i=l

-H(Wilxi)

(14.302)

H(Wi)-H(WiIX,>-H(wi>+H(w,(y,)

(14.303)

I(Wi; Xi> - I(Wi; Yi)

(14.304)

Ry(Ed(Xi,

(14.305)

(~ ~ H(Wi(Yi)
i=l

=

i
i=l

= i
i=l

2

2
i=l

=

Tit

$44
i

R,(Ed(X,,

Cj)

g’,i(w,

yi)))

g’,itwi,

yi)))

2 nR,(E k $ldCXi, g',i(Wi, Yi)))

(14.306)
(14.307)

i

(k)

(14.308)

where
(a) follows from the fact that the range of 2’ is { 1,2, . . . , 2nR},
(b) from the fact that conditioning
reduces entropy,
(c) from the chain rule for mutual information,
(d) from the fact that Xi is independent
of the past and future Y’s and
XS
given Yi,
(e) from the fact that conditioning
reduces entropy,
(f) follows by defining Wi = (Z’, Y”-‘, Yy+l ),
(g) follows from the defintion of mutual information,
(h) follows from the fact that since Yi depends only on Xi and is
conditionally
independent
of 2’ and the past and future Y’s, and
therefore Wi + Xi + Yi forms a Markov chain,
(i) follows from the definition
of the (information)
conditional
rate
distortion
function, since % = g,i( T, Y” ) e g’,i( Wi, Yi >, and hence
I( Wi ; Xi ) - I( Wi ; Yi ) 2 minw :Ed(x, 2)s~~ I( W; X) - I( W; Y) = R,(D, ),
(j> follows from Jensen’s inequality
and the convexity of the conditional rate distortion function (Lemma 14.9.1), and
(k) follows from the definition of D = E A Cy=1 d(Xi , I).
Cl

It is easy to see the parallels between this converse and the converse
for rate distortion without side information
(Section 13.4). The proof of

442

NETWORK

INFORMATION

THEORY

achievability
is also parallel to the proof of the rate distortion theorem
using strong typicality.
However, instead of sending the index of the
codeword that is jointly
typical with the source, we divide these
codewords into bins and send the bin index instead. If the number of
codewords in each bin is small enough, then the side information
can be
used to isolate the particular codeword in the bin at the receiver. Hence
again we are combining random binning with rate distortion encoding to
find a jointly typical reproduction
codeword. We outline the details of
the proof below.

Proof (Achievability
of Theorem 14.9.1):
flw, y). Calculate p(w) = C, p(x)p(w Ix).

Fixp(w

Ix) and the function

Generation
of codebook. Let R, = I(X, W) + E. Generate ZnR i.i.d.
codewords
W”(S)
-lly=, p(zq),
and index
them
by s E
{1,2, . . . , znR1}*
Let R, = 1(X, W) - ICY, W) + 5~. Randomly
assign the indices
s E {1,2,. . . , ZnR1} to one of ZnR2 bins using a uniform distribution
over the bins. Let B(i) denote the indices assigned to bin i. There
are approximately
2n(R1-R2) indices in each bin.
Encoding.
Given a source sequence X”, the encoder looks for a
codeword W”(s) such that (X”, W”(s)) E AT’“! If there is no such W”,
the encoder sets s = 1. If there is more than one such s, the encoder
uses the lowest s. The encoder sends the index of the bin in which s
belongs.
Decoding. The decoder looks for a W”(s) such that s E B(i) and
(W”(s), _y”> E AT’“‘. If he finds a unique s, he then calculates p,
where Xi = fl Wi, Yi). If he does not find any such s or more than
one such s, he sets p = P, where in is an arbitrary sequence in 2”.
It does not matter which default sequence is used; we will show
that the probability
of this event is small.
of error. As usual, we have various error
Analysis of the probability
events:
1. The pair (X”, Y” ) $Af”!
The probability
of this event is small for
large enough n by the weak law of large numbers.
2. The sequence X” is typical, but there does not exist an s such that
theorem,
(X”, W”(s)) E A;‘“! As in the proof of the rate distortion
the probability
of this event is small if
R, >I(W,X).
3. The pair

of sequences

(X”, W”(s)) E AT’“’

(14.309)
but (W”(s), Y”)eAf”‘,

14.9

RATE

443

WZTH SZDE 1NFORMATlON

DISTORTION

i.e., the codeword is not jointly typical with the Y” sequence. By
of this event is
the Markov lemma (Lemma 14.&l), the probability
small if n is large enough.
4. There exists another s’ with the same bin index such that
(WV),
Y”) E AT’“! Since the probability
that a randomly chosen
W” is jointly typical with Y” is = 2-nz(Y’ “‘, the probability
that
there is another W” in the same bin that is typical with Y” is
bounded by the number of codewords in the bin times the probability of joint typicality,
i.e.,

(14.310)
which goes to zero since R, - R, c I(Y, W) - 3~.
5. If the index s is decoded correctly, then (X”, W”(s)) E AT’“! By item
1, we can assume that (X”, Y”) EAT’“! Thus by the Markov lemma,
we have (X”, Y”, W”) E AT’“’ and therefore the empirical
joint
distribution
is close to the original distribution
p(x, y)p(w Ix) that
we started with, and hence (X”, p) will have a joint distribution
that is close to the distribution
that achieves distortion D.

Hence with high probability,
the decoder will produce e such that the
distortion between X” and e is close to nD. This completes the proof of
the theorem.
0
The reader is referred to Wyner and Ziv [284] for the details of the
proof.
After the discussion of the various situations of compressing distributed data, it might be expected that the problem is almost completely
solved. But unfortunately
this is not true. An immediate
generalization

X”

I

z- Encoder 1

I
D

i(x”) E 2”RI

Decoder 1

Y”

>A Encoder 2

z (in, h)

D
i(p)

E 2nR2

Figure 14.33. Rate distortion

for two correlated

sources.

NETWORK

INFORMATION

THEORY

of all the above problems is the rate distortion problem for correlated
sources, illustrated
in Figure 14.33. This is essentially the Slepian-Wolf
problem with distortion in both X and Y. It is easy to see that the three
distributed
source coding problems considered above are all special
cases of this setup. Unlike the earlier problems, though, this problem
has not yet been solved and the general rate distortion region remains
unknown.

14.10

GENERAL

MULTITERMINAL

NETWORKS

We conclude this chapter by considering a general multiterminal
network of senders and receivers and deriving some bounds on the rates
achievable for communication
in such a network.
A general multiterminal
network is illustrated
in Figure 14.34. In
this section, superscripts denote node indices and subscripts denote time
indices. There are m nodes, and node i has an associated transmitted
variable Xi’ and a received variable Y”‘. The node i sends information
at
rate R’“’ to node j. We assume that all the messages WC” being sent
from node i to node j are independent
and uniformly
distributed
over
their respective ranges { 1,2, . . . , ZnR(“‘}.
The channel is represented
by the channel transition
function
p(p), . . . , p’ldl’,
. . . , dm) ), which is the conditional
probability
mass
function of the outputs given the inputs. This probability
transition
function captures the effects of the noise and the interference
in the
network. The channel is assumed to be memoryless, i.e., the outputs at
any time instant depend only the current inputs and are conditionally
independent
of the past inputs.

S

l

Figure 14.34.

SC

0

A general multiterminal

(&r

Y,)

network.

14.10

GENERAL

MULTITERMlNAL

445

NETWORKS

Corresponding
to each transmitter-receiver
node pair is a message
wCU) E {1,2, . . . , 2nR(ti) }. The input symbol Xci’ at node i depends on
W”l,jE{l,...,
m}, and also on the past values of the received symbol
pi’ at node i. Hence an encoding scheme of block length n consists of a
set of encoding and decoding functions, one for each node:
. Encoders. x’,“(W’il’,
WCi2’, . . . , W”“‘, Yy’, Y’!:‘, . . . , Y’Lll),
19’ * * 9n. The encoder maps the messages and past received

k=
sym-

bols into the symbol X(,i) transmitted
at time k.
. Decoders. W’j”‘(Yi’,
. . . , Y’,“, WCil’, . . . , Wtim)), j = 1,2, . . . , m. The
decoder j at node i maps the received symbols in each block and his
own transmitted
information
to form estimates of the messages
intended for him from node j, j = 1,2, . . . , m.
Associated with every pair of nodes is a rate and a corresponding
probability
of error that the message will not be decoded correctly,
p$'(G)

where

=pr(@r(ti)(y(j',

wCj1:

...

, wUm))+

w(G)),

(14.311)

pr)(ii)

is defined under the assumption that all the messages are
independent
and uniformly
distributed
over their respective ranges.
A set of rates {I?“‘}
is said to be achievable if there exist encoders
and decoders with block length n with Pr”ti’+
0 as n + 00 for all
i, j E (1,2, . . . , m>.
We use this formulation
to derive an upper bound on the flow of
information
in any multiterminal
network. We divide the nodes into two
sets, S and the complement
SC. We now bound the rate of flow of
information
from nodes in S to nodes in SC.
Theorem
14.10.1: If the information
rates (R’“‘) are achievable, then
there exists some joint probability
distribution
p(x”), xC2),. . . , xCm)), such
that
(14.312)
for all S C {1,2, . . . , m>. Thus the total rate of flow of information
cut-sets is bounded by the conditional
mutual information.

across

Proof: The proof follows the same lines as the proof of the converse
for the multiple
access channel. Let T = {(i, j): i E S, j E SC} be the set
of links that cross from S to SC, and let T” be all the other links in the
network. Then

NETWORK
n

2

iES,

ZNFORh4ATZON

THEORY

(14.313)

R(U)

j&SC

z

2
iES,

H(W”“)

(14.314)

jESc

($&W(T))

(14.315)

$(W’T),W(TC))

(14.316)

= I( wtT);

Cd)
I

Yy),

. . . , y’,““‘I

(14.317)

WTC’)

+ H( w(TqYyC), . . . , PnSC
), WCTC’)

(14.318)

I( WtT); Vy),

(14.319)

. . . , F!f”‘I WtTc’) + ne,

(e)
=

(8)
I

(14.320)

- H(Yy(Y(lsc),

. * . , Y’fTi, WcTC’, WcT)) + ne,

2 H(YylYy

? * * - , Yyf;, wCTC’,xy’)

k=l

- H(Yy(Yy),
(h)
I

i

. . . , Y’ks_“:,WcTC),WcT), Xi”,

H(y’,sc’lXfc’)

Xr”)

X,“‘) + nEn

- H(r’IXr’,

k=l

(14.321)

+ ne,

(14.322)
(14.323)

n

=

C I(tif);

*c’l~sc))

k=l
(i)
=n-

1

n

n zl I(&:‘;

%1(X$

~~c)l&~c’,

pF)IXz’),

= n(H(y’BSc)I~~),

+ mn

(14.324)

Q = k) + ne n

(14.325)

Q) + ne,
Q) - H(F~c’IX’$“,

(14.326)
Pi”,

Q)) + nq,

(14.327)

(k)

5 n(H(~~‘l*~c’)

- H(~~‘IX!~‘,

(0
5 n(H(F~‘IX~c’)

- H(y’B”c)Ix(gs), 2:“))

= nI(Pi’;

y’B”“‘lP~c’)

+ ne, ,

X”“,

Q)) + nq,

(14.328)

+ nc,

(14.329)
(14.330)

14.10

GENERAL

MULTITERMINAL

NETWORKS

where
(a) follows from the fact that the messages WC” are uniformly
distributed
over their respective ranges { 1,2, . . . ,Z”@“)},
(b) follows from the definition of WCT) = { W’“’ : i E S, j E SC} and the
fact that the messages are independent,
(c) follows f rom the independence of the messages for 2’ and T”,
(d) follows f rom Fano’s inequality
since the messages W’*) can be
decoded from Y(s) and WfTc),
(e) is the chain rule for mutual information,
(f) follows from the definition of mutual information,
(g) follows from the fact that Xfc’ is a function of the past received
symbols Y@” and the messages WCTC) and the fact that adding
conditioning
reduces the second term,
(h) from the fact that y’ksc) depends only on the current input symbols
Xr’ and Xr),
(i) follows after we introduce a new timesharing
random variable Q
uniformly
distributed
on {1,2, . . . , n},
(j) follows from the definition of mutual information,
(k) follows f rom the fact that conditioning
reduces entropy, and
(1) follows from the fact that ptc’ depends only the inputs Xl) and
Xrc) and is conditionally
independent
of Q.
Thus there exist random variables X@’ and XCSc) with some arbitrary
joint distribution
which satisfy the inequalities
of the theorem.
Cl
The theorem has a simple max-flow-min-cut
interpretation.
The rate
of flow of information
across any boundary is less than the mutual
information
between the inputs on one side of the boundary and the
outputs on the other side, conditioned
on the inputs on the other side.
The problem of information
flow in networks would be solved if the
bounds of the theorem were achievable. But unfortunately
these bounds
are not achievable even for some simple channels. We now apply these
bounds to a few of the channels that we have considered earlier.
l

Multiple
access channel. The multiple access channel is a network
with many input nodes and one output node. For the case of a
two-user multiple
access channel, the bounds of Theorem 14.10.1
reduce to

R,5 ex~;YIX2))

(14.331)

R+I(X,;

(14.332)

YIX,),

R,+R,~I(X,,X,;Y)

(14.333)

NETWORK

448

Figure

l

14.35.

INFORMATION

THEORY

The relay channel.

for some joint distribution
p(xl , x&( y 1x1, x2>. These bounds coincide with the capacity region if we restrict the input distribution
to
be a product distribution
and take the convex hull (Theorem
14.3.1).
Relay channel. For the relay channel, these bounds give the upper
bound of Theorem 14.7.1 with different choices of subsets as shown
in Figure 14.35. Thus
C 5 sup min{l(X,
Pk Xl)

Xl; Y), 1(X; Y, Y1 IX, )} .

This upper bound is the capacity of a physically
channel, and for the relay channel with feedback

(14.334)

degraded
[67].

relay

To complement
our discussion of a general network, we should
mention two features of single user channels that do not apply to a
multi-user
network.
. The source channel

separation theorem. In Section 8.13, we discussed the source channel separation theorem, which proves that
we can transmit the source noiselessly over the channel if and only
if the entropy rate is less than the channel capacity. This allows us
to characterize a source by a single number (the entropy rate) and
the channel by a single number (the capacity).
What about the multi-user
case? We would expect that a distributed source could be transmitted
over a channel if and only if the
rate region for the noiseless coding of the source lay within the
capacity region of the channel. To be specific, consider the transmission of a distributed
source over a multiple
access channel, as
shown in Figure 14.36. Combining
the results of Slepian-Wolf
encoding with the capacity results for the multiple
access channel,
we can show that we can transmit the source over the channel and
recover it with a low probability
of error if

14.10

GENERAL

MULTZTERMINAL

449

NETWORKS

u -x,
Pw,, +,I
If -x,

Figure 14.36. Transmission

=

Y‘(G)

)I

of correlated

sources over a multiple

MU,V)~I(x,,x,;Y,Q)

access channel.

(14.337)

for some distribution
p( q)p(x, 1~)JI(x, 1q)p( y 1x1, x2 1. This condition
is equivalent
to saying that the Slepian-Wolf
rate region of the
source has a non-empty intersection with the capacity region of the
multiple
access channel.
But is this condition also necessary? No, as a simple example
illustrates.
Consider the transmission
of the source of Example
14.4 over the binary erasure multiple
access channel (Example
14.3). The Slepian-Wolf
region does not intersect the capacity
region, yet it is simple to devise a scheme that allows the source to
be transmitted
over the channel. We just let XI = U, and X, = V,
and the value of Y will tell us the pair (U, V) with no error. Thus
the conditions (14.337) are not necessary.
The reason for the failure of the source channel separation
theorem lies in the fact that the capacity of the multiple
access
channel increases with the correlation
between the inputs of the
channel. Therefore, to maximize the capacity, one should preserve
the correlation
between the inputs of the channel. Slepian-Wolf
encoding, on the other hand, gets rid of the correlation.
Cover, El
Gamal and Salehi [69] proposed an achievable region for transmission of a correlated source over a multiple
access channel based on
the idea of preserving the correlation.
Han and Costa [131] have
proposed a similar
region for the transmission
of a correlated
source over a broadcast channel.
Capacity regions with feedback. Theorem 8.12.1 shows that feedback does not increase the capacity of a single user discrete
memoryless
channel. For channels with memory, on the other
hand, feedback enables the sender to predict something about the
noise and to combat it more effectively, thus increasing capacity.

NETWORK

450

INFORMATION

THEORY

What about multi-user
channels? Rather surprisingly,
feedback
does increase the capacity region of multi-user
channels, even
when the channels are memoryless.
This was first shown by
Gaarder and Wolf [ 1171, who showed how feedback helps increase
the capacity of the binary erasure multiple
access channel. In
essence, feedback from the receiver to the two senders acts as a
separate channel between the two senders. The senders can decode
each other’s transmissions
before the receiver does. They then
cooperate to resolve the uncertainty
at the receiver, sending information at the higher cooperative capacity rather than the noncooperative capacity. Using this scheme, Cover and Leung [73]
established an achievable region for multiple
access channel with
feedback. Willems [273] showed that this region was the capacity
for a class of multiple
access channels that included the binary
erasure multiple
access channel. Ozarow [204] established
the
capacity region for the two user Gaussian multiple access channel.
The problem of finding the capacity region for the multiple
access
channel with feedback is closely related to the capacity of a
two-way channel with a common output.
There is as yet no unified theory of network information
flow. But
there can be no doubt that a complete theory of communication
networks would have wide implications
for the theory of communication
and computation.

SUMMARY

OF CHAPTEIR 14

Multiple access channel: The capacity of a multiple accesschannel (EI x gz,
p( y Ix,, x,), 3 ) is the closure of the convex hull of all (R,, RJ satisfying
YIX,),

(14.338)

R, < Kq; YIX, 1,

(14.339)

R, -Mx~;

R, +~~<w~,&;

Y)

(14.340)

for some distribution pl(xl)&,)
on & x &..
The capacity region of the m-user multiple accesschannel is the closure of
the convex hull of the rate vectors satisfying
R(S) 5 Z(X(S); YIX(S”))

for all S C {1,2, . . . , m}

for some product distribution pl(xl)p,(z,)

. . . p,(q,,).

(14.341)

SUMMARY

OF CHAPTER

14

R,+R,sC(f#,

(14.344)

(14.345)

C(x) = ; log(1 +x) .

Slepian-Wolf
coding. Correlated sources X and Y can be separately described at rates R, and R, and recovered with arbitrarily low probability of
error by a common decoder if and only if

R, > H(XIY) ,

(14.346)

R, > HWIX) ,

(14.347)

R,+R,>H(X,Y).

(14.348)

Broadcast
channels:
The capacity region of the degraded broadcast channel X-* Y1 + Yz is the convex hull of the closure of all (RI, R,) satisfying

for some joint distribution

R, = NJ; Y,> ,

(14.349)

R,=Z(X,Y,IU)

(14.360)

p(u)p(~iu)p(y~,

y,lx).

Relay channel: The capacity C of the physically
p(y, yll~,~,) is given by

degraded relay channel

C = p~ufl) min{Z(X, Xl; Y), 1(x; Yl IX, 1) ,
where the supremum

is over all joint distributions

(14.361)

on 8? x gl.

Source coding with aide information:
Let (X, Y) -p(x, y). If Y is encoded
at rate R, and X is encoded at rate R,, we can recover X with an arbitrarily
small probability of error iff

R, NiUIU),

(14.362)

452

NETWORK

R,rl(Y,

lNFORh4ATlON

U)

THEORY

(14.353)

for some distribution p( y, u), such that X+ Y+ U.
Rate distortion with side information: Let (X, Y) -p(=c, y). The rate
distortion function with side information is given by
R,(D)=

min

min 1(X; W)-I(Y,

Pb Ix)pB x w-d

W),

(14.354)

where the minimization is over all functions f and conditional distributions
p(wjx), Iw”l I I%‘1+ 1, such that
z z z p(x, y)ph.ulM~,
x UJ Y

PROBLEMS
1.

(14.355)

fly, ~1) 5 D .

FOR CHAPTER 14

The cooperative capacity of a multiple accesschannel. (See Figure
14.37.)

Figure

14.37.

Multiple

access channel with cooperating

senders.

(a) SupposeXI and Xz have accessto both indices WI E { 1, 2nR}, Wz E
{ 1, ZnR2}. Thus the codewords X1(WI, W,), X,( WI, W,) depend on
both indices. Find the capacity region.
(b) Evaluate this region for the binary erasure multiple access
channel Y = XI + Xz, Xi E (0, 1). Compare to the non-cooperative
region.
2. Capacity of multiple accesschannels.Find the capacity region for each
of the following multiple accesschannels:
(a) Additive modulo 2 multiple access accesschannel. XI E (0, l},
x,E{0,1},Y=X,$X,.
(b) Multiplicative multiple accesschannel. XI E { - 1, l}, Xz E { - 1, l},
Y=X, ‘X2.
3.

Cut-set interpretation of capacity region of multiple accesschannel. For
the multiple accesschannel we know that (R,, R2) is achievable if

R, <K&; YlX,>,

(14.356)

R, < I(&; YIX, 1,

(14.357)

PROBLEMS

FOR

CHAPTER

453

14

R, +&o&,X,;
for X1, Xz independent.

(14.358)

Y>,

Show, for X1, X2 independent,
1(X,; YIX,) = I(x,;

that

Y, x,>.

Y

Interpret the information
cutsets S,, S, and S,.
4.

bounds as bounds on the rate of flow across

Gaussian multiple access channel cupacify. For the AWGN multiple
access channel, prove, using typical sequences, the achievability of
any rate pairs (R,, R,) satisfying
R&og

( 1+&l

(14.359)

1,

(14.360)
.

(14.361)

The proof extends the proof for the discrete multiple access channel
in the same way as the proof for the single user Gaussian channel
extends the proof for the discrete single user channel.
5.

Converse for the Gaussian multiple uccess channel. Prove the converse
for the Gaussian multiple access channel by extending the converse
in the discrete case to take into account the power constraint on the
codewords.

6.

Unusual multiple uccess channel. Consider the following multiple access channel: 8$ = Z& = ?!/= (0, 1). If (X1, X,) = (0, 0), then Y = 0. If
If (X1,X,)=(1,0),
then Y=l.
If
(Xl, X2> = (0, 11, th en Y=l.
(X1, X,) = (1, l), then Y = 0 with probability i and Y = 1 with probability 4.
(a) Show that th e rate pairs (1,O) and (0,l) are achievable.
(b) Show that f or any non-degenerate distribution
p(rl)p(z,),
we
have 1(X1, Xz; Y) < 1.
(c) Argue that there are points in the capacity region of this multiple
access channel that can only be achieved by timesharing,
i.e.,
there exist achievable rate pairs (RI, R,) which lie in the capacity
region for the channel but not in the region defined by

R, 5 I(&; Y(X,),

(14.362)

454

NETWORK

ZNFORMATlON

R, 5 I(&; Y(X, 1,
R, +R,~I(X,,X,;

Y)

THEORY

(14.363)
(14.364)

for any product distribution p(xl)p(x,). Hence the operation of
convexification strictly enlarges the capacity region. This channel
was introduced independently by Csiszar and Korner [83] and
Bierbaum and Wallmeier [333.
7.

Convexity of capacity region of broadcastchannel. Let C G R2 be the
capacity region of all achievable rate pairs R = (R,, R,) for the
broadcast channel. Show that C is a convex set by using a timesharing argument.
Specifically, show that if R(l) and Rc2’are achievable, then AR(l) +
(1 - A)Rc2)is achievable for 0 I A 5 1.

8. Slepian-Wolf for deterministically related sources.Find and sketch the
Slepian-Wolf rate region for the simultaneous data compression of
(X, Y), where y = f(x) is some deterministic function of x.
9. Slepian-Wolf. Let Xi be i.i.d. Bernoulli(p). Let Zi be i.i.d. - Bernoulli(r), and let Z be independent of X. Finally, let Y = X63 Z (mod 2
addition). Let X be described at rate R, and Y be described at rate R,.
What region of rates allows recovery of X, Y with probability of error
tending to zero?
10.

Broadcastcapacity dependsonly on the conditional marginals.Consider
the general broadcast channel (X, YI x Y2, p(yl, y21x)). Show that the
capacity region depends only on p(y,lx) and p(y,)x). To do this, for
any given ((2”R1,2nR2),n) code, let

P:“’ = P{WJY,)

# Wl} ,

(14.365)

PF’ = P{*2(Y2) # W2} ,

(14.366)

P = P{(bv,, Iv,> # cw,, W,>} .

(14.367)

Then show

The result now follows by a simple argument.
Remark: The probability of error Pen’does depend on the conditional joint distribution p(y I, y21x). But whether or not Pen’ can be
driven to zero (at rates (RI, R,)) does not (except through the conditional marginals p( y 1Ix), p( y2 Ix)).
11.

Conversefor the degradedbroadcastchannel. The following chain of
inequalities proves the converse for the degraded discrete memoryless broadcast channel. Provide reasons for each of the labeled
inequalities.

PROBLEMS

FOR

CHAPTER

455

14

Setup for converse for degraded broadcast channel capacity
cwl$

+xyw1,

W2)indep.

w,>-+

yn+zn

Encoding
f, :2nRl x gnR2_)gfy””
Decoding
g,: 9P+2nRl,
Let Vi = (W,, P-l).
fi,

h, : 2fn + 2nR2

Then

2 Fan0mv,; 2”)

(14.368)

‘2 i

(14.369)

I(W,; zi pF)

i=l
(L)c

(H(Zip?-L)

-

H(Zi

Iw,,

P1)>

(14.370)

2x (H(q) - H(ZilWZ, f-l, yi-1))

(14.371)

zx W(Zi)
- H(Z,
Iw,,
y”-l))

(14.372)

2) i I(ui;zi).

(14.373)

i

i=l

Continuation
equalities:

of converse. Give reasons for the labeled innR, k Fan0I( Wl; Y”>

(14.374)

(f)
5 I(W,;

Y”, w,>

(14.375)

(2)I(W,;

Y”IW,)

(14.376)

‘2 i I(W,; Yip-,

W,)

(14.377)

i-l

~ ~ I(Xi; Yi(Ui) I

(14.378)

i-1

12. Capacity poinfs.
(a> For the degraded broadcast channel X-, YI + Yz, find the points
a and b where the capacity region hits the R, and R, axes (Figure
14.38).
(b) Show that b 5 a.

NETWORK

456

a

1NFORMATION

THEORY

Rl

Figure 14.38. Capacity region of a broadcast channel.

13. Degradedbroadcastchannel. Find the capacity region for the degraded
broadcast channel in Figure 14.39.
1 -P

1 -P

Figure 14.39. Broadcast channel-BSC

and erasure channel.

14.

Channelswith unknown parameters.We are given a binary symmetric
channel with parameter p. The capacity is C = 1 - H(p).
Now we change the problem slightly. The receiver knows only that
p E {pl, p,}, i.e., p =pl or p =p2, where p1 and pz are given real
numbers. The transmitter knows the actual value of p. Devise two
codesfor use by the transmitter, one to be used if p = pl, the other to
be used if p = p2, such that transmission to the receiver can take
place at rate = C(p,) ifp =pr and at rate = C(p,) ifp =pz.
Hint: Devise a method for revealing p to the receiver without
affecting the asymptotic rate. Prefixing the codeword by a sequenceof
l’s of appropriate length should work.

15.

Two-way channel. Consider the two-way channel shown in Figure
14.6. The outputs YI and Yz depend only on the current inputs XI and
x2!*
(a) By using independently generated codesfor the two senders,show
that the following rate region is achievable:
(14.379)

R, < eq; Y#J
for some product distribution p(x,)p(x,)p(y,,

(14.380)
Y~~x~,x2).

HISTORICAL

457

NOTES

(b) Show that the rates for any code for a two-way
arbitrarily

small probability

channel with

of error must satisfy

R, 5 1(x,; YJXJ

(14.382)

for somejoint distribution p(xl, x,)p(y,, y21x,, x,1.
The inner and outer bounds on the capacity of the two-way
channel are due to Shannon [246]. He also showed that the inner
bound and the outer bound do not coincide in the case of the binary
multiplying channel ZI = Z& = (?I1= %z= (0, l}, YI = Yz = X1X2. The
capacity of the two-way channel is still an open problem.

HISTORICAL

NOTES

This chapter is based on the review in El Gamal and Cover [98]. The two-way
channel was studied by Shannon
[246] in 1961. He derived inner and outer
bounds on the capacity region. Dueck [90] and Schalkwijk
[232,233] suggested
coding schemes for two-way channels which achieve rates exceeding Shannon’s
inner bound; outer bounds for this channel were derived by Zhang, Berger and
Schalkwijk
[287] and Willems and Hekstra [274].
[3] and
The multiple
access channel capacity region was found by Ahlswede
Liao [178] and was extended to the case of the multiple
access channel with
common information
by Slepian and Wolf [254]. Gaarder and Wolf [117] were the
first to show that feedback increases the capacity of a discrete memoryless
multiple access channel. Cover and Leung [73] proposed an achievable region for
the multiple access channel with feedback, which was shown to be optimal for a
accesschannels by Willems [273]. Ozarow [204] has determined
class of multiple
the capacity region for a two user Gaussian multiple access channel with
feedback.
Cover, El Gamal and Salehi [69] and Ahlswede
and Han [6] have
considered
the problem
of transmission
of a correlated
source over a multiple
access channel.
The Slepian-Wolf
theorem was proved by Slepian and Wolf [255], and was
extended to jointly ergodic sources by a binning
argument
in Cover [63].
Broadcast channels were studied by Cover in 1972 [60]; the capacity region for
the degraded broadcast channel was determined
by Bergmans [31] and Gallager
[119]. The superposition
codes used for the degraded broadcast channel are also
optimal for the less noisy broadcast channel (Kiirner and Marton [160]) and the
more capable broadcast channel (El Gamal [97]) and the broadcast channel with
degraded
message sets (Kiirner
and Marton
[161]). Van der Meulen
[26] and
Cover [62] proposed
achievable regions for the general broadcast channel. The
best known achievable
region for broadcast channel is due to Marton [189]; a
simpler proof of Marton’s
region was given by El Gamal and Van der Meulen
[loo]. The deterministic
broadcast channel capacity was determined
by Pinsker
[211] and Marton [189]. El Gamal [96] showed that feedback does not increase the
capacity of a physically degraded broadcast channel. Dueck [91] introduced
an
example to illustrate
that feedback could increase the capacity of a memoryless

458

NETWORK INFORMATION

THEORY

broadcast channel; Ozarow and Leung [205] described a coding procedure for the
Gaussian broadcast channel with feedback which increased the capacity region.
The relay channel was introduced by Van der Meulen [262]; the capacity
region for the degraded relay channel was found by Cover and El Gamal[67]. The
interference channel was introduced by Shannon [246]. It was studied by
Ahlswede [4], who gave an example to show that the region conjectured by
Shannon was not the capacity region of the interference channel. Carleial [49]
introduced the Gaussian interference channel with power constraints,
and
showed that very strong interference is equivalent to no interference at all. Sato
and Tanabe [231] extended the work of Carleial to discrete interference channels
with strong interference. Sato [229] and Benzel [26] dealt with degraded interference channels. The best known achievable region for the general interference
channel is due to Han and Kobayashi [132]. This region gives the capacity for
Gaussian interference channels with interference parameters greater than 1, as
was shown in Han and Kobayashi [132] and Sato [230]. Carleial [48] proved new
bounds on the capacity region for interference channels.
The problem of coding with side information was introduced by Wyner and
Ziv [283] and Wyner [280]; the achievable region for this problem was described
in Ahlswede and Klimer [7] and in a series of papers by Gray and Wyner [125]
and Wyner [281,282]. The problem of finding the rate distortion function with
side information was solved by Wyner and Ziv [284]. The problem of multiple
descriptions is treated in El Gamal and Cover [99].
The special problem of encoding a function of two random variables was
discussed by Khmer and Marton [162], who described a simple method to encode
the modulo two sum of two binary random variables. A general framework for
the description of source networks can be found in Csiszar and Khmer [82], [83].
A common model which includes Slepian-Wolf encoding, coding with side
information,
and rate distortion with side information as special cases was
described by Berger and Yeung [3O].
Comprehensive
surveys of network information theory can be found in El
Gamal and Cover [98], Van der Meulen [262,263,264], Berger [28] and Csiszar and
Khmer [83].

Elements of Information Theory
Thomas M. Cover, Joy A. Thomas
Copyright  1991 John Wiley & Sons, Inc.
Print ISBN 0-471-06259-6 Online ISBN 0-471-20061-1

Chapter 15
