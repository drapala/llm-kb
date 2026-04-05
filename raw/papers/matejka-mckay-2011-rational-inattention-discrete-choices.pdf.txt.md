# matejka-mckay-2011-rational-inattention-discrete-choices.pdf — Texto extraído de PDF

**Metadados da conversão:**
- Tamanho original: 788K
- Páginas: 29
- Convertido em: 2026-04-05
- Ferramenta: pdftotext (poppler)

---

RATIONAL INATTENTION
TO DISCRETE CHOICES:
A NEW FOUNDATION FOR
THE MULTINOMIAL LOGIT MODEL

Filip Matějka
Alisdair McKay

CERGE-EI
Charles University
Center for Economic Research and Graduate Education
Academy of Sciences of the Czech Republic
Economics Institute

WORKING PAPER SERIES (ISSN 1211-3298)
Electronic Version

442

Working Paper Series
(ISSN 1211-3298)

442

Rational Inattention to Discrete Choices:
A New Foundation for
the Multinomial Logit Model
Filip Matějka
Alisdair McKay

CERGE-EI
Prague, June 2011

ISBN 978-80-7343-244-7 (Univerzita Karlova. Centrum pro ekonomický výzkum
a doktorské studium)
ISBN 978-80-7344-236-1 (Národohospodářský ústav AV ČR, v.v.i.)

Rational Inattention to Discrete Choices: A New Foundation for
the Multinomial Logit Model†
Filip Matějka∗ and Alisdair McKay∗∗
June 21, 2011

Abstract
Often, individuals must choose among discrete alternatives with imperfect information
about their values, such as selecting a job candidate, a vehicle or a university. Before choosing, they may have an opportunity to study the options, but doing so is costly. This costly
information acquisition creates new choices such as the number of and types of questions
to ask the job candidates. We model these situations using the tools of the rational inattention approach to information frictions (Sims, 2003). We find that the decision maker’s
optimal strategy results in choosing probabilistically exactly in line with the multinomial
logit model. This provides a new interpretation for a workhorse model of discrete choice
theory. We also study cases for which the multinomial logit is not applicable, in particular
when two options are duplicates. In such cases, our model generates a generalization of the
logit formula, which is free of the limitations of the standard logit.
Abstract
Vsichni musı́ občas vybı́rat mezi diskrétnı́mi alternativami, jako vybrat kandidáta na
zaměstnánı́, dopravnı́ prostředek nebo vhodnou školu. Před výběrem mohou prozkoumat
jednotlivě možnosti, což je však nákladné. V tomto článku modelujeme tento proces pomoci
teorie rational inattention (Sims, 2003). Zjistili jsme, že takto racionálně nepozorný agent
vybı́rá mezi jednotlivými nabı́dkami přesně podle logit modelu. Náš model tedy poskytuje
novou interpretaci pro logit, ale i opravuje jeho nedostatky.

Keywords: rational inattention, discrete choice, logit model.
JEL: D81, D83, D01.

†

We thank Christopher Sims, Per Krusell, and Christian Hellwig for helpful discussions.
Center for Economic Research and Graduate Education, joint workplace of Charles University and the
Academy of Sciences of the Czech Republic, Prague. filip.matejka@cerge-ei.cz
∗∗
Boston University. amckay@bu.edu.
∗

1

1

Introduction

At times, individuals must choose among discrete alternatives with imperfect information about
the value of each alternative. Before making a choice, one often has an opportunity to study
the options. In most cases, however, it is too costly to investigate the options to the point
where their values are known with certainty and, as a result, some uncertainty about the
values remains when one chooses among the options. Because of this uncertainty, the option
that is ultimately chosen may not be the one that provides the highest utility to the decision
maker (DM). Moreover, the noise in the decision process may lead identical individuals to make
different choices. That is, imperfect information naturally leads choices to contain errors and
be probabilistic as opposed to deterministic.
In this context, the DM faces choices of how much to study the options and what to investigate when doing so. For example, a firm might choose how long to spend interviewing
candidates for a job and choose what to ask them during the interview. After completing the
interview, the firm faces a discrete choice among the candidates.
We explore the optimal “information processing” behavior of a DM for whom acquiring
information is costly and characterize the resulting choice behavior in a discrete choice context.
As choices are probabilistic, our characterization involves describing the probability with which
the DM selects a particular option in a particular choice situation. Specifically, we model the
cost of acquiring and processing information using the rational inattention framework introduced
by Sims (1998, 2003).
The major appeal of the rational inattention approach is that it does not impose any particular assumptions on what agents learn or how they go about learning it. Instead, the rational
inattention approach derives the information structure from the utility-maximizing behavior
of the agents for whom information is costly to acquire. As a result, rationally inattentive
agents process information they find useful and ignore information that is not worth the effort
of acquiring and processing.
Our main finding is that the resulting choice probabilities follow the multinomial logit formula, but modified to incorporate prior information about the values of the options. According
to the multinomial logit formula, the DM selects option i ∈ {1, · · · , N } with probability
eqi /λ
PN q /λ ,
j
j=1 e
where qi is the value of option i and λ is a scale parameter. The scale parameter controls the
amount of noise in the choice probabilities. As λ goes to zero, the DM selects the option with
the highest value with probability one. As λ goes to infinity, the DM selects all options with
probability 1/N . In our work, the scale parameter is exactly equal to the marginal cost of a
unit of information.
The multinomial logit model is the most commonly used model of discrete choice behavior
and is one of the principal tools of applied researchers studying discrete choices (McFadden,
1974). The multinomial logit is also used in industrial organization as a model of consumer
demand (Anderson et al., 1992), and it is used in experimental economics to capture an element
of bounded rationality in subject behavior (McKelvey and Palfrey, 1995). It is so widely used
because it is particularly tractable both analytically and computationally and because it has a
connection to consumer theory through a random utility model.
We distinguish between two cases depending on what the DM knows about the options before acquiring information. If the DM views the options symmetrically a priori, then he or she
chooses according to the multinomial logit formula above. In other cases, the DM might have

2

some prior information that will inform his or her choice. We therefore also analyze the more
general model in which the DM incorporates prior knowledge of the options into the choice.
In this context, we arrive at a model that can be interpreted as a multinomial logit in which
the value of each option is shifted by an amount that reflects its a priori attractiveness. One
implication of these adjustments for a priori attractiveness is that the generalized model does
not have the independence of irrelevant alternatives property, which is a feature of the multinomial logit that has been criticized for generating counterintuitive predictions. Importantly,
these results do not depend on any distributional assumptions about the DM’s prior knowledge.
There are two canonical derivations of the multinomial logit.1 First, the multinomial logit
can be derived from Luce’s (1959) Choice Axiom. Second, the multinomial logit can be derived
from a random utility model. According to that derivation, the DM evaluates the options
with some noise either due to randomness in his or her evaluation of the alternatives or due to
some unobserved factor that is known to the agent, but unknown to the economic modeler. If
the noise in the evaluation is additively separable and independently distributed according to
the extreme value distribution, then the multinomial logit model emerges.2 The extreme-value
distributed noise is often interpreted in terms of idiosyncratic tastes that are not observable to
the analyst, but it is also sometimes interpreted as errors of perception (e.g. McFadden, 1980,
p. S15).
We believe our findings are important for two reasons. First, the wide popularity of the
multinomial logit is in part due to its connection to the random utility model. This foundation
allows researchers to interpret the choice probabilities in terms of optimizing behavior. While
the logit model is sometimes used in situations in which information frictions are thought to be
an important part of the choice environment, we are not aware of previous work that justifies
the use of the logit model in terms of a fully specified model of information frictions. Second,
most existing work with rational inattention has focused on situations where the DM chooses
from a continuous choice set.3 In this context, the model remains tractable if one assumes
the agent is acquiring information about a normally-distributed quantity and the objective
function is quadratic, as under these assumptions the DM chooses normally distributed signals.
Beyond this situation, however, the continuous-choice rational inattention model must be solved
numerically. In contrast, we show here that the discrete-choice version of the rational inattention
model is extremely tractable. Because discrete choices arise in many economic contexts, we
expect that these results will be useful in applying the rational inattention framework to a
number of questions.
Using our new derivation of the logit model we can view its features and flaws from a
different perspective. For example, we can address Debreu’s (1960) well-known criticism of
the multinomial logit. Debreus’s critique is best presented in the form of an example: The
agent is confronted with a choice between a yellow bus and a train and selects each with
probability 1/2. If a red bus is introduced to the choice set and the agent is thought to be
indifferent between the two buses, then it makes sense to think that each bus is equally likely
to be selected. Then it follows from the multinomial logit that each of the buses and the
train is selected with probability 1/3. Debreu argued that this is counterintuitive because
1

See McFadden (1976), Anderson et al. (1992), and Train (2009) for surveys.
Luce and Suppes (1965, p. 338) attribute this result to Holman and Marley (unpublished). See McFadden
(1974) and Yellott (1977) for the proof that a random utility model generates the logit model only if the noise
terms are extreme value distributed.
3
Rational inattention has mostly been applied in macroeconomic contexts. The major applications have been
consumption-savings problems (Sims, 2006; Luo, 2008; Tutino, 2009), price setting (Mackowiak and Wiederholt,
2009; Woodford, 2009; Matejka, 2010a,b), and portfolio choices (Van Nieuwerburgh and Veldkamp, 2010; Mondria,
2010). In a microeconomic context, Yang (2010) uses rational inattention to endogenize the information structure
in a global game.
2

3

duplicating one option should not materially change the choice problem. We formalize the
notion of duplicate options as a scenario in which two options have perfectly correlated values.
That is, the prior is asymmetric because the correlation between two options is higher than it
is between other pairs of options. Given this asymmetry in the prior, we no longer expect the
multinomial logit to hold exactly, but rather the values should be adjusted for their a priori
attractiveness. We show that in this situation, the rationally inattentive agent does not display
the counterintuitive behavior that Debreu criticized. In particular, we show that a rationally
inattentive agent treats two duplicate options as a single option. In the bus example, the DM
chooses each bus with probability 1/4 and the train with probability 1/2.
When Debreu presented the critique that is now known as the bus problem, he was responding to Luce’s Choice Axiom from which the multinomial logit follows. The central idea of the
Choice Axiom is the property of independence of irrelevant alternatives (IIA), which states that
the ratio of choice probabilities associated with two options should not depend on the other
options that are available. Given that we have just claimed that the rationally inattentive agent
violates this property in the bus problem, one might reasonably ask how our work still generates
a multinomial logit. The answer is that when the prior is asymmetric, the values of the options
are adjusted for their a priori attractiveness. This adjustment breaks the IIA property. Yet,
when the options are a priori symmetric, they have the same a priori attractiveness. In this
case, no adjustment occurs and the IIA property holds.
The rational inattention framework uses information theory (Shannon, 1948) to measure
the amount of information that the DM acquires about the choice environment. In information
theory, a probability distribution is associated with an amount of entropy. If one acquires some
information that leads to a reduction in uncertainty, the entropy of the posterior distribution is
smaller than the entropy of the prior distribution. The reduction in entropy is a measure of the
amount of information that has been acquired. Luce (1959) notes that there is a close connection
between Shannon’s axiomatic derivation of entropy as a natural measure of information and the
Choice Axiom.
The paper is organized as follows, after reviewing the most closely related literature, we
turn to a presentation of the problem faced by the rationally inattentive agent in section 2. We
then analyze the model’s predictions for a generic prior in section 3. Section 4 considers the
case when the options are a priori symmetric and provides the connection to the multinomial
logit. In section 5, we discuss cases where the options are not symmetric a priori, including the
possibility that two of the options are duplicates.
Related Literature There is an extensive literature on discrete choice theory including other
generalizations of the multinomial logit model. The best known example is the nested logit
(Ben-Akiva, 1973; Daly and Zachary, 1979; Williams, 1977). Many of these generalizations
were designed to break the IIA property. Here we focus on those discrete choice theories that
are most closely related to our work.
Gul et al. (2010) have proposed a new axiomatic foundation for the multinomial logit that
weakens Luce’s Choice Axiom. While, the Choice Axiom states that the ratio of selection probabilities should remain unchanged as the choice set varies, Gul et al. only require that the
ordering of selection probabilities remains unchanged. They show that if there is sufficient variety of choices and the ordering of selection probabilities is stable, then the selection probabilities
must follow a logit model.
There are several papers that explicitly look at information frictions in a discrete choice
setting. Weibull et al. (2007) consider a discrete choice problem in which the DM receives
signals about the options before making the choice and allow the DM to select the precision
of the signals at a cost. When the signals are additively separable from the true values of the
4

options and are drawn from the extreme value distribution, the result is a multinomial logit in
which the DM can choose the scale parameter. That their model takes the logit form is not
surprising as mathematically it is still the random utility model, but the interpretation is now
different from the usual one because the DM does not know which option is best. Weibull et al.
show that this interpretation can lead to surprising situations in which an improvement in the
value of each option can lead the DM’s expected utility to fall. In these cases, the good and bad
options become more difficult to tell apart and the DM is more likely to choose a bad option.
Recently, Natenzon (2010) has proposed a model in which the DM has Gaussian priors on
the utilities of the options and then receives Gaussian signals about the utilities. As more signals
are collected, the DM updates his or her posterior and when forced to make a choice, selects the
option with the highest posterior mean utility. Natenzon shows that this model can reconcile
two seemingly contradictory phenomena. In some situations, introducing a similar option, such
as a second bus, disproportionately reduces the probability that the original option (the first
bus) is selected. In other situations, introducing a similar option raises the probability that
original option is selected. The latter phenomenon is known as the attraction effect in the
marketing literature. Natenzon’s model can generate both of these effects.
A key difference difference between these models and ours is that we consider an agent who
is actively seeking out the most important information about the alternatives while Weibull
et al.’s and Natenzon’s DMs are either responding to an exogenous information structure or
choosing the amount, but not type, of information to acquire.
Finally, while various connections between Shannon’s concept of entropy and the multinomial logit model have been known for some time, we believe the link we make here is new.
Specifically, the use of information theory to formulate an information flow constraint on an
individual’s decision problem does not appear before Sims’s work on rational inattention and we
are not aware of any previous attempts to consider discrete choices in this framework. Perhaps
the closest to our line of reasoning are Mattsson and Weibull (2002) and the related work of
Stahl (1990). These authors consider the problem of an agent who knows which option is best,
but can only implement that decision with some noise. These authors allow for mixed strategies
and treat the agent’s choice as a vector of probabilities of selecting each option. The agent is
penalized to the extent that the choice that is implemented differs from some default option.
These authors use information theoretic concepts to measure the distance between the chosen
probabilities and the default probabilities. If the default option is a uniform distribution, then
the resulting choice probabilities follow the multinomial logit. Our work differs in that we explicitly link the agent’s difficulty in implementing the correct decision to the cost of processing
information about the options.

2

The model

The DM is presented with a group of N options. The values of these options potentially differ,
and the agent wishes to select the option with the highest value. Let qi denote the value of the
selected option i ∈ {1..N }. Initially, the agent possesses some knowledge about the available
option and this prior knowledge can be described by a joint probability distribution with a pdf
→
→
g(−
q ), where −
q = (q1 , .., qN ) is the vector of values of the N options.
Following the rational inattention approach to information frictions, we assume that information about the N options is available to the DM, but processing the information is costly. If
the DM could process information costlessly, he or she would select the best available option.
With costly information acquisition, the DM must choose how much and which information to
acquire and process. Formally, we follow Sims and quantify the amount of information processed using information theory. A random variable is associated with a level of entropy, which
5

measures the amount of information that is conveyed when the random variable is realized. In
our setting, the prior g has a level of entropy and after processing information the DM has a
posterior distribution over the values of the available options, call it g ∗ . On average, g ∗ has a
smaller level of entropy than g because some uncertainty has been resolved through information
processing. With the posterior distribution in mind, the DM makes his or her choice.
For a random variable X with density function f , the entropy is given by
Z
H[f (X)] = − f (x) log f (x)dx.
(1)
Now suppose the DM receives a signal, Y , about X. The DM’s knowledge of X is now given
by the conditional distribution f (X|Y ) and the entropy of this distribution is H[f (X|Y )]. The
amount of information processed is given by the reduction in entropy H[f (X)] − H[f (X|Y )] ≡
I(X; Y ). The quantity I(X; Y ) is referred to as the mutual information between X and Y . If
Y is informative about X, I(X; Y ) will be positive. While particular signals may make the DM
less certain about X and therefore lead to a higher level of entropy, on average these signals
will lead to more precise knowledge of X and lower levels of entropy.4
While there is an intuitive appeal to thinking of the DM as asking for a signal about the
unknown values and then choosing an option conditional on that signal, the rational inattention
approach abstracts from the signals and models a joint probability distribution between the true
values and the DM’s action. For example, the DM might receive a signal y about the values
→
−
q and then implement a choice, i, as some function h(y). As h(·) is a deterministic function
→
→
of y, the joint distribution between y and −
q then generates a joint distribution between −
q
and the choice, i. The explicit treatment of signals, however, is not necessary and the rational
→
inattention approach abstracts from signals and works with the joint distribution between −
q
→
−
→
−
0
N
and i. We can describe this joint distribution by a collection {Pi , f ( q |i)}i=1 , where f ( q |i) is
the distribution of the true values conditional on option i being selected and Pi0 is the marginal
probability of selecting option i. Another way of looking at these probabilities is that Pi0 is
→
the DM’s subjective probability of selecting i before processing information and f (−
q |i) is the
→
DM’s posterior on −
q conditional on selecting option i. In total, this collection describes the
→
joint distribution of the agent’s choice and the vector −
q.
Our DM faces a cost of processing information that is quantified in terms of the reduction
in entropy. The decision making process can be thought of as a series of question that the DM
asks. The number and types of questions that the DM asks and the accuracy with which the
DM determines the answers to the questions generates a posterior distribution and a resulting
entropy reduction. This formulation of the information processing cost is meant to capture the
fact that it takes time and effort to carefully study the available options. The DM maximizes the
→
expected value of the option that he or she selects less the quantity λI(−
q ; i), where λ is a scalar
→
−
that controls the degree of the information friction. I( q ; i) is the mutual information between
the true values and the selected option. If the DM carefully studies the options before making
a choice, then observing which option the DM selects, i, provides relatively more information
about what the options are than it would if the DM acquired less information before choosing.
→
As such, when the DM processes more information, the mutual information between i and −
q
rises.
One might ask how the cost of information should be interpreted. Sims (2010) argues that
a person has a finite amount of attention—or capacity for processing information—to devote to
a number of things. As such, the parameter λ reflects the shadow cost of allocating attention
to the decision that we are considering.
4

See Cover and Thomas (2006) for further discussion of these concepts.

6

We can now state the DM’s optimization problem .
Z
X
→
→
0
max
P
qi f ( −
q |i)d−
q − λκ,
i
−
→
{Pi0 ,f ( q |i)}N
i=1 ,κ

−
→
q

i

(2)

subject to

X

→
I(−
q ; i) ≤ κ
→
→
0 −
Pi f ( q |i) = g(−
q)

(3)
→
∀−
q

(4)

i

X

Pi0 = 1, Pi0 ∈ [0, 1] .

i

Equation (3) limits how much the agent can find out about the options by processing the selected
amount of information, κ. Equation (4) states that posterior knowledge has to be consistent
with the DM’s prior. If this constraint were omitted, the DM could raise his or her expected
utility by selecting a probability distribution that places a large weight on high values even if
the agent knows (according to the prior) that this is not the case. Readers who are familiar with
rational inattention will recognize this problem as a standard information-constrained, static
optimization problem very similar to the generic example presented by Sims (2010, p. 162).
The only difference is that here the DM is choosing over a discrete set of actions.
An alternative modeling assumption would be to assume that the DM has a fixed capacity
for information processing to devote to the decision. In that case, κ would not be a choice
variable but an exogenous parameter and λ would be the Lagrange multiplier associated with
the constraint (3).

3

Solving the model

Let us study the case of λ > 0, solutions for λ = 0 are trivial since the perfectly attentive DM
simply selects the option(s) of the highest value with the probability one. We show in Appendix
→
A that the first order condition for the DM’s choice of f (−
q |i) is
qi
→
→
f (−
q |i) = h(−
q )e λ

∀i;

Pi0 > 0

(5)

where h is a function of Lagrange multipliers on the prior, (4). Plugging (5) into (4) we get
→
g(−
q)
→
h(−
q ) = PN
q .
0 λi
i=1 Pi e

(6)

The first order condition (5) thus takes the following form.
qi
→
g(−
q )e λ
→
−
f ( q |i) = PN
q .
0 e λi
P
i=1 i

7

(7)

Since f is a pdf, it satisfies
Z
1=
Z
1=

→
→
f (−
q |i)d−
q,
qi
→
g(−
q )e λ
→
−
qj d q ,
PN
0
λ
j=1 Pj e

(8)

for all Pi0 > 0. As we demonstrate below, this normalization condition can be useful in characterizing the solution when the prior is asymmetric.
Given a set of values, the probability of selecting i is the following conditional probability
→
P 0 f (−
q |i)
→
.
P(i|−
q)= i −
→
g( q )

(9)

→
→
From now on, we denote P(i|−
q ) as Pi (−
q ). Plugging (7) into (9) we get
P 0 eqi /λ
→
Pi (−
q ) = PN i
,
0 qj /λ
j=1 Pj e

(10)

We can now state the first result.
Theorem 1. Let a rationally inattentive agent be presented with N options and maximize the
expected utility, which is the expected value of the selected option minus the cost of processing
→
information, g(−
q ) be a pdf describing his prior knowledge of the options’ values and λ > 0 be
the unit cost of information. Then, the probability of choosing option i as a function of the
realized values of the options is given by (10). If λ = 0, then the perfectly attentive DM simply
selects the option(s) with the highest value.
What is left to fully solve the agent’s problem is to find the unconditional probabilities of
selecting each option, {Pi0 }N
i=1 . These probabilities are independent of a specific realization of
→
values −
q , they are the marginal probabilities of selecting each option before the agent starts
processing any information and they depend only on g(·) and λ.
If we omit the Pi0 terms from equation (10) we have the usual multinomial logit formula.
The implication is that the relative probability of selecting i is not driven just by eqi /λ , as in
the logit case, but also by the prior probability of selection option i, Pi0 .
The prior probability on option i depends on the value of qi relative to the values of other
options. For example, if option i is likely to have a high value, but sure to be dominated
by another option, then Pi0 will be zero. Conversely, an option might have an extremely low
expected value but with some probability have the highest value in the choice set and therefore
have a positive prior probability.
The dependence of the model on the cost of information, λ, is very intuitive. As information
processing becomes more costly the DM processes less and the selection probabilities depend less
on the actual realization of values and more on the prior Pi0 . Simply put, the less information
is processed the more prior knowledge enters in the DM’s decision. On the other hand, as λ
falls, the DM processes more information and in the extreme, as λ → 0, the DM selects the
option with the highest value with probability one, which is to say that all uncertainty about
which option is best is resolved.
A fairly obvious, but important, point is that λ converts bits of information to utils. Therefore, if one scales the utility function by a constant c, one must also scale λ by the same factor
for consistency. Of course, if the the utility levels are scaled up because the stakes are higher

8

(at a fixed λ) the selection probabilities change in a manner equivalent to a reduction in the
information friction (scaling λ down by 1/c). The reason is that the DM chooses to process
more information when more is at stake and thus makes less error in selecting the best option.
Finally, we offer an alternative way of interpreting equation (10), which we can rewrite as
e(qi +vi )/λ
→
,
Pi (−
q ) = PN
(qj +vj )/λ
e
j=1

where vi = λ log Pi0 . Written this way, the selection probabilities can be interpreted as a
multinomial logit in which the value of option i is shifted by the term vi . vi reflects the a priori
attractiveness of option i as measured by the prior probability that the option is selected. As
the cost of information, λ, rises, the weight on the prior rises. Notice that the choice behavior
generated by the multinomial logit does not depend on the location of utilities, but only the
differences between utilities. Therefore, the relevant feature of the vi terms is not their level,
but how they differ across options.

3.1

Independence of irrelevant alternatives

Unlike the multinomial logit, the rationally inattentive agent’s choice probabilities do not generally have the IIA property. IIA states that the ratio of the selection probabilities for two
alternatives is independent of what other alternatives are included in the choice set. According
to equation (10), the ratio of the selection probabilities of alternatives i and j is
→
Pi (−
q)
Pi0 eqi /λ
=
.
→
Pj (−
q)
Pj0 eqj /λ
The reason that IIA does not hold here is that the prior selection probabilities, Pi0 and Pj0 can
change in complex ways as new choices are added to the set of available alternatives. Section
5.2 provides an example of the failure IIA.
The multinomial logit’s IIA property is closely related to its predictions for the way the DM
will substitute across options as their values change. Suppose the value of option k increases.
The DM will be more likely to select this options and less likely to select other options. The
logit predicts that the probability of selecting all other options, i 6= k, will be reduced by the
same proportion. This proportionate shifting is an implication of IIA in that this is the only way
that the ratio of selection probabilities can remain the same as the value option k changes. In
the rational inattention model, there is a crucial distinction between changes in the value of an
option that are known a priori and those that are not. Using equation (10), the proportionate
change in the probability of selecting option i can be written
PN
0 q /λ
→
Pi (−
q)
P̂i0 eq̂i /λ j=1 Pj e j
=
,
P
→
0 q̂j /λ
Pi (−
q)
Pi0 eqi /λ N
j=1 P̂j e
where a hat on a variable indicates the value after the value of option k has changed and
variables without hats refer to the choice probabilities before the change. We assume that the
value of option i has not changed, qi = q̂i , so the second fraction drops out of the expression. In
the multinomial logit case, the Pi0 are not present and it follows that this expression is the same
for any i 6= k. Notice, that if the prior information is fixed and therefore the prior selection
probabilities are the same before and after the change, P̂i0 = Pi0 , then we arrive at the same
conclusion. If, however, the DM is (even partially) aware of the change a priori, then the prior
selection probabilities may change. In this case, the model can generate richer substitution
9

patterns as the ratio P̂i0 /Pi0 can vary across options.

3.2

Existence and uniqueness of the solution

In the optimization problem stated above, the objective function is continuous and the constraint
set is compact so a solution exists by the extreme value theorem.5 Whether or not the solution
is unique, depends on whether the options are sufficiently different. Consider a case where two
options have values that are perfectly equal in all states of the world. Call these options, option
1 and option 2. The DM is indifferent between the two options as he or she knows that selecting
one is always equivalent to selecting the other. Therefore the objective function does not change
as the DM increases P10 and reduces P20 as long as the sum of these probabilities is held fixed.
In this case, the solution would not be unique unless P10 = P20 = 0. When we rule out cases such
as this, the solution is indeed unique. The following assumptions are each sufficient conditions
for a unique solution to exist.
Assumption 1. The options are exchangeable in the prior in that, for any permutation, π, of
the indices, the random vectors {q1 , q2 , · · · , qN } and {qπ1 , qπ2 , · · · , qπN } are equal in distribution
with respect to the prior and for any i and j in {1, · · · , N }, qi and qj are not almost surely
equal.
Assumption 2. N = 2 and the values of the two options are not almost surely equal.
Assumption 3. For all but at most one k ∈ {1..N }, there exist two sets S1 ⊂ RN , S2 ⊂ RN
→
→
with positive probability measures with respect to the prior, g(−
q ), such that for all −
q 1 ∈ S1
→
→
→
there exists −
q 2 ∈ S2 where −
q 1 and −
q 2 differ in k th entry only.
In assumption 1, the condition that the options are exchangeable in the prior is a formalization of the notion that they are viewed symmetrically ex ante. The second part of the
assumption is that there is some positive probability that the options have different values.
When N = 2, as in assumption 2, we do not need to assume symmetry. For N > 2 and ex
ante asymmetric options, we have assumption 3. In words, this assumption says that there is
independent variation in the value of all options except possibly one. Assumption 3 is satisfied if
the values of the options are independently distributed and no more than one of their marginals
is degenerate to a single point although the assumption is quite a bit weaker than independence
as it just requires that there is not some form of perfect co-movement between the values. With
these assumptions in hand, we can now state the result.
Theorem 2. If any of assumptions 1, 2, or 3 holds, then the solution to the DM’s optimization
problem is unique.
Proof. See corollaries 8, 9, and 10 in Appendix B.

4

Ex ante symmetric options: the multinomial logit

In this section, we assume that all the options seem identical to the buyer a priori so the values
are exchangeable in the prior g. That is, the DM finds differences between the options only
after he or she starts processing information. We also assume that there are some states of the
world in which the options take different values. If this is not the case, the DM does not face a
meaningful choice. These assumptions are stated as assumption 1 in the previous section.
5

See Lemma 6 in Appendix B for details.

10

Under these assumption, the DM forms a strategy such that Pi0 = 1/N for all i. If there
were a solution with non-uniform Pi0 , then any permutation of the set would necessarily be a
solution too6 . However, Theorem 2 tells us that there is a unique solution. Using Pi0 = 1/N in
equation (10), we arrive at the following result.
→
Theorem 3. Let a rationally inattentive agent be presented with N options with g(−
q ) symmetric with respect to permutations of its arguments. The options are ex ante identical. Then,
the probability of choosing an option i as a function of realized values of all of options, is given
by
eqi /λ
→
Pi (−
q ) = PN
,
qj /λ
j=1 e
which is the multinomial logit formula.
→
It is worth mentioning that Pi (−
q ) does not depend on the prior g. Moreover the DM
always chooses to process some information, which is not necessarily the case when the prior is
asymmetric. Here the marginal expected value of additional information is initially infinite and
then decreasing with more information processed so the DM chooses to process some positive
amount of information as long as λ is finite.

5

Asymmetric options

In the previous section, we provided an analytic solution for the case where the prior is symmetric
with the result that the selection probabilities are given by the multinomial logit. For an
asymmetric prior, the selection probabilities are given by equation (10), which depends on the
prior probabilities {Pi0 }N
i=1 , which in turn depend on the specifics of the prior. We now explore
how these prior probabilities are formed.
If the cost of information is sufficiently high, the DM may not process any information, in
which case he or she simply selects the option with the highest expected value according to
the prior. Notice that these expected values only depend on the marginal distributions of the
values. When the DM does process information, choices depend on the full joint distribution of
the values.
If an option has higher expectation than another one, then it is often more likely to be
selected even when both options take the same values. The option with a higher expected
value is simply a safer bet and the rational inattentive agent is aware of his limits to processing
information. However, it does not always need to be the case. Imagine a situation where the
DM chooses from 101 different options. Option 1 takes value 0.99 with certainty, while all the
other options take the value 0 with the probability 99% and the value 1 otherwise. If the DM
processed little information, then he or she would most certainly choose option 1. The DM would
often choose the first option even if after processing quite a bit of information simply because
all other options’ realized values would equal zero, or because of uncertainty about whether a
certain option’s realized value equals 1 and thus going for q = 0.99 with certainty would be a
good choice. If the values of options 2 through 101 are independent of one another, option 1
will be selected with some positive probability. However, the situation changes drastically if the
values of options 2 to 101 co-move in such a way that exactly one of them takes the value 1,
while all others 0. In this case, the DM knows there is one better option than option 1. If the
information is costly, the DM will always choose option 1. If it is very cheap, the DM will never
choose option 1, although its expected value is 0.99 compared to 0.01 for the other options.
6

Appendix B

11

We now provide several examples of how a rationally inattentive agent would behave for
different specifications of his or her prior knowledge of the options. In doing so, there are two
main points that we would like to convey. First, these examples demonstrate how one can solve
for the prior selection probabilities Pi0 when the options are asymmetric. It is important to
find these probabilities because they are needed to compute the conditional selection probabil→
ities Pi (−
q ) as shown in equation (10). Second, we demonstrate how the IIA property of the
multinomial logit fails when the options are asymmetric.

5.1

Simple asymmetric case

In this subsection we consider a simple example in which the prior is asymmetric. In this
example there are two options, one of which has a known value while the other takes one of two
values. One interpretation is that the known option is an outside option or reservation value.
Problem 1. The DM chooses i ∈ {1, 2}. The value of option 1 is distributed as q1 = 0 with the
probability g0 and q1 = 1 with the probability 1 − g0 . Option 2 carries the value q2 = R ∈ (0, 1)
with certainty. The cost of information is λ.
To solve the problem, we must find {Pi0 }2i=1 . To do so we use the normalization conditions
→
on the distribution of −
q conditional on each choice i ∈ {1, 2}, equation (8), which take the
following form
1 =

1

g0
R

P10 + P20 e λ

+

R

1 =

(1 − g0 )e λ
1

(11)

R

P10 e λ + P20 e λ
R

g0 e λ

R

P10 + P20 e λ

+

(1 − g0 )e λ
1

R

P10 e λ + P20 e λ

.

(12)

These are two equations in the unknowns {Pi0 }2i=1 although if Pi0 = 0 then the equation for
the corresponding choice of i need not hold. Solutions
to the system of equations generated by
P
the normalization conditions will always satisfy i Pi0 = 1.7 There are three solutions to this
system,
 1


R
R
1

e λ −e λ + e λ − g0 + g0 e λ 


P10 ∈
0, 1, −  1
(13)
R
R


−1 + e λ
eλ − e λ
P20 = 1 − P10 .
The first solution to the system, P10 = 0, corresponds to the case when the DM chooses option 2
without processing any information. The utility is then R with certainty. The second solution,
P10 = 1, results in the a priori selection of option 1, expected utility equals (1 − g0 ). The third
solution describes the case when the DM chooses to process a positive amount of information.
Problem 1 satisfies assumption 2 as there are just two options and they never take the same
values. Therefore, theorem 2 establishes that the solution to the DM’s optimization problem
7

It follows from equation (8) that
N
X
i=1

Pi0 =

N
X
i=1

Pi0

Z

qi

→
g(−
q )e λ
−
→
qj d q .
PN
0 λ
P
e
j=1 j

Then exchanging the order of summation and integration and noting that the prior integrates to one yields the
result.

12

probability
1.0

0.8

0.6

0.4

0.2

0.2

0.4

0.6

0.8

1.0

R

Figure 1: P10 as a function of R and λ = 0.1, g0 = 0.5.
must be unique. In fact, there is an alternative way to see that the solution must unique.
Following Appendix B, any convex linear combination of two solutions needs to be a solution
too. Since P10 satisfies the normalization condition at three different values only, never on an
entire interval, the solution to the DM’s problem has to be unique.
Given that there must be a unique solution, not all three solutions to the system of equations
(11) and (12) can be solutions to the DM’s optimization problem. Since the expected utility is a
continuous function of P10 , R, λ and g0 , then the optimal P10 must be a continuous function of the
parameters. Otherwise, there would be at least two solutions at the point of discontinuity of P10 .
We also know that, when no information is processed, option 1 generates higher expected utility
than option 2 for (1 − g0 ) > R, and vice versa so for some configurations of parameters P10 = 0
is the solution and for some configurations of parameters P10 = 1 is the solution. Therefore, the
solution to the DM’s problem has to include the non-constant branch, the third solution. To
summarize this, the only possible solution to the DM’s optimization problem is
 1
 


R
R
1
e λ −e λ + e λ − g0 + g0 e λ

  .
P10 = max 0, min 1, −  1
(14)
R
R
λ
λ
λ
−1 + e
e −e
For a given set of parameters, P10 as a function of R is shown in Figure 1. For R close to 0 or
to 1, the DM decides to process no information and selects one of the options with certainty.
In the middle range however, the DM does process information and the selection of option 1 is
less and less probable as R increases, since option 2 is more and more appealing.
In general, one would expect that as R increases, the DM would be more willing to reject
option 1 and receive the certain value R. Indeed, differentiating the non-constant part of
(14) with respect to R we find ∂P10 /∂R < 0, the function is non-increasing.8 Similarly, one
would expect the unconditional probability of selecting option 1 to fall as g0 rises, as it is more
likely to have a low value. Again, the intuition can be confirmed from differentiating the nonconstant part of (14) with respect to g0 . The dependence of the model on the cost of processing
information, λ, is more difficult to characterize analytically. Figure 2 plots P10 for three values
of the prior, g0 . When processing information is cheap—low values of λ—P10 is just equal to
1 − g0 because the DM will always learn the value of option 1 and choose it when it has a high
value, which occurs with probability 1 − g0 . As λ increases, P10 fans out away from 0.5 because
the DM no longer learns as much about the value of option 1 and eventually just selects the
option with the highest value according to the prior. For g0 = 1/2 and R = 1/2, P10 simplifies
8

Verifying this inequality requires a few steps and details are available upon request.

13

Probability

æ
æ æ
æ æ
æ
0.8
æ æ
æ æ æ æ æ æ

æ

g0 =0.25

à

g0 =0.5

ì

g0 =0.75

0.6
à à à à à à à à à à à à à à

0.4
0.2

ì ì ì ì ì ì ì

ì ì ì

ì ì

0.0
0.0

0.1

0.2

0.3

ì ì
0.4

Λ

Figure 2: P10 as a function of λ evaluated at various values of of g0 and R = 0.5.
to 1/2. In this case the DM is a priori indifferent between the two options and even for high
values of λ, the DM will process at least a small amount of information in order to break the
tie.9

5.2

Duplicate options

The previous subsection studied a case where the options differ in the marginal distributions
of their values. Options may also differ in other features of the joint distribution of their
values. For example, the values of two options may be more highly correlated with each other
than they are with a third option. In the extreme, two options might be exact duplicates. The
multinomial logit has well known difficulties when some options are similar or duplicates. These
difficulties were illustrated in the introduction with Debreu’s bus paradox. Debreu’s logic was
that duplicating an option does not fundamentally change the choice facing the DM and so
should not have a substantial impact on the choice probabilities. In this section, we begin by
showing that the rationally inattentive DM treats duplicate options as a single option. We then
extend this idea in section 5.3 to consider a case where two options are similar, but not exact
duplicates.
We use a version of the bus problem to analyze how the rationally inattentive agent treats
duplicate options. In our framework there are two sets of selection probabilities: the probabilities of selecting each option conditional on the true values of the options and the prior
probabilities of selecting each option that would describe the DM’s anticipated actions before
he or she begins processing information. The notion that the values of the available options are
uncertain and believed to be distributed according to a prior distribution is a particular feature
of our framework so it is reasonable to think that the conditional probabilities are closer to what
Debreu and the subsequent literature have in mind. Nevertheless, the rationally inattentive DM
treats duplicate options as a single option both in terms of prior probabilities and in terms of
conditional probabilities.
To show that the DM treats duplicate options as a single option we state two choice problems. In the first, the DM chooses from the set {yellow bus, train} and in the second the DM
chooses from {yellow bus, red bus, train}. When the buses are exact duplicates—a notion that
we formalize below in assumption 4—the probability of choosing a bus (of any color) is the
same in both of these choice problems. We now state the two choice problems formally.
9

To see that some information
is always processed, notice that the conditional probability of selection option

1 is eq1 /λ / eq1 /λ + e1/(2λ) , which is never equal to the unconditional probability P10 = 1/2 for q1 ∈ {0, 1} and
a finite λ.

14

Problem 2. The DM chooses from the set {yellow bus, train}. The prior distribution for the
values of the two options is g 1 (qy , qt ), where qy is the value of the yellow bus and qt is the value
of the train. qy and qt are not a.s. equal. The cost of information is λ1 .
Problem 3. The DM chooses from the set {yellow bus, red bus, train}. The prior distribution
for the values of the options is g 2 (qy , qr , qt ), where qr is the value of the red bus. The cost of
information is λ2 .
We now introduce our assumptions. The first assumption formalizes the notion that the
buses are duplicates. We assume that the two buses are duplicates in that the prior places no
weight on their values being different. The meaning of this assumption is that the DM knows
the two buses are identical before processing any information although does not know what
their (joint) value is. It is also natural to assume that the joint distribution of a bus and the
train is the same as in the one-bus case.
Assumption 4. The prior for the two-bus case satisfies
(
g 1 (qy , qt ) if qy = qr ,
g 2 (qy , qr , qt ) =
0
if qy 6= qr .

Our second assumption is simply that the cost of a bit of information is the same in the two
problems.
Assumption 5. λ1 = λ2 .
Before we state the proposition, we must introduce some notation to describe the solutions
to these problems. Let Pb0 be the prior probability of selecting the (yellow) bus in problem 2
→
→
and Pb (−
q ) be the probability of selecting the bus conditional on a realization of −
q in problem
2. For problem 3 we use analogous notation with the subscript y to denote probabilities of
selecting the yellow bus and subscript r to denote probabilities of selecting the red bus.
Our first proposition is that the prior probability of selecting a bus is the same in both
problems.
Proposition 4. If assumptions 4 and 5 hold, then Pb0 = Py0 + Pr0 .
Proof. See Appendix C.
A corollary to this proposition is that the probability of selecting a bus conditional on
realized values of the options is the same in both problems. As the two buses are duplicates it
→
is natural to restrict attention to realizations of the vector −
q for which qy = qr .
→
Corollary 5. If assumptions 4 and 5 hold, then for any −
q = (qy , qr , qt ) that satisfies qy = qr
→
−
→
−
→
−
we have Pb ( q ) = Py ( q ) + Pr ( q ).
Proof. See Appendix C.

5.3

Correlated values

The previous subsection considered the case where two options are known to be exactly identical.
In this subsection we explore the behavior of the rationally inattentive agent as the co-movement
of two options varies. We do so in the context of a choice among three options for which we
can make some progress analytically.
15

bus probability
0.50
0.45
0.40

Λ=0

0.35
Λ=0.4
0.30
g1
0.1

0.2

0.3

0.4

0.5

Figure 3: Py0 for various values of λ and g1 and R = 1/2.
Problem 4. The DM chooses from the set {yellow bus, red bus, train}. The DM knows the
quality of the train exactly, qt = R ∈ (0, 1). The buses each take one of two values, either 0 or
1, with expected values 1/2 for each. The joint distribution of the values of all three options is
g(0, 0, R) = 1/2 − g1
g(1, 0, R) = g1
g(0, 1, R) = g1
g(1, 1, R) = 1/2 − g1 .

(15)

The DM can process information about the values of the busses at a cost λ.
We are going to illustrate how the choice probabilities vary with the correlation of the values
of the two buses. Given the joint distribution above, the correlation between qy and qr is 1−4g1 .
Notice that when g1 is greater than zero, the conditions of assumption 3 are satisfied as it
is possible to vary each bus value while holding the values of the other options constant. When
g1 equals zero, this problem resolves to the duplicates case and assumption 3.

As before, to find the solution to the DM’s optimization problem we must solve for Py0 , Pr0 , Pt0 .
The normalization condition on choosing the first option is
1/2 − g1
g1 e1/λ
+
Py0 + Pr0 + (1 − Py0 − Pr0 )eR/λ Py0 e1/λ + Pr0 + (1 − Py0 − Pr0 )eR/λ

1=
+

g1
(1/2 − g1 )e1/λ
+
(16)
P20 e1/λ + Py0 + (1 − Py0 − Pr0 )eR/λ Py0 e1/λ + Pr0 e1/λ + (1 − Py0 − Pr0 )eR/λ

Due to the symmetry between the buses, we know Py0 = Pr0 . This problem can be solved
analytically using the same technique as in the previous sections, the resulting expression is
however too complicated to include here.10 Instead, we illustrate the behavior of the model
for R = 1/2 and various values of g1 and λ in Figure 3. As g1 increases, and the correlation
between the values of the buses decreases, the unconditional probability of choosing either bus
increases. If they are perfectly correlated, then their collective probability decreases to 0.5, they
are effectively treated as one option. To see that they are treated as a single option, recall from
Section 5.1 that when values of zero and one were equally likely (g0 = 1/2) and the reservation
value was equal to 1/2, we found Py0 = 1/2 for all λ. That case corresponds to the situation
here with just a single bus in the choice set. So with two buses in the choice set we find that
the sum of their selection probabilities is equal to 1/2 as section 5.2 tells us we should.
In the perfect information case, the probability of choosing the yellow bus, Py0 , equals
10

They can be provided upon request.

16

1/4 + g1 /2, if we assume that ties are broken at random. As the correlation between the values
of the buses decreases, the probability that option 3 has the highest value decreases, and thus
Py0 increases. This effect persists when λ > 0. The more similar the two buses are, the lower is
the probability of either of them being selected. This is the extension of the duplicates results.
For λ > 0, however, Py0 is larger than it is in the perfect information case. If the DM does
not possess perfect information, then he or she considers that a priori it is more likely that
either of the buses, rather than the train, possesses the highest value among the three options.
With g1 > 0 and increasingly costly information, the DM would shift his or her attention to
which one of the two buses to select rather than whether to select the train, since the buses
values are more likely to be the highest.

6

Concluding remarks

In this paper, we have studied the optimal behavior of a rationally inattentive agent who faces
a discrete choice problem and shown that this model gives rise to the multinomial logit model
when the options are a priori symmetric. This finding opens the door for future research to
combine the rational inattention framework with our existing knowledge of the implications of
the multinomial logit.
We have also analyzed the way in which prior knowledge of the available options affects
choice behavior when information costs result in the DM choosing with incomplete information.
The incorporation of this prior knowledge can lead to more intuitive predictions than those
that arise out of the standard multinomial logit. For example, the rationally inattentive agent
treat’s duplicate options as a single option while the multinomial logit’s IIA property implies
that they are treated as distinct options.

17

A

Derivation of the first order condition

Here we derive the first order condition, equation (5). Using equation 2.35 in Cover and Thomas,
we can write the mutual information as
Z
→
X
P 0 f (−
q |i) −
→
→
−
0
f (−
q |i) log i 0 −
I( q ; i) =
Pi
d→
q
−
→
P g(→
q)
i

q

i

replacing the prior with equation (4) and canceling two Pi0 terms
Z
→
X
f (−
q |i)
→
→
→
I(−
q ; i) =
Pi0
f (−
q |i) log P 0 −
d−
q.
→
−
→
P
f
(
q
|j)
q
j
j
i

(17)

The Lagrangian is then
Z
X
→
→
0
L=
Pi
qi f (−
q |i)d−
q − λκ
−
→
q

i

"
−χ

X
i

Pi0

# Z
"
#
→
X
f (−
q |i)
→
−
→
−
→
→
−
→
→
−
0 −
f ( q |i) log P 0 −
dq −κ −
µ( q )
Pi f ( q |i) − g( q ) d−
q,
→
−
→
−
→
P
f
(
q
|j)
q
q
j j
i

Z

where χ ∈ R and µ ∈ L∞ (RN ) are Lagrange multipliers. The first order condition with respect
→
to κ is simply λ = χ. The first order condition with respect to f (−
q |i) is
P 0 −
→
→
1
f (−
q |i)
j Pj f ( q |j)
→
0 −
0
0
P 0 −
− χPi f ( q |i)
Pi qi − χPi log P 0 −
→
−
→
→
f ( q |i)
j Pj f ( q |j)
j Pj f ( q |j)
P 0 −
→
→
X
f (−
q |k)Pi0
j Pj f ( q |j)
→ 0
−
→
0 −
+χ
Pk f ( q |k)
hP
i2 − µ( q )Pi = 0.
→
−
f ( q |k)
→
0 −
k
j Pj f ( q |j)
We can now cancel a number of terms and replace
Pi0



→
→
−
0 −
j Pj f ( q |j) with g( q ) to arrive at

P

→
f (−
q |i)
→
− µ(−
q)
qi − χ log
→
g(−
q)


= 0.

→
If Pi0 > 0 and λ > 0, solving for f (−
q |i) we obtain
 


→
qi
µ(−
q)
→
−
→
f ( q |i) = exp
exp −
g(−
q)
χ
χ

−
→ 
→
→
using λ = χ and defining h(−
q ) ≡ exp − µ(λq ) g(−
q ) produces equation (5).

B

Existence and Uniqueness of Solutions to the DM’s Problem

Lemma 6. The DM’s optimization (2)-(4) problem always has a solution.
Proof: Since (10) is a necessary condition for the maximum, then the collection {Pi0 }N
i=1
determines the whole solution. However, the objective is a continuous function of {Pi0 }N
,
since
i=1
→
0 N
f (−
qP|i) is also a continuous function of {Pi0 }N
i=1 . Moreover, the admissible set for {Pi }i=1 given
by i Pi0 = 1 and Pk0 ≥ 0 ∀k, is compact. Therefore, the maximum always exists.

18

→
→
0 ˆ−
N
Lemma 7. If S = {Pi0 , f (−
q |i)}N
i=1 and Ŝ = {P̂i , f ( q |i)}i=1 are two distinct solutions to the
DM’s optimization problem, then
X
(Pi0 − P̂i0 )eqi /λ = 0
a.s.
(18)
i

Proof: Mutual information is a convex function of the joint distribution of the two variables.
The objective (2) is thus a concave functional: the first term is linear and the second is concave.
→
Moreover, the admissible set of {Pi0 , f (−
q |i)}N
i=1 , satisfying the constraints is convex: (3) is a
concave constraint and all other are linear. Therefore, any convex linear combination S̃(ξ) of
the solutions S and Ŝ


ξ ∈ [0, 1], ∀i.
(19)
P̃i0 (ξ) = Pi0 + ξ P̂i0 − Pi0
is also a solution. This solution thus needs to satisfy (8) for all ξ ∈ [0, 1]. The right hand side
of (8) has to be a constant as a function of ξ. However, its second derivative with respect to ξ
at ξ = 0, which has to equal zero, is
P
qj 2
qi
N
→
0 − P 0 )e λ
Z g(−
(
P̂
q )e λ
j
j
j=1
→
d−
q.
P
qj 3
N
0
λ
P̃
e
j=1 j

(20)

Therefore, for the two solutions to exist, (18) has to hold.
Corollary 8. If assumption 1 holds then the solution to the DM’s optimization problem is
unique.
Proof: Let the solution be non-unique. (18) thus needs to hold. According to the corollary’s
→
assumption, there exists S1 ⊂ RN with a positive measure w.r.t. g, such that all −
q in S1 are
non-constant vectors. Since the solution is non-unique, (18) holds almost surely and S1 has a
→
→
→
positive mass, then there surely exist −
q and −
q 0 generated from −
q only by switching entries i
→
and j, where that qi 6= qj , satisfying (18) point-wise. By subtracting the equations for −
q and
→
−
0
q we get
 qi
qj 
(∆i − ∆j ) e λ − e λ = 0,
(21)
where ∆i denotes (Pi0 − P̂i0 ). We get ∆i = ∆j . However, since we can reshuffle
P the entries
arbitrarily, ∆i equals a constant ∆ for all i in {1..N }. Moreover, ∆ = 0 since i ∆i = 0. The
solution must be unique.
.
Corollary 9. If assumption 2 holds then the solution to the DM’s optimization problem is
unique.
Proof: for N = 2, (P10 − P̂10 ) = −(P20 − P̂20 ) (18) takes the form:
q1

q2

(P10 − P̂10 )(e λ − e λ ) = 0

a.s.

(22)

If q1 and q2 are not equal almost surely, then P10 = P̂10 .
The following corollary of Lemma 7 is more directly linked to the analytical structure of
(18), and its assumptions are perhaps less intuitive. Let (Pk0 − P̂k0 ) 6= 0. It is clear that if (18)
→
→
→
holds for −
q 1 than it can not hold for any −
q 2 that differs from −
q 1 in the k th entry only.
Corollary 10. If assumption 3 holds then the solution to the DM’s optimization problem is
unique.
19

Proof: The Corollary follows directly from Lemma 7 and the discussion right above it,
adjusted to satisfy the requirement of “almost sure” equality. What we need to explain is
why it does not matter for the uniqueness if there exists exactly one k that does not satisfy
the assumptions. If {Pi0 }i and {P̂i0 }i are two different solutions then there exist at least two
different k’s s.t. (Pk0 − P̂k0 ) 6= 0. Therefore, being able to vary only one of these two entries
suffices for the uniqueness.
Corollary 10 applies to setups in Sections 5.1 and 5.3. In these cases, one option takes value
R with certainty, its marginal is degenerate. That is why we explicitly allowed for one entry not
satisfying the assumptions. However, the corollary does not apply to the case of pure duplicates
in Section 5.2 and g1 = 0 in 5.3. In these cases, we can not vary values corresponding to both
of the duplicates independently of each other. But this is fine, the solution is not unique. If two
options are exactly equivalent in all realizations, then the DM chooses only the sum of their
probabilities.

C

Proofs for section 5.2

Proof of proposition 4. The normalization conditions for problem 2 can be written as11
Z Z
1=
Z Z
1=

eqy /λ
g 1 (qy , qt )dqy dqt
Pb0 eqy /λ + (1 − Pb0 )eqt /λ

(23)

eqt /λ
g 1 (qy , qt )dqy dqt
Pb0 eqy /λ + (1 − Pb0 )eqt /λ

(24)

Both of these equations must hold for Pb0 ∈ (0, 1). For Pb0 = 1 only equation (23) must hold and
for Pb0 = 0 only equation (24) must hold. This system of equations has two or three possible
solutions: Pb0 = {0, P ∗ , 1} where P ∗ is an interior solution that may or may not exist. To see
that there cannot be multiple interior solutions, subtract equation (24) from (23) and rearrange
to arrive at
Z Z
1 − e(qt −qy )/λ
0=
g 1 (qy , qt )dqy dqt .
(25)
Pb0 + (1 − Pb0 )e(qt −qy )/λ
Define the random variable z ≡ e(qt −qy )/λ so we can write equation (25) as


1−z
0=E
.
Pb0 + (1 − Pb0 )z

(26)

The right-hand side of this equation is decreasing in Pb0 , so there can be at most one solution.
To see this, differentiate w.r.t. Pb0
"
#


∂
1−z
(1 − z)2
E
= E −
2
∂Pb0
Pb0 + (1 − Pb0 )z
P 0 + (1 − P 0 )z
b

b

and on the right-hand side, the expectation is taken over a function that is negative for all z 6= 1
and zero for z = 1. Given that we have qy is no a.s. equal to qt , the expectation places some
weight of z 6= 1.
R → −
Note that previously we have written g(−
q )d→
q to indicate integration with respect to the prior, but in this
section we find it useful to distinguish between the dimensions over which we are integrating.
11

20

In problem 3, the normalization condition for the yellow bus is
Z Z Z
1=

eqy /λ
g 2 (qy , qr , qt )dqy dqr dqt .
Py0 eqy /λ + Pr0 eqr /λ + (1 − Py0 − Pr0 )eqt /λ

This normalization condition involves integrating over a three-dimensional space, but the assumption that the buses are exact duplicates means that the prior only places weight on a two
dimensional subspace. Therefore, we can think of integrating just over qy and using the fact
that qr = qy . Doing so yields
Z Z
1=
Z Z
=

eqy /λ
g 2 (qy , qy , qt )dqy dqt
Py0 eqy /λ + Pr0 eqy /λ + (1 − Py0 − Pr0 )eqt /λ

(27)

eqy /λ


g 1 (qy , qt )dqy dqt .
Py0 + Pr0 eqy /λ + 1 − Py0 + Pr0 eqt /λ

(28)



Now notice that the sum of Py0 and Pr0 enters equation (28) just as Pb0 enters equation (23)
and otherwise the two equations are the same. Using similar steps, we find that the three
normalization conditions for problem 3 reduce to the same equations as (23) and (24) with
Py0 + Pr0 replacing Pb0 . Therefore, any pair of Py0 and Pr0 that sum to a Pb0 that solves equations
(23) and (24) satisfies the normalization conditions for problem 3.
The final step of the proof is to establish that the particular solution to the normalization
conditions for problem 2 that yields the highest value to the DM is also the one that yields
the highest value to the DM in problem 3. Suppose the DM in problem 2 chooses Pb0 = 1 or
Pb0 = 0. Then there is no reason to process any information and the objective function value is
just the expected value of the bus or train, respectively. The exact same holds in problem 3 if
the DM selects Py0 + Pr0 = 0, Py0 = 1, Pr0 = 1, or Py0 + Pr0 = 1. For interior solutions in problem
3, the expected value of the selected option, which differs from the objective function by the
information cost, can be written

Z Z Z 0 qy /λ
Py e
qy + Pr0 eqr /λ qr + 1 − Py0 − Pr0 eqt /λ qt 2

g (qy , qr , qt )dqy dqr dqt .
Py0 eqy /λ + Pr0 eqr /λ + 1 − Py0 − Pr0 eqt /λ
Restricting attention to cases where qy = qr , we have


Z Z
Py0 + Pr0 eqy /λ qy + 1 − Py0 − Pr0 eqt /λ qt 1


g (qy , qt )dqy dqt ,
Py0 + Pr0 eqy /λ + 1 − Py0 − Pr0 eqt /λ
which is the same as the expected value of the selected option in problem 2 if Py0 + Pr0 = Pb0 .
What is left is to establish that the information flow is the same in both problems. Plug equation
(7) into equation (17) to find the mutual information between the DM’s choice and the vector
→
−
q
→
I(−
q ; i) =

X
i

Pi0

Z
−
→
q

eqi /λ
eqi /λ
→
→
log
g(−
q )d−
q.
P
0
0
q
/λ
q
/λ
j
j
j Pj e
j Pj e

P

Consider this equation for problem 3, using the same logic
P as above, we can restrict attention
to those cases where qy = qr . In that case, the term j∈{r,y,t} Pj0 eqj /λ only depends on the
sum of Py0 and Pr0 and takes the same value as in problem 2 if Py0 + Pr0 = Pb0 . And similarly
for the outer sum over the Pi0 . This establishes that the information flow is the same in the

21

two problems. As the expected value of the selected option and the information flow are the
same in the two problems, the objective function takes the same value across problems for each
of the two or three candidate solutions. So whichever yields the highest value in one problem
will yield the highest value in the other problem. This establishes that the DM treats the two
identical buses as a single option in terms of prior probabilities.
Proof of corollary 5. From equation (10) we have
Py0 eqy /λ + Pr0 eqr /λ

→
→
Py (−
q ) + Pr (−
q)=


Py0 eqy /λ + Pr0 eqr /λ + 1 − Py0 − Pr0 eqt /λ

Py0 + Pr0 eqy /λ



=
Py0 + Pr0 eqy /λ + 1 − Py0 + Pr0 eqt /λ

Pb0 eqy /λ


Pb0 eqy /λ + 1 − Pb0 eqt /λ
→
= P (−
q ),

=

b

where the second equality follows from qy = qr and the third follows from proposition 4.

22

References
Anderson, S. P., de Palma, A., and Thisse, J.-F. (1992). Discrete Choice Theory of Product
Differentiation. MIT Press, Cambridge, MA.
Ben-Akiva, M. (1973). Structure of Passenger Travel Demand Models. PhD thesis, MIT,
Cambridge, Mass. Department of Civil Engineering.
Cover, T. M. and Thomas, J. A. (2006). Elements of Information Theory. Wiley, Hoboken, NJ.
Daly, A. and Zachary, S. (1979). Improved multiple choice models. In Hensher, D. and Dalvi, Q.,
editors, Identifying and Measuring the Determinants of Mode Choice, pages 335–57. Teakfield,
London.
Debreu, G. (1960). Review of individual choice behavior by R. D. Luce. American Economic
Review, 50(1):186–188.
Gul, F., Natenzon, P., and Pesendorfer, W. (2010). Random choice as behaviorial optimization.
Princeton University Working Paper.
Luce, R. D. (1959). Individual Choice Behavior: a Theoretical Analysis. Wiley, New York.
Luce, R. D. and Suppes, P. (1965). Preference, utility, and subjective probability. In Luce,
R. D.; Bush, R. and Galanter, E., editors, Handbook of Mathematical Psychology, volume 3,
pages 249–410. Wiley.
Luo, Y. (2008). Consumption dynamics under information processing constraints. Review of
Economic Dynamics, 11(2):366 – 385.
Mackowiak, B. and Wiederholt, M. (2009). Optimal sticky prices under rational inattention.
The American Economic Review, 99:769–803(35).
Matejka, F. (2010a). Rationally inattentive seller: Sales and discrete pricing. CERGE-EI
Working Papers wp408.
Matejka, F. (2010b). Rigid pricing and rationally inattentive consumer. CERGE-EI Working
Papers wp409.
Mattsson, L.-G. and Weibull, J. W. (2002). Probabilistic choice and procedurally bounded
rationality. Games and Economic Behavior, 41(1):61 – 78.
McFadden, D. (1974). Conditional logit analysis of qualitative choice behavior. In Zarembka,
P., editor, Frontiers in Econometrics, pages 105–142. Academic Press, New York.
McFadden, D. (1976). Quantal choice analysis: A survey. Annals of Economic and Social
Measurement, 5(4):363 – 390.
McFadden, D. (1980). Econometric models for probabilistic choice among products. The Journal
of Business, 53(3):pp. S13–S29.
McKelvey, R. D. and Palfrey, T. R. (1995). Quantal response equilibria for normal form games.
Games and Economic Behavior, 10(1):6 – 38.
Mondria, J. (2010). Portfolio choice, attention allocation, and price comovement. Journal of
Economic Theory, 145(5):1837 – 1864.
23

Natenzon, P. (2010). Random choice and learning. Working paper, Princeton University.
Shannon, C. E. (1948). A mathematical theory of communication. The Bell System Technical
Journal, 27.
Sims, C. A. (1998). Stickiness. Carnegie-Rochester Conference Series on Public Policy, 49:317
– 356.
Sims, C. A. (2003). Implications of rational inattention. Journal of Monetary Economics,
50(3):665 – 690.
Sims, C. A. (2006). Rational inattention: Beyond the linear-quadratic case. The American
Economic Review, 96(2):pp. 158–163.
Sims, C. A. (2010). Rational inattention and monetary economics. In Friedman, B. M. and
Woodford, M., editors, Handbook of Monetary Economics, volume 3A, pages 155 – 181.
Elsevier.
Stahl, D. O. (1990). Entropy control costs and entropic equilibria. International Journal of
Game Theory, 19(2):129 – 138.
Train, K. (2009). Discrete Choice Methods with Simulation. Cambridge University Press,
Cambridge, U.K.
Tutino, A. (2009). The rigidity of choice: Lifetime savings under information-processing constraints. Working paper.
Van Nieuwerburgh, S. and Veldkamp, L. (2010).
Information acquisition and underdiversification. Review of Economic Studies, 77(2):779–805.
Weibull, J. W., Mattsson, L.-G., and Voorneveld, M. (2007). Better may be worse: Some
monotonicity results and paradoxes in discrete choice under uncertainty. Theory and Decision,
63:121–151.
Williams, H. C. W. L. (1977). On the formation of travel demand models and economic evaluation measures of user benefit. Environment and Planning A, 9(3):285–344.
Woodford, M. (2009). Information-constrained state-dependent pricing. Journal of Monetary
Economics, 56(Supplement 1):S100 – S124.
Yang, M. (2010). Coordination with rational inattention. Princeton University Working Paper.
Yellott, J. I. (1977). The relationship between luce’s choice axiom, thurstone’s theory of comparative judgment, and the double exponential distribution. Journal of Mathematical Psychology,
15(2):109 – 144.

24

Working Paper Series
ISSN 1211-3298
Registration No. (Ministry of Culture): E 19443
Individual researchers, as well as the on-line and printed versions of the CERGE-EI Working
Papers (including their dissemination) were supported from the European Structural Fund
(within the Operational Programme Prague Adaptability), the budget of the City of Prague, the
Czech Republic’s state budget and the following institutional grants:




Center of Advanced Political Economy Research [Centrum pro pokročilá politickoekonomická studia], No. LC542, (2005-2011);
Economic Aspects of EU and EMU Entry [Ekonomické aspekty vstupu do Evropské
unie a Evropské měnové unie], No. AVOZ70850503, (2005-2011);
Economic Impact of European Integration on the Czech Republic [Ekonomické dopady
evropské integrace na ČR], No. MSM0021620846, (2005-2011);

Specific research support and/or other grants the researchers/publications benefited from are
acknowledged at the beginning of the Paper.
(c) Filip Matějka and Alisdair McKay, 2011
All rights reserved. No part of this publication may be reproduced, stored in a retrieval system or
transmitted in any form or by any means, electronic, mechanical or photocopying, recording, or
otherwise without the prior permission of the publisher.
Published by
Charles University in Prague, Center for Economic Research and Graduate Education (CERGE)
and
Economics Institute ASCR, v. v. i. (EI)
CERGE-EI, Politických vězňů 7, 111 21 Prague 1, tel.: +420 224 005 153, Czech Republic.
Printed by CERGE-EI, Prague
Subscription: CERGE-EI homepage: http://www.cerge-ei.cz
Phone: + 420 224 005 153
Email: office@cerge-ei.cz
Web: http://www.cerge-ei.cz
Editor: Michal Kejak
Editorial board: Jan Kmenta, Randall Filer, Petr Zemčík
The paper is available online at http://www.cerge-ei.cz/publications/working_papers/.
ISBN 978-80-7343-244-7 (Univerzita Karlova. Centrum pro ekonomický výzkum
a doktorské studium)
ISBN 978-80-7344-236-1 (Národohospodářský ústav AV ČR, v. v. i.)

