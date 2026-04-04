---
source: Wibral, M., Priesemann, V., Kay, J.W., Lizier, J.T., Phillips, W.A. (2017). Partial information decomposition as a unified approach to the specification of neural goal functions. Brain and Cognition, 112, 25-38. arXiv:1510.00831
author: Michael Wibral et al.
date: 2015-10-04
type: paper
quality: primary
stance: neutral
---


Partial Information Decomposition as a Unified Approach to
the Specification of Neural Goal Functions

arXiv:1510.00831v1 [q-bio.NC] 3 Oct 2015

Michael Wibral1 , Viola Priesemann2 , Jim W. Kay3 , Joseph T. Lizier4 , William
A. Phillips5

Abstract
In many neural systems anatomical motifs are present repeatedly, but despite their structural similarity they can serve very different tasks. A prime example for such a motif is
the canonical microcircuit of six-layered neo-cortex, which is repeated across cortical areas, and is involved in a number of different tasks (e.g.sensory, cognitive, or motor tasks).
This observation has spawned interest in finding a common underlying principle, a ’goal
function’, of information processing implemented in this structure. By definition such
a goal function, if universal, cannot be cast in processing-domain specific language (e.g.
’edge filtering’, ’working memory’). Thus, to formulate such a principle, we have to use a
domain-independent framework. Information theory offers such a framework. However,
while the classical framework of information theory focuses on the relation between one
input and one output (Shannon’s mutual information), we argue that neural information
processing crucially depends on the combination of multiple inputs to create the output
of a processor. To account for this, we use a very recent extension of Shannon Information theory, called partial information decomposition (PID). PID allows to quantify the
information that several inputs provide individually (unique information), redundantly
(shared information) or only jointly (synergistic information) about the output. First,
we review the framework of PID. Then we apply it to reevaluate and analyze several
earlier proposals of information theoretic neural goal functions (predictive coding, infomax and coherent infomax, efficient coding). We find that PID allows to compare these
goal functions in a common framework, and also provides a versatile approach to design
new goal functions from first principles. Building on this, we design and analyze a novel
goal function, called ’coding with synergy’, which builds on combining external input and
prior knowledge in a synergistic manner. We suggest that this novel goal function may
be highly useful in neural information processing.
Keywords: Information theory, unique information, shared information, synergy,
redundancy, predictive coding, neural coding, coherent infomax, neural goal function

1 wibral@em.uni-frankfurt.de, MEG Unit, Brain Imaging Center, Goethe University, Heinrich Hoffmann Straße 10, 60528 Frankfurt am Main, Germany
2 Department of Non-linear Dynamics, Max Planck Institute for Dynamics and Self-Organization, &
Bernstein Center for Computational Neuroscience, Göttingen, Germany
3 Department of Statistics,University of Glasgow, Glasgow, G12 8QQ, UK
4 School of Civil Engineering, The University of Sydney, NSW, Australia
5 School of Natural Sciences, University of Stirling, Stirling, UK

Preprint submitted to Elsevier

October 6, 2015

1. Introduction
In many neural systems anatomical and physiological motifs are present repeatedly in
the service of a variety of different functions. A prime example is the canonical cortical
microcircuit that is found in many different regions of the six-layered mammalian neocortex. These different regions serve various sensory, cognitive, and motor functions, but
how can a common circuit be used for such a variety of different purposes? This issue
has spawned interest in finding a common abstract framework within which the relevant
information processing functions can be specified.
Several solutions for such an abstract framework have been proposed previously,
among them approaches that still use semantics to a certain extent (predictive coding
with its initial focus on sensory perception), teleological ones that prescribe a goal based
on statistical physics of the organism and its environment (free energy principle) and
information theoretic ones that focus on local operations on information (Coherent Infomax). While these are all encouraging developments, they also beg the question of how to
compare these approaches, and how many more possibilities of defining new approaches
of this kind exist. Ideally, an abstract framework that would comprise these approaches
as specific cases would be desirable. This article suggests a possible starting point for the
development of such a unifying framework.
By definition this framework cannot be cast in processing-domain specific language,
such as ‘edge-filtering’ or ‘face perception, or ‘visual working memory, for example, but
must avoid any use of semantics beyond describing the elementary operations that information processing is composed of 6 . A framework that has these properties is information
theory. In fact, information theory is often criticized exactly for its lack of semantics, i.e.
for ignoring the meaning of the information that is processed in a system. As we will
demonstrate here, this apparent shortcoming can be a strength when trying to provide a
unified description of the goals of neural information processing. Moreover, by identifying
separate component processes of information processing, information theory provides a
meta-semantics that serves to better understand what neural systems do at an abstract
level (for more details see [1]). Last, information theory is based on evaluating probabilities of events and thereby closely related to the concepts and hypotheses of probabilistic
inference that are at the heart of predictive coding theory [2, 3, 4, 5]. Thus information
theory is naturally linked to the domain-general semantics of this and related theories.
Based on the domain-generality of information theory several variants of information theoretic goal functions for neural networks have been proposed. The optimization
of these abstract goal functions on artificial neural networks leads to the emergence of
properties also found in biological neural systems – this can be considered an amazing
success of the information theoretic approach given that we still know very little about
general cortical algorithms. This success raises hopes for finding unifying principles in
the flood of phenomena discovered in experimental neuroscience. Examples of successful,
information-theoretically defined goal functions are Linsker’s infomax [6] – producing re6 To be truly generic, the framework should also avoid to resort too strongly to semantics in terms of
“survival of the organism” as even that maybe not desirable for each and every individual organism in
certain species. This is because “programmed death” will allow a more rapid turnover of generations and
thereby more rapid evolutionary adaptation.

2

ceptive fields and orientation columns similar to those observed in primary visual cortex
V1 [7], recurrent infomax – producing neural avalanches, and an organization to synfirechain like behaviour [8], and coherent infomax [9]. The goal function of coherent infomax
is to find coherent information between two streams of inputs from different sources, one
conceptualized as sensory input, the other as internal contextual information. As coherent infomax requires the precomputation of an integrated receptive field input as well as
an integrated contextual input to be computable efficiently (and thereby, in a biologically
plausible way), the theory predicted the recent discovery of two distinct sites of neural integration in neocortical pyramidal cells [10]. For details see the contribution of Phillips to
this special issue. We will revisit some of these goal functions below and demonstrate how
they fit in the larger abstract framework aiming at a unified description that is presented
here.
Apart from the desire for a unified description of the common goals of repeated
anatomical motifs, there is a second argument in favor of using an abstract framework.
This argument is based on the fact that a large part of neural communication relies on
axonal transmission of action potentials and on their transformation into post-synaptic
potentials by the receiving synapse. Thus, for neurons, there is only one currency of
information. This fact has been convincingly demonstrated by the successful rewiring of
sensory organs to alternative cortical areas that gave rise to functioning, sense-specific
perception (see for example the cross-wiring, cross-modal training experiments in [11]). In
sum, neurons only see the semantics inherent in the train of incoming action potentials,
not the semantics imposed by the experimenter. Therefore, a neurocentric framework
describing information processing must be necessarily abstract. From this perspective
information theory is again a natural choice.
Classic Shannon information theory, however, mostly deals with the transmission of
information through a communication channel with one input and one output variable. In
a neural setting this would amount to asking how much information present at the soma
of one cell reaches the soma of another cell across the connecting axons, synapses and
dendrites, or how much information is passed from one circuit to another. Information
processing, however, comprises more operations on information than just its transfer. A
long tradition dating back all the way to Turing has identified the elementary operations
of information as information transfer, active storage, and modification. Correspondingly,
measures of information transfer have been extended to cover more complex cases than
Shannon’s channels, incorporating directed and dynamic couplings [12] and multivariate
interactions [13], and also measures of active information storage have been introduced
[14]. Information modification, seemingly comprising of subfunctions such as de novo
creation and fusion of information, however, has been difficult to define [15].
One reason for extending our view of information processing to more complicated cases
is that even the most simple function from Boolean logic that any other logic function can
be composed of (NAND, see for example [16], chapter 1) uses two distinct input variables
and one output. While such a logic function could be described as a channel between the
two inputs and the outputs, this does not do justice to the way the two inputs interact with
each other. What is needed instead is an extension of classic information theory to three
way systems, describing how much information in the output of this Boolean function, or
any other three-way processor of information, comes uniquely from one input, uniquely

3

A

B

X2

C

X2=Ce/i

Ce/i
Ca2+

X1=Re/i

Na+

F

Re/i

Y

Y

Ca2+

X1

Modulatory
Interaction

Modulatory
Interactions

Na+

Y

Figure 1: Neural processors:(A) neural processor with multidimensional inputs X1 , X2 , and output Y .
(B) Processor with local weighted summation of inputs as used in coherent infomax and in this study.
To establish the link to the coherent infomax literature we identify the input X1 with the receptive field
input R, which may be excitatory (e) or inhibitory (i), and which is summed. In the same way, X2 is
identified with the contextual input C. (C) Overlay of the coherent infomax neural processor on a layer
5 pyramidal cells, highlighting potential parallels to existing physiological mechanisms. Layer 5 cells
created with the TREES toolbox [21], courtesy of Hermann Cuntz.

from the other input, how much they share about the output, and how much output
information can only be obtained from evaluating both inputs jointly.
These questions can be answered using an extension of information theory called
partial information decomposition (PID) [17, 18, 19, 20].
This article will introduce PID and show how to use it to specify a generic goal function for neural information processing. This generic goal function can then be adapted to
represent previously defined neural information processing goals such as infomax, coherent infomax and predictive coding. This representation of previous neural goal functions
in just one generic framework is highly useful to understand their differences and commonalities. Apart from a reevaluation of existing neural goal functions, the generic neural
goal function introduced here also serves to define novel goals not investigated before.
The remainder of the text will first introduce partial information decomposition, and
then demonstrate its use to decompose the total output information of a neural processor.
From this decomposition we derive a generic neural goal function “G”, and then express
existing neural goal functions as specific parameterizations of G. We will then discuss how
the use of G simplifies the comparison of these previous goal functions and how it helps
to develop new ones.
2. Partial Information decomposition
In this section we will describe the framework of partial information decomposition
(PID) to the extent that is necessary to understand the decomposition of the mutual
information between the output Y of a neural processor and a set of two inputs X1 , X2
(Figure 1). The inputs themselves may be multivariate random variables but we will not
attempt to decompose their contributions further. This is linked to the fact that in many
neurons contextual and driving inputs are first summed separately before being brought
to interact to produce the output. This summation strongly reduces the parameter space

4

and thereby makes learning tractable – see [22, 23].7 Therefore, we limit ourselves to the
PID of the mutual information between one “left hand side” or “output” variable Y and
two “right hand side” or “input” variables X1 , X2 . That is, we decompose the mutual
information I(Y : X1 , X2 ) 8 , the total amount of information held in the set {X1 , X2 }
about Y :9
I(Y : X1 , X2 ) =

X

p(x1 , x2 , y) log2

x1 ∈AX1 ,x2 ∈AX2 ,y∈AY

= H(Y ) − H(Y |X1 , X2 ) ,

p(y|x1 , x2 )
p(y)

(1)
(2)

where the A· signifiy the support of the random variables and H(·), H(·|·) are the entropy
and the conditional entropy, respectively (see [25] for definitions of these information
theoretic measures).
The PID of this mutual information addresses the questions:
1. What information does one of the variables, say X1 , hold individually about Y that
we can not obtain from any other variable (X2 in our case)? This information is
the unique information of X1 about Y : Iunq (Y : X1 \ X2 ).
2. What information does the joint input variable {X1 ; X2 } have about Y that we
cannot get from observing both variables X1 , X2 separately? This information is
called the synergy, or complementary information, of {X1 ; X2 } with respect to Y :
Isyn (Y : X1 ; X2 ).
3. What information does one of the variables, again say X1 , have about Y that we
could also obtain by looking at the other variable (X2 ) alone? This information is
the shared information10 of X1 and X2 about Y : Ishd (Y : X1 ; X2 ).
Following [17], the above three types of partial information terms together by definition
provide all the information that the set {X1 , X2 } has about Y , and other sources agree
on this [17, 20, 18, 19], i.e.:

I(Y : X1 , X2 ) = Iunq (Y : X1 \X2 )+Iunq (Y : X2 \X1 )+Ishd (Y : X1 ; X2 )+Isyn (Y : X1 ; X2 ) ,
(3)
Figure 2 is a graphical depiction of this notion by means of the partial information (PI-)
diagrams introduced in [17]. In addition, there is agreement that the information one
input variable has about the output should decompose into a unique and a shared part
7 Furthermore, the formulation of measures providing generally-accepted decompositions [19, 20] at
the present time are only defined for two variables [24].
8 As the concepts of unique, shared and synergistic information require a more fine grained distinction
of how individual variables are grouped, we employ the following extended notation that was introduced
in [19] and defined in Appendix Appendix A: “:” separates sets of variables between which mutual
information or partial information terms are computed, “;” separates multiple sets of variables on one
side of a partial information term, whereas “,” separates variables within a set that are considered jointly
(see the Appendix Appendix A for examples).
9 See notational definitions in Appendix Appendix A.
10 Also known as redundant information in [17].

5

as:
I(Y : X1 ) = Iunq (Y : X1 \ X2 ) + Ishd (Y : X1 ; X2 )
I(Y : X2 ) = Iunq (Y : X2 \ X1 ) + Ishd (Y : X1 ; X2 ) .

(4)

For the treatment of neural goal functions we have to furthermore give PID representations of the relevant conditional mutual information terms. These can be obtained
from equations 3 and 4 as :
I(Y : X1 |X2 ) = Iunq (Y : X1 \ X2 ) + Isyn (Y : X1 ; X2 )
I(Y : X2 |X1 ) = Iunq (Y : X2 \ X1 ) + Isyn (Y : X1 ; X2 ) .

(5)

Moreover, all parts of the PI-diagram are typically required to be positive to allow an
interpretation as information terms.

(Y
I syn

)
;X 2
1
X
:

Iunq(Y : X1\X 2)

Ishd(Y : X1;X 2)
Iunq(Y : X1\X 2)
I(Y : X 1)
I(Y : X 1; X 2)

I(Y : X 2)

Figure 2: Partial information diagram with both classical information terms (solid lines) and PID terms
(color patches).

Due to the pioneering work of Williams and Beer [17] it is now well established that
neither unique, nor shared, nor synergistic information can be obtained from the definitions of entropy, mutual information and conditional mutual information in classical
information theory. Essentially, this is because we have an underdetermined system, i.e.
we have fewer independent equations relating the output and inputs in classical information theory (three for two input variables) than we have PID terms (four for two input
variables). For at least one of these PID terms a new, axiomatic definition is necessary,
from which the others then follow, as per equations 3-5. To date, the equivalent axiom
systems introduced by Bertschinger and colleagues [19], and by Griffiths and Koch [20]
have found the widest acceptance. They also yield results that are very close to an earlier
proposal by Harder and colleagues [18]. All of these axiom systems lead to measures that
are sufficiently close to a common sense view of unique, shared and synergistic information, and all satisfy equations 3-5. Hence, their exact details do not matter at first reading
for the purposes of this paper, and will therefore be presented in Appendix Appendix B.

6

The one exception to this statement is that we have to mention here already that
shared information may arise in the frameworks of Bertschinger at al. [19], Griffiths et
al. [20] , and also Harder et al. [18] for two reasons. First, there can be shared information
because the two inputs X1 , X2 have mutual information between them (termed source
redundancy in [18], and source shared information here) – this is quite intuitive for most.
Second, shared information can arise because of certain mechanisms creating the output
Y (mechanistic redundancy in [18], mechanistic shared information here). This second
possibility of creating shared information is less intuitive but nevertheless arises in all
of the frameworks mentioned above. For example, the binary AND operation on two
independent (identically distributed) binary random variables creates 0.311 bits of shared
information in [19, 18, 20], and 0.5 bits of synergistic mutual information, while there is
no unique information about the inputs in its output.
3. A generic decomposition of the output information of a neural processor
We use PID in this section to decompose the information H(Y ) that is contained in
the output of a general neural processor (Figure 1) with two input (sets) X1 and X2 and
an output Y :
H(Y ) =I(Y : X1 , X2 ) + H(Y |X1 , X2 )

(6)

=Iunq (Y : X1 \ X2 ) + Iunq (Y : X2 \ X1 )
+ Ishd (Y : X1 ; X2 ) + Isyn (Y : X1 ; X2 )
+ H(Y |X1 , X2 ) .
To arrive at a neural goal function we can add weight coefficients to each of the terms
in the entropy decomposition above to specify how ’desirable’ each one of one of these
should be for the neural processor, i.e. we can specify a neural goal function G as a
function of these coefficients. Since all the terms in equation 6 are non-overlapping, and
the coefficients can be be chosen independently, this is the most generic way possible to
specify such a goal function:
G =Γ0 Iunq (Y : X1 \ X2 ) + Γ1 Iunq (Y : X2 \ X1 )

(7)

+ Γ2 Ishd (Y : X1 ; X2 ) + Γ3 Isyn (Y : X1 ; X2 )
+ Γ4 H(Y |X1 , X2 ) .
which can also be rewritten with another set of of coefficients γi as:
G =γ0 Iunq (Y : X1 \ X2 ) + γ1 Iunq (Y : X2 \ X1 )

(8)

+ γ2 Ishd (Y : X1 ; X2 ) + γ3 Isyn (Y : X1 ; X2 )
+ γ4 H(Y ) ,
using γi = Γi − Γ4 (i = 0 . . . 3), γ4 = Γ4 (and equation 6).
Note that training a neural processor will obviously change the value of the goal
function in equation 7, but of course also change the relative composition of the entropy
in equation 6.

7

This decomposition of the entropy and its parametrization are closely modeled on the
approach taken by Kay and Phillips in their formulation of another versatile information
theoretic goal function (“F ”, see below) for the coherent infomax principle [9, 26, 22, 23].
In general, we will choose the formulation used in equation 7 because the conditional
entropy does not overlap with the parts in the PI-diagram (Figure 2), but note that the
formulation used in equation 8 may be useful when goals with respect to total bandwidth,
rather than unused bandwidth, are to be made explicit. This could for example happen
when neuronal plasticity acts to increase to total bandwidth of a neural processor11 .
In the next sections we introduce coherent infomax and analyze it by means of PID.
We then show how to (re-)formulate infomax, and predictive coding using specific choices
of parameters for G. Last, we will introduce a neural goal function, called coding with
synergy, that explicitly exploits synergy for information processing.
4. The coherent infomax principle and its goal function as seen by PID
4.1. The coherent infomax principle
The coherent infomax principle (CIP) proposes an information theoretically defined
neural goal function in the spirit of domain-independence laid out in the introduction, and
a neural processor implementing this goal function [9, 26, 22, 23]. The neural processor
operates on information it receives from two distinct types of inputs X1 , X2 and send
the results to a single output Y (see Figure 1). The two distinct types of input in CIP
were described as driving and modulatory, formally defined by their distinct roles in local
processing as detailed in the coherent infomax principles CIP.1-CIP.4, below. Here we
will denote the driving input by X1 , and the contextual input by X2 .
In the mammalian brain the driving input X1 includes, but is not limited to, both
external information received from the sensors and information retrieved from memory.
The contextual input X2 arises from diverse sources as lateral long-range input from the
same or different brain regions, descending inputs from hierarchically higher regions, and
input via non-specific thalamic areas. Phillips, Clark and Silverstein [27] provide a recent
in-depth review of this issue in relation to the evidence for such distinct inputs from
several disciplines.
The coherent infomax principle (CIP) states the following four goals of information
processing:
CIP.1 The output Y should transmit information that is shared between the two inputs,
so as to enable the processor to preferentially transmit information from the driving
inputs (X1 ) that is supported by context-carrying information from internal sources
elsewhere in the system arriving at input X2 . This is what the term ’coherent’ refers
to.
CIP.2 The output Y could transmit some information that is only in the driving input
X1 , but not in the context, so as to enable that local processors transmit some
11 Along similar lines one may wish to add the total information in both inputs H(X ) and H(X )
1
2
(or,H(X1 |Y, X2 ) and H(X2 |Y, X1 ), respectively) to G. However, since the neural processor has only
control over the output Y , changing the amount of this initial information in the inputs is beyond the
scope of its goal function.

8

information that is not related to the information currently available to it from
elsewhere in the system.
CIP.3 The output Y should minimize transmission of information that is only in the
contextual input X2 . This is necessary to ensure that the effects of the context
do not become confounded with the effects of the drive and thereby reduce the
reliability of coding .
CIP.4 The output Y should be optimally used in terms of bandwidth.
To state these goals more formally, Kay and Phillips first decomposed the total entropy
of the output, H(Y ) as:
H(Y ) = I(Y : X1 : X2 ) + I(Y : X1 |X2 ) + I(Y : X2 |X1 ) + H(Y |X1 , X2 ) ,

(9)

where the three-term multi-information I(Y : X1 : X2 ) is defined as:
I(Y : X1 : X2 ) = I(X1 : Y ) − I(X1 : Y |X2 )
= I(X1 : X2 ) − I(X1 : X2 |Y )
= I(Y : X2 ) − I(Y : X2 |X1 ) .

(10)

Kay and Phillips then re-weighted the terms of this decomposition by coefficients Φi
to obtain a generic information theoretic goal function F as:
F = Φ0 I(Y : X1 : X2 ) + Φ1 I(Y : X1 |X2 ) + Φ2 I(Y : X2 |X1 ) + Φ3 H(Y |X1 , X2 )

(11)

Here, the first term, I(Y : X1 : X2 ), was meant to reflect the information in the
output that is shared between the two inputs, the second term the information in the
output that was only in the driving input, the third term the information in the output
that was only in the contextual input, while the last term represents the unused bandwidth
(see Figure 3 for a graphical representation of these terms). Below, these assignments
will be investigated using PID.
In previous work [9], the goal of coherent infomax was implemented by setting Φ0 =
1, Φ1 = Φ2 = Φ3 = 0, leading to the objective function I(Y : X1 : X2 ). While this
objective function appears not to explicitly embody any asymmetry between the influences
of the X1 and X2 inputs, it is important to realize that the modulatory role played by
the contextual input X2 is expressed through the special form of activation function
introduced in Phillips et al. (1995), and defined in Appendix 7.4. The possibility of
expressing this asymmetry explicitly in the objective function was also discussed in [9, 26]
by taking Φ0 = 1, 0 ≤ Φ1 < 1, Φ2 = Φ3 = 0, leading to the goal function
FCIP = I(Y : X1 : X2 ) + Φ1 I(Y : X1 |X2 ),

(12)

which is a weighted combination of the multi-information and the information between
Y and the driving input X1 conditional on the contextual input X2 . This last term was
meant to represent information that was both in the output Y and the driving input X1 ,
but not in the contextual input X2 .

9

Next, we will investigate how this goal function FCIP implements the goals CIP.1CIP.4 when these are restated using the language of PID.
4.2. F as seen by PID
We first take the generic goal function F from equation 11, that is independent of CIP
proper, and rewrite it as a sum of mutual information terms and decompose these using
PID. We will sort the resulting decomposition by PID terms and compare this result to
the general goal function G. This will tell us about the space of goal functions covered
by F . Knowing this space is highly useful as a working neural network implementation
of F with learning rules exists (reviewed in [22, 23]). This implementation can also be
used to implement goal functions formulated in the precise PID framework based on G,
whenever the specific G that is of interest lies in the space that can be represented by
F ’s.
We begin by decomposing F mutual information terms:
F =Φ0 I(Y : X1 : X2 ) + Φ1 I(Y : X1 |X2 ) + Φ2 I(Y : X2 |X1 ) + Φ3 H(Y |X1 , X2 )
=Φ0 (I(Y : X2 ) − I(Y : X2 |X1 ))
+ Φ1 (I(Y : X1 , X2 ) − I(Y : X2 ))
+ Φ2 (I(Y : X2 , X1 ) − I(Y : X1 ))
+ Φ3 H(Y |X1 , X2 ) ,

(13)

which, using the PID equations 3-5, and collecting PID terms, turns into:
F =Φ1 Iunq (Y : X1 \ X2 )
+ Φ2 Iunq (Y : X2 \ X1 )
+ Φ0 Ishd (Y : X1 ; X2 )
+ (Φ1 + Φ2 − Φ0 )Isyn (Y : X1 ; X2 )
+ (Φ3 )H(Y |X1 , X2 ) .

(14)

Comparing this to the general PID goal function G, we see that the coefficients Γ =
[Γ0 . . . Γ4 ] and Φ = [Φ0 . . . Φ3 ] are linked by the matrix Ω as:
ΩΦ =: Γ


0

 0

Ω=
 1

 −1
0

(15)


1 0 0

0 1 0 

0 0 0 
 .

1 1 0 
0 0 1

(16)

Since Ω is not invertible, there are parameter choices in terms of Γ that have no counterpart in Φ. These are described by the complement of the range of this matrix (the null

10

space of ΩT ). This one-dimensional subspace is described by12 :
VΓ = {Γ ∈ R5 : Γ = α · [−1, −1, 1, 1, 0]T , α ∈ R} .

(17)

The existence of this subspace of coefficients not expressible in terms of Φi ’s means that
it is impossible to prescribe the goal of simultaneously maximizing synergistic and shared
information, while minimizing the two unique contributions, and vice versa when using
F . Ultimately, the existence of a subspace not representable by Φi ’s is a consequence of
the fact that PID terms cannot be expressed using classic information theory (while F in
contrast was defined from classical information theoretic terms only).
4.3. The coherent infomax principle as seen by PID
For the investigation of the specific goal function FCIP , we first want to clarify how
we understand the four goals listed in the previous section. To this end we identify them
one to one with goals in terms of PID as:
1. → CIP.1: The output should contain as much shared information Ishd (Y : X1 , X2 )
as possible.
2. → CIP.2: The output could contain some unique information Iunq (Y : X1 \ X2 ).
3. → CIP.3: The output should minimize unique information Iunq (Y : X2 \ X1 ).
4. → CIP.4: The unused output bandwidth H(Y |X1 , X2 ) should be minimized.
With respect to item 1 on this list, it is important to recall from section 2 that shared
information can arise from mutual information between the sources (source shared information) or be created by a mechanism in the processor (mechanistic shared information).
Kay and Phillips had in mind the first of these two possibilities.
To see whether FCIP indeed reflects these goals as stated via PID, we look at the
specific choice of parameters, Φ0 = 1, 0 ≤ Φ1 < 1, Φ2 = Φ3 = 0, that was used to
implement the coherent infomax principle, and find using equations 3-5 (the reader may
also verify this graphically using Figure 3):
FCIP = Ishd (Y : X1 ; X2 ) + Φ1 Iunq (Y : X1 \ X2 ) − (1 − Φ1 )Isyn (Y : X1 ; X2 ).

(18)

We will now discuss the various contributions to FCIP in detail, starting with the
shared information, which figures most prominently in the goals CIP.1-CIP.4.
Shared information. We see that shared information is maximized. This shared information contains contributions from mutual information between the sources (source shared
information) as well as shared information created by mechanisms in the processor (mechanistic shared information, see the note on item 1 above). The first type of shared information is the one aimed for in CIP.1. Thus, for inputs that are not independent the
coherent infomax goal function indeed maximizes source shared information as desired.
We will investigate the case of independent inputs below.
12 The corresponding nullspace for the γ reads: V = {γ ∈ R5 : γ = α · [−1, −1, 1, 1, 0]T ,
γ
i

11

α ∈ R}.

Unique information. In addition to the shared information, the unique information from
the driving input is also maximized, albeit to a lesser degree. In contrast, synergy between
the output and the combined inputs is minimized. Therefore, goals 1, 2 and 3 are expressed explicitly in this objective function but there is no explicit mention of minimizing
the output bandwidth.
Synergistic information. Of all the PID terms, synergy is discouraged. This may at first
seem surprising as the mapping of goals of coherent infomax to PID, did not appear
to make any explicit statements about synergistic components – unless one views the
transmission of undesirable synergistic components as being an extra component of the
bandwidth (along with H(Y |X1 , X2 )) that is not used in the optimal attainment of goals
1-3. Nevertheless the minimization of synergy serves the original goals of coherent infomax. This can be seen when we consider that these were formulated for two different
types of inputs, driving and modulatory. For these two types of input, the goal of coherent
infomax is to use the modulatory inputs to guide transmission of information about the
driving inputs. Synergistic components would transmit information about both driving
and modulatory inputs, so transmitting them would be treating the modulatory inputs
as driving inputs. This is clearly undesirable in the setting of coherent infomax.
At a more technical level, we note the trade-off in that increasing the value of the
parameter Φ1 towards 1 at once serves to enhance promotion of the unique information
from the driving input while simultaneously lessens the pressure to minimize the synergy.
This is a remnant of the term Φ1 I(Y : X1 |X2 ) in equation 12 which had been included in
order to capture information that was both in Y and X1 but not in X2 (i.e. the unique
information from the driving input), but inadvertently also served to capture the synergy.
In terms of the range of tasks that can be learned by a processor with FCIP , the
minimization of synergy between the two types of inputs means for example that learning
tasks that require a lot of synergy between the inputs, like the XOR-function, cannot be
achieved easily. It is crucial, however, to realize that discouragement of synergy concerns
only relations between drive X1 and modulation X2 . In contrast, synergistic relations
between just the components of a multivariate X1 can be learned by the coherent infomax
learning rule. The XOR between components of X1 for example can be learned reliably if
supervised, and still occasionally if not [9].
Independent sources. What remains to be investigated is what the goal functions aims for
in the specific case of statistically independent inputs, i.e. when source shared information
cannot be obtained. In other words, we may ask whether the coherent infomax processor
will maximize mechanistic shared information in this case?
Since the mutual information between the inputs, I(X1 : X2 ), is assumed to be zero,
then using one of the forms of the multi-information (eq. 10) we have
I(Y : X1 : X2 ) = I(X1 : X2 ) − I(X1 : X2 |Y ) = −I(X1 : X2 |Y )

(19)

and so the multi-information is non-positive. It follows from the other forms of the multiinformation (eq. 10) that
I(Y : X1 |X2 ) ≥ I(Y : X1 )

and I(Y : X2 |X1 ) ≥ I(Y : X2 ).

12

(20)

This implies directly (compare 2A) that for independent inputs we must have:
Ishd (Y : X1 ; X2 ) ≤ Isyn (Y : X1 ; X2 ) ,

(21)

– an important additional constraint that arises from independent inputs. Thus, in this
case the minimization of synergy and the maximization of shared information compete,
giving more effective weight to the unique information from the driving input. Nevertheless, limited shared information may exist in this scenario, and if so it will be of the
mechanistic type.
In sum, we showed that (i) the generic goal function F in the coherent infomax
principle cannot represent all goal functions that are possible in the PID framework using
the goal function G – specifically, F lacks one degree of freedom; (ii) for the CIP this
leads to a weighted maximization of the shared information (source shared information
and mechanistic shared information) and the unique information from the driving input;
(iii) it can be shown that within the space of all possible goal functions F it is impossible
to maximize synergy and shared information together, while minimizing the two unique
information terms, and vice versa; (iv) and for the CIP synergy between the driving and
modulatory inputs is explicitly discouraged.
A

C

B
H(Y:(X1,X2))

I(Y:X1 | X2)

Φ3

I(Y:X2)

H(Y)
I(Y:(X1,X2))

Φ1

I(Y:X1)

E

D

F
I(Y:X2) (+)
I(Y:X2|X1) (-)

I(Y:X2 | X1)

Φ2

Φ0

Φ0 Φ1 Φ2

Figure 3: Graphical depiction of the various contributions to F and their weighting coefficients in the
PID diagram. (A) Classical unconditional mutual information terms. (B) Unused bandwidth, weighted
by Φ3 . (C) Conditional mutual information I(Y : X1 |X2 ), weighted by Φ1 . (D) Conditional mutual
information I(Y : X2 |X1 ), weighted by Φ2 . Note the overlap of this contribution with the one from (C).
(E) The three way information I(Y : X1 : X2 ), weighted by Φ0 . Here the three way information is the
checkered minus the striped area. (F) This region appears in (C),(D),(E) and is weighted accordingly by
three coefficients simultaneously (Φ0 ,Φ1 , Φ2 ). The area in (F) is the synergistic mutual information that
is also shown in cyan in Fig. 2.

13

5. Partial information decomposition as a unified framework to generate neural goal functions
In the this section we will use PID to investigate infomax, another goal function
proposed for neural systems, and we will formulate an information-theoretic goal function
for a neural processor aimed at predictive coding.
5.1. Infomax
To investigate infomax, we recall that the goal stated there is to maximize the information in the output about the relevant input X1 , which typically is multivariate [6].
This goal function is implicitly designed for situations with limited output bandwidth, i.e.
H(X1 ) > H(Y ). Not considering a second type of input X2 it is obvious that PID will not
contribute to the understanding of infomax. This changes however if the variables in a
multivariate input will be considered separately. Then, it may make sense to ask whether
the output information in a given system is actually being maximized predominantly due
to unique or synergistic information.
Mathematically, the infomax goal can also be represented by using F with two types
of inputs X1 , X2 , where the information transmitted about X1 is to be maximized. This
can be achieved by choosing Φ0 = Φ1 = 1 to obtain (e.g. [22]):

FIM =Φ0 I(Y : X1 : X2 ) + Φ1 I(Y : X1 |X2 )

(22)

=Iunq (Y : X1 \ X2 ) + Ishd (Y : X1 ; X2 )
=I(Y : X1 ) .
The insight to be gained using PID here is that infomax does not incorporate the use
of auxiliary variables X2 to extract even more information from X1 via the synergy
I(Y : X1 ; X2 ), nor does it prefer either shared or unique information over the other.
5.2. Predictive coding
In predictive coding the goal is to predict inputs X1 (t) using information available
from past inputs X1 (t − 1) = [X1 (t − 1) . . . X1 (t − k)]13 . Thus, the processor has
to learn a model MP C that yields predictions X2 (t) = MP C (X1 (t − 1)), such that
X2 (t) ≈ X1 (t). This is the same as maximizing the mutual information between outcome and prediction I(X1 (t), X2 (t)) = I(X1 (t), MP C (X1 (t − 1))), at least if we do not
care how exactly X2 (t) represents 14 the prediction. Under some mild constraints 15 the
data processing inequality here actually states that trying to tackle this problem information theoretically is trivial, as I(X1 (t), X2 (t)) = I(X1 (t), MP C (X1 (t − 1))) is maximized by MP C (X1 (t − 1)) = X1 (t − 1), i.e. all the information we can ever hope to
13 These past inputs may in principle lie arbitrarily far in the past (i.e. with arbitrarily large k), meaning
that also long term memory in a system may contribute to the predictions.
14 Here, representation is used in the sense of lossless encoding. Thus, for us X (t) is equivalent to all
2
lossless (re-)encodings of X2 (t), e.g. in other alphabets, amongst others the alphabet of X1 (t).
15 The relevant constraints here are that the collections of input values X (t) are sampled appropriately,
1
such that they form a Markov chain X1 (t − 2) → X1 (t − 1) → X1 (t)

14

exploit for prediction is already in the raw data (and it is a mere technicality to extract it in a useful way). The whole problem becomes interesting only when there is
some kind of bandwidth limitation on MP C , i.e. when for example MP C (X1 (t − 1))
has to use the same alphabet as X1 (t), meaning that we have to state our prediction
as a single value that X1 (t) will take. Of course, this actually is the typical scenario
in neural circuits. Therefore, we state the main goal of predictive coding as maximizing I(X1 (t), X2 (t)) = I(X1 (t), MP C (X1 (t − 1))), under the constraint that X1 (t) and
MP C (X1 (t − 1))) have the same “bandwidth” (the same raw bit content to be precise).
Despite of the goal to maximize a simple mutual information this is not an infomax problem, due to the temporal order of the variables, i.e. we need the output X2 (t) before the
input X1 (t) is available. Thus, we have to find a different solution to our problem.
To this end, we suggest that a minimal circuit performing predictive coding will have to
perform at least three subtasks, (i) produce predictions as output, (ii) detect whether there
were errors in the predictions, (iii) use these for learning. In Fig. 4 we detail a minimalistic
circuit performing these tasks, with subtask (i) represented in X2 (t), subtask (ii) in Y (t)
and subtask (iii) in MP C . This circuit assumes the following properties for its neural
circuits: (a) neurons have binary inputs and outputs, (b) information passes through a
neuron in one direction, and (c) information from multiple inputs can be combined into
one output only. The circuit consists of two separate units: (1) the error detection unit
that operates on past predictions X2 (t − 1) = MP C (X1 (t − 2)), obtained via a memory
buffer, and past inputs X1 (t − 1), to create the output Y via an XOR operation, with
y = 1 indicating an erroneous prediction in the past; (2) the prediction unit that has the
capability to produce output based on a weighted summation over a vector of past inputs
X1 (t − 1) via a weighting function in the model MP C . MP C will update its weights
whenever an error was received.
Outputs

current
prediction

last
error

XOR

0 = do not update
I = update MPCT

Memory

Inputs

Figure 4: Graphical depiction of a minimalistic, binary predictive coding circuit. This circuit can be
conceived of as one neural processor (indicated by the box) with inputs X1 (t − 1), X1 (t − 1) and (main)
output Y (t).

15

We suggest that the information theoretic goal function of this circuit is simply to
minimize the entropy of the output of the error unit, i.e. H(Y ). In principle, this would
drive the binary output of the circuit either to p(y = 1) → 1 or to p(y = 0) → 1. Of these
two possibilities, only the second one is stable, as the constant signaling of the presence
of an error will lead to incessant changes in MP C , which in turn will change Y even for
unchanging input X1 . Thus, minimizing H(Y ) should enforce pY (y = 0) → 1. Therefore,
we can formulate an information theoretic goal function of the form G if we conceive of
the whole circuit as being just one neural processor with inputs X1 (t − 1) and X1 (t − 1),
and as having the error Y as its main output. In this case, we find as a goal function for
the predictive coding error (PCE):
GP CE =γ0 Iunq (Y : X1 (t − 1) \ X1 (t − 1))

(23)

+ γ1 Iunq (Y : X1 (t − 1) \ X1 (t − 1))
+ γ2 Ishd (Y : X1 (t − 1); X1 (t − 1))
+ γ3 Isyn (Y : X1 (t − 1); X1 (t − 1))
+ γ4 H(Y ) ,
with the weights γP CE = [0, 0, 0, 0, −1] using the γ-notation from equation 8 where the
total output entropy was made explicit, or equivalently, ΓP CE = [−1, −1, −1, −1, −1].
Interestingly, this goal function formally translates to Φ = [−1, −1, −1, −1], or F =
−H(Y ). This gives hope that one can translate the established formalism for F to the
present case by taking into account that the original architecture behind F is augmented
here by an additional XOR subunit. Learning of the circuit’s goal function may have to
proceed in two steps if we do not have subunits able to perform XOR at the beginning.
In this case, the “XOR” subunit will first have to learn to perform its function. This can
be achieved by maximizing the synergy of two uniform, random binary inputs and the
subunit’s output Y . After this initial learning the XOR-subunit is ‘frozen’ and learning of
predictions can proceed to minimize H(Y ). One conceivable mechanism for this would be
to use learning based on coincidences between input bits in M (X1 (t − 2)) and the error
bit Y .
We note that this goal function is not entirely new, as the idea of making the output
of a processing unit as constant as possible in learning has been used before in various
implementations (e.g. [28, 29, 30]). It is also closely related to the homeostatic goals
pursued by the free energy minimization principle [31, 32, 33]. We have merely added here
a generic minimal circuit diagram and the information theoretic interpretation to these
previous approaches. Also, note that the actual prediction X2 (t) = MP C (X1 (t − 1))
must be implicitly part of the information theoretic goal function, as the goal function
we suggest here would be nonsensical on many other circuits.
As a next level of complication one may consider that the predictions X2 that are
created within our minimal circuit are sent back to the source of the input X1 to interact
with it there. One such interaction scheme will be studied in the next section.

16

6. Coding with synergy
So far the goal functions investigated in our unifying framework G had in common
that maximization of synergy did not appear as a desirable goal. This may historically
be simply due to the profound mathematical difficulties that had to be overcome in the
definition of synergistic information. In this section we will therefore show how synergy
naturally arises in a generalization of ideas from efficient coding by PID. We will call the
goal function simply coding with synergy (CWS).
The neural coding problem that we will investigate here is closely related to predictive coding discussed in the previous section. However, in contrast to predictive coding
where the creation of predictions was in focus, here we focus on possible uses of prior (or
contextual) information from X2 , be it derived from predictions or by any other means.
In other words, we here simply assume that there is (valid) prior information in the system that does not have to be extracted from the ongoing input stream X1 by our neural
processor. Moreover, we assume that there is no need to waste bandwidth and energy on
communicating X2 as this information is already present in the system. Last, we assume
that we want to pass as much of the information in X1 as possible, as well as of the
information created synergistically by X1 and X2 . This synergistic information will arise
for example when X2 serves to decode or disambiguate information in X1 .
Looking at the PID diagram (Fig. 2) one sees that in this setting it is optimal to
minimize Iunq (Y : X2 \ X1 ) and the unused bandwidth H(Y |X1 , X2 ) while maximizing
the other terms. This leads to:

GCW S =Iunq (Y : X1 \ X2 )

(24)

− Iunq (Y : X2 \ X1 )
+ Ishd (Y : X1 ; X2 )
+ Isyn (Y : X1 ; X2 )
− H(Y |X1 , X2 ) ,
or Γ = [1, −1, 1, 1, −1]. The important point here is that this is different from maximizing
just I(Y : X1 |X2 ), as this would omit the shared information, i.e. we would lose this part
of the information in X1 . The goal function GCW S is also different from just maximizing
I(Y : X1 ), as this would omit the synergistic information, i.e. the possibility to decode information from X1 by means of X2 . Furthermore, there is no corresponding goal function
F here in terms of classical information theoretic measures. This can easily be proven by
noting that Γ = [1, −1, 1, 1, −1] has a non-zero projection in VΓ (equation 17). In other
words, there is no Φ that satisfies equation 15.
Given there were bandwidth constraints on Y , one might want to preferentially communicate one or two of the positively weighted terms in equation 24. The natural choice
here is to favor synergy and unique information about X1 , because the shared information
with X2 is already in the system. If just one contribution can be communicated this leaves
us with three choices. We will quickly discuss the meaning of each here: first, focusing on
the unique information Iunq (Y : X1 \ X2 ) emphasizes the surprising information in X1 ,
because this is the information that is not yet in the system at all (i.e. not in X2 ); second,

17

focusing on the shared information Ishd (Y : X1 ; X2 ) basically leads to coherent infomax;
third, focusing on the synergistic information Isyn (Y : X1 ; X2 ) emphasizes information
which can only be obtained when putting together prior knowledge in X2 and incoming
information X1 - this would be the extreme case of CWS. This case should arise naturally in binary error computation, e.g. in error units suggested as integral parts of certain
predcitive coding architectures (see [3] for a discussion of error units, also compare the
XOR unit in Figure 4).
A classic example for this last coding strategy would be cryptographic decoding. Here,
the mutual information between cypher text (serving as input X1 ) and plain text (serving
as output Y ) is close to zero, i.e. I(Y : X1 ) ≈ 0, given randomly chosen keys and a
well performing cryptographic algorithm. Nevertheless the mutual information between
the two, given keys (serving as input X2 ), is the full information of the plain text, i.e.
I(Y : X1 |X2 ) = H(Y ), assuming the unused bandwidth is zero (H(Y : X1 , X2 ) = 0). As
the mutual information between key and plain text should also be zero (I(Y : X2 ) = 0)
we see that in this case the full mutual information is synergistic: I(Y : X1 , X2 ) =
Isyn (Y : X1 ; X2 ). In a similar vein, any task in neural systems that involves an arbitrary
key-dependent mapping between information sources – as in the above cryptographic
example – will involve CWS. One such task would be to read a newspaper printed in
Latin characters (which could be in quite a range of languages) to get knowledge about
the current state of the world (or at least some aspects of it). Visually inspecting the text,
without the information incorporated in the rules of the unknown written language used
will not reveal information about the world. Yet, having all the information on the rules
of written language, without having a specific text will also not reveal anything about
the world. To obtain this knowledge we need, both, the text of the newspaper and the
language-specific information how written words map to possible states of the world.
A corollary of the properties of synergistic mutual information is that when a neuron’s inputs are investigated individually they will seem unrelated to the output – to the
extent that synergistic information is transmitted in the output. Therefore, the minimal
configuration of neuronal recordings needed to investigate the synergistic goal fucntion
is a triplet of two inputs and one output. Thus, though coding with synergy has not
been prominent in empirical reports to date, it might become more frequently detected
as dense and highly parallel recordings of neuronal acticity become more widely available.
The general setting of coding under prior knowledge discussed here is also related
to Barlow’s efficient coding hypothesis [34] if we take the prior information X2 to be
information about which inputs to our processor are typical for the environment it lives
in. We here basically generalize Barlow’s principle by dropping reference to what the
input or the prior knowledge are about.
Last, this goal function seems significant to us as synergy is seen by some authors as
useful in an formal definition of information modification (e.g. [15]). Thus synergy is a
highly useful measure in the description of neural processor with two or more inputs (or
one input and an internal state), as it taps into the potential of the processor to genuinely

18

modify information 16
7. Discussion
7.1. Biological neural processors and PID
In this study we introduced partial information decomposition (PID) as a universal
framework to describe and compare neural processors in a domain-independent way. PID
is indispensable for the information theoretic analysis of systems where two (or more)
inputs are combined to one output, because it allows to decompose the information in
the output into contributions provided either uniquely by any one of the inputs alone
(unique information), by either of them (shared information), or only by both of them
jointly (synergistic information). Using PID, the information processing principles of the
processor can be quantitatively described by specific coefficients Γ for each of the PID
contributions in a PID-based goal function G(Γ), which the processor maximizes.
This framework is useful in several ways. First, and perhaps most importantly, it
allows the principled comparison of existing neural goal functions, such as infomax, coherent infomax, predictive coding, and efficient coding. Second, it aids in the design of
novel neural goal functions. Here we presented a specific example, coding with synergy
(CWS), that exploits synergy to maximize the information that can be obtained from the
input when prior information is available in the system. Note, however, that the actual
implementation of a neural circuit maximizing the desired goal function is not provided
by the new framework and will have to be constructed on a case by case basis at the moment. This is in contrast to coherent infomax where a working implementation is known.
Third, applying this framework to neural recordings may help us understand better how
neural circuits that are far away from sensory and motor periphery, and for which we do
not have the necessary semantics, function.
Currently, the applicability of our framework rests on the assumption that a neural
processor with two inputs is a reasonable approximation of a neuron or microcircuit 17 .
Of course, neurons typically have many more inputs than just two. However, if such
inputs naturally fall into two groups, e.g. being first integrated locally in two groups on
the dendrites before being brought to interact at the soma, then indeed the two input
processor is a useful approximation. If, moreover, these integrated inputs are measured
before their fusion in the soma, then the formalism of goal functions presented here will
allow us to assess the function of this neuron in a truly domain independent way, relying
only on information that is also available to the neuron itself.
For example, two such spatially segregated and separately integrated inputs can be
distinguished on Pyramidal cells (Fig. 1). Pyramidal cells are usually highly asymmetric
and consist of a cell body with basal dendrites and an elongated apical dendrite that
rises to form a distal dendritic tuft in the superficial cortical layers. Thus, the inputs
are spatially segregated into basal/perisomatic inputs, and inputs that target the apical
16 Most interestingly, the current definition of information transfer via the transfer entropy [12] actually
also contains an element of synergy between the source’s and the target’s past [35], and thus there are
basically modifying and non-modifying forms of information transfer.
17 Although the work of Griffiths [20] and colleagues as well as Bertschinger and colleagues [24] allows
some extensions to more inputs and outputs, respectively.

19

tuft. Intracellular recordings indicate that there are indeed separate integration sites for
each of these two classes of input, and that there are conditions in which apical inputs
amplify (i.e. modulate) responses to the basal inputs in a way that closely resembles
the schematic two-input processor shown in Fig. 1. There is also emerging evidence
that these segregated inputs have driving and modulatory functions and are combined in
a mechanism of apical amplification of basal inputs – resembling the coherent infomax
goal function. Direct and indirect evidence on this apical amplification and its cognitive
functions is reviewed by Phillips [submitted to this special issue]. That evidence shows
that apical amplification occurs within pyramidal cells in the superficial layers, as well
as in layer 5 cells, and suggests that it may play a leading role in the use of predictive
inferences to modulate processing.
Which of the goal functions proposed here, e.g infomax, coherent infomax, or coding
with synergy a neural processor actually performs is an empirical question that must be
answered by analyzing PID footprints of G obtained from data recorded in neural processors. At present this is still a considerable challenge when applied to the level of single
cells or microcircuits because this requires the separate recording of at least one output
and two inputs, wich must moreover be of different type in the case of coherent infomax.
Next, the PID terms have to be estimated from data, instead of distributions that are
known. This type of estimation is still a field of ongoing research at present. Overcoming
these challenges will yield in-depth understanding of, for example, the information processing of the layer 5 cell described above in terms of PID, and elucidate which of the
potential goal functions is implemented in such a neuron.
In the spirit of the framework proposed here, classical information theoretic techniques
have already been applied to psychophysical data to search for coherent infomax-like processing at this level [36]. These studies confirmed for example that attentional influences
are modulatory, and showed how modulatory interactions can be distinguished from interactions that integrate multiple driving input streams. These result are a promising
beginning of a more large scale analysis of neuronal data at all levels with information
theoretic tools, such as PID.
Further information theoretic insight relevant to predictive processing may also be
gained by relating the predictable information in a neural processor’s inputs (measured
via ’local active information storage’ [14]) to the information transmitted to its output
(measured via transfer entropy [12], or local transfer entropy [13]) to investigate whether
principles of predictive coding apply to the information processing in neurons. This is
discussed in more detail in [1].
7.2. Conclusion
We here argued that the understanding of neural information processing will profit
from taking a neural perspective, focusing on the information entering and exiting a
neuron, and stripping away semantics imposed by the experimenter – semantics that
is not available to a neuron. We suggest that the necessary analyses are best carried
out in an information theoretic framework, and that this framework must be able to
describe the processing in a multiple input system to accommodate neural information
processing. We find that PID provides the necessary measures, and allows to compare
most if not all theoretically conceivable neural goal functions in a common framework.

20

Moreover, PID can also be used to design new goal functions from first principles. We
demonstrated the use of this technique in understanding neural goal functions proposed for
the integration of contextual information (coherent infomax), the learning of predictions
(predictive coding), and introduced a novel one for the decoding of input based on prior
knowledge called coding with synergy (CWS).
Acknowledgements
The authors would like to thank Nils Bertschinger for inspiring discussions on partial
information decomposition and for reading an earlier version of the manuscript. MW
received support from LOEWE Grant ”Neuronale Koordination Forschungsschwerpunkt
Frankfurt (NeFF)”. VP received financial support from the German Ministry for Education and Research (BMBF) via the Bernstein Center for Computational Neuroscience
(BCCN) Göttingen under Grant No. 01GQ1005B.
References
[1] M. Wibral, J. T. Lizier, V. Priesemann, Bits from Brains for Biologically-Inspired
Computing, Computational Intelligence 2 (2015) 5, 00000. doi:10.3389/frobt.
2015.00005.
URL http://journal.frontiersin.org/article/10.3389/frobt.2015.00005/
abstract
[2] J. Hohwy, The Predictive Mind, Oxford University Press, 2013.
[3] A. Clark, Whatever next? Predictive brains, situated agents, and the future of
cognitive science, Behavioral and Brain Sciences 36 (03) (2013) 181–204. doi:10.
1017/S0140525X12000477.
URL http://journals.cambridge.org/article_S0140525X12000477
[4] T. S. Lee, D. Mumford, Hierarchical Bayesian inference in the visual cortex., Journal
of the Optical Society of America. A, Optics, image science, and vision 20 (7) (2003)
1434–1448.
URL
http://view.ncbi.nlm.nih.gov/pubmed/12868647;http://www.
bibsonomy.org/bibtex/2136bababe707c0ef6f612fdedaeaacfa/meduz
[5] R. P. Rao, D. H. Ballard, Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects., Nat Neurosci 2 (1) (1999)
79–87. doi:10.1038/4580.
URL http://dx.doi.org/10.1038/4580
[6] R. Linsker, Self-organisation in a perceptual network, IEEE Computer (1988) 105–
117.
[7] A. J. Bell, T. J. Sejnowski, The ‘independent components’ of natural scenes are
edge filters, Vision Research 37 (23) (1997) 3327–38.
URL http://www.bibsonomy.org/bibtex/20dabc7935b10ef7fa0df72a1ec2f4020/
meduz

21

[8] T. Tanaka, T. Kaneko, T. Aoyagi, Recurrent Infomax Generates Cell Assemblies,
Neuronal Avalanches, and Simple Cell-Like Selectivity., Neural Computation 21 (4)
(2009) 1038–1067.
URL http://dblp.uni-trier.de/db/journals/neco/neco21.html#TanakaKA09;
http://dx.doi.org/10.1162/neco.2008.03-08-727;http://www.bibsonomy.
org/bibtex/266091b497b7737276a8d8f2d85327554/dblp
[9] W. Phillips, J. Kay, D. Smyth, The discovery of structure by multi-stream networks
of local processors with contextual guidance., Network: Computation in Neural
Systems 6 (1995) 225–246.
URL http://www.bibsonomy.org/bibtex/28911c0fa10104682d5ef293908bace70/
brian.mingus
[10] M. Larkum, A cellular mechanism for cortical associations: an organizing principle
for the cerebral cortex., Trends Neurosci. 36 (3) (2013) 141–51. doi:10.1016/j.
tins.2012.11.006.
[11] L. von Melchner, S. L. Pallas, M. Sur, Visual behaviour mediated by retinal
projections directed to the auditory pathway, Nature 404 (2000) 871–876.
URL http://www.bibsonomy.org/bibtex/2aae98ae21e3a4f2ecd83255dec13fdb4/
brian.mingus
[12] Schreiber, Measuring information transfer, Phys Rev Lett 85 (2) (2000) 461–464.
[13] J. T. Lizier, M. Prokopenko, A. Y. Zomaya, Local information transfer as a spatiotemporal filter for complex systems., Phys Rev E 77 (2 Pt 2) (2008) 026110.
[14] J. T. Lizier, M. Prokopenko, A. Y. Zomaya, Local measures of information storage
in complex distributed computation, Information Sciences 208 (2012) 39–54.
[15] J. T. Lizier, B. Flecker, P. L. Williams, Towards a synergy-based approach to measuring information modification, in: Artificial Life (ALIFE), 2013 IEEE Symposium
on, IEEE, 2013, pp. 43–51.
[16] E. T. Jaynes, Probability Theory: The Logic of Science, Cambridge University Press,
2003.
[17] P. L. Williams, R. D. Beer, Nonnegative decomposition of multivariate information,
arXiv preprint arXiv:1004.2515.
[18] M. Harder, C. Salge, D. Polani, Bivariate measure of redundant information., Phys
Rev E Stat Nonlin Soft Matter Phys 87 (1) (2013) 012130.
[19] N. Bertschinger, J. Rauh, E. Olbrich, J. Jost, N. Ay, Quantifying Unique Information,
Entropy 16 (4) (2014) 2161–2183, 00002.
URL http://www.mdpi.com/1099-4300/16/4/2161
[20] V. Griffith, C. Koch, Quantifying Synergistic Mutual Information, in: M. Prokopenko
(Ed.), Guided Self-Organization: Inception, Vol. 9 of Emergence, Complexity and
Computation, Springer, Berlin/Heidelberg, 2014, pp. 159–190.

22

[21] H. Cuntz, F. Forstner, A. Borst, M. Häusser, One Rule to Grow Them All:
A General Theory of Neuronal Branching and Its Practical Application., PLoS
Computational Biology 6 (8).
URL
http://dblp.uni-trier.de/db/journals/ploscb/ploscb6.html#
CuntzFBH10;http://dx.doi.org/10.1371/journal.pcbi.1000877;http:
//www.bibsonomy.org/bibtex/2c90df6ccace51669cace8cac2cff2204/dblp
[22] J. Kay, Neural Networks for Unsupervised Learning Based on Information Theory,
in: J. W. Kay, D. M. Titterington (Eds.), Statistics and Neural Networks, Oxford
University Press, Inc., New York, NY, USA, 1999, Ch. Neural Networks for Unsupervised Learning Based on Information Theory, pp. 25–63.
URL http://dl.acm.org/citation.cfm?id=348227.348246
[23] J. W. Kay, W. A. Phillips, Coherent Infomax as a computational goal for neural
systems., Bull Math Biol 73 (2) (2011) 344–372. doi:10.1007/s11538-010-9564-x.
URL http://dx.doi.org/10.1007/s11538-010-9564-x
[24] J. Rauh, N. Bertschinger, E. Olbrich, J. Jost, Reconsidering unique information:
Towards a multivariate information decomposition, arXiv:1404.3146 [cs, math]00001
arXiv: 1404.3146.
URL http://arxiv.org/abs/1404.3146
[25] T. M. Cover, J. A. Thomas, Elements of information theory, Wiley-Interscience, New
York, NY, USA, 1991.
[26] J. Kay, D. Floreano, W. A. Phillips, Contextually guided unsupervised learning
using local multivariate binary processors, Neural Networks 11 (1) (1998) 117–140.
doi:10.1016/S0893-6080(97)00110-X.
URL
http://www.sciencedirect.com/science/article/pii/
S089360809700110X
[27] W. A. Phillips, A. Clark, S. M. Silverstein, On the functions, mechanisms, and
malfunctions of intracortical contextual modulation, Neuroscience and Biobehavioral
Reviews 52 (2015) 1–20. doi:10.1016/j.neubiorev.2015.02.010.
[28] R. Wyss, P. König, P. F. M. J. Verschure, A model of the ventral visual system
based on temporal stability and local memory., PLoS Biol 4 (5) (2006) e120. doi:
10.1371/journal.pbio.0040120.
URL http://dx.doi.org/10.1371/journal.pbio.0040120
[29] W. B. Cannon, The Wisdom of the Body, Norton, New York, 1932.
[30] R. Der, U. Steinmetz, F. Pasemann, Homeokinesis - A new principle to back up
evolution with learning, in: Computational Intelligence for Modelling, Control, and
Automation, Vol. 55 of Concurrent Systems Engineering Series, IOS Press, Amsterdam, 1999, pp. 43–47.
[31] K. Friston, J. Kilner, L. Harrison, A free energy principle for the brain., J Physiol
Paris 100 (1-3) (2006) 70–87.
URL http://dx.doi.org/10.1016/j.jphysparis.2006.10.001
23

[32] K. J. Friston, K. E. Stephan, Free-energy and the brain., Synthese 159 (3) (2007)
417–458.
URL http://dx.doi.org/10.1007/s11229-007-9237-y
[33] K. Friston, The free-energy principle: a rough guide to the brain?, Trends Cogn Sci
13 (7) (2009) 293–301.
URL http://dx.doi.org/10.1016/j.tics.2009.04.005
[34] H. B. Barlow, Possible Principles Underlying the Transformations of Sensory Messages, in: W. A. Rosenblith (Ed.), Sensory Communication, MIT Press, 1961.
[35] P. L. Williams, R. D. Beer, Generalized measures of information transfer, arXiv
preprint arXiv:1102.1507.
[36] W. A. Phillips, B. J. Craven, Interactions between coincident and orthogonal cues
to texture boundaries, Perception & Psychophysics 62 (5) (2000) 1019–1038.
[37] A. B. Barrett, An exploration of synergistic and redundant information sharing in
static and dynamical Gaussian systems, arXiv:1411.2832 (2014). arXiv:1411.2832.
URL http://arxiv.org/abs/1411.2832
[38] E. Olbrich, N. Bertschinger, J. Rauh, Information Decomposition and Synergy, Entropy 17 (5) (2015) 3501–3517. doi:10.3390/e17053501.
URL http://www.mdpi.com/1099-4300/17/5/3501
Appendix A. Notation
Appendix A.1. Probability distributions
We write probability distributions of random variables X1 , X2 , Y as P (X1 , X2 , Y )
wherever we’re talking about the distribution as an object itself, i.e. when we treat a
distribution P (X1 , X2 , Y ) as a point of in the space of all joint probability distributions
of these three variables. To signify a value that such a distribution takes for specific
realizations x1 , x2 , y of these variables, we either write P (X1 = x1 , X2 = x2 , Y = y), or
use the shorthand p(x1 , x2 , y).
Appendix A.2. Notation of PID terms
To highlight the necessity of the notation used here and to deepen the understanding
of the various partial information terms we give the following example where we add
explicit set notation for clarity:
Ishd (Y : A; B; C; D) 6=

(A.1)

Ishd (Y : A, B, C, D) =

(A.2)

Ishd (Y : {A, B, C, D}) =
Ishd (Y : {A, B, C, D}; {A, B, C, D}) =
I(Y : A, B, C, D),

24

Ishd (Y : A; B; C; D) 6=

(A.3)

Ishd (Y : A, B; C, D) =

(A.4)

Ishd (Y : {A, B}; {C, D}) .
Here, the first expression (A.1) asks for the information that all four right hand side
variables share about Y , while the second expression (A.2) asks for the information that
the set {A, B, C, D} shares (with itself) about Y . By the self-redundancy axiom 18 [17]
this is just the mutual information between the set {A, B, C, D} and Y . In the next
example in equations A.3 and A.4 we ask in equation A.4 for the information shared
between the two sets of variables {A, B} and {C, D}, meaning that the information about
Y can be obtained from either A, or B, or from them considered jointly, but must also
be found in either C or D or in the two of them considered jointly. This means in the
latter case information held jointly by A and B about Y is considered if it is shared with
information about Y obtained from any combination of C, D, including their synergistic
information.
Appendix B. Partial Information Decomposition
Appendix B.1. Partial information decomposition based on unique information
We here present a definition of unique information given by Bertschinger et al. [19],
which is equivalent to that provided by Griffith and Koch [20]. We assume (that neural
signals can be described by) discrete random variables X1 , X2 , Y with (finite) alphabets
AX1 = {x11 , . . . , x1M }, AX2 = {x21 , . . . , x2N }, AY = {y1 , . . . , yL }, described by their
joint probability distribution P (X1 , X2 , Y ) = {p(x11 , x21 , y1 ), . . . , p(x1M , x2N , yL )}.
As already mentioned above, a definition of either unique, or shared, or synergistic
information that X1 , X2 and {X1 , X2 } have about a variable Y is enough to have a well
defined PID. Among these possibilities, Bertschinger and colleagues opt for a definition of
unique information based on the everyday notion that having unique information about
Y implies that we can exploit this unique information to our favor against others who do
not have this information – at least given a suitable situation. Thus if we are allowed to
construct such a suitable situation to our liking, we may prove to have unique information
for example by winning bets on the outcomes of Y , where the bets are constructed by us
against an opponent who does not have that unique information.
More formally, one can imagine two players Alice and Bob. Alice has access to the
variable X1 from equation 3, while she does neither have access to variable X2 , nor direct
access to variable Y . Bob has access to the variable X2 , but neither direct access to X1 ,
nor to Y . To the extent that the mutual information terms I(Y : X1 ), and I(Y : X2 )
allow, Alice and Bob however, do have some information about the variable Y , despite
not having direct access to Y . If Alice wants to prove that having access to X1 gives
her unique information about Y 19 , then she can suggest to Bob to play a specific game,
18 The self-redundancy axiom states that the shared information is just the mutual information between
input and output when considering the same input twice, i.e. Ishd (Y : X1 ; X1 ) = I(Y : X1 ). This axiom
becomes important in extensions of PID to more than two input variables.
19 Remember that the unique information is part of a decomposition of a mutual information, I(Y :
X1 , X2 ), so we’re looking at information about Y . We do not care how much information X1 has about
X2 , and vice versa.

25

designed by her, where the payout depends only on the outcomes of Y . In such a game,
her reward will depend only on the probability distribution p(x1 , y) = p(x1 |y)p(y), while
Bob’s reward will depend only on p(x2 , y) = p(x2 |y)p(y). The winner is thus determined
simply by the two distributions p(x1 , y) and p(x2 , y), but not by the details of the full
distribution p(x1 , x2 , y). Practically speaking, Alice should therefore construct the game
in such a way that her payout is high for outcomes y about which she can be relatively
certain, knowing x1 .
From this argument, it follows that Alice could not only prove to have unique information in the case described by the full joint distribution P = P (X1 , X2 , Y ), but also for
all other cases described by distributions Q = Q(X1 , X2 , Y ) that have the same pairwise
marginal distributions, i.e. p(x1 , y) = q(x1 , y) ∧ p(x2 , y) = q(x2 , y) ∀x1 , x2 , y ∈ AX1 ,X2 ,Y .
Based on this observation it makes sense to request that Iunq (Y : X1 \ X2 ) and Iunq (Y :
X2 \ X1 ) stay constant on a set ∆P of probability distributions that is defined by:
∆P = {Q ∈ ∆ : Q(X1 = x1 , Y = y) = P (X1 = x1 , Y = y)

(B.1)

andQ(X2 = x2 , Y = y) = P (X2 = x2 , Y = y)}
where ∆ is the set of all joint probability distributions of X1 , Y , X2 .
From this, it follows from equation 4 that also the shared information Ishd (Y : X1 ; X2 )
must be constant on ∆P (consult Figure B.5, and take into account that the mutual
information terms I(Y : X1 ) and I(Y : X2 ) are also constant on ∆P ). Hence, the
only thing that may vary when exchanging the distribution P, for which we want to
determine the unique information terms,for another distribution Q ∈ ∆P is the synergistic
information Isyn (Y : X1 ; X2 ). It therefore makes sense to look for a specific distribution
Q0 ∈ ∆P where the unique information terms coincide with something computable from
classic information theory. From Figure 2 we see that for the case of a distribution
Q0 ∈ ∆P where synergistic information vanishes, the unique information terms would
coincide with conditional mutual information terms, i.e. Iunq,P (Y : X1 \X2 ) = Iunq,Q0 (Y :
X1 \ X2 ) = IQ0 (Y : X1 |X2 ). It is known, however, that a Q0 with this property does
not necessarily exist for all definitions of unique, shared and synergistic information that
satisfy equations 3-5, and that also satisfy the above game-theoretic property (being able
to prove the possession of unique information). Therefore, Bertschinger and colleagues
suggested to define a measure I˜unq of unique information via the following minimization:
I˜unq (Y : X1 \ X2 ) = min IQ (Y : X1 |X2 )

(B.2)

I˜unq (Y : X2 \ X1 ) = min IQ (Y : X2 |X1 ) .

(B.3)

Q∈∆P

Q∈∆P

From this, measures for shared and synergistic information can be immediately obtained via equations 4, 3 as:
I˜shd (Y : X1 ; X2 ) = max (I(Y : X1 ) − I(Y : X1 |X2 ))
Q∈∆P

(B.4)

= max CoIQ (Y ; X1 ; X2 ) ,
Q∈∆P

I˜syn (Y : X1 ; X2 ) = I(Y : (X1 , X2 )) − min IQ (Y : (X1 , X2 )) .
Q∈∆P

26

(B.5)

A
(Y
I syn

)
;X 2
: X1

Iunq(Y : X1\X 2)

Ishd(Y : X1;X 2)
Iunq(Y : X1\X 2)
I(Y : X 1)

B

I(Y : X 1; X 2)

I(Y : X 2)

The aim is to quantify Iunq, Ishd, and Isyn.

B1

B2

B3

B4

B5

B6

I(Y : X1) is known from information
theory. It is constant on ∆P, i.e.
independent of the choice of Q.

Iunq(Y : X1 \ X2) is unkown in classical information theory, but constant
on ∆P by assumption from game
theory.
With the aim to estimate
Iunq(Y : X1 \ X2), one defines a set of
IQ(Y : {X1, X2}`) on ∆P.
IQ depends on the choice of Q (see
main text).

IQ(Y : X1 | X2) is known from information theory, and depends on the
choice of Q.

Likewise, Isyn,Q(Y : X1; X2) depends
on the choice of Q.

By minimizing IQ(Y : X1 | X2),
Isyn,Q(Y : X1; X2) is also minimized,
~
and therefore only Iunq remains:
~
Iunq(Y : X1 \ X2) = min IQ(Y : X1 | X2).
QЄ∆

B7

B8

~
With knowing Iunq(Y : X1 \ X2),
~
Ishd(Y : X1; X2) is calculated with
I(Y : X1).

~
Last, Isyn(Y : X1 ; X2) is caluclated
from the known quantities
~
I(Y : X1 ; X2), Iunq(Y : X1 \ X2),
~
~
Iunq(Y : X2 \ X1) and Ishd(Y : X1; X2).

Figure B.5: Graphical depiction of the principle behind the definition of unique information in [19]. For
details also see the main text. (A) Reminder of the partial information diagram. (B) Explanation how
unique information can be defined using minimization of conditional mutual information on the space of
probability distributions ∆P (see text). Note that if the synergy in (B6) can not be reduced to 0, then
we simply define the unique information measure as I˜unq (Y : X1 \ X2 ) = min I(Y : X1 |X2 ).
Q∈∆P

27

Note that CoI refers to the co-information CoI(Y ; X1 ; X2 ) = I(Y : X1 ) − I(Y : X1 |X2 )
(see [19] for details). For this particular choice of measures it can be shown that there is
always at least one distribution Q0 ∈ ∆P for which the synergy vanishes, as was desired
above. As knowledge of the pairwise marginal distributions P (X1 , Y ), P (X2 , Y ) only
specifies the problem up to any Q ∈ ∆P , and as the synergy varies on ∆P , we need to
know the joint distribution P (X1 , X2 , Y ) to know about the synergy. This is indeed an
intuitively plausible property and supports the functionality of the definitions given by
Bertschinger and colleagues [19].
From Figure 2 and the definition of I˜unq , I˜shd , and I˜syn in equations B.2-B.5 it seems
obvious that the following bounds hold for these measures:
I˜unq (Y : X1 \ X2 ) ≥ Iunq (Y : X1 \ X2 ),
I˜unq (Y : X2 \ X1 ) ≥ Iunq (Y : X2 \ X1 ),

(B.6)

I˜shd (Y : X1 ; X2 ) ≤ Ishd (Y : X1 ; X2 ),
I˜syn (Y : X1 ; X2 ) ≤ Isyn (Y : X1 ; X2 ),

(B.8)

(B.7)

(B.9)

and this can indeed be proven, given that Iunq , Ishd , and Isyn is taken to mean any other
definition of PID that satisfies equations 3-5 [19] and the above game theoretic assumption
of a constant Iunq on ∆P .
The measures I˜unq , I˜shd , and I˜syn require finding minima and maxima of conditional
mutual information terms on ∆P . Fortunately, these constrained optimization problems
are convex for two inputs as shown in [19], meaning that there is only one local minimum (maximum) which is the desired global minimum (maximum). Incorporating the
constraints imposed by ∆P into the optimization maybe non-trivial, however.
Appendix B.2. PID by example: Of casinos and spies
A short example may demonstrate the above reasoning: Let Alice and Bob bet on the
outcomes Y of a (perfect, etc.) Roulette table at a Casino in a faraway city, such that
they do not have immediate access to these outcomes; they will only get a list of these
outcomes when the Casino closes, but will have to place their bets before that. Alice has
a spy X1 at the Casino who informs here directly after an outcome was obtained there,
but only tells the truth when the outcome was even (this includes 0). Otherwise he tells
her a random possible outcome from a uniform distribution across natural numbers from
0 and 36 (just like the Roulette). Bob also has a spy X2 at the casino, but in contrast to
Alice’s spy he only tells Bob the truth for uneven outcomes and for 0, otherwise he lies
in the same way as the one of Alice, picking a random number. Neither Alice nor Bob
knows about the spy of the other 20 . While this situation looks quite symmetric at first
glance, both can prove to each other to have unique information about the outcomes at
the casino, y. To see this, remember that Alice may suggest a game constructed by herself
when trying to prove the possession of unique information. Thus, Alice could suggest to
20 This is actually irrelevant, since the game is about Y only. The statement is intended for readers
with a game theoretic background and should clarify that this is a trivial game, where knowledge about
the opponent doesn’t influence Alice’s or Bob’s strategy.

28

double the stakes for bets on even numbers21 . At the end of the day, both Alice and Bob
will have won a roughly equal amount of bets, but the bets Alice will typically have won
payed out more, and Alice wins. In the same way, Bob could suggest to double the stakes
for uneven outcomes if it were his turn to prove the possession of unique information.
Thus, both have the same amount of information about the outcomes at the casino, but
a part of that information is about different outcomes.
In this example, there is also redundancy as both will have the same information
about the outcome Y = 0.
It is left for the reader to verify that Alice and Bob will gain some information (i.e.
synergy) by combining what their spies tell them, but that this is not enough to be certain
about the the outcome of the Roulette, i.e. I(Y : X1 , X2 ) < H(Y ) 22 .
Appendix B.3. Estimating Synergy and PID for jointly Gaussian variables
While synergy, shared and unique information are already difficult to estimate for
discrete variables, it is not immediately clear how to extend the definitions to continuous
variables in general. Barrett has made significant advances in this direction though by
considering PID for jointly Gaussian variables [37]. Approaches to Gaussian variables
are important analytically because the classical information theoretic terms there may be
computed directly from the covariance matrix of Y , X1 , X2 , and are important empirically
due to the wide use of Gaussian models to simplify analysis (e.g. in neuroscience).
First, Barrett was able to demonstrate the existence of cases of non-zero quantities
for each of synergy and shared information for such variables. This was done without
reference to any specific formulation of PID measures by examining the ‘net synergy’
(synergy minus shared information), i.e. I(Y : X1 , X2 ) − I(Y : X1 ) − I(Y : X2 ), which
provides a sufficient condition for synergy where it is positive and for shared information
where it is negative. This was an important result, since the intuition of many authors was
that the linear relationship between such Gaussian variables could not support synergy.
Next, Barrett demonstrated a unique form for the PID for jointly Gaussian variables
which satisfies the original axioms of Williams and Beer [17] as well as having unique
and shared information terms depending only on the marginal distributions (X1 , Y ) and
(X2 , Y ) (as argued by Bertschinger et al. [19] above, and consistent with [18, 20]). To
be specific, this unique form holds only for a univariate output (though multivariate
inputs are allowed). This formulation maps the shared information to the minimum of
the marginal mutual information terms I(Y : X1 ) and I(Y : X2 ) – hence is labeled
the Minimum Mutual Information (MMI) PID – and the other PID terms follow from
equations 3-5. Interestingly, this formulation always attributes zero unique information
to the input providing less information about the output. Furthermore, synergy follows
directly as the additional information provided by this “weaker” input after considering
21 In roughly 50% of the cases the outcome of the Roulette, y, will be even, and in these cases Alice
will be told the truth. In the other 50% of the cases, the outcome will be odd, and the spy will report a
random number. Of these roughly 50% will be even, roughly 50% will be odd. Thus Alice will receive on
average roughly 75% even and 25% odd numbers. Of the even numbers 2/3 will be correct. Of the odd
numbers only 1/18 will be correct – by chance. For Bob the situation is reversed. Forcing higher stakes
for even outcomes will, therefore, be an advantage for Alice.
22 Hint: Think about what they can conclude if the parities of their outcomes match, and what if they
don’t match.

29

the “stronger” input. Some additional insights into this behaviour have recently been
provided by Rauh and colleagues in [38]
Appendix C. Learning rules for maximizing F and for learning the coherent
infomax goal function FCIP
We here briefly present the learning rules for gradient ascent learning of neural processor learning to maximize the goal function F from equation 11. We only consider the
basic case of a single a neural processor with binary output Y here [26, 22]. The inputs to
this processor are partitioned into two groups {X1i }, representing the driving inputs and
{X2j }, representing the contextual inputs. These inputs enter the information theoretic
goal function F (X1 , X2 , Y ) via their weighted sums per group as:
X1 =

m
X

wi X1i − w0 = wT X1 − w0

i=1
n
X

X2 =

vj X2j − v0 = vT X2 − v0 .

(C.1)
(C.2)

j=1

The inputs affect the output probability of the processor via an activation function
A(x1 , x2 ) as:
Θ ≡ p(Y = 1|X1 = x1 , X2 = x2 ) =

1
.
1 + exp(−A(x1 , x2 ))

(C.3)

For the sake of deriving general learning rules, A may be any general, differentiable nonlinear function of the input. Note that Θ fully determines the information theoretic
operation that the processor performs. Θ is a function of the weights used in the summation of the inputs. Thus, learning a specific information processing goal can only be
done via learning these weights – assuming that the input distributions of the processor
can not be changed. Learning rules for these weights will now be presented.
To write the learning rules in concise form, the additional definitions:
E = hΘix1 ,x2

(C.4)

Ex2 = hΘix1 |x2

(C.5)

Ex1 = hΘix2 |x1

(C.6)

are introduced to abbreviate the expectation of the activation across all input vectors
x1 = [x11 . . . x1m ], x2 = [x21 . . . x2n ]. These expectations are functions of the input
distributions as well as of the weights and have to be recomputed after weight changes.
Using online learning therefore necessitates computing these expectations over a suitable
time window of past inputs. To write the learning rules in concise notation a non-linear
floating average Ō of the above expectations is introduced as:

Ō = Φ0 log

Ex1
Ex2
E
− (Φ0 − Φ2 ) log
− (Φ0 − Φ1 ) log
.
1−E
1 − Ex1
1 − Ex2

(C.7)

Using this notation, the gradients for the updates of weights w = [w1 . . . wm ],v =
30

[v1 . . . vn ], and the bias coefficients w0 , v0 are:

 ∂A
(Φ1 + Φ2 − Φ3 − Φ0 )A − Ō
Θ(1 − Θ)x1
∂x1
x ,x

 1 2
 ∂A
∂F
= (Φ1 + Φ2 − Φ3 − Φ0 )A − Ō
Θ(1 − Θ)x2
∂v
∂x2
x ,x

 1 2
 ∂A
∂F
= (Φ1 + Φ2 − Φ3 − Φ0 )A − Ō
Θ(1 − Θ)(−1)
∂w0
∂x2
x ,x

 1 2
 ∂A
∂F
= (Φ1 + Φ2 − Φ3 − Φ0 )A − Ō
Θ(1 − Θ)(−1)
∂v0
∂x2
x1 ,x2
∂F
=
∂w



(C.8)
(C.9)
(C.10)
(C.11)

Last, we note that for the specific implementations of CIP, the activation function was
chosen as:
A(x1 , x2 ) = x1 [k1 + (1 − k1 ) exp(k2 x1 x2 )] ,
(C.12)
with 0 ≤ k1 < 1 and k2 > 0, and with x1 , x2 being realizations of X1 , X2 from equations
C.1, C.2. This specific activation function [22, 9] guarantees that:
• Zero output activation can only be obtained if the summed driving input X1 is zero.
• For zero summed contextual input X2 , the output equals the summed driving input.
• A summed contextual input of the same sign as the summed driving input leads to
an amplification of the output. The reverse holds for unequal signs.
• The sign of the output is equal to the sign of the summed driving input.
These four properties were seen as essential for an activation function that supports
coherent infomax.

31

