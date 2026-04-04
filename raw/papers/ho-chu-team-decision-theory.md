---
source: Ho, Y.C., Chu, K.C. (1972). Team Decision Theory and Information Structures in Optimal Control Problems — Part I. IEEE Transactions on Automatic Control, 17(1), 15-22.
author: Yu-Chi Ho, K.C. Chu
date: 1972-01-01
type: paper
quality: primary
stance: neutral
---


15

IEEE TRANSACTIONS ON AUTObTATIC CONTROL, VOL. AC-17,.NO. 1, FEBRUARY 1972

action a t each layer. These parameters axe chosen such
that a favorable tradeoff betweenoperating costs and
performa.nce level achieved is obtained. An approximate
tradeoff measure is developed to ease the computational
burden required to carry out the tradeoff
analysis.
The investigations reported in the preceding
sections
represent an initial step in the formal treatment of this
multilayer strategy and its
associated tra.deoff problem.
There is, therefore, a considerable need for further research
in this area.

John F. Donoghue (SJ60-M’7O) was born in
New York, N. Y., on February 6, 1940. H e
received the B.S. and 31,s.degrees in electrical engineering from Northeastern University,
Boston, Mass., in 1963 and 1965, respecin control
tively, andthe
Ph.D.
degree
engineering from Case Western Reserve
Universit.y, Cleveland, Ohio, in 1970.
He is cnrrentlywiththeIndustrial
Kucleonics Corporation, Columbus, Ohio, and
is engaged in the design of computer control
systems for the basic industries.
Dr. Donoghue is a member of the Operations Research Society
of America, Sigma ,Xi, Tau BetaPi, and Eta Kappa
Nu.

REFERENCES
I. Lefkowitz, “Multilevel approach applied to controlsystem

design,” Trans. ASlME, vol. 88, June 1966.
Ifr. Findeisen and I. Lefkowitz, “Design and applicat,ions of
multilayer control,” in PTOC.
4th ZFAC Congr., Warsan-, Poland,
1969.
J. F. Donoghue, “Economic tradeoffs formultilayer cont,rol
systems,”Ph.D.dissertation,Syst.
Res. Cent,., Case Western
Reserve Univ., Cleveland, Ohio, Oct. 1970.
R. A. Rohrer and M. Sobral, Jr., “Sensit,ivity considerations
inoptimal syst.em design,” IEEE Tram. Automat. Cmtp..,vol.
AC-10, pp. 43-48, Jan. 1965.
G. Hadley and T. M . Whitin, Analysis of Inventory Systems.
Englewood Cliffs, N. J. : Prent.ice-Hall, 1963.

Irving Lefkowitz (h.1’67) received the B.S.
degree in chemical engineering from Cooper
York,
Union School of Engineering,New
N. Y., and the M.S. and Ph.D.degreesin
of
control engineering fromCase1nstitut.e
Technology, Cleveland, Ohio.
He is present,ly Professor of Engineering
a t Case Western Reserve University, Cleveland, Ohio, and Director of the research
program in the control of complex syst.ems.

Team Decision Theory and Information
Structures in Optimal Control Problems-Part
Abstract-Information structures of organizations are studied and
applied to problems of dynamic team decisions. For a causal system
it ishown that thereis a partiallyordered precedence relation existing among the decision makers.
The team decision problem with linear information structure and
quadratic payoff function is dealt with. The primitive random variables are assumedto be jointly Gaussian. The optimal solutions for
the teamsin which precedents’ informtionis available for thefollowers are obtained. It isshown that the well-known linear-quadraticGaussian stochastic control problem and static team decision problem arespecial cases of the structure considered.

I. INTRODUCTION
- 4 m PROBLEM
STATEMENT

W

ITHIN a generalorganization
therearemany
members,each cont.roUing M e r e n t action or decision variables at different. t.imes, each having access to
Xanuscript. received April 19, 1971. Paper recommended by P. P.
Varaiya, past chairman of the B E E S-CS LargeSystems, Differential Games Comittee. This work was supported in part by the
Joint Services Electronics Program under Cont,ract N00014-67-A0298-0006 through Harvard University and in part by t.he Guggenheirn Foundation througha grant toY.-C. Ho.
Y.-C. Ho is with t,he Division of Engineering and Applied Physics,
Harvard University, Cambridge, Mass. 02138.
K.-C. Chu was with the Division of Engineering and Applied
Physics, Harvard University, Cambridge, Mass. He is now wit.h
Systems Control, Inc., Palo Alto, Calif. 94306.

I

different information, a.nd each attemptingto
at.t.ain
different goals. A team is an organizat.ion in which t,hcre is
a single goal or payoff common to all themembers. Let us
consider a team composed of i E 1 = {1,2, . , hr ] members. Each member receives cert.ain informat.ion zi and
controls t.he decision variable ui, where thenature of
these variables will be defined presently. ?Ire denote t,he
payoff funct.ion for all the members as

--

J

= J(w

YZ, *

* 1

YN),

.

(1)

where yi is the control ha or decision rule,
Ut

=

r d z J and ~t E rc

(2)

used by the it,h member and ri is t.he class of admissible
control lawsfori. The
t.eam-theoretic optimization problem
can then be informally stated as follows.
Problem I : Find -yi* E T ifor all i such that,J ( n , YZ, . -,
rN)is minimized. If the system or organization evolves
dynamically in t.ime and the decisions of the members
interact with thepayoff as well as the informa.tion received
by the members, then we have an optimal control problem
in which team decision theory and information structure
plays a decisive role. The purpose of this paper is to investi-

16

IEEE TRANS.4CTIONS O N AUTOMATIC CONTROL, FEBRUAEY 1972

1 2 3
gate one such class of problems and to present various
0
0
0
.... N -02 N-10 N0
explicit resubs.
Fig. 1.
Marschak [l] first formulated the team problem more
than 16 years ago. So far, theoret,ic work is mainly 1imit.ed
E x a m p b 1:
to the static teams[2], [3] in which informat.ion x f is only
the function of some random variable4 but is independent
of what other members have done. However, in a dynamic
team, present information is affected by what, has been
done in the past. Therefore, the present estimation
a.nd The precedence diagram for this systemis simply isolated
decision are dependent. on the a.ctions of the other mem- nodes. (See Fig. 1.) Since there isno explicit causal relation
bers in the past; this verydependence is itself affected by between the control and informationof different members,
the past actions which are part of t,he solution to be ob- we call structures such as this, with isolated members in
tained. Because of the difficulties caused by the interactions the precedence diagram, static teams.
among information estimation andcont.ro1variables, there
I n a. st,atic teamt,heinforma.tion of each membermay not
has been no substanlial work done in the dynamic case.
be obt.ained at the same time, nor
need the control actions
executed by each member t.ake place
simult,aneously. As
A . I n f w m t i o n Structures
long
as
there
a.re
no
casual
precedence
relations amongt.he
Let, 4 E R“ denote a ra.ndom vector definedon anundermembers,
the
actual
time
instants
when
the observat,ion
lying probabi1it.y space (R”, 5, P ) , and let it represent all
and
actions
occm
are
not
important,.
the uncert.ainties of t.he external world which are not conExample 2: I n a classical multistage stochastic control
trolled by any of t,he members. We assume that the probproblem,
the dynamic equation is
ability dist.ribution of f is known to all t.he members and
is Gaussian N ( 0 , X ) with X > 0.
The informationzi each memberreceives includes everything available as knowledge to himfor making decisions. and the observation a t each stage is
This consists of what he has remembered, what he has
~t = H x ~ vi,
i = 1, . * -,N ,
(7)
observed, and what other members have communicated
to him, etc. The information zi is assumed to be a known where x i is t.he state, ut the control, and wt and vi the inlinear function in Rqi of 5 and some of the control actions dependent sequences of random variables. The distribuother members have taken, i.e.,
tions of X I , w i , and v i for alli are known to be independent
zero-mean and Gaussian. The system is assumed to be of
zt = H &
Cj Dijuj, V iJ
(3)
perfect W M ~ O T Y in the sense that at time i, the decision
where H i and D,, are matrices of appropriate dimensions maker remembers perfectly what he has known and what
he has done before. Imagine there are N members of a
and are known to a.11 t,he members. We shall be interested
member is
in only real causal systems where what happens in the t.eam t,o control the system and that the ith
responsible
for
ui at the ith&age.
future cannot affect Khat, is observednow. Thus, in (3) we
Since
assume

+

+

ut cannot a.ffect t,he
informat.ion of j . We have in mind here which is clear from the recursive equation (6),the informaessentially a discrete-time dynamicsituationin
which
t.ion for member i is
current actions can affect., a t most., information in the succeeding, but. not the current, stage.
We formalize this in the following definitions.
Definition I : We sa.yj is related to i, j R i , if D i j # 0.
Definition I
:
We say j is a precedent of i,j { i, iff (a,) j R i
linear
or (b) there exists distinct r, s, t, . ., k E 1 such that j R r
and r R s and sRt, . ., kRi.
Graphically, we can represent, the ideaof precedence in a
precedence diagram. Each member of t.he team [decision
maker (DM)] is represented by a node so placed that the
node for j is above t,hat for i if j { i. One then draws a.
directed segment from node j to node i if j R i and t,here
V I , . . .,us),
Y i. (9)
exists no k such that j { k and k { i. A path, consisting of a
connected series of directed segments,exists between j and The random variableszl;a, w,; 01, . vN all together
iif and only if j { i.
represent the wrne thing
as f defined earlier, t.hat
e ,

a ,

E O AND C W : TEAM DECISION THEORY-PART

17

I

I

I
I

N-2
GROUP II

GROUP I

Fig. 3.

Fig. 2.

zf = linear in (E, ul, . . -,ui-l)

The information structure diagram is displayed in Fig. 3.
(lo) Members one, two, and seven are starting decision makers of
the team; members five, six, a.nd eight, are the terminating
decision makers. In thesequel we shall index t.he members
in such a wag t,hatif j is a precedent of i, t,henj < i.

Each decision maker makes a decision at. a single time
for some H i and Dij and
for all i, where none of the matrices
D f jare zero matrices. We note from (9) that 25 is imbedded moment. The information zi is made available for the ith
in zi as components if j < i. We stress this fact bydrawing member just. before he makes hisdecision. I n practice someone may have to make a decision more than once at.differa memory-communication line segment, (dotted line) from
informationavailable on a.11
j to i on the precedence diagram. Intuitively, this suggests ent. times, theneitherthe
that, whatever j knows is either remembered by i (in the these occasions is the same, and then these decisions are
case of one player acting as a. different DIU at different considered as a single one picked from a product set, or
times) or is passed on to i (when we have different.players). else the informa.tion available isnot. the same, and then one
The precedence diagram with itsmemory-communication
line for this example is shown in Fig. 2. Note, since zj includes z + ~ , it is not necessary to havea dotted-line segment
joining nodesj 1 and j - 1.
The precedence diagram with its memory-communication lines will be called the information structure diagram.
It. isagraphicrepresentation
of (3). The information
struct,ure diagram is essential to the analysis of information transmission and causal relations. Any linear dynamic
system of (6) and (7) (time varying or not) can be put in
our normalized form of (3) by a method similar to that of
Example 2. Lineardynamic
processes withoutperfect
memory or with only partial feedback fit
naturally into
our structure. A general exampleof a 1inea.r-Gaussiant,eam
problem is foundin Example 3.
Example 3:

+

can assume sepa.rate members for each occasion.
We define the class of admissible control Ian-s for the ith
DM, T i , as the set of all Borel-measurable functions y i :
p i --t RLi
. Note that forfixed y i E rr,i = 1, . . *, N , (3) induces for each i a sub-u-algebra Z i c 5, and zi are welldefined random variables measurable with
respect to &.
Let ui take value in U i= Rki,then we have a u-algebra F1
on U t such that. y i - l ( S f ) = Zi. Note that with the excep
tion of the st,atic team, Example1, St, Z t V i, are dependent,
on the choice of y = 171, * , yN]. Therein lie the major
difficulties of the solution of dynamic team problems.
Fortunat.ely, for a large
class of such problems withspecial
information st,ructures,this difficulty can be circumvented.

-

C. Payoff Function
The common goal for all members is to minimize the
function
J(y1,

'

a

*

,

-yN) =

E[$]= E [ + U T & U

+UTSf+

UTC],

where Q is symmetric posit.ive definite and ut are given by
(2) and theexpectation is taken with respect to thea priori
5. Mat,rices Q, S and vector c are of appropriat,e dimensions and are known to all the members. As st,ated earlier,
with the particular choice for theclass of admissible control
laws, all u f are well-defined randomvariables andthe

11. NECESSARY
CONDITIONS
FOR OPTIMALITY
Problem 1: This problem is st.at,ed in the so-called “normal form.”‘ From a practical viewpoint, Problem 1 is not
in a suitable
form
for
explicit solution
except
in the case
where the cardina.lity of eachadmissiblecontrol
setis
h i t e and very small. To put it in a more useful form, we
&st consider arelaxedversion of t.he problem.for
P,roblem 2: Find yr* E rSfor all i such that the ith

+

[UrTQr,

d
eu,
E(r,lz*)+ d
-E(wTS,41z,)
aut

a
+ aa ~ ,
E(Y,TIzOCj + C -E(y,T&,y,lzt)]
k#i

= 0

aut

(17)

-

all values of z f and for all i = 1, . *,N where Qu means
row- a n d j t h column-partitioned block of Q, S,, the
j
t
h
row-partit.ioned
block of S, ct, and the ith part,itioned
J(Yl*, * * -,Yr-1 * Y t *, Yt+l *> * .- I YN*)
subvector of c. The last four
part.ia1derivat.ive termsof (17)
5 J ( Y I * , * * Y~-I*,7 2 , Y ~ + I, * -,YN*) (14) depend explicitly on the form of controls of the following
members. This is rather unsatisfactory inasmuchas we are
for all Y~ E ri and for all i.
att.empting
t.o solve for t,hose cont.ro1 laws through the
Optimality relat.ion (14) is certainly a necessary, but. not
considerat.ion
of(17).
Now we see more explicitly the
sufficient, condition for the global solution of Problem 1.
difficulties
connected
with
the solution of dyna.mic tea.m
I n ot,her words, Problem 2 is a noncooperat.ive version of
opt.imizat,ion
problems.
Furthermore,
because of this
Problem 1 in the language of game theory. We call the
causal
dependence
of
yj
on
Yr for j } i, t.he payoff function
solut.ion of Problem 2 member-by-member optimal. Kext.
in Problem3 is not generallyconvex in y f even thoughit is
we rewrite the expectation in(13) as
quadra.t,ic in u with Q > 0, nor are zt generally Gaussian
J = E{$[Yi*(zl), * * *, Yr-i*(zr-1), Yt(zr),
even
though
4: are
given
Gaussian.
as
The
quadraticGaussian
nature
of
J
and
z
is
dependent
on t.he form of the
Yf+l*(zi+l>,* * ’ > YN*(zN), E1 ]
controlaws Yt chosen. Fortunately, for a variety of
= E,, !E[$lzrl] for fixed x * ,
-,Yf-l *,
classes of problems these difficulties can be overcome or
~ r ,
?$+I*, * * , YN*, (15)
contained in one way or another. I n lat.er sections and in
Part
I1 of this paper t.hese solut,ions will be discussed.
where the second expectationis t.aken withrespect to any
given values of zi. However, for f i e d control laws yl*, ,
*
*
111. STATICTEAIIS
Yt-1 , Y~+I , * , YN* and any $xed z t ,
The results of this section are essent,ially t.hose first obm i n - ~ , ( ~ [ ~ l z t ~ ]
+-+min~[$(n*(z1),* ..,
tained
by
Radner
[2]. We shall
derive
them
in terms of our
f

-

--

--

-

Problem 3: We come to the t,hird version of the t,eam
optimization problem, i.e.,
min E [ $ uTQu
ui

+ uTS[+ uTclzf]A min J ,
ui

where
UT =

trl*T(zl),

*, Yr-1 *T (Zt-l),

rrT(z3,

Y*+l*T(z*+l), * 2 YN*T(zN)1
a

for fixed -y,*(z,), j # i, and any zi.
Problem 3 is in the so-called “extensive form” or ‘‘seminormalized form” in the sense that all except one control
variable are given as strategies. A necessary condition for
the optima.lity of Problem 3 can be obt.ained by t,aking
partial derivatives of J i with respect to ur. However, t.he
partial different.iat.ion mustbeconsidered
wit.h care.
T e r m involve ujsuch that j } i must be included since u j
= y j * ( z j ) and zj depends on ui t.hrough the causal relation.
Thus in general, t<he partial differentiation will result in
It is stated in accordance with the usually accepted meaning in
game theory [7] or Bayesian statistical decision t,heory [8].

function of 4: only, i.e., D f j = 0 in (3) and
zi = Hit,

Vi.

(18)

to avoid trivialky, we assume H i is qt X n with n > qr and
t,hat it is of maximal rank.
The necessary condition of (17) immediately simplifies
to
QtiYt(zt)

+C

Qc&’(yj(zj>Izt)

jZi

+ StE(tlzJ + ct = 0,
Y zi a.nd V i, (19)

since all partial derivative terms in(17) are zero. Furthermore, we have thefollowing lemma.
Lemma: The optimal solution of J of (13) is unique in
st.atic teams.
Proof: Consider y i = yt e ai. Since zj is independent
of -yt for all j and i, J is strictlyconvex and quadratic in all
T i . This, together with the dominated convergence theorem,
enables one to interchange expectation and differentiation
[2] and to show ( a 2 J / W ) = Ej&TQti6i)> 0. This shows
that, J is st,rictly convex inc and the conclusion follows.
Consequently, any solution of the necessary conditions

+

HO AND C W : TEAM DECISION THEORY-PAET

19

I

(19) by uniqueness will be t.he global optimal solution. We
try thecontrol l a w of the form
ui = yt(z3 = At%

+ bf,

v i,

(20)

where A t and b, are k f X q,matrix and k,vector, respectively, to be determined. Substituting (20) into (19),
QtdAtzt

GROUP I

GROUP III

Fig. 4.

+ + C QtJ(AfljC; + bjlzt)
bt)

GROUP TI

i#i

+ siE(glzi)+ cf = 0 world C;, whichis not solution or control law dependent.
QsAArzt

+ b J + [-Qd8,+ St]

+C

*E(E[zr)

QtPj+

i#d

ci = 0

We define such structure formally.
Definition 3: An information
structure
(3) is called
purtiuUy nested if j{ i implies Z, c Zr for all i, j,and y E I’.
Example I:

1

-XHtT(H,XHiT)-’ z f = 0 (21)
for all x , and for all i, where we have ut,ilized simple propert.iw of joint.ly Gaussianrandomvariables
to evaluat,e
E(&,) and tohe fact
that H,XHfThas aninverse. Since (21)
must be truefor all zt, we get

bzT,

.

e ,

bNT)

= c’Q-’

(22)

and

Q di

+C
i#i

-’

QtjAjHjXHtT(HZHtT)

= -SfXHtT(HiTXHtT)
-l,

‘d i,

or

QidA,(HjXHtT) = -XfXHiT,

V i.

(23)

i

The c0efficient.s of the elements of A , in the linear simult,aneous equa.tion (23) form a positive-definite matrix
12, p. 870, lemma]; hence the elements of all A , are uniquely
solvable from(23). Thus, we have t,hefollowing theorem.
Th.eorem (Rudner):The cont.ro1 lawof (20) with (22) and
(23) is optimal for t,he static-team optimization problem
with the informat.ion structure (18).

IV. DYNAMIC
TEAMWITH PARTIALLY
NESTED
INFORXATION
STRUCTURE
I n this sect,ion we wish to study a special class of information structure mot,ivated by the following informal
consideration. Suppose, for each DM i and allhis precedent
j , the information variables z j can be generated from x < in
the sense t.hat knowing zi implies knowing z5. A particular
case of such informat.ion st.ructure is t.hat. of Example 2 of
Sect.ion I. I n ot.her words, the memory-communicat.ion
structure is t,he same as the precedence relat.ion in t.he information st.ructure diagram. Such structure hast.he property t.hat t.he action of all t,he precedents is completely
determined once the controllaws are fixed. Thus t.he only
random effects in zi are due to the structure
of t.he external

28 =

HBC;.

Theinformationstructurediagram
of this exampleis
displayed in Fig. 4. It. is clear from t.he diagram and above
informat.ion struct,urethat Khat, the precedentshave
known will always be known by
their followers. For inst.ance, member three’s precedents are one a.nd t.wo; however, z1 and z2 are the first and second components of 23,
respectively.
I n a system wit.h partially nested information pat.tern,
the follower ca.nalways deducet.he action of its precedents.
For example, for a fixed 71,the first member of Example 2
has as his cont,rol
u1 = Yl(Z1).

(24)

Since t.he team ca.n agree in advance on the decision rule
or control law used, the thirdmember can deducethe action
u1 exactly by using (24). Thus, the extra information u1 is
redundant when the value of z1 is already part of the third
member’s information. The term D31u1 is redundant and
hence can be deleted from 23. Lilre\.r-ise,term D32% is also
redunda,nt. and hence
ca.n be deleted from 23, since zz is the
second component) of 23.
Thus, we can formulate 2 3 in an equivalent. way such
that

20

IEEE TRANSACTIONS ON AUTOMATIC

(23
Similarly, all the ZDiluj terms attached toz4, zj, and 27 can
be deleted without. any change in the t.eam performance.
I n general, it. is clear that we have thefollowing theorem.
Theorem 1: I n a dynamic team s7it.h the partially nested
information structure,
2%

HtE

+ Ci{ Dijuj

(26)

i

CONTROL, FEBRUARY 1972

ture (27). Therefore, by Radner's theorem, the optimal cont.rol law exists, is unique and linear in ii.Since i t = zi for
i E Nl1 y i is linear in z i for i E N1 also. By (28) we deduce
that y i is linear also in zi for i E N2. Repeated application
of Theorem 1 and (28) yields the desired result. Q.E.D.
Application I-Linear Quadratic-Gaussian Control Problens: Consider againExample 2 of Section I1 n i t h a
quadratic payoff function

[::

+1

J = E - x ~ + I ~ S N + ~ X -N + ~ (skTHTHxt
2 h.=1
-

+

(30)

is equivalent, to an informat.ion structure in static form
for any fixed set. of control laws

where SN+1 2 0, B > 0.
Afterabsorbingrecursivedynamicrelations
informationfunctions (9) a.nd payofffunction
Proof: We partition the N-members into thefollowing ha.ve
disjoint sets:

pi = [{H,& { i or j

=

ill.

1

~ k ' b ~ k )

(27)

(6) into
(30),we

N1 = {set.of start.ing members}
N z = {set,of members having i a.sprecedent, where i E AT1 }

. .

N j = {set of members having i as precedent., where
i E NjPl

1.

It is clear t.hat.i i = zi = H i [ for a.11i E Nl. Now let
= zi -

&i

DijYj(Zj)

and

iii
= H&,

V i E N 2a n d j E N1.

(28)

J =E

Since Zi 3 Zj, then 2, will bc Zimeasurable. Conversely,
knowing pi IVC can computc
zi = 2i

+

Dijyj(&),
i

'PL i E N z and j E N l .

(29)

[I: + 1+
- uTQu

uTSt

ternlsindependent of u (32)

where ET = (xlT; w l T 1 . . ., uiVT;
vlT, . . ., V , ~ T ) , which is
Gaussian. Also Q > 0, Q and S are matrices dependent on
only the original parameters of the problem.
Since t.he information z i for different members is nested
in their natural sequence, by Theorem 2 the optimal conlinear in zisuch that
trols exist, are unique and

Now, by rccursion we can calculate zi from f i or vice versa
for i E N3, N,,
ctc.
Q.E.D.
Remark 1 : The reduction of (26) to (27) is possible only
when we arc considering pure strategysolution exclusively.
ui* = Aizi
bi,
V i
(33)
I n more general game-theoretic optimization problems with
for some A iand bi.
different. information for each member inateamand
I n control literature t,hesolution (33) permits further
different payoff functions for each of t.he teams, partially
.

.

e

J

+

nested information structure

alone may not be sufficient simplification in thesense tha,t,the measurement hiistory zi

to effect the reduction-since with mixed strategies know- admits a pair of finite-dimensional sufficient statistics .Ti
ing all that others have known is not sufficient. to deduce (linear in g r ) and P in-hich are the mean and covariance,
respectively: of a Kalman-Bucy filter. ui*can be expressed
what they have actually
done.
Remark 8: Note that the validity of Theorem 1 is in- as a linear functionof f i only. Computationally and physidependent. of the nature of the criterion function J . Fur- cally, this isboth meaningful and simplifying [4].However,
our purposehereis to demonstratethe intrinsic natureofthe
thermore, so long as some invertibilityconditionsare
1inea.r functions of E and uj classic linear-quadratic-Gaussian (LQG) control problem.
satisfied, zi need notbe
for j { i; nor does haveto beGaussian. The pr0pert.y We have observed that its information structure is basiof partia.1 nesting only depends on the definition of the cally equivalent to a static one and itpermits a linearsohtion.
various sub-o algebra in Definition 3.
Remark 3: Notethatthis
conclusion concerning the
Theorem 2: I n a dynamic team withpa.rtially nested information structure, the optimal control for each member optimality of the 1inea.r solutionis independent of the
various
correlations between2 1 , zci, u j for all i,j. In fact, the
exists, is unique and linear in zi.
noise sequences need not even be Markov. We only rePi*OOf: As shown by Theorem 1, a team with information structure (26) is equivalent to one xith static struc- quire that they be jointly Ga,ussian distributed.

HO AND CHU: TEAN DECISION THEORY-PhRT

I

21

“1

ut (t

II

I

m
Fig. 7.

Fig. 6.

Fig. 5.

N
Application 2 4 n e - S t e p CmzmunicutionDelay Control
J
=
E
2
~N+lTQX+l~X+I
ZfTQfX*
Systems [B]: Suppose -we have two coupled linear-discrete
i=l
{l
time-dynamic systems controlled by ul(t) and N ( t ) , t = 1,
2, . . ., N , mith the usual Gaussian disturbance and noise
UliTRluli- ~ 4 r ~ R 2 ~ 2 i ) ) .
(37)
setup. yl(t) and yz(t) are the noise observationsfor the
system.Suppose
This problem does not have partially nested information
structure. On the other hand,
since the problem is zero sum
Zl(t) = (y1(7), yz(k)[i = 1, 2, * . -,t; IC = 1, * * ., t - 1)
there is no cooperation feat.ure in the problem. Thus the
z2(t) = {y2(7), y1(IC)]7 = 1, 2, . . ., t ; k = 1,
., t - 1)
Problem 1 version of the problem is equivalent to that of
Problem 2. Now, if one assumes a linear control lawof the
i.e., two controllers share all past informa.tionwith one-step
will be Ga,ussian for
communication delay. The information structure diagram type of (20) for all u z r , then P(zj2/zi1)
all
i,
j
,
and
t.he
partial
derivative
t,erms
in (17) can be exof such a system will have the appearance of Fig. 5. It is
plicitly
evaluated.
The
problem
from
the viewpoint of
by inspection partially nested. Hence, if the criterion is
player
one
is
then
an
LQG
dynamic
optimization
problem
quadmticinthestateand
controlvariables, thenby
with
partially
nested
information
struct,ure.
Consequently,
Theorem 2, the optimal solution is linear. Furthermore, if
there isa t.hird linear system
coupled to thefirst system via ulf* will have a linear structure of the type of (20). Now,
the second system as shown in Fig. 6, then we may con- when this control law for u1 is used again in (17) for ull, -we
get the self-consistent result that u z i is linear. These linear
clude that t,he first system can tolerate a two-step delay
for both players in a
insharing
informationwitht,he
third sgst.em. Since saddlepointcontrolsareoptimal
global
sense
by
the
reason
that
in
a
zero-sum game any
u3(t - 1) does not a.ffect t,he information zl(t), we do not
saddle
point
stra.tegy
still
be
equivalent
and intercha.ngehave to know zg(t - 1) to ma,intain linearity ofthe optimal
a.ble
[9].
The
details
of
this
a.re
best
illust,rated
via a twosolution.
stage
example
where
the
arithmetic
is
not
too
cumbersome.
Application 3-Hierarchical Control System: Suppose a.n
The point, here is that linearity of the opt.imal solution in
information steructwediagram is t,hat, of Fig. 7, which inan
LQG zero-sum multistage game is primarily due to the
formallyrepresentsachain
of commands. Thenunder
absence
of cooperation and, only as a seconda,ry matter,
linear-quadratic-Gaussian assumptions, the optimal soludependent
on the perfect nlemory fea.ture of the players.
tion isagain linear without,
the need for lateralcornmumication.
IT. CONCLUSION
Roughly speaking, the implication of Theorem 2, is that,
In thispaper we have essentia.lly answered the question
i f a DM’S a.ction affects our information, th.en knowing what
(‘when does a general linear-quadra,tic-Ga.ussian probh.e knows will yield linearO p i ? i 7 ? ~ dsolutions.
solut,ions” in the context of
Application &-Tuw-Pe~son Zero-Sum Multistage Ganzes: lem haveoptimalinear
In theusual formula.tion of LQG zero-sum decision games, decentralized multidecision-maker environment. We have
shown the importa.nceof the concept of a partially nested
we have
information struct.ure diagra.m which enables the reducZi+l =
Dluli
D ~ u z ~~ 2 , i = I, * . * 7 N (34) tion of a dynamic problem of a static one.
YZ‘ = H1xi
~ 2 ’
REFERENCES
yf2 = H ~ x Z p i 2 ,
i = 1, . * ., N
(35)
J. Marschak,“Elements for a theory of teams,” Nanagemmf

+ c(
+

+

+

+

+

+

I i]

Zfl

= {?Jj’lj

zi2

= {y&

_< i},

i = 1, .., N ,

(36)

i.e., each player has perfect memory but does not know the
other plagrers’ information.

Sci., V O ~ .1, pp. 127-137, 1955.
R. Radner, “Team decision problems,” Ann. Muth. Statist., vol.
33, no. 3, pp. 857-881, 1962.
- “The evaluat.ion of information in organizations,” in Proc.
ga kerkelq Symp. X ~ k h .Stat.&. and Probab. Berkeley, Calif.:
University of California Press, 1961,pp. 491-530.
C. Striebel, “SufEcient statistics m the opt,imum control of
stochastic systems,” J . N d h . Anal., vol. 12, pp. 576-592, 1965.

IEEE TRANSACTIONS ON AUTOX4TIC CONTROL, VOL. AC-17, NO. 1, FEBRGARY 1972

22

[5] K.-C. Chu and Y.-C. Ho, “On the generalized linear-quadraticGaussia.nproblems,” in Differentiel Games and Related Top&, H.
W. Kuhn and G. P. Szego, Eds.Amsterdam:North-Holland,
1971, pp. 373-388.
161 H. S. ‘A7itsenhausen,“Separation of estimation and control for
discrete time systems,” Proc. IEEE, vol. 59, pp. 1557-1566,
Nov. 1971.
[7] G. Owens, Game Theory. Philadelphia, Pa.: Saunders, 1968.
[8] hi. DeGroot., Optimal Statistical DeczsiunTheory.
New York:
IlcGraw-Hill, 1970,.,
[9] W. Fy. Will.man, Formal solutions for a class of stochastic
pursmt-evasion games, IEEE Trans. A u k m a t . Contr., vol.
AC-14, pp. 504-509, Oct. 1969.

Mathematics. H e is a consult.ant t.o various indust.rial and research
organizations and coinvent.or of four U.S. patents on various aspects
of numerical and digital control systems. He is coaut.hor of the book
AppliedOptimal
Control: Optimization,Estimation
and Control
(Blaisdell, 1969).
Dr. Hois a member of the Army Scientific Advisory Panel, a member of the Editorial Board of the IEEE Press, and Associate Editor
of the Journal of Optimization Theory and Applications. I n 1969 he
was the Chairman of t,he First International Conference on the
Theory and Application of Differential Games. In 1970 he was a
Guggenheim Fellow at Imperial College, London, England, and
Cambridge University, Cambridge, England.

Yu-Chi Ho (SJ54-M’55SM’62) was born in
China on hiarch 1, 1934. He received the B.S.
and M S . degrees in eIect.rica1 engineering
fromthe Massachusetts1nst.itute of Technology, Cambridge, in 1953 and 1955, respec2..
-e~=.
t.ivelv, and
Ph.D.
the
deaee
in auplied
mathematics from Rarvard University,‘Cambridge, Mass., in 1961.
From 1955 to 1958 he worked on numerical
control systems at the Research Laboratory
Division, Bendix CorDoration, Mich. Since
1961 he has been on the faculty of Harvard University, where he is
presently Gordon McKay Professor of Engineering and Applied

K’ai-Ching Chu (S’69-M’71) was born in
Szechuan, China, on November 19, 1944. He
received the B.S. degree in elect.ricalengineeringfrom theNational TaiwanUniversity,
Taipei, Taiwan, China, in 1966, and the M.S.
.~
and Ph.D. degrees in applied mathematics
~.
from Harvard GniverJit.y, Cambridge, Mass.,
in 1968 and 1951, respect.ively.
From 1968 to 1971 he was a Research
Assistant, and Teaching Fellow at Harvard
University. H e has been a consultant to
Bolt, Beranek, and Xewman, Inc., Cambridge, Mass. Since September
1971, he has been aMathemat.ician with SystemsControl,Inc.,
Palo Alto, Calif. His current research interests involve t.he theory
and application of opt,imal control, st.atistica1 decision analysis,
and game theory.

t

Team Decision Theory and Information Structures
in Optimal Control Problems-Part I1

Absfract-General dynamic team decision problems with linear
information structures and quadratic payoff functions are studied.
The primitive randomvariables arejointly Gaussian. No constraints
on the information structures are imposed except causality.
Equivalence relationsin information andin control functions

I. INTRODUCTION

I

X Part I of this paper, Ho and Chu [l]have discussed

the information struct,ures a.
ingeneral organization and
among different systems are developed. These equivalence relationst.heir relation to team decision problems. It. is found that
aid in the solving of many general problems by relating their solu- in a general causal system a part.ially ordered precedence
tions to thoseof the systemswith “perfect memory.” The lattercan relation { canbe defined among all the members. This
be obtained by the method derived in Part I. A condition is found precedence relation then specifies tjhe nature of the soluwhich enables each decision maker to infer the
information available
to his precedents, while at the same time the controls which will tion.
A linear-quadrat,ic-Gaussian (LQG) t.eam problem (Q,
affect the information assessed can be proven optimal. When this
S, c, Hi,
DiiIi, j = 1, . . -,N ) is an opt.imal dccision probcondition fails, upper and lower bounds of the payoff function can
still be obtained systematically, and suboptimal controls can be ob- lem with payoff function
tained.

J = E [ $ ]= E [ $ U T & U
Manuscript. received April 19, 1971. Paper recommended by P. P.
Varaiya, past. Chairman of the IEEES-CS Large Systems, Differential Games Committee. This research was supported by the Joint.
Services Electronics ProgramunderContract
N00014-67-A-02980006 through Harvard Universit.y.
The author was with the Division of Engineering and Applied
Physics, Harvard University, Cambridge, Mass.Heis
now wlt,h
Systems Control, Inc., Palo Alto, Calif. 94306.

+ UTE.$ + uTc]

(1)

where uT = (ulT, ., uAvT)
and uiis the action varia.ble of
team member i; matrices Q , S and vector c are fixed and
of appropriate dimensions, Q is symmetric positive definite; t.he random variable of the externalworld .$ is u priori
Gaussian with dist.ribution N ( 0 , X). The information zf

