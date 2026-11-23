---
title: "In Pursuit of a Proof of the Riemann Hypothesis"
subtitle: "From Schur minors and heat collisions to Gaussian detectors and signed primes"
author: "Alexandre Dumas"
orcid: "0009-0003-1695-0086"
date: "23 November 2026 — critically revised edition"
lang: en-GB
---

# Abstract {.unnumbered #atlas-abstract}

The Riemann hypothesis asks whether every zero of $\Xi(z)=\xi(1/2+iz)$ is real. This critically revised monograph records the available 2026 written research corpus and earlier intellectual precursors without assigning unverified dates to missing drafts. Its finite and local results range from Schur-cocircuit algebra (with a corrected invalid forced-root claim), adjacent Jensen Wronskians and backward-heat collisions to complete-form coercivity, heat/discriminant identities, scalar Pringsheim criteria and source-specific Jensen residue bounds. Its arithmetic results include a coercivity estimate for the complete odd Weil form on a terminal strip, an explicit prime-diagonal coefficient in a signed-correlation problem, and a Gaussian determinant that has opposite-sign eigenvalues for every hypothetical off-line quartet. The same detector reduces the independent arithmetic question to the growth of three ordinary-prime moments. A scalar variant uses recurrent widths. A different approach relates positive and negative parts of a prime sum to the supremum of the real parts of the zeros and leads to an inequality between products of least common multiples.

The opening equation atlas gives derivations, domains and remaining hypotheses. The November synthesis and the fifty-chapter September foundation preserve the complete technical record available in the supplied edition, including negative results, finite certificates and their source keys. The independent routes still require an all-scale estimate or a transfer to the actual xi coefficients. The deduction using the external arithmetic estimate (W) is attributed in the synthesis. No independent proof of RH is claimed in this volume.

**Author.** Alexandre Dumas, independent researcher, Singapore. [ORCID 0009-0003-1695-0086](https://orcid.org/0009-0003-1695-0086).

**Critical-edition warning.** The 9 October exact audit disproved the historical Paper III universal forced-root skeleton in its printed form: at $(n,k,m)=(4,4,4)$ the corrected gate is $-13\,888$, not zero. The underlying fourfold algebraic factor remains exact. Statements about this historical skeleton in the September preservation layer are explicitly superseded by the correction chapter of this edition. The original paper series, Referee papers, velocity studies and Residual Dynamics are *different* numbered families.

**Reading the volume.** Start with the [guide to the principal results](#atlas-map), consult the [principal equation index](#atlas-locator), or go directly to the [historical equation index](#app-equations). Theorems reported from a primary manuscript retain that manuscript's hypotheses. A finite check applies to the specific objects and inputs it checks. A proof using an external arithmetic estimate retains that dependency. Computational assistance was used in manuscript preparation and selected checks. The author takes responsibility for the work.

**Edition and DOI note.** The original Atlas was deposited as DOI [10.5281/zenodo.24454608](https://doi.org/10.5281/zenodo.24454608). This is a corrected **local** critical edition; its PDF must not be represented as a new Zenodo version until actually deposited.

**2020 Mathematics Subject Classification.** Primary 11M26. Secondary 11M06, 30C15, 42A38, 47B65, 65G30.


\part{The equation atlas}

# Where the strongest equations lead {#atlas-map}

Write $\Xi(z)=\xi(1/2+iz)$. The question is whether every zero of this entire function is real. In this programme the same question takes several forms. A Jensen polynomial can lose real roots at a collision. A logarithmic derivative can acquire a pole away from the support of a positive measure. A Gaussian test can turn that pole geometry into an exponentially large signed prime sum. The equations below give each of these statements a precise object on which it can be tested.

| Research family | Result to read first | Scope or outstanding step |
|:---|:---|:---|
| Papers I--V, Schur minors | [Boundary absorption, reciprocal pairs, corrected cocircuit and residuals](#ch-boundary-gate), S3.1--S3.6 and A37--A38 | Finite identities; $n=2$ exception and invalidated Paper III skeleton |
| Papers VI--VIII, Jensen and Airy | [Adjacent shifts, May curvature-2 and October residue protection](#atlas-algebra), A1--A2 and A29--A30, A33--A34 | Source/shift and global coverage remain necessary |
| Paper IX, v150 to v442 | [Bernstein gates, collision degree and boundary counts](#paper-ix-version-by-version-what-actually-survived), S4.2--S4.7 | Finite regions and local index, with the small-time region still open |
| Theta, Hankel and Bezoutian | [Positive measures and the 64-node interpolation result](#atlas-moments), A3--A4 | Distinct normalisations and an explicit finite-data premise |
| Fixed-base moments and RESET | [Hausdorff measures, Christoffel steps and source energy](#atlas-moments), A5 | The next actual moment must be funded at every depth |
| Physical Weil form | [The six gates and terminal-strip theorem](#atlas-physical), A6--A7 | A local lower bound and a cofinal criterion on the full domain |
| Divisors and signed primes | [October correlations and the separate scalar Pringsheim programme](#atlas-primes), A8--A10, A32 | Signed off-diagonal or middle-range prime estimate remains open |
| Finite Weil matrices | [Parity selection and mixed resolvents](#atlas-parity), A11--A12 | Every finite dimension in specified cutoff regimes |
| Pole-neutral Gaussian probes | [Quartet determinant, prime moments and reconstruction](#atlas-gaussian), A13--A18 | The ordinary-prime growth estimate carries the RH difficulty |
| Scalar Gaussian and Möbius routes | [Recurrent widths, prime-power budgets and transfer](#atlas-transfer), A19--A20 | Scalar and matrix criteria use different limiting quantifiers |
| One-sided windows and LCMs | [Growth exponent and integer inequality](#atlas-windows), A21--A23 | The external arithmetic-window estimate has its own provenance |

![Research-route map. The dark nodes are exact or source-reported restricted statements; dotted edges identify the genuinely outstanding global theorem. The diagram is logical, not a claim that the terminal inequality has been proved.](figures/dependency-map.pdf){ width=92% }

**How to read the figure.** The dashed links carry the work: a finite Schur factor is not an all-degree Xi inequality; a protected Jensen residue is not protection at every real root; a local Weil bound is not a complete cofinal bound; and an analytic ramp criterion is not the external estimate (W). These non-implications are essential to the scientific record.

The [additional theorems and short deduction under (W)](#atlas-frontier) give the finite heat-gap barrier, the sharp October symbol, thin-strip pole rigidity, and the exact growth of the LCM ratios on squares. The [principal equation index](#atlas-locator) gives page references. The [historical ranking](#research-importance-an-explicit-non-probabilistic-ranking) records 37 families and revisions. The [mechanism locator](#app-results) and [numbered-equation index](#app-equations) lead into the fifty technical chapters. A number such as (37.5) belongs to that historical sequence. The prefixes A and S refer to this atlas and the November synthesis respectively. In particular, original Paper III treats cocircuits, while *Referee* Paper III treats the physical Weil form.

# Finite factors, real roots and heat collisions {#atlas-algebra}

## Two finite reductions that stand on their own

Original Paper III extracts a fourfold difference from a flagged Schur determinant. For $XY\ne0$ its low part is
$$
 P_{\rm low}(X,Y,Z)=\frac{Z(X-Y)^3(Y-Z)}{XY}
     =X^2Z(1-Y/X)^3(1-Z/Y).
 \tag{A1}\label{eq:A1}
$$
This identifies three differences in one direction and one in the other. Applying a first difference to a finite geometric chain leaves its endpoints. That cancellation explains the divisor in (A1) before the residual sign enters. **Correction:** the 9 October 2026 audit established that the printed identification of this kernel with the full mixed flagged gate was false; at $(n,k,m)=(4,4,4)$ the correctly counted coefficient is $-13\,888$, contradicting the original forced-root skeleton. Equation (A1) is an exact *kernel* identity only. See [A37--A38 and the corrected theorem register](#atlas-corrected-original-paper-iii). Paper I instead completes a boundary sum, Paper II resolves mixed perturbations from reciprocal pairs, and Papers IV and V test the remaining signs with rising factorials and a finite Sturm ladder. Their respective statements appear in S3.1--S3.6.

For $J_{n,d}(z)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}z^j$, set $P=J_{n,d}$, $Q=J_{n+1,d}$ and $R=J_{n,d+1}$. Pascal's rule gives $R=P+zQ$ and termwise differentiation gives $R'=(d+1)Q$. Substitution into $W=P'Q-PQ'$ yields
$$
 W=\frac{d(R')^2-(d+1)RR''}{(d+1)^2}.
 \tag{A2}\label{eq:A2}
$$
This converts an adjacent-shift computation into a differential expression in one known polynomial. The anti-diagonal minor expansion (S3.9) gives a second way to compute the same $W$. The source supplies a finite Gram feasibility problem for its sign. An all-degree argument needs the actual coefficients in the required unshifted family. Griffin, Ono, Rolen and Zagier's fixed-degree eventual hyperbolicity theorem gives a precise comparison of the quantifiers [E9].

## How many roots enter at a heat collision?

For $\partial_\tau H=-\partial_y^2H$, the leading multiplicity-four model is $P_4=e^{-\tau\partial_y^2}y^4=y^4-12\tau y^2+12\tau^2$. At positive time, $y^2=(6\pm2\sqrt6)\tau$. At negative time both values are negative. Thus the distinct real-root count goes from zero to four across the collision. The Paper IX local-degree formula gives $-\lfloor m/2\rfloor=-2$ for the oriented map $(H,-H_y)$ at this event. Under isolated collisions, controlled remainders, zero-free vertical sides and regular horizontal slices, (S4.5) adds these contributions over a rectangle. The top count and side guards are substantive hypotheses.

![The exact fourth-degree heat polynomial. The two line styles distinguish the two values of the coefficient in the positive-time root formula. The point at time zero counts one distinct root of multiplicity four.][plate-heat-collision]


# Actual theta moments and the cost of a new direction {#atlas-moments}

## The all-rank criterion and the finite input

Let $F$ be the normalised even descent of $\xi$ in (2.4), with $F(0)=F'(0)=1$. Its Taylor series defines the quantities
$$
 p_r=(-1)^{r-1}r[w^r]\log F(w),\qquad
 H_n=(p_{i+j+1})_{0\le i,j<n},\qquad
 \frac{F'(w)}{F(w)}=\sum_{j\ge0}(-1)^jp_{j+1}w^j .
 \tag{A3}\label{eq:A3}
$$
The last identity is local at zero. Cofinal positive semidefiniteness gives positivity at each fixed rank by taking principal submatrices. The Hamburger moment theorem then gives a positive measure. The analytic growth bounds in [the single-Hankel chapter](#ch-hankel) confine its support to a compact real interval. The meromorphic logarithmic derivative can consequently have no nonreal pole. Since $F$ is positive on the nonnegative axis, all its zeros must then lie on the negative real axis. This is where all ranks enter the argument.

The November relative-interpolation note uses a different descent, $A(t)=\Xi(2\sqrt t)/\Xi(0)$, and $\widehat H_k=(s_{i+j+2})$ with $s_m=-m[t^m]\log A(t)$. For $\rho=1/2+\delta+i\gamma$, $\gamma>0$, write $\lambda_\rho=4/(\gamma-i\delta)^2$. With $T=3\cdot10^{12}$, summation by parts gives
$$
 \sum_{\gamma>T}\gamma^{-4}
 =-\frac{N(T)}{T^4}+4\int_T^\infty\frac{N(y)}{y^5}\,dy,\qquad
 \sum_{\gamma>T}|\lambda_\rho|^2<9\cdot10^{-37}.
 \tag{A4}\label{eq:A4}
$$
Here $N$ counts positive ordinates with multiplicity. The second bound uses $|\lambda_\rho|^2\le16/\gamma^4$ and the explicit zero-count error in the relative-interpolation note, §2. The sign of the endpoint term improves the bound. Platt and Trudgian supply finite-height zero verification [E5]. The 64-node calculation in §5A also uses particular hundredth-width brackets for 64 selected ordinates. Subject to those brackets and the cited zero-count inputs, the source obtains $\widehat H_{64}\succeq G_{64}/3\succ0$, where $G_{64}$ is the positive reference Gram of those nodes. This version preserves that finite-data qualification.

## Fixed-base Hausdorff moments and RESET

At a fixed base $a=30$, the logarithmic derivative gives the compact transform (34.1). Under RH its moment sequence has atoms at $a^2/(a^2+\gamma^2)$ with positive weights given by (34.2). A converse must construct a Hausdorff representation for this same sequence. In the F-series, endpoint Christoffel transforms and canonical moments track successive depths. At an invertible positive detail block the exact elimination step has the form
$$
 \epsilon_{\rm fine}=\epsilon_{\rm coarse}-r^*S^{-1}r .
 \tag{A5}\label{eq:A5}
$$
The subtracted term measures the energy of the actual new source $r$ in its detail block $S$. The even-section determinant factorisation (37.5) resolves a related inverse-RESET ambiguity into one boundary scalar. [Chapters 33--38](#ch-layercake) give the fixed-base, canonical-wall, Darboux and RESET arguments, including the corrected off-resonance chart. A separate native finite-section calculation at $H=6144$ gives $\|R\mathcal M_HR^*-I\|_\infty\le0.74042452559637051$ in its preconditioned matrix [S6.2]. Extending this estimate to the continuum requires uniform control of the omitted directions.

# The physical Weil form and its six gates {#atlas-physical}

The odd Weil form retains the archimedean term, every active prime power and the boundary pole subtraction in (S5.1). At each aperture $b$ the test $u$ and its norm belong to the physical form domain. There are two complementary theorems to compare. Referee III gives a positive lower bound on a shrinking terminal strip. The spectral detector tests a lower bound on the entire pole-neutral space along an unbounded sequence of apertures:
$$
 \operatorname{supp}u\subset(b-10^{-3}b e^{-b},b),\quad b\ge10
 \quad\Longrightarrow\quad q_{\rm comp,b}[u]\ge\tfrac b2\|u\|^2 .
 \tag{A6}\label{eq:A6}
$$
$$
 \begin{gathered}
 b_j\longrightarrow\infty,\quad \beta_j\ge0,\quad\log(1+\beta_j)=o(b_j),\\
 q_{\rm comp,b_j}[u]\ge-\beta_j\|u\|^2
 \quad\text{for every admissible pole-neutral }u
 \end{gathered}
 \quad\Longrightarrow\quad{\rm RH}.
 \tag{A7}\label{eq:A7}
$$
A hypothetical off-line quartet produces exponentially negative tests for all sufficiently large apertures in the G6 construction. Thus even a subexponential loss on a cofinal sequence would suffice in (A7). The quantifier on $u$ is the distance between the local theorem and the global estimate.

| Gate | September 24 freeze | What the September 26 audit retained or required |
|:---|:---|:---|
| G1. Full form and pole carrier | Internal pass | Retained in scope. Keep all Euler towers, the physical normalisation and the pole carrier. |
| G2. Centred physical placement | Internal pass | Reopened. Place the grouped remainder on the actual analysis range with the requisite norm. |
| G3. Finite-horizon inverse cost | Internal pass | Reopened. Pay the cost in the complete future denominator, including cross terms. |
| G4. Shift discipline | Internal pass | Reopened. Use one consistent shift through each comparison and justify its growth. |
| G5. Continuation | Internal pass | Reopened. Control the actual source after elimination and propagate the bound cofinally. |
| G6. Exponential detection | Internal pass | Retained in scope for the complete pole-neutral odd test space. |

II.1 recorded all six internal passes with the global RH flag false. II.8 and II.9 supplied the later decisions. In particular, the projected first-prime cross on the whole unweighted $L^2$ space has norm $\Theta_a(e^{b/2})$ for fixed old aperture $a$. This rules out the proposed unrestricted small-norm estimate. A bound restricted to the physical source direction and its energy remains a separate question. For a genuinely positive denominator $D\ge dI>0$, the exact comparison is $v^*D^{-1}v\le C\iff\left(\begin{smallmatrix}D&v\\v^*&C\end{smallmatrix}\right)\succeq0$. Already the scalar block with diagonal entries $1,1$ and coupling $t$ has Schur complement $1-t^2$. Both diagonal blocks stay positive as the full form changes sign. See [the source-cost argument](#ch-funding) and [the full-space detector](#ch-detector).

# What survives cancellation over the primes {#atlas-primes}

## An exact divisor filter and the quarter surplus

Let $\mathbf1(n)=1$, let $\varepsilon$ be the identity for Dirichlet convolution, and put $u=\mathbf1-\varepsilon$. The coefficient $\nu=\sum_{j\ge0}(-1)^ju^{*j}/(j+1)$ is defined by a finite sum at every integer. Expanding the convolution logarithm of the Euler product gives, for $n\ge2$,
$$
 \sum_{\substack{d\mid n\\d<n}}\nu(d)=
 \begin{cases}1/m,&n=p^m,\\0,&n\text{ has at least two distinct prime factors}.\end{cases}
 \tag{A8}\label{eq:A8}
$$
For $n=pq$ the three terms are $1,-1/2,-1/2$. For $p^2$ the surviving $1/2$ is squared in the arithmetic energy. Chapter 18 constructs a cutoff containing every required proper divisor on rows coprime to 210. With its specified weights and constrained minimisation, the net surplus $\mathcal S(t)-P_1(t)$ tends to $1/4$ in (18.10). Identifying that arithmetic Gram with the denominator of a physical Weil form would require an additional comparison.

## The October signed-correlation theorem

For the third-kind Chebyshev polynomials $V_0=1$, $V_1=2x-1$, $V_{m+1}=2xV_m-V_{m-1}$, the test $P_m(y)=(y-2)V_m(9y/8-1)$ removes a completion pole in the October chart. Let $W_m$ be the explicit Laguerre stencil in [D3, (5.10)] and let $h_m$ be the reciprocal-zero diagonal of the transformed test. For integers $m\ge1$ that source gives
$$
 U_m=\sum_{p\le506^{m+2}}\frac{\log p}{p^2}W_m(\log p),\qquad
 U_m+h_m=\kappa+r_m,\quad\kappa<0,\quad \sum_{m\ge1}|r_m|^2<\infty .
 \tag{A9}\label{eq:A9}
$$
The correction $-128/6561$ in $\kappa$ comes from prime squares at the endpoint of a moving cutoff. The limiting kernel alone misses it. In the quadratic expansion set $q_m(\ell)=e^{-3\ell/2}W_m(\ell)$. The diagonal has the explicit asymptotic
$$
 \sum_{p\le506^{m+2}}\frac{(\log p)^2}{p}\,q_m(\log p)^2
  =\frac{2768896}{14348907}\left(m+\tfrac12\right)+D_\infty+o(1).
 \tag{A10}\label{eq:A10}
$$
The positive linear coefficient quantifies the cancellation required from *distinct* primes. The October manuscript derives RH criteria including eventual negativity of $U_m$. It proves the decomposition in its own analysis and leaves the required unconditional sign on the actual prime sequence open within the programme. Its second half develops a separate complete-theta and heat-discriminant continuation route. The [October synthesis](#octobers-signed-prime-and-complete-theta-programme) and the 92-page primary manuscript [D3] give the two arguments.

# Parity selection in finite arithmetic Weil matrices {#atlas-parity}

A second November route treats the finite Connes--Consani--Moscovici (CCM) Fourier matrix $W(c,N)$ of [E10]. In the orthonormal parity basis its even block $A$ has dimension $N+1$ and its odd block $B$ dimension $N$. Set $v=(1,\sqrt2,\ldots,\sqrt2)^T$ and let $e_0$ select the constant mode. For $z$ off the even spectrum, the parity note derives a mixed resolvent:
$$
 e_0^T(zI-A)^{-1}v=\frac{\det(zI-B)}{\det(zI-A)}.
 \tag{A11}\label{eq:A11}
$$
The displacement identity for the arithmetic matrix yields an invertible change of basis $S=[v\ J]$ with $S^{-1}v=e_0$, $e_0^TS=e_0^T$. In that basis the lower principal block equals $B$, so Cramer's rule gives (A11). At a simple even eigenvalue with unit eigenvector $u_j$, its residue is $(e_0^Tu_j)(u_j^Tv)$. Unlike a norm square, that product has a sign to prove. Strict interlacing of all levels corresponds to strictly positive mixed residues when the even eigenvalues are simple and no poles cancel.

In the prime-free interval $1<c\le2$, the corrected coefficients have $b_n=n\sum_j\mu_j/(n^2+s_j)$ with $\mu_j>0$ and $s_j>0$. Hence the even/odd comparison contains the Gram
$$
 \frac{b_n+b_m}{n+m}
   =\sum_j\mu_j\,\frac{nm+s_j}{(n^2+s_j)(m^2+s_j)} .
 \tag{A12}\label{eq:A12}
$$
Each summand is the sum of two rank-one positive kernels. For any finite $N$, vanishing of the quadratic form would force a rational function of $s$ with poles among $-1^2,\ldots,-N^2$ to vanish at infinitely many distinct $s_j$. Its residues then force every coordinate to vanish. A two-coordinate even witness and a positive supersolution for the odd block complete the first-gap argument in the 9 November source:
$$
 \epsilon_0(c,N)<\eta_0(c,N)<\epsilon_1(c,N)
 \qquad (1<c\le2,\ N\ge1).
$$
Here $\epsilon_0,\epsilon_1$ are the two lowest even eigenvalues and $\eta_0$ the lowest odd one. For $2\le c\le2\exp(10^{-5})$ the threshold note proves the narrower conclusion $\min(\eta_0,\epsilon_1)-\epsilon_0>10^{-3}$ at every finite $N$. It establishes simplicity and even parity of the ground state and leaves the order of $\eta_0$ and $\epsilon_1$ open above 2. At the separate endpoint $c=3$ the certificate gives $\epsilon_0<\eta_0<\epsilon_1$ and $\eta_0-\epsilon_0>6\cdot10^{-7}$ by ball arithmetic and an analytic tail argument for all finite $N$. The intervening interval and growing-cutoff convergence to $\Xi$ require further analysis. The [atlas source concordance](#atlas-sources) identifies each of these four primary records.

# Two poles, two probes and the zero that dominates {#atlas-gaussian}

The completed explicit formula evaluates the tests at the two pole locations $s=0,1$. In $z=(s-1/2)/i$ these are $z=\pm i/2$. The completed function $\xi$ is entire. The two poles here refer to evaluations in the explicit formula. A *probe* is a test function. At carrier $a>0$ and width parameter $k\ge1$ take
$$
 F_0(z)=(z^2+\tfrac14)\big(e^{-k(z-a)^2}-e^{-k(z+a)^2}\big),
 \qquad F_1(z)=z^2F_0(z).
 \tag{A13}\label{eq:A13}
$$
Both probes are odd, real on the real axis and vanish at the pole locations. If the second probe in (S8.1) is denoted by $F_{\rm old}$, then $F_1=a^2F_0+2aF_{\rm old}$. This real invertible change of basis carries the old quadratic form to the new one by congruence.

For a hypothetical off-line quartet take $z=x+iy$ with $x>0$, $0<|y|<1/2$, and let $m$ be its common multiplicity. Its four points are $\pm z,\pm\bar z$. With $w=(1,z^2)^T$, their joint contribution to the *bilinear* zero sum is
$$
 H_z=4m\operatorname{Re}(F_0(z)^2ww^T),\qquad
 \boxed{\det H_z=-64m^2|F_0(z)|^4 x^2y^2<0.}
 \tag{A14}\label{eq:A14}
$$
Indeed $F_0(z)=(z^2+1/4)e^{-k(z-a)^2}(1-e^{-4kaz})$ is nonzero since $x>0$. Write $A+iD=e^{i\arg F_0(z)}w$. After removing the positive scalar $4m|F_0(z)|^2$, the matrix is $AA^T-DD^T$, whose determinant is $-\det(A,D)^2=-(2xy)^2$. The direction $r=(-A_2,A_1)^T$ gives a negative value at every phase. Its direction can vary with the phase.

![A synthetic quartet with representative z = 1 + i/3. A scalar test crosses zero twice, while the smaller eigenvalue of the normalised two-probe matrix stays negative. The product of the two eigenvalues is exactly −4/9 at every phase.][plate-detector-phase]

## From one quartet to all zeros and the actual primes

With $C(t)=(2\pi)^{-1}\int_{\mathbb R}F_0(u)^2e^{iut}\,du$ and $D_t=-\partial_t^2$, form three ordinary-prime moments:
$$
 b_j(a,k)=\sum_p\frac{\log p}{\sqrt p}(D_t^j C)(\log p),\quad
 j=0,1,2,\qquad M=\begin{pmatrix}b_0&b_1\\b_1&b_2\end{pmatrix}.
 \tag{A15}\label{eq:A15}
$$
The complete zero matrix satisfies $Q=A_{\rm arch}-2M-2M_{\ge2}$. The archimedean part and the proper-prime-power part have uniformly bounded norms on each compact interval of positive carriers as $k\ge1$ varies. For squares this follows by summing the Gaussian envelope using Chebyshev's bound on unit logarithmic intervals. For powers of exponent at least three the weights themselves are summable.

To compare all zeros put $s_z(a)=y^2-(x-a)^2$ and $S(a)=\max_z s_z(a)$, including critical-line pairs ($y=0$) and merging identical $(x,|y|)$. On compact carrier intervals there are only finitely many candidates for the maximum. Differences of scores are affine in $a$. If an off-line quartet exists, choosing $a=x$ for one such quartet gives a positive score. Moving a little avoids the finitely many ties. On a smaller interval a unique positive maximizer $z_*$ has a uniform gap and the interval contains a rational carrier. Polynomial growth in $x$ times Gaussian decay bounds the sum over every other zero, using $N(T+1)-N(T)=O(\log(T+2))$. The large negative eigenvalue forced by (A14) then gives a large positive eigenvalue of $M$. On RH the real-zero sum is positive semidefinite. These two implications give the criterion in the source:
$$
 {\rm RH}\quad\Longleftrightarrow\quad
 \forall a\in\mathbb Q_{>0},\quad
 \liminf_{k\to\infty}\frac{\log(1+[\lambda_{\max}M(a,k)]_+)}{k}=0 .
 \tag{A16}\label{eq:A16}
$$
Here $[t]_+=\max(0,t)$. In the simplifying basis (A15), $2\lambda_{\max}=b_0+b_2+\sqrt{(b_0-b_2)^2+4b_1^2}$. The independent arithmetic problem is to bound this expression for the ordinary primes.

## What the growth curve reconstructs

Away from a tie between maximizers, the source gives the full exponent
$$
 \mathcal L(a)=\lim_{k\to\infty}\frac{\log(1+[\lambda_{\max} M(a,k)]_+)}{k}
              =2[S(a)]_+ .
 \tag{A17}\label{eq:A17}
$$
On an open positive arc with a unique winner, differentiation gives
$$
 \mathcal L''(a)=-4,\qquad
 x_*=a+\tfrac14\mathcal L'(a),\qquad
 |y_*|=\sqrt{\tfrac12\mathcal L(a)+\tfrac1{16}\mathcal L'(a)^2}.
 \tag{A18}\label{eq:A18}
$$
These formulas recover the ordinate and the absolute horizontal displacement of an *exposed* quartet. A quartet whose entire score curve lies below the envelope need never appear. In the synthetic example below, at $a=10.8$ the height is $0.135$ and slope is $-0.60$. Equation (A18) recovers $x_*=10.65$ and $|y_*|=0.30$.

![Positive upper envelope for the finite synthetic zero configuration in the detector stress test. Two competing branches are shown individually. No ordinate in this illustration is offered as an observed off-line zeta zero.][plate-gaussian-envelope]

# A scalar detector and an exact bridge between prime tests {#atlas-transfer}

## What one moment buys, and what it costs

At a unique positive maximizer $z=x+iy$, choose a carrier interval away from $a=x$. The scalar quartet contribution is proportional in leading order to $e^{2ks_z(a)}\cos(\alpha-\omega k)$, where $\omega=4y(x-a)$ and $\alpha=\arg((z^2+1/4)^2)$. On a compact subinterval, $0<\delta\le|\omega|<1$. The arc on which the cosine is at most $-1/2$ has length $2\pi/3$. Consecutive unwrapped phases take steps of magnitude at most one, so a sufficiently long block, of length depending only on $\delta$, must enter this arc. Dominance over all other quartets and the bounded proper-power budget then force exponentially positive scalar prime moments along a bounded-gap sequence of integer widths.

The one-moment addendum thus gives, with the same $b_0$ as (A15),
$$
 {\rm RH}\quad\Longleftrightarrow\quad
 \forall a\in\mathbb Q_{>0},\quad
 \limsup_{n\to\infty}\frac1n\log(1+[b_0(a,n)]_+)=0 .
 \tag{A19}\label{eq:A19}
$$
For each fixed $a$, truncating the sum at $p\le e^{4n}$ costs $O_a(n^{-1/2})$ in that note. In (A16) a negative eigenvector is available at every large width. In (A19) the scalar can pass through zero at some widths, hence the $\limsup$. Replacing it by the matrix criterion's $\liminf$ for a single fixed scalar would discard the phase information used in the proof.

## A distributional bridge with its boundary terms

For Euler's constant $\gamma$ let $G(y)=\sum_{n\le y}\Lambda(n)(y/n-1)-y\log y+(1+\gamma)y$. Set $\mathcal R(t)=\mathbf1_{t\ge0}e^{-t/2}G(e^t)$ and $L=\partial_t^2-1/4$. The prime ramp has Green kernel $2\sinh(t/2)\mathbf1_{t\ge0}$. In distributions,
$$
 L\mathcal R
 =\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}
  -e^{t/2}\mathbf1_{t\ge0}
  +\tfrac{\gamma-1}{2}\delta_0+(1+\gamma)\delta'_0 .
 \tag{A20}\label{eq:A20}
$$
The smooth term before differentiation is $e^{t/2}(1+\gamma-t)$ on $t\ge0$. Its right derivative and value at zero give the two boundary coefficients. For an even Gaussian test $A$, $\delta'_0$ drops out and the ramp is paired with $LA$. Since $LA$ can change sign, a one-sided upper bound for $G$ does not directly bound this Gaussian response. The bridge identifies exactly what a transfer must control.

The November source also gives $A_{\rm arch}-2M_{\ge2}+22G_{\rm Gram}\succeq G_{\rm Gram}$ in its physical Gram normalisation on the stated odd test domain. Its Möbius tail (S8.7) uses an RH-strength Mertens estimate. The projected displacement formula (S8.9) acquires the defect $CB^*-BC^*$, which can survive even when the uncompressed commutator has rank two. These results are pertinent to source-selected projections, the 21-direction phase construction, and the three-microcarrier mosaic. The proposed common-width signed Möbius bound remains the point at which the mosaic needs new arithmetic. The [November continuity index](#november-1320-micro-results-the-detailed-continuity-index) locates the Type I, Type II, dispersion, and endpoint-neutrality work.

# One-sided growth and one integer inequality {#atlas-windows}

Let $\Theta=\sup_\rho\Re\rho$ over nontrivial zeta zeros. For $\lambda>1$ and $\theta>0$ the one-sided paper [D7] uses the ramp $G$ in (A20) to obtain, separately for each sign,
$$
 \lim_{Y\to\infty}\frac{\log\!\left(1+
       \int_Y^{Y^\lambda}[\pm G(x)]_+\,x^{-\theta}\frac{dx}{x}\right)}
       {\log Y}=\lambda(\Theta-\theta)_+ .
 \tag{A21}\label{eq:A21}
$$
The analytic argument selects a frequency with a unique, separated maximizing score that exceeds both zero and the zero-frequency score. It does not require the existence of a rightmost zero. Taking $Y=4^k$ and $\lambda=3/2$ gives the integer statistic in (S10.4). The one-sided estimate (W) in [E1--E2] is an external arithmetic input to a short deduction using (A21). This compilation records the internal analytic argument and its existing audit separately from that imported estimate.

Write $L_N=\prod_{j=1}^{N-1}\operatorname{lcm}(1,\ldots,j)$, $L_1=1$, and $R(x)=\sum_{m\le x}(x-m)\Lambda(m)$. Each prime power $m\le N$ contributes $\log p$ at exactly $N-m$ indices of the running product. Thus $\log L_N=R(N)$, and the LCM manuscript's criterion is
$$
 {\rm RH}\quad\Longleftrightarrow\quad
 L_{n^2}^4\le 2^{n^3}L_{2n^2}\qquad(n=1,2,\ldots).
 \tag{A22}\label{eq:A22}
$$
The forward argument uses the absolutely summable zero coefficients and $C_*=2+\gamma-\log(4\pi)$. The converse acts on $B(x)=(4R(x)-R(2x))/x$. For $\Re s>1$ its Mellin multiplier is $(4-2^{s+1})/[s(s+1)]$ times $-\zeta'(s)/\zeta(s)$. The numerator cancels the pole at $s=1$ and is nonzero for $1/2<\Re s<1$. The square-to-continuum bound and positivity argument in the [LCM chapter](#a-least-common-multiple-formulation-of-rh) are needed to exclude a pole in that strip. The universal inequality in (A22) is the arithmetic assertion that remains to prove independently.

For the dilation $Df(x)=f(2x)$, a third-order filter yields an entirely finite prime-power window:
$$
 (D-1)(D-2)(D-4)R(x)=\sum_{x<m<8x}\Lambda(m)w_x(m).
 \tag{A23}\label{eq:A23}
$$
The weight in (S11.17) changes sign at $m=10x/3$. As a function of $m$, its positive and negative areas both have magnitude $28x^2/3$. This balance concerns continuous area. The arithmetic sum samples the weights only at prime powers. At $n=42$ exact integer comparison gives $2^{123}<L_{n^2}^4/L_{2n^2}<2^{124}$, while (A22) allows $2^{74088}$. One can check this instance without rounding logarithms.

![Left, the piecewise-linear filter of (A23) in scale-free coordinates. Right, the two-scale statistic in (A22) computed from actual prime powers for integers 12 through 64; the highlighted point is n = 42. The vertical axis is magnified around zero. The universal comparison level is 1.][plate-arithmetic-windows]

# Further theorems and the short conditional proof {#atlas-frontier}

## An invariant gap and a sharp prime-sampling symbol

For the centred Paper VII polynomial (30.2), let $y_i=\log X_i$ be the ordered logarithms of its simple positive roots at parameter $h>0$. A differentiation at a simple root gives a closed system which the source uses to prove
$$
 y_i'=\tfrac12\sum_{j\ne i}\coth\frac{y_i-y_j}{2},
 \qquad y_{i+1}(h)-y_i(h)>h .
 \tag{A24}\label{eq:A24}
$$
How can a differential equation protect a gap? At first contact with the line $h$, let $L$ and $R$ be the numbers of roots strictly to the left and right of the adjacent pair. The compression terms telescope. The gap derivative is at least $[\coth((L+1)h/2)+\coth((R+1)h/2)]/2>1$, which exceeds the speed of the line. Small positive $h$ is supplied by the Hermite splitting of the initial multiple root. The analogous evolution of the actual theta moments introduces a fresh moment at each rank, as [Chapter 22](#ch-heat-controls) explains.

A different finite band appears in the October prime-sampling theorem [D3, Th. 7.3]. Its normalised Toeplitz symbol has coefficients $(a_0,a_1,a_2,a_3)=(8112,-5112,960,128)$:
$$
 \sigma(\theta)=a_0+2\sum_{j=1}^{3}a_j\cos(j\theta),\qquad
 64\le\sigma(\theta)\le20000.
 \tag{A25}\label{eq:A25}
$$
This range has a short independent check. For $u=\cos\theta$ the cubic is $1024u^3+3840u^2-10992u+6192$. Its derivative is increasing on $[-1,1]$ and at $1$ equals $-240$. The cubic therefore decreases throughout that interval and both endpoint values are attained. The actual sampling operator has the Jacobi weight and compact correction specified in the October paper. The positive symbol constrains the diagonal energy before any correlation between distinct primes is estimated.

## What a matched trace formula would imply

Here the natural variable is $v_\rho=\rho-1/2$, without the factor $1/i$ of the Gaussian chart. Given $0<\alpha<1/2$, let $Z_\alpha$ be the set of distinct nontrivial zeros with $|\Re\rho-1/2|\ge\alpha$. Suppose a thin-strip trace formula has exactly the complete Weil prime side and matching multiplicities, in the precise sense that $\sum_{\rho\in Z_\alpha}m_\rho\widehat{L^2\psi}(v_\rho)=0$ for every smooth compact $\psi$ supported away from zero. Here $L=\partial_t^2-1/4$ and $\widehat\psi(v)=\int\psi(t)e^{vt}\,dt$. The trace-rigidity paper obtains
$$
 \sum_{\rho\in Z_\alpha}
 \frac{m_\rho(v_\rho^2-1/4)^2}{(s-v_\rho)^9}=0
 \qquad(\Re s>1/2).
 \tag{A26}\label{eq:A26}
$$
Seven integrations by parts give a distribution of order at most seven. The matching assumption confines its support to $\{0\}$. Multiplication by $t^8$ kills its boundary distribution, and the one-sided Laplace transform produces (A26). On compact sets away from its potential poles the series converges normally. An omitted zero would give a nonzero ninth-order principal part, impossible for the analytic continuation of zero. Thus $Z_\alpha$ is empty under the stated matching hypothesis. Obtaining that hypothesis along $\alpha\downarrow0$ is the independent unresolved input of this trace route.

## A power-window deduction and its arithmetic premise

The external estimate (W) says that for each $\eta>0$ there is $K_\eta$ and there are arbitrarily large common windows $[Y,Y^{3/2}]$ on which $G(x)\le K_\eta x^{1/2+\eta}$ for every $x$. If $\Theta>1/2$, choose $1/2+\eta<r<\Theta$ and put $h=r-1/2-\eta>0$. On those windows,
$$
 \int_Y^{Y^{3/2}}[G(x)]_+x^{-r}\frac{dx}{x}
 \le \frac{K_\eta}{h}Y^{-h}\longrightarrow0.
 \tag{A27}\label{eq:A27}
$$
Equation (A21) at $(\theta,\lambda)=(r,3/2)$ gives this integral a strictly positive logarithmic growth exponent on *every* sufficiently large such window. This contradiction proves $\Theta\le1/2$. The functional equation reflects every nontrivial zero across the critical line and proves RH under (W). The deep input in this short proof is the simultaneous arithmetic bound (W) supplied by the external development [E1--E2].

The expanded integer-criterion manuscript in the evidence directory also gives a quantitative version of (A22). Let $U_n$ be either $L_{n^2}^4/L_{2n^2}$ or the four-scale ratio $V_n$ of (S11.16). For each fixed $\lambda>1$ and each sign, its result is
$$
 \lim_{N\to\infty}
 \frac{\log\!\left(1+\max_{N\le n\le N^\lambda}
                 [\pm n^{-3}\log U_n]_+\right)}{\log N}
       =2\lambda(\Theta-\tfrac12).
 \tag{A28}\label{eq:A28}
$$
The maximum runs over integers. At $x=n^2$ the normalised ratio equals a smoothed prime sum divided by $\sqrt x$. When $\Theta>1/2$, choosing an exponent $1/2<r<\Theta$ leaves an error $O(\sqrt x\log(2x))=o(x^r)$ on moving from $x$ to a nearest square. The expanded paper supplies the slope estimate and both sign arguments. It also identifies the endpoint constant under RH: on every fixed power window the maximum of $G(x)/\sqrt x$ tends to $C_*$. These finite-support, signed-growth and endpoint statements have different hypotheses.



# Recovered star equations: critical update {#atlas-recovered-star-equations}

The following statements were recoverable from original documents but absent or insufficiently prominent in the first edition's A1--A28 index. They are **source-reported theorem statements**, not new independent certifications by this compilation. Domain restrictions, negative controls and still-unproved source estimates are part of each statement.

## May 15: raw Xi curvature and the curvature-two saddle margin

Paper IX v0.4, *Curvature-2 Saddle Transfer and Finite Vertical Certificates for the Raw Xi-Jensen Program* (15 May 2026), distinguishes the raw even coefficients from a curvature-one surrogate. In its asserted theta-kernel saddle regime,

$$
 -\Delta^2\log\gamma_N^\Xi
 =\frac2N\left(1+O\left(\frac1{\log N}\right)\right),\qquad N\to\infty.
 \tag{A29}\label{eq:A29}
$$

This selects the leading model $P^{(2)}_{n,d}(z)=\sum_{k=0}^d\binom dk(n+k)^{-2(n+k)}z^k$. Its algebraic saddle-angle calculation yields

$$
 \Lambda_2=2\sqrt{6\sqrt3-9}<\pi,\qquad
 \frac\pi{\Lambda_2}>1.
 \tag{A30}\label{eq:A30}
$$

The strict leading-model margin is not a certified margin for every actual Xi window. The document itself requires an effective threshold, all remaining finite gates and matching hard-edge certificates. The eventual global transfer was not established in that edition. The original 100-page Paper IX source is preserved in the companion provenance manifest; these are newly highlighted, not newly proved, asymptotics.

## October 9: harmonic heat/discriminant cancellations

The *Harmonic Heat Research Master* develops an algebraic discriminant barrier $\mathcal B_N$ and a differential operator $\mathcal L$. With the precise polynomial normalization of that source it reports

$$
 \mathcal L\mathcal B_N=0,\qquad
 \sum_i\left(x_i\partial_{x_i}^2+\tfrac12\partial_{x_i}\right)\beta_N=0,
 \qquad H_N(u)=\beta_N(u_1^2,\ldots,u_m^2),\quad \Delta H_N=0.
 \tag{A31}\label{eq:A31}
$$

The identities are algebraic; the positive-degree harmonic polynomial is **not** asserted to have a fixed sign. The original research reports exact low-degree checks and a degree-16 counterpacket test. Its missing ingredient is a source-specific uniform sign/controlled-loss theorem across all degrees, not the cancellation identity itself.

## October 11: a single scalar Pringsheim sequence

In the 295-page *Complete Standalone Collected Edition* (11 October, Chapter 9), let $\widehat F_b$ denote the paper's particular normalized reciprocal-zero function, let $\widehat\beta_\nu$ denote its reciprocal zeros, and put $P_m(y)=(y-2)V_m(2y/b-1)$ with the **third-kind** Chebyshev $V_m$. For the exact source quadratic statistic $h_m=\widehat H[P_m]$, its Theorem 9.4 claims the equivalence

$$
 \mathrm{RH}\quad\Longleftrightarrow\quad h_m\ge0\ \ (m\ge0)
 \quad\Longleftrightarrow\quad
 \limsup_{m\to\infty}\frac1m\log\bigl(1+[S_1[P_m]]_+\bigr)=0.
 \tag{A32}\label{eq:A32}
$$

The generating function $D(z)=\sum_{m\ge0}h_mz^m$ has an explicit rational kernel with denominator $(1-z)((1+z)^2-4x_\nu^2z)$, $x_\nu=2\widehat\beta_\nu/b-1$. Under the source's pole noncancellation and normal-convergence hypotheses, an off-axis reciprocal zero forces a pole inside $|z|<1$ while the series remains analytic near every positive $0<z<1$. Pringsheim's theorem then detects an obstruction to nonnegative coefficients. **Crucial quantifier:** the subexponential one-sided bound is needed at *every sufficiently large index*, not an arbitrary subsequence. Chapter 10 reduces the still-unproved arithmetic step to a finite moving ordinary-prime sum between $(m+2)^8$ and $2^{12(m+2)}$.

## October 13: actual Jensen residue protection and the next-moment constraint

The 75-page *Jensen Residue Protection for the Riemann Xi Function* uses the complete theta source and an **unshifted** Jensen chain. At a simple predecessor root $v$, the successor sign is exactly

$$
 w_{n,v}=-\frac{p_{n+1}(v)}{p_n'(v)}.
 \tag{A33}\label{eq:A33}
$$

The paper proves positive residues in several specified regions, including an effective dominant branch and a shrinking source-dependent band. Its exact stated lower-band threshold is

$$
 \nu_0>\nu_*:=\frac{4911678521}{7734244776}
 =0.6350559961900022\ldots,
 \qquad \frac{\nu_0 W(2n/\pi)}n\le x\le\delta_0,
 \tag{A34}\label{eq:A34}
$$

with $n$ sufficiently large according to the source; $W$ is Lambert's function and $x$ the paper's scaled real-root coordinate. The significance is protection of **actual** residues without assuming global hyperbolicity. The source explicitly leaves the complete growing-frequency core and all-degree induction open. In addition, the optimized pair of protected bulk roots constrains the relative width of the prescribed next-moment interval to $2^{-n+o(n)}$, while the actual moment's normalized placement between the endpoints is $1/2+O(n^{-1})$. It therefore does **not** follow that the required global gate is automatic; the tiny admissible width is itself a severe conditioning obstruction.

## October 5--7: two nonidentical root-velocity systems

*RH Dumas Paper IV* (5 October) and *Dumas Residual Dynamics IV* (7 October) must not be merged with the **original May Paper IV** on rising factorials. The velocity paper states a source-forced implicit matrix with normalized spectrum $\{1,1-1/n,\ldots,1/n\}$; the later root-speed formulation uses an unnormalised $n$-dimensional matrix:

$$
 M_nq=(n+\alpha)\mathbf1-a_ny,
 \qquad \operatorname{spec}(M_n)=\{1,2,\ldots,n\},
 \qquad \det M_n=n!.
 \tag{A35}\label{eq:A35}
$$

These exact matrix/spectral descriptions concern the finite polynomial flow and its source forcing. They do not establish the sign of the new theta moment or complete the Xi real-rootedness induction.

## November 16 and 20: useful obstructions worth preserving

The 16 November Möbius--Gaussian note partitions divisor sizes and leaves an explicitly identified central signed band,

$$
 e^{3k/8}<d\le e^{21k/8}.
 \tag{A36}\label{eq:A36}
$$

The outer estimates depend on the specified external $7/8$ zero-free input; they do not establish central-band cancellation. The 20 November physical-metric audit constructs a family with $\|G_m-G_0\|\to0$ while a physically normalized operator retains eigenvalue $-1$. This is a **general countermodel** to an invalid spectral inference, not a counterexample to Suzuki's particular Xi operator.

# Original Paper III: corrected theorem and exact counterexample {#atlas-corrected-original-paper-iii}

This is the most consequential correction made after the first Atlas. The recovered May Paper III states a forced-root skeleton based on an identification of a flagged Jacobi--Trudi determinant with a boundary kernel. The independent 9 October source audit checks that identification using two implementations and finds an explicit contradiction in its claimed domain.

Let $\mathcal A_k^{\mathrm{mix}}(n,m)$ denote the **correctly counted ordered-triple** fully mixed coefficient in the original determinant convention. The audit gives

$$
 \boxed{\mathcal A_4^{\mathrm{mix}}(4,4)=-13\,888\ne0,}
 \tag{A37}\label{eq:A37}
$$

where the historical asserted value-root interval includes $m=4$ for $n=k=4$. Consequently the claimed universal skeleton divisor of old equation (26.4) is **false as stated**. The original summation additionally counted permutation orbits twice. Replacing that convention does not repair the counterexample.

The same audit supplies the corrected all-parameter coefficient-extraction formula. Put

$$
 V=(X-Y)(X-Z)(Y-Z),\quad L=\frac{Z(X-Y)^3(Y-Z)}{XY},
 \quad E_r=(2n+1-r,n,r),
$$

and let $[E_r]$ mean the indicated trivariate coefficient extraction applied to the source generating function $F_{k,m}$. Then the corrected **source-audited** identity is

$$
 \boxed{\frac{\mathcal A_k^{\mathrm{mix}}(n,m)}{2^k k!}
 =(n-1)[E_{n-1}]\,V F_{k,m}
 -[E_0]\,L\!\left(1-(X/Z)^{n-1}\right)F_{k,m}.}
 \tag{A38}\label{eq:A38}
$$

The report supplies a direct coefficient proof and 243 exact finite checks. The individual cocircuit **kernel** identity (A1)/(S3.4) survives. What does **not** survive is the uncorrected identification of that kernel with the complete flagged determinant or its forced-root divisibility theorem. No claim of global positivity or RH follows from the corrected extraction identity alone.

**Supersession rule.** The historical Chapter 26 and the associated original Paper III PDF are retained for scientific provenance, but their printed skeleton theorem and any downstream step explicitly using it are **retracted pending a replacement proof**. References in the older September layer to a 'proved skeleton' must be read subject to this correction. The corrected identity is the starting point for any future replacement theorem.

# Source genealogy, numbering and coverage audit {#atlas-source-genealogy}

The naming collisions in this archive are not cosmetic. They caused earlier research rankings to merge unrelated theorem families and made the earliest results appear later than their underlying source dates.

| Identifiable series | Primary source identity | Relevant coverage and archival status |
|:---|:---|:---|
| Original Papers I--V (May) | Boundary Schur gates; reciprocal insertions; cocircuit; rising factorials; minor ladders | Original ZIPs were recoverable from 19 May Library deposits; III's skeleton is superseded by A37--A38. |
| Original Papers VI--VIII (May) | Jensen proper-position, heat root flows, saddle/Airy | Distinct from October's newly numbered velocity papers. |
| Paper IX v0.4 through v442 (May--September) | Curvature-two saddle, finite gates, backward-heat collision/zero-number and later interval records | **Many versions, one evolving line**; no proof-grade joint global closure. |
| Referee I--III, II.1--II.9 (September) | Physical completed Weil form, six gates, metric corrections | Not the original polynomial Papers I--III. |
| Dumas velocity papers (October) | Critical-level geometry, prescribed next moment and successor residues | A paper called *RH Dumas Paper IV* is **not** original May Paper IV. |
| Residual Dynamics I--IV (October) | Root-speed, entropy/energy, signed source and capacity | Related but structurally separate from both preceding series. |
| 'Paper X', 'XI', 'XII' research leads | September 'Paper X readiness' note and historical conversational references | No standalone authored final *Paper X*, *XI* or *XII* individually recovered by the 23 November filename census. They are **unrecovered, not disproved or declared never written**. |

**Chronological caution.** The oldest individually dated RH file recovered directly in this Library census is Paper IX v0.4, 15 May 2026. Other May ZIPs are dated 19 May. Those are **saved-file dates**, not proof of the date of first investigation. An alternative early *Paper VII* title appears in conversation-era summaries but lacks a verifiable standalone recovered source. Do not merge it with the saved centered-heat Paper VII without a byte-identical match or other documentary evidence. No verified pre-2026 authored RH paper has been recovered in this audit.

**Provenance and source identifiers.** Primary documents supporting this critical update are the 15 May 100-page *Paper IX v0.4*; the 9 October *Harmonic Heat Research Master*; the 9 October *Programme Reading Audit*; the 11 October 295-page *Complete Standalone Collected Edition*, Chapters 9--11; the 13 October 75-page *Jensen Residue Protection*; the 5 October *RH Dumas Paper IV*; and the 13 September *Paper X Readiness* checkpoint. The claim ledger and the companion ZIP record file sizes and SHA-256 digests of the materialized copies. All mathematical status labels remain provisional pending specialist verification.


# Sources behind the atlas {#atlas-sources}

| Result | Primary evidence included in the source edition |
|:---|:---|
| 9 October Paper III correction and revised numbering | The exact 10-page *Programme Reading Audit* gives the invalidated skeleton, corrected boundary extraction and ordered-triple convention; see A37--A38 and the source genealogy. |
| May/October recovered stars | Original Paper IX v0.4 (100 pp); *Harmonic Heat Research Master* (9 Oct); *Complete Standalone Collected Edition* (295 pp, 11 Oct); *Jensen Residue Protection* (75 pp, 13 Oct); *RH Dumas Paper IV* (5 Oct). |
| Original Papers I--VIII, IX versions, fifty-chapter core | The original edition archive, including the source register, the adjacent-shift paper and the v150, v421--423 and v442 exhibits. |
| Complete Weil form and the six gates | Referee II.1 freeze of 24 September, II.8 terminal audit and II.9 repair of 26 September in the evidence directory. Referee III full PDF in the original edition. |
| Divisor programme, Hausdorff/RESET, finite sections and spectral alternatives | Historical chapters 13--18 and 33--45. The original computational receipts and their scope are indexed in the [computational appendix](#app-computations). |
| October signed primes and complete theta | *Signed Prime Correlations and Theta Continuation*, equations (1.1)--(1.6), (5.10), theorems 7.3 and 8.1, and the subsequent correlation criteria. Full paper in the original edition. |
| Rank-64 finite result | *Relative Interpolation*, 4 November, §§2 and 5A. The pilot's explicit finite bracket assumption appears beside (A4). |
| Finite arithmetic parity | *Actual Weil Stieltjes Parity*, 8 November. *Prime-Free All-N Perron–Padé*, *Prime Threshold Energy Continuation*, and *C3 Certificate and Prolate Convergence*, 9 November. All four primary notes accompany this edition. |
| Gaussian matrix, growth and scalar follow-up | *Two Poles, Two Probes, Three Prime Moments*, *Pole-Neutral Trace Rigidity*, the finite synthetic stress test, and the complete *Scalar One-Moment* addendum of 22 November. |
| Ramps, one-sided sums, LCMs and external inputs | One-sided and LCM papers, the expanded integer-criterion manuscript, November Gaussian consolidation §§T8--T10 and 14, and the independent one-sided audit in the original edition. References [E1--E10] are listed in the synthesis. |

The figures are computed from the equations and the finite data described in their captions. The companion includes the plotting code, the prime-window data, exact algebra and integer checks, and the historical source archive. The finite tests cover polynomial identities, matrix signs in specified examples, the window weights and particular LCM ratios. The general analytic results retain the hypotheses and verification status of their primary papers.


# Index of principal equations {#atlas-locator}

| Equation | Page | Equation | Page |
|:---|---:|:---|---:|
| \hyperref[eq:A1]{A1} Cocircuit | \pageref{eq:A1} | \hyperref[eq:A2]{A2} Wronskian | \pageref{eq:A2} |
| \hyperref[eq:A3]{A3} Hankel criterion | \pageref{eq:A3} | \hyperref[eq:A4]{A4} Zero tail | \pageref{eq:A4} |
| \hyperref[eq:A5]{A5} RESET cost | \pageref{eq:A5} | \hyperref[eq:A6]{A6} Terminal strip | \pageref{eq:A6} |
| \hyperref[eq:A7]{A7} Cofinal bound | \pageref{eq:A7} | \hyperref[eq:A8]{A8} Divisor filter | \pageref{eq:A8} |
| \hyperref[eq:A9]{A9} Sector remainder | \pageref{eq:A9} | \hyperref[eq:A10]{A10} Prime diagonal | \pageref{eq:A10} |
| \hyperref[eq:A11]{A11} Mixed resolvent | \pageref{eq:A11} | \hyperref[eq:A12]{A12} Parity Gram | \pageref{eq:A12} |
| \hyperref[eq:A13]{A13} Pole-neutral probes | \pageref{eq:A13} | \hyperref[eq:A14]{A14} Quartet determinant | \pageref{eq:A14} |
| \hyperref[eq:A15]{A15} Prime moments | \pageref{eq:A15} | \hyperref[eq:A16]{A16} Matrix criterion | \pageref{eq:A16} |
| \hyperref[eq:A17]{A17} Growth envelope | \pageref{eq:A17} | \hyperref[eq:A18]{A18} Reconstruction | \pageref{eq:A18} |
| \hyperref[eq:A19]{A19} Scalar criterion | \pageref{eq:A19} | \hyperref[eq:A20]{A20} Boundary terms | \pageref{eq:A20} |
| \hyperref[eq:A21]{A21} One-sided growth | \pageref{eq:A21} | \hyperref[eq:A22]{A22} LCM criterion | \pageref{eq:A22} |
| \hyperref[eq:A23]{A23} Dilation filter | \pageref{eq:A23} | \hyperref[eq:A24]{A24} Heat-gap barrier | \pageref{eq:A24} |
| \hyperref[eq:A25]{A25} Sampling symbol | \pageref{eq:A25} | \hyperref[eq:A26]{A26} Trace rigidity | \pageref{eq:A26} |
| \hyperref[eq:A27]{A27} External-window deduction | \pageref{eq:A27} | \hyperref[eq:A28]{A28} LCM growth on squares | \pageref{eq:A28} |
| \hyperref[eq:A29]{A29} Raw-Xi curvature | \pageref{eq:A29} | \hyperref[eq:A30]{A30} Curvature-two margin | \pageref{eq:A30} |
| \hyperref[eq:A31]{A31} Harmonic heat | \pageref{eq:A31} | \hyperref[eq:A32]{A32} Pringsheim scalar criterion | \pageref{eq:A32} |
| \hyperref[eq:A33]{A33} Actual residue | \pageref{eq:A33} | \hyperref[eq:A34]{A34} Shrinking Jensen band | \pageref{eq:A34} |
| \hyperref[eq:A35]{A35} Finite velocity spectrum | \pageref{eq:A35} | \hyperref[eq:A36]{A36} Central Möbius band | \pageref{eq:A36} |
| \hyperref[eq:A37]{A37} Paper III counterexample | \pageref{eq:A37} | \hyperref[eq:A38]{A38} Corrected boundary map | \pageref{eq:A38} |

## Selected equations in the synthesis and historical chapters

| Equation | Page | Equation | Page |
|:---|---:|:---|---:|
| \hyperref[eq:S3.2]{S3.2} Boundary reservoir | \pageref{eq:S3.2} | \hyperref[eq:S3.3]{S3.3} Reciprocal deformation | \pageref{eq:S3.3} |
| \hyperref[eq:S3.5]{S3.5} Rising-factorial expansion | \pageref{eq:S3.5} | \hyperref[eq:S3.6]{S3.6} Finite Sturm ladder | \pageref{eq:S3.6} |
| \hyperref[eq:S4.2]{S4.2} Bernstein subdivision | \pageref{eq:S4.2} | \hyperref[eq:S4.4]{S4.4} Collision index | \pageref{eq:S4.4} |
| \hyperref[eq:S5.1]{S5.1} Complete Weil form | \pageref{eq:S5.1} | \hyperref[eq:S5.5]{S5.5} Positive Green kernel | \pageref{eq:S5.5} |
| \hyperref[eq:S5.6]{S5.6} Schur complement | \pageref{eq:S5.6} | \hyperref[eq:S6.2]{S6.2} Native mesh bound | \pageref{eq:S6.2} |
| \hyperref[eq:S6.3]{S6.3} External fixed window | \pageref{eq:S6.3} | \hyperref[eq:S8.7]{S8.7} Möbius tail | \pageref{eq:S8.7} |
| \hyperref[eq:S8.9]{S8.9} Projected commutator | \pageref{eq:S8.9} | \hyperref[eq:S10.4]{S10.4} One-sided integer sum | \pageref{eq:S10.4} |
| \hyperref[eq:S11.8]{S11.8} Zero-coefficient mass | \pageref{eq:S11.8} | \hyperref[eq:S11.13]{S11.13} LCM Mellin transform | \pageref{eq:S11.13} |
| \hyperref[eq:18.10]{18.10} Divisor optimisation | \pageref{eq:18.10} | \hyperref[eq:19.3]{19.3} Actual logarithmic moments | \pageref{eq:19.3} |
| \hyperref[eq:34.2]{34.2} Fixed-base Hausdorff law | \pageref{eq:34.2} | \hyperref[eq:36.2]{36.2} Off-resonance transport | \pageref{eq:36.2} |
| \hyperref[eq:37.5]{37.5} Inverse-RESET scalar | \pageref{eq:37.5} | \hyperref[eq:S11.17]{S11.17} Explicit filter weights | \pageref{eq:S11.17} |

The [historical equation index](#app-equations) gives the chapter and context for the full September sequence.



\part{November synthesis and research priorities}

# The mathematical problem and the shape of the programme

## What an RH proof must establish

Write

$$
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \Xi(t)=\xi\left(\frac12+it\right).
\tag{S1.1}\label{eq:S1.1}
$$

RH is the assertion that every zero of $\Xi$ is real. Equivalently, the nontrivial zeros $\rho$ of $\zeta$ satisfy $\Re\rho=1/2$. The programme has repeatedly converted this assertion into a positivity condition, a spectral-coercivity problem, a real-rootedness problem, a moment condition or an arithmetic growth inequality. Such a conversion is useful only when it yields a genuinely easier *unconditional* estimate. A criterion equivalent to RH has **not**, by itself, solved the problem.

Four principal routes survive as useful frameworks:

1. **Finite positivity and Jensen:** obtain the correct actual-$\Xi$ coefficients and prove real-rootedness of enough unshifted Jensen polynomials, or an equivalent all-rank moment positivity condition.
2. **Physical Weil forms:** prove a suitable cofinal lower bound for the entire completed quadratic form in the same physical Hilbert space and with all prime powers, pole terms and old--new interactions retained.
3. **Signed arithmetic sources:** exploit cancellation among prime and prime-power contributions at the exact scale required by a pole-neutral detector, rather than applying unsigned estimates that lose the necessary sign.
4. **One-sided arithmetic windows:** deduce zero location from an exact growth formula for the von Mangoldt ramp and a strong arithmetic estimate supplied, after November 2026, by the external Alpöge--Claude theorem.

The work spans many useful subproblems, but the same logical bottleneck recurs: an identity is constructed exactly, and an all-scale *sign or rate inequality* on the corresponding actual arithmetic object remains.

## A common hierarchy of evidence

Consider the hierarchy

$$
\text{identity}\quad\Longrightarrow\quad
\text{finite/local theorem}\quad\Longrightarrow\quad
\text{quantified global estimate}\quad\Longrightarrow\quad\text{RH}.
\tag{S1.2}\label{eq:S1.2}
$$

None of these arrows is automatic. A finite Gram matrix can be positive although the infinite completion has negative directions. A model polynomial may be hyperbolic while the actual xi polynomial is not known to be. A compressed positive block does not guarantee that its Schur complement stays positive. A Gaussian test can detect an off-line zero but does not bound the arithmetic response without a separate estimate. The historical counterexamples are therefore part of the programme's mathematical content rather than an embarrassment to erase.

## Three particularly economical RH endpoints

**Physical endpoint.** If $q_{\mathrm{comp},b}$ denotes the complete odd Weil form on its actual domain and the pole-neutral condition is retained, a proposed sufficient statement is a sequence $b_j\to\infty$ for which

$$
q_{\mathrm{comp},b_j}[u]\ge -\beta_j\|u\|^2,
\qquad \log(1+\beta_j)=o(b_j),
\tag{S1.3}\label{eq:S1.3}
$$

for *all* admissible neutral tests at each $b_j$. The fixed two-packet detector shows why such a cofinal bound would exclude a hypothetical off-line zero. It is **not proved** for the actual full form.

**Moment endpoint.** Let $F$ be the normalised even descent of xi and $p_j$ the logarithmic coefficients as in the preserved book. The Hankel matrices

$$
H_n=(p_{i+j+1})_{0\le i,j<n}
\tag{S1.4}\label{eq:S1.4}
$$

lead to a positive-measure condition. The corresponding all-rank positivity is another endpoint, but finite positivity through the recorded ranks does not establish it.

**Arithmetic endpoint.** The first-prime Gaussian matrix $M_1(a,k)$ has an RH-strength bound proposed in the November ledger:

$$
\boxed{\quad
\liminf_{k\to\infty}\frac1k
\log\!\left(1+[\lambda_{\max}M_1(a,k)]_+\right)=0
\quad\text{for every rational }a>0.\quad}
\tag{S1.5}\label{eq:S1.5}
$$

This remains an **open unconditional arithmetic inequality** in the independent programme. A route that assumes it has merely relocated the central difficulty.

# Chronology and architecture: April to November 2026

## April--May: Schur algebra and the first numbered papers

The earliest recovered work explored Herglotz--Pick, Stieltjes, P\'olya frequency, logarithmic derivatives, theta/Mellin transforms and finite-symbol positivity. An initial finite-symbol scaling proposal did not survive scrutiny. Original **Papers I--V** then developed concrete finite determinant and polynomial mechanisms: boundary absorption; flagged reciprocal-pair perturbations; cocircuit--Brion factorisation; rising-factorial coefficients of residuals; and finite Sturm/Schur boundary ladders. These are distinct from later arithmetic Weil-form methods. Their standalone exact identities should be evaluated as algebra and combinatorics even when the proposed Xi transfer remains open.

Original **Papers VI--VIII** moved toward actual Jensen polynomials: adjacent-shift proper position, Wronskian and Gram feasibility, heat-root flows, log-gap barriers, and saddle/Airy asymptotics. They explain why positivity in a model is insufficient unless a transfer theorem controls the actual coefficient sequence with the correct degree and shift.

## May--September: the Paper IX revision tree

Paper IX grew into an unusually large family of region routers, Wronskian certificates, backward-heat collision studies and finite-height bridges. The early seven-region target covered protected bulk, small-parameter heat, soft-edge Airy, low-slope overlap, hard-left edge, outer strips and finite repositories. Later audits found gaps in strict overlap margins, parameter dictionaries and some dependency requirements. The original $M_\star=671{,}088{,}640$ should therefore be read as a *historical routing threshold*, not an established cutoff at which the actual all-parameter theorem becomes true.

The important version changes are not chronological refinements of one proof: v150 created detailed finite Bernstein/Wronskian proof objects; v421 and v422 developed collision-degree and zero-number compression; v423--v427 probed finite-height guards and the remaining small-time horn; v437--v442 produced thousands of interval records for a separately normalised outer region. The source versions and their different lambda charts must not be conflated.

## June--August: compact moments and finite-prime activation

The F18--F22 branch developed Bernstein/Laguerre and Joukowski folds, compact Hausdorff and Jacobi/CMV transforms, and conditions relating positive measures to xi zeros. The fixed-base F35--F42 family converted part of the desired condition into explicit ordinary-prime windows and canonical moment depths. F161--F166 developed Darboux/Christoffel and RESET transport with corrected off-resonance coordinates and source-dependent entry conditions. A finite matrix certificate or a conditional transport identity is valuable but does not furnish automatic regeneration of the next actual Xi moment or prime-activation front.

## September: physical Weil forms, referee editions and hostile audit

The physical programme treated the complete odd Weil quadratic form, prime powers, boundary poles, old--future blocks and inverse-energy budgets. A candidate chain was assembled in September's proof-facing V and referee manuscripts. The original II.1 six-gate internal pass was subsequently narrowed: II.5 retained valid two-coordinate and same-Gram identities, while II.8--II.9 reopened their application to the actual post-short physical denominator. Referee III replaced that broad inference with a carefully scoped moving terminal-strip theorem. A separate W200 fixed-window certificate, originating with Vincent Liu, supplied local evidence but not a global expanding-window theorem.

## October: signed correlations, complete theta source and source obstructions

The October manuscript *Signed Prime Correlations and Theta Continuation for the Riemann Xi Function* isolated a pole-neutral ordinary-prime statistic, square-summable sector remainder, explicit prime-diagonal energy and the unresolved signed off-diagonal estimate. Its theta side developed exact heat/discriminant identities and conditional continuation criteria. This was one of the most substantial attempts to create an independent arithmetic closure, with its limitations explicitly stated.

## November: Gaussian compression, external formal proof and two arithmetic criteria

The November Gaussian work reduced the first-prime quadratic form to three actual logarithmic prime moments, clarified the proper-prime-power budget in the physical Gram metric, constructed pole-neutral two-probe and multi-carrier detectors and exhibited counterexamples to invalid metric transfers. On 20 November Alpöge announced a Lean formalization developed with Claude; on 21 November the Lean and Mathlib communities certified the formal RH statement and proof according to their public verification report [E1]. Rubinstein's 164-page explanation explicitly imports its deepest arithmetic inequality (M) from the Lean library [E2]. Subsequent Dumas manuscripts of 22--23 November established proposed exact growth and least-common-multiple reformulations; the distinction between an internal analytic theorem, an RH-equivalent criterion and an imported external proof is central.

# The first five papers and the finite algebraic inheritance

## Paper I: a completed boundary reservoir

The first boundary-absorption mechanism considers a signed Schur-minor gate

$$
G_n=(n-1)T+\sum_{r=0}^{n-2}(C_r+D_r-2A_r),
\tag{S3.1}\label{eq:S3.1}
$$

where the local curvature terms may have either sign. The positive endpoint emerges from cancellation across the *completed* expression. Its hook-content and telescoping certificates yield, for $n\ge3$, a product with factors of the form

$$
G_n(1^m)=\frac{6(m+1)(m+2)}{n!(n+1)!(n-2)!}
\prod_{j=0}^{n-1}(m-j)^{e_{n,j}},
\quad e_{n,j}=\min\{3,\max(1,n-j-1)\}.
\tag{S3.2}\label{eq:S3.2}
$$

The original source printed a formula also at $n=2$; the later book checked that boundary case separately and gave $G_2(1^m)=\frac12m(m-1)(m+2)$. It would be incorrect to silently retain the uniform claim at $n=2$. The endpoint positivity is exact within the finite Schur problem but does not prove an all-rank xi positivity theorem.

## Paper II: reciprocal-pair deformation

For $u=\cosh a-1$, $v=\cosh b-1$ and two reciprocal pairs, the elementary-symmetric row has the exact decomposition

$$
e_r(e^a,e^{-a},e^b,e^{-b},1^{m-4})
=\binom mr+2(u+v)\binom{m-2}{r-1}+4uv\binom{m-4}{r-2}.
\tag{S3.3}\label{eq:S3.3}
$$

This isolates mixed perturbation channels that cannot be discarded. The valid literal alphabet requires $m\ge4$; polynomial continuation outside the literal range must be labeled as such. The coefficients and certificate layers support finite robustness, not an unrestricted xi deformation theorem.

## Paper III: cocircuit identity, corrected boundary map and invalidated skeleton

The surviving exact kernel factorisation is

$$
P_{\mathrm{low}}(X,Y,Z)
=Z\frac{(X-Y)^3(Y-Z)}{XY}
=X^2Z(1-Y/X)^3(1-Z/Y).
\tag{S3.4}\label{eq:S3.4}
$$

**Critical edition, source audit of 9 October:** the *factorisation* above holds algebraically, but the original identification with the complete flagged gate and the resulting universal forced-root skeleton were disproved. The exact counterexample and corrected map are given in (A37)--(A38). No downstream divisibility proof may cite S3.4 alone.

The apparent cubic is actually a *fourth-order mixed difference*: three differences in one direction, one in the other. Multiplication of a finite chain by its first difference leaves endpoints, a Brion-type cancellation. The source then builds forced-root skeletons with multiplicities detected by values and first/second parameter derivatives. The crucial inferential boundary: an exact divisor of a finite flagged determinant does not establish the sign of its residual, much less identify it with an arithmetic Weil form.

## Papers IV--V: residual positivity and a finite Sturm transport

Paper IV studies shifted residuals in rising factorials,

$$
R_{n,k}(y)=\sum_{j\ge0}a_{n,k,j}\,y^{\overline j},
\qquad a_{n,k,j}=\frac{\nabla^jR_{n,k}(0)}{j!}.
\tag{S3.5}\label{eq:S3.5}
$$

Nonnegative rising-factorial coefficients imply additional finite positivity, but the source proves selected layers and cases rather than every residual. Paper V transports a polynomial-remainder ladder and identifies a third-order minor controlling monotone ratios,

$$
K_j-K_{j+1}=
\frac{\Delta_{1,j}}{\Omega_{j+1}\Omega_{j+2}}.
\tag{S3.6}\label{eq:S3.6}
$$

The resulting Sturm argument is conditional on the full admissible determinant and descent hypotheses. It is not an unrestricted theorem about all actual Jensen polynomials.

## Paper VI: proper position and the Wronskian

For a positive sequence $\gamma_n$, put

$$
J_{n,d}(z)=\sum_{k=0}^{d}\binom dk\gamma_{n+k}z^k.
\quad R=J_{n,d+1},\;P=J_{n,d},\;Q=J_{n+1,d}.
\tag{S3.7}\label{eq:S3.7}
$$

The identities

$$
R=P+zQ,\qquad Q=\frac{R'}{d+1},\qquad
P=R-\frac{zR'}{d+1}
\tag{S3.8}\label{eq:S3.8}
$$

link higher-degree hyperbolicity to adjacent-shift proper position. One may write the Wronskian explicitly as an anti-diagonal sum of adjacent coefficient minors,

$$
W[P,Q](z)=\sum_{0\le i<j\le d}
(j-i)\binom di\binom dj
\bigl(\gamma_{n+i+1}\gamma_{n+j}-\gamma_{n+i}\gamma_{n+j+1}\bigr)z^{i+j-1}.
\tag{S3.9}\label{eq:S3.9}
$$

The global Wronskian sign can be recast as a one-variable sum-of-squares/Gram feasibility problem with an affine Gram fibre of dimension $(d-1)(d-2)/2$, subject to exact-degree caveats. The relationship is useful outside RH, but it is already close to classical polar-derivative and real-rooted polynomial theory; priority and newness require specialist comparison.

## Papers VII--VIII: heat flow, cubic symmetry, and saddles

A finite centred heat model is

$$
H_{d,h}(X)=\sum_{k=0}^d(-1)^k\binom dk\exp\!\left(\frac h2k(d-k)\right)X^k,
\qquad \partial_hH=\frac12(d\theta-\theta^2)H,
\quad\theta=X\partial_X.
\tag{S3.10}\label{eq:S3.10}
$$

It exhibits an exact barrier for logarithmic root gaps within the model. Reflection gives $X^dH_t(1/X)=(-1)^dH_{-t}(X)$, and for even $d$ the central-gap first derivative vanishes for odd centred perturbations, including cubic perturbations. This does not control second-order or outer-root effects.

The variable-curvature saddle analysis and Airy module address a different cubic: coalescing saddles lead to a cubic phase and the $d^{-2/3}$ edge scale. Such local asymptotics require contour dominance, uniform remainder bounds and a proved actual-coefficient transfer before they can establish RH-scale hyperbolicity.

# Paper IX, version by version: what actually survived {#paper-ix-version-by-version-what-actually-survived}

## The seven-region ambition and its logical burden

Paper IX attempted to cover infinitely many Jensen degrees and shifts by assigning each parameter pair to a theorem owner. In one early notation the nominal finite region contained

$$
G(M)=\left\{(n,d):n\ge0,\;d\ge1,\;
 n+\frac{d+1}{2}<M\right\},\qquad |G(M)|=M(M-1).
\tag{S4.1}\label{eq:S4.1}
$$

At $M=M_\star=671{,}088{,}640$, the number of gates is approximately $4.5036\times10^{17}$. One cannot confuse a finite list of a few hundred checked gates with all $G(M_\star)$. In addition, the later v442 lambda variable was defined in a distinct heat/height chart; it must **not** be identified with the earlier Jensen variable $d/(n+d/2)$, which is at most two.

Each region requires (a) the actual coefficient normalisation, (b) explicit parameter coverage, (c) quantitative error and strict margin, (d) compatible overlap on adjoining edges, and (e) a proof or independently checked numerical certificate with all prerequisites. In the retrospective, the original seven-owner global PASS was withdrawn because these conditions were not simultaneously established.

## v150: genuine finite proof objects

At version v150 the Wronskian $W[P,Q]$ was compactified on each real half-line through

$$
H_\pm(t)=(1-t)^{2d-2}
W\!\left(\pm 2^e\frac{t}{1-t}\right),\quad 0\le t\le1.
\tag{S4.2}\label{eq:S4.2}
$$

Dyadic de Casteljau subdivisions supplied positive Bernstein coefficient leaves, with prefix-free interval cover certificates. The archived report records 656 accepted gates in $0\le n\le40$, $1\le d\le16$, and 3,616 detailed Bernstein leaves. This is a meaningful finite interval-arithmetic achievement, but cannot substitute for the remaining infinite-degree geometry. The report's verifier description is a source claim; a new independent complete replay is not claimed in this volume.

## v421: the local backward-heat degree

For a real analytic solution of the backward heat equation, the local polynomial at a multiple zero of multiplicity $m$ is modelled by

$$
P_m(\tau,y)=e^{-\tau\partial_y^2}y^m
=\sum_{k=0}^{\lfloor m/2\rfloor}
\frac{(-\tau)^k}{k!}\frac{m!}{(m-2k)!}y^{m-2k}.
\tag{S4.3}\label{eq:S4.3}
$$

The archive's local Brouwer degree calculation yields

$$
\deg(H,-H_x)=-\lfloor m/2\rfloor.
\tag{S4.4}\label{eq:S4.4}
$$

The key feature is *sign rigidity*: different collisions have negative degree and cannot cancel in a total degree-zero argument. The August audit judged the finite derivation credible, but specifically requested proof-quality control of the analytic remainder under parabolic rescaling, the local homotopy, event isolation and orientations. This is theorem-scale mathematics, not a certificate for a new global rectangle. Its priority relative to classical parabolic zero-count literature remains to be established.

## v422: zero-number compression

When a space--time rectangle has verified zero-free vertical guards and suitable isolated interior collisions, the archive proposes the zero-count relation

$$
Z(t_1)-Z(t_0)=2\sum_{p}\lfloor m_p/2\rfloor.
\tag{S4.5}\label{eq:S4.5}
$$

Equality of endpoint counts would then exclude all interior multiple-zero events. This compresses a huge branch-tracking problem to boundary data. However, the missing *verified boundary guards and top counts* cannot be replaced by the local formula. The published classical zero-number and de Bruijn--Newman literature must be distinguished from any programme-specific deduction.

## v423--v427: why finite height is not the missing theorem

The rigorous Platt--Trudgian verified-height source supplied the input $T_*=3{,}000{,}175{,}332{,}800$ and the associated $X_*=2T_*$. The later audit observed a crucial asymptotic mismatch. If high-height control begins only for $X\gtrsim \exp(C/t)$, then **every finite** $X_*$ leaves a small positive-$t$ horn uncovered. Increasing a fixed computed height buys only logarithmic improvement in the time cutoff.

The analytic transition in the relevant saddle chart occurs near

$$
\lambda=t\log\!\left(\frac{x}{4\pi}\right)=2,
\tag{S4.6}\label{eq:S4.6}
$$

where the effective saddle crosses $\Re s=1$. A phase-aware argument in the intermediate range could be more important than brute-force extension of trillions of verified zeros. This is a *research target*, not a proved improvement to the de Bruijn--Newman constant.

## v437--v442: a substantial outer-region archive

The v442 source archive was inspected at the archive level in preparing this synthesis. It contains 3,526 ZIP members and 3,500 post-v437 interval records, with the supplied README describing coverage of its outer chart from $\lambda=5.52$ to $15$ and an asymptotic predecessor beyond. The finite height range stated there extends from $X_*$ to approximately $4.38997\times10^{20}$. The recorded outstanding region is

$$
x\ge X_*,\qquad0<\lambda<5.52.
\tag{S4.7}\label{eq:S4.7}
$$

Archive count, checksum, or a metadata-level interval partition check does **not** independently establish each input lemma of its complex first-contact/Rouch\'e chain. Some predecessor computational modules are not included in the v442 bundle. The mathematical status is *restricted source-reported regional certificates and a major uncovered horn*, not complete RH coverage.

## Paper IX's enduring contribution

The most reusable pieces are not necessarily the most recent files: the v150 finite-proof-object design; the v421 negative collision degree; the v422 zero-number compression; the saddle/phase geometry; the Airy matching obligations; and the explicit demonstration that no finite height alone closes a small-time problem. As a historical proof programme it is unusually rich, but its global theorem flag remains **false within the original Dumas work**.

# The physical Weil form and the referee series

## One complete quadratic form, not several convenient substitutes

Let $\mathcal H_b=L^2(0,b)$ and let $J_bu$ be the unnormalised odd zero extension. Then $\|J_bu\|^2=2\|u\|^2$. Write

$$
\begin{split}
q_{\mathrm{arch},b}[u]
&=\frac1{4\pi}\int_{\mathbb R}
\bigl(\Re\psi(1/4+it/2)-\log\pi\bigr)|\widehat{J_bu}(t)|^2\,dt,\\
q_{\mathrm{raw},b}[u]
&=q_{\mathrm{arch},b}[u]
+\sum_{n<e^{2b}}\frac{\Lambda(n)}{\sqrt n}
\langle u,(R_{\log n}-S_{\log n})u\rangle,\\
q_{\mathrm{comp},b}[u]
&=q_{\mathrm{raw},b}[u]-|\langle g_b,u\rangle|^2,
\qquad g_b(x)=2\sinh(x/2).
\end{split}
\tag{S5.1}\label{eq:S5.1}
$$

Here $S_\lambda$ and $R_\lambda$ are the exact truncated translation and reflected-shift operators defined in the preserved physical chapter. The density domain carries a logarithmic Fourier weight. Keeping the pole subtraction and the correct norm matters: a positive coefficient Gram obtained in an unrelated basis is not necessarily the physical Weil-form denominator.

For pole-neutral smooth odd tests, this representation agrees with the corresponding full-line Weil form up to the harmless normalising factor of two. Under RH, the spectral representation suggests nonnegativity; conversely, a hypothetical off-line quartet can create sharply negative tests. The technical problem is to derive an unconditional lower bound on the *entire actual form* on expanding windows.

## Referee III's moving terminal strip

The strongest source-contained local physical theorem is the terminal-strip bound. For $b\ge10$ and

$$
\delta=10^{-3}b e^{-b},\qquad
\operatorname{supp}u\subset (b-\delta,b),
\tag{S5.2}\label{eq:S5.2}
$$

Referee III gives

$$
\boxed{\quad q_{\mathrm{comp},b}[u]\ge \frac b2\|u\|^2,
\qquad q_{\mathrm{raw},b}[u]\ge\frac b2\|u\|^2.\quad}
\tag{S5.3}\label{eq:S5.3}
$$

The argument proves an uncertainty lower bound for the Archimedean term,

$$
q_{\mathrm{arch},b}[u]\ge
\left(\log\frac{\pi}{2\delta}-1-C_0\right)\|u\|^2,
\qquad C_0<4.68,
\tag{S5.4}\label{eq:S5.4}
$$

and pays the reflected prime, proper-power and pole contributions using explicit inequalities. This is a substantive theorem on the *complete form in the stated strip*. In integer apertures $b=\tfrac12\log N$, the protected new-index batch has asymptotic order $\sqrt N\log N/1000$.

The missing implication is important: the direct compression to a new terminal strip being positive does not mean that the **Schur complement after eliminating all older directions** is positive. Local strips do not automatically assemble into a cofinal global estimate. Each elimination changes the future denominator and incurs a potentially adverse inverse cost.

## Exact positive reference and the wrong-denominator trap

The positive Green-type kernel

$$
G_b(x,y)=e^{-|x-y|/2}-e^{-(x+y)/2}
\tag{S5.5}\label{eq:S5.5}
$$

is a genuine Gram kernel; combined with a pole vector it participates in an exact integrated-shift cancellation. A typical block decomposition is

$$
A=\begin{pmatrix}X&B\\B^*&D\end{pmatrix},
\qquad S=X-B(D+sI)^{-1}B^*.
\tag{S5.6}\label{eq:S5.6}
$$

Only when the denominator and the source are the *actual ones after shorting* does an inverse estimate bound the desired loss. The elementary identity

$$
(Bc)^*(BB^*)^\dagger(Bc)\le\|c\|^2
\tag{S5.7}\label{eq:S5.7}
$$

is true in its own Gram metric, but substituting it for $D$ without proving a compatible comparison is a logical error. This is the central correction from the September referee cycle and remains relevant to the November Gaussian work.

## The referee revision chain

**Referee I / September 23 candidate.** The initial Brehmer/current-prime source decomposition, pole channels and common-cut idea were assembled into a proposed $N^{o(1)}$ inverse-debt chain. Later examination distinguished a bounded independent-prime component map from an unbounded common-input physical map; the candidate had not proved the required identification.

**Referee II / September 24.** The smooth first-prime component was extracted into its natural pole channel, with a bounded lower-order correction. This is a valid structural improvement. The residual centred physical source and its actual common denominator still required proof.

**II.1 historical freeze.** A six-gate PASS was recorded internally. Subsequent scope and metric objections mean that label cannot be used today as a proof premise. The chronology of the historic claim is preserved, not erased.

**II.5.** Two-dimensional ODE transfer and same-Gram Woodbury identities survived under their assumptions. What failed was the inference that a low-dimensional local representation per prime automatically creates one common global port range after all Schur operations.

**II.8.** Reopened source placement, actual projector range, denominator sign, mixed collar costs and the induction/cofinal passage. This critique is a contribution because it identifies exact missing implications rather than merely declaring the whole programme false.

**II.9.** Constructed a decisive high-frequency countertest for an unrestricted centred old/future $L^2$ cross, of order $\Theta_a(e^{b/2})$ after fixed finite-rank pole projection. The weighted Archimedean penalty means this does not refute all *observable-specific* physical energy estimates. The revised statement prevents an invalid absolute-norm shortcut while preserving more targeted routes.

**Referee III.** Returned to one physical normalisation and proved the local theorem (S5.3), exact sharp cuts, reference-relative Schur formulae and conditional cofinal detector consequences, with the global signed estimate explicitly open.

## Detector: why a global lower floor would suffice

The source constructs compactly supported exactly pole-neutral odd tests whose transforms localise around a hypothetical off-real zero quartet. An illustrative entire transform is

$$
F_\tau(z)=(z^2+1/4)
\left(e^{-\tau(z-\omega)^2}-e^{-\tau(z+\omega)^2}\right).
\tag{S5.8}\label{eq:S5.8}
$$

The prefactor cancels the two polar values; the odd Gaussian difference selects a nonzero carrier. A generic-carrier argument avoids score ties without assuming a rightmost off-line zero. On a phase-aligned subsequence the zero spectral term becomes exponentially negative, while compactification errors and test norms are controlled. The resulting conditional upper bound on the bottom Rayleigh quotient is of the form

$$
\nu_0(b)\le -e^{cb}
\quad\text{for every sufficiently large }b,
\tag{S5.9}\label{eq:S5.9}
$$

with a zero-dependent $c>0$. Therefore any fully physical cofinal lower sequence satisfying (S1.3) would contradict such a zero. The detector is **not** the missing signed-prime estimate.

# Canonical moments, finite arithmetic and alternative spectral geometries

## The compact Hausdorff and Jacobi/CMV route

The logarithmic derivative of the even xi descent can be mapped to positive-measure questions on a compact interval and then to Jacobi or unitary CMV models. The attraction is structural: a positive measure provides a spectral representation without checking every zero individually. The limitation is equally sharp: obtaining positive moments of an auxiliary completion does not establish positivity of the **actual** xi-derived infinite sequence.

The archived F21 finite tests reached deeper orders than some later September unshifted Hankel computations, but used a different normalisation and criterion. Their ranks are not interchangeable. The recorded initial segments are valuable diagnostics and algebraic input; an all-rank theorem needs a positive fresh moment at every stage.

## Fixed-base prime windows and F39--F166

In the fixed-base branch $a=30$ is a right-half-plane base, *not* a physical aperture or a Jensen degree. An explicit finite-prime Hausdorff-depth criterion and associated canonical wall were developed. The qd/Christoffel/Darboux relay encodes the next-front update, but still needs actual-index regeneration, retention, and landing in the correct scalar coordinates. The later F166.11--.18 notes sharpen low-branch amplitude, Borel response and activation residuals. They do not automatically establish the cofinal positive continuation.

A useful exact transport identity in this class can have the generic form

$$
\epsilon_{\mathrm{fine}}
=\epsilon_{\mathrm{coarse}}
-r^*S^{-1}r,
\tag{S6.1}\label{eq:S6.1}
$$

where $S$ is the exact post-short detail denominator. The formula is universal block linear algebra; the mathematical challenge is to bound the actual source $r$ in the same physical metric as $S$.

## Native finite sections, W200 and the continuum

At mesh $D=\log2/2048$ and terminal index $H=6144$, the historical numerical record gives a preconditioned interval enclosure

$$
\|R\mathcal M_H^{\mathrm{exact}}R^*-I\|_\infty
\le0.74042452559637051<1.
\tag{S6.2}\label{eq:S6.2}
$$

This establishes positivity of its *particular finite matrix* if the archived interval premises and arithmetic are reproduced faithfully. The source reports a complete computational receipt, but this synthesis has not rerun all its original generators. Later continuum tests discovered extraordinarily soft directions missed by finite meshes. Hence one cannot promote (S6.2) to full Weil-form positivity without a proved continuum tail estimate.

A separate fixed-window W200 theorem, originally due to Vincent Liu, reports a bound of the form

$$
Q_W(f)\ge2^{-151}\|f\|^2,
\qquad \operatorname{supp}f\subset(-1,1),
\tag{S6.3}\label{eq:S6.3}
$$

in its declared normalisation. Later W200-related variants have different constants and hypotheses; one should not amalgamate their numerical claims. The attempted direct splice to a broader three-gate induction failed at concrete collar stages. Fixed support is not cofinal support.

## Weyl, Liv\v{s}ic, Pontryagin and the spectral-realisation reserve

The Weyl-function route asks for a positive self-adjoint or canonical-system realisation of the actual xi data. For a self-adjoint $J$ and vector $e$, the familiar resolvent

$$
m(z)=\langle e,(J-zI)^{-1}e\rangle
\tag{S6.4}\label{eq:S6.4}
$$

has a positive spectral-measure representation. Finite Liv\v{s}ic and Schur identities and rank-one mixed resolvent formulas are exact, but the all-scale identification with the actual xi object and its positive Hamiltonian remain unproved. Generalised-Schur/Pontryagin methods keep track of finite negative indices instead of simply assuming they vanish. The two approaches are complementary: they describe possible structure, not a completed Xi-specific positivity argument.

## Jump-process and gauge alternatives

The killed-jump representation regards the complete raw arithmetic as a generator plus a scalar shift. Its path occupation record preserves order-sensitive prime interactions that may disappear from a commutative moment reduction. Gauge and Cayley transformations can simplify source coordinates but do not change the physical sign of an operator; a nonunitary basis change requires transporting the metric $G=S^*S$. These ideas are recorded because they identify otherwise hidden terms, not because they independently establish a spectral gap.

# October's signed-prime and complete-theta programme {#octobers-signed-prime-and-complete-theta-programme}

## A finite ordinary-prime statistic with a square-summable remainder

The October manuscript's chief result is a source-claimed unconditional decomposition for a pole-neutral Chebyshev--Laguerre statistic $U_m$ of the form

$$
U_m+h_m=\kappa+r_m,\qquad \kappa<0,\qquad (r_m)_{m\ge1}\in\ell^2.
\tag{S7.1}\label{eq:S7.1}
$$

Here $h_m$ is a reciprocal-zero diagonal, $U_m$ is a finite ordinary-prime sum with a moving explicit cutoff, and $\kappa$ includes a necessary prime-square endpoint correction. The cutoff, kernel and prime-square constant are displayed in the [atlas chapter on signed primes](#atlas-primes) and defined in full in the October paper [D3]. Several boundedness, quadratic-average and eventual-sign tests are asserted to be RH-equivalent **given the proved decomposition**. This is an economical arithmetic reduction, not a proof that its strong signed inequality holds unconditionally.

A related two-prime analysis isolates prime-diagonal energy

$$
E_{\mathrm{diag}}(m)
=\frac{2768896}{14348907}\left(m+\frac12\right)
+D_\infty+o(1),
\tag{S7.2}\label{eq:S7.2}
$$

where the signed off-diagonal terms must cancel this linear growth to reach the bounded mean-square target. This division into an exact diagonal and an unpaid signed interaction is one of the October programme's most important methodological gains. Replacing the off-diagonal by an unsigned bound generally loses the needed rate.

## Complete theta source and the heat discriminant

The same manuscript develops heat-flow and harmonic discriminant identities for the complete theta source and records eventual fixed-degree radial positivity and conditional cofinal continuation criteria. It includes a coupled-saddle result for a specified growing radial window, source perturbations with nonreal quartets, and numerical certificates. The mathematical boundary is strict: a generic positive heat model, a small number of coefficient moments, or a diagonal analytic estimate does not supply the exact source pairing required to control all actual xi roots.

The October programme is especially important as an *independent* attempt: its signed arithmetic theorem obligations were formulated before the November external formal proof. After that external proof, conditional consequences of RH become available, but the original unconditional derivation remains a distinct research problem. The manuscript's internal proofs and code deserve independent specialist verification, especially its moving cutoffs, square-endpoint term, and claimed norm of the sector remainder.

# November's Gaussian two-probe and the three-prime-moment theorem

## Pole-neutral two-probe observables

At a real carrier $a>0$ and width $k>0$, consider

$$
F_0(z;k,a)=(z^2+1/4)
\bigl(e^{-k(z-a)^2}-e^{-k(z+a)^2}\bigr),
\qquad F_1(z;k,a)=\frac{z^2-a^2}{2a}F_0(z;k,a).
\tag{S8.1}\label{eq:S8.1}
$$

The prefactor is the exact pole-neutralising filter. The pair distinguishes a hypothetical nonreal zero quartet despite possible carrier phase cancellation; choosing a rational carrier in an open successful interval avoids any need for a rightmost zero. The complete zero spectral form contains a signed quadratic response, not a sum of absolute squares outside RH. Its decisive role is to produce a *witness*, not to prove an unconditional arithmetic upper bound.

The November consolidation corrects several earlier shortcuts: signs lost by scalar averaging; changed Schur denominators; ordinary positive Gram matrices used instead of the complete signed metric; source norms after noncommuting projections; and injectivity confused with absence of a zero mode in a completed space.

## Exactly three actual-prime moments

A particularly useful compression chooses $\widetilde F_1(z)=z^2F_0(z)$ and the correlation function $C_{00}(t)$ of the underlying real-space test. Define

$$
b_j(a,k)=\sum_{p}\frac{\log p}{\sqrt p}
\left[(-\partial_t^2)^j C_{00}(t)\right]_{t=\log p},
\qquad j=0,1,2,
\tag{S8.2}\label{eq:S8.2}
$$

and

$$
\widetilde M(a,k)=\begin{pmatrix}b_0&b_1\\b_1&b_2\end{pmatrix}.
\tag{S8.3}\label{eq:S8.3}
$$

The change of probe basis

$$
T_a=\begin{pmatrix}1&0\\a^2&2a\end{pmatrix},
\qquad\widetilde M=T_a M_1 T_a^T
\tag{S8.4}\label{eq:S8.4}
$$

is invertible when $a>0$. Thus the first-prime quadratic criterion depends on only three numerical functions. For a hypothetical off-line quartet $z=x+iy$ and $w=(1,z^2)^T$, its single-quartet matrix is

$$
H_z=4m_z\Re(F_0(z)^2ww^T),\qquad
\det H_z=-64m_z^2|F_0(z)|^4x^2y^2<0.
\tag{S8.5}\label{eq:S8.5}
$$

This exact negative determinant exposes a suitable direction for detection. In the full formula, other zero contributions and arithmetic corrections must still be bounded with uniformity. The source reports that the complete proper-prime-power contribution has an unconditional bounded budget at fixed carrier intervals, whereas the first-prime *signed* estimate is the open arithmetic heart of an independent route.

The resulting RH-equivalent criterion can be written with the elementary largest-eigenvalue expression

$$
2\lambda_{\max}(\widetilde M)
=b_0+b_2+\sqrt{(b_0-b_2)^2+4b_1^2}.
\tag{S8.6}\label{eq:S8.6}
$$

The source states that subexponential upper growth at each rational carrier forces RH; under the external RH theorem the same upper bound is a consequence. To present this as an **independent** proof would require establishing the bound *without* importing RH or an equivalent arithmetic assertion.

## Prime powers, Möbius divisors, and conditional completion

The proper-power sector is much easier than the first-prime sector. Gaussian derivative estimates and a classical Chebyshev bound yield an unconditional $O_I(1)$ contribution to the simplified matrix on each compact positive carrier interval $I$. This is sufficient for exponential-scale detection and does not use the hard arithmetic theorem. A stronger physical-Gram calculation is retained in the source audit; the two normalisations should not be confused.

The November Möbius--Gaussian tail theorem uses the external RH implication $M(x)=\sum_{n\le x}\mu(n)=O_\varepsilon(x^{1/2+\varepsilon})$. Under its documented contour and compact-carrier conditions, for $D_\lambda(k)=\lfloor e^{\lambda k}\rfloor$ it obtains the conditional estimate

$$
\sup_{a\in I}|T_{>D_\lambda(k)}(a,k)|
\ll_{I,\lambda,\varepsilon}k^{-1/2}
\exp\!\left[\left(-\frac{\lambda^2}{8}
+\lambda\varepsilon\right)k\right].
\tag{S8.7}\label{eq:S8.7}
$$

This is a useful analytic consequence of *external* RH. The zero-free half-plane needed to move the contour is precisely where the difficult arithmetic information enters. The tail estimate cannot be detached from that dependency and advertised as an independent proof.

## Rank-two Fourier displacement and the compressed defect

The exact finite Fourier identity has the form

$$
[X,H]=c(ah^*-ha^*).
\tag{S8.8}\label{eq:S8.8}
$$

A noncommuting orthogonal projection $P$ produces a correction, not the same identity without change. If $Q=I-P$, $A=PXP$, $H_P=PHP$, $B=PXQ$, and $C=PHQ$, then

$$
[A,H_P]
=c(a_Ph_P^*-h_Pa_P^*)
+\underbrace{(CB^*-BC^*)}_{E}.
\tag{S8.9}\label{eq:S8.9}
$$

The defect $E$ obeys $\operatorname{rank}E\le2\operatorname{rank}B$ and $\|E\|\le2\|B\|\|C\|$. Its appearance explains why an apparently elegant rank-two inverse-pole formula can fail after passing to a physical prolate or source-selected subspace. The November paper derives the corrected inverse identity and checks a rational counterexample; it leaves quantitative control of $E$ in expanding physical spaces as an open issue.

## The twenty-one directions and microcarrier mosaics

The November ledger also retains a finite twenty-one-direction phase frame and a smaller three-carrier alternative for detecting off-line quartets without a vulnerable fixed phase. These are *detector* constructions. The three-rational-microcarrier mosaic and proposed recurrent-strip bootstrap may sharpen the search for an arithmetic lemma, but the claimed $3/4$ zero-free theorem and the full RH result were not established in those notes. The resulting research priority is to estimate the complete first-prime signed quadratic form simultaneously at the carriers and in the same physical normalisation.

# The external Alpöge--Claude theorem and its proper role

## What changed on 20--21 November 2026

On 20 November 2026, Levent Alpöge announced a Lean formalisation of RH developed with Claude. On 21 November the Lean and Mathlib communities published a joint statement certifying that the released code proves the correct Mathlib RH statement and that their stipulated kernel and statement checks had succeeded [E1]. Rubinstein's public verification page reports compilation and kernel replay of the formal development [E2]. These are **external results**. Their public certification status is not conferred on Dumas's independently written reformulations.

The initial human-readable accounts are not a substitute for the 17-million-line formal library. Rubinstein's 164-page working exposition explicitly imports the arithmetic inequality (M) from that development; its own text does not establish (M) from the stated classical inputs [E2]. Other contemporary expositions simplify certain downstream analytic or character-comparison steps under the deep arithmetic hypotheses. None of those simplifications should be mistaken for a wholly independent proof of the formal theorem's hardest arithmetic component.

## The arithmetic window estimate used by the new papers

Define the centred von Mangoldt ramp

$$
G(x)=\sum_{n\le x}\Lambda(n)\left(\frac{x}{n}-1\right)
-x\log x+(1+\gamma)x,
\qquad x\ge1.
\tag{S9.1}\label{eq:S9.1}
$$

The external arithmetic construction supplies a window statement denoted (W) in the 22--23 November Dumas manuscripts:

$$
\begin{gathered}
\forall\,\eta>0\quad\exists\,K_\eta>0\quad\forall\,Y_0\ge1\quad\exists\,Y\ge Y_0:\\
G(x)\le K_\eta x^{1/2+\eta}\qquad\text{for every }x\in[Y,Y^{3/2}].
\end{gathered}
\tag{S9.2}\label{eq:S9.2}
$$

The quantifiers matter: one common $Y$ must work uniformly for all $x$ in its power window, and the statement must hold along unboundedly many windows. The available human-readable deduction uses character twists, common-scale comparisons and the deep arithmetic bound (M). The 23 November limited audit checked this logic against Rubinstein's exposition but did not independently compile the complete formal development to verify every paraphrased intermediate statement.

Under ordinary RH and the explicit formula, the stronger bound $|G(x)|\ll x^{1/2}$ follows. Therefore (W) is itself RH-equivalent *given the analytic zero-growth arguments below*. It is not a mathematically weaker, independently proved elementary assumption.

# One-sided prime sums and an exact zero-growth law

## An absolutely convergent explicit formula

Let $\mathcal Z$ be the set of distinct nontrivial zeta zeros, and $m_\rho$ the multiplicity of $\rho$. The 22 November paper derives an explicit formula with absolutely summable zero coefficients:

$$
G(x)=\log(2\pi)+\sum_{\rho}c_\rho x^\rho
-\sum_{j\ge1}\frac{x^{-2j}}{2j(2j+1)},
\qquad c_\rho=\frac{m_\rho}{\rho(1-\rho)}.
\tag{S10.1}\label{eq:S10.1}
$$

The elementary absolute convergence of the zero weights follows from the classical zero-counting bound; this smoothed formula is substantially easier to manipulate than a sharp explicit formula for $\psi(x)$. The paper's audit independently checked the Mellin-transform algebra, a high-precision numerical identity and sample values, but did not supply specialist peer review of every infinite-series interchange.

Define $\Theta=\sup_\rho\Re\rho$ and, for $\lambda>1$ and $\theta>0$,

$$
M_\theta^\pm(Y,\lambda)
=\int_Y^{Y^\lambda}[\pm G(x)]_+x^{-\theta}\frac{dx}{x}.
\tag{S10.2}\label{eq:S10.2}
$$

The paper's principal analytic assertion is

$$
\boxed{\quad
\lim_{Y\to\infty}
\frac{\log\bigl(1+M_\theta^\pm(Y,\lambda)\bigr)}{\log Y}
=\lambda(\Theta-\theta)_+.
\quad}
\tag{S10.3}\label{eq:S10.3}
$$

The two signs are separate statements. The Gaussian frequency-selection argument isolates a nonreal-frequency zero contribution against the zero-frequency average and shows growth on *every fixed power interval*, without assuming that the supremum $\Theta$ is attained. A technical audit dated 23 November found no decisive internal error, re-ran finite checks and identified the external dependency. That is encouraging but not a formal verification or comprehensive priority assessment [D9].

## A finite integer statistic

At $\theta=1/2$, $Y=4^k$ and $Y^\lambda=8^k$, the paper defines

$$
A_k=\sum_{n=4^k}^{8^k}
\frac{[G(n)]_+}{n^{3/2}},
\qquad
\Theta=\frac12+
\lim_{k\to\infty}\frac{\log(1+A_k)}{3k\log2}.
\tag{S10.4}\label{eq:S10.4}
$$

Consequently, if the analytic growth theorem is correct, $\log(1+A_k)=o(k)$ along *one unbounded subsequence* would imply RH. The finite numerical enclosures $A_1,\ldots,A_5$ do **not** establish that asymptotic condition. The external arithmetic window (W) provides a short conditional deduction of the zero-free conclusion.

The strongest independent content is the exact analytic growth law (S10.3), not the final implication using (W). Any publication should compare that law carefully against classical oscillation and one-sided prime-sum literature, including Kaczorowski--Pintz [E4].

# A least-common-multiple formulation of RH {#a-least-common-multiple-formulation-of-rh}

## A precise integer statistic

Let $\Lambda$ denote the von Mangoldt function, let $\psi(x)=\sum_{m\le x}\Lambda(m)$, and define the running product of least common multiples by

$$
L_N=\prod_{j=1}^{N-1}\operatorname{lcm}(1,2,\ldots,j),
\qquad L_1=1.
\tag{S11.1}\label{eq:S11.1}
$$

**All logarithms in this chapter are natural**, except when explicitly indicated by $\log_2$. The contribution of a prime $p$ to the $j$th lcm is $p^{\lfloor\log_p j\rfloor}$; equivalently,

$$
\log\operatorname{lcm}(1,\ldots,j)
=\sum_{p^a\le j}\log p=\sum_{m\le j}\Lambda(m)=\psi(j).
$$

Interchanging the finite sums gives the exact identity

$$
\begin{aligned}
\log L_N
 &=\sum_{j=1}^{N-1}\psi(j)
 =\sum_{m=1}^{N-1}\Lambda(m)\sum_{j=m}^{N-1}1\\
 &=\sum_{m<N}(N-m)\Lambda(m)
 =\sum_{m\le N}(N-m)\Lambda(m)=:R(N).
\end{aligned}
\tag{S11.2}\label{eq:S11.2}
$$

The notation $m\le N$ and $m<N$ is interchangeable in the last expression **only because the term with $m=N$ is zero**. For real $x>0$ we use $R(x)=\sum_{m\le x}(x-m)\Lambda(m)$.

The source manuscript dated 23 November 2026 states the following proposed equivalence:

$$
\boxed{\qquad
\mathrm{RH}\quad\Longleftrightarrow\quad
L_{n^2}^{\,4}\le 2^{n^3}L_{2n^2}
\quad\text{for every integer }n\ge1.
\qquad}
\tag{S11.3}\label{eq:S11.3}
$$

It also states that the inequality for all sufficiently large $n$ suffices. The key normalization is

$$
B(x)=\frac{4R(x)-R(2x)}{x},
\qquad B(n^2)\le n\log2.
\tag{S11.4}\label{eq:S11.4}
$$

Here $x=n^2$ yields $x^{3/2}=n^3$. The integer relation is an exact rearrangement of (S11.3), **not** an independent proof of its infinite equivalence to RH. The latter is argued via an explicit formula and Mellin positivity in [D8]; the details and their proof dependencies are expanded below for auditing. This monograph does not independently certify those arguments.

## The explicit-formula coefficient and the constant $C_*$

For $\ell=\log(2\pi)$ and Euler's constant $\gamma$, the source defines

$$
G(x)=\sum_{m\le x}\Lambda(m)\left(\frac{x}{m}-1\right)
       -x\log x+(1+\gamma)x.
\tag{S11.5}\label{eq:S11.5}
$$

With $\mathcal Z$ the set of distinct nontrivial zeta zeros and $m_\rho$ their multiplicities, the manuscript derives the absolutely convergent formulas

$$
\begin{aligned}
G(x)&=\ell+\sum_{\rho\in\mathcal Z}
 \frac{m_\rho x^\rho}{\rho(1-\rho)}
 -\sum_{j\ge1}\frac{x^{-2j}}{2j(2j+1)},\\[2pt]
R(x)&=\frac{x^2}{2}-\ell x+b
 -\sum_{\rho\in\mathcal Z}\frac{m_\rho x^{1+\rho}}{\rho(1+\rho)}
 -\sum_{j\ge1}\frac{x^{1-2j}}{2j(2j-1)}.
\end{aligned}
\tag{S11.6}\label{eq:S11.6}
$$

The convergence and normalization arguments are in [D8] and require an independent specialist check before the equivalence is treated as established beyond the source. The constant $b$ in that normalization is

$$
b=\ell-\frac12+\log2+
\sum_{\rho\in\mathcal Z}\frac{m_\rho}{\rho(1+\rho)}.
\tag{S11.7}\label{eq:S11.7}
$$

**The previously compressed $G(1)\to C_*$ calculation.** Under RH,
$1-\rho=\overline\rho$ and $c_\rho=m_\rho/|\rho|^2>0$.
Since the prime sum is empty at $x=1$, we have $G(1)=1+\gamma$.
Also, by partial fractions,

$$
\sum_{j\ge1}\frac1{2j(2j+1)}
=\sum_{j\ge1}\left(\frac1{2j}-\frac1{2j+1}\right)
=1-\log2.
$$

Putting $x=1$ in (S11.6) thus yields, with no omitted step,

$$
\begin{aligned}
1+\gamma
 &=\ell+\sum_\rho c_\rho-(1-\log2),\\
C_*:=\sum_\rho c_\rho
 &=2+\gamma-\ell-\log2
 =2+\gamma-\log(4\pi)
 \approx0.0461914179.
\end{aligned}
\tag{S11.8}\label{eq:S11.8}
$$

A referee does not need to trust the decimal approximation for the forward bound: using the elementary rational enclosures $\gamma<0.5774$ and $\log(4\pi)>2.5305$ gives

$$
0<C_*<2+0.5774-2.5305=0.0469<0.047.
\tag{S11.9}\label{eq:S11.9}
$$

The source gives rational checks, reproduced by the integer-check program in this edition, based on $\gamma<H_{4096}-\log4096$ and the series $\log v=2\sum_{k\ge0}q^{2k+1}/(2k+1)$ for $q=(v-1)/(v+1)$. The displayed decimals and this rational majorant are separate statements; a certified implementation should retain its outward rounding and exact input bounds.

Under RH the coefficients in (S11.6) have total absolute mass at most $C_*$. In $4R(x)-R(2x)$ the quadratic main term vanishes, and the sum of the absolute values of all nontrivial-zero contributions is at most $(4+2\sqrt2)C_*x^{3/2}$. The elementary and trivial-zero terms have the favorable sign for $x\ge4$ in the source's normalization. In particular,

$$
\begin{aligned}
4R(x)-R(2x)
 &\le (4+2\sqrt2)C_*x^{3/2}\\
 &<6.83(0.047)x^{3/2}
 <\frac{\log2}{2}\,x^{3/2}
 \quad(x\ge4),
\end{aligned}
\tag{S11.10}\label{eq:S11.10}
$$

where $\log2>0.69$ suffices for the last inequality. With $x=n^2$ this yields (S11.3) for $n\ge2$; the $n=1$ case is immediate. This is a **conditional RH-to-inequality implication**, not an unconditional bound.

## The exact ramp identity and Mellin converse

For $m\le x$, the elementary integral that relates the two smoothed von Mangoldt sums is

$$
\begin{aligned}
2\int_m^x\left(\frac{t}{m}-1\right)\,dt
 &=\frac{(x-m)^2}{m},\\
x\left(\frac{x}{m}-1\right)
 -\frac{(x-m)^2}{m}&=x-m.
\end{aligned}
\tag{S11.11}\label{eq:S11.11}
$$

Thus if $S(x)=G(x)+x\log x-(1+\gamma)x=\sum_{m\le x}\Lambda(m)(x/m-1)$, termwise finite integration gives

$$
R(x)=xS(x)-2\int_1^x S(t)\,dt.
\tag{S11.12}\label{eq:S11.12}
$$

This accounts for the $R$ formula in (S11.6); it does not require silently replacing the ramp by a sharp prime sum.

For $\Re s>1$, the Mellin transform of $B$ in (S11.4) is, by integrating the ramps before summing,

$$
\begin{aligned}
\int_0^\infty\frac{R(ax)}{x}x^{-s}\frac{dx}{x}
 &=\frac{a^{s+1}}{s(s+1)}\sum_{m\ge1}\frac{\Lambda(m)}{m^s},\\
\mathcal MB(s):=\int_0^\infty B(x)x^{-s}\frac{dx}{x}
 &=-\frac{\zeta'(s)}{\zeta(s)}\,
 \frac{4-2^{s+1}}{s(s+1)}.
\end{aligned}
\tag{S11.13}\label{eq:S11.13}
$$

The first identity is stated for $a>0$; the second follows with $a=1,2$ and $\sum_m\Lambda(m)m^{-s}=-\zeta'(s)/\zeta(s)$. At $s=1$ the simple pole of $-\zeta'/\zeta$ is cancelled by $4-2^{s+1}$; for a nontrivial zero $\rho$ with $1/2<\Re\rho<1$, this multiplier is nonzero since

$$
\left|2^{1+\rho}\right|=2^{1+\Re\rho}<4.
\tag{S11.14}\label{eq:S11.14}
$$

**Why positivity enters.** If (S11.3) holds eventually, the source bounds the derivative of $R(ax)/x$ by $O_a(\log(2x))$ between consecutive squares. Consequently $B(x)\le C\sqrt x\log(2x)$ for all large real $x$. For every $1/2<\sigma_0<1$ choose $K$ so that $H(x)=Kx^{\sigma_0}-B(x)\ge0$ for all $x\ge1$. A nonnegative Mellin kernel has a singularity at its finite real abscissa of convergence (the Landau positivity principle); the proof in [D8] uses nonnegative Taylor coefficients and monotone convergence. Comparing its Mellin transform with (S11.13), which has no real poles for $\sigma_0<s\le1$, forces the abscissa to be at most $\sigma_0$. Any zeta zero with $\Re\rho>\sigma_0$ would then contradict (S11.13) and (S11.14). Letting $\sigma_0\downarrow1/2$ and using zeta functional-equation symmetry gives the claimed converse.

**Audit qualification.** This is an explanatory reconstruction of the source's converse, **not an independently refereed proof**. The precise analytic continuation across the Mellin abscissa, sign and regularity assumptions on $H$, and zero multiplicities remain priority review targets. The source's finite integer tests do not validate those global steps.

## A cubic filter supported on a finite prime-power window

Let $(Df)(x)=f(2x)$ and define

$$
Q(z)=(z-1)(z-2)(z-4)=z^3-7z^2+14z-8.
\tag{S11.15}\label{eq:S11.15}
$$

The associated integer ratio is

$$
V_n=\frac{L_{8n^2}\,L_{2n^2}^{\,14}}{L_{4n^2}^{\,7}L_{n^2}^{\,8}},
\qquad
\log V_n=Q(D)R(n^2).
\tag{S11.16}\label{eq:S11.16}
$$

For a single prime-power location $m$, expand each ramp $(ax-m)_+$ in $R(ax)$ **before** estimating. This gives $Q(D)R(x)=\sum_{m\ge1}\Lambda(m)w_x(m)$ with

$$
w_x(m)=\begin{cases}
  0,&m\le x,\\
  8(x-m),&x<m\le2x,\\
  6m-20x,&2x<m\le4x,\\
  8x-m,&4x<m\le8x,\\
  0,&m>8x.
\end{cases}
\tag{S11.17}\label{eq:S11.17}
$$

For example, at $m\le x$ the weight equals
$(8x-m)-7(4x-m)+14(2x-m)-8(x-m)=0$; the other rows follow by retaining only the ramps that are active in that interval. This proves the **exact finite-support identity**: $V_n$ depends only on prime powers in $(n^2,8n^2)$. The source goes on to state $\mathrm{RH}\Longleftrightarrow V_n\le 2^{9n^3}$ for every integer $n\ge2$; that infinite equivalence is source-proved but still requires the independent analytic audit described above.

The polynomial $Q$ is a **dilation filter**, not the cocircuit difference of original Paper III, the Airy cubic normal form, or a third-order differential operator. Their shared motif is cancellation, not mathematical identity.

## Gaussian growth law: complete notation and its separate dependency

The same source treats a real spectral sum

$$
F(x)=\sum_{\rho\in\mathcal Z}a_\rho x^\rho+O(1),
\qquad \sum_\rho|a_\rho|<\infty,
\qquad a_{\bar\rho}=\overline{a_\rho},
\tag{S11.18}\label{eq:S11.18}
$$

under the spectral hypotheses of [D8]. Each distinct nontrivial zero has one combined nonzero coefficient, with $0<\Re\rho<1$, $\Im\rho\ne0$, conjugation symmetry and local finiteness. The function $F$ is real and locally integrable on $[1,\infty)$, and the bounded remainder is uniform for $x\ge1$. For $0<r<\Theta:=\sup_\rho\Re\rho$, put $t_\rho=\Im\rho$ and $b_\rho=\Re\rho-r$. Writing $x=e^t$ and multiplying by $e^{-rt}$ yields a sum of exponentials. A Gaussian density centered at $T$ and having variance $vT$ produces the score

$$
H_\rho(u)=b_\rho+
 \frac v2\left[b_\rho^{\,2}-(t_\rho-u)^2\right],
\qquad
H(u)=\max_\rho H_\rho(u).
\tag{S11.19}\label{eq:S11.19}
$$

For the small variance parameter $v>0$ chosen in the source, a frequency $u$ is selected with $H_{\rho_*}(u)>\max\{0,H(0)\}$, so that **one index $\rho_*$ uniquely maximizes** the score and every competing zero satisfies $H_\rho(u)\le H_{\rho_*}(u)-\delta$ for some gap $\delta>0$. Here $\rho_*$ is a selected zero, **not** a zero assumed to attain $\Theta$. This explicit notation prevents the commonly seen plain-text/OCR loss of the subscript or the gap symbol. The Gaussian modulation then compares the size of a nonzero-frequency integral with its zero-frequency average and produces lower bounds for **both** positive and negative parts on every fixed power interval. Under the hypotheses of [D8], its claimed exponent law is

$$
\lim_{Y\to\infty}
\frac{\log\!\left(1+\int_Y^{Y^\lambda}[\pm F(x)]_+x^{-\theta}\frac{dx}{x}\right)}{\log Y}
=\lambda(\Theta-\theta)_+,
\quad \lambda>1,\ \theta>0.
\tag{S11.20}\label{eq:S11.20}
$$

The signs $+$ and $-$ are two separate assertions, not a cancellation of an unsigned estimate. The complete analytic proof, including the Gaussian tail bound, appears in the original LCM and one-sided-prime-sums manuscripts. The present volume explains the choices of $\rho_*$ and $\delta$ but does not replace a specialist check of the infinite spectral sum.

## Numerical example, computational provenance, and source boundaries

The original paper records $L_4=12$, $L_8=217\,728\,000$ and
$L_4^4/L_8=1/10\,500$, and supplies the $n=42$ ratio bound
$2^{123}<L_{42^2}^{\,4}/L_{2\cdot42^2}<2^{124}$.
The selected exact regression script in the companion archive checks the lcm/prime-power identity for $1\le N\le34$ and the finite inequality for $1\le n\le10$. These computations validate **particular finite instances**, not the universal inequality, the Mellin argument, or the Gaussian growth law.

The original standalone article describes other directed-rounding numerical enclosures in its computational supplement. They should be checked against their original scripts, environments, precision policies, and source hashes before their precision is cited as independently reproduced. The source archive explicitly distinguishes archived verification receipts from computations rerun for the present monograph.

**Typographical audit.** The most conspicuous missing mathematical glyphs reported from plain-text rendering of the seven-page PDF (such as $\Im\rho$, starred zero labels, and $\delta$) were **not reproduced as omissions in the TeX source**. They are primarily PDF text-extraction/OCR issues. The revised monograph does, however, spell out every crucial index, ramp and constant bound in typeset mathematics to prevent those ambiguities from propagating to secondary expositions. No original historical file has been silently overwritten.

**External arithmetic input (W).** The alternative short deduction of RH assumes that, for each $\eta>0$, arbitrarily large $Y$ admit a fixed-interval estimate $G(x)\le K_\eta x^{1/2+\eta}$ simultaneously for $Y\le x\le Y^{3/2}$. This is an **imported** arithmetic result from the Alpöge--Claude development and its exposition; it is not proved in the LCM manuscript. Its use in combination with the growth law is a conditional explanatory bridge, not an independent Dumas proof of RH.

# The cubic, third-order, and three-port constructions: a concordance

A recurring historical risk is to declare that two formulas have the same content because each contains a cubic polynomial or three distinguished coordinates. This chapter records the distinctions and the few real conceptual connections.

## Paper III: fourth-order cocircuit difference

Equation (S3.4) has the factor $(1-Y/X)^3(1-Z/Y)$. It annihilates low polynomial/character moments in a finite flagged combinatorial structure. Its coefficient support and finite-chain endpoints belong to Jacobi--Trudi and Brion algebra. What survives is an exact finite difference and forced-root divisor.

## Paper V: third-order minors in the boundary ladder

Equation (S3.6) expresses a difference of compensated ratios by a $3\times3$ minor $\Delta_{1,j}$. The relevant positivity concerns the *signs of adjacent finite-rank minors*. It is not a third-order differential operator and does not automatically imply total positivity in the actual infinite coefficient sequence.

## Paper VII: odd centred cubic perturbation

For the symmetric centred heat polynomial, odd centred modes change sign under the involution $t\mapsto-t$ and root reversal. For even degree, this forces the first derivative of the central log gap to vanish at $t=0$. The cubic is a *perturbation mode*. This statement alone neither ensures a globally positive gap nor controls a finite cubic deformation of arbitrary amplitude.

## Papers VIII--IX: an Airy cubic

Near coalescing saddles, a third-degree phase is the universal local normal form; an Airy model gives $d^{-2/3}$ edge scaling. Its mathematical legitimacy requires a specified analytic contour, a nonzero cubic coefficient, control of all competing saddles, and two-sided overlap errors. The term "cubic" is universal asymptotic geometry, not an arithmetic cancellation identity.

## The cubical/wedge protection of the F166 relay

The mature fixed-base relay used a protected cubic-wedge parameter range and later corrected its off-resonance chart. Exact finite update rules survive. They must not be extended to unprotected physical landing indices without a new amplitude/retention theorem. The similar words *cubic*, *cube* and *third-order* conceal different domains and operators.

## A three-port Redheffer edge

In the old terminating-edge reduction, two pole modes (one positive, one negative in the real pole sector) and a border-completion port motivate a $3\times3$ effective matrix. That is a boundary *channel count*, not a statement that the entire signed arithmetic operator has rank three. Exact elimination still introduces a complement Schur debt.

## The four-scale dilation cubic

The four-scale $Q(D)$ filter (S11.15), with weights in (S11.17), is a polynomial in the **scaling operator** $Df(x)=f(2x)$. It annihilates chosen smooth main terms and low-scale prime contributions. Its three roots should not be equated with the Airy phase, the finite cocircuit derivative, or the three-port Schur reduction.

## A legitimate cross-era lesson

All these mechanisms share only a careful methodological principle: remove forced or low-order structure **exactly before estimating the remainder**. The repeated success of this principle motivates source-specific cancellations; it does **not** prove an intertwining operator connecting unrelated constructions. A future unification would require a map preserving (1) the exact arithmetic object, (2) the form domain, (3) the metric, (4) the cutoff and (5) the signs of the completed remainder.

# A register of decisive corrections and failed proof transfers

The programme's scientific value is partly in its explicit falsification record. The following entries are not rhetorical caveats: each identifies a specific false implication or an unproved dependency whose omission could manufacture a spurious RH proof.

| ID | Proposed shortcut | Why it fails or remains open | Valid residue |
|:---|:---|:---|:---|
| F01 | Finite Jensen certificates imply global hyperbolicity | A finite set cannot cover unbounded degree/shift without a uniform theorem | Exact local root/Wronskian certificates |
| F02 | Seven named Paper IX regions imply a no-gap cover | At least one region lacked a strict, compatible proof-grade contract | Region-specific asymptotics and audit requirements |
| F03 | A huge verified zero height closes the $t\downarrow0$ horn | For any finite height, $\exp(C/t)$ eventually exceeds the finite cutoff | Need genuine uniform small-$t$ analysis |
| F04 | A positive finite mesh controls the continuum Weil form | Soft continuum directions may not be represented or bounded by the mesh | Finite interval-positive matrix theorem |
| F05 | W200 fixed-window positivity iterates automatically | Actual cross-collar Schur debt is not covered; specific splice attempts failed | Fixed-window theorem with attribution |
| F06 | A two-port description per prime gives one common two-dimensional range | Port maps may have different images; compression adds transverse source | Exact source-range criteria when actually proved |
| F07 | Same-Gram inverse cost bounds a different physical denominator | $BB^*$ need not be comparable to post-short $D$ | Same-Gram Woodbury identity |
| F08 | A positive future compression stays positive after old elimination | A Schur complement subtracts a nonnegative inverse term | Complete block recursion |
| F09 | An operator norm on ordinary $L^2$ suffices for the Weil form | High-frequency countertests have large raw cross, and Archimedean energy matters | Weighted observable-specific funding |
| F10 | Positive reference plus small kernel error controls physical sign | Different metrics and completions can hide negative spectrum | Reference identity and completed-domain audit |
| F11 | Injectivity of the compact $L^2$ operator excludes completion zero modes | A zero mode may arise in the form completion | Need closability/domain proof |
| F12 | Rank-two commutator survives an arbitrary projection unchanged | $[PXP,PHP]$ picks up $CB^*-BC^*$ | Corrected displacement identity (S8.9) |
| F13 | A nonreal zero must maximise real part globally | A supremum need not be attained | Frequency-local score maximisation |
| F14 | Scalar averaging detects every quartet | Oscillatory sign and phase cancellation can erase a scalar signal | Two-probe or multiple-carrier detector |
| F15 | Unsigned prime majorants prove the needed signed rate | Absolute estimates lose arithmetic cancellation and can have wrong exponential order | Explicit signed first-prime target |
| F16 | A few positive actual Hankel matrices imply an infinite positive measure | Artificial negative-heat controls pass finite tests with nonreal roots | Need all-rank or controlled positive completion |
| F17 | A generic positive auxiliary model approximates actual xi uniformly | Model matching can fail at moving edges and fresh moments | Positive prefix interpolation plus precise residual obligation |
| F18 | External RH makes a derived Gaussian criterion independent | RH is an input to its strongest tail bounds | Correct conditional corollaries |
| F19 | Alpöge's formal certification certifies every human-readable paraphrase | Each deduction from a quoted Lean inequality needs its own statement match | Precise dependency and attribution chain |
| F20 | A finite LCM check confirms an infinite equivalence | Examples test only finite algebra and not the Mellin converse | A short, auditable criterion for specialist review |

Other corrected details include the Paper I $n=2$ boundary case, the ordered/orbit counting in reciprocal-pair expansions, actual-vs-model saddle normalisations, the distinction between unweighted and physical Gram metrics, and source-specific finite-rank versus infinite-rank claims. The comprehensive 28 September archive preserves the original counterexamples, their amended scopes, and the result locators for inspection.

## Why a no-go theorem can outrank a proof candidate

If a proposed universal step is false, even a counterexample in dimension two can remove a large number of invalid proof programmes. A correct local obstruction may therefore be more scientifically important than a long conditional chain with no closed arithmetic estimate. Conversely, a failed global inference does **not** annul a valid independent lemma. The exact unit of assessment should be a theorem with its quantifiers, operator, norm, domain and proof dependency, rather than the branding of its manuscript.

# Research importance: an explicit, non-probabilistic ranking {#research-importance-an-explicit-non-probabilistic-ranking}

## What a score means

The following scores are editorial **research-value indices out of 100**, not peer-review grades, probabilities of mathematical correctness, novelty certifications or percentages of RH solved. A score combines four qualitative considerations: (A) potential standalone mathematical content, (B) conceptual reach or usefulness across approaches, (C) clarity and reproducibility of the existing source, and (D) proximity to the actual arithmetic or analytic RH endpoint. Mathematical depth can score highly even when the independent RH closure is absent. Exact values have uncertainty of at least several points; near ties should not be interpreted as measured distinctions.

This critical edition includes the newly recovered October Jensen, Pringsheim, harmonic and velocity work; the Paper III score and scope are revised following the exact October counterexample. The ranking is of **distinct manuscript families and important version milestones**, not every repeated export, small-numbered patch or archive copy. External W200 and Alpöge--Claude are included separately for context, and **not** ranked as Dumas discoveries. A score may change after a proper originality search or expert referee report. The table is thus a retrieval and review priority map, not a declaration of publication merit.

## Principal contributions, ordered by research value

| Rank | Manuscript, theorem family or version | Score /100 | Why it matters / current boundary |
|---:|:---|---:|:---|
| 1 | [Signed Prime Correlations and Theta Continuation (Oct)](#atlas-primes) | **92** | Deep independent arithmetic criteria; signed off-diagonal estimate remains |
| 2 | [Referee III: Local Coercivity of the Complete Odd Weil Form (Sep)](#atlas-physical) | **91** | Explicit genuine physical-form strip theorem; no global Schur continuation |
| 3 | [Jensen Residue Protection: actual-theta sign regions (Oct 13)](#atlas-recovered-star-equations) | **91** | Actual-source residue bounds, effective dominant branch and exponential moment conditioning; core remains open |
| 4 | [Gaussian Prime Moments / Two-Probe Detector (Nov)](#atlas-gaussian) | **90** | Phase-robust detector, three moments, exact metric audits; first-prime rate open independently |
| 5 | [One-Sided Prime Sums and Real Parts of Zeta Zeros (Nov)](#atlas-windows) | **90** | Exact proposed signed growth exponent; limited technical audit, priority check pending |
| 6 | [Paper IX v421--v422: heat collision and zero-number compression](#atlas-algebra) | **89** | Theorem-scale boundary reduction; global guard absent, novelty review pending |
| 7 | [Referee II.9: physical norm countertest and repaired comparisons](#ch-referee-history) | **88** | Corrected major inference and exposed credible remaining routes |
| 8 | [Harmonic–Heat discriminant cancellation (Oct 9)](#atlas-recovered-star-equations) | **88** | All-degree exact harmonic polynomial identities; uniform sign/controlled loss open |
| 9 | [Scalar Pringsheim / fixed five-term middle-prime criterion (Oct 11)](#atlas-recovered-star-equations) | **88** | One test at each index, with non-cancelled interior poles; arithmetic middle range open |
| 10 | [LCM Inequality Criterion (Nov)](#a-least-common-multiple-formulation-of-rh) | **87** | Striking accessible proposed RH equivalence; external RH deduction separately attributed |
| 11 | [Paper VI / Adjacent-Shift Jensen and Wronskian Gram Theory](#ch-vertical) | **86** | Focused finite algebraic result and conventional publication candidate |
| 12 | [May Paper IX v0.4 curvature-two saddle certificate](#atlas-recovered-star-equations) | **85** | Source-reported raw-Xi curvature and exact leading saddle margin; effective Xi transfer open |
| 13 | [Referee II.8: terminal layer audit](#atlas-physical) | **84** | Precise source/metric reopening of the speculative global proof chain |
| 14 | [Original Paper VII: centred heat root flows](#ch-centered-heat) | **81** | Exact model root-gap barrier, with actual-Xi transfer outstanding |
| 15 | [Native Finite Sections / RESET $H=6144$](#ch-native) | **81** | Large finite interval certificate and honest continuum countercontrols |
| 16 | [Referee II.5: post-short source and Woodbury algebra](#ch-schur) | **81** | Reusable same-Gram identities; incomplete common physical range |
| 17 | [Dumas velocity Paper IV / source-forced root flow](#atlas-recovered-star-equations) | **81** | Distinct October numbered series; exact velocity identity, next-moment source sign unresolved |
| 18 | [Paper IX v437--v442 outer-region package](#paper-ix-version-by-version-what-actually-survived) | **80** | 3,500 recorded interval objects; low-slope horn and some regeneration gaps |
| 19 | [Complete Weil--Euler / Brehmer source factorisations](#ch-euler) | **80** | Exact source architecture; actual signed physical budget unpaid |
| 20 | [Original Paper III: corrected cocircuit, invalidated skeleton](#atlas-corrected-original-paper-iii) | **79** | Exact cocircuit algebra and corrected extraction; historic universal skeleton refuted at (4,4,4) |
| 21 | [Original Paper I: boundary-absorbed Schur gates](#ch-boundary-gate) | **79** | Exact endpoint product and reservoir principle; corrected $n=2$ case |
| 22 | [F21 Hausdorff / Jacobi / CMV original-Xi moments](#ch-layercake) | **79** | Exact compact-moment mapping; required all-rank positivity open |
| 23 | [Dumas Residual Dynamics, related transport/geometry](#ch-crossfields) | **78** | Exact finite root-speed spectral system and source-forced identity; global next-moment sign open |
| 24 | [Paper IX v150 finite Wronskian certification](#paper-ix-version-by-version-what-actually-survived) | **77** | Reproducible finite Bernstein scheme, not a global cover |
| 25 | [F39--F166 prime activation and Darboux/RESET relay](#ch-mature) | **77** | Detailed transport identities; regeneration and landing not proved |
| 26 | [Original Paper V: boundary-minor Newton--Jensen mechanisms](#ch-ladder) | **76** | Correct finite Sturm ladder, conditional all-degree transfer |
| 27 | [Original Paper VIII: saddle separation / Airy edge](#ch-paper-nine) | **76** | Strong conditional asymptotic apparatus, uniform Xi bridge absent |
| 28 | [Weyl/Liv\v{s}ic and canonical-system realization](#ch-spectral) | **76** | Compelling spectral alternative, Xi-specific positivity and limit open |
| 29 | [Theta--Mellin/Hankel--Bezoutian alternative](#atlas-moments) | **75** | Direct coefficient and spectral-moment line; growing-rank sign open |
| 30 | [Original Paper II: reciprocal-pair flagged gates](#ch-reciprocal) | **74** | Exact finite perturbation calculus, limited transfer |
| 31 | [Referee II September 24 proof-facing candidate](#ch-referee-history) | **74** | Useful pole extraction, physical source placement open |
| 32 | [Original Paper IV: rising-factorial residual layers](#ch-rising) | **73** | Finite coefficient signs; universal positivity unproved |
| 33 | [V13 common-cut physical assembly](#ch-weil) | **72** | Important structural source; later physical interface disputes |
| 34 | [Original Paper IX early seven-region series](#ch-paper-nine) | **70** | Broad historical route design, failed joint proof-grade coverage |
| 35 | [Three-port Redheffer / cubic edge](#ch-schur) | **70** | Small boundary model; complete arithmetic rank not reduced |
| 36 | [Referee I September 23 candidate](#ch-referee-history) | **68** | Historical first full assembly; later projection/funding mismatches |
| 37 | [Paper IX v423--v427 finite-height bridge scouts](#ch-paper-nine) | **68** | Effective diagnosis of small-time horn, not closed global guard |
| 38 | [Fixed-base F18--F20 orthogonal Hardy/Joukowski folds](#ch-folds) | **67** | Exact scalarised energies; all-scale inference absent |
| 39 | [Cubic-wedge F166 asymptotic protection](#ch-relay-continuation) | **63** | Restricted parameter protection, physical endpoint absent |
| 40 | [Referee II.1 historical six-gate freeze](#atlas-physical) | **60** | Important provenance; downstream dependencies reopened |
| 41 | [Three Expositions Comparative Research Dossier](#atlas-frontier) | **60** | Valuable external-proof study and audit; primarily explanatory synthesis |
| 42 | [September Unified Book of Workings](#ch-overview) | **59** | Exceptional preservation and retrieval infrastructure; not a single new theorem |

These scores intentionally differ from journal-referee confidence: a clean short theorem might be easier to publish than a highly ranked 92/100 programme containing unresolved all-scale arithmetic. The apparent precision is a convenience for sorting, not a claim to calibrated measurement.

## Historical external works: separate attribution

- **Alpöge--Claude formal RH/Dirichlet-GRH development:** an external, community-certified formal proof according to the public 21 November verification statement. It is not part of the Dumas independent theorem count.
- **Rubinstein's and other contemporary expositions:** external, evolving explanatory accounts; quoted deep arithmetic inputs must remain flagged.
- **Vincent Liu's W200:** a separate fixed-window local theorem with its original authorship retained; Dumas source-completion, attempted extensions and corrections are the programme's work.
- **Classical sources:** de Bruijn, Newman, Griffin--Ono--Rolen--Zagier and subsequent effective Jensen authors, Platt--Trudgian, Kaczorowski--Pintz, Weil, Connes, Suzuki, Jacobi/CMV and other referenced work supply conceptual and theorem inputs, not discoveries attributable to this research programme.

# Ranked publication and continuation plan

## The strongest credible independent articles

**First: one-sided prime-sum oscillation.** Separate the analytic theorem (S10.3) from the external arithmetic-window corollary. Give a self-contained Mellin representation, Gaussian selection lemma, tail estimates, nonattained-supremum handling, finite discretisation and a careful literature comparison. A specialist review should attempt counterexamples to the frequency-selection argument before any strong novelty claim.

**Second: the LCM inequality criterion.** The algebraic relation (S11.2), RH-to-inequality estimate and Mellin-positivity converse should be audited independently line by line. The text should accurately describe the external arithmetic-window deduction as a consequence of a formally certified theorem, not its replacement. Priority versus existing lcm/Lagarias/weighted-prime criteria is unresolved.

**Third: Referee III's physical terminal-strip theorem.** Present the exact norm, form domain, digamma uncertainty lemma, ordinary-prime short-interval bound, proper-power estimate and pole subtraction without relying on the invalidated older cofinal chain. Its limited scope is a strength of its scientific presentation.

**Fourth: Paper III and Paper VI, subject to correction.** Paper VI remains a focused adjacent-shift and Wronskian project. Any new Paper III article must present only the corrected cocircuit identity and (A38), **not** the retracted forced-root skeleton; the older paper needs a new theorem before its residual divisions are used. They are natural submissions to different specialist audiences; they do not need to claim RH.

**Fifth: Paper IX collision compression.** Publish a narrowly scoped local-degree/zero-number note only after exact comparison with classical parabolic PDE literature and a complete proof of event isolation and homotopy in the declared sign convention.

**Sixth: the Gaussian programme.** Split the long synthesis into (a) detector and three-moment equivalence, (b) operator metric/projection obstruction, and (c) conditional Möbius--Gaussian tails. Keeping unconditional, conditional and negative results distinct will make each easier to review.

## The remaining independent arithmetic theorem

A genuinely independent continuation of the Gaussian/Weil programme requires proving its first-prime signed growth estimate (S1.5) or a logically comparable full-source inequality without assuming RH. That is the difficult mathematical target. An import from the external Lean theorem would establish the criterion only as a corollary, not supply a second proof.

A productive next technical audit should therefore proceed in this order: source-exact matrix; correct physical Gram; exact ordinary-prime and prime-power decomposition; rational carrier choices; same-denominator Schur cost; negative-heat/artificial-source countercontrols; and a fully quantified signed arithmetic bound. One must not spend further work on a generic positivity assertion already contradicted by a two-dimensional counterexample.

## What could change the priority order

A fresh theorem that transports the actual Xi coefficients into the finite Jensen models through *cofinal unshifted degree* would immediately elevate Papers VI--IX. A verified exact physical signed estimate on cofinal Weil windows would elevate Referee III and the two-probe route. A uniform positive-measure/next-moment theorem for the true Xi sequence would elevate F21 and the Hankel family. A complete published human-readable derivation of Alpöge's hardest arithmetic inequality would improve interpretability of the new arithmetic-window corollaries but would remain an *external* input unless independently proved and attributed.

# Reproducibility, source inventory and limits

## Source genealogy and status keys

The principal recovered files used for this synthesis are as follows. Their dates refer to internal manuscript dates or explicitly named historical freezes, not necessarily first public release.

| Key | Source | Role |
|:---|:---|:---|
| D1 | *The Riemann Hypothesis Programme: A Unified Book of Workings* (28 Sep 2026), Markdown/PDF | Complete preserved 50-chapter technical foundation and historical primary-source register |
| D2 | *RH Master Research Ledger* (13 Nov, with later revisions), Markdown | Current supersession and proof-dependency ledger |
| D3 | *Signed Prime Correlations and Theta Continuation for the Riemann Xi Function* (12--13 Oct), 92-page manuscript | Signed arithmetic and complete-theta programme |
| D4 | *Referee Paper III: Local Coercivity and Exact Schur Reductions for the Odd Weil Form* (27 Sep) | Source-contained local theorem and operator-domain corrections |
| D5 | *PaperIX v442 effective lambda >= 5.52 owner* (7 Sep), ZIP | Outer-region interval data, verifier and README; dependencies limited to supplied archive |
| D6 | *Gaussian Prime Moments, Mobius Tails and Weil Forms* (22 Nov), consolidated Markdown/PDF | Modern analytic, operator and computational synthesis |
| D7 | *One-Sided Prime Sums and the Real Parts of the Zeta Zeros* (22 Nov), PDF/source | Six-page analytic growth and arithmetic-window manuscript |
| D8 | *The Riemann Hypothesis in One Inequality for Least Common Multiples* (23 Nov), PDF/source | Seven-page integer criterion and external-RH corollary |
| D9 | *Independent Technical Audit of One-Sided Prime Sums* (23 Nov), Markdown | Algebraic/numerical audit, scope and dependency checks |
| D10 | *RH v421--v423 rigorous file audit* (8 Aug), Markdown | Replayed small symbolic checks and enumerated global guard failures |
| D11 | *Paper IX v150 Rigorous Progress Report*, Markdown | Finite Wronskian certificate design and 656-gate report |
| D12 | *RH Retrospective and Architecture Log* (21 Sep), Markdown | Originality/attribution and source genealogy review |
| D13 | *Three Expositions Comparative Proof Dossier* (22 Nov), Markdown | External proof decomposition, imports and arithmetic estimate boundary |
| D14 | *Adjacent-Shift Proper Position for Jensen Polynomials* (17 Sep), PDF/TeX | Standalone conventional Jensen note |

The historical technical book's source register additionally indexes the exact original TeX for Papers I--VIII, Paper IX version collections, Referee II.1--II.9, W200-derived local material, the F-series, corrected finite certificates and the 28 September archive. That register is included intact below. The source package accompanying this new book includes a selected set of exact files and SHA-256 checksums; the source selection is **not** a guarantee that every historical conversation, ephemeral scratch file or massive external data archive is represented byte-for-byte.

## Public external sources

- **[E1]** Lean and Mathlib communities, *Lean verification of the Riemann Hypothesis*, joint statement, 21 November 2026. \url{https://leanprover-community.github.io/blog/posts/riemann-hypothesis/}.
- **[E2]** Michael O. Rubinstein, *Alpöge/Claude proof of the Generalized Riemann Hypothesis* (verification reports and links), with *The Alpöge--Claude proof of the Riemann hypothesis explained for the Riemann zeta function*, 164-page working draft, 21 November 2026. \url{https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/}.
- **[E3]** twinheterodox, *Three simplifications in the Alpöge--Claude argument for Dirichlet GRH*, Hexagon 2611.00828v1, 21 November 2026. \url{https://hexagonmath.org/2611.00828v1}.
- **[E4]** J. Kaczorowski and J. Pintz, *Oscillatory properties of arithmetical functions I*, Acta Math. Hungar. 48 (1986), 173--185, doi `10.1007/BF01949062`.
- **[E5]** D. Platt and T. Trudgian, *The Riemann hypothesis is true up to $3\cdot10^{12}$*, Bull. London Math. Soc. 53 (2021), 792--797; arXiv:2004.09765.
- **[E6]** D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn--Newman constant*, arXiv:1904.12438.
- **[E7]** J. C. Lagarias, *An elementary problem equivalent to the Riemann hypothesis*, Amer. Math. Monthly 109 (2002), 534--543.
- **[E8]** L. Alpöge, announcement of a Lean formal proof of RH and Dirichlet GRH, 20 November 2026, \url{https://alpo.ge/remark.pdf}; formal library \url{https://github.com/leanprover-community/riemann-hypothesis}.

- **[E9]** M. Griffin, K. Ono, L. Rolen and D. Zagier, *Jensen polynomials for the Riemann zeta function and other sequences*, Proc. Natl. Acad. Sci. USA 116 (2019), 11103--11110. \url{https://doi.org/10.1073/pnas.1902572116}.
- **[E10]** A. Connes, C. Consani and H. Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755. \url{https://arxiv.org/abs/2511.22755}.

External claims have been checked against contemporary public HTML records when available. These records concern the external proof and literature, not an independent audit of the Dumas equations.

## Detailed verification legend

- **Exact algebra, manuscript proof:** a source has an explicit proof; independent review may still detect a gap.
- **Finite rational check:** a finite identity is established using exact arithmetic, with scope restricted to checked sizes or degrees.
- **Outward interval certificate:** a finite sign statement follows from enclosures provided all inputs, arithmetic and coverage are correct. Hash validation is not numerical replay.
- **Diagnostic:** floating-point data or a plot without certified error control.
- **Conditional theorem:** conclusion established only under stated assumptions, possibly RH itself or a result of equivalent strength.
- **RH equivalence:** a new reformulation that still needs an unconditional proof of one side.
- **External formal theorem:** verified according to the named Lean/Mathlib statement, not reverified in this paper.
- **Historical PASS:** retained for provenance, not inherited when later amendments refute a premise.

## Reproducible small symbolic checks supplied with this volume

The accompanying lightweight script checks selected algebraic statements at finite test values: the Schur cocircuit factorisation, the dilation polynomial, the Jensen adjacent-shift identities, the exact LCM-to-prime-power finite relation, and a random finite-matrix block/projection commutator. They are educational regression checks rather than substitutes for the corresponding infinite theorems. The ZIP contains a machine-readable inventory with SHA-256 hashes of included source objects, as well as instructions for compiling the final PDF from its Markdown and LaTeX headers.

# November 13--20 micro-results: the detailed continuity index {#november-1320-micro-results-the-detailed-continuity-index}

The most recent consolidated Gaussian paper incorporates fourteen intermediate notes from 17--18 November plus several later audits. They should not disappear behind the label "November Gaussian work". This continuity index preserves their mathematical contributions and the restrictions identified in the later consolidation. It is an index rather than a reprint of every daily notebook; exact source filenames, scripts and retained derivations are in [D6].

| Code | Principal result or avenue | Surviving use and explicit limitation |
|:---|:---|:---|
| N01 | Dressed source, inverse-pole and Krylov identities | Exact finite formulas; incomplete uniform response, corrected under noncommuting compression |
| N02 | Screened pole/Picard continuation | Useful conditional source localisation; physical Gram and deep-tail bound unpaid |
| N03 | Pole-transition, parity inertia and filter bank | Finite experimental structure; neither complete positivity nor an all-band frame proved |
| N04 | Source-exact prolate Schur and finite Möbius inversion | No automatic convolved Gram lower floor |
| N05 | Single-divisor reformulation and moving-window audit | RH-equivalent reduction; no independent divisor cancellation |
| N06 | Gevrey localisation and polylogarithmic complement | Reduces analytic loss; retains a hard signed Möbius complement |
| N07 | Symmetric residual and double-notch construction | Identifies energy obstruction; Gevrey smoothing improves the analytic representation |
| N08 | Triangle-kernel and nonlinear multiwindow tests | Pairwise favourable tests insufficient for full matrix positivity |
| N09 | Multiscale energy and finite-band obstruction | No finite-frequency scanner replaces the infinite signed tail |
| N10 | Dispersion/cartography and heat-variance identities | Strong structural map; off-diagonal arithmetic remains decisive |
| N11 | Type-II residue rigidity and phase obstruction | Disproves an averaging shortcut; no new exponent-saving theorem |
| N12 | Two-sided Vaughan decomposition with joint roots | Exact localisation of hard signed Type II correlation; estimate not yet won independently |
| N13 | Joint Type-I boundary neutrality | Improves a boundary-root cancellation by keeping the logarithmic moment |
| N14 | Endpoint-neutral continuation and compensated shells | Partial exact cancellation; a root of one factor is insufficient |

Additional follow-ups after that chain include the **15 November Gaussian-strip audit**, the **16 November Möbius outer-range analysis**, the **20 November Suzuki physical-metric audit**, and the **22 November triple-exposition comparative proof dossier**. Their valid parts are retained in the consolidation and the accompanying source package. The Quasi-RH $7/8$ zero-free region, the Connes--Andrews--La Gatta conditional positivity framework, and Suzuki's screw-function/Weil operator papers are **external** inputs and comparators, not Dumas discoveries. The later internal calculations do not inherit unrestricted conclusions from those sources without checking domains and normalization.

## Minimal evidence protocol for every retrieved result

To turn any N01--N14 item into a publishable lemma, the checking record must specify its exact version, hypotheses, object and functional space, whether all prime powers and polar terms are included, which quantities are fixed or tend to infinity, whether a computation is interval-certified, the missing arithmetic inequality, and any later counterexample. Positive metadata such as `PASS`, a checksum, or successful reconstruction of a ZIP directory structure is not itself a mathematical proof.


# Conclusions and remaining arithmetic estimates

The work's strongest unifying insight is **source fidelity before positivity**. The critical-edition additions show how source fidelity also applies to scholarship itself: the exact Paper III counterexample must supersede a historically asserted skeleton, differently numbered series must remain separate, and bounded-region theorem statements must not become all-degree claims. Across finite Schur algebra, Jensen hyperbolicity, canonical moments, Weil forms and arithmetic sums, most successful reductions identify a small structural obstruction only after exact cancellation of the forced parts. Most unsuccessful global proofs silently crossed an unverified bridge: a finite certificate to an infinite family, a model coefficient to an actual xi coefficient, a positive reference to a complete signed operator, or a valid source-specific inverse identity to an unrelated denominator.

The archive is therefore not merely a sequence of attempts to solve RH. It is a collection of finite theorems, local analytic estimates, exact transforms, computational techniques, counterexamples, and well-stated research problems. The two new arithmetic criteria offer especially accessible statements; the October signed-prime programme and the September physical Weil work contain the most elaborate independent analytic material; the old Paper III and Paper VI remain worthwhile finite-mathematics works; and the Paper IX collision compression deserves serious review outside the original proof ambition.

With the November external formal result publicly certified, the publication task has changed. It is no longer necessary to describe these results as competing complete proofs. Their independent value should stand on **precise definitions, correct quantifiers, transparent provenance, independent replication, scholarly attribution and honest separation of arithmetic inputs**. Preserving negative results alongside positive ones is not a concession: it is what makes a complex scientific programme usable by future researchers.

\part{Technical foundation of 28 September 2026}

# Note on the preserved fifty-chapter book {.unnumbered}

The following material preserves the recovered technical work-book body dated 28 September 2026, but *superseded assertions are explicitly tagged in situ* where later exact audits invalidate them (notably Chapter 26). Its original claims remain traceable in the unchanged primary archive. Its equations, original P1--P8 source names, Paper IX records, referee history, computational scopes, negative controls, historical appendices and source-key catalogue are intentionally retained. Claims described as contemporary or open *in that dated historical text* should be interpreted as September statements; the November developments and external certification status are described in the opening synthesis. This is a preservation layer, not a claim that every historical assertion was newly re-proved during the compilation of this volume.



# Preface {.unnumbered}

This book follows a mathematical programme through its changes of representation. Its subject is not one continuously improving proof draft, but a collection of interconnected attempts to understand why the zeros of the completed zeta function should lie on the critical line. The programme has worked with Schur minors, reciprocal-pair deformations, Jensen polynomials, heat flows, compact moment sequences, finite-prime activation, canonical systems, localized Weil forms, Euler products, boundary states, and source-dependent inverse energies. The same algebraic operation often reappears in different coordinates; the difficulty is deciding when that resemblance represents a genuine mathematical identification.

The exposition is organized by present usefulness, with chronology retained inside each family. The complete physical Weil form is treated first because it supplies both a fixed arithmetic object and an endpoint detector. The actual central-coefficient moment problem follows as an independent approach. The older polynomial and finite-prime programmes are then developed in their own right, rather than reduced to a catalogue of abandoned names. Their exact formulas, local results, failed extensions, and outstanding problems remain available for reuse.

Several conventions distinguish this book from a stack of working papers. A recurring identity receives a principal treatment and subsequent occurrences refer to that treatment. A change in normalization is written as a formula. A historical claim that was later narrowed is presented together with the narrowing, while its original source remains preserved. Numerical evidence is described by what was enclosed or tested, not by the enthusiasm with which a checkpoint was announced. An unresolved application is stated as a mathematical question with its quantifiers; it is not hidden in an editorial label.

The source material includes original TeX for Papers I–VIII, Paper IX dossiers and certificate packages, the fixed-parameter prime-Hausdorff and RESET handovers, the W200 working corpus, the referee series through II.9 and III, and the 28 September arithmetic, multiplier, moment, and all-rank studies. The book is an authored synthesis of those materials. Its companion source collection retains the recovered texts, programs, and recorded outputs in their original form. The source catalogue and formula index distinguish exact files from historical summaries and identify the remaining retrieval gaps. A complete export of every past conversation is not among the recovered inputs.

The author of the research programme is Alexandre Dumas. The exposition was assembled with AI assistance from the recovered mathematical record. Imported results and packages retain their original attribution. In particular, W200 is a local certificate used within the programme, not the origin of every architecture in the book. Theorems below are presented with their hypotheses and source locations; the current unresolved questions are part of the mathematics, not omissions to be repaired by an optimistic label.

The central practical purpose is continuity: a subsequent investigation should be able to recover not just what was tried, but the precise object involved, why a result mattered, what invalidated a proposed extension, and where an alternative remains possible.

# How to read the book {.unnumbered}

The first three chapters establish the language shared by the later parts. Chapters 4–12 develop the complete physical form and its continuation problem. Chapters 13–18 follow arithmetic cancellation from finite Euler identities to the fixed-window prime-excess formulation. Chapters 19–23 develop the actual-$\Xi$ moment route and its controls. Chapters 24–32 reconstruct the original polynomial series and its newer multiplier extensions. Chapters 33–38 treat the older compact-moment and actual-prime relay. Chapters 39–45 develop finite sections, RESET energy, spectral folds, jump processes, gauges, and geometric connections. Chapters 46–50 collect the implication-level counterexamples, cross-era connections, chronology, current research frontier, and audit discipline. The appendices supply notation, result locators, computation records, the source register, and the numbered-equation index.

Three kinds of passage recur. A **result** is a statement accompanied by an argument or a source-supplied proof in its displayed scope. A **recorded certificate** is a finite computation with retained inputs and outputs; this book does not describe a historical execution as a newly performed one. A **connection** is either an explicitly derived identification or a proposed transfer whose missing hypotheses are named. This distinction is particularly important where two chapters use the word *Gram*, *source*, *owner*, *front*, or *boundary* for different objects.

Source keys such as **RIII**, **II9**, **SC4**, and **F166.78** resolve in the source register. Content hashes provide a second, filename-independent locator. The equation index preserves the location of formulas outside the principal exposition as well. References to an original paper number and to a referee paper number are never interchangeable: *Original Paper III* is the cocircuit–Brion paper; *Referee III* is the localized Weil-form paper.


\part{Objects, conventions, and the logic of the programme}

# 1. One programme, several mathematical objects {#ch-overview}

## From a zero statement to a structural question

The Riemann hypothesis is a statement about the zeros of one analytic function. Most of this programme does not attack individual zeros directly. Instead it asks whether an arithmetic construction belongs to a positivity class whose analytic consequences force the required zero geometry.

There are three principal forms of that question. The physical formulation asks for a lower bound for a complete quadratic form on expanding intervals. The coefficient formulation asks for positivity of a structured sequence of Hankel matrices. The polynomial formulation asks for hyperbolicity of Jensen polynomials and related vertical gates. Each formulation is legitimate, but none is made easier merely by giving its last condition a new name.

The development repeatedly exposed a distinction between **constructing an identity** and **obtaining its useful estimate**. An exact Schur complement makes the inverse-energy term visible; it does not pay it. A positive synthesis Gram supplies a metric; it need not be the metric of the complete signed operator. A hyperbolicity-preserving multiplier supplies a real-rooted model; it does not prove that the model matches the actual coefficient sequence sufficiently well. A feasible finite moment interval contains possible next moments; it need not contain the next moment prescribed by \(\Xi\).

These are not reasons to discard the constructions. They tell us what each construction has achieved. A principal aim of the book is to keep the algebraic gain and the remaining analytic burden in the same place.

## The present order of work

The highest-priority physical question is a same-form cofinal estimate. Let \(q_{\mathrm{comp},b}\) denote the complete odd Weil form on an interval of aperture \(b\), with the pole term included. The target has the form

$$
q_{\mathrm{comp},b_j}[u]\ge-\beta_j\|u\|^2,
\qquad b_j\longrightarrow\infty,
\qquad \log(1+\beta_j)=o(b_j).
\tag{1.1}\label{eq:1.1}
$$

The test space and any pole-neutral restriction must be the same ones used by the detector. This is weaker than a uniform positive gap, and weaker than nonnegativity at every aperture. It remains a global arithmetic estimate because every old/future interaction, shift, and complementary direction must be included.

The independent coefficient question starts from a normalized even descent \(F\) of \(\xi\). Its logarithmic coefficients define matrices

$$
H_n=(p_{i+j+1})_{i,j=0}^{n-1}.
\tag{1.2}\label{eq:1.2}
$$

Positivity at unbounded sizes has a direct analytic implication. The computational record reaches size 20 for the actual sequence, but an altered negative-heat function passes the same finite tests while having nonreal zeros. Thus rank is a measure of finite coverage, not a percentage of an infinite proof.

The polynomial question is most economically posed on a cofinal sequence of unshifted Jensen polynomials. The old two-parameter Paper IX programme remains useful for its phase, curvature, and finite-certificate machinery, but a theorem in a large-shift region does not automatically reach growing unshifted degree.

These priorities are a research allocation, not probabilistic odds. They reflect how directly an available source identifies the final arithmetic object and how specifically its missing estimate can be stated.

## The historical structure

The earliest recovered work in April explored Herglotz, Pick, Stieltjes, and Pólya-frequency representations. The original Papers I–V developed finite determinant and boundary-reservoir mechanisms. Papers VI–IX turned toward vertical proper position, centered heat, saddle separation, and global parameter routing. In June, compact Hausdorff and Jacobi/CMV representations provided another exact endpoint. August concentrated on finite-prime activation at one fixed base parameter, canonical-moment defects, Darboux transformations, and mature rank-to-rank recruitment.

Early September reorganized that relay around physical prefixes, Haar refinement, finite Toeplitz-minus-Hankel sections, and terminal innovation. The W200 and common-cut work then brought the complete Weil form, Euler excitation, source geometry, and boundary reduction to the foreground. The September 23–26 candidate manuscripts attempted to assemble those modules. The referee amendments identified precise failures in the physical transfer, denominator, and continuation interfaces. Referee III retained a complete physical normalization and proved local statements without inheriting those disputed global steps.

The September 28 studies explored two directions in parallel. One made the physical source quotient more selective and reduced the arithmetic detector to a fixed pair of packets. The other pursued actual central coefficients through finite-free models, positive prefix completions, moment matrices, and a direct coefficient kernel. Neither direction is to be erased when the other becomes fashionable: their controls test different weaknesses.

## Why the original wording must remain available

The programme contains historical claims labelled PASS, ACTIVE, and proof candidate. They have documentary value. Some were correct within a narrower scope; some were later contradicted; some relied on premises that changed. The right editorial operation is a dependency-specific correction, not deletion of the old source and not unconditional inheritance of its label.

For example, the same-Gram inverse identity in II.5 survives as elementary linear algebra. The later objection concerns using it after shorting a different, complete denominator. Similarly, the existence of a finite matrix certificate for a trial space is not retracted merely because a continuum test outside that space has much smaller energy. What fails is the extrapolation from one space to the other.

The resumption rule is therefore precise: identify the source statement, its object, its assumptions, and the later scope correction before using it as a premise. Throughout the book this rule is applied mathematically, by displaying the relevant maps and estimates.

*Sources:* [MASTER](#source-master), [ATLAS](#source-atlas), [V10B](#source-v10b), [II8](#source-ii8), [II9](#source-ii9), [RIII](#source-riii), [AR](#source-ar), ARK. The priority order is an editorial synthesis of their current obligations.

# 2. Functions, transforms, and metrics {#ch-conventions}

## Completed zeta and the two even descents

The completed zeta function is

$$
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \xi(s)=\xi(1-s).
\tag{2.1}\label{eq:2.1}
$$

Write

$$
\Xi(z)=\xi(\tfrac12+iz).
\tag{2.2}\label{eq:2.2}
$$

Then \(\Xi\) is even, and the desired zero statement is reality of its zeros. A different but equivalent even function is \(z\mapsto\xi(1/2+z)\). Confusing these two conventions reverses the sign in a square-root descent.

For the actual central coefficients use

$$
\xi(\tfrac12+z)=\sum_{j\ge0}\frac{\gamma_j}{j!}z^{2j},
\qquad \kappa=\frac{\gamma_1}{\gamma_0},
\tag{2.3}\label{eq:2.3}
$$

and

$$
F(w)=\frac{\xi(1/2+\sqrt{w/\kappa})}{\gamma_0}
     =\sum_{j\ge0}c_jw^j,
\qquad c_0=c_1=1.
\tag{2.4}\label{eq:2.4}
$$

The square root in (2.4) is notation for an even power series, not a choice of analytic branch. Consequently \(F\) is entire. In the equivalent \(\Xi\) notation it is \(\Xi(\sqrt{-w/\kappa})/\Xi(0)\).

The exponential-normalized coefficients are

$$
R_j=j!c_j
=\frac{\gamma_j\gamma_0^{j-1}}{\gamma_1^j},
\qquad R_0=R_1=1.
\tag{2.5}\label{eq:2.5}
$$

A root \(w=-a^{-1}<0\) of \(F\) corresponds to a purely imaginary displacement from \(1/2\) in the \(s\)-plane, hence to a critical-line zero. The variable \(a\) in such a factor \(1+aw\) is not an aperture. It is a reciprocal zero coordinate.

## Fourier and odd half-line conventions

For a full-line function \(f\), the convention in Referee III is

$$
\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx,
\qquad
\|f\|_2^2=\frac1{2\pi}\int_{\mathbb R}|\widehat f(t)|^2\,dt.
\tag{2.6}\label{eq:2.6}
$$

Let \(\mathcal H_b=L^2(0,b)\). The map \(J_b\) makes an odd zero extension without normalization. Thus

$$
\|J_bu\|_2^2=2\|u\|_2^2.
\tag{2.7}\label{eq:2.7}
$$

The half-line quadratic form is half the full-line Weil form. Both energy and norm acquire the same factor, so Rayleigh quotients agree. This is the reason a factor of two can disappear from a quotient but not from an intermediate identity.

The pole vector is

$$
g_b(x)=2\sinh(x/2),
\qquad \ell_b(u)=\langle g_b,u\rangle.
\tag{2.8}\label{eq:2.8}
$$

For an odd full-line extension, its two exponential moments are opposite. The completed pole term is consequently negative in the odd sector. It must not be imported with the even-sector sign.

All inner products are conjugate-linear in their first argument. A transpose in a real finite model becomes an adjoint in the complex Hilbert-space application. A spectral pairing \(G(z)^2\) from a real-even test is not automatically the positive quantity \(|G(z)|^2\).

## The physical logarithmic form domain

The Archimedean symbol is

$$
m(t)=\operatorname{Re}\psi(\tfrac14+\tfrac{it}2)-\log\pi.
\tag{2.9}\label{eq:2.9}
$$

The form domain is

$$
\mathcal D_b=\left\{u\in\mathcal H_b:
\int_{\mathbb R}\log(2+|t|)|\widehat{J_bu}(t)|^2\,dt<\infty\right\}.
\tag{2.10}\label{eq:2.10}
$$

The logarithmic weight matters twice. It makes high-frequency concentration energetically expensive, so a large unweighted norm witness need not be a negative Weil-form witness. It also gives compact embedding into \(L^2\) at a fixed spatial aperture, allowing a genuine finite low-energy spectral core. It does not give uniform bounds as the aperture grows without additional estimates.

Sharp spatial cuts preserve this domain only after their off-diagonal interaction is controlled. Referee III supplies that control. A formal block decomposition of an unbounded operator must therefore be read first at the closed-form level.

## Parameters that must not be identified

The physical aperture is usually \(b\), with arithmetic coordinate \(N=e^{2b}\). A canonical integer shell has endpoints \(a_n=\frac12\log n\). The letter \(D\) can mean a mesh size in a finite-section paper, a denominator in a Schur formula, or a polynomial degree in an early paper. The book writes subscripts when the distinction matters.

In Jensen notation, \(d\) is degree and \(n\) is shift. The centered index is \(m=n+d/2\). The fixed-prime Hausdorff programme instead keeps a base parameter \(a=30\) fixed while varying a prime cutoff \(P\) and depth. Its canonical moments \(p_j\) are not the logarithmic moments \(p_r\) of (2.4). We write \(p_j^{\mathrm{can}}\) where both appear in one discussion.

Paper IX uses more than one dimensionless parameter called \(\lambda\). The early ratio \(d/(n+d/2)\) is at most two. It cannot be identified with a later chamber coordinate whose reported range begins at \(5.52\). The exact chart must be recovered before comparing such thresholds.

## A typed estimate

An estimate is fully specified only after recording its source and target spaces, norms, parameter range, and order of operations. For example,

$$
C^*(BB^*)^\dagger C\preceq I
\tag{2.11}\label{eq:2.11}
$$

means something different when \(C=B\widetilde C\) and the denominator is the synthesis Gram than when the denominator is a screened physical form. If a new metric is \(D=BB^*+K\), both the source and the inverse must be reconstructed in that metric. This book repeatedly uses elementary identities such as (2.11), but it never treats their notation as an identification of unrelated operators.

*Sources:* [RIII](#source-riii) §§2, 4–7; [II8](#source-ii8) §2; [ARK](#source-ark) §1; [HYB](#source-hyb); [AR](#source-ar); [F39](#source-f39) and F166 handovers.

# 3. Cofinality, convergence, and the actual endpoint {#ch-endpoints}

## A lower allowance can be enough

A cofinal estimate is one that holds along a sequence of parameters tending to the required limiting regime. The physical detector makes the following target useful:

$$
\nu(b_j)\ge-\beta_j,
\qquad b_j\to\infty,
\qquad \frac{\log(1+\beta_j)}{b_j}\to0.
\tag{3.1}\label{eq:3.1}
$$

Here \(\nu(b)\) is the infimum of the complete-form Rayleigh quotient over the declared full test class. The detector states that an off-line zero would force \(\nu(b)\le-e^{cb}\) for every sufficiently large \(b\), for some \(c>0\). These two bounds are incompatible.

A fixed finite negative allowance is permissible. So is a polynomial in \(b\). A fixed power \(N^\varepsilon\), with \(N=e^{2b}\), is not permissible unless the exponent tends to zero along the cofinal sequence. This distinction is why a growing logarithmic shift can be harmless but an uncontrolled square-root-prime loss cannot.

## The adaptive staircase

Suppose the old stage has lower bound \(A_M\succeq-b_MI\), and the complete new block is

$$
A_N=\begin{pmatrix}A_M&B\\B^*&D\end{pmatrix}.
\tag{3.2}\label{eq:3.2}
$$

Assume at one common future horizon that

$$
D+sI\succ0,
\qquad B(D+sI)^{-1}B^*\preceq\Delta I,
\qquad s,\Delta\ge0.
\tag{3.3}\label{eq:3.3}
$$

Completing the square in the future variable gives the safe lower bound

$$
A_N\succeq-(b_M+s+\Delta)I.
\tag{3.4}\label{eq:3.4}
$$

The later II.9 formulation is sharper when the entire residual is exposed, but (3.4) captures the basic staircase. Suppose that after every old stage is frozen, and for every \(\varepsilon>0\), arbitrarily remote admissible horizons satisfy

$$
s_{M,N}+\Delta_{M,N}\le N^\varepsilon.
\tag{3.5}\label{eq:3.5}
$$

Choose \(\varepsilon_j\downarrow0\). At the next stage choose \(N_{j+1}\) so remote that both (3.5) and \(b_{N_j}\le N_{j+1}^{\varepsilon_j}\) hold. Then

$$
b_{N_{j+1}}\le2N_{j+1}^{\varepsilon_j},
\qquad
\frac{\log(1+b_{N_{j+1}})}{\log N_{j+1}}\to0.
\tag{3.6}\label{eq:3.6}
$$

The order of quantifiers is essential: freeze the old stage, then choose a future horizon satisfying all simultaneous conditions. Separate unbounded sets of good horizons need not intersect. A separate small error for each channel does not prove a small total error if the number of channels grows too quickly.

## Why a fixed global shift is optional, but its replacement is not automatic

The September 24 architecture sought one fixed shift large enough to pay a horizon-independent lifetime majorant. That is a valid strategy if the majorant is proved in the complete physical metric. The later adaptive strategy permits the shift to vary, provided its final contribution is subpower in \(N\).

This is a weakening of the sufficient hypotheses, not a proof of the weakened hypotheses. A positive shifted finite matrix cannot be relabelled as the unshifted denominator. Nor does a shift that makes one compression positive make all future compressions positive at the same cost.

## The coefficient endpoint

For a normalized entire \(F\), all-rank positivity of the logarithmic Hankel matrices yields a positive representing measure. Local analyticity makes its support compact; analytic continuation then rules out nonreal zeros. A cofinal sequence of matrix sizes suffices because every smaller leading principal block occurs inside some larger positive matrix.

Unlike the physical endpoint, this route needs no lower-eigenvalue rate. Every matrix may have an extraordinarily small last positive pivot. What is needed is positivity at every finite size, not a bound keeping those pivots away from zero. This makes it a different target, not a weaker conclusion obtained for free.

## The polynomial endpoint

For

$$
F(w)=\sum_{k\ge0}\frac{\gamma_k}{k!}w^k,
\qquad
J_d(X)=\sum_{k=0}^{d}\binom dk\gamma_kX^k,
\tag{3.7}\label{eq:3.7}
$$

one has \(J_d(w/d)\to F(w)\) locally uniformly. Indeed \(\binom dk/d^k\le1/k!\) and converges to \(1/k!\) for fixed \(k\); the entire series supplies domination on compact disks. If \(J_{d_j}\) has only negative real roots along \(d_j\to\infty\), Hurwitz excludes every nonreal zero of the limit.

This endpoint avoids proving the full two-parameter Jensen family as a separate task. It does not allow a large-shift theorem to propagate backwards. The elementary example \(w^2+2w+2\), whose derivative is real-rooted, shows why information about differentiated or shifted families can miss the original nonreal pair.

## The shared lesson

Cofinality can remove excessive uniformity demands. Exact convergence can remove unnecessary root-by-root perturbation estimates. Neither operation removes the need to prove a statement for the actual arithmetic sequence or physical form. A correct endpoint is valuable precisely because it tells us how weak that statement is allowed to be.

*Sources:* [II8](#source-ii8) §7; [II9](#source-ii9) §6; [RIII](#source-riii) §9; [AR](#source-ar); [PC](#source-pc); [MC](#source-mc); ARK.


\part{The complete physical Weil form}

# 4. The odd Weil form and its exact embeddings {#ch-weil}

## Translation, reflection, and the arithmetic sum

Fix \(b>0\), and let functions in \(L^2(0,b)\) be extended by zero when their arguments leave the interval. For \(\lambda>0\), define

$$
(S_\lambda u)(x)=\mathbf1_{x+\lambda<b}u(x+\lambda)
                 +\mathbf1_{x>\lambda}u(x-\lambda),
\tag{4.1}\label{eq:4.1}
$$

$$
(R_\lambda u)(x)=\mathbf1_{0<\lambda-x<b}u(\lambda-x).
\tag{4.2}\label{eq:4.2}
$$

These are bounded self-adjoint maps. In this elementary estimate \(\|S_\lambda\|\le2\) and \(\|R_\lambda\|\le1\). The combined odd full-line representation can sometimes improve the bound on \(R_\lambda-S_\lambda\), but that improvement belongs to the combined operator, not to its terms separately.

Let \(\alpha_n=\Lambda(n)/\sqrt n\), where \(\Lambda\) is the von Mangoldt function. Define

$$
q_{\mathrm{arch},b}[u]
=\frac1{4\pi}\int_{\mathbb R}m(t)|\widehat{J_bu}(t)|^2\,dt,
\tag{4.3}\label{eq:4.3}
$$

$$
q_{\mathrm{raw},b}[u]
=q_{\mathrm{arch},b}[u]
+\sum_{n<e^{2b}}\alpha_n
\langle u,(R_{\log n}-S_{\log n})u\rangle,
\tag{4.4}\label{eq:4.4}
$$

$$
q_{\mathrm{comp},b}[u]
=q_{\mathrm{raw},b}[u]-|\ell_b(u)|^2.
\tag{4.5}\label{eq:4.5}
$$

Every prime power with nonzero weight occurs. The cutoff is strict because the endpoint lag has zero overlap in these \(L^2\) forms. Replacing the sum by primes alone would change the operator, although higher powers may later be estimated separately.

## The full-line identity

For a smooth odd \(f=J_bu\), let

$$
H_f(v)=\int_{\mathbb R}f(x+v)\overline{f(x)}\,dx,
\qquad L_\pm(f)=\int_{\mathbb R}e^{\pm x/2}f(x)\,dx.
\tag{4.6}\label{eq:4.6}
$$

Oddness gives \(L_+(f)=\ell_b(u)\) and \(L_-(f)=-\ell_b(u)\). Splitting the correlation at the origin gives

$$
H_f(\lambda)
=\langle u,S_\lambda u\rangle-\langle u,R_\lambda u\rangle.
\tag{4.7}\label{eq:4.7}
$$

The explicit formula in the retained convention is

$$
Q_W(f)=\frac1{2\pi}\int m(t)|\widehat f(t)|^2\,dt
-2\sum_n\alpha_n\operatorname{Re}H_f(\log n)
+2\operatorname{Re}\!\left(L_+(f)\overline{L_-(f)}\right).
\tag{4.8}\label{eq:4.8}
$$

Substitution proves

$$
Q_W(J_bu)=2q_{\mathrm{comp},b}[u].
\tag{4.9}\label{eq:4.9}
$$

Together with \(\|J_bu\|^2=2\|u\|^2\), this identifies the Rayleigh quotients exactly. On \(\ker\ell_b\), the raw and completed forms agree. This last fact is a restriction of the complete operator, not permission to discard the pole before an unrelated decomposition.

## Closed forms and compact resolvent

The digamma series gives \(m(t)\ge m(0)\) and \(m(t)=\log|t|+O(1)\) at large frequency. Thus the shifted Archimedean form norm is equivalent to the norm in (2.10). It is closed and densely defined. At fixed \(b\), the arithmetic sum is finite and bounded; the pole term is bounded rank one. Bounded form perturbation therefore yields closed lower-bounded raw and completed forms on the same domain.

Compactness of the embedding can be seen without treating the logarithmic form as a second-order Sobolev norm. If a family is bounded in the form norm, its Fourier tails satisfy

$$
\int_{|t|>T}|\widehat{J_bu}(t)|^2\,dt
\le\frac{C}{\log(2+T)}.
\tag{4.10}\label{eq:4.10}
$$

The spatial supports are uniformly bounded. Fourier translation criteria then yield compactness in \(L^2\). The associated self-adjoint operator has compact resolvent. This gives a finite-dimensional spectral subspace below any fixed energy level at a fixed aperture; the dimension can grow very rapidly with \(b\).

A form core is obtained by inward dilation, smoothing with an even mollifier, and then an even cutoff near the origin. The last cutoff is harmless because a smooth odd function is \(O(x)\) there. It is important that the approximation takes place in the logarithmic form norm, not merely in \(L^2\).

## Exact old-block nesting

Let \(E_{a,b}\) extend a profile on \((0,a)\) by zero to \((0,b)\), where \(a<b\). Its odd full-line extension is unchanged. Every new lag exceeds the diameter of the old support, and the pole vector restricts exactly. Hence

$$
q_{\mathrm{raw},b}[E_{a,b}u]=q_{\mathrm{raw},a}[u],
\qquad
q_{\mathrm{comp},b}[E_{a,b}u]=q_{\mathrm{comp},a}[u],
\tag{4.11}\label{eq:4.11}
$$

$$
\ell_b(E_{a,b}u)=\ell_a(u).
\tag{4.12}\label{eq:4.12}
$$

This nesting is stronger than agreement of matrix entries in a numerical truncation. It identifies the complete old form inside the new Hilbert space. It is the correct starting point for a block continuation argument.

## Why the pole-neutral space is not a direct sum of neutral pieces

For an old/future split, neutrality is one condition on the complete profile:

$$
\ell_a(u_{\mathrm{old}})+\ell_{(a,b)}(u_{\mathrm{future}})=0.
\tag{4.13}\label{eq:4.13}
$$

It is not equivalent to imposing neutrality only on the old profile and allowing an arbitrary future profile. The finite pole channel must therefore be carried through the split or removed with a legitimate global neutralizing operator. This bookkeeping is the first place where a formally attractive direct-sum proof can change the test space.

*Sources:* [RIII](#source-riii) §2; [II8](#source-ii8), G1 report. Equations (4.1)–(4.13) use the complete half-line convention throughout.

# 5. Arithmetic shells and positive terminal strips {#ch-strips}

## The arithmetic-free canonical diagonal

At integer aperture \(a_N=\frac12\log N\), the next canonical shell is

$$
I_N=(a_N,a_{N+1}),
\qquad |I_N|=\tfrac12\log(1+N^{-1}).
\tag{5.1}\label{eq:5.1}
$$

Two points of this shell have a difference smaller than \(\log2\), so no direct prime-power translation joins them. Their sum lies strictly between \(\log N\) and \(\log(N+1)\), so no logarithm of an integer lies in the reflected window. Consequently the direct compression of the arithmetic part to one shell vanishes exactly.

This is a statement about a diagonal compression. It does not say the shell has no arithmetic interactions with earlier shells. The new-old cross can be large, and the Schur screen of that cross can be adverse. The entire common-cut programme exists because this distinction cannot be ignored.

## A support-measure uncertainty bound

Referee III establishes an elementary lower bound in terms of the measure of a profile's support. If \(u\in\mathcal D_b\) is supported on a measurable set of measure at most \(\delta\), then

$$
q_{\mathrm{arch},b}[u]
\ge\left(\log\frac{\pi}{2\delta}-1-C_0\right)\|u\|^2,
\tag{5.2}\label{eq:5.2}
$$

where

$$
C_0=\gamma+\frac\pi2+2\log2+\log\pi<4.68.
\tag{5.3}\label{eq:5.3}
$$

For completeness, normalize \(f=J_bu\) and put

$$
p(t)=\frac{|\widehat f(t)|^2}{2\pi\|f\|^2}.
\tag{5.4}\label{eq:5.4}
$$

Plancherel gives \(\int p=1\), while the support bound gives \(p(t)\le\delta/\pi\). For \(R>0\),

$$
\int\log|t|p(t)\,dt
\ge\log R-\frac{\delta}{\pi}
\int_{-R}^{R}\log(R/|t|)\,dt
=\log R-\frac{2\delta R}{\pi}.
\tag{5.5}\label{eq:5.5}
$$

Choosing \(R=\pi/(2\delta)\) proves the logarithmic support term. The digamma series supplies \(m(t)\ge\log|t|-C_0\), completing (5.2). The estimate pays for concentration by frequency energy; it does not use a conjectural prime estimate.

## The complete terminal-strip theorem

Let

$$
b\ge10,
\qquad c=10^{-3},
\qquad \delta=cbe^{-b}.
\tag{5.6}\label{eq:5.6}
$$

For every profile supported in \((b-\delta,b)\), the source proves

$$
q_{\mathrm{comp},b}[u]\ge\frac b2\|u\|^2,
\qquad
q_{\mathrm{raw},b}[u]\ge\frac b2\|u\|^2.
\tag{5.7}\label{eq:5.7}
$$

The proof keeps the whole completed form. The support estimate gives

$$
q_{\mathrm{arch},b}[u]
\ge(b-\log b+K)\|u\|^2,
\qquad K=\log(\pi/(2c))-1-C_0>1.
\tag{5.8}\label{eq:5.8}
$$

All direct arithmetic terms vanish because \(\delta<\log2\). A reflected contribution requires

$$
X<n<N,
\quad N=e^{2b},
\quad X=Ne^{-2\delta},
\quad Y=N-X.
\tag{5.9}\label{eq:5.9}
$$

In this range, \(cbe^b\le Y\le2cbe^b\) and \(\log Y\ge b/2\). The unconditional short-interval bound used in the source is \(\pi(X+Y)-\pi(X)<2Y/\log Y\). Since each reflection is a contraction, the total ordinary-prime contribution is bounded in norm by \(32cb\).

For a proper power \(n=a^k\), the number of possible integer bases in the interval is at most

$$
N^{1/k}-X^{1/k}+1
\le\frac{Y}{kX^{1-1/k}}+1
\le\frac{Y}{2\sqrt X}+1.
\tag{5.10}\label{eq:5.10}
$$

There are at most \(2b/\log2\) exponents. The total proper-power contribution is less than one for \(b\ge10\). This estimate overcounts harmlessly; it does not omit repeated prime powers.

Finally, \(g_b(x)^2\le e^b\) on the strip gives

$$
|\ell_b(u)|^2\le\delta e^b\|u\|^2=cb\|u\|^2.
\tag{5.11}\label{eq:5.11}
$$

Taking adverse signs for the entire reflected arithmetic sum and pole gives

$$
q_{\mathrm{comp},b}[u]
\ge[(1-33c)b-\log b+K-1]\|u\|^2
\ge0.717b\|u\|^2.
\tag{5.12}\label{eq:5.12}
$$

The advertised \(b/2\) floor leaves a simple margin and threshold.

## Integer batches and the inverse bound

At \(b=\frac12\log N\), put \(M=\lceil Ne^{-2\delta}\rceil\). The future interval \((\frac12\log M,b)\) lies inside the terminal strip, so its complete and raw direct compressions satisfy

$$
D_{M,N}\succeq\frac{\log N}{4}I,
\qquad
\|D_{M,N}^{-1}\|\le\frac4{\log N},
\tag{5.13}\label{eq:5.13}
$$

and

$$
N-M\sim\frac{\sqrt N\log N}{1000}.
\tag{5.14}\label{eq:5.14}
$$

Thus one local theorem covers many new integer indices. Nevertheless both endpoints move. It gives no arbitrarily remote future compression after an arbitrary old endpoint has been fixed.

## The two iteration traps

The first trap is geometric. Strip width shrinks like \(be^{-b}\); there are exponentially many such strips per macroscopic aperture unit. A local allowance of order \(1/b\), summed blindly, can become \(e^b/b^2\), which is not a permitted cofinal error.

The second trap is algebraic. Eliminating an earlier block changes the next denominator. The theorem above applies to the original direct compression, not automatically to the denominator after previous Schur complements. Any iterative application must either identify the modified denominator with a controlled form or prove a new positive comparison.

The positive-reference method in the next chapter resolves the pure-reference accumulation without pretending that the signed arithmetic part is also paid.

*Sources:* [RIII](#source-riii) §§3–4; [V10B](#source-v10b) §3; canonical-shell records in the September 14 corpus. The explicit constants above are those of the retained Referee III proof.

# 6. A positive reference with exact boundary cancellation {#ch-reference}

## The Green compression

Define

$$
G_b(x,y)=e^{-|x-y|/2}-e^{-(x+y)/2}.
\tag{6.1}\label{eq:6.1}
$$

For \(x,y>0\),

$$
G_b(x,y)=\int_0^\infty
\mathbf1_{t<x}e^{-(x-t)/2}
\mathbf1_{t<y}e^{-(y-t)/2}\,dt.
\tag{6.2}\label{eq:6.2}
$$

This is a genuine positive Gram kernel. Its norm is bounded by four using domination by \(e^{-|x-y|/2}\) and the Schur test.

Put \(B_\lambda=R_\lambda-S_\lambda\). Direct integration of the reflection and translation kernels gives

$$
\int_0^{2b}B_\lambda\,d\lambda=0,
\tag{6.3}\label{eq:6.3}
$$

$$
\int_0^{2b}e^{\lambda/2}B_\lambda\,d\lambda
=|g_b\rangle\langle g_b|+G_b.
\tag{6.4}\label{eq:6.4}
$$

For (6.4), the integral kernel is \(e^{(x+y)/2}-e^{|x-y|/2}\). Expanding \(g_b(x)g_b(y)\) and adding (6.1) gives exactly this expression. The identity explains why a smooth prime-density contribution and the pole must be centered together rather than estimated separately.

## The retained perturbation

Let \(V_{\mathrm{first}}\) be the ordinary-prime sum and \(V_{\mathrm{proper}}\) the proper-prime-power sum. The complete centered perturbation is

$$
V_0=V_{\mathrm{first}}+V_{\mathrm{proper}}
-|g_b\rangle\langle g_b|-G_b.
\tag{6.5}\label{eq:6.5}
$$

The source also writes this as \(Z_0+V_{\mathrm{proper}}-E_0\), where \(Z_0\) is a prime-minus-continuum discrepancy with weight \(e^{\lambda/2}-1/2\), and \(E_0\) is the low-cutoff correction on \((0,\log2)\). Both descriptions are exact. The low-cutoff term cannot be deleted because the prime sum begins at two.

With \(\mu=1-m(0)\), define

$$
H_b^{\mathrm{comp}}=A_{\mathrm{arch},b}+G_b+\mu I,
\qquad
H_b^{\mathrm{raw}}=H_b^{\mathrm{comp}}+|g_b\rangle\langle g_b|.
\tag{6.6}\label{eq:6.6}
$$

Then the same \(V_0\) satisfies

$$
A_{\mathrm{comp},b}+\mu I=H_b^{\mathrm{comp}}+V_0,
\qquad
A_{\mathrm{raw},b}+\mu I=H_b^{\mathrm{raw}}+V_0.
\tag{6.7}\label{eq:6.7}
$$

The shift \(\mu\) remains in every final lower-bound calculation.

## The lowest Archimedean exponential cancels exactly

The lowest nonconstant digamma term is

$$
\frac{4t^2}{t^2+1/4}=4-\frac1{t^2+1/4}.
\tag{6.8}\label{eq:6.8}
$$

The inverse Fourier kernel of \((t^2+1/4)^{-1}\) is \(e^{-|x|/2}\); its odd compression is exactly \(G_b\). Adding \(G_b\) therefore cancels that negative kernel, leaving

$$
H_b^{\mathrm{comp}}=5I+\text{a nonnegative closed form}.
\tag{6.9}\label{eq:6.9}
$$

This is not an approximate cancellation. It holds before a finite-dimensional truncation or a spatial decomposition.

Between adjacent old and future intervals, the remaining kernel is bounded by \(1/[2(s+t)]\), where \(s,t\) are distances to the cut. The Hilbert-kernel Schur test gives

$$
\|(H_b^{\mathrm{comp}})_{OF}\|\le\frac\pi2.
\tag{6.10}\label{eq:6.10}
$$

The raw reference additionally has a pole cross; the completed-reference constant must not be assigned to the raw reference without that term.

## Total reference debt is bounded once

Fix an old aperture \(a\), and let the entire future endpoint \(b>a\) vary. Write

$$
H_b=\begin{pmatrix}H_a&C\\C^*&Q\end{pmatrix}.
\tag{6.11}\label{eq:6.11}
$$

Since \(Q\succeq5I\) and \(\|C\|\le\pi/2\),

$$
0\preceq CQ^{-1}C^*\preceq\frac{\pi^2}{20}I.
\tag{6.12}\label{eq:6.12}
$$

The right side is independent of the remote endpoint. If the future is split into many pieces and eliminated exactly, variational shorting is associative: the final reference short is the infimum over all future variables, irrespective of elimination order. Thus (6.12) is the total pure-reference debt, not a per-strip debt to be summed.

For the raw reference, the corresponding upper allowance is \(\pi^2I/20+|g_a\rangle\langle g_a|\). It is still independent of remote \(b\) for fixed \(a\), but it is not independent of the old aperture.

## The architectural gain

The reference absorbs the singular Archimedean cross and its lowest exponential exactly. It also incorporates the smooth density/pole relation. This removes a false source of repeated loss. What remains is the transported signed perturbation, including its mixed terms. The gain is that the arithmetic question is no longer entangled with an artificial sum of separate reference penalties.

The same lesson was present in V10B's global Archimedean square,

$$
\mathcal D_A(f)=\int_0^\infty
\frac{e^{-s/2}}{1-e^{-2s}}\|f-T_sf\|^2\,ds,
\tag{6.13}\label{eq:6.13}
$$

which retains all collar diagonals and crosses inside one nonnegative integral. The exact reference in (6.6) is the version used by the present Schur calculation; the two expressions should be connected through their stated normalization rather than combined term by term by analogy.

*Sources:* [RIII](#source-riii) §5.1; [COMP](#source-comp) §§2–3; [V10B](#source-v10b) §4. This chapter combines their matching reference statements without changing the arithmetic perturbation.

# 7. Schur reduction and the source that actually survives {#ch-schur}

## The complete block inverse

Let

$$
M=\begin{pmatrix}A&C\\C^*&D\end{pmatrix}\succ0,
\qquad b=\binom uw.
\tag{7.1}\label{eq:7.1}
$$

Set

$$
S=D-C^*A^{-1}C,
\qquad r=w-C^*A^{-1}u.
\tag{7.2}\label{eq:7.2}
$$

Completing the square, or multiplying the block inverse, gives

$$
b^*M^{-1}b=u^*A^{-1}u+r^*S^{-1}r.
\tag{7.3}\label{eq:7.3}
$$

The residual \(r\) is not the raw future component \(w\). It is the source after the same operation that produced the denominator \(S\). This identity is the common algebraic core of the old RESET energy calculation and the later complete-source repairs.

If \(S=L\operatorname{diag}(h_j)L^*\), then

$$
r^*S^{-1}r=\sum_j\frac{|(L^{-1}r)_j|^2}{h_j}.
\tag{7.4}\label{eq:7.4}
$$

Thus a small pivot is dangerous only through its overlap with the transformed source. A global inverse-norm estimate can be much more expensive than the actual source energy.

## Reduction relative to a positive reference

Let \(H\succeq hI>0\) be a closed form on an old/future direct sum, with bounded cross \(C=H_{OF}\), and let \(V\) be bounded self-adjoint. Put \(A=H+V\) and assume the complete future denominator

$$
D=H_{FF}+V_{FF}\succeq dI>0.
\tag{7.5}\label{eq:7.5}
$$

Define

$$
T=H_{FF}^{-1}C^*,
\qquad S_H=H_{OO}-CH_{FF}^{-1}C^*,
\tag{7.6}\label{eq:7.6}
$$

$$
E=V_{OF}-T^*V_{FF},
\tag{7.7}\label{eq:7.7}
$$

$$
W=V_{OO}-V_{OF}T-T^*V_{FO}+T^*V_{FF}T.
\tag{7.8}\label{eq:7.8}
$$

Then

$$
\operatorname{Sch}_F(A)=S_H+W-ED^{-1}E^*,
\qquad S_H\succeq hI.
\tag{7.9}\label{eq:7.9}
$$

To prove it, substitute \(y=z-Tx\). The reference cross vanishes and the complete form becomes

$$
q_A[x,z-Tx]
=\langle x,(S_H+W)x\rangle
+2\operatorname{Re}\langle x,Ez\rangle
+\langle z,Dz\rangle.
\tag{7.10}\label{eq:7.10}
$$

Completing the \(D\)-square proves (7.9). The substitution preserves the old variable, so a lower bound \(-\beta\|x\|^2\), with \(\beta\ge0\), also gives a lower bound \(-\beta(\|x\|^2+\|y\|^2)\) in the original physical norm. No unrecorded norm equivalence is required.

The remaining arithmetic expression is \(W-ED^{-1}E^*\). Its two terms are linked by the transformation. Estimating them separately can remove the very cancellation that (7.9) exposes.

## Quotient first: old ports can be eliminated exactly

For a finite positive matrix \(A\) and column families \(F,E\), define the old-port inverse quotient

$$
\begin{aligned}
\Gamma_A(E\mid F)={}&E^*A^{-1}E\\
&-E^*A^{-1}F(F^*A^{-1}F)^\dagger F^*A^{-1}E.
\end{aligned}
\tag{7.11}\label{eq:7.11}
$$

Let \(P\) be the ordinary physical orthogonal projection onto \(\ker F^*\). The first scout proves

$$
\Gamma_A(E\mid F)
=(PE)^*\bigl((PAP)|_{\ker F^*}\bigr)^{-1}(PE).
\tag{7.12}\label{eq:7.12}
$$

For each coefficient vector \(x\), the left side is the minimum over \(y\) of \(\|A^{-1/2}(Ex-Fy)\|^2\). At a minimizer, \(z=A^{-1}(Ex-Fy)\) satisfies \(F^*z=0\), so \(PAPz=PEx\). Substitution gives (7.12). Redundant ports are handled by the pseudoinverse.

Consequently a correction of the form

$$
\Delta=FCF^*+FT^*+TF^*,\qquad C=C^*,
\tag{7.13}\label{eq:7.13}
$$

has \(P\Delta P=0\). Its mixed terms disappear from this quotient by exact compression. This does not permit removing a genuinely transverse term or enlarging the old-port family until the detector has been removed.

For example,

$$
A_\varepsilon=\begin{pmatrix}\varepsilon^2&\varepsilon/2\\
\varepsilon/2&1\end{pmatrix},\quad F=e_1,\quad E=e_2
\tag{7.14}\label{eq:7.14}
$$

has an arbitrarily bad global lower eigenvalue, yet \(\Gamma_{A_\varepsilon}(E\mid F)=1\). The quotient does not pay for a direction already removed.

## Boundary completion in a graph chart

Suppose the complete matrix is

$$
D=\begin{pmatrix}C&B^*\\B&W\end{pmatrix}\succ0,
\qquad C_0=C-B^*W^{-1}B.
\tag{7.15}\label{eq:7.15}
$$

The triangular compiler

$$
R_D=\begin{pmatrix}I&-B^*W^{-1}\\0&I\end{pmatrix}
\tag{7.16}\label{eq:7.16}
$$

satisfies \(R_DDR_D^*=\operatorname{diag}(C_0,W)\). It must be applied to both old and new source columns.

If the old family is \(F=(L_F,T_F)^T\) with \(T_F\) square and invertible, set

$$
K=L_FT_F^{-1}-B^*W^{-1},
\qquad Y_E=L_E-B^*W^{-1}T_E.
\tag{7.17}\label{eq:7.17}
$$

Then the exact quotient is

$$
\Gamma_D(E\mid F)
=(Y_E-KT_E)^*(C_0+KWK^*)^{-1}(Y_E-KT_E).
\tag{7.18}\label{eq:7.18}
$$

This formula retains the positive boundary completion \(KWK^*\), while also retaining the full residual difference in the numerator. Its hypotheses include an actual graph chart. A source described informally as harmonic does not prove \(Y_E=0\).

## What changes when the background changes

For a pure synthesis Gram \(BB^*\), shorting gives \(B_RP_{\ker B_F}B_R^*\). That identity is not the short of \(BB^*\) plus an arbitrary background. Take \(B=(1,1)^T\) and source \(v=B\). The pure-Gram short and retained source vanish. For \(D=BB^*+I\), the retained short is \(3/2\), the retained source is \(1/2\), and its inverse cost is \(1/6\).

This exact example is the decisive reason the II.5 same-Gram identity does not itself close complete physical funding. Changing the denominator also changes its compiler and residual source. Freezing the old compiled columns while changing the metric is not an invariant operation.

*Sources:* [RIII](#source-riii) Theorem 5.1; [II8](#source-ii8) §5; [II9](#source-ii9) §5; [SC1](#source-sc1) §§quotient and projected funding; [SC2](#source-sc2) §§compiler and boundary completion; RESET sources.

# 8. The infinite complement and the local inverse budget {#ch-tail}

## A fixed-aperture spectral cut

The completed reference \(H_b\) has compact resolvent. In a physical sine basis, the complement note writes it as a diagonal symbol minus a bounded positive boundary correction:

$$
H_b=\operatorname{diag}(h(j\pi/b))-C_b,
\qquad 0\preceq C_b,\quad\|C_b\|\le\pi/2,
\tag{8.1}\label{eq:8.1}
$$

$$
h(t)\ge5+\tfrac12\log(1+4t^2/25).
\tag{8.2}\label{eq:8.2}
$$

It follows that for \(L\ge5\),

$$
\operatorname{rank}\mathbf1_{(-\infty,L]}(H_b)
\le\frac{5b}{2\pi}\exp(L-5+\pi/2).
\tag{8.3}\label{eq:8.3}
$$

This is a dimension estimate, not a numerical construction of an eigenbasis at that cutoff.

The full bounded perturbation satisfies

$$
\|V_b\|\le v_b
:=2\sum_{n<e^{2b}}\frac{\Lambda(n)}{\sqrt n}
+2(\sinh b-b)+4,
\tag{8.4}\label{eq:8.4}
$$

and the retained elementary estimate gives \(v_b\le(16\log2+1)e^b+4\) for \(b\ge1\).

Let \(P=\mathbf1_{(-\infty,L]}(H_b)\), \(Q=I-P\), and \(L>v_b\). The reference cross vanishes at this spectral cut. The complete tail denominator is

$$
D=Q(H_b+V_b)Q\succeq(L-v_b)I_Q.
\tag{8.5}\label{eq:8.5}
$$

The entire mixed debt is bounded by

$$
\begin{aligned}
0\preceq PV_bQD^{-1}QV_bP
&\preceq\frac{PV_b^2P-(PV_bP)^2}{L-v_b}\\
&\preceq\frac{v_b^2}{L-v_b}P.
\end{aligned}
\tag{8.6}\label{eq:8.6}
$$

The middle term is the actual source covariance and is stronger than the scalar endpoint.

## A valid but very large finite core

Taking \(L\ge v_b+v_b^2/\varepsilon\) makes the final error in (8.6) at most \(\varepsilon\). The exact finite effective operator is

$$
K_b=P(H_b+V_b)P-PV_bQD^{-1}QV_bP.
\tag{8.7}\label{eq:8.7}
$$

If \(K_b\succeq-\beta_bP\), then completion of the square gives

$$
A_{\mathrm{comp},b}\succeq-(\mu+\beta_b)I.
\tag{8.8}\label{eq:8.8}
$$

The cost is dimensional. For fixed \(\varepsilon\), the explicit allowance grows on the scale

$$
b\exp\!\bigl(O(e^{2b}/\varepsilon)\bigr).
\tag{8.9}\label{eq:8.9}
$$

Making an infinite tail harmless is therefore not the same as making the retained finite sign problem small. It is, however, a complete complement theorem at each fixed aperture and a valid fallback against the error of certifying only a trial space.

## Energy-relative finite capture

Absolute finite-rank approximation of the unweighted arithmetic perturbation is obstructed by its essential norm. At fixed aperture, the source records an exponentially large lower bound on \(\|V_b-F\|\) for every compact \(F\). This rules out trying to capture a globally small unweighted residual with finitely many ports.

The energy-relative operator is different:

$$
\mathcal K_b=H_b^{-1/2}V_bH_b^{-1/2}.
\tag{8.10}\label{eq:8.10}
$$

It is compact because \(H_b\) has compact resolvent. For \(F_L=PV_bP\), the complete residual satisfies

$$
\|H_b^{-1/2}(V_b-F_L)H_b^{-1/2}\|
\le\frac{c+\sqrt{c^2+4a^2}}2,
\tag{8.11}\label{eq:8.11}
$$

with \(a=v_b/\sqrt{5L}\), \(c=v_b/L\). Thus, for \(0<\eta<1\), a sufficient cutoff is

$$
L\ge\max\left\{5,\frac{v_b}{\eta}+\frac{v_b^2}{5\eta^2}\right\},
\tag{8.12}\label{eq:8.12}
$$

which yields \(-\eta H_b\preceq V_b-F_L\preceq\eta H_b\). One fraction of reference energy pays all tail and mixed terms. The finite condition

$$
(1-\eta)PH_bP+PV_bP\succeq-\beta_bP
\tag{8.13}\label{eq:8.13}
$$

then implies the physical floor (8.8). Conversion back to \(L^2\) is explicit; a negative energy-relative estimate is not silently interpreted as a scalar physical floor.

## A local complete inverse has a rapidly convergent expansion

Return to an original terminal strip from Chapter 5. Use the completed matched reference, write \(Q=H_{FF}\), and set

$$
Z=Q^{-1/2}(V_0)_{FF}Q^{-1/2},
\qquad Y=EQ^{-1/2},
\qquad D=Q+(V_0)_{FF}.
\tag{8.14}\label{eq:8.14}
$$

The source proves

$$
Q\succeq\frac{3b}{4}I,
\qquad\|Z\|\le\frac{67}{375}<\frac15,
\qquad\frac45Q\preceq D\preceq\frac65Q.
\tag{8.15}\label{eq:8.15}
$$

For \(P_r(Z)=\sum_{k=0}^r(-Z)^k\),

$$
-\frac{YY^*}{4\cdot5^r}
\preceq ED^{-1}E^*-YP_r(Z)Y^*
\preceq\frac{YY^*}{4\cdot5^r}.
\tag{8.16}\label{eq:8.16}
$$

This follows from the self-adjoint remainder \((-Z)^{r+1}(I+Z)^{-1}\). The error must be multiplied by the same source Gram; convergence of \(P_r\) alone does not give an absolute budget.

## Paying that source-amplified error

The last source-audit note supplies a deliberately crude bound, used only here. Since \(\Lambda(n)\le2b\), \(\sum_{n<e^{2b}}n^{-1/2}<2e^b\), \(\|g_b\|^2\le e^b\), and \(\|G_b\|\le4\),

$$
\|V_0\|\le13be^b\qquad(b\ge10).
\tag{8.17}\label{eq:8.17}
$$

The completed-reference cross gives \(\|T\|\le2\pi/(3b)<1/4\). Hence \(\|E\|<17be^b\), and

$$
\|Y\|^2\le400be^{2b}.
\tag{8.18}\label{eq:8.18}
$$

Combining with (8.16),

$$
\|ED^{-1}E^*-YP_r(Z)Y^*\|
\le100be^{2b}5^{-r}.
\tag{8.19}\label{eq:8.19}
$$

Choose

$$
r(b)=\left\lceil\frac{4b+4\log b+\log100}{\log5}\right\rceil.
\tag{8.20}\label{eq:8.20}
$$

Then

$$
\|ED^{-1}E^*-YP_{r(b)}(Z)Y^*\|
\le e^{-2b}b^{-3}.
\tag{8.21}\label{eq:8.21}
$$

A linear expansion degree suffices even against this exponential source upper bound. The leading signed expression \(S_H+W-YP_r(Z)Y^*\) is still to be estimated; (8.21) pays the approximation error, not that expression.

The recorded interval-count calculation makes these scalar tolerances summable for the family of original one-cut comparisons. It does not identify the successive denominators of an iterated elimination with the original strips. Also, finite order in \(Z\) is not finite dimension: these remain continuum operators unless a separate spectral reduction is applied.

*Sources:* [COMP](#source-comp) §§3–6 and companion complement certificate; [RIII](#source-riii) Proposition 5.2; INV. The final local inverse calculation is the latest recovered physical addition in this edition.

# 9. Literal arithmetic: carries, generators, and frames {#ch-carries}

## Why integer labels alone do not identify a physical map

A coefficient model indexed by integers is attractive because prime factorization gives exact orthogonal decompositions. The physical space is an interval of real multiplicative coordinates. Passing between the two introduces a within-cell coordinate and carries. Removing those carries changes the operator.

On \(L^2([1,N),dt/t)\), define

$$
(Uf)_n(x)=\frac{f(n+x)}{\sqrt{n+x}},
\qquad 1\le n<N,\quad0\le x<1.
\tag{9.1}\label{eq:9.1}
$$

This is unitary onto \(\bigoplus_{n=1}^{N-1}L^2([0,1),dx)\). Its inverse is \((U^*F)(t)=\sqrt t\,F_{\lfloor t\rfloor}(\{t\})\).

For the truncated dilation \(D_pf(t)=\mathbf1_{pt<N}f(pt)\),

$$
(UD_pU^*F)_n(x)
=\sqrt p\,F_{pn+\lfloor px\rfloor}(\{px\}).
\tag{9.2}\label{eq:9.2}
$$

The carry identity

$$
q\lfloor px\rfloor+\lfloor q\{px\}\rfloor=\lfloor pqx\rfloor
\tag{9.3}\label{eq:9.3}
$$

proves \(D_pD_q=D_{pq}\), including the cutoff. Thus exact multiplicative composition survives in the lifted space only if all branches are retained.

For \(p=2,N=4\), choose \(F_3=1\) and other components zero. Deleting the branch \(\lfloor2x\rfloor=1\) removes squared output norm one. It is not a uniformly small approximation.

## Reflection and old support after changing aperture

Set \(t=e^{x+b}\) and \(f(t)=(J_bu)(\log t-b)\). Oddness becomes

$$
f(N/t)=-f(t),\qquad N=e^{2b}.
\tag{9.4}\label{eq:9.4}
$$

In unweighted coordinates \(G(t)=f(t)/\sqrt t\), the reflection acts by \(G(t)\mapsto\sqrt N\,G(N/t)/t\). The pole functional is

$$
\ell_b(u)=N^{-1/4}\int_1^NG(t)\,dt.
\tag{9.5}\label{eq:9.5}
$$

When an old aperture \(a<b\) is embedded, its support is \([e^{b-a},e^{b+a}]\), not \([1,e^{2a}]\). The exact formula is

$$
G_b(t)=e^{(a-b)/2}G_a(e^{a-b}t)
\tag{9.6}\label{eq:9.6}
$$

on that translated multiplicative support. These formulas are the correct physical dictionary for any subsequent coefficient factorization.

## Coefficient energy and physical fibre energy differ

For an integer basis vector \(e_n\), the prime-tensor number operator gives

$$
\sum_p(\log p)v_p(n)=\log n.
\tag{9.7}\label{eq:9.7}
$$

On a physical \(p\)-fibre \(t=rp^k\), \(1\le r<p\), the number is instead \(\lfloor\log t/\log p\rfloor\). Summing gives

$$
\sum_{p<N}(\log p)\left\lfloor\frac{\log t}{\log p}\right\rfloor
=\sum_{p^k\le t}\log p=\psi(t).
\tag{9.8}\label{eq:9.8}
$$

At \(N=8\), for \(7<t<8\), the right side is \(\log420>\log8\). This positive-measure example disproves the naive identification of the physical generator with a \(\log N\) coefficient budget.

The one-prime Hamiltonians may still be positive. Their physical sum contains a compensating term involving \(\psi(t)\). Dropping the positive Hamiltonian and keeping only the negative potential loses the mechanism rather than estimating it. The correct task is a restricted synthesis or an exact whole-form comparison retaining the compensation.

## A collar frame and its scope

The first-Blaschke collar construction has the form

$$
\mathcal B_n=-\sum_{q=p^k\le n}\beta_qV_q,
\qquad
\beta_q=\left(1-\frac1p\right)\frac{\log p}{p^{k/2}},
\tag{9.9}\label{eq:9.9}
$$

with a tight-frame identity in its declared collar metric,

$$
\mathcal B_n\mathcal B_n^*=s_n^{\mathrm B}I,
\qquad s_n^{\mathrm B}\ge\frac{(\log2)^2}{8}.
\tag{9.10}\label{eq:9.10}
$$

For the batch direct sum \(S=\bigoplus\mathcal B_n\), one obtains a uniform right inverse and a polylogarithmic upper frame bound. The V10B audit uses this to prove that a subpower lower floor for \(S^*DS\) is quantitatively equivalent to a subpower physical lower floor for \(D\).

This is useful conditioning, but not a weaker sign theorem. Surjectivity means every physical adverse direction is still represented. If \(SS^*\succeq a_0I\), then

$$
S^*DS\succeq-eI\quad\Longrightarrow\quad D\succeq-(e/a_0)I.
\tag{9.11}\label{eq:9.11}
$$

Conversely, \(D\succeq-dI\) gives \(S^*DS\succeq-d\|S\|^2I\). At subpower scale these are the same unresolved comparison.

## The safe use of a coefficient model

A coefficient identity can expose cancellation, decompose prime history, or identify a phase. To become a physical estimate, the analysis map and synthesis map must be stated with their actual norms. Their dependence on the cutoff and the old stage must be visible. An orthogonal decomposition before synthesis does not imply that the synthesized prime columns are orthogonal afterward.

This is why the carry-preserving lift and generator comparison belong near the beginning of the physical exposition. They prevent an abstract Hilbert-space lemma from being attached to the wrong arithmetic operator.

*Sources:* [RIII](#source-riii) §6; [II9](#source-ii9) §3 and global-Gram repair; [V10B](#source-v10b) §§1–3; [V12](#source-v12) and the September 23 literal-placement notes, read with [II8](#source-ii8)–II9.

# 10. Funding a direction rather than a whole inverse {#ch-funding}

## The augmented source matrix

Let \(D\succ0\) be the actual complete denominator and \(v\) the actual source. Then

$$
v^*D^{-1}v\le C
\quad\Longleftrightarrow\quad
\begin{pmatrix}D&v\\v^*&C\end{pmatrix}\succeq0.
\tag{10.1}\label{eq:10.1}
$$

For \(C>0\), this is also equivalent to \(D\succeq vv^*/C\). It is a rank-one comparison; funding every column of a larger birth synthesis is unnecessary if the proof consumes only this source.

For several sources \(V\), the scalar \(C\) is replaced by a coefficient-space Gram \(C_0\), and the inequality is \(V^*D^{-1}V\preceq C_0\). The mixed entries in that Gram are part of the assertion.

## Actual source fitting with a residual

If an explicit comparison proves

$$
D\succeq FF^*+dI,\qquad d>0,
\tag{10.2}\label{eq:10.2}
$$

then

$$
v^*D^{-1}v
\le\inf_c\left(\|c\|^2+\frac{\|v-Fc\|^2}{d}\right).
\tag{10.3}\label{eq:10.3}
$$

The equality of the infimum with \(v^*(FF^*+dI)^{-1}v\) follows from the normal equations. This is a legitimate alternative to exact transverse annihilation. It requires a quantitative residual in the actual physical norm and a reserve \(d\) that survives in the complete denominator.

A small coefficient residual is not automatically a small physical residual after an unbounded or poorly conditioned synthesis. The map must remain in the formula.

## Regular and finite-port pieces

For

$$
D=\begin{pmatrix}A&K\\K^*&E\end{pmatrix},
\qquad v=\binom{v_R}{v_P},
\tag{10.4}\label{eq:10.4}
$$

put

$$
S=E-K^*A^{-1}K,
\quad w=v_P-K^*A^{-1}v_R,
\quad \alpha=v_R^*A^{-1}v_R.
\tag{10.5}\label{eq:10.5}
$$

The complete debt is \(\alpha+w^*S^{-1}w\). If

$$
S=\begin{pmatrix}a&b\\\overline b&d\end{pmatrix}\succ0,
\qquad w=\binom xy,
\tag{10.6}\label{eq:10.6}
$$

then a budget \(C\) is equivalent to

$$
(C-\alpha)(ad-|b|^2)
\ge d|x|^2+a|y|^2-2\operatorname{Re}(\overline xby).
\tag{10.7}\label{eq:10.7}
$$

The pole/boundary mixed term is explicit. An estimate that replaces it by two unrelated norms can be much weaker. A favorable two-by-two determinant also does not certify the omitted regular complement: positivity of \(A\) and of \(S\) are premises of the calculation.

## A proved gain reduces debt only through its source overlap

Suppose the complete denominator admits \(D=D_0+UU^*\), with \(D_0\succeq dI>0\), and every residual already included in \(D_0\). Then

$$
\begin{aligned}
BD_0^{-1}B^*-BD^{-1}B^*
={}&BD_0^{-1}U(I+U^*D_0^{-1}U)^{-1}\\
&\hspace{18mm}\cdot U^*D_0^{-1}B^*.
\end{aligned}
\tag{10.8}\label{eq:10.8}
$$

The right side is nonnegative. If a favorable update is orthogonal to the source in the \(D_0^{-1}\) metric, it provides no saving. For several gains, concatenate their columns before forming \(U^*D_0^{-1}U\); separate diagonal treatment discards interactions and requires justification.

This identity gives the correct interpretation of a local geometric or clock-derived gain. It must first be a comparison for the complete denominator, then it must overlap the debt source. Rank alone proves neither condition.

## Low-energy overlap rather than a global spectral gap

For a positive finite operator \(A\), define the source spectral mass

$$
M_E(s)=E^*\mathbf1_{(0,s]}(A)E.
\tag{10.9}\label{eq:10.9}
$$

The spectral theorem gives

$$
E^*A^{-1}E=\int_0^\infty M_E(s)\,\frac{ds}{s^2}.
\tag{10.10}\label{eq:10.10}
$$

If \(M_E(s)\preceq CsI\) below one and the high-energy inverse contribution is at most \(H_0I\), then

$$
E^*A^{-1}E
\preceq\left[H_0+C\left(1+\log\frac1{\lambda_{\min}(A)}\right)\right]I
\tag{10.11}\label{eq:10.11}
$$

when \(\lambda_{\min}(A)<1\). Exponentially small eigenvalues then cost only a logarithm, provided the source avoids them at the displayed rate.

The example \(A=\operatorname{diag}(\varepsilon^2,1)\), \(E=(\varepsilon,1)^T\), has inverse energy two despite \(\|A^{-1}\|=\varepsilon^{-2}\). This illustrates the potential gain, not a proof that the native source has the required spectral overlap.

## A whole-positive-block alternative

II.9 also gives an alternative that does not invert the birth Gram at all. For bounded maps \(B,C\),

$$
\mathcal G(B,C)=
\begin{pmatrix}C^*C&C^*B^*\\BC&BB^*\end{pmatrix}\succeq0,
\tag{10.12}\label{eq:10.12}
$$

because its form is \(\|Cx+B^*y\|^2\). If the actual full operator is

$$
A_N=\operatorname{diag}(A_M-C^*C,D_0)+\mathcal G(B,C)+R,
\tag{10.13}\label{eq:10.13}
$$

with \(C^*C\preceq cI\), \(D_0\succeq-sI\), \(A_M\succeq-b_MI\), and complete \(R\succeq-rI\), then

$$
A_N\succeq-[\max\{b_M+c,s\}+r]I.
\tag{10.14}\label{eq:10.14}
$$

The positive square is dropped as a whole. This tolerates a large or rank-deficient \(B\). The burden is the exact arithmetic decomposition (10.13) with its complete residual. A coefficient-to-fibre substitution contradicted by (9.8) cannot supply that decomposition.

*Sources:* [II9](#source-ii9) §§4–6 and directional-funding proof; [COMP](#source-comp) §5; [SC2](#source-sc2) source spectral-mass lemma. These are alternative sufficient mechanisms, not a demand to prove all of them simultaneously.

# 11. The referee sequence: repairs and the interfaces they leave {#ch-referee-history}

## The September 23 candidate

The first referee-facing Brehmer–Schur candidate assembled common-product current-prime placement, literal first-Blaschke columns, physical collar frames, and chronological dyadic control. Its intended estimate was a polylogarithmic inverse debt, sufficient for the adaptive staircase. The actual input space of the coefficient row and the norm of its physical postprocessor were decisive.

The later audit found that reading the row as a common-input stack produces a large norm already on one basis vector. Reading it as independent prime components gives a different, elementary bounded operator, but does not identify that operator with the complete physical cross. The two readings cannot be interchanged during a proof.

## The September 24 pole extraction

A raw first-prime wide cross has a large smooth component. The R2 calculation extracts it exactly:

$$
B_{a,b}^{(1)}=P_{a,b}+E_{a,b}-C_{a,b},
\tag{11.1}\label{eq:11.1}
$$

$$
(P_{a,b}g)(x)=-2\sinh(x/2)\int_a^be^{y/2}g(y)\,dy.
\tag{11.2}\label{eq:11.2}
$$

The correction \(C_{a,b}\), from the extra \(p^{-1}\) factor, is bounded by the convergent sum \(2\sum_p(\log p)p^{-3/2}\). Proper prime powers have a separate lower-order budget. The smooth carrier is not small; it belongs to the pole channel.

The amended candidate then tried to place only the centered regular packet and to keep the pole/boundary channel in a finite soft ledger. It replaced a literal strong-limit lifetime row by a uniform finite-horizon Gram majorant. That is logically safer if the actual majorant is proved, because rows at different horizons need not be consistent truncations of one operator.

## The historical freeze and the scoped G5 repair

The frozen II.1 record did mark all six Layer-1 gates PASS while retaining a separate global proof flag. II.9 confirms this history. Later reopening is permitted by the audit protocol when a scope, metric, domain, dependency, or quantifier mismatch is found. The historical PASS record is neither erased nor treated as immutable mathematical evidence.

II.5 addressed a particular post-short E1 component. Its source decomposition separated the regular pole-neutral piece from a rank-one centered pole part. It then used a two-coordinate Cauchy state for homogeneous solutions of \(u''-u/4=0\), with transfer matrix

$$
F_\lambda=
\begin{pmatrix}
\cosh(\lambda/2)&2\sinh(\lambda/2)\\
\tfrac12\sinh(\lambda/2)&\cosh(\lambda/2)
\end{pmatrix}.
\tag{11.3}\label{eq:11.3}
$$

For a genuinely port-supported update \(E=CH\), the Woodbury normalization simplifies exactly. The same-Gram inverse identity also holds. The unresolved issue is whether the complete post-short arithmetic source and screen satisfy those port-support and metric assumptions.

## Why finite rank did not prove port support

Let \(A\succ0\) and \(C\) have independent columns. Put

$$
P=A^{-1/2}C(C^*A^{-1}C)^{-1}C^*A^{-1/2}.
\tag{11.4}\label{eq:11.4}
$$

The favorable and adverse normalization denominators are

$$
S_+=I+E^*A^{-1/2}(I-P)A^{-1/2}E,
\tag{11.5}\label{eq:11.5}
$$

$$
S_-=I-U^*A^{-1/2}(I-P)A^{-1/2}U.
\tag{11.6}\label{eq:11.6}
$$

The identity \(S_+=I\) therefore requires actual range containment. For \(A=I_3\), \(C=[e_1,e_2]\), \(E=e_3\), one gets \(S_+=2\). For a nearly transverse adverse vector, \(S_-\) can be arbitrarily small while the full update remains positive. Omitting this inverse can underestimate the screen by an arbitrarily large factor.

Two state coordinates per individual prime tooth are not necessarily one common two-dimensional physical range across all teeth. A fixed common extractor must be exhibited.

## The growing-shift repair and the stale fixed-shift use

Suppose the actual coherent block obeys

$$
A_E\succeq-O(\log L)I,
\quad C_N\succeq(L-o(L))I,
\quad\|Z_E\|^2\le(\tfrac12+o(1))L^2,
\quad L=\log N.
\tag{11.7}\label{eq:11.7}
$$

Adding the same \(s_N=\sigma L+O(\log L)\) to both diagonals gives fresh Schur floor

$$
S_E\succeq
\left(\sigma-\frac1{2(1+\sigma)}-o(1)\right)LI.
\tag{11.8}\label{eq:11.8}
$$

For \(\sigma=1/2\), this is \((1/6-o(1))LI\). The two-block model

$$
D_L=L\begin{pmatrix}0&1/\sqrt2\\1/\sqrt2&1\end{pmatrix}
\tag{11.9}\label{eq:11.9}
$$

shows why this does not imply any fixed-shift theorem: \(\lambda_{\min}(D_L+s_*I)=s_*-(\sqrt3-1)L/2\), eventually negative. A later argument still consuming the unshifted or fixed-shift premise is stale even if the growing-shift calculation is correct.

## The actual unweighted centered-norm obstruction

II.9 goes beyond the small-model objections. For the complete unweighted old/future spaces it constructs high-frequency tests and proves

$$
\|P_a^0E_{a,b}\|_{L^2(a,b)\to L^2(0,a)}
=\Theta_a(e^{b/2}).
\tag{11.10}\label{eq:11.10}
$$

At fixed \(b\), simultaneous recurrence makes the finitely many prime phases nearly align. A terminal bump modulated by these frequencies has direct and reflected envelopes of size \(e^{b/2}\), by the ordinary prime number theorem. The modulation makes their interference and any fixed finite-dimensional pole projection vanish in the limit. Only after taking this high-frequency limit is \(b\) increased.

The order of limits is allowed by an unrestricted operator norm. It does not produce a negative complete Weil-form witness: its Archimedean frequency energy may be very large. Restricted source ranges, frequency cutoffs, or inverse-energy estimates are not refuted by (11.10).

## The source-level reconciliation

The governing history is consequently: candidate placement, pole extraction, scoped repairs, then explicit reopening of the stronger assembled interfaces. G1's complete form and G6's detector remain available in their repaired scope. The physical placement, complete future funding, and cofinal arithmetic assembly remain mathematical obligations.

Referee III responds by proving local complete-form theorems directly and stating the remaining signed estimate. It does not rely on calling a corrected hypothesis already certified. II.9 further clarifies that whole-Gram domination and one fixed global shift are sufficient approaches, not uniquely necessary approaches; direct positive-block completion and adaptive same-horizon bounds are legitimate alternatives.

*Sources:* [V12](#source-v12), [RII](#source-rii), [II1](#source-ii1) source freeze, [II5](#source-ii5), [II8](#source-ii8), [II9](#source-ii9), RIII. The chapter is a chronological reconciliation of those sources, not a new vote on their labels.

# 12. Exponential detection on the full test space {#ch-detector}

## The spectral pairing must retain conjugation correctly

Let \(\Gamma\) denote the zeros of \(\Xi\), with multiplicities. For a compact smooth test,

$$
Q(f)=\sum_{\gamma\in\Gamma}m_\gamma
\widehat f(\gamma)\overline{\widehat f(\overline\gamma)}.
\tag{12.1}\label{eq:12.1}
$$

Under RH this becomes a sum of nonnegative absolute squares. Before RH it is a different pairing, and replacing it by absolute squares would assume the desired sign.

Define \(\nu_0(a)\) as the infimum of \(Q(f)/\|f\|^2\) over nonzero compact smooth odd tests supported in \((-a,a)\), with both polar transforms zero. The retained detector proves that an off-real zero of \(\Xi\) implies

$$
\nu_0(a)\le-e^{ca}\qquad(a\ge a_0)
\tag{12.2}\label{eq:12.2}
$$

for some \(c>0\). The constants may depend on the selected zero; no uniform zero-displacement bound is needed.

## Selecting a quartet without a rightmost-zero assumption

Choose an off-real zero \(\gamma_0=x_0+iy_0\), with \(x_0>0\), \(y_0\ne0\). For a real parameter \(\omega\) near \(x_0\), define

$$
\eta_\gamma(\omega)=y^2-(x-\omega)^2.
\tag{12.3}\label{eq:12.3}
$$

Only finitely many zeros can have positive score for \(\omega\) in a fixed small interval, since \(|y|<1/2\) and the zero set is locally finite. The difference of scores for distinct quartet representatives is affine in \(\omega\), and is not identically zero. Avoiding finitely many ties and the candidate abscissae yields one unique maximizing quartet, with \(\eta_*>0\) and \(x_*-\omega\ne0\).

This selects a maximum of a localized Gaussian score, not a maximum real part of the entire zero set. It therefore requires no rightmost off-line zero.

## A sign-controlled spectral test

Set \(P(z)=z^2+1/4\), and

$$
F_\tau(z)=P(z)\left[e^{-\tau(z-\omega)^2}
-e^{-\tau(z+\omega)^2}\right],\qquad\tau\ge1.
\tag{12.4}\label{eq:12.4}
$$

The transform is odd and real-entire. Its spectral pairing equals \(F_\tau(\gamma)^2\), not \(|F_\tau(\gamma)|^2\). The maximizing quartet contributes

$$
4m_*e^{2\eta_*\tau}
\operatorname{Re}\{w e^{-i\theta\tau}\}
+o(e^{2\eta_*\tau}),
\tag{12.5}\label{eq:12.5}
$$

where \(w=P(\gamma_*)^2\ne0\) and \(\theta=4(x_*-\omega)y_*\ne0\). Choose the positive terms of the real arithmetic progression on which \(\arg w-\theta\tau=\pi\pmod{2\pi}\). The leading contribution is then negative.

The other quartets in a bounded range have a strict score deficit. Outside that range, Gaussian decay dominates the polynomial zero count. The whole auxiliary spectral sum is absolutely convergent and is eventually bounded above by \(-C_*e^{2\eta_*\tau}\) on the selected progression.

## Compact support and exact pole neutralization

The inverse transform before filtering is

$$
h_\tau(x)=\frac{i}{\sqrt{\pi\tau}}e^{-x^2/(4\tau)}\sin(\omega x).
\tag{12.6}\label{eq:12.6}
$$

Choose an even smooth cutoff \(\chi\), equal to one on \([-1,1]\) and supported in \((-2,2)\). Put

$$
g_\tau(x)=\chi(x/(4\tau))h_\tau(x),
\qquad
f_\tau=(-\partial_x^2+1/4)g_\tau.
\tag{12.7}\label{eq:12.7}
$$

Then \(f_\tau\) is compactly supported in \((-8\tau,8\tau)\), odd, and exactly pole neutral because

$$
\widehat f_\tau(z)=(z^2+1/4)\widehat g_\tau(z).
\tag{12.8}\label{eq:12.8}
$$

No approximate polar cancellation is used. The test is nonzero by injectivity of the differential filter on compact smooth functions.

For \(|\operatorname{Im}z|\le1/2\), repeated integration by parts gives

$$
|\widehat f_\tau(z)-F_\tau(z)|
\le C_J(1+\tau)^{M_J}e^{-2\tau}
(1+|\operatorname{Re}z|)^{-J}.
\tag{12.9}\label{eq:12.9}
$$

The zero-counting bound turns this into a complete quadratic-form error of order \((1+\tau)^Me^{-7\tau/4}\). The norm of \(f_\tau\) has only polynomial growth. Thus its Rayleigh quotient remains exponentially negative on the phase-aligned progression.

## Every sufficiently large aperture

If the progression spacing is \(d_0=2\pi/|\theta|\), take the largest aligned \(\tau\le a/8\). For large \(a\), it satisfies \(\tau\ge a/16\), so the compact witness fits inside the aperture and gives (12.2). This proves the conclusion at every large aperture, not merely on a favorable subsequence.

It follows that an arbitrarily sparse cofinal lower-bound sequence can contradict the detector. What matters is that each lower bound applies to the full test class containing these witnesses. A favorable finite-dimensional compression does not suffice unless the complement or approximation error is controlled well enough to retain the witness.

## What the detector does not require from the research programme

It uses the classical explicit formula, zero symmetry, local finiteness, a polynomial zero count, and the absence of real nontrivial zeta zeros. It does not use a numerical zero list, simplicity, a rightmost off-line zero, or the old Brehmer placement theorem. The main remaining dependency is therefore not spectral detection. It is the complete physical lower floor that must be placed against it.

*Sources:* [II8](#source-ii8) G6 independent report, especially the generic quartet selection and compactification proof; [RIII](#source-riii) §9; [RII](#source-rii) appendix. The variable \(\tau\) here is the Gaussian concentration parameter, not the heat deformation parameter of Chapter 22.


\part{Arithmetic cancellation and the complete response}

# 13. Finite Euler algebra and the surviving bilinear sum {#ch-euler}

## Exact finite convolution before compression

On the full finite Mellin interval, the truncated dilations satisfy \(D_mD_n=D_{mn}\) and vanish beyond the cutoff. Hence

$$
Z_N(s)=\sum_{n<N}n^{s-1/2}D_n,
\qquad M_N(s)=\sum_{n<N}\mu(n)n^{s-1/2}D_n
\tag{13.1}\label{eq:13.1}
$$

obey

$$
M_N(s)Z_N(s)=Z_N(s)M_N(s)=I.
\tag{13.2}\label{eq:13.2}
$$

These are finite divisor-convolution identities. The logarithmic derivative retains all prime powers:

$$
\mathcal L_N=\sum_{n<N}\frac{\Lambda(n)}{\sqrt n}D_n
=\sum_{p<N}(\log p)R_p(I-R_p)^{-1},
\quad R_p=p^{-1/2}D_p.
\tag{13.3}\label{eq:13.3}
$$

The full towers must be formed before odd compression. In general \(PD_p^kP\ne(PD_pP)^k\), because an intermediate trajectory can leave the compressed subspace and return. An exact finite Euler identity on the full space is not automatically the same identity for the compressed one-step generator.

For \(T_N(s)=M_N(s)Z_N(0)\),

$$
T_N(s)-zI=M_N(s)\bigl(Z_N(0)-zZ_N(s)\bigr).
\tag{13.4}\label{eq:13.4}
$$

The left factor is independent of the cyclic phase \(z\). This matters when a finite difference must be formed before physical postprocessing. It does not bound that postprocessor's norm.

## One-prime Poisson cancellation and weighted rows

For one prime, let

$$
T_{p,\theta}=(I-e^{i\theta}R_p)(I-R_p)^{-1},
\quad
K_{p,\theta}=(I-R_p^*R_p)^{1/2}(I-e^{i\theta}R_p)^{-1}.
\tag{13.5}\label{eq:13.5}
$$

Direct multiplication gives \(K_{p,\theta}T_{p,\theta}=K_{p,0}\). If an independent cyclic shift \(S\) acts on a separate factor, then

$$
K_{p,\theta}(T_{p,\theta}-S)=K_{p,0}-SK_{p,\theta}.
\tag{13.6}\label{eq:13.6}
$$

The same left map acts on both halves of the gap. This is the appropriate algebraic ordering; introducing two unrelated inverse gauges can destroy it.

At critical increment \(h=1/\log N\),

$$
U_{p,h}=(1-e^{ih\log p})R_p(I-R_p)^{-1}
\tag{13.7}\label{eq:13.7}
$$

satisfies

$$
\sum_{p<N}\frac{\|U_{p,h}\|^2}{\log p}
\ll\frac1{\log N}.
\tag{13.8}\label{eq:13.8}
$$

Indeed \(\|R_p\|\le p^{-1/2}\) and \(|1-e^{ix}|\le|x|\), so the sum is bounded by \((\log N)^{-2}\sum_{p<N}(\log p)/(\sqrt p-1)^2\). The ordinary Mertens-type estimate gives the stated scale. This controls a specified coefficient row; the physical placement remains a separate assertion.

## Largest-prime decomposition and its domain

Every integer \(1<n<N\) has a unique representation \(n=p^km\), with \(p=P^+(n)\), \(k\ge1\), and \(P^+(m)<p\). This gives an orthogonal decomposition before physical synthesis. On the first-harmonic coefficient slice,

$$
J_p^*D_NJ_p=D_{<p,N/p}+\log p.
\tag{13.9}\label{eq:13.9}
$$

The source's common-product identity applies a spectral multiplier in the complete Euler product and then recovers the lower-prime component by an orthogonal projection. This avoids an uncontrolled simultaneous Hardy boundary evaluation. But a stack of copies of one common input is not the same as a direct sum of independent prime inputs. The II8 counterexample exploits exactly that distinction.

The raw physical logarithmic derivative and the birth-normalized coefficient row therefore remain distinct until a literal map with an explicit norm is supplied. This is where the narrow harmonic or shell result must be attached, not where it may be assumed.

## Exact pole neutrality pays the Type I main terms

A later arithmetic checkpoint works directly on \(u\in H_0^1(0,b)\), with \(\ell_b(u)=0\) and \(\|u'\|\le T\|u\|\). Let \(f=J_bu\), \(r=\|u\|^2\), and

$$
W(x)=x^{-1/2}H_f(\log x).
\tag{13.10}\label{eq:13.10}
$$

The autocorrelation identity

$$
\int_0^\infty(e^{av}+e^{-av})H_f(v)\,dv
=-\left|2\int_0^b\sinh(ax)u(x)\,dx\right|^2
\tag{13.11}\label{eq:13.11}
$$

implies, at \(a=1/2\), cancellation of the right side and its first derivative. The checkpoint obtains

$$
\left|\int_1^\infty W(x)\,dx\right|\le4r,
\qquad
\left|\int_1^\infty\log x\,W(x)\,dx\right|\le8r.
\tag{13.12}\label{eq:13.12}
$$

Thus neutrality controls continuous Type I main terms, not just lattice errors.

For \(U,V\ge2\), the exact Vaughan decomposition then yields

$$
q_{\mathrm{raw}}[u]
=q_{\mathrm{arch}}[u]-\mathcal B_{U,V}(u)+E(u),
\tag{13.13}\label{eq:13.13}
$$

where

$$
\mathcal B_{U,V}(u)
=\sum_{\substack{m>U,\ n>V\\mn<N}}
\frac{\mu(m)\beta_V(n)}{\sqrt{mn}}H_f(\log(mn)),
\quad
\beta_V(n)=\sum_{\substack{d\mid n\\d>V}}\Lambda(d),
\tag{13.14}\label{eq:13.14}
$$

and

$$
|E(u)|\le C(U,V,T)r,
\tag{13.15}\label{eq:13.15}
$$

$$
\begin{aligned}
C(U,V,T)={}&4\sqrt V\log V
+16(3+T)\sqrt U\\
&+8(3+2T)\sqrt{UV}\log V.
\end{aligned}
\tag{13.16}\label{eq:13.16}
$$

For \(U=V=\lceil e^{\sqrt{\log N}}\rceil\) and fixed \(T\), this is subpower in \(N\). The surviving sum is genuinely two-variable and signed. The two factors exceed growing cutoffs; they need not be comparable in size.

The compact pole-filtered Gaussian detector has bounded derivative-to-norm ratio for each fixed carrier family. Thus an upper bound of the required scale for (13.14) on those detector packets would suffice as an alternative endpoint. It is not supplied by the decomposition itself.

## Young atoms: a separate local budget

Call \(\delta=2b-\log n\) the age of an arithmetic atom. For \(0<\delta<b\), its direct translation has not entered the positive interval; its contribution is a terminal reflection. Let \(Y_b\) contain all prime powers with \(0<\delta\le e^{-b}/64\), and let \(\mathsf H=A_{\mathrm{arch}}-m(0)I+I\). The checkpoint proves

$$
q_{\mathsf H}[u]+q_{Y_b}[u]
\ge\tfrac34q_{\mathsf H}[u]
-\frac{be^{-b/2}}{256\pi}\|u\|^2
\qquad(b\ge8).
\tag{13.17}\label{eq:13.17}
$$

This is a complete continuum estimate for the declared youngest layer. It uses elementary counting and a concentration bound, not a prime-discrepancy hypothesis. As atoms age they leave the layer; the same quarter of reference energy cannot be spent anew indefinitely.

The young-layer and Vaughan decompositions analyze the same complete arithmetic form in different ways. Their gains cannot simply be added as disjoint resources. A combined argument needs an exact allocation showing which terms each estimate pays.

*Sources:* [RIII](#source-riii) §6; [II8](#source-ii8) G1–G2; [RII](#source-rii) §§4–5; [GAP](#source-gap) arithmetic-progress and Type II proof; young-birth jet note. The later signed bilinear target is kept separate from the earlier coefficient-row target.

# 14. Coherent rational interactions and harmonic boundary data {#ch-rational}

## A fixed source does not pay a collar-count factor

Let \(U_q\) be the appropriate full-line translation for one arithmetic label, and let \(P_n\) be orthogonal collar projections. For a fixed source,

$$
\sum_n\|P_nU_qP_Ef\|^2=\|P_EU_qP_Ef\|^2\le\|f\|^2.
\tag{14.1}\label{eq:14.1}
$$

This prevents an artificial factor equal to the number of future collars. The unresolved accumulation is cross-source coherence, not subdivision of a single source's lifetime.

After inserting two birth syntheses around an arithmetic operator, however, one obtains compositions involving three labels. With orientation signs \(\eta_q,\eta_s,\eta_r\in\{\pm1\}\), write

$$
y=\log q+\eta_qu,
\quad y=\log s+\eta_sx,
\quad x=\log r+\eta_rv.
\tag{14.2}\label{eq:14.2}
$$

Eliminating intermediate coordinates gives

$$
u=\eta_q(\log s+\eta_s\log r-\log q)
+\eta_q\eta_s\eta_rv.
\tag{14.3}\label{eq:14.3}
$$

Its multiplicative scale is

$$
\left(\frac{s r^{\eta_s}}q\right)^{\eta_q}.
\tag{14.4}\label{eq:14.4}
$$

Even all-direct orientations give \(sr/q\), which need not be integral. Thus the meaningful split is divisibility and semigroup closure, not simply direct versus reflected orientation. The rational scales must be represented in the physical cell geometry rather than deleted by a coefficient orthogonality relation that no longer applies after the middle operator is inserted.

## Exact Blaschke-adapted centering

For first-prime weights \(a_p=1-p^{-1}\), use logarithmic bands \(\mathcal P_j\) of width at most \(\Delta\). Define

$$
c_j^{\mathrm B}
=\frac{\sum_{p\in\mathcal P_j}a_p(\log p)^2/p}
{\sum_{p\in\mathcal P_j}a_p(\log p)/p},
\qquad \delta_p^{\mathrm B}=\log p-c_j^{\mathrm B}.
\tag{14.5}\label{eq:14.5}
$$

The center is a positive weighted average, so \(|\delta_p^{\mathrm B}|\le\Delta\), and

$$
\sum_{p\in\mathcal P_j}a_p\delta_p^{\mathrm B}\frac{\log p}{p}=0.
\tag{14.6}\label{eq:14.6}
$$

This is exact return nulling. The variance obeys

$$
\sum_{p<N}\frac{a_p^2|\delta_p^{\mathrm B}|^2}{p}
\ll\frac{(\log N)^2\log\log N}{K^2}
\quad\text{when }\Delta=\frac{\log N}{K}.
\tag{14.7}\label{eq:14.7}
$$

The retained source analysis bounds the centered forward and adjoint clouds. At \(K=N^\kappa\), \(\kappa>1/2\), the displayed bounds tend to zero in their declared scope. This removes many terms with at least one centered birth leg. The coherent–coherent, nondivisible rational component still requires its same-metric estimate. The later audits also require the physical identification behind any imported cloud bound to be retained explicitly.

## A compact exact representation of actual sine matrices

The harmonic study supplies a different reduction, directly in the physical trial space. Let

$$
\phi_i(x)=\sqrt{2/b}\sin(q_ix),\quad q_i=i\pi/b,
\quad z_i=q_i^2,\quad d_i=\phi_i'(b).
\tag{14.8}\label{eq:14.8}
$$

Define

$$
a_b(t)=m(t)-2\sum_{n<e^{2b}}\alpha_n\cos(t\log n),
\tag{14.9}\label{eq:14.9}
$$

$$
H_b(z)=\sum_{k\ge0}\frac{1-e^{-2\lambda_kb}}{\lambda_k^2+z}
+\sum_{n<e^{2b}}\alpha_n\frac{\sin(\sqrt z\log n)}{\sqrt z},
\quad \lambda_k=2k+\tfrac12.
\tag{14.10}\label{eq:14.10}
$$

The sine quotient is entire in \(z\). Let \(\mathcal L_H\) be the Loewner divided-difference matrix, with derivative on its diagonal. The complete finite raw matrix is

$$
A=D_d\mathcal L_HD_d+
\operatorname{diag}(a_b(q_1),\ldots,a_b(q_d)),
\quad D_d=\operatorname{diag}(d_i).
\tag{14.11}\label{eq:14.11}
$$

No term in (14.11) is claimed positive separately. The Archimedean contribution is the divided difference of \((\lambda_k^2+z)^{-1}\); the arithmetic term comes from exact sine overlaps. The known diagonal multiplier is indispensable.

## Rank-two displacement, not rank-two matrix

Let \(Z=\operatorname{diag}(z_i)\), \(d=(d_i)\), and \(v_i=d_iH_b(z_i)\). Then

$$
[Z,A]=vd^*-dv^*.
\tag{14.12}\label{eq:14.12}
$$

Thus the commutator has rank at most two. The matrix \(A\) itself may have full rank and many negative directions. Its diagonal and two boundary generators determine all off-diagonal entries. This is a genuine reduction in representation and elimination cost, not a coercivity estimate.

The pole coordinates satisfy

$$
\gamma_i=\langle g_b,\phi_i\rangle
=-\frac{\beta d_i}{z_i+1/4},
\qquad Z\gamma=-\tfrac14\gamma-\beta d,
\quad\beta=g_b(b).
\tag{14.13}\label{eq:14.13}
$$

For an isometry \(U\) onto \(\gamma^\perp\), define

$$
A_0=U^*AU,
\quad Z_0=U^*ZU,
\quad d_0=U^*d,
\tag{14.14}\label{eq:14.14}
$$

$$
v_0=U^*v-\frac{\beta}{\|\gamma\|^2}U^*A\gamma.
\tag{14.15}\label{eq:14.15}
$$

Then \([Z_0,A_0]=v_0d_0^*-d_0v_0^*\). The extra mixed term in \(v_0\) is exactly what a naive projection would miss. The compressed displacement nodes interlace the original \(z_i\) and solve \(\sum_i|\gamma_i|^2/(z_i-\zeta)=0\).

## The structure survives a complete coordinate Schur step

Partition \(A\) and the diagonal nodes into old and future coordinates. For invertible \(D+sI\), define

$$
S_s=X-B(D+sI)^{-1}B^*,
\tag{14.16}\label{eq:14.16}
$$

$$
v_s=v_O-B(D+sI)^{-1}v_F,
\quad d_s=d_O-B(D+sI)^{-1}d_F.
\tag{14.17}\label{eq:14.17}
$$

The product rule for commutators gives

$$
[Z_O,S_s]=v_sd_s^*-d_sv_s^*.
\tag{14.18}\label{eq:14.18}
$$

The same inverse appears in every term. This algebra holds even for an indefinite invertible denominator, but such a denominator cannot then be used as a positive square in a lower-bound argument. The sign and inertia remain separate information.

The harmonic representation is one of the strongest exact finite reductions recovered outside the short referee manuscripts. It belongs in the active toolkit: it makes the complete matrix, pole-neutral compression, and elimination update explicit with few generators. It does not replace the signed cofinal estimate.

*Sources:* [V10B](#source-v10b) §§5, 8–10; [HARM](#source-harm), sine-displacement and Loewner replay; [RIII](#source-riii) §8. Formula (14.3) retains the source notation of the triple-routing identity, with \(u\) as the input coordinate.

# 15. A fixed pair of packets and the complete zero response {#ch-packets}

## Building one test with no off-axis blind spot

Let \(a_j=2^{-j-1}\), and let \(g\) be the density of the sum of independent uniform variables on \([-a_j,a_j]\). The total half-width is \(1/2\). Its bilateral Laplace transform is

$$
G(z)=\prod_{j\ge1}\frac{\sinh(a_jz)}{a_jz}.
\tag{15.1}\label{eq:15.1}
$$

The product converges locally uniformly. Every individual zero lies on the imaginary axis, and local convergence of the logarithms away from those zeros shows

$$
G(z)\ne0\qquad(\operatorname{Re}z\ne0).
\tag{15.2}\label{eq:15.2}
$$

The infinitely convolved density is real, even, nonnegative, smooth, and supported on \([-1/2,1/2]\). Put \(k=g*g\). Then \(k\) is supported on \([-1,1]\), has integral one, and is positive in its interior. Rapid vertical decay of \(G\) ensures absolute convergence of the zero sums used below.

The point of this fixed choice is not cosmetic smoothing. An arbitrary compact test can have a transform zero at a hypothetical off-line zero. Equation (15.2) excludes that failure for every off-line zero simultaneously.

## Two packets in the actual physical norm

Let \(q_0=Q_W(g)\), \(n_0=\|g\|^2\), and for \(t>1\) set

$$
f_{t,\pm}(x)=g(x+t/2)\pm g(x-t/2).
\tag{15.3}\label{eq:15.3}
$$

Their supports are disjoint, so \(\|f_{t,\pm}\|^2=2n_0\). If \(W\) is the complete Weil distribution and

$$
c(t)=W(k(\,\cdot-t)),
\tag{15.4}\label{eq:15.4}
$$

translation invariance and polarization give

$$
Q_W(f_{t,\pm})=2q_0\pm2c(t).
\tag{15.5}\label{eq:15.5}
$$

In the two-packet basis the norm Gram is exactly \(n_0I\), and the Weil Gram is

$$
\begin{pmatrix}q_0&c(t)\\c(t)&q_0\end{pmatrix}.
\tag{15.6}\label{eq:15.6}
$$

There is no synthetic metric or unspecified whitening constant. The lower Rayleigh value in this two-dimensional space is \((q_0-|c(t)|)/n_0\).

## The spectral exponential series

With \(z_\rho=\rho-1/2\), the complete response is

$$
c(t)=\sum_\rho m_\rho G(z_\rho)^2e^{z_\rho t}.
\tag{15.7}\label{eq:15.7}
$$

The coefficient is a complex square. This matters: a proof replacing it by an absolute square would have inserted the desired positivity by hand. The zero symmetry makes \(c(t)\) real and even without making each term positive.

Let

$$
R_\zeta=\sup_\rho|\operatorname{Re}\rho-1/2|.
\tag{15.8}\label{eq:15.8}
$$

The second scout proves the growth identity

$$
\lim_{T\to\infty}
\frac{\log(1+\max_{0\le t\le T}|c(t)|)}{T}=R_\zeta.
\tag{15.9}\label{eq:15.9}
$$

The supremum need not be attained. The proof selects a zero arbitrarily close to it and uses an auxiliary Gaussian transform to prevent cancellation from hiding the exponential rate.

## Gaussian isolation of a dominant contribution

Choose \(0<\theta<1\), small \(\kappa>0\), and a modulation \(\tau\). Consider

$$
I_T=\frac1{\sqrt{4\pi\kappa T}}
\int_{\mathbb R}c(t)
\exp\!\left[-\frac{(t-\theta T)^2}{4\kappa T}\right]
 e^{-i\tau t}\,dt.
\tag{15.10}\label{eq:15.10}
$$

Termwise integration yields

$$
I_T=\sum_\rho m_\rho G(z_\rho)^2
\exp\{T[\theta(z_\rho-i\tau)+\kappa(z_\rho-i\tau)^2]\}.
\tag{15.11}\label{eq:15.11}
$$

The real exponent contains the negative term \(-\kappa(\operatorname{Im}z_\rho-\tau)^2\), suppressing high ordinates. Generic \(\tau\) avoids ties. A zero near the real-part supremum can be made to contribute a unique dominating exponent. Its coefficient is nonzero by (15.2), so it cannot cancel against a strictly lower exponential remainder.

Meanwhile \(|\operatorname{Re}z_\rho|\le1/2\) bounds growth outside the aperture, and the Gaussian tails can be made negligible. Exponential growth of \(I_T\) forces the maximum of \(|c|\) inside \([-T,T]\) to have the same limiting rate. The Gaussian is only a proof device; the tests inserted into the Weil form remain compactly supported packets.

## One sign and integrated mass also suffice

The third scout strengthens (15.9): for either sign separately,

$$
\lim_{T\to\infty}
\frac{\log(1+\int_0^T[\pm c(t)]_+\,dt)}{T}=R_\zeta.
\tag{15.12}\label{eq:15.12}
$$

Its extra ingredient is the absence of a zero-frequency term. Nontrivial zeros have nonzero ordinate, and local finiteness gives a gap around zero. Comparing a modulated Gaussian integral with the unmodulated one makes the latter exponentially smaller. If \(B_+,B_-\) are the positive and negative Gaussian-weighted masses, then

$$
B_\pm\ge\tfrac12(|I_T|-|J_T|).
\tag{15.13}\label{eq:15.13}
$$

Both signs therefore carry the exponential rate. Removing the Gaussian weight costs only subexponential factors.

This statement would be false for a raw growing pole, such as \(\cosh(\alpha t)\), which has no negative part. Exact completion is essential.

## Sparse apertures and the quantitative implication

For packets fitting inside \((-b_j,b_j)\), a lower bound with allowance \(\beta_j\) bounds \(|c(t)|\) over an interval of separations with length asymptotic to \(2b_j\). Therefore

$$
2R_\zeta\le
\liminf_j\frac{\log(1+\beta_j)}{b_j}.
\tag{15.14}\label{eq:15.14}
$$

There is no restriction on the gaps between the \(b_j\). Sampling one endpoint would be insufficient: \(\cosh(\alpha t)\cos(\gamma t)\) vanishes at infinitely many endpoints while growing exponentially between them. The interval maximum or signed mass removes that loophole.

*Sources:* [SC2](#source-sc2) fixed-bump and exponential-series theorems; [SC3](#source-sc3) signed-mass refinement; [SC4](#source-sc4) normalization. These packet tests are distinct from the odd pole-filtered Gaussian family in Chapter 12, although both support cofinal endpoint logic.

# 16. Prime excess, square bias, and unconditional smoothing bounds {#ch-prime-excess}

## The exact centered prime window

Let \(A=G(1/2)^2\). For \(t>1\), the explicit formula gives

$$
c(t)=Ae^{t/2}
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}k(t-\log n)
-\mathcal T_g(t),
\tag{16.1}\label{eq:16.1}
$$

where

$$
\mathcal T_g(t)=\sum_{m\ge1}
G(2m+1/2)^2e^{-(2m+1/2)t}>0.
\tag{16.2}\label{eq:16.2}
$$

The decaying pole cancels the leading Archimedean exponential exactly. The remaining tail satisfies

$$
0<\mathcal T_g(t)
\le\frac{e^{-5(t-1)/2}}{1-e^{-2(t-1)}}.
\tag{16.3}\label{eq:16.3}
$$

Only \(e^{t-1}\le n\le e^{t+1}\) contributes to the arithmetic sum. Thus the observable is one fixed-shape multiplicative window. Its growing main term and prime sum must be centered before taking an absolute value.

## Removing higher prime powers without losing the bias

Write

$$
P_1(t)=\sum_p\frac{\log p}{\sqrt p}k(t-\log p),
\quad
P_2(t)=\sum_p\frac{\log p}{p}k(t-2\log p).
\tag{16.4}\label{eq:16.4}
$$

The ordinary prime number theorem, not an RH-strength error term, gives

$$
P_2(t)\longrightarrow\frac12.
\tag{16.5}\label{eq:16.5}
$$

To see this, write \(P_2=\int x^{-1}k(t-2\log x)\,d\vartheta(x)\). Replacing \(d\vartheta\) by \(dx\) gives exactly \(\frac12\int k=1/2\). Integration by parts against \(\vartheta(x)-x=o(x)\) gives an \(o(1)\) error uniformly on this fixed-ratio window.

For powers \(p^m\) with \(m\ge3\), elementary counting gives \(O(t^2e^{-t/6})\). Together with (16.3),

$$
P_{\ge2}(t)+\mathcal T_g(t)=\frac12+o(1).
\tag{16.6}\label{eq:16.6}
$$

Hence, for \(D(t)=P_1(t)-Ae^{t/2}\),

$$
D(t)=-c(t)-\frac12+o(1).
\tag{16.7}\label{eq:16.7}
$$

The preceding scout's coarser explicit bound \(P_{\ge2}(t)+\mathcal T_g(t)\le22(t+1)\), for \(t\ge2\), remains useful when an asymptotic threshold is not needed. The later half-unit limit is the sharper statement for the same fixed kernel.

## A one-sided averaged endpoint

Define

$$
\mathcal E(T)=\int_2^T[P_1(t)-Ae^{t/2}]_+\,dt.
\tag{16.8}\label{eq:16.8}
$$

The signed-mass detector and the controlled higher-power contribution give

$$
\lim_{T\to\infty}\frac{\log(1+\mathcal E(T))}{T}=R_\zeta.
\tag{16.9}\label{eq:16.9}
$$

A subexponential bound along any cofinal sequence therefore implies RH. Under RH the absolutely convergent zero sum is bounded, and the nonnegative higher-power correction gives \(\mathcal E(T)=O(T)\). This is an equivalent arithmetic criterion, not an already-established estimate.

The possible advantage is one-sidedness. An upper majorant need only control prime excess; it need not estimate prime deficits or the absolute prime-number-theorem error. The next chapters examine a natural majorant and the exact cancellation needed to make its excess small enough.

## What unconditional zero-free information gives for this observable

The third scout combines the established Korobov–Vinogradov zero-free region with the special decay of the product (15.1). Uniformly for \(|\alpha|\le1/2\), the source derives

$$
|G(\alpha+iy)|^2
\le C\exp\left[-\frac{(\log|y|)^2}{\log2}+3\log|y|\right]
\tag{16.10}\label{eq:16.10}
$$

at large \(|y|\). In a logarithmic height shell \(e^n\le|\operatorname{Im}\rho|<e^{n+1}\), the zero-free region and this damping yield a bound of the shape

$$
C\exp\left[
\frac t2-
\frac{c_1t}{(n+1)^{2/3}(\log(n+1))^{1/3}}
-an^2\right].
\tag{16.11}\label{eq:16.11}
$$

Balancing the two savings at \(n\asymp t^{3/8}(\log t)^{-1/8}\) gives

$$
|c(t)|\le C\exp\left[
\frac t2-d\frac{t^{3/4}}{(\log t)^{1/4}}\right]
\tag{16.12}\label{eq:16.12}
$$

for suitable constants and large \(t\). This is a source-derived estimate for the heavily smoothed observable, not a claimed improvement of the unsmoothed prime number theorem.

The exponential rate of this upper envelope is still \(1/2\). Improving constants in the saving term does not turn it into rate zero. The mathematical gap is between an estimate \(e^{t/2-o(t)}\) and the required \(e^{o(t)}\), not between a rough and a polished numerical constant.

## Why smoothing must stay fixed

A smoothing parameter depending on the final aperture can suppress a hypothetical off-axis mode and thereby alter the detector. For a synthetic mode \(e^{\alpha t}\cos(\gamma t)\), heat smoothing on time \(\kappa T\) modifies its exponent to \(\alpha+\kappa(\alpha^2-\gamma^2)\). It can become negative even when \(\alpha>0\).

Such a calculation may be useful for another theorem, but it does not prove the fixed-kernel estimate (16.9). The source, its normalization, and its dependence on aperture must remain part of the statement.

*Sources:* [SC2](#source-sc2) exact tail cancellation; [SC3](#source-sc3) §§unconditional estimate and prime-only excess; [SC4](#source-sc4) square bias. External zero-free inputs retain the scope stated in those reports.

# 17. Divisor covariance and the subcritical sieve obstruction {#ch-gcd}

## An arithmetic covariance with a tractable inverse

For \(1\le m,n\le L\), define

$$
K_L(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}.
\tag{17.1}\label{eq:17.1}
$$

Let

$$
d_L=\max_{n\le L}\tau(n),
\quad r_L=\max_{n\le L}\frac n{\varphi(n)},
\quad h_L=\sum_{n\le L}\frac1n.
\tag{17.2}\label{eq:17.2}
$$

The scout proves

$$
\|K_L\|\le d_Lh_L,
\qquad
\|K_L^{-1}\|\le d_Lr_Lh_L.
\tag{17.3}\label{eq:17.3}
$$

Use the divisor-incidence factor

$$
Z_{nd}=\mathbf1_{d\mid n}\sqrt{\frac{\varphi(d)}n}.
\tag{17.4}\label{eq:17.4}
$$

The identity \(\sum_{d\mid g}\varphi(d)=g\) gives \(K_L=ZZ^*\). Möbius inversion gives

$$
(Z^{-1})_{nd}=\mathbf1_{d\mid n}\mu(n/d)\sqrt{\frac d{\varphi(n)}}.
\tag{17.5}\label{eq:17.5}
$$

A weighted Schur test with weights \(n^{-1/2}\) gives (17.3). Since \(r_L\le d_L=L^{o(1)}\) and \(h_L\le1+\log L\), both the upper and inverse growth are subpower in the largest integer label.

The height is the largest label, not the number of selected columns. To obtain \(e^{o(b)}\), one needs a relation such as \(\log L=O(b)\). A construction using products whose logarithms grow much faster can lose the desired scale despite a formally subpower covariance estimate.

## Keeping synthesis explicit

Let actual source families be \(F=SU\), \(E=SV\), and let \(P\) project away the actual old ports. If

$$
(PAP)|_{\ker F^*}\succeq\eta(PS)K(PS)^*,
\tag{17.6}\label{eq:17.6}
$$

then the quotient identity gives

$$
\Gamma_A(E\mid F)\preceq\eta^{-1}\Gamma_K(V\mid U).
\tag{17.7}\label{eq:17.7}
$$

This follows by applying the contraction \(A_\perp^{-1/2}(PS)K^{1/2}\) to \(Vx-Uy\) and minimizing over \(y\). For \(K=K_L\),

$$
x^*\Gamma_Ax
\le\eta^{-1}d_Lr_Lh_L\min_y\|Vx-Uy\|^2.
\tag{17.8}\label{eq:17.8}
$$

The bound pays an arithmetic coefficient residual modulo old ports. It does not invert the physical synthesis. Its application still requires the actual projected funding inequality (17.6).

The need for that distinction is visible in \(e^{it\log n}\) and \(e^{it\log(n+1)}\) on a fixed interval. Their physical Gram has a small eigenvalue of order \(n^{-2}\), whereas the two-label GCD Gram has smallest eigenvalue tending to one. The labels alone do not identify the metrics.

## The standard quadratic majorant

For \(w_t(n)=(\log n)n^{-1/2}k(t-\log n)\), choose \(D<e^{t-1}\) and coefficients \(\lambda_1=1\). Every prime in the window exceeds \(D\), so

$$
P_1(t)\le\sum_nw_t(n)
\left(\sum_{\substack{d\mid n\\d\le D}}\lambda_d\right)^2.
\tag{17.9}\label{eq:17.9}
$$

The exact Gram is

$$
A_t(d,e)=\sum_{\ell\ge1}w_t([d,e]\ell)\succeq0.
\tag{17.10}\label{eq:17.10}
$$

Its main covariance is

$$
M_D(d,e)=\frac1{[d,e]}=\frac{\gcd(d,e)}{de}.
\tag{17.11}\label{eq:17.11}
$$

Möbius inversion yields

$$
(M_D^{-1})_{11}=H_D,
\qquad H_D=\sum_{n\le D}\frac{\mu(n)^2}{\varphi(n)},
\tag{17.12}\label{eq:17.12}
$$

and the constrained minimum of \(\lambda^TM_D\lambda\) is \(1/H_D\). The source proves \(H_D=\log D+C_0+o(1)\).

## Why more coefficient optimization cannot fix this scale

Write \(A_t=W(t)M_D+R_t\), where

$$
W(t)=e^{t/2}\{At+2G(1/2)G'(1/2)\}.
\tag{17.13}\label{eq:17.13}
$$

For fixed \(0<\theta<1/2\) and \(D=\lfloor e^{\theta t}\rfloor\), the variation bound on the exact arithmetic remainder, combined with (17.3), gives

$$
\|(WM_D)^{-1/2}R_t(WM_D)^{-1/2}\|
\le e^{-(1-2\theta)t+o(t)}\to0.
\tag{17.14}\label{eq:17.14}
$$

Therefore the optimized actual quadratic satisfies

$$
\min_{\lambda_1=1}\lambda^TA_t\lambda
=\left(\frac1\theta+o(1)\right)Ae^{t/2}.
\tag{17.15}\label{eq:17.15}
$$

Its leading coefficient is greater than two. The desired centered main coefficient is one. This is an obstruction for the entire specified subcritical class, not just for a poor numerical choice of weights.

## The exact remainder short

The optimized expression also admits a complete-block identity. Let \(\lambda_0=M_D^{-1}e_1/H_D\), let \(U\) insert coordinates other than the first, and set \(B_t=U^TA_tU\), \(r_t=U^TR_t\lambda_0\). Then

$$
\min_{\lambda_1=1}\lambda^TA_t\lambda
=\frac{W(t)}{H_D}+\lambda_0^TR_t\lambda_0
-r_t^TB_t^\dagger r_t.
\tag{17.16}\label{eq:17.16}
$$

This is the complete arithmetic denominator, not just \(WM_D\). It mirrors the physical source-budget problem: a remainder short can improve a main covariance, but its inverse must be the actual one. The next construction changes the cutoff and response algebra rather than trying to beat the fixed leading constant in (17.15).

*Sources:* [SC1](#source-sc1) GCD factorization and projected funding; [SC3](#source-sc3) positive-divisor majorant and exact optimum. The argument is a scoped sieve obstruction, not a statement that all sieve methods are incapable of addressing the prime-excess problem.

# 18. Exact composite cancellation and the quarter-surplus theorem {#ch-quarter}

## A finite logarithm in the divisibility algebra

Let \(*\) denote Dirichlet convolution, \(\varepsilon\) its identity, and \(u=\mathbf1-\varepsilon\). Define

$$
\nu=\sum_{j\ge0}\frac{(-1)^j}{j+1}u^{*j}.
\tag{18.1}\label{eq:18.1}
$$

At each integer the sum is finite. Multiplication by \(u\) gives \(u*\nu=\log_*(\mathbf1)\). The formal Euler product therefore yields the exact proper-divisor response

$$
\sum_{\substack{d\mid n\\d<n}}\nu(d)
=\begin{cases}
1/m,&n=p^m,\\
0,&n\text{ has at least two distinct prime factors}.
\end{cases}
\tag{18.2}\label{eq:18.2}
$$

For example, \(\nu(1)=1\), \(\nu(p)=-1/2\), \(\nu(p^2)=-1/6\), and \(\nu(pq)=1/6\). A distinct semiprime has response \(1-1/2-1/2=0\), while a prime square has response \(1/2\). The cancellation occurs before squaring.

For a squarefree integer with \(r\) distinct prime factors, \(\nu(n)=B_r\), with the convention \(B_1=-1/2\). The large even Bernoulli coefficients show why a raw coefficient-norm estimate is inappropriate. The useful small quantity is the synthesized divisor response.

## A cutoff that includes every proper divisor

Restrict integer rows to \((n,210)=1\), and use

$$
L_t=\left\lfloor\frac{e^{t+1}}{11}\right\rfloor.
\tag{18.3}\label{eq:18.3}
$$

Because \(e^2<11\), \(L_t<e^{t-1}\), so every prime in the window exceeds the divisor cutoff. Every surviving composite has least prime factor at least 11, so all its proper divisors are at most \(n/11\le L_t\). This realizes the complete sum (18.2) without missing boundary divisors.

For \(t\ge3\), excluding primes 2, 3, 5, and 7 removes no prime from the window. The exact Gram on divisors coprime to 210 is

$$
\mathcal A_t(d,e)=
\sum_{\substack{(n,210)=1\\{}[d,e]\mid n}}w_t(n).
\tag{18.4}\label{eq:18.4}
$$

The explicit quadratic \(\mathcal Z(t)=\nu_t^T\mathcal A_t\nu_t\) is

$$
\mathcal Z(t)=P_1(t)
+\sum_{\substack{p>7\\m\ge2}}
\frac{\log p}{m\,p^{m/2}}k(t-m\log p).
\tag{18.5}\label{eq:18.5}
$$

The square term is \(P_2(t)/2\to1/4\); higher powers vanish. Thus

$$
\mathcal Z(t)-P_1(t)\longrightarrow\frac14.
\tag{18.6}\label{eq:18.6}
$$

Unlike (17.15), the excess is bounded rather than exponentially large.

## Why the quarter cannot be optimized away

Define \(\mathcal S(t)=\min_{\lambda_1=1}\lambda^T\mathcal A_t\lambda\). Prime rows always contribute \(P_1(t)\). Choose a central prime interval near \(e^{t/2}\), with all pairwise products inside the interior of the support window. Put \(u_p=\lambda_p+1/2\).

Distinct semiprime responses are \(u_p+u_q\); square responses are \(u_p+1/2\). The associated energy is

$$
\sum_{p<q}w_t(pq)(u_p+u_q)^2
+\sum_pw_t(p^2)(u_p+1/2)^2.
\tag{18.7}\label{eq:18.7}
$$

For a complete graph on \(v\) vertices,

$$
\sum_{i<j}(u_i+u_j)^2
=(v-2)\sum_i u_i^2+\left(\sum_i u_i\right)^2.
\tag{18.8}\label{eq:18.8}
$$

The weights are bounded below by a constant times \(te^{-t/2}\), and the vertex count is comparable to \(e^{t/2}/t\). Their product gives a fixed positive graph floor.

Let \(Q_{\mathrm{sg}}\) be this signless graph matrix, \(d_p=w_t(p^2)\), \(D_0=\operatorname{diag}(d_p)\), and \(d=D_0\mathbf1\). Minimizing (18.7) gives

$$
\frac14\sum_pd_p
-\frac14d^T(Q_{\mathrm{sg}}+D_0)^{-1}d.
\tag{18.9}\label{eq:18.9}
$$

The denominator includes the square contribution. Its inverse correction tends to zero because \(\max_pd_p=O(te^{-t/2})\), \(\sum_pd_p=O(1)\), and the graph has a fixed lower bound. Expanding the central interval to the full support makes \(\sum_pd_p\to1\). Therefore

$$
\mathcal S(t)-P_1(t)\longrightarrow\frac14,
\qquad
P_1(t)\le\mathcal S(t)\le\mathcal Z(t).
\tag{18.10}\label{eq:18.10}
$$

This is a source-specific funding theorem for a fully specified arithmetic optimization. It is not an identification with the complete physical Boundary–Weyl denominator.

## The centered comparison that remains

The Gram has a prime-free outer representation,

$$
\mathcal A_t(d,e)
=\sum_{a\mid210}\mu(a)\sum_{m\ge1}w_t(a[d,e]m).
\tag{18.11}\label{eq:18.11}
$$

There are sixteen outer terms. This makes a concrete integer-multiple expression for the desired comparison:

$$
\log\left(1+\int_3^{T_j}
[\nu_t^T\mathcal A_t\nu_t-Ae^{t/2}]_+\,dt\right)=o(T_j).
\tag{18.12}\label{eq:18.12}
$$

It would imply the prime-excess criterion. The bounded overcount in (18.6) means the majorant itself no longer consumes an exponential budget. The leading centered comparison remains unproved.

## The conditional negative margin

The fourth scout interval-encloses the seed trace and records \(q_0<1/16\). Under RH the spectral coefficients \(G(i\gamma)^2\) are nonnegative, giving \(|c(t)|\le q_0\). Equations (16.7) and (18.6) then imply

$$
\mathcal Z(t)-Ae^{t/2}=-c(t)-\frac14+o(1)
\le-\frac3{16}+o(1).
\tag{18.13}\label{eq:18.13}
$$

This is a robust conditional margin. It cannot be reversed into an unconditional estimate by assuming \(|c(t)|\le c(0)\); that is the spectral positivity used only under RH.

The value of the construction is exact removal of an artificial obstruction. It reorganizes prime detection into a positive quadratic with a sharp bounded surplus. It does not by itself estimate the remaining weighted prime total.

*Sources:* [SC4](#source-sc4) §§2–8 and exact checkers; [SC3](#source-sc3) for the predecessor obstruction. The logarithmic construction, the signless-graph lower bound, and the seed interval calculation are kept as separate arguments.


\part{The actual central coefficients and positive completion}

# 19. The theta coefficients and the single-Hankel theorem {#ch-hankel}

## The complete theta kernel

The all-rank studies use

$$
\Phi(u)=\sum_{m\ge1}(8v_m^2-12v_m)e^{u/2-v_m},
\qquad v_m=\pi m^2e^{2u},\quad u\ge0.
\tag{19.1}\label{eq:19.1}
$$

Every summand is positive on the half-line. The exact Jacobi transformation makes the even extension smooth. In the retained normalization,

$$
\xi(\tfrac12+z)=\int_0^\infty\Phi(u)\cosh(zu)\,du,
\qquad
\gamma_j=\frac{j!}{(2j)!}\int_0^\infty u^{2j}\Phi(u)\,du.
\tag{19.2}\label{eq:19.2}
$$

Thus \(\gamma_j>0\). The normalized descent is (2.4). It has order at most one half and is positive on the nonnegative real axis.

Define the logarithmic quantities from the actual Taylor series,

$$
p_r=(-1)^{r-1}r[w^r]\log F(w),
\qquad\mu_j=p_{j+1}.
\tag{19.3}\label{eq:19.3}
$$

They are not introduced by assuming a positive measure or a real-zero list. Locally,

$$
\frac{F'(w)}{F(w)}=\sum_{j\ge0}(-1)^j\mu_jw^j.
\tag{19.4}\label{eq:19.4}
$$

If \(F(w)=\sum c_jw^j\), a direct recurrence for \(\ell_r=r[w^r]\log F\) is

$$
\ell_r=rc_r-\sum_{j=1}^{r-1}\ell_jc_{r-j},
\qquad p_r=(-1)^{r-1}\ell_r.
\tag{19.5}\label{eq:19.5}
$$

The recurrence follows by comparing coefficients in \(F'=F(\log F)'\). Its cancellations motivate the direct coefficient formulation in Chapter 23.

## One all-rank family suffices

Form

$$
H_n=(\mu_{i+j})_{i,j=0}^{n-1}.
\tag{19.6}\label{eq:19.6}
$$

**Single-Hankel theorem.** For the actual normalized entire \(F\), if \(H_n\succeq0\) at an unbounded sequence of sizes, then all zeros of \(F\) are negative real.

**Proof.** Every smaller leading matrix is a principal submatrix of some positive larger matrix. Thus the functional \(L(x^j)=\mu_j\) is nonnegative on every polynomial square. Hamburger's theorem gives a positive measure \(\nu\) on \(\mathbb R\) with moments \(\mu_j\). Since \(\mu_0=1\), it is a probability measure.

The logarithmic derivative is analytic on a disk around zero. Cauchy's estimate supplies constants \(C,R>0\) with \(|\mu_j|\le CR^j\). If \(\nu\) had positive mass outside \([-R-\varepsilon,R+\varepsilon]\), its even moments would grow faster than this bound. Therefore the support is compact.

The function

$$
G(w)=\int\frac{d\nu(x)}{1+xw}
\tag{19.7}\label{eq:19.7}
$$

is holomorphic in each nonreal half-plane and agrees with (19.4) near zero. Meromorphic uniqueness identifies it with \(F'/F\) throughout each half-plane. A zero of \(F\) would give a nonremovable pole of its logarithmic derivative, impossible there. The positive Taylor coefficients exclude nonnegative real zeros. This proves the claim.

The argument uses exact analytic continuation of the actual \(F\). It does not say that a finite Hankel matrix forces support localizers to be positive, nor does it remove localizers from an unrelated finite-prime moment problem.

## Integer multiplicities become automatic only at the limit

After the zero locations have been established, order below one gives the genus-zero factorization

$$
F(w)=\prod_i(1+a_iw)^{m_i},
\quad a_i>0,\quad m_i\in\mathbb N.
\tag{19.8}\label{eq:19.8}
$$

There is no nonconstant exponential factor. Differentiation at zero gives \(\sum_i m_i a_i=1\), so

$$
p_r=\sum_i m_i a_i^r,
\qquad
\nu=\sum_i m_i a_i\delta_{a_i},
\quad0<a_i\le1.
\tag{19.9}\label{eq:19.9}
$$

The support restriction and integer residues therefore follow after the all-rank analytic argument. Imposing them on every finite approximation is stronger than the limiting proof requires.

Conversely, under RH the representation (19.9) makes every \(H_n\) positive definite, since infinitely many distinct support points remain. Thus the all-rank condition is equivalent in strength to the desired zero statement. Its utility is structural precision, not an automatic reduction of mathematical difficulty.

## The next actual pivot

For \(H_n\succ0\), put

$$
v_n=(p_{n+1},\ldots,p_{2n})^T,
\qquad
\delta_n=p_{2n+1}-v_n^TH_n^{-1}v_n.
\tag{19.10}\label{eq:19.10}
$$

Then

$$
H_{n+1}\succ0\ \Longleftrightarrow\ \delta_n>0,
\qquad\det H_{n+1}=\det H_n\,\delta_n.
\tag{19.11}\label{eq:19.11}
$$

The inverse is the complete actual preceding Hankel matrix. A fitted zero model or a reference covariance cannot replace it. No uniform lower bound on \(\delta_n\) is required; every positive value, however small, is acceptable. The missing theorem is its sign for every actual rank.

## The finite record

The most recent retained calculation encloses \(\gamma_0,\ldots,\gamma_{39}\), certifies \(H_{20}\succ0\), three size-19 support matrices, and 38 canonical coordinates in \((0,1)\). The final positive \(LDL^T\) pivot of \(H_{20}\) is approximately \(7.5316718348997\times10^{-75}\). It is a pivot, not a lower bound for the smallest eigenvalue.

These results are substantial finite coverage of the actual coefficient object. The negative-heat control in Chapter 22 passes the same ranks. That control is retained beside the certificate because it prevents a finite tower from being mistaken for an induction.

*Sources:* [MC](#source-mc) §§1–2; [ARK](#source-ark) §§1–2 and actual coefficient routines. The Hamburger theorem is an external mathematical input cited in those sources; the compact-support and logarithmic-derivative specialization are written out above.

# 20. Positive prefixes and uniform analytic transfer {#ch-prefix}

## Entire approximants with prescribed zero geometry

Consider

$$
H(w)=e^{qw}\prod_{i=1}^{m}(1+a_iw),
\quad q\ge0,\quad a_i\ge0,
\quad q+\sum_i a_i=1.
\tag{20.1}\label{eq:20.1}
$$

Every zero is negative real. The normalization fixes the constant and linear Taylor coefficients. Coefficientwise,

$$
0\le[w^j]H\le\frac1{j!},
\qquad |H(w)|\le e^{|w|}.
\tag{20.2}\label{eq:20.2}
$$

The inequality follows by replacing each factor \(1+a_iw\) by \(e^{a_iw}\) in the nonnegative coefficient order.

Suppose \(H_\ell\) agrees with the actual \(F\) through order \(K_\ell\), where \(K_\ell\to\infty\). For \(0<r<s\),

$$
\sup_{|w|\le r}|F(w)-H_\ell(w)|
\le\left(\frac rs\right)^{K_\ell+1}F(s)
+e^r\frac{r^{K_\ell+1}}{(K_\ell+1)!}.
\tag{20.3}\label{eq:20.3}
$$

The common prefix cancels. Positivity bounds the remaining \(F\)-tail by its value at \(s\); (20.2) bounds the model tail. Both terms tend to zero, giving locally uniform convergence. Hurwitz then transfers nonvanishing off the negative axis.

This theorem removes a separate critical-point transfer test for every degree. The remaining task is constructing admissible prefixes of unbounded length. Exact matching is sufficient, not necessary: an approximate-prefix version adds \(\sum_{j\le K}|c_j-h_j|r^j\) to the right side.

## Finite positive models from actual moments

Expanding the logarithm of (20.1) gives the matching equations

$$
q+\sum_i a_i=1,
\qquad\sum_i a_i^r=p_r\quad(2\le r\le K).
\tag{20.4}\label{eq:20.4}
$$

The prefix-energy study records interval fixed-point certificates for three exact actual-coefficient solutions. Prefix lengths 3, 6, and 7 use respectively 3, 16, and 24 positive linear factors, counted with multiplicity. Their exponential parameters are approximately

$$
0.5628462990894294,
\quad0.2978696919558082,
\quad0.2514706657133620.
\tag{20.5}\label{eq:20.5}
$$

The certificates include inverse-Jacobian preconditioners and enclosing boxes, so they establish solutions for the enclosed actual coefficients, not merely rounded numerical targets. The unsuccessful searches for longer integer-factor models remain recorded as searches, not infeasibility theorems.

At prefix seven, the uniform bound gives errors below \(2.897\times10^{-7}\) on \(|w|\le1/2\) and \(1.007\times10^{-4}\) on \(|w|\le1\). These are small-disk approximation bounds. Fixed prefix length does not control arbitrary disks.

## Polynomial rather than exponential models

The exponential factor can be replaced by \((1+qw/N)^N\), preserving negative real zeros. For \(N>qr\), put

$$
\varepsilon_N=\frac{q^2r^2}{2N(1-qr/N)}.
\tag{20.6}\label{eq:20.6}
$$

The logarithmic series yields

$$
\sup_{|w|\le r}\left|
H(w)-(1+qw/N)^N\prod_i(1+a_iw)\right|
\le e^r(e^{\varepsilon_N}-1).
\tag{20.7}\label{eq:20.7}
$$

Thus the transfer need not rely on an exponential factor at all. It still depends on the existence of the prescribed prefixes.

## Fractional exponents enlarge the feasible class

For a positive probability measure \(\nu\) on \([0,1]\), define

$$
B_\nu(w)=\exp\left\{
\int_{[0,1]}\frac{\log(1+xw)}x\,d\nu(x)\right\},
\tag{20.8}\label{eq:20.8}
$$

with the integrand at zero interpreted as \(w\). This is analytic and nonvanishing on \(D=\mathbb C\setminus(-\infty,-1]\). Since \(\log|1+xw|/x\le|w|\),

$$
|B_\nu(w)|\le e^{|w|}.
\tag{20.9}\label{eq:20.9}
$$

Its logarithm has moments

$$
\log B_\nu(w)
=\sum_{r\ge1}\frac{(-1)^{r-1}}r
\left(\int x^{r-1}\,d\nu(x)\right)w^r.
\tag{20.10}\label{eq:20.10}
$$

An atomic measure produces fractional powers \((1+a_iw)^{\eta_i/a_i}\). These functions are generally not entire, but their common slit domain is sufficient for a normal-family argument. If they match increasingly long actual prefixes, local convergence near zero identifies every subsequential limit with \(F\). The identity theorem extends the equality throughout \(D\), and Hurwitz excludes nonreal zeros.

This enlargement removes an artificial finite integrality requirement without weakening the analytic endpoint. It does not establish positive moment representability at unbounded size.

## A positive resolvent from finite moments

For matched moments \(\mu_0,\ldots,\mu_{2n-1}\), form

$$
H_0=(\mu_{i+j})_{i,j=0}^{n-1},
\qquad H_1=(\mu_{i+j+1})_{i,j=0}^{n-1}.
\tag{20.11}\label{eq:20.11}
$$

If \(H_0\succ0\), \(H_1\succ0\), and \(H_0-H_1\succ0\), then with \(h=H_0e_0\),

$$
R_n(w)=h^T(H_0+wH_1)^{-1}h
=\sum_{i=1}^n\frac{\eta_i}{1+a_iw},
\tag{20.12}\label{eq:20.12}
$$

where \(0<a_i<1\), \(\eta_i>0\), and \(\sum_i\eta_i=1\). Gaussian quadrature moment identities give agreement with \(F'/F\) through the corresponding \(2n\)-term prefix. Integrating gives (20.8).

For \(\operatorname{Im}w>0\), the exact energy identity is

$$
-\frac{\operatorname{Im}R_n(w)}{\operatorname{Im}w}
=h^*(H_0+\overline wH_1)^{-1}
H_1(H_0+wH_1)^{-1}h\ge0.
\tag{20.13}\label{eq:20.13}
$$

The numerator, denominator, and metric are the same actual coefficient matrices. This is an explicit passive finite model. It is not a positive realization of the entire actual function until unbounded moment coverage has been proved.

*Sources:* [PC](#source-pc) uniform-prefix theorem, model certificates, and resolvent section; [MC](#source-mc) fractional transport and finite quadrature. The model class changes are explicit throughout.

# 21. Moment correction, canonical coordinates, and collision-free paths {#ch-continuation}

## A flow preserving the matched prefix

Suppose (20.1) matches \(p_2,\ldots,p_K\). Choose \(K-1\) distinct positive adjustable parameters \(x_i\), with positive integer multiplicities \(m_i\), and introduce \(N\) new factors \((1+bw)^N\). Keep the other parameters fixed. Let

$$
L_i(b)=\prod_{j\ne i}\frac{b-x_j(b)}{x_i(b)-x_j(b)}.
\tag{21.1}\label{eq:21.1}
$$

Define

$$
\frac{dx_i}{db}=-\frac{Nb}{m_ix_i(b)}L_i(b).
\tag{21.2}\label{eq:21.2}
$$

Lagrange interpolation gives \(\sum_iL_i(b)x_i^{r-2}=b^{r-2}\) for \(2\le r\le K\). Differentiating the power sums therefore gives zero for every already-matched moment.

Adjust \(q(b)\) to keep the linear coefficient one. The exact derivative is

$$
q'(b)=-N\prod_i\left(1-\frac b{x_i(b)}\right).
\tag{21.3}\label{eq:21.3}
$$

The complete logarithmic response, after all compensations, is

$$
\frac{\partial}{\partial b}\log H_b(w)
=-\frac{Nb\,w^{K+1}\prod_i(x_i(b)-b)}
{(1+bw)\prod_i(1+x_i(b)w)}.
\tag{21.4}\label{eq:21.4}
$$

While \(0<b<\min_i x_i(b)\) and \(q(b)\ge0\), the model remains admissible and decreases on every positive real argument. Its already-matched prefix remains unchanged.

## The next-moment budget

For the next power sum \(P_{K+1}(b)\),

$$
P_{K+1}'(b)
=(-1)^{K-1}(K+1)Nb\prod_i(x_i(b)-b).
\tag{21.5}\label{eq:21.5}
$$

Combining with (21.3) gives

$$
(-1)^{K-1}dP_{K+1}
=(K+1)b\left(\prod_i x_i(b)\right)(-dq).
\tag{21.6}\label{eq:21.6}
$$

This is an explicit correction budget. It is not an abstract storage function defined using an unknown future cost. The obstacle is global reach: the target deficit must be paid before collision, loss of positivity, or exhaustion of \(q\).

The recorded seven-prefix paths with \(N=1,2,4,8,16,32,64\) supplied approximately 1.74%, 2.40%, 3.01%, 3.51%, 3.90%, 4.18%, and 4.38% of the next required correction before their stopping boundaries. These are numerical diagnostics. They show that the executed paths did not close the next step; they do not prove that another path cannot.

## Canonical coordinates measure feasibility directly

For a feasible moment prefix on \([0,1]\), let \([L_k,U_k]\) be the interval of permitted next moments. The canonical coordinate is

$$
\chi_k=\frac{\mu_k-L_k}{U_k-L_k}.
\tag{21.7}\label{eq:21.7}
$$

This removes artificial singularities caused by colliding quadrature nodes. For \(k=2m\), the lower endpoint is

$$
L_{2m}=v^TA^{-1}v,
\quad A=(\mu_{i+j})_{i,j=0}^{m-1},
\quad v=(\mu_m,\ldots,\mu_{2m-1})^T,
\tag{21.8}\label{eq:21.8}
$$

and the upper endpoint is

$$
U_{2m}=\mu_{2m-1}-w^TB^{-1}w,
\quad B=(\mu_{i+j+1}-\mu_{i+j+2})_{i,j=0}^{m-2},
\tag{21.9}\label{eq:21.9}
$$

with \(w_i=\mu_{m+i}-\mu_{m+i+1}\). An empty inverse term is zero. For odd \(k=2m+1\), use the shifted Hankel lower matrix and the upper-support matrix:

$$
L_{2m+1}=v^TA^{-1}v,
\quad A=(\mu_{i+j+1})_{i,j=0}^{m-1},
\quad v=(\mu_{m+1},\ldots,\mu_{2m})^T,
\tag{21.10}\label{eq:21.10}
$$

$$
U_{2m+1}=\mu_{2m}-w^TB^{-1}w,
\quad B=(\mu_{i+j}-\mu_{i+j+1})_{i,j=0}^{m-1}.
\tag{21.11}\label{eq:21.11}
$$

The interval widths satisfy

$$
U_k-L_k=\prod_{j<k}\chi_j(1-\chi_j).
\tag{21.12}\label{eq:21.12}
$$

This identity quantifies the conditioning of extension. At the recorded 38th step the interval width is about \(1.85\times10^{-72}\). An absolute error described merely as small is inadequate; it must be compared with that actual width.

## Paying the old deficit by moving measures

The moment-continuation study constructs a twelve-node positive quadrature from the actual matrices. Its fractional model matches \(F\) through Taylor order 24. The old seven-prefix entire model has measure

$$
\nu_{\mathrm{old}}=q_{\mathrm{old}}\delta_0+
\sum_i m_i a_i\delta_{a_i}.
\tag{21.13}\label{eq:21.13}
$$

Let \(\nu_{\mathrm{new}}\) be the certified twelve-node measure. The path

$$
\nu_t=(1-t)\nu_{\mathrm{old}}+t\nu_{\mathrm{new}},
\qquad0\le t\le1,
\tag{21.14}\label{eq:21.14}
$$

remains positive and preserves the common prefix. Its next moment moves linearly. The recorded eighth-moment deficit is \(\Delta_8=2.6039136879\ldots\times10^{-11}\), and

$$
p_8(B_t)=p_8(H_{\mathrm{old}})+t\Delta_8.
\tag{21.15}\label{eq:21.15}
$$

At \(t=1\) the entire deficit is paid. There is no node-collision boundary because the path is taken in the convex measure space. The intermediate functions generally have fractional powers and are analytic on the common slit plane, not entire. Chapter 20 explains why that is sufficient for a cofinal limiting argument.

This resolves a particular finite continuation failure in a larger class. It does not imply that a positive endpoint measure exists for the next actual moment at every rank.

## The logical boundary of convexity

The feasible set is convex. Its next-moment interval is nonempty. These statements say that some extensions exist. They do not say that the prescribed \(\Xi\) extension belongs to the interval. The missing assertion is still \(L_k\le\mu_k\le U_k\) for every actual index, or equivalently the appropriate all-rank Hankel condition with analytic continuation.

The value of the convex reformulation is therefore methodological: it removes artificial coordinate failure and shows which boundary is genuinely arithmetic. It is not a proof of that arithmetic boundary's sign.

*Sources:* [PC](#source-pc) §5 and flow diagnostics; [MC](#source-mc) §§3–5 and canonical interval certificates. The integer-factor flow and fractional measure path are different constructions and retain distinct conclusions.

# 22. Heat evolution and the controls that defeat naive induction {#ch-heat-controls}

## Exact evolution of the logarithmic moments

Before renormalizing the linear coefficient, define

$$
A_\tau(w)=\int_0^\infty e^{\tau u^2}\Phi(u)\cosh(u\sqrt w)\,du,
\qquad r_\tau=\partial_w\log A_\tau.
\tag{22.1}\label{eq:22.1}
$$

Differentiation gives

$$
\partial_\tau A_\tau=4wA_{\tau,ww}+2A_{\tau,w},
\tag{22.2}\label{eq:22.2}
$$

and therefore

$$
\partial_\tau r=4wr''+6r'+8wrr'+4r^2.
\tag{22.3}\label{eq:22.3}
$$

Write \(r=\sum_{j\ge1}(-1)^{j-1}\widetilde p_jw^{j-1}\). Coefficient comparison yields

$$
\widetilde p_j'
=-2j(2j+1)\widetilde p_{j+1}
+4j\sum_{a=1}^{j}\widetilde p_a\widetilde p_{j+1-a}.
\tag{22.4}\label{eq:22.4}
$$

Renormalizing \(F'(0)=1\) introduces the derivative of \(\widetilde p_1\). The unscaled hierarchy cannot be applied directly to normalized coefficients without those terms.

For a Schur pivot, set \(q_n=(-H_n^{-1}v_n,1)^T\). Since it minimizes the extended quadratic form with last coordinate fixed,

$$
\delta_n'=q_n^TH_{n+1}'q_n.
\tag{22.5}\label{eq:22.5}
$$

The derivatives of the minimizing vector cancel. Substituting (22.4), the highest new moment appears with coefficient

$$
\widetilde\delta_n'
=-2(2n+1)(4n+3)\widetilde p_{2n+2}
+\mathcal R_n(\widetilde p_1,\ldots,\widetilde p_{2n+1}).
\tag{22.6}\label{eq:22.6}
$$

Thus the previous positive block does not close its own evolution. A first-contact argument needs an independent bound on the next moment or a special identity of the actual kernel. Finite positive pivot derivatives are not an all-rank inward-boundary theorem.

## The complete negative-heat control

Take the complete kernel, not a truncation, and replace it by

$$
\Phi_\tau(u)=e^{\tau u^2}\Phi(u),\qquad\tau=-1/100.
\tag{22.7}\label{eq:22.7}
$$

It retains positivity, smoothness, rapid decay, evenness, and every odd boundary cancellation. Its normalized coefficient matrices pass the same rank-20 and size-19 localizer tests as the actual function. The recorded last Hankel pivot is approximately \(7.5338142431837\times10^{-75}\).

The exact scale dictionary to the Rodgers–Tao heat family is

$$
\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du
=8H_{4\tau}^{\mathrm{RT}}(2z).
\tag{22.8}\label{eq:22.8}
$$

The known nonnegativity of the de Bruijn–Newman constant implies nonreal zeros at negative heat time. There are no purely imaginary zeros because the corresponding cosh integral is positive. Hence the even descent also has nonreal zeros. The single-Hankel theorem then forces failure at a later finite rank.

This is an altered function, not a counterexample to RH. It disproves any proposed induction whose only premises are the properties retained by (22.7) and finite positivity. The exact undeformed arithmetic theta structure must enter somewhere.

## Finite theta truncations lose a boundary cancellation

Let \(\Phi_M=\sum_{m=1}^M\phi_m\), with \(\phi_m\) the summands of (19.1). Direct differentiation gives

$$
\phi_m'(0)=e^{-\pi m^2}
[-16(\pi m^2)^3+60(\pi m^2)^2-30\pi m^2].
\tag{22.9}\label{eq:22.9}
$$

For \(m\ge2\) this is negative, while the full modular identity gives \(\Phi'(0)=0\). Therefore

$$
\Phi_M'(0)=-\sum_{m>M}\phi_m'(0)>0.
\tag{22.10}\label{eq:22.10}
$$

For the truncated cosine transform \(C_M(t)\), two integrations by parts yield

$$
C_M(t)=-\frac{\Phi_M'(0)}{t^2}+o(t^{-2}).
\tag{22.11}\label{eq:22.11}
$$

It has eventually fixed sign and only finitely many real zeros. The descended entire function is nonpolynomial of order below one, so it has infinitely many zeros; consequently infinitely many are nonreal. The same argument applies when the omitted tail is multiplied by any nonnegative constant other than its exact coefficient one.

This explains why a tiny omitted tail may be structurally decisive. The validated coefficient calculations enclose that tail rather than replacing it by zero as an exact function. Small numerical size does not imply stability of the global real-zero property.

## A hierarchy of necessary information

The truncation example shows that boundary evenness is necessary for this family of approximations. The negative-heat example shows it is not sufficient. The heat hierarchy identifies an extra moment entering each pivot. Together they narrow what a successful proof must contain: an arithmetic identity or inequality that distinguishes the undeformed kernel and controls new moment information, not merely a general smooth positive-kernel theorem.

*Sources:* [MC](#source-mc) theta-boundary theorem; [ARK](#source-ark) §§3–5 and negative-heat dictionary. The use of the de Bruijn–Newman theorem is the external input recorded in [ARK](#source-ark); the finite computations are retained as source certificates.

# 23. A direct coefficient kernel and the limits of probabilistic positivity {#ch-bezout}

## Avoiding the logarithmic recurrence in matrix assembly

Let \(F(w)=\sum_{j\ge0}c_jw^j\), with \(c_0=c_1=1\). Define the entire bivariate kernel

$$
\mathcal B_F(z,w)=
\frac{zF'(z)F(w)-wF'(w)F(z)}{z-w},
\tag{23.1}\label{eq:23.1}
$$

with the diagonal singularity removed. Its coefficient matrix is

$$
B_{ij}=\sum_{\ell=0}^{\min(i,j)}
(i+j+1-2\ell)c_{i+j+1-\ell}c_\ell.
\tag{23.2}\label{eq:23.2}
$$

The formula follows by expanding the numerator, pairing the antisymmetric monomials, and dividing \(z^kw^\ell-z^\ell w^k\) by \(z-w\). For actual \(\Xi\), every summand is positive.

Define the triangular matrix

$$
(T_n)_{ij}=\begin{cases}(-1)^jc_{i-j},&i\ge j,\\0,&i<j.
\end{cases}
\tag{23.3}\label{eq:23.3}
$$

The all-rank scout proves the exact congruence

$$
B_n=T_nH_nT_n^T,
\qquad\det B_n=\det H_n.
\tag{23.4}\label{eq:23.4}
$$

Thus the sign problem is identical. Leading determinant ratios, hence corresponding elimination pivots, agree. This is not a proxy matrix with similar entries; it is an exact same-sequence transformation.

## Numerical value without a new sign theorem

Direct assembly avoids the large cancellations in (19.5). The recorded diagonal-scaled conditioning diagnostics improve from roughly \(9.6\times10^{50}\) for \(H_{20}\) to \(1.1\times10^{42}\) for \(B_{20}\). These are numerical condition estimates, not interval eigenvalue bounds. The direct interval certificate for \(B_{20}\) agrees with the Hankel pivot enclosures.

Positive entries do not imply positive semidefiniteness. The exact polynomial

$$
P(w)=1+3w+3w^2+\tfrac12w^3
\tag{23.5}\label{eq:23.5}
$$

gives

$$
B_3=\begin{pmatrix}3&6&3/2\\6&21/2&3\\3/2&3&3/2\end{pmatrix},
\qquad\det B_3=-27/8.
\tag{23.6}\label{eq:23.6}
$$

A positive-kernel factorization of (23.1) for the exact actual \(F\) would therefore be substantive new information. Formula (23.2) alone is not such a factorization.

## Complete monotonicity of the reciprocal is weaker

A possible probabilistic weakening asks whether \(1/F\) is a Laplace transform of a positive density. The scout gives a counterexample to using that property alone. Let

$$
P(w)=1+w+\tfrac38w^2+\tfrac1{16}w^3
=\frac{(1+w/2)((1+w/2)^2+1)}2.
\tag{23.7}\label{eq:23.7}
$$

Then

$$
\frac1{P(w)}=\int_0^\infty e^{-wt}\,4e^{-2t}(1-\cos2t)\,dt.
\tag{23.8}\label{eq:23.8}
$$

The density is nonnegative, so the reciprocal is completely monotone on the positive axis. Yet \(P\) has zeros \(-2,-2+2i,-2-2i\), and its third logarithmic Hankel determinant is \(-1/4096\).

The desired Stieltjes structure of \(F'/F\) is stronger than a positive Laplace representation of \(1/F\). A generalized-gamma-convolution or Thorin representation may contain stronger information, but the exact hypotheses and basepoint persistence must be proved; they cannot be replaced by (23.8).

## What an actual factorization would have to do

A usable factorization of \(\mathcal B_F\) would express every finite coefficient matrix as a positive Gram in a metric derived independently from the actual theta structure. It must survive the negative-heat and truncated-theta controls by using a feature they do not retain. A fitted positive measure reproducing finitely many coefficients is not enough; it merely returns to the finite-prefix problem.

The direct kernel is therefore best viewed as a new calculation surface for the same all-rank question. It can improve symbolic identities, interval conditioning, and recognition of a hidden positive representation. Its main value is eliminating avoidable numerical cancellation while keeping the exact arithmetic target fixed.

*Sources:* [ARK](#source-ark) §§5–7 and Bezout/heat checker; [PC](#source-pc) and [MC](#source-mc) for the positive-resolvent comparison. The recurrence (19.5), the Hankel matrix, and the direct coefficient matrix are three exact descriptions of one sequence.


\part{The original determinant and Jensen programme}

# 24. Boundary absorption: the first Schur gate {#ch-boundary-gate}

The original papers did not begin with the continuum Weil operator. They began with finite determinant inequalities. Their central question was how a signed combination of nearby Schur minors could become positive even though its individual terms were not. This is the earliest precise appearance of a principle that later governed the physical programme: the boundary contribution is part of the object, not an error to be discarded.

The initial result is particularly useful because its domain and its conclusion can be separated completely. It is an exact principal-specialization identity for a family of Schur functions. It is not a theorem asserting total positivity of the actual central coefficients of $\xi$. Its relevance to the later programme is methodological and algebraic; its statement deserves preservation independently of whether that original global application succeeds.

## The three adjacent shapes

For $n\ge3$, define the three-column partitions

$$
\begin{aligned}
 A_r&=(3^r,2^{n-1-r},1^{n-r}),&&0\le r\le n-1,\\
 C_r&=(3^r,2^{n-2-r},1^{n+2-r}),&&0\le r\le n-2,\\
 D_r&=(3^r,2^{n-r},1^{n-2-r}),&&0\le r\le n-2,
\end{aligned}
$$

and $T=A_{n-1}=(3^{n-1},1)$. In this chapter the same symbol denotes a partition and its Schur function; an argument such as $A_r(1^m)$ makes the specialization explicit. The stopped and completed gates are

$$
 P_k=kT+\sum_{r=0}^{k-1}(C_r+D_r-2A_r),\qquad
 G_n=P_{n-1}.
 \tag{24.1}\label{eq:24.1}
$$

The coefficient $k$ multiplying $T$ is the accumulated reservoir for a prefix of length $k$. It is not chosen afterward to force a desired sign. Pieri's rule gives the exact identity

$$
 G_n=(n+2)s_{(3^{n-1},1)}
 -3s_{(1^n)}s_{(2^{n-1})}
 +s_{(1^n)}s_{(2^{n-2},1^2)}.
 \tag{24.2}\label{eq:24.2}
$$

Indeed, the first product on the right expands as $\sum_{r=0}^{n-1}A_r$, and the second as $\sum_{r=0}^{n-2}(C_r+A_r+D_r)$. The top $A_{n-1}=T$ then changes $(n+2)T$ into $(n-1)T$. This derivation explains why the coefficient of the boundary term is fixed.

## Curvature on the $A_2$ strip

Write $\mathscr S(x,y,z)=s_{(x,y,z)'}$ and put

$$
 p_r=(2n-1-r,n-1,r),\quad
 \alpha=(1,-1,0),\quad\beta=(-1,0,1).
$$

Conjugating the three partitions gives

$$
 C_r=\mathscr S(p_r+\alpha),\quad
 A_r=\mathscr S(p_r),\quad
 D_r=\mathscr S(p_r-\alpha).
$$

Thus $C_r+D_r-2A_r=\Delta_\alpha^2\mathscr S(p_r)$, while $p_{r+1}=p_r+\beta$. The completed gate is an integrated transverse curvature along a finite strip, with an endpoint reservoir. The source's counterexamples to local positivity are not defects in this description. They explain why a term-by-term proof would demand more than the gate itself requires.

There is a direct analogy with reference-relative Schur accounting, but not an identification: the variables here are shapes and specialization parameters, not physical functions or prime-dependent source columns. In both settings the useful cancellation is visible only after the complete signed expression has been retained.

## Hook-content evaluation and the forced roots

For a three-column partition $(3^a,2^b,1^c)$, let $N=a+b+c$ and use falling factorials $x^{\underline r}$. The specialization is

$$
 S(a,b,c;m)=
 \frac{m^{\underline a}(m+1)^{\underline a}(m+2)^{\underline a}
 (m-a)^{\underline b}(m+1-a)^{\underline b}
 (m-a-b)^{\underline c}}{\mathcal H(a,b,c)},
 \tag{24.3}\label{eq:24.3}
$$

where

$$
 \mathcal H(a,b,c)=
 \frac{(N+2)!}{(N+2-a)!}
 \frac{(a+b+1)!}{(b+1)!}a!
 \frac{(b+c+1)!}{(c+1)!}b!c!.
$$

The minimum content multiplicity shared by the terms of a prefix gives the baseline factor

$$
 \mathcal B_n(m)=
 (m-n+1)(m-n+2)(m-n+3)(m+1)
 \prod_{j=0}^{n-4}(m-j)^2.
 \tag{24.4}\label{eq:24.4}
$$

This part is termwise: one obtains it by listing the contents in each column and taking the minimum number of occurrences of each linear factor. There are two further cancellation mechanisms, neither termwise.

First, $P_k(-2)=0$. Principal specialization at $-2$ conjugates the partitions, up to their common parity. All three-column conjugates vanish in two variables except the $r=0$ remnants. Their dimensions are $n+3$, $n+1$, and $n-1$, so the relevant combination is

$$
 (n+3)+(n-1)-2(n+1)=0.
$$

This supplies the universal factor $m+2$.

Second, the completed Pieri form has one additional zero at each integer $t$ with $0\le t\le n-3$, after the baseline is divided out. The hook-content formula counts the order at $m=t$ by counting cells of content $-t$. The three terms of (24.2) each have at least one more such cell than the common baseline requires. For the normalized local summands, indices $r\ge t+3$ already vanish separately because of the third-column cell $(t+3,3)$. Therefore the remaining finite band satisfies

$$
 \sum_{r=0}^{t+2}
 \left.\frac{C_r(m)+D_r(m)-2A_r(m)}{\mathcal B_n(m)}\right|_{m=t}=0.
 \tag{24.5}\label{eq:24.5}
$$

This is the finite-band cancellation. It is a statement about the completed sum, not positivity of its summands.

## Degree cancellation completes the factorization

All the shapes have size $3n-2$. If $\sigma(\lambda)$ is the sum of contents, then

$$
 s_\lambda(1^m)=
 \frac{m^{3n-2}}{\mathcal H(\lambda)}
 +\frac{\sigma(\lambda)}{\mathcal H(\lambda)}m^{3n-3}
 +O(m^{3n-4}).
$$

Paper I gives exact rational telescoping certificates for the reciprocal-hook coefficient and the centered first content moment. They yield

$$
 [m^{3n-2}]G_n=0,\qquad
 [m^{3n-3}]G_n=\frac6{n!(n+1)!(n-2)!}.
 \tag{24.6}\label{eq:24.6}
$$

For example, if

$$
 f_r=\mathcal H(C_r)^{-1}+\mathcal H(D_r)^{-1}-2\mathcal H(A_r)^{-1},
$$

the certificate is $f_r=Z_{r+1}-Z_r$ with $Z_0=0$ and, for $r\ge1$,

$$
 Z_r=\frac{P_n(r)}{(r-1)!(n+1)!(2n-r+2)!},
$$

$$
\begin{aligned}
P_n(r)={}&n^4-4n^3r-n^3+6n^2r^2-19n^2-4nr^3+3nr^2\\
&+17nr-23n+r^4-2r^3-4r^2+11r-6.
\end{aligned}
$$

The boundary value $r=0$ is checked directly rather than assigning a meaning to $(-1)!$. Summing gives precisely the negative of the reservoir's leading coefficient. The full first-content certificate is retained in the source and equation register; it is a degree-six polynomial identity, not an asymptotic numerical fit.

The forced roots in (24.4)–(24.5), the factor $m+2$, and the degree and leading coefficient now determine the polynomial:

$$
 \boxed{
 G_n(1^m)=
 \frac{6(m+1)(m+2)}{n!(n+1)!(n-2)!}
 \prod_{j=0}^{n-1}(m-j)^{e_{n,j}},
 \quad e_{n,j}=\min\{3,\max(1,n-j-1)\},
 \quad n\ge3.}
 \tag{24.7}\label{eq:24.7}
$$

In particular it is positive for $m\ge2n-1$.

The original text prints this formula also for $n=2$. Direct substitution into its defining Schur gate instead gives

$$
 G_2(1^m)=\frac12m(m-1)(m+2).
 \tag{24.8}\label{eq:24.8}
$$

The extra $m+1$ in the printed uniform product is absent in this boundary case. The book therefore separates $n=2$ explicitly. The original file is unchanged, and the exact small-case calculation is included in the editorial verification record. This boundary correction does not alter the $n\ge3$ product.

## The unfinished prefix extension

After removing the roots available to $P_k$, define the shifted residual at $m=2n-1+y$. Paper I conjectured nonnegative coefficients of that residual for all prefixes. The completed endpoint (24.7) does not prove this stronger assertion: stopping the sum removes part of the cancellation. The distinction led directly to Paper IV's rising-factorial analysis.

**Sources:** [P1](#source-p1), especially the Pieri reduction, hook-content kernel, finite-band theorem, and endpoint certificates. The $n=2$ boundary correction is recorded separately in the editorial checks. The original principal-specialization argument is not an actual-$\xi$ total-positivity theorem.

# 25. Reciprocal pairs and the flagged reservoir {#ch-reciprocal}

The second paper asks whether the reservoir survives perturbing the all-ones alphabet by reciprocal pairs. Such a deformation is more informative than evaluating a single symmetric point: it tests distinct real directions in a finite root cloud. The important discovery is that the perturbation changes both the row degree and the effective alphabet size. Treating it as an unqualified row-lowering operator loses the correct cross terms.

## Row entries before determinant expansion

Put $u=\cosh a-1$ and $v=\cosh b-1$. The elementary symmetric function on two reciprocal pairs is

$$
 e_r(e^a,e^{-a},e^b,e^{-b},1^{m-4})
 =\binom mr+2(u+v)\binom{m-2}{r-1}
 +4uv\binom{m-4}{r-2}.
 \tag{25.1}\label{eq:25.1}
$$

This follows directly by multiplying the generating factors

$$
 (1+te^a)(1+te^{-a})=(1+t)^2+2ut
$$

and its $b$ counterpart. For $k$ pairs, the same argument gives

$$
 e_r=\sum_{\ell=0}^k2^\ell e_\ell(u_1,\ldots,u_k)
 \binom{m-2\ell}{r-\ell}.
 \tag{25.2}\label{eq:25.2}
$$

The literal alphabet requires $m\ge2k$. Evaluations outside this range can still be polynomial continuations of the binomial determinant, but must not be described as literal alphabets.

For a row-level vector $s=(s_1,s_2,s_3)$, define

$$
 D_\lambda^s(m)=
 \det\left[\binom{m-2s_i}{\lambda'_i-i+j-s_i}\right]_{i,j=1}^3.
 \tag{25.3}\label{eq:25.3}
$$

Insert these determinants in (24.1) to obtain the flagged gate $\mathcal M_n^s$. If $\mathcal O(a,b,c)$ is its sum over distinct row permutations, then the two-pair middle coefficients are

$$
\begin{aligned}
 c_{11}&=4[\mathcal O(2,0,0)+2\mathcal O(1,1,0)],\\
 c_{21}&=8[\mathcal O(2,1,0)+3\mathcal O(1,1,1)],\\
 c_{22}&=16[\mathcal O(2,2,0)+2\mathcal O(2,1,1)].
\end{aligned}
 \tag{25.4}\label{eq:25.4}
$$

The repair is not optional. In particular, the isolated second-shift orbit $\mathcal O(2,0,0)$ is not the correct positivity object. Its forced partner $2\mathcal O(1,1,0)$ is the reservoir supplied by the same reciprocal expansion.

## A counting convention that matters

It is safest to write the fully mixed coefficient first as an ordered row-level sum:

$$
 M_k=2^k\sum_{s_1+s_2+s_3=k}
 \frac{k!}{s_1!s_2!s_3!}\mathcal M_n^{(s_1,s_2,s_3)}.
 \tag{25.5}\label{eq:25.5}
$$

The multinomial counts the distribution of the $k$ distinct variables among the three rows. Grouping the ordered triples into permutation orbits yields

$$
 M_k=2^k\sum_{\substack{a\ge b\ge c\ge0\\a+b+c=k}}
 \frac{k!}{a!b!c!}\mathcal O(a,b,c).
 \tag{25.6}\label{eq:25.6}
$$

The source prints an orbit-sum formula with an unrestricted triple index. Its explanatory convention and examples require each orbit to occur once. Equations (25.5)–(25.6) make that convention explicit: summing all ordered triples *and* summing all row permutations again would double-count. This is an indexing reconciliation, not a new positivity assertion.

For $k=3$, the result is

$$
 M_3=d_{111}=8[\mathcal O(3,0,0)
 +3\mathcal O(2,1,0)+6\mathcal O(1,1,1)].
 \tag{25.7}\label{eq:25.7}
$$

The integers $1,3,6$ have a combinatorial origin; replacing them by arbitrary favorable weights would change the gate.

## What the finite positivity theorem actually controls

Paper II's principal theorem is coefficientwise positivity of the complete two-pair specialization for $n\ge3$ and $m\ge2n-1$. It also treats the first fully mixed three-pair coefficient. It does not establish positivity of the whole $k$-pair polynomial for arbitrary $k$.

The proof reduces coefficients to rational functions of the endpoint shift $h=m-(2n-1)\ge0$. After dividing positive affine skeletons, the remaining polynomials have small fixed degree in $h$. The dangerous two-pair coefficients have residual degrees four or six. The proof is therefore not an enormous numerical scan over $h$: it is a finite symbolic coefficient calculation followed by parameter inequalities in $n$.

For the three-pair term and $n\ge9$, write

$$
 d_{111}=\frac{S_{3,n}(h)}{D_{3,n}}\sum_{j=0}^6R_j(n)h^j,
 \qquad D_{3,n}=\frac{n!(n+1)!(n-2)!}{48},
 \tag{25.8}\label{eq:25.8}
$$

where

$$
\begin{aligned}
S_{3,n}(h)={}&(h+n-1)(h+n)(h+n+1)(h+n+2)^2\\
&\times\prod_{j=n+3}^{2n-7}(h+j)^3
 \prod_{j=2n-6}^{2n-3}(h+j)^2(h+2n-2)(h+2n-1).
\end{aligned}
$$

All these affine factors are positive. The leading residual coefficients are

$$
 R_6=3(n+2)(3n-5)(3n-4),
$$

$$
 R_5=3(3n-5)(30n^3-n^2-98n+8),
$$

and the constant coefficient is

$$
 R_0=36n(n-3)(n-2)(n+1)
 (12n^5-12n^4-75n^3+55n^2+96n-20).
 \tag{25.9}\label{eq:25.9}
$$

The intermediate coefficient polynomials and all small-case factorizations are retained in the exact source corpus. Their proof follows a reusable pattern: group a high power of $n$ times an increasing positive quadratic and leave a manifestly positive lower-degree remainder. For example,

$$
\begin{aligned}
R_4/3={}&n^3(369n^2-882n-970)\\
&+2859n^2-502n-360.
\end{aligned}
$$

Both groups are positive from $n=9$ onward. Analogous decompositions handle $R_3,R_2,R_1,R_0$. The cases $3\le n\le8$ use direct factorizations; for instance

$$
 d_{111}(3,5+h)=4(25h^3+390h^2+1925h+2754)>0.
$$

At $h=0$ this is a polynomial continuation, because a literal three-pair alphabet needs six variables.

## The lasting insight

The reciprocal construction supplies an exact finite instance of cancellation among channels generated by a common input. It anticipates why a common multiplier in the later Euler framework must be applied to the complete difference rather than separately to its two halves. However, the finite Schur alphabet does not furnish the physical norm of that later multiplier. What transfers without further proof is the discipline of retaining the forced mixed terms; the analytic estimate does not transfer by analogy.

**Sources:** [P2](#source-p2), the flagged determinant and coefficient-extraction sections, all four certificate appendices; [P3](#source-p3) for the inherited orbit convention. The ordered/orbit distinction in (25.5)–(25.6) is recorded in the editorial correction register.

# 26. Cocircuits, finite chains, and the retracted skeleton {#ch-cocircuit}

**Later audit supersedes this historical chapter.** The October 9 exact calculation $\mathcal A_4^{\mathrm{mix}}(4,4)=-13\,888$ disproves the original value-root skeleton. The original determinant-to-boundary map also fails; see the corrected (A38) and its hypotheses. The source-era derivation and notation are retained below solely as historical evidence. Any assertion of universal vanishing or the divisor (26.4) is **not** an accepted theorem in this edition.

The third original paper changes the question from positivity to divisibility. Before estimating a residual polynomial, identify every root forced by the finite combinatorics. A large part of a complicated polynomial can then be removed exactly, with no inequality and no numerical root finding.

The official gate remains a finite flagged Jacobi–Trudi expression. The coefficient model is its proposed boundary representation, not a new arithmetic object that may be substituted without checking the determinant-to-kernel map. The orbit convention of the preceding chapter is retained explicitly.

## The fourth-order difference hidden in the boundary

The low boundary kernel is

$$
 P_{\rm low}(X,Y,Z)=Z\frac{(X-Y)^3(Y-Z)}{XY}.
$$

Set $\nabla_\alpha=1-Y/X$ and $\nabla_\beta=1-Z/Y$. Direct multiplication gives

$$
 \boxed{P_{\rm low}=X^2Z\nabla_\alpha^3\nabla_\beta.}
 \tag{26.1}\label{eq:26.1}
$$

The total difference order is four: cubic in one direction and linear in another. Referring to this simply as “the cubic” risks losing the transverse factor. The monomial $X^2Z$ shifts coefficient targets; all annihilation lies in the difference operators.

The finite chain uses $e^\delta=X/Z$ and

$$
 \sum_{r=0}^{n-2}e^{r\delta}
 =\frac{1-e^{(n-1)\delta}}{1-e^\delta}.
$$

Multiplication by $\nabla_\delta=1-e^\delta$ leaves only the two endpoints:

$$
 \nabla_\delta\sum_{r=0}^{n-2}e^{r\delta}
 =1-e^{(n-1)\delta}.
 \tag{26.2}\label{eq:26.2}
$$

The low/high difference is the elementary Brion decomposition used in the source. Its virtue is not the name of the formula but that the endpoint cancellation is performed before expanding the determinant into many separate terms.

## Coefficient targets and derivative layers

The coefficient functional samples the chain

$$
 (E_X(r),E_Y,E_Z(r))=(2n+1-r,n,r),\qquad0\le r\le n-2.
$$

For each row level, binomial series such as $(1+X)^{m-2s_X}$ are interpreted polynomially in $m$ at each fixed coefficient. Thus the finite mixed gate $\mathcal A_k(n,m)$ is a polynomial in $m$, even when an individual generating expression has a negative exponent.

The source studies the first three derivative layers

$$
 \mathcal A_k^{[j]}(n,t)
 =\left.\partial_m^j\mathcal A_k(n,m)\right|_{m=t},
 \qquad j=0,1,2.
$$

Its **historically claimed but invalidated** skeleton theorem, for $k\ge4$, used the intervals

$$
\begin{array}{lll}
L_{k,0}=\lfloor(2k-4)/3\rfloor,&
U_{k,0}=n+\lfloor(k-3)/3\rfloor,\\
L_{k,1}=2\lfloor k/2\rfloor,&U_{k,1}=n-3,\\
L_{k,2}=2k,&U_{k,2}=n-4.
\end{array}
 \tag{26.3}\label{eq:26.3}
$$

The original source *purported* to prove vanishing by combining low-endpoint bounds, high-endpoint bounds, and proper-face clearing; the 9 October counterexample shows the global claimed implication is false. The first-derivative upper boundary includes an exceptional $XZ$ contribution that cancels only after the paired Brion endpoints are combined. The isolated high vertex is not the completed boundary functional.

The resulting **invalidated** proposed divisor is

$$
 S_{k,n}(m)=
 \prod_{t=L_{k,0}}^{U_{k,0}}(m-t)
 \prod_{t=L_{k,1}}^{U_{k,1}}(m-t)
 \prod_{t=L_{k,2}}^{U_{k,2}}(m-t).
 \tag{26.4}\label{eq:26.4}
$$

Empty intervals contribute one. Wherever the derivative intervals are nonempty, they are nested inside the preceding value intervals. Formally, *if* the stated vanishing held, the value/derivative layers would force multiplicities one, two and three. **Because their premise fails, no such universal multiplicity conclusion is established.** This last divisibility step is elementary; the substantive source-specific work is the determinant-to-boundary representation and the clearing of every face.

The complete proof bodies and the chain-alignment and $XZ$-gluing coefficient certificates remain separately retrievable. The book does not replace those hypotheses by the visually attractive factorization (26.1).

## Why the residual is the real object

A valid forced-root skeleton would say where zeros must occur, not where remaining zeros lie; the historical universal skeleton in this chapter has been invalidated. Dividing $\mathcal A_k$ by $S_{k,n}$ was proposed as a reduction, but it is not generally polynomial division after the 9 October counterexample. A replacement forced divisor must first be rigorously established. This is the conceptual transition to Paper IV and, later, to curvature-matched Jensen models: remove what is known exactly, then make the unknown remainder explicit.

There is a useful candidate connection to the modern neighboring-band response. The pole, first harmonic, and boundary jets are low-order modes. If their *actual* removal generated a native third difference, the signed response could have improved regularity. The archive contains no identity proving that this modern residual equals the old cocircuit operator. The connection is a precisely stated research possibility, not a transfer theorem. The missing item is an intertwining map carrying the complete source and its physical metric to the finite-difference representation, including cutoff boundaries.

**Sources:** [P3](#source-p3), especially the determinant definition, cocircuit factorization, proper-face and endpoint arguments, skeleton intervals, and the two coefficient-certificate appendices. Equations (26.1)–(26.2) are direct algebra; the full gate divisibility uses the additional source-specific identifications.

# 27. Prefix residuals and rising-factorial positivity {#ch-rising}

Paper I closes the full endpoint. A prefix loses some of the completed cancellation. Paper IV asks whether a positive basis still organizes what remains after the roots already forced at the prefix are divided out. This is a more precise question than “is the polynomial positive?” because the basis encodes a family of finite-difference inequalities at the shifted endpoint.

## The residual and the two factorial bases

For the interior range

$$
 n\ge4,\qquad2\le k\le n-2,\qquad D=n-k,
$$

put

$$
 \mathcal C^+_{n,k}(m)=(m+2)\prod_{j=0}^{k-3}(m-j),
$$

$$
 R_{n,k}(y)=
 \frac{P_k(2n-1+y)}{
 \mathcal B_n(2n-1+y)\mathcal C^+_{n,k}(2n-1+y)}.
 \tag{27.1}\label{eq:27.1}
$$

The degree in this stable interior is $D+1$. Expand it in rising factorials,

$$
 R_{n,k}(y)=\sum_{j=0}^{D+1}a_{n,k,j}y^{\overline j},
 \qquad y^{\overline j}=y(y+1)\cdots(y+j-1).
 \tag{27.2}\label{eq:27.2}
$$

The coefficients satisfy

$$
 a_{n,k,j}=\frac{\nabla^jR_{n,k}(0)}{j!},
 \qquad\nabla f(y)=f(y)-f(y-1).
$$

This follows from the Newton expansion at the backward lattice. A nonnegative rising expansion implies a nonnegative falling-factorial expansion because

$$
 y^{\overline r}=\sum_{j=0}^rL(r,j)y^{\underline j},
 \qquad L(r,j)\ge0.
 \tag{27.3}\label{eq:27.3}
$$

Dividing $y^{\underline j}$ by $j!$ then yields nonnegative Newton-binomial coefficients. This is a valid positive change of basis. It must not be confused with the later invalid assertion that an arbitrary factorial normalization is a positive *matrix congruence* on a Hankel form.

## Four layers, not the whole polynomial

The source proves the four highest rising coefficients in the interior range:

$$
 a_{n,k,D+1}>0,\quad a_{n,k,D}>0,\quad
 a_{n,k,D-1}>0,\quad a_{n,k,D-2}>0.
 \tag{27.4}\label{eq:27.4}
$$

The complete coefficientwise claim $a_{n,k,j}\ge0$ for every $j$ is left as a conjecture. This is a meaningful distinction even though $D$ is arbitrary: the theorem is uniform in the parameters for four layers, not uniform in layer depth.

The common proof mechanism is worth preserving in detail. A Schur specialization has leading coefficients given by elementary symmetric polynomials in its contents, divided by its hook product. At each of the first four layers, the signed prefix sum admits a rational antidifference. The entire prefix contribution collapses to an endpoint at $r=k$, plus the accumulated reservoir. After positive factors are removed, the remaining comparison is controlled by

$$
 \mathscr R_{n,D}
 =\frac{(n-D)!(n+D+2)!}{(n-1)!(n+2)!}.
 \tag{27.5}\label{eq:27.5}
$$

The source's reservoir domination proof rewrites the factorial ratio as a product, separates the potentially adverse endpoint term, and substitutes $n=D+s+2$. The resulting polynomial in $D$ and $s$ has nonnegative coefficients in the stated range.

This procedure is stronger than checking many $n$ values: a finite polynomial identity and positivity of its coefficients establish every allowed $n$. Conversely, a successful certificate at content layers $0,1,2,3$ gives no automatic certificate at layer $4$.

## An example of the bookkeeping principle

If a signed layer is $f_r=Z_{r+1}-Z_r$, the prefix is $Z_k-Z_0$. Its sign may be unfavorable. The gate, however, is $kT+Z_k-Z_0$. The relevant inequality compares that *whole expression* with zero. Estimating $|Z_k|+|Z_0|$ would erase the endpoint cancellation; ignoring $Z_k$ would fabricate positivity.

In the modern physical language, this is the distinction between a complete reference-plus-perturbation form and a separate cross norm. The correspondence is conceptual: the source does not supply a map from $\mathscr R_{n,D}$ to the available spectral energy in a Weil block.

The shortest prefix $k=1$ and the full endpoint $k=n-1$ are treated separately in the source, since the stable skeleton or residual degree can change. This is the same reason the $n=2$ exceptional product in Chapter 24 cannot be absorbed by informal empty-product conventions.

## What would make the method reusable today

The algebra offers two concrete tools. First, look for an exact antidifference before estimating a signed band sum. Second, choose a basis whose finite-difference coefficients match the desired one-sided inequality. Neither requires that the whole original prefix conjecture be solved first.

A transplant must retain the actual summation weights, the endpoint contribution, and any change in the domain. The all-prime rational triple sum is not a sequence of Schur-content polynomials merely because both have adjacent indices. The unsolved connection is an exact representation theorem, not an invitation to rename the arithmetic variables.

**Sources:** [P4](#source-p4), the residual definition, top-four-layer theorems, rational telescoping certificates, reservoir polynomials, and separate boundary cases. [P1](#source-p1) supplies the endpoint skeleton. The full rising-residual conjecture remains distinct from (27.4).

# 28. Boundary ladders and a finite Sturm mechanism {#ch-ladder}

The fifth original paper introduces a local dynamical description of Euclidean polynomial division. Rather than recompute every next polynomial, it transports a small collection of boundary determinants and a closed coefficient ladder. This produces a genuine propagation theorem under explicit sign conditions. The all-degree application remains a separate issue.

## One signed remainder

Let

$$
 A(z)=\sum_{i=0}^ma_iz^i,\qquad
 B(z)=\sum_{i=0}^{m-1}b_iz^i,\qquad b_{m-1}\ne0,
$$

and let $S=-\operatorname{rem}(A,B)$. Since the degree gap is one,

$$
 S=(q_1z+q_0)B-A,
 \quad q_1=\frac{a_m}{b_{m-1}},
 \quad q_0=\frac{\Theta}{b_{m-1}^2},
$$

where

$$
 \Theta=a_{m-1}b_{m-1}-a_mb_{m-2},\qquad
 \Phi=\Theta b_0-a_0b_{m-1}^2.
 \tag{28.1}\label{eq:28.1}
$$

Then $S(0)=\Phi/b_{m-1}^2$. For $0\le j\le m-3$, define

$$
 \Omega_j=a_mb_{m-3-j}b_{m-1}
 +\Theta b_{m-2-j}-a_{m-2-j}b_{m-1}^2,
$$

with $\Omega_{-1}=0$ and $\Omega_{m-2}=\Phi$. Direct coefficient comparison gives

$$
 [z^{m-2-j}]S=\frac{\Omega_j}{b_{m-1}^2}.
 \tag{28.2}\label{eq:28.2}
$$

The endpoint convention is mathematically substantive. It makes the bottom coefficient part of the same closed ladder as the leading coefficient.

## Transport to the next pair

Moving from $(A,B)$ to $(B,S)$ gives polynomial numerators

$$
\begin{aligned}
 \Theta^+&=b_{m-2}\Omega_0-b_{m-1}\Omega_1,\\
 \Phi^+&=\Theta^+\Phi-b_0\Omega_0^2,\\
 \Omega_j^+&=b_{m-1}\Omega_0\Omega_{j+2}
 +\Theta^+\Omega_{j+1}-b_{m-3-j}\Omega_0^2.
\end{aligned}
 \tag{28.3}\label{eq:28.3}
$$

The actual next determinants are $\Theta^+/b_{m-1}^2$, $\Phi^+/b_{m-1}^4$, and $\Omega_j^+/b_{m-1}^4$. These formulas follow by substituting (28.2) into the definitions for the next pair. Positive rescaling of $A$ and $B$ changes them by positive powers, so sign checks may be carried out in a primitive pseudo-remainder gauge rather than with enormous rational coefficients.

Assume the current ladder is positive. Introduce the compensated ratio

$$
 K_j=\frac{b_{m-3-j}\Omega_0-b_{m-1}\Omega_{j+2}}
 {\Omega_{j+1}}.
$$

Equation (28.3) becomes

$$
 \Omega_j^+=\Omega_{j+1}(\Theta^+-\Omega_0K_j).
 \tag{28.4}\label{eq:28.4}
$$

Thus the first next rung is enough if all later $K_j$ lie below $K_0$. This reduces many transported inequalities to one starting inequality and a monotonicity condition.

## The exact third-order minor

For $0\le j\le m-5$, set

$$
 \Delta_{1,j}=
 \det\begin{pmatrix}
 \Omega_0&b_{m-1}&0\\
 \Omega_{j+2}&b_{m-3-j}&\Omega_{j+1}\\
 \Omega_{j+3}&b_{m-4-j}&\Omega_{j+2}
 \end{pmatrix}.
$$

Subtracting the two fractions gives

$$
 \boxed{K_j-K_{j+1}
 =\frac{\Delta_{1,j}}{\Omega_{j+1}\Omega_{j+2}}.}
 \tag{28.5}\label{eq:28.5}
$$

The minors come from one closed three-row matrix with columns

$$
 C_t=\begin{pmatrix}\Omega_t\\b_{m-1-t}\\\Omega_{t-1}\end{pmatrix}:
 \qquad\Delta_{1,j}=\det(C_0,C_{j+2},C_{j+3}).
$$

This is not an arbitrary list of determinants. It is a special third-order positivity condition on the same transported boundary data. Full total positivity is stronger than the argument needs.

Consequently, if the current ladder and bottom determinant are positive, and

$$
 \Phi^+>0,\qquad\Omega_0^+>0,\qquad
 \Delta_{1,j}>0\quad\text{for every admissible }j,
 \tag{28.6}\label{eq:28.6}
$$

the next pair has positive bottom determinant and positive ladder. Indeed, (28.5) makes $K_j$ decreasing, so (28.4) propagates the first-rung bound to every later rung. The separate $\Phi^+$ inequality controls the bottom.

## From local propagation to vertical interlacing

For a monic Newton–Jensen family of degree $D+1$, the raising pair is

$$
 T_0=\widehat J_{n,D},\qquad
 T_1=\widehat J_{n+1,D}-\widehat J_{n,D},\qquad
 T_{r+1}=-\operatorname{rem}(T_{r-1},T_r).
 \tag{28.7}\label{eq:28.7}
$$

Full degree descent and the required endpoint signs let the signed Sturm argument conclude vertical interlacing. Paper V formulates the finite $D=5$ mechanism, including the degree pattern $6,5,4,3,2,1,0$ and lower-degree tail reductions. Its conditional moving theorem requires the listed base, initial, propagation, and descent certificates. It is not an unrestricted theorem that every Newton–Jensen family has those signs.

The important reusable module is (28.3)–(28.6): a nonlinear boundary recursion with an explicit first-rung criterion. It suggests the correct form of a new invariant theorem, but the actual $\Xi$ parameters still have to satisfy its hypotheses throughout the desired range.

**Sources:** [P5](#source-p5), local Euclidean identities, transported ladder, compensated ratios, Boundary–Hausdorff minors, primitive gauge, and the conditional $D=5$ certificate architecture. Original [P5](#source-p5)'s polynomial degree label differs from the later convention $\deg J^{d,n}=d$; the definitions, not the shared letter, determine the map.


# 29. Vertical proper position and the Jensen Wronskian {#ch-vertical}

Paper VI supplies a particularly durable finite theorem. It translates one-degree-higher hyperbolicity into oriented interlacing of two adjacent-shift descendants. The identities are exact for any coefficient sequence; positivity enters only at the proper-position step. This clean separation makes the module useful independently of the much more ambitious later attempts to cover all parameter values.

## Three identities with one normalization

For a positive sequence $\gamma_n$, let

$$
 J_{n,d}(z)=\sum_{k=0}^d\binom dk\gamma_{n+k}z^k.
$$

With $R=J_{n,d+1}$, $P=J_{n,d}$ and $Q=J_{n+1,d}$, binomial identities give

$$
 Q=\frac{R'}{d+1},\qquad
 P=R-\frac{zR'}{d+1},\qquad
 R=P+zQ.
 \tag{29.1}\label{eq:29.1}
$$

For example, differentiating the $z^{k+1}$ coefficient uses
$(k+1)\binom{d+1}{k+1}=(d+1)\binom dk$. The last identity is Pascal's rule. They are not asymptotic approximations and require no information about zeros.

Say $P\ll Q$ when both have simple negative roots, positive leading coefficients, and the source's oriented Wronskian is positive:

$$
 W[P,Q]=P'Q-PQ'>0\quad\text{on }\mathbb R.
$$

The strict convention matters. Repeated roots require limiting statements and do not automatically satisfy the strict inequality.

## The polar-derivative theorem

Suppose $R(z)=c\prod_{i=1}^{d+1}(z+\alpha_i)$, where $c>0$ and the $\alpha_i$ are positive and distinct. Rolle's theorem gives negative simple roots for $Q=R'/(d+1)$. The polar descendant $P$ has the corresponding negative interlacing roots. The orientation can be proved directly:

$$
 W[P,Q]=\frac{d(R')^2-(d+1)RR''}{(d+1)^2}.
 \tag{29.2}\label{eq:29.2}
$$

Away from the roots of $R$, the numerator divided by $R^2$ is

$$
 (d+1)\sum_i\frac1{(z+\alpha_i)^2}
 -\left(\sum_i\frac1{z+\alpha_i}\right)^2>0.
$$

This is the strict Cauchy–Schwarz variance of the distinct reciprocal distances. The polynomial identity extends across the roots. Thus $P\ll Q$.

Conversely, suppose $P,Q$ have the same degree $d$ and $P\ll Q$. The roots of $P+\lambda zQ$, $\lambda>0$, satisfy

$$
 \frac{Q(z)}{P(z)}=-\frac1{\lambda z}.
 \tag{29.3}\label{eq:29.3}
$$

On each interval cut by the negative roots of $P$, the left side has negative derivative and the appropriate pole jumps; the right side is positive and increasing on the negative axis. The endpoint limits give one crossing in each of the $d+1$ intervals. Positive coefficients exclude positive roots. Thus $P+\lambda zQ$ has $d+1$ simple negative roots.

At a crossing, implicit differentiation also shows that its root moves right as $\lambda$ increases. The derivative of the left-minus-right equation in $z$ is negative; its derivative in $\lambda$ is positive. Therefore the root velocity is positive. This monotonicity is a real theorem about the interpolating pencil, not a monotonicity claim for arbitrary changes of the $\Xi$ coefficients.

Combining the two directions with (29.1) gives the vertical equivalence in its strict form:

$$
 J_{n,d+1}\text{ has simple negative roots}
 \iff J_{n,d}\ll J_{n+1,d}.
 \tag{29.4}\label{eq:29.4}
$$

## The coefficient-side Wronskian

Define the adjacent coefficient minors

$$
 D_{i,j}^{(n)}=
 \gamma_{n+i+1}\gamma_{n+j}
 -\gamma_{n+i}\gamma_{n+j+1}.
$$

Pairing the $(i,j)$ and $(j,i)$ terms of $P'Q-PQ'$ yields

$$
 W_{n,d}(z)=
 \sum_{0\le i<j\le d}
 (j-i)\binom di\binom djD_{i,j}^{(n)}z^{i+j-1}.
 \tag{29.5}\label{eq:29.5}
$$

This formula retains signs that can be lost in a coefficientwise argument: odd powers of a negative $z$ contribute negatively even when their coefficients are positive. Positivity of individual adjacent minors therefore does not settle positivity of the whole Wronskian on the real line.

Let $W_{n,d}(z)=\sum_{r=0}^{2d-2}q_rz^r$ and $v_d(z)=(1,z,\ldots,z^{d-1})^T$. The Gram representations form an affine space

$$
 \mathcal G_{n,d}=
 \left\{M=M^T:\sum_{i+j=r}M_{ij}=q_r,
 \ 0\le r\le2d-2\right\}.
 \tag{29.6}\label{eq:29.6}
$$

Its dimension is $(d-1)(d-2)/2$. If the Wronskian has degree exactly $2d-2$ and is strictly positive on $\mathbb R$, there is a positive-definite Gram in this space. To see this explicitly, subtract a sufficiently small positive multiple of $1+z^2+\cdots+z^{2d-2}$; strict positivity and the positive leading coefficient ensure the remainder is still nonnegative. A univariate nonnegative polynomial is a sum of squares, and adding back the small multiple yields a positive-definite Gram. Conversely a positive-definite Gram is visibly strictly positive on the monomial vector.

The exact-degree requirement prevents a misleading extension: a positive constant polynomial cannot have a positive-definite Gram in an arbitrarily high monomial basis, because that would force a positive highest coefficient.

## What this buys, and what remains

The finite feasibility problem (29.6) is often more manageable than roots themselves. Its affine degrees of freedom permit a Gram completion without assigning one canonical matrix to the Wronskian. Paper VI further develops low-degree gates, Schur-pivot curvature, descendant Sturm conditions, and a $D=6$ gateway. Those are preserved as separate modules, with the degrees and determinant hypotheses in the source register.

The later observation that cofinal *unshifted* Jensen hyperbolicity suffices for RH reduces the desired endpoint. It does not let one move backward from a proved large-shift region to $n=0$. Differentiation can erase nonreal roots, as the polynomial example in Chapter 3 shows. The vertical identities explain how a verified proper-position statement would perform that move; they do not assert the missing proper position.

**Sources:** [P6](#source-p6), Jensen identities, polar derivative, reconstruction, Wronskian coefficients and affine Gram sections. The strict/weak-root distinction and the exact-degree condition are stated explicitly here to retain the theorem's usable scope.

# 30. The centered heat model and its exact gap barrier {#ch-centered-heat}

Paper VII contains a complete model theorem rather than just an analogy with heat flow. It constructs a finite coefficient deformation, derives the dynamics of its roots, and proves a barrier that no adjacent logarithmic gap can cross. The later difficulty is not whether this model works. It is whether the actual coefficient residual can be transported through the model's available gap.

## The finite heat polynomial

For $d\ge2$ and $h>0$, put

$$
 P_d(z;e^{-h})=\sum_{k=0}^d\binom dk
 e^{-hk(k-1)/2}z^k.
 \tag{30.1}\label{eq:30.1}
$$

With $\theta=z\partial_z$,

$$
 P_d(z;e^{-h})=
 \exp\{-\tfrac h2(\theta^2-\theta)\}(1+z)^d.
$$

This exponential is exact on a finite-dimensional polynomial space. It does not entail an ill-posed backward-heat evolution of arbitrary functions.

The centered form is

$$
 H_{d,h}(X)=P_d(-e^{(d-1)h/2}X;e^{-h})
 =\sum_{k=0}^d(-1)^k\binom dk e^{hk(d-k)/2}X^k.
 \tag{30.2}\label{eq:30.2}
$$

Its coefficients are reciprocal up to parity, and it solves

$$
 \partial_hH=\tfrac12(d\theta-\theta^2)H.
 \tag{30.3}\label{eq:30.3}
$$

For small positive $h$, the multiple root at $X=1$ splits according to the real simple Hermite roots after the logarithmic $\sqrt h$ scaling. This supplies the initial simple positive configuration. The source gives the finite Taylor/Hermite calculation; continuation then uses the exact differential equation.

## The hyperbolic root equation

Let $X_i=e^{y_i}$ be the positive roots. Differentiating $H(X_i,h)=0$ and using

$$
 \frac{H_{XX}(X_i)}{H_X(X_i)}
 =2\sum_{j\ne i}\frac1{X_i-X_j}
$$

gives

$$
 \boxed{y_i'
 =\frac12\sum_{j\ne i}\coth\frac{y_i-y_j}{2}.}
 \tag{30.4}\label{eq:30.4}
$$

The constant part of $X_i/(X_i-X_j)$ cancels the centering term in (30.3). Thus this is the dynamics of the *centered* logarithms, not the uncentered root radii.

Suppose $\ell_i=y_{i+1}-y_i$ first touches the wall $h$. At contact all other gaps are at least $h$. If there are $L$ roots to the left and $R$ to the right of this adjacent pair, the nearest-neighbor repulsion contributes $\coth(h/2)$. The distant-root compression telescopes. For the $L$ roots on the left it is at most

$$
 \frac12\left[\coth(h/2)-\coth((L+1)h/2)\right],
$$

with the analogous right term. Hence

$$
 \ell_i'\ge\frac12\coth((L+1)h/2)
 +\frac12\coth((R+1)h/2)>1.
 \tag{30.5}\label{eq:30.5}
$$

The wall has slope one. A first contact from above would need a nonpositive derivative of $\ell_i-h$, contradicting (30.5). Nonzero endpoint coefficients prevent a root from reaching zero or infinity in finite $h$, and the gap prevents collisions. Therefore

$$
 \log\frac{\rho_{i+1}}{\rho_i}>h
 \quad\text{for all }h>0,
 \tag{30.6}\label{eq:30.6}
$$

where $-\rho_i$ are the roots of $P_d$. This is precisely the strict vertical interlacing with $P_d(e^{-h}z;e^{-h})$.

## A quantitative reserve

For a stronger wall $\lambda h$ and a bounded heat width $dh\le u_0$, the same telescoping argument gives

$$
 \ell_i'\ge\coth(\lambda u_0/4)
$$

at contact. Thus any $\lambda>1$ satisfying

$$
 \lambda<\coth(\lambda u_0/4)
$$

is protected. Let $\lambda_{u_0}>1$ be the equality solution. Then every $\lambda<\lambda_{u_0}$ gives

$$
 dh\le u_0\quad\Longrightarrow\quad\ell_i>\lambda h.
 \tag{30.7}\label{eq:30.7}
$$

At $u_0=2$, the source records $\lambda_2\approx1.5434046384$. The mathematically useful margin is the strict inequality with any smaller constant, not the rounded decimal treated as an exact root.

This finite model has what several later architectures sought: an explicit invariant region and an inward-pointing first-contact field. It succeeds because the equations close on the root configuration. The actual logarithmic-Hankel heat flow of Chapter 22 does not close at a fixed rank; it contains a fresh moment. Those are different differential systems.

## Which perturbations actually move a gap?

For

$$
 H_t(X)=\sum_{k=0}^db_ke^{tE_k}X^k,
 \qquad b_k=(-1)^k\binom dk e^{hk(d-k)/2},
$$

put $H_E=\sum E_kb_kX^k$. At a simple root,

$$
 y_i'(0)=-\frac{H_E(X_i)}{\theta H(X_i)},
 \quad
 \ell_i'(0)=-\frac{H_E(X_{i+1})}{\theta H(X_{i+1})}
 +\frac{H_E(X_i)}{\theta H(X_i)}.
 \tag{30.8}\label{eq:30.8}
$$

Constants only rescale the polynomial. Linear coefficient modes translate all log-roots. A centered quadratic changes the fitted heat parameter. These modes should be removed before measuring the remaining error.

If $E_{d-k}=-E_k$, reciprocal symmetry gives

$$
 X^dH_t(1/X)=(-1)^dH_{-t}(X),
 \qquad y_{d+1-i}(t)=-y_i(-t).
$$

For even $d$, the two central roots therefore have equal first-order velocities, so

$$
 \boxed{\ell_{
m central}'(0)=0.}
 \tag{30.9}\label{eq:30.9}
$$

Every centered odd mode, including the cubic, has this property. It is a first-order central-gap statement. It does not remove higher-order cubic effects, peripheral gaps, or a large finite deformation.

The next central smooth candidate is the projected quartic

$$
 E_k^{(4)}=\left(\frac{k-d/2}{d}\right)^4-a-b\left(\frac{k-d/2}{d}\right)^2.
$$

Its first-order central effect is $-2H_{E^{(4)}}(X_{d/2+1})/\theta H(X_{d/2+1})$. The archived positive scout values are not a uniform sign theorem. This distinction prevents the attractive cubic cancellation from becoming an unsupported actual-$\Xi$ stability claim.

**Sources:** [P7](#source-p7), exact Euler heat identities, Hermite splitting, hyperbolic root flow, barrier proofs, reciprocal perturbation identities and quartic target. [P8](#source-p8) develops the variable-curvature extension.

# 31. Saddle chambers, Airy edges, and Paper IX {#ch-paper-nine}

A quadratic heat fit is locally compelling but need not approximate an entire growing coefficient window. Papers VIII and IX introduce variable-curvature saddles and divide the parameter space into regimes. This produces some strong local asymptotics and a large computational infrastructure. It also creates a new global obligation: all regimes must join without a gap, in one normalization, with the right error scale.

## The saddle-spacing mechanism

For a model

$$
 F_d(z)=\sum_{k=0}^d\binom dk e^{d\psi(k/d)}z^k,
$$

put $z=-e^{Y/d}$ and $p=k/d$. The alternating phase is

$$
 \Phi(p)=-p\log p-(1-p)\log(1-p)+\psi(p)+i\pi p.
$$

Suppose the relevant contour is dominated by one simple conjugate saddle pair $p_0\pm i\kappa$, with no equally large competitor and a uniform steepest-descent error. Then the oscillating term has the form

$$
 A(Y)\{\cos\theta(Y)+O(d^{-1})\},
 \qquad\theta'(Y)=\kappa(Y)+O(d^{-1}).
$$

After establishing one root in each phase cell, the logarithmic root spacing satisfies

$$
 d\,g(Y)\longrightarrow\frac\pi{\kappa(Y)}.
 \tag{31.1}\label{eq:31.1}
$$

Thus $g>h=u/d$ follows in that region from $u\kappa<\pi$ with enough margin for the errors. This is a conditional saddle theorem. Dominance, contour deformation, cell endpoints, and error uniformity are part of the hypothesis, not consequences of solving the formal saddle equation.

## The early hard-window profile

The early source introduces $m=n+d/2$ and $\lambda=d/m$, hence $0<\lambda\le2$ for $n\ge0$. Its leading-model construction uses a logarithmic coefficient profile and, after removing affine terms, a phase involving

$$
 Q(p)=1+\lambda(p-1/2),\qquad
 -\lambda^{-1}Q(p)\log Q(p).
$$

Writing the saddle as $p=a+i\kappa$ gives the angle equation

$$
 \arctan\frac\kappa a+
 \arctan\frac\kappa{1-a}+
 \arctan\frac{\lambda\kappa}{1+\lambda(a-1/2)}=\pi.
$$

Its tangent identity yields

$$
 \kappa^2=\frac1\lambda+\frac12-(a-1)^2,
 \quad\lambda\kappa\le2<\pi.
 \tag{31.2}\label{eq:31.2}
$$

Within the assumed saddle regime, this gives a leading gap ratio at least $\pi/2$. The source explicitly calls the actual profile transfer and several uniform statements theorem-candidates. The moment normalization in its schematic leading-profile discussion also differs from the factorial-normalized Jensen convention. Therefore (31.2) is retained as a model computation, not used as an unconditional global estimate for actual $\gamma_n$.

This is an instructive failure mode: an excellent leading margin can coexist with an unproved transfer, especially near an edge where the relevant derivatives or coordinates become singular.

## Coalescing saddles and the Airy scale

At a simple soft edge, two saddles coalesce and the local phase has cubic normal form. The correct spatial scale is $d^{-2/3}$, not the bulk $d^{-1}$. The source's local Airy module gives, under its contour and uniform-remainder assumptions,

$$
 y_{j,d}=y_*+d^{-2/3}\frac{a_j}{c_*}+O(d^{-1}),
 \tag{31.3}\label{eq:31.3}
$$

for fixed Airy zeros $a_j$. It also matches the Airy and bulk phases in an overlap region, with separate errors of the form

$$
 O(|s|^{-3/2})+O(d^{-1/3}|s|^2).
$$

Both terms must be small simultaneously, so the overlap has two scale restrictions. One cannot choose $s$ arbitrarily large merely to reduce the first error.

The cubic here is a phase normal form. It is not the cocircuit finite difference of Chapter 26 or the centered coefficient mode of Chapter 30. Their common lesson is to remove degenerate low-order structure exactly; their operators and quantitative conclusions differ.

## The seven-region architecture

The Paper IX series attempted a no-gap cover by protected bulk, small-parameter heat, soft-edge Airy, low-slope overlap, hard-left edge, outer-edge strips, and finite Wronskian repositories. Each region needed an explicit domain, normalized coefficient map, primitive proof or verified certificate, quantitative margin, and overlap map. Historical `ACTIVE` labels recorded progress inside this design, but did not replace those data.

The historical threshold

$$
 M_*=671{,}088{,}640
$$

belongs to that earlier routing. The later v222/v426R review found that none of the seven region records simultaneously met every proof-grade contract. An exact heat-overlap ratio of $1/2$ had been used where a strict margin was required; other problems involved missing domain or dependency information. These findings do not negate every local Airy or determinant theorem. They prevent inheriting the whole infinite cover from its label.

## The later v442 frontier is a different record

The recovered v442 package contains actual interval records, not merely a filename. Its README composes a finite-height bridge from $\lambda=5.52$ to $15$, together with an asymptotic continuation and a predecessor for $\lambda\ge15$. The finite $x$ interval is

$$
 X_*=6{,}000{,}350{,}665{,}600
 \le x\le438{,}996{,}997{,}250{,}838{,}852{,}252.
$$

The recorded post-v437 rectangle count is 3,500, including the refined contact and phase-disk families. The corresponding claimed remaining region is

$$
 x\ge X_*,\qquad0<\lambda<5.52.
 \tag{31.4}\label{eq:31.4}
$$

This $\lambda$ cannot be the early $d/(n+d/2)$ coordinate, which never exceeds two. The book therefore keeps the v442 coordinate chart separate until the exact dictionary is supplied. A later threshold is not automatically comparable with the earlier $M_*$.

The package's successful interval records are preserved as historical computations with their verification scripts and parameters. This consolidation checks their identity and organization, not every long analytic prerequisite of the first-contact/Rouché framework. The manuscript's remaining low-slope range is not filled by a large-shift Jensen theorem from another normalization.

## How to use Paper IX without rebuilding its old burden

The recoverable value is substantial: raw coefficient enclosures, saddle normalization, boundary asymptotics, root-cell certificates, and the Wronskian bridge. The most efficient reuse is not necessarily restoring all seven old regions. Cofinal unshifted Jensen hyperbolicity is already a sufficient endpoint. A new model that controls that narrow family could bypass the original two-parameter cover.

The next chapter records the actual attempts to do this and their finite failures. Keeping those failures beside the successful model theorems is essential: it prevents “the model is real-rooted” from being remembered as “the actual coefficients have been transferred.”

**Sources:** [P8](#source-p8); the original and later Paper IX sources in the historical registry; [IX442](#source-ix442); [AR](#source-ar) for the cross-version audit. The full region-router and primitive-certificate records remain indexed under their original version names.

# 32. Preserving operators and the actual-coefficient transfer tests {#ch-preservers}

The late-September Jensen scouts deliberately tested candidate preservation mechanisms against the unshifted actual coefficients. Their strongest contribution is not a successful global fit. It is a combination of useful preserving families and explicit obstructions that rule out repeated investment in the wrong parameter class.

## One-sided transfer at critical points

Let $p_d$ have $d$ distinct negative roots and $d-1$ critical points $c_j$. Suppose $J_d=p_d+r_d$ has positive leading coefficient and $J_d(0)>0$. If

$$
 \frac{r_d(c_j)}{p_d(c_j)}>-1\qquad\text{for all }j,
 \tag{32.1}\label{eq:32.1}
$$

then $J_d(c_j)$ has the same alternating sign as $p_d(c_j)$. Together with the signs at negative infinity and zero, this forces one negative root in each of the $d$ intervening intervals. The degree makes these all its roots.

This permits a large residual of favorable sign. The stronger condition $|r_d(c_j)|<|p_d(c_j)|$ is unnecessary. The exact example $p=(x+1)(x+2)(x+3)$, $J=3p+1/10$ passes (32.1) although the absolute relative error exceeds one at both comparison critical points.

The difficulty is uniform control of the actual ratios, particularly at an edge where $p_d(c_j)$ is small.

## Why arbitrarily many standard Jacobi factors do not fix the fit

Normalize $R_j=\gamma_j\gamma_0^{j-1}/\gamma_1^j$ and define

$$
 q_j=\frac{R_{j+1}^2}{R_jR_{j+2}}.
$$

For products of the tested normalized Jacobi factors

$$
 R_j^{(i)}=s_i^j\frac{(a_i)_j}{a_i^j(b_i)_j},
 \qquad b_i>0,\quad a_i\ge b_i+d-1,
$$

including the corresponding Laguerre limits, the scout proves

$$
 Q_1\ge1+\frac{d-1}{d+1}(1-Q_0^{-1}).
 \tag{32.2}\label{eq:32.2}
$$

For one factor the identity is
$q_1=1+(1-q_0^{-1})a/(a+2)$; admissibility supplies the lower bound, and a product inequality preserves it under factor multiplication.

The actual coefficient enclosures give

$$
 q_0\approx1.0748439425,\qquad q_1\approx1.0627436663.
$$

Matching these values in (32.2) forces

$$
 d\le\frac{2(1-q_0^{-1})}{2-q_0^{-1}-q_1}-1<19.216371.
$$

Hence exact matching of the first three nonconstant normalized coefficients in this factor class is impossible for $d\ge20$. This is not a no-go theorem for all finite-free or Jacobi constructions. It eliminates the stated admissible product class as an unlimited exact-matching strategy.

## An Euler escape and its failure at degree eight

Start with the Laguerre model

$$
 L_d(x;C,S)=\sum_{j=0}^d\binom dj\frac{S^j}{(C)_j}x^j.
$$

For $\beta>0$, the operator $1+x\partial_x/\beta$ preserves negative real roots. At a root of a real-rooted $p$, its value is proportional to $xp'(x)$; alternating signs force the new roots between the old ones and zero. The resulting coefficients are

$$
 R_j^p=\frac{S^j(1+j/\beta)}{(C)_j}.
 \tag{32.3}\label{eq:32.3}
$$

The actual three-coefficient fit was interval-certified near

$$
 \beta=4.44551084695,\quad
 C=25.9085689570,\quad S=21.1507841164.
$$

This genuinely leaves the obstructed class. But at degree eight the source's interval calculation finds a critical point near $x=-2.579145127$ where the model is negative and the actual normalized Jensen polynomial is positive. Thus the sufficient sign-transfer test fails. The actual Jensen polynomial is not thereby shown to have a nonreal root; only this comparison has failed.

## The broader Pólya–Schur symbol

A stronger preserving coefficient multiplier is

$$
 g_j=1+(a+b)j+abj(j-1),\qquad a,b>0,
$$

with exponential generating function $e^z(1+az)(1+bz)$. Its differential operator is

$$
 T_{a,b}p=p+(a+b)xp'+abx^2p''.
 \tag{32.4}\label{eq:32.4}
$$

It is not a composition of two Euler factors: that composition has a different coefficient of $xp'$. The scout interval-certifies a four-coefficient fit to $S^jg_j/(C)_j$ near

$$
 C=35.8865931969,\quad S=25.9057862416,
 \quad a=0.26211872135,\quad b=0.12315454780.
$$

Its finite critical-point tests pass at degrees six, eight and ten, and fail numerically at twelve. Those root-ratio tests are diagnostics; the parameter fit itself has a separate interval certificate.

The natural extension is

$$
 T_{\mathbf a}p=
 \sum_{k=0}^m e_k(a_1,\ldots,a_m)x^kp^{(k)}(x),
 \qquad a_i\ge0,
 \tag{32.5}\label{eq:32.5}
$$

whose multiplier symbol is $e^z\prod(1+a_iz)$. It provides a controlled class for degree-adaptive fitting. No uniform parameter-and-transfer theorem for actual $\Xi$ has been established by these finite tests.

## A second obstruction forces the Laguerre scale to grow

Suppose a nonnegative preserving sequence $\sigma_j$, with $\sigma_0=1$, is used in

$$
 R_j^{\rm mod}=\frac{S^j\sigma_j}{(C)_j},\qquad R_1^{\rm mod}=1.
$$

Its log-concavity gives $\sigma_j\le\sigma_1^j$, hence

$$
 R_j^{\rm mod}\le\frac{C^j}{(C)_j}.
 \tag{32.6}\label{eq:32.6}
$$

The actual positive theta kernel has mass arbitrarily far out. For every fixed $U$, its even moments satisfy $I_j\ge m_UU^{2j}$ with $m_U>0$. After the factorial normalization and Stirling ratio are included, this yields

$$
 \liminf_{j\to\infty}[(C)_jR_j]^{1/j}=\infty
 \quad\text{for every fixed }C.
 \tag{32.7}\label{eq:32.7}
$$

Thus increasing multiplier complexity cannot produce arbitrarily long exact prefixes while keeping $C$ bounded. The scale itself must change, or the representation must change. The positive entire/fractional models in Chapters 20–21 are one such change: they move the problem from a root-by-root transfer to positive moment completion.

## External methods that were examined

The source scouts considered finite-free convolution, real-stability preservers, and free-probability limits. These remain methodological inputs, not assumed solutions. The recorded large-shift Jensen region does not include the unshifted boundary. An empirical limiting root distribution can ignore finitely many exceptional nonreal roots. In the Appell normalization examined in the scout, a hypothetical fixed nonreal $\Xi$ zero produces an escaping root at scale $N/\log N$, outside a fixed bulk window.

One printed general Jensen criterion was also stress-tested. An $o(1)$ logarithmic error cannot guarantee hyperbolicity when the negative quadratic coefficient tends to zero faster. The positive sequence $a(n)=1+(-1)^n/(n+2)$ satisfies that weak error description, yet its degree-two Jensen discriminant is negative for every even $n$. The exact needed scale is relative to the shrinking quadratic margin. This counterexample is to the displayed broad hypothesis, not to every specialized result of the cited paper.

**Sources:** [AR](#source-ar), [HYB](#source-hyb), [PC](#source-pc) and their exact/interval companions. Their bibliographic inputs are preserved in the source references; the present synthesis does not assume that every recent external preprint has been independently validated.


\part{Compact moments, prime activation, and the mature relay}

# 33. The self-layer-cake and Jacobi–CMV route {#ch-layercake}

The compact-moment programme predates the current rank-20 central Hankel calculation. Its purpose was to replace an unbounded spectral domain by a positive measure on a fixed interval, then express that support condition through Jacobi or canonical coordinates. The smoothing and normalization differ from those in Chapter 19, so their finite certificate sizes are not interchangeable.

## Smoothing the logarithmic moments

Use the older normalization

$$
 F_0(w)=\frac{\Xi(\sqrt{-w})}{\Xi(0)},\qquad
 \frac{F_0'(w)}{F_0(w)}=\sum_{n\ge0}(-1)^nS_{n+1}w^n.
$$

For an integer $p\ge0$ and a fixed scale $R>0$, define

$$
 m_n^{(p)}=\frac{S_{n+1}}{(n+1)^p},\qquad
 q_n^{(p)}=\frac{m_n^{(p)}}{R^n}.
 \tag{33.1}\label{eq:33.1}
$$

Under the desired negative-real-zero property, the genus-zero product has parameters $f_\nu>0$ and $S_{n+1}=\sum_\nu f_\nu^{n+1}$. Let $U_1,\ldots,U_p$ be independent uniform variables. The positive measure

$$
 \mu_p=\sum_\nu f_\nu\,
 \operatorname{Law}\!\left(\frac{f_\nu}{R}U_1\cdots U_p\right)
$$

has moments $q_n^{(p)}$ whenever $R\ge\sup f_\nu$.

The converse is also exact. If $q_n^{(p)}$ is Hausdorff, then

$$
 M_p(z)=\int_0^1\frac{d\mu(t)}{1-zt}
$$

is analytic off $[1,\infty)$. The differential operator
$\mathcal D=z\partial_z+1$ multiplies the $n$-th coefficient by $n+1$, so

$$
 \mathcal D^pM_p(-Rw)=\frac{F_0'(w)}{F_0(w)}.
 \tag{33.2}\label{eq:33.2}
$$

The right side has no off-cut pole, which excludes an off-axis zero. Thus each *fixed* smoothing order gives an exact alternative criterion. An order changing with the rank would need its own limit argument.

For $p=1$, the measure becomes particularly transparent:

$$
 d\mu_1(t)=R\,\#\{\nu:f_\nu\ge Rt\}\,dt,
$$

$$
 \log F_0(w)=w\int_0^1\frac{d\mu_1(t)}{1+Rwt}.
 \tag{33.3}\label{eq:33.3}
$$

Each reciprocal zero contributes one interval to the layer cake. The formula is not a construction of a positive measure before the sign of the reciprocal zeros is known; the independent target is positivity of the actual coefficient moments.

## Jacobi contraction and the unitary fold

A positive compact moment measure gives multiplication by $t$ on $L^2(\mu)$, a self-adjoint contraction $J$ with $0\le J\le I$. In its orthogonal-polynomial basis,

$$
 q_n=\langle e_0,J^ne_0\rangle,
$$

with the norm of the cyclic vector matching the total mass. Normalizing that mass to one produces the standard canonical moments. The ordinary, shifted and support-localizing Gram matrices express positivity of $1,t,1-t$, or the parity-specific product $t(1-t)$ on the interval.

The F22 construction folds the Jacobi interval into a unit circle representation. Its unitary/CMV structure follows *after* the contraction and support conditions are established. A unitary matrix assembled from an arbitrary proxy sequence would not prove that its moments are the actual $q_n$.

The archived finite work reports Hausdorff degree 255, Jacobi order 64, 127 canonical moments and an atomic CMV test of order 64. A September extension records all-$k$ positivity for rows $0\le n\le40$ of certain Hausdorff-difference arrays, together with additional parameter regions. An all-$k$ row theorem must not be reduced in memory to a finite sample; equally, forty-one rows are not all rows.

## Infinite-order smoothing without an artificial heat anchor

A further source considers

$$
 \Phi(z)=\prod_{j\ge1}(1+z/c_j),\qquad c_j>0,
 \qquad\sum_jc_j^{-1}<\infty,
$$

and $a_n=1/\Phi(n)$. If $X_j\sim\operatorname{Beta}(c_j,1)$ independently, then

$$
 a_n=\mathbb E\left(\prod_jX_j\right)^n.
 \tag{33.4}\label{eq:33.4}
$$

Indeed, $-\log X_j$ is exponential with mean $1/c_j$, so the sum is finite almost surely. Thus $a_n$ is itself Hausdorff. The proposed smoothed owner is $a_nS_{n+1}/R^n$.

The converse uses the zero exponential type of $\Phi$ to justify the infinite-order operator $\Phi(w\partial_w)$ on a common slit domain. The source provides the local derivative estimates needed for that operator series. This is stronger than formally writing an inverse smoothing symbol. It still leaves positivity of the resulting actual sequence unproved.

The benefit is flexibility in damping without introducing an unrelated starting function. It does not imply that enough smoothing creates the required sign: the converse is designed to prevent smoothing from concealing the off-axis obstruction.

## Why the pairwise-tail shortcut failed

The source's Gaussian complex-tail control shows that strip geometry alone cannot make every hypothetical off-line pair contribute positively at every rank. A theorem based on the aggregate arithmetic moments must therefore retain cancellation among the full set of contributions. Positivity of a dominant reference pair, or verification of finitely many ordinates, is insufficient.

This is the same distinction exposed later by the negative-heat control, but in another representation. It keeps the F21 route valuable as an independent framework while preventing the reference-model inequalities from being mistaken for a completed actual moment theorem.

**Sources:** [F21](#source-f21), [F21-NEAR](#source-f21-near), [F21-CHERNOFF](#source-f21-chernoff) and the September master addenda; [F22](#source-f22) and the original compact-Jacobi/CMV packet. Their smoothing order and scale are part of every finite certificate.

# 34. The fixed-base prime-Hausdorff criterion {#ch-fixedbase}

The actual-prime route uses a different source of finite approximations: truncate the absolutely convergent prime-power expansion at one fixed real base. This keeps each finite stage arithmetic and makes coordinatewise convergence straightforward. The challenge is proving that its depth of positive compact moments becomes unbounded.

## Fix the base once

Let

$$
 Q(y)=\frac{\xi'}{\xi}(\tfrac12+y),\qquad
 R(x)=\frac{Q(\sqrt x)}{\sqrt x},
$$

and fix $a>1/2$ with $Q(a)>0$, ultimately $a=30$. Define

$$
 G_a(z)=\frac{R(a^2(1-z))}{R(a^2)}
 =\frac{Q(a\sqrt{1-z})}{\sqrt{1-z}\,Q(a)}.
 \tag{34.1}\label{eq:34.1}
$$

The full centered $\xi$ function is even, so $R$ is a single-valued meromorphic function of $x$. Its compact transform is Hausdorff exactly when the corresponding zero geometry is real. Under RH,

$$
 \mu_n(a)=\sum_{\gamma>0}
 \frac{2m_\gamma/(a^2+\gamma^2)}{R(a^2)}
 \left(\frac{a^2}{a^2+\gamma^2}\right)^n.
 \tag{34.2}\label{eq:34.2}
$$

This exhibits the support in $(0,1)$. Conversely a Hausdorff representation makes $R$ a Stieltjes function off the appropriate cut, excluding an off-cut logarithmic-derivative pole.

The base is fixed throughout the limiting theorem. Choosing a new $a$ at each rank changes the coefficient sequence and requires an additional identification that the original criterion does not provide.

## Literal finite prime-power stages

For $s=1/2+y>1$, use the exact expansion

$$
 Q_P(y)=\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)-\sum_{2\le m\le P}\Lambda(m)m^{-s}.
 \tag{34.3}\label{eq:34.3}
$$

Let $c_n^{(P)}$ be the coefficients of
$Q_P(a\sqrt{1-z})/(a\sqrt{1-z})$ and normalize by the positive $c_0^{(P)}$ when it is available. The finite truncation need only be analytic in the chosen local chart; its global parity is not silently identified with the complete function.

For even moment order $N=2m$, the two necessary compact-interval matrices are

$$
 A_{2m}=[\mu_{i+j}]_{i,j=0}^m,
 \quad B_{2m}=[\mu_{i+j+1}-\mu_{i+j+2}]_{i,j=0}^{m-1}.
$$

For odd order $N=2m+1$, they are

$$
 A_{2m+1}=[\mu_{i+j+1}]_{i,j=0}^m,
 \quad B_{2m+1}=[\mu_{i+j}-\mu_{i+j+1}]_{i,j=0}^m.
 \tag{34.4}\label{eq:34.4}
$$

The strict depth $D(P)$ is the last order through which both parity-correct matrices remain positive definite. The source's finite certificates give $D(10^4)\ge67$, $D(10^5)\ge79$, and $D(3\cdot10^5)\ge85$ at $a=30$. These are exact finite prime-power truncations, not truncated data padded by an unknown favorable tail.

## Reverse-Bessel prime impulses

An individual prime-power activation has

$$
 u=a\log m,\qquad
 w_m=\frac{\Lambda(m)}a m^{-a-1/2},
$$

and changes the unnormalized coefficients by

$$
 \delta c_n(m)=-w_mB_n(u),\qquad
 \sum_{n\ge0}B_n(u)z^n
 =(1-z)^{-1/2}e^{u(1-\sqrt{1-z})}.
 \tag{34.5}\label{eq:34.5}
$$

In particular $B_0=1$, $B_1=(u+1)/2$, and $B_2=(u^2+3u+3)/8$. At each fixed $n$, $B_n$ is a polynomial of degree $n$ with positive coefficients. Therefore

$$
 \sum_{m\ge2}w_mB_n(a\log m)
 \ll_{a,n}\sum_{m\ge2}\Lambda(m)m^{-a-1/2}(1+\log m)^n<\infty.
$$

This proves coefficientwise convergence of the finite prime stages to the actual compact moment sequence. It does not prove that every impulse is favorable for every canonical coordinate.

## Why unbounded depth is exactly the missing statement

The finite Hausdorff cones are compact and closed. If $D(P_j)\to\infty$ along $P_j\to\infty$, then every fixed prefix converges inside its closed cone. Compactness of probability measures on $[0,1]$ yields one measure representing all limiting moments, and (34.1) gives RH.

Conversely, under RH the measure (34.2) has infinitely many distinct support points in $(0,1)$. Every nonzero polynomial has positive squared integral against each relevant localizer, so each finite limiting prefix is strictly interior. Coordinatewise convergence then makes every fixed prefix valid for all sufficiently large $P$. Consequently

$$
 \boxed{\mathrm{RH}\iff D(P)\to\infty
 \iff\limsup_{P\to\infty}D(P)=\infty.}
 \tag{34.6}\label{eq:34.6}
$$

Closedness is the final implication, not the engine producing unbounded depth. This is the older counterpart of the cofinal positive-prefix theorem in Part IV.

**Sources:** [F36](#source-f36), [F37](#source-f37), [F38](#source-f38) and F39. The finite certificate sizes, parity conventions, and literal prime cutoff are retained separately in the computation register.

# 35. Canonical walls, trace constraints, and the two-defect geometry {#ch-walls}

The first prime-Hausdorff scouts suggested a monotone staircase. The subsequent analysis found that the actual geometry is less simple: late prime impulses have opposite effects on different walls, and a harmonic-looking finite tail cannot continue indefinitely. These failures forced the mature relay to become source-specific and trace-compatible.

## The formal Wall lattice and its boundary at infinity

For $x=a^2$, the full canonical coordinates obey the source's exact lattice

$$
 x\frac{dp_n}{dx}
 =p_n(1-p_n)\{1+(n-1)p_{n-1}-(n+1)p_{n+1}\},
 \qquad p_0=0.
 \tag{35.1}\label{eq:35.1}
$$

Each finite face $p_n=0$ or $1$ is formally invariant. At every fixed index, the source also derives $p_n(x)\to1/2$ as $x\to\infty$. These facts do not determine an infinite-dimensional backward evolution: information may enter from arbitrarily large indices. The missing no-inflow/well-posedness condition is a real uniformity theorem.

The prime-face polarization result is similarly directional rather than globally favorable. If an order-$N$ prefix reaches a canonical wall, sufficiently late reverse-Bessel impulses decrease $p_N$; $u\ge3N^2$ is a universal sufficient threshold in the source. At an upper wall this is inward; at a lower wall it is outward. A capture theorem must therefore compare the new upper-wall gain with the losses of previously positive lower walls.

## The lower-Hankel quotient

Let $\mathcal A_n=\det A_n$ denote the parity-correct lower matrix and set

$$
 W_n=\prod_{j<n}p_j(1-p_j),\qquad
 \mathcal A_n=\mathcal A_{n-2}W_np_n.
$$

Dividing successive recurrences gives

$$
 \boxed{\alpha_n=(1-p_{n-1})p_n
 =\frac{\mathcal A_n\mathcal A_{n-3}}
 {\mathcal A_{n-1}\mathcal A_{n-2}}.}
 \tag{35.2}\label{eq:35.2}
$$

Thus the next renewal coefficient is precisely one more lower determinant sign, not a consequence of knowing the side of the first failed wall. The source's exact test fixes a strict prefix and $p_{N+1}=3/2$; choosing $p_{N+2}=-2$ gives $\alpha_{N+2}=1$, while choosing $p_{N+2}=2$ gives $\alpha_{N+2}=-1$. The same earlier prefix allows opposite outcomes.

## Why the harmonic tube must remain retired

The compact spectral support under the desired limiting positivity consists of

$$
 t_\gamma=\frac{a^2}{a^2+\gamma^2}.
$$

Multiplication by $t$ on the representing $L^2$ space is trace class. Its trace is the sum over distinct support points. If zero multiplicities are retained as weights, they do not create additional dimensions in this scalar cyclic space. The safe statement is therefore

$$
 \sum_j\alpha_j=\operatorname{Tr}J
 =\sum_{\gamma\,\mathrm{distinct}}t_\gamma
 \le\sum_\gamma m_\gamma t_\gamma
 =\frac a2Q(a)<\infty.
 \tag{35.3}\label{eq:35.3}
$$

This form avoids requiring simple zeros. Some historical trace displays identify the two sums without that qualification; the inequality is sufficient for the obstruction.

If a two-sided harmonic tube imposed $p_j\ge c/j$ while its upper bound kept $p_{j-1}$ away from one, then $\alpha_j=(1-p_{j-1})p_j\gtrsim1/j$, contradicting (35.3). Hence a finite window with $jp_j$ approximately constant cannot be promoted to an unbounded invariant tube.

The replacement mature scale is summable, of order $\log^2j/j^2$ in the programme. It is compatible with the trace obstruction; compatibility alone does not prove that the actual trajectory occupies it.

## The exceptional pair and resonance

The F43 architecture focuses on two neighboring invalid coordinates

$$
 x=p_{N+1}>1,\quad y=p_{N+2}<0,\quad
 B=(1-x)y>0,
$$

with the following coordinate $z=p_{N+3}$ small. At a saddle parameter $0<t<1$, define

$$
 A=\frac{(1+t)^2}{4t},\qquad
 M=A-1=\frac{(1-t)^2}{4t},\qquad A-M=1.
 \tag{35.4}\label{eq:35.4}
$$

The resonance condition is $B=A-x$. The two defects are not independent errors: their product and the adjacent transfer matrix create an exact Szegő factorization. This is the geometric mechanism behind recruitment of a new valid prefix.

A source-independent whole-cube inward theorem was falsified. The retained programme instead controls a protected prefix, a specific exceptional pair, and the later capture. This distinction is essential when reusing the exact two-defect algebra: it is not a universal stability theorem for every point of a canonical cube.

**Sources:** [F36](#source-f36), [F39](#source-f39)–[F43](#source-f43) and the definitive August master. Equation (35.3) uses the multiplicity-safe trace form; its finite-trace consequence is the one needed by the source's harmonic-tube obstruction.

# 36. Exact mature transport and the corrected off-resonance chart {#ch-mature}

The August relay accumulated many local results. Their logical order matters more than their count. The principal advance was replacing singular heuristic coordinates by an exact physical normalization, then separating the saddle-response theorem from the hypotheses needed to regenerate it at the next stage.

## The width is $x-1$, not the resonance proxy

Let

$$
 e=x+B-A,\qquad\Delta=M-B.
$$

Since $A-M=1$,

$$
 x=1+\Delta+e,\qquad\omega=x-1=\Delta+e.
 \tag{36.1}\label{eq:36.1}
$$

The exact neighboring quantities are

$$
 y=-B/\omega,\qquad1-y=(M+e)/\omega,
 \qquad C=(1-y)z=(M+e)z/\omega.
$$

A formula replacing $\omega$ by $\Delta$ is exact only on resonance. The earlier broad safe cone permitted $e$ much larger than the selected deep width, so the replacement was not harmless.

Let

$$
 H=(\Phi_N+\Phi_N^*)/2,\qquad
 E=(\Phi_N-\Phi_N^*)/2,\qquad\varepsilon=E/H,
$$

and keep the original raw endpoint difference $D=r\Phi_{N+2}-\Phi_{N+2}^*$. The correct desingularized quantity is $\mathscr D=\omega D$. Exact transfer multiplication gives

$$
 \frac{\mathscr D}{H}=F_H(r)+F_E(r)\varepsilon(r),
 \tag{36.2}\label{eq:36.2}
$$

$$
\begin{aligned}
F_H(r)&=(r-1)[\omega(1+r)^2-4r(1+\omega)(\omega+B)],\\
F_E(r)&=(r+1)[\omega(r-1)^2-4r(1+\omega)B].
\end{aligned}
$$

At $r=t$, the source obtains

$$
 F_H(t)=4t(1-t)[B+e\omega],\quad
 F_E(t)=-4t(1+t)[B-\Delta\omega].
 \tag{36.3}\label{eq:36.3}
$$

These identities locate exactly where the off-resonance terms enter. They supersede only the invalid broad normalization, not the original on-resonance factorization.

## An exact resonance-defect integral

The retained differential relation reduces to

$$
 e_x=-\frac{Ae}{x(A-x)}.
$$

Hence

$$
 \boxed{\frac{ex}{A-x}=\text{constant on the frozen stage}.}
 \tag{36.4}\label{eq:36.4}
$$

The corrected transported coordinate is

$$
 Y^\sharp=\frac{Mx}{x-1}z.
 \tag{36.5}\label{eq:36.5}
$$

This is the appropriate quantity for the thin-core transport; replacing its denominator by a resonance width without an error estimate returns to the old defect.

The source's actual-prime endpoint approximation uses a mesh increasingly fine in the switching coordinate. It removes the need for an exact prime to hit a codimension-one continuous crossing. The proof must still establish a continuous crossing, the response bounds there, and that the chosen actual endpoint is close enough in the correct coordinate.

## Saddle desingularization and the BR estimate

The F161 mechanism is an exact integration by parts

$$
 \mathcal I_N[qf]=-\frac{1}{N}\mathcal I_N[\mathcal Lf],
 \tag{36.6}\label{eq:36.6}
$$

which removes the leading saddle-zero factor before estimating the amplitude. The later BR theorem is therefore not derived by dividing two independently small approximate terms. Under the explicit mature amplitude and transport hypotheses, F163 yields $J_{\rm actual}>6/5$, and F164 gives a safe-cone sign.

F165 narrows the selected crossing to $4<d_*<10$. The constants are conclusions of the stated local regime. They do not prove that every subsequent actual-prime stage enters the same regime.

## PREFIX-51 and the concrete constants

The F166.11–18 chain treats low-branch packets, RESET amplitude, endpoint-Darboux transport, prefix retention, and the resulting qd margin. The source records explicit constants including $C_W=6915$, a retained PREFIX-51 factor exceeding $0.999987558$, an excursion factor exceeding $0.99999375$, and a margin target $3/5$. These belong to the particular hypotheses and thresholds of that chain; they are not free reserves available in an unrelated metric.

Its activation residual is

$$
 \mathcal E_N=\frac{59}{60}c_N-2\log N+\log\log N,
 \qquad c_N=u_N/N.
 \tag{36.7}\label{eq:36.7}
$$

For $N\ge10^{12}$, the displayed hypothesis $|\mathcal E_N|\le24$ implies the coarse activation band

$$
 \log N<c_N<4\log N.
 \tag{36.8}\label{eq:36.8}
$$

This numerical implication is elementary once (36.7) is controlled. The unresolved arithmetic question is the uniform control of that residual along the actual sequence.

The old local transport, PREFIX, retention and margin implications remain reusable. What cannot be inferred is their all-cycle activation from a successful first entrance. The following chapter explains the more precise later RESET developments.

**Sources:** [F161](#source-f161)–[F164](#source-f164) as retained in the August master; [F165-NORM](#source-f165-norm) and its thin-core certificates; [F166.11](#source-f166-11)–18. The source dates and later corrections are tracked at the module level rather than treating all of “F166” as a single theorem.

# 37. Endpoint Christoffel transport and the later RESET sequence {#ch-reset-index}

The later F166 files resolved several apparent normalization mysteries. Their value is lost when they are compressed into “the reset is still open.” Some maps are now exact; the unresolved part is quantitative retention and actual next-stage identification. The distinction is especially sharp between a fixed section, the forced wall, and the later entrance.

## The endpoint transform and its seed

For a normalized functional $\mu$, put

$$
 c=\mu(1-X)>0,\qquad
 \nu(g)=\frac{\mu((1-X)g)}c.
 \tag{37.1}\label{eq:37.1}
$$

The endpoint-$1$ Christoffel transform changes the Stieltjes coefficients from

$$
 \alpha_n^\mu=(1-p_{n-1})p_n
$$

to

$$
 \alpha_n^\nu=p_n(1-p_{n+1}).
 \tag{37.2}\label{eq:37.2}
$$

Canonical coordinates of the transformed functional still depend on the incoming seed. They are not obtained by merely shifting the index of the old $p_n$.

For local numerators $a=x(1-y)$, $b=y(1-z)$ and $d=z(1-w)$, with incoming seed $s$, the recursion

$$
 u=\frac a{1-s},\qquad v=\frac b{1-u},\qquad r=\frac d{1-v}
$$

gives the exact fractional map

$$
 r(s)=d\frac{1-s-a}{(1-s)(1-b)-a},\qquad
 r'(s)=\frac{abd}{[(1-s)(1-b)-a]^2}.
 \tag{37.3}\label{eq:37.3}
$$

This makes the seed sensitivity visible. A large derivative near a small denominator cannot be ignored because the output itself is small.

## Equilibrium residue and physical residue are different

One earlier shortcut identified an equilibrium residue with the actual Stieltjes residue. F166.5 replaces that identification by an explicit barrier comparison. The physical Darboux step is an $LU\to UL$ factorization with its own normalization. It is not the informal exchange of two canonical labels.

Subsequent files treat switch-then-strip order, two-parity defect deletion, normalized unit-block sources, moderate-band Borel response, and edge trapping. In particular, the Borel endpoint response has an exact finite product representation of the form

$$
 H_P(t)=\prod_i(1-\rho_i/t).
 \tag{37.4}\label{eq:37.4}
$$

In an integer extremal case it is represented by a normalized associated Laguerre polynomial; the fractional case uses a two-Laguerre pencil. This gives exact response geometry, but the polynomial's argument and the actual prime-activation coordinate must stay synchronized.

The historical elementary local matching closure in F166.44 was later reopened. It must not be treated as an all-cycle theorem merely because the original file contains closure language. The source register keeps the intervening F166.48, .52C, .54–.64 refinements and their dependencies.

## The same-index determinant map

F166.78 gives a useful exact fixed-section identity. At even rank $2m$, replace the monomial basis by

$$
 1,\quad1-X,\quad X(1-X),\ldots,X^{m-1}(1-X).
$$

The basis change is triangular with determinant of magnitude one. The lower Gram becomes

$$
 \begin{pmatrix}1&cv^T\\cv&cB_{2m-1}(\nu)\end{pmatrix},
 \qquad v=(\nu_0,\ldots,\nu_{m-1})^T.
$$

Thus

$$
 \mathcal A_{2m}(\mu)
 =c^m\mathcal B_{2m-1}(\nu)
 [1-cv^TB_{2m-1}(\nu)^{-1}v].
 \tag{37.5}\label{eq:37.5}
$$

The odd version has the corresponding shifted moment vector and leading scalar $1-c$. The inverse-RESET ambiguity at a fixed section is one Schur boundary scalar, not an unknown high-dimensional normalization.

Moreover,

$$
 \boxed{\alpha_n^\mu=
 \alpha_n^\nu\frac{1-p_{n-1}}{1-p_{n+1}}.}
 \tag{37.6}\label{eq:37.6}
$$

If both neighbors lie in $[0,q]$, $q<1$, this ratio lies in $[1-q,(1-q)^{-1}]$. In particular it is near one for a small ordinary tail. The large apparent amplification arose from comparing different absolute indices, not from (37.6) itself.

## What F166.85A actually settles

The recovered September 3 source resolves the pure index/rank question at the forced wall. In its notation, with regular wall parameters $\delta,\varepsilon,\zeta$, the stripped canonical sequence begins

$$
 P_1=\delta,\qquad P_2=\frac\varepsilon{1-\delta}.
$$

Consequently the stripped Stieltjes slots are $\delta,\varepsilon,\zeta,\ldots$, and the absolute index rule is

$$
 \boxed{
 \alpha^{\rm strip}_{N+4+t}
 =\lim_{r\to1^-}\widetilde\alpha^{\rm pre}_{N+6+t},
 \qquad t\ge0.}
 \tag{37.7}\label{eq:37.7}
$$

One physical Jacobi level contains two alternating Stieltjes slots; stripping that level explains the shift by two. Thus the correct regular candidate is the pre-strip $N+6$ quantity, not an adjacent older slot.

This is a real improvement over the earlier F166.78 state, and it must not be forgotten. It does not prove $\delta>0$, the bound $\delta=O(K/N^2)$ at the wall, or retention of that scale until the next entrance. The source explicitly isolates the subsequent target:

$$
 \delta_{\rm selected}=O(K/N^2)
 \Longrightarrow\delta_{\rm wall}=O(K/N^2)
$$

under the actual short-flight dynamics, followed by the same-section inverse map. A fixed-wall indexing theorem does not itself perform a moving-window estimate.

## The old tiny deposit is not the naive associated coordinate

At exact resonance, $x=1+\Delta$, $B=M-\Delta$, and $y=-(M-\Delta)/\Delta$. The sum of the two transformed local coefficients is

$$
 x(1-y)+y(1-z)=A+Bz/\Delta\ge A
$$

for $z\ge0$. The earlier wall quantity

$$
 p_{\rm dep}=\frac{A\Delta}{M^2+\Delta}
$$

is instead of the small selected scale. They cannot be the same coordinate. Rejecting that naive identification does not invalidate the old wall formula; it identifies a missing chart map.

**Sources:** [F166.3](#source-f166-3), .5, .19–.64, [F166.78](#source-f166-78), [F166.85A](#source-f166-85a) and F167. The standalone .78 and .85A texts were recovered in addition to their cumulative-master appearances. The forced-wall index result supersedes the earlier statement that the pure index shift was still unknown; the quantitative flight remains distinct.

# 38. Cube-only protection, amplitude control, and the remaining invariant {#ch-relay-continuation}

Two later deductions reduce the number of hypotheses that a mature relay must carry. They do not complete the relay, but they prevent the programme from repeatedly demanding stronger estimates than necessary.

## A relative light cone from the cube alone

For an older protected coordinate, the source response estimate is

$$
 \left|\frac{d\log p_j}{dx}\right|
 \le R\frac{2(j+1)}u
 \prod_{r=j+1}^N
 \left[\frac{2(r+1)}u p_r(1-p_r)\right],
 \tag{38.1}\label{eq:38.1}
$$

where $R$ is the bounded front-response ratio. While the prefix remains in the canonical cube,
$p_r(1-p_r)\le1/4$. Thus, with $\lambda_N=(N+1)/(2u)$,

$$
 \left|\frac{d\log p_{N-d}}{dx}\right|
 \le R\frac{2(N+1)}u\lambda_N^d.
 \tag{38.2}\label{eq:38.2}
$$

The response decays geometrically with distance from the active front. No pointwise harmonic upper tube is needed. This is valuable because the harmonic lower tube was already ruled out by the trace constraint.

The proof is a direct product estimate, conditional on the underlying response identity and the protected-prefix hypothesis. It does not prove that the active front is captured before any protected coordinate reaches its lower wall. For that, the integrated displacement and the available initial margins must still be compared.

## A summable tail makes the amplitude hypothesis eventual

The F43 product recurrence has

$$
 H_j(r)=(1-p_j)(1+r)H_{j-1}(r)(1+\delta_j(r)).
$$

On $|r|\le1/3$, the retained estimates give, for $q_j=p_j/(1-p_j)$,

$$
 |\delta_j|\le4q_j,\qquad|\delta_j'|\le45q_j.
$$

If $q_j\le1/8$, then

$$
 |(\log(1+\delta_j))'|\le90q_j.
$$

Factor the universal powers and scalar terms out of $H_N$ and call the remaining amplitude $A_N$. For a nonvanishing finite head $A_J$, let

$$
 L_{\rm head}=\sup_{|r|\le1/3}|A_J'/A_J|,
 \qquad\tau_J=\sum_{j\ge J}q_j.
$$

Logarithmic differentiation gives

$$
 \sup|A_N'/A_N|\le L_{\rm head}+90\tau_J,
 \quad\sup|G_N'/G_N|\le2L_{\rm head}+180\tau_J
 \tag{38.3}\label{eq:38.3}
$$

when $G_N=A_N^2$. The summable-tail product condition also supplies nonvanishing.

If the activation lower band gives $c_N=u_N/N\ge\log N$, the saddle

$$
 t_N=\sqrt{1+c_N^2}-c_N
 =\frac1{\sqrt{1+c_N^2}+c_N}
$$

satisfies $t_N\le1/(2\log N)$. Hence

$$
 t_N\sup|G_N'/G_N|
 \le\frac{L_{\rm head}+90\tau_J}{\log N}.
 \tag{38.4}\label{eq:38.4}
$$

The usual $1/2$ amplitude condition is therefore automatic once
$\log N\ge2L_{\rm head}+180\tau_J$. It is not a separate all-cycle contraction theorem.

## The invariant that is still needed

The mature relay must actually regenerate a positive small canonical tail, retain a nonvanishing finite head, establish the activation band, and synchronize the selected coefficient with the next entrance. The finite seam must reach the region where these estimates apply. The exact forced-wall shift in (37.7) and the eventual amplitude implication (38.4) remove two auxiliary burdens; they do not supply the remaining sign and scale.

This gives a disciplined restart point for the older route. It should not restart the disproved whole-cube monotonicity, the harmonic lower tube, the naive deposit map, or an equilibrium-to-actual identification. It should ask which quantitative source estimate establishes the actual small regular pivot throughout the short flight.

## Fractional activation as a diagnostic, not a substitute trajectory

The archive also considered choosing fractions of prime impulses. For a reachable zonotope

$$
 \mathcal Z=\{h-\sum_i\theta_id_i:0\le\theta_i\le1\}
$$

and the truncated Hausdorff cone, finite-dimensional separation gives the exact dual test

$$
 \mathcal Z\cap\mathcal C_N\ne\varnothing
 \iff
 \mathcal L_h(f)+\sum_iw_i[-\ell_{u_i}(f)]_+\ge0
$$

for every polynomial $f\ge0$ on $[0,1]$ of the allowed degree, with the source's impulse normalization. This can determine whether a proposed finite seam has enough directional freedom.

A favorable fractional path is not the actual arithmetic path. Recovering the literal prime endpoint is an additional task. The archived scouts did not establish that fractional control outperformed full natural activation, and some apparent high-rank successes were numerical conditioning artifacts. The dual theorem remains a useful finite tool even though the original global route was deprioritized.

**Sources:** [F167](#source-f167), [F168](#source-f168), the [F156](#source-f156) relative-response theorem, and the fractional-prime control records. These conditional reductions are retained because they reduce auxiliary demands without claiming the missing actual invariant.


\part{Finite sections, innovation, and spectral alternatives}

# 39. Native finite sections: what the mesh really certifies {#ch-native}

## The Toeplitz-minus-Hankel core

The native finite-section programme approximates an odd physical profile by step functions on a logarithmic mesh. Its matrix is not an arbitrary Toeplitz covariance. Odd reflection creates the Hankel subtraction. At mesh width $D$ and positive-half length $h$, the raw matrix and its pole completion are

$$
 T_{D,h}=(c_{|i-j|}-c_{i+j+1})_{i,j=0}^{h-1},
 \qquad Q_{D,h}=T_{D,h}-t_{D,h}t_{D,h}^{*}.
 \tag{39.1}\label{eq:39.1}
$$

The lag coefficients include the Archimedean integrals and every visible prime power, with interpolation determined by the actual mesh. The vector $t_{D,h}$ is the physical pole functional in that basis. A different normalization of the step basis changes both the matrix and pole vector; it cannot be applied to one alone.

When $T=T_{D,h}\succ0$, positivity of $Q$ is equivalent to the scalar condition

$$
 \epsilon_{D,h}=1-t^{*}T^{-1}t>0.
 \tag{39.2}\label{eq:39.2}
$$

Indeed $Q=T^{1/2}(I-vv^{*})T^{1/2}$ with $v=T^{-1/2}t$. Its only potentially nonpositive direction is the distinguished Riesz direction. This is the precise setting in which a large matrix can reduce to one soft scalar: the raw core must already be positive. A negative raw mode cannot be removed merely by naming a soft state.

## A terminal matrix contains all earlier prefixes

The September 12 record contains a particularly useful finite theorem. At a fixed mesh, build the augmented terminal matrix

$$
 \mathcal M_H=\begin{pmatrix}T_{D,H}&t_{D,H}\\t_{D,H}^{*}&1\end{pmatrix}.
$$

The faithful matrix for $h\le H$ is its principal submatrix on indices $0,\ldots,h-1$ together with the final pole index. A source at lattice lag greater than $2h-1$ cannot enter that prefix: neither $|i-j|$ nor $i+j+1$ reaches its support. Thus

$$
 \mathcal M_H\succ0
 \quad\Longrightarrow\quad
 Q_{D,h}\succ0\quad(1\le h\le H).
 \tag{39.3}\label{eq:39.3}
$$

This genuinely removes the need to certify each earlier source admission separately. It does not remove the need to refine the mesh or control the continuum complement.

The recorded terminal choice is $D=\log2/2048$, $H=6144$, and aperture $HD=3\log2$. It includes the 26 prime-power sources from 2 through 61. Source 64 is not yet active: its lattice position is 12288, one beyond the largest Hankel lag. The retained preconditioned interval budget is

$$
 \|R\mathcal M_H^{\mathrm{exact}}R^{*}-I\|_\infty
 \le0.74042452559637051<1.
 \tag{39.4}\label{eq:39.4}
$$

This number combines lag and pole entry enclosures, the transported exact-input error, floating-point matrix-product allowance, and an extra cushion. The archive retains the inputs and receipt. Equation (39.4) is a historical certificate, not an execution repeated while writing this chapter.

## First visibility is not a permanent positive resource

At the first visibility of source $4=2^2$, the isolated source update has two off-diagonal entries equal to $\log2/2$ and eigenvalues $\pm\log2/2$. Source 5 enters a different parity chamber and initially contributes a positive rank-one diagonal update. Consequently a universal induction based on positive first contact is false even in the native builder.

The terminal certificate avoids this problem by estimating the full accumulated matrix. It permits an indefinite source increment whose interaction with the existing matrix remains harmless. This is a finite analogue of the distinction, in the physical chapters, between a locally signed contribution and the sign of the complete form.

## Source71 and the continuum distinction

The later Source71 work sharpened finite entry and residual budgets after a hostile audit. The consolidated repair records a coarse congruence factor above $0.9933$ and a first finite RESET Schur floor above $1.2382$, yielding a finite refined-space lower bound above $3\times10^{-16}$ under its stated multiplication and input model. It also constructs a continuum test with absolute Rayleigh quotient below $5\times10^{-124}$.

These statements concern different trial spaces. The tiny continuum value neither contradicts the finite positive bound nor proves that the continuum gap is exactly zero. Its sign is not determined by an absolute upper bound. The correct lesson is that a mesh can miss an extremely soft direction.

Several historical summaries called an almost-zero computed continuum eigenvalue a zero-gap theorem. The later repair retracts that promotion. The book retains the small-test construction, the corrected finite bound, and the distinction between them.

## W200 as a local theorem

W200 supplies a separate fixed-window result, recorded in its digest as

$$
 Q_W(f)\ge2^{-151}\|f\|_2^2,
 \qquad f\in C_c^\infty((-1,1)).
 \tag{39.5}\label{eq:39.5}
$$

Its proof-bearing numerical premises, normalization, and original certificate package belong to the W200 source family. Later margin variants must be read in their own normalization; the label W200 alone does not identify a particular constant. It is an imported local engine, not an attribution of the rest of this programme to that artifact.

The attempted direct patch from W200 to the Desogus induction failed in exact small collar examples at the recorded $k=7,8$ stages. The failure concerns the proposed augmented inequality, not the local theorem (39.5). The valid continuation principle remains the shifted-cofinal endpoint of Chapter 3, but no fixed-window statement supplies its expanding sequence automatically.

**Sources:** [NATIVE6144](#source-native6144), [RESET12](#source-reset12), [AUDIT19](#source-audit19), [W200-DIGEST](#source-w200-digest), [W200-CORPUS](#source-w200-corpus), and the Desogus/collar audit records. The source register identifies the particular files; historical numerical receipts are not amalgamated across normalizations.

# 40. RESET, Riccati energy, and the distinguished source {#ch-reset-energy}

## The fine/coarse identity

The dyadic Haar split makes the energy-balance mechanism particularly transparent. At fixed physical aperture,

$$
 V_{D/2}=V_D\oplus W_D,
 \qquad
 T_{D/2}\sim\begin{pmatrix}T_D&B_D\\B_D^{*}&F_D\end{pmatrix}.
$$

Write $u_D=T_D^{-1}t_D$, and define

$$
 S_D=F_D-B_D^{*}T_D^{-1}B_D,
 \qquad r_D=t_{\mathrm{detail}}-B_D^{*}u_D.
$$

The block-inverse identity of Chapter 7 gives

$$
 \epsilon_{D/2}=\epsilon_D-r_D^{*}S_D^{-1}r_D,
 \qquad
 S_{Q,D}=S_D-\frac{r_Dr_D^{*}}{\epsilon_D}.
 \tag{40.1}\label{eq:40.1}
$$

These two formulas express the same event in raw and completed coordinates. The first measures the loss of pole reserve; the second is the actual completed detail denominator. A bound for $F_D$ alone is insufficient because $S_D$ already includes the coarse screen.

For a more general evolving budget $B$, the identical algebra reads

$$
 \delta_{\mathrm{fine}}
 =\delta_{\mathrm{coarse}}+\Delta B-r^{*}S^{-1}r.
 \tag{40.2}\label{eq:40.2}
$$

If $S=L\operatorname{diag}(h_j)L^{*}$ and $z=L^{-1}r$, then the debt is exactly $\sum_j|z_j|^2/h_j$. The appearance of this equation in both the old RESET programme and the newer source-funding work is a genuine algebraic connection. Identification of their arithmetic $r,S,B$ is a separate matter.

## A useful local summability theorem

Suppose, for a frozen aperture and finite arithmetic source set, that all sufficiently fine dyadic meshes satisfy

$$
 S_D\succeq c\log(1/D)I,
 \qquad \|r_D\|^2\le C D^2\log(1/D).
 \tag{40.3}\label{eq:40.3}
$$

Then the debt at scale $D$ is at most $(C/c)D^2$. Along $D_j=D_J2^{-j}$,

$$
 \sum_{j\ge0}r_{D_j}^{*}S_{D_j}^{-1}r_{D_j}
 \le\frac{4C}{3c}D_J^2.
 \tag{40.4}\label{eq:40.4}
$$

The geometric sum is the complete proof of this conditional local theorem. It tolerates constants depending on the frozen source set. A subsequent diagonal cofinal construction must choose its refinement depth after those constants are known and retain the source-admission errors.

The recorded first refinement at aperture $3\log2$ has soft scalar $8.0838\times10^{-8}$, debt $5.5182\times10^{-8}$, and retained fraction about $0.31738$. The next numerical refinement retains about $0.250387$. These are useful indications of a dyadic scale, not an induction theorem. The source explicitly distinguishes interval-enclosed fine matrix entries from an interval-certified complete inverse computation.

## Why the residual, not a raw cross norm, matters

The exact low/detail multiplier contains

$$
 b(\phi)=-\frac i2\sin(\phi/2)
 [\sigma(\phi/2)-\sigma(\phi/2+\pi)],
 \qquad b(0)=0.
 \tag{40.5}\label{eq:40.5}
$$

The proposed smallness comes from the forced Riesz state meeting that zero, and from cancellation of the common logarithmic term in the bracket. A global norm estimate for the coupling discards this information. The three frequency regimes in the original plan were low-frequency tangency, intermediate-frequency common-part cancellation, and high-frequency detail coercivity.

None of those observations proves the first inequality in (40.3). The complete screened detail form, not the uneliminated detail compression, must have the stated floor.

## A trial image and its exact transverse defect

For $Q=T-tt^{*}$ with $T\succ0$, take a trial vector $p$ satisfying $t^{*}p=1$, and put

$$
 p_* =\frac{T^{-1}t}{t^{*}T^{-1}t},
 \qquad \epsilon=1-t^{*}T^{-1}t.
$$

The difference $w=p-p_*$ is $T$-orthogonal to $p_*$. Therefore

$$
 \frac{\epsilon}{1-\epsilon}
 =Q(p,p)-\|p-p_*\|_T^2,
 \tag{40.6}\label{eq:40.6}
$$

and

$$
 \|p-p_*\|_T^2
 =\sup_{t^{*}x=0,\,x\ne0}
 \frac{|Q(p,x)|^2}{x^{*}Tx}.
 \tag{40.7}\label{eq:40.7}
$$

A small self-energy is only one term of (40.6). A small mixed transverse defect is the additional information needed to compare the explicit image with the actual forced state. This explains the failed fixed-mesh crossover: the cell representation of a smooth Xi image can stabilize at a nonzero discretization defect while the physical soft scalar continues to shrink.

The moving-corridor source uses $\alpha_D=\tfrac12\log\log(1/D)+C_0$. Its periodized Xi tail can then beat any prescribed algebraic mesh loss after fixing $C_0$ large enough. The independent cell error is still of size $C_SD/\sqrt{\gamma_D}$ in the dual energy estimate. Thus the necessary budget contains

$$
 \frac{C_S^2D^2}{\gamma_D}
 +\frac{\alpha_De^{23\alpha_D}e^{-2\pi e^{2\alpha_D}}}{\gamma_D}.
 \tag{40.8}\label{eq:40.8}
$$

Only the second term is freely improved by the offset. A transverse-gap or direct dual estimate remains required for the first. The source's bilinear Xi-tail assertion is used with its stated radical identity and admissible test class, not as an unconditional positivity theorem for every translated source.

## Pole compression and the three-port edge

In the older terminating-edge coordinates, the pole read is

$$
 \operatorname{PoleRead}
 =16\bigl(\cosh(D/2)-1\bigr)(C^2-S^2),
$$

where $C=\sum_jx_j\cosh(jD/2)$ and $S=\sum_jx_j\sinh(jD/2)$. Thus the real pole sector is one positive rank-one contribution minus one negative rank-one contribution. The geometric modes are $e^{D/2}$ and $e^{-D/2}$.

Two pole modes and one border-completion port explain the natural $3\times3$ Redheffer edge. They do not imply that the complete arithmetic remainder has rank three. The practical use is to keep the small explicit edge separate from the regular complement and its source-dependent debt. The projected Green/Jost target at $E_D=2\cosh(D/2)$ and the Christoffel prediction-error target $\epsilon_D\asymp D^2L(D)$ were attempts to control that special forcing. The latter would explain a refinement ratio tending to $1/4$, but it remained an asymptotic target for the actual singular arithmetic symbol.

**Sources:** [RESET12](#source-reset12), [MOVING-MEL](#source-moving-mel), the September 9 RESET/Redheffer master, and the Source71 repair family. Equations (40.1), (40.2), and (40.6) share block algebra; their source hypotheses are not interchangeable.

# 41. Weyl functions, canonical systems, and positive realizations {#ch-spectral}

## What a positive realization would accomplish

The earliest Herglotz–Pick investigations and later Suzuki/Livšic work seek a realization of a Xi-derived analytic function as the resolvent, Weyl function, or transfer function of a positive or self-adjoint system. Such a realization would encode zero geometry structurally rather than certify each finite polynomial.

For a self-adjoint operator $J$ and vector $e$, a resolvent expression

$$
 m(z)=\langle e,(J-zI)^{-1}e\rangle
$$

has a spectral integral with a positive measure. Conversely, a positive measure gives a multiplication-operator realization. This familiar correspondence explains why the moment, Hankel, and Weyl approaches repeatedly meet. The crucial Xi-specific statement is the positivity of the representing measure or Hamiltonian. Defining a candidate analytic function does not establish that property.

The actual coefficient resolvent of Chapter 20 is useful because it uses literal moment matrices and a declared source. At finite size it has an exact sign identity. Extending the construction to unbounded size is precisely the positivity obligation of Chapter 19, not a consequence of the word *resolvent*.

## Finite Livšic functions and the limiting question

The recovered Suzuki branch constructs finite operators, finite Livšic functions, a structural spectral shift, and bridges toward Donoghue and Stieltjes coordinates. The finite Schur/scattering algebra remains useful. The difficult transition is from those finite functions to a global function identified with the actual Xi object, including domains, normalization, and local uniform convergence.

There are two different ways that this transition can fail. The functions may converge to the wrong analytic object because their normalization changes with the aperture. Or the candidate limit may be correctly identified but the positivity or nonvanishing property may not survive without the required topology and control at the boundary. The direct approximation theorems in Chapters 3 and 20 are examples of how such a limit must be proved, rather than inferred from visual agreement.

The September 23 revision of the Suzuki work appears in the programme as an external framework with a conjectural global limiting statement. The book preserves that source's role without using its conjectural part as a completed premise.

## Cauer factorization and discrete supersymmetry

For positive Stieltjes continued-fraction coefficients $\alpha_j$, a bidiagonal operator $D_C$ yields the paired Jacobi operators

$$
 J_+=D_CD_C^{*},\qquad J_-=D_C^{*}D_C.
 \tag{41.1}\label{eq:41.1}
$$

In the archive's indexing, the corresponding Jacobi entries include

$$
 d_0=\alpha_1,\qquad
 d_n=\alpha_{2n}+\alpha_{2n+1},\qquad
 e_n=\sqrt{\alpha_{2n-1}\alpha_{2n}}.
 \tag{41.2}\label{eq:41.2}
$$

The factorization proves positivity once the $\alpha_j$ are positive. It is also the discrete Miura correspondence between Volterra/Kac–van Moerbeke variables and Toda/Jacobi variables. This is a valuable bridge between continued fractions and integrable dynamics.

For the programme, the unresolved statement is that the coefficients generated by the actual Xi function remain in that positive class. A flow that preserves positivity of arbitrary positive initial data does not solve the initialization or exact-identification problem. A finite Darboux step must also retain the physical LU-to-UL normalization from Chapter 37.

## Negative squares are a bookkeeping alternative

The generalized-Schur/Pontryagin route allows an indefinite system and records its negative index rather than demanding immediate positivity. At a finite aperture one can set

$$
 \kappa_a=\operatorname{ind}_{-}A_a.
$$

A related finite expression in the archive is $\operatorname{ind}_{-}(R_k^{\dagger}-I/2)$, under that branch's matrix dictionary. A valid Kreĭn–Langer correspondence could translate negative squares into scalar pivot failures. It would help locate and propagate the dangerous sector.

What is missing is an exact dictionary for the complete arithmetic operator, followed by a bound excluding the relevant negative sector on the expanding sequence. A representation that faithfully counts negative directions is useful even when it does not prove their absence. The finite-index route should not be summarized as having already supplied a positive Hamiltonian.

## Why this family remains a reserve

These constructions have strong structural reach: self-adjointness, a positive Hamiltonian, or a unitary CMV model can impose the desired analytic geometry automatically. They also concentrate the arithmetic burden into their realization theorem. The archive contains substantial finite and conditional pieces, but no recovered argument constructs the complete required positive Xi realization. Their best current role is to suggest explicit factors, boundary maps, and canonical coordinates for the primary routes.

**Sources:** [ATLAS](#source-atlas), the September 9–10 cumulative spectral handovers, [F21](#source-f21)/[F22](#source-f22), and the finite Suzuki/Livšic records. External canonical-system and operator-theory results retain their own hypotheses; the all-rank arithmetic realization remains separate.

# 42. Orthogonal folds, Hardy norms, and cutoff-free arithmetic {#ch-folds}

## Bernstein energy and its Laguerre realization

The F18/F19 programme converts a folded spectral functional into scalar orthogonal coefficients. Let $\beta_{N,k}$ be its Bernstein row and define

$$
 W_N(\zeta)=\sum_{k=0}^{N}\beta_{N,k}\zeta^k.
$$

Parseval gives

$$
 \mathcal E_N=\frac1{2\pi}\int_0^{2\pi}|W_N(e^{i\theta})|^2d\theta
 =\sum_{k=0}^{N}|\beta_{N,k}|^2.
 \tag{42.1}\label{eq:42.1}
$$

With the associated coefficients $q_n$, the polynomial

$$
 P_N(x)=\sum_{n=0}^{N}\binom Nn\frac{(-x)^n}{n!}q_n
$$

has the exact representation $\mathcal E_N=\int_0^\infty e^{-x}|P_N(x)|^2dx$ in the source's normalization. This replaces angular optimization by a genuine squared norm. The inequality $\sqrt{\mathcal E_N}\le\sup_{|\zeta|=1}|W_N(\zeta)|\le\sqrt{N+1}\sqrt{\mathcal E_N}$ shows that the two versions have the same exponential scale.

## The Joukowski change of geometry

For the exact oriented-segment functional $\mathcal L$ of this branch, put

$$
 C_N=\mathcal L(T_N(2t-1)).
$$

The substitution $t=(1+\cos\theta)/2$ converts the Chebyshev polynomial into $\cos(N\theta)$. The coefficient can be computed from the Bernstein row by

$$
 C_N=\sum_{k=0}^{N}(-1)^{N-k}
 \frac{\binom{2N}{2k}}{\binom Nk}\beta_{N,k}.
 \tag{42.2}\label{eq:42.2}
$$

An endpoint $s$ outside $[0,1]$ is measured by the exterior Joukowski coordinate

$$
 \Phi_J(s)=2s-1+2\sqrt{s(s-1)},\qquad |\Phi_J(s)|>1.
$$

The relevant segment integral has leading term

$$
 \int_0^sT_N(2t-1)dt
 =\frac{\Phi_J(s)^{N-1}(\Phi_J(s)^2-1)}{8N}
 (1+O(N^{-1}))+O(N^{-1}).
 \tag{42.3}\label{eq:42.3}
$$

The source proves, for its exact functional,

$$
 \mathrm{RH}\iff(C_N)\in\ell^2
 \iff\limsup_{N\to\infty}|C_N|^{1/N}\le1.
 \tag{42.4}\label{eq:42.4}
$$

This is not an assertion that subexponential growth implies square summability for arbitrary sequences. The equivalence uses the specified spectral functional: real endpoints give an $L^2$ folded density, whereas nonreal endpoints give an exponentially growing finite leading combination. The branch's summability and endpoint-selection arguments are part of the theorem.

For $s=x+iy$ close to the interior interval, the older ellipse measure has logarithmic growth of order $y^2/[2x(1-x)]$, while the Joukowski measure has leading order $|y|/\sqrt{x(1-x)}$. The gain is linear rather than quadratic sensitivity to a small off-axis displacement.

## The global Hardy function and its unresolved estimate

The generating function $\mathscr C(r)=\sum_{N\ge0}C_Nr^N$ is written in the original source as a logarithmic quotient evaluated at

$$
 \omega_R(r)=-\frac{4r}{R(1+r)^2},\qquad
 \omega_R(r)=\omega_R(1/r).
$$

Its exact displayed expression is

$$
 \mathscr C(r)=\frac{q_0}{2}
 -\frac{R(1-r^2)}{8r}
 \log\frac{A(\omega_R(r))}{F(\omega_R(r))},
 \tag{42.5}\label{eq:42.5}
$$

where $A,F,R$ are the archived branch's reference, target, and scale, not the same symbols as the physical block matrices. The apparent origin singularity is interpreted through the Taylor expansion. The desired condition is $\mathscr C\in H^2(\mathbb D)$.

The finite record encloses $C_0,\ldots,C_{255}$ at $R=13597/2500000$. Their partial squared sum is about $2.69012\times10^{-6}$. That gives a concrete scalar sequence, but no bound for its infinite tail. Removing the universal $r=-1$ growth by an outer factor, deflating known real zeros, and finding a unitary realization were alternative attacks. None supplied the global Hardy estimate.

## The co-Poisson identity preserves a different tail

The cutoff-free arithmetic branch starts instead from a Müntz/co-Poisson transform

$$
 f\longmapsto\sum_{j\ge1}f(jx)-x^{-1}\int_0^\infty f.
$$

Its exact main-plus-tail representation has the form

$$
 D_k(t)=a_Y(t)+I(t)v_Y-
 \int_1^\infty M_Y(x)R_t'(x)\,dx.
 \tag{42.6}\label{eq:42.6}
$$

All quantities in (42.6) belong to that source's cutoff convention. In particular, even where a finite raw sampling term $W_t(d)$ vanishes, the centered remainder can satisfy $R_t(d)=-I(t)/d$. Such terms cannot be removed from the product expansion. This warning is directly useful for the divisor-logarithm construction of Chapter 18: cancellation must include the subtracted continuum term, not just visible integer samples.

The Nyman–Beurling and co-Poisson ideas are preserved as density and exact-transform alternatives. They have not been identified with the complete physical Schur source by an isometry or a funded inverse estimate.

## A countable test family is not a finite certificate

The rational Gabor branch records a countable outer criterion using packets indexed by rational scale and frequency. Its usefulness is that a dense, explicitly parameterized family can organize testing and continuity arguments. The missing bridge was from the protected native prefix to the complete rational packet class. Checking many rational pairs does not complete that bridge, just as checking many Chebyshev modes does not prove (42.4).

**Sources:** [JOUKOWSKI](#source-joukowski), the F19 theorem and interval package, [ATLAS](#source-atlas), the cutoff-free co-Poisson records, and the direct Gabor criterion in the early-September master. The functional $\mathcal L$ must be recovered from those sources before transporting the displayed scalar criteria to another normalization.


\part{Alternative structures and the information they preserve}

# 43. A killed jump process and order-sensitive arithmetic paths {#ch-jumps}

## An exact representation of the raw operator

The jump-process scout is one of the more concrete cross-field constructions because it starts with the actual raw operator. Put $I_b=(-b,b)$, $N=e^{2b}$, $\alpha_n=\Lambda(n)/\sqrt n$, and $S_N=\sum_{n<N}\alpha_n$. The full-line expression compressed by zero exterior values is

$$
 \mathcal A_b=P_b\left[m(D)-\sum_{n<N}\alpha_n
 (T_{\log n}+T_{-\log n})\right]P_b.
 \tag{43.1}\label{eq:43.1}
$$

Its odd restriction, using $J_b/\sqrt2$, has the physical half-line normalization of Chapter 4. The digamma identity gives

$$
 m(\xi)-m_0=\int_{\mathbb R}K(|z|)(1-\cos(\xi z))\,dz,
 \qquad K(s)=\frac{e^{-s/2}}{1-e^{-2s}}.
$$

The measure $K(|z|)dz$ satisfies the integrability conditions for a symmetric jump generator. Add the actual prime-power atoms:

$$
 \nu_N(dz)=K(|z|)dz+
 \sum_{n<N}\alpha_n(\delta_{\log n}+\delta_{-\log n})(dz).
 \tag{43.2}\label{eq:43.2}
$$

The corresponding nonnegative whole-line operator has symbol

$$
 \Psi_N(\xi)=m(\xi)-m_0+
 2\sum_{n<N}\alpha_n(1-\cos(\xi\log n)).
$$

Consequently, with $L_N^{I_b}$ its killed, zero-exterior restriction,

$$
 \mathcal A_b=L_N^{I_b}-c_NI,
 \qquad c_N=2S_N-m_0.
 \tag{43.3}\label{eq:43.3}
$$

The scalar subtraction is essential. Positivity of $L_N$ alone yields a lower bound of order $-S_N$, not the desired subpower floor. The random-process interpretation has organized the complete arithmetic, but has not removed its centered comparison.

For a future region after freezing $a<b$, the correct killed domain is $(-b,-a)\cup(a,b)$. It is not a translated single interval. Jumps may cross the old hole if their landing point survives; their intervening straight segment is not part of a jump trajectory.

## A complete path needs its occupation information

For an increment path $X_s$, define

$$
 W_\Omega(X)=\{x:x+X_s\in\Omega\text{ for every }0\le s\le t\}.
$$

At trace-class times, the return-bridge formula is

$$
 \operatorname{Tr}(e^{-tL_N^\Omega})
 =p_{N,t}(0)\,\mathbb E\bigl[|W_\Omega(X)|\mid X_t=0\bigr].
 \tag{43.4}\label{eq:43.4}
$$

For a symmetric domain, reflection contributes

$$
 \operatorname{Tr}(Re^{-tL_N^\Omega})
 =\frac12\mathbb P\{-X_t/2\in W_\Omega(X)\}.
 \tag{43.5}\label{eq:43.5}
$$

The factor $1/2$ comes from changing the starting point $x$ to the reflected displacement $-2x$. Taking the odd projection $(I-R)/2$ and including the scalar in (43.3) gives

$$
 \operatorname{Tr}_{\rm odd}(e^{-t\mathcal A_b})
 =\frac{e^{tc_N}}2\left[
 p_{N,t}(0)\mathbb E(|W_{I_b}|\mid X_t=0)
 -\frac12\mathbb P\{-X_t/2\in W_{I_b}\}\right].
 \tag{43.6}\label{eq:43.6}
$$

The difference of the two positive quantities is the actual odd-sector object. Dropping the favorable subtraction leaves only the large elementary scalar bound.

For a single interval, $|W_{I_b}|=(2b-R_t)_+$, where $R_t$ is the path's excursion span. Thus one part of the trace depends only on a span. With an old hole, however, the full occupation set is required. This is a specific reason an apparently simple probabilistic reduction ceases to close under successive physical cuts.

## Two identical prime products can have different boundary effects

Let $a_2=\log2$, $a_3=\log3$. The words

$$
 (a_2,a_3,-a_2,-a_3),\qquad
 (a_2,-a_2,a_3,-a_3)
$$

both have product one and displacement zero. Their spans are $\log6$ and $\log3$. At interval width $\log4$, the first compressed word vanishes and the second is a nonzero projection with surviving starting length $\log(4/3)$.

The boundary therefore remembers the order of arithmetic operations, even when multiplicative exponents and endpoints agree. This gives a concrete obstruction to replacing all physical histories by a commutative prime-product coefficient.

For one interval, a sufficient finite-word invariant is $(d,m,M)$: final displacement, minimum partial displacement, and maximum partial displacement. Concatenation obeys

$$
 (d,m,M)\star(d',m',M')
 =\bigl(d+d',\min(m,d+m'),\max(M,d+M')\bigr).
 \tag{43.7}\label{eq:43.7}
$$

This is exact dynamic programming, but not a bounded-state model. Values range over an expanding set of logarithms of rationals; holes and continuous Archimedean increments add further information.

## The completed pole remains a separate perturbation

For $C_b=A_b-g_bg_b^{*}$, the exact Duhamel equation is

$$
 e^{-tC_b}=e^{-tA_b}+
 \int_0^t e^{-(t-s)A_b}g_bg_b^{*}e^{-sC_b}\,ds.
 \tag{43.8}\label{eq:43.8}
$$

It retains the dressed pole correlations. Although raw and completed quadratic forms agree on pole-neutral vectors, that subspace is not generally invariant under the raw semigroup. Projecting a positive heat kernel onto it does not automatically reproduce the completed evolution.

The lasting contribution of this scout is the exact arithmetic process and its order-sensitive boundary invariant. A quantitative estimate of the signed expression (43.6), with the appropriate pole treatment, remains necessary.

**Source:** [JUMP](#source-jump), with the locked physical operator from [RIII](#source-riii) and the RGPAP physical-block records. The general killed-process framework is external; the atomic arithmetic jump measure and the explicit source normalization are particular to this calculation.

# 44. Gauges, implicit steps, and what a change of coordinates cannot improve {#ch-gauges}

## The physical metric travels with the coordinates

Let $A=A^{*}$ be an actual finite physical compression. Under $u=Sx$ with $S$ invertible, define

$$
 B=S^{*}AS,\qquad G=S^{*}S,\qquad L=G^{-1}B=S^{-1}AS.
$$

Then

$$
 A\succeq-sI\iff B\succeq-sG.
 \tag{44.1}\label{eq:44.1}
$$

The pole vector becomes $S^{*}g$, and the physical old projection $P$ becomes $S^{-1}PS$, which is orthogonal in the $G$ metric. A physical shift $sI$ becomes $sG$, including its cross blocks if the coordinates mix old and future spaces.

The exact example $A_N=\operatorname{diag}(-\sqrt N,1)$, $S_N=\operatorname{diag}(N^{-1/4},1)$ gives $B_N=\operatorname{diag}(-1,1)$. Its ordinary lower bound looks constant, but the generalized eigenvalue relative to $G_N$ is still $-\sqrt N$. This is the simplest model of a false gain obtained by forgetting the metric.

## A moving frame has a connection term

For $iu'=Au$ and a unitary $u=Q(t)y$,

$$
 iy'=\bigl(Q^{*}AQ-iQ^{*}Q'\bigr)y.
 \tag{44.2}\label{eq:44.2}
$$

The connection can absorb an evolution without changing its original energy sign. With scalar $A=-1$ and $Q=e^{it}$, the transformed dynamical generator is zero, but the physical form remains negative. Similarly, averaging two unitary gauges is not an equivalence: a signed off-diagonal contribution can disappear in the average while remaining in each original operator.

These observations explain why a coordinate or clock adjustment must produce a comparison theorem, not merely a simpler looking matrix.

## A real Cayley transform records the sign exactly

Set $H=A+sI$ and suppose $I+hH$ is invertible. For

$$
 R=(I+hH)^{-1},\qquad C_h(H)=(I-hH)(I+hH)^{-1},
$$

direct multiplication gives

$$
 I-C_h(H)^{*}C_h(H)=4hRHR.
 \tag{44.3}\label{eq:44.3}
$$

Thus contractivity is exactly equivalent to $H\succeq0$. A norm-expanding vector $w$ gives the physical witness $x=Rw$ with

$$
 x^{*}Hx=\frac{\|w\|^2-\|C_h(H)w\|^2}{4h}<0.
$$

In nonorthogonal coordinates, (44.3) becomes $G-C_G^{*}GC_G=4hR_G^{*}BR_G$. The transform can be useful numerically, but a fixed tolerance can hide a very negative eigenvalue because its Cayley modulus tends back toward one as the eigenvalue tends to minus infinity.

The imaginary Cayley transform $(I-ihA)(I+ihA)^{-1}$ is unitary for every Hermitian $A$, positive or not. Its eigenvalue phases encode the sign. Unitarity alone is therefore not the property required by an RH energy argument.

## Displacement structure survives an implicit step

If the actual sine matrix satisfies

$$
 [Z,A]=vd^{*}-dv^{*},
$$

then the inverse commutator identity gives

$$
 [Z,C_h(H)]=-2h\bigl[(Rv)(Rd)^{*}-(Rd)(Rv)^{*}\bigr].
 \tag{44.4}\label{eq:44.4}
$$

A bounded rational step preserves displacement rank two. This can reduce storage or accelerate exact assembly without presuming positivity. Displacement rank is not ordinary matrix rank; the spectrum can still contain many nontrivial eigenvalues.

Cutting the implicit step also has a precise self-energy. If $A=\left(\begin{smallmatrix}X&B\\B^{*}&D\end{smallmatrix}\right)$, its retained Cayley block equals the Cayley transform of

$$
 X_{h,s}=X+sI-B\bigl(D+(s+h^{-1})I\bigr)^{-1}B^{*}.
 \tag{44.5}\label{eq:44.5}
$$

The deleted region returns through the complete denominator. Removing it without this term changes the evolution. The example $X=0$, $B=1$, $D=1$, $s=0$, $h=1/2$ gives $X_{h,s}=-1/3$ and retained amplification $7/5$, whereas simply retaining $X$ would give one.

## Why unrestricted storage existence is not a new estimate

Let $u_{j+1}=T_ju_j$ with invertible transports, and let

$$
 S_k=\sum_{j<k}\Phi_j^{*}Q_j\Phi_j,
 \qquad \Phi_j=T_{j-1}\cdots T_0.
$$

A uniform lower bound $S_k\succeq-CI$ is equivalent to the existence of nonnegative storage matrices satisfying

$$
 Q_j\succeq T_j^{*}X_{j+1}T_j-X_j,
 \qquad X_0\preceq CI.
 \tag{44.6}\label{eq:44.6}
$$

One direction telescopes. In the other direction, $X_k=\Phi_k^{-*}(CI+S_k)\Phi_k^{-1}$ supplies storage directly from the unknown lower bound. Hence an unrestricted existence assertion can be circular as a proof strategy, even though the equivalence is valid.

The useful objective is an explicit arithmetic storage with an independently controlled budget. The moment flow of Chapter 21 and the RESET identity of Chapter 40 are concrete calculations of this kind. Neither has yet been identified with a globally funded native continuation.

**Sources:** [GAUGE](#source-gauge), [HYB](#source-hyb), and the same-metric reference reductions of RIII. The identities in this chapter are exact finite algebra; their cofinal application requires the original physical quantifiers.

# 45. Transported observations, reflection geometry, and arithmetic polarization {#ch-crossfields}

## Qualitative visibility versus quantitative energy

The many-clock and ghost-space programme describes what information survives observation after changing coordinate frames. Its rank and matroid ideas can identify redundant measurements or directions that can be quotiented out. Those statements are useful for selecting ports. They do not estimate the smallest nonzero observation eigenvalue.

For example, two observations making an angle $\theta$ can remain independent for every $\theta>0$, while the least eigenvalue of their Gram is of order $\theta^2$. An aperture-dependent angle $e^{-b^2}$ gives a superexponentially large inverse cost. A rank theorem cannot rule this out.

There is also a separate sign issue. Two full-rank maps $A=I$ and $B=\operatorname{diag}(2,1)$ have $A^{*}A-B^{*}B=\operatorname{diag}(-3,0)$. Complete visibility does not mean that a favorable source funds an adverse screen.

## A genuine damping estimate

The cross-field source does give a useful quantitative theorem when actual positive losses are present. Let $U_j$ be unitary, $0\preceq D_j\preceq I$, and $K_j=I-D_j^2$. Define undamped and damped propagators

$$
 \Psi_{j+1}=U_j\Psi_j,\qquad
 \Phi_{j+1}=D_jU_j\Phi_j,\qquad \Psi_0=\Phi_0=I,
$$

and the transported observation Gram

$$
 G_m=\sum_{j=0}^{m-1}\Psi_{j+1}^{*}K_j\Psi_{j+1}.
$$

Then

$$
 I-\Phi_m^{*}\Phi_m\succeq\frac{2}{m(m+1)}G_m.
 \tag{45.1}\label{eq:45.1}
$$

For a proof, set $x_j=\Phi_jx$, $y_j=\Psi_jx$, and $a_j=\|K_j^{1/2}U_jx_j\|$. The exact loss is $\sum a_j^2=\|x\|^2-\|\Phi_mx\|^2$. Since $(I-D_j)^2\preceq K_j$, the discrepancy between trajectories is at most $\sum_{\ell<j}a_\ell$. Consequently the $j$th undamped observation is at most $\sum_{\ell\le j}a_\ell$. Cauchy–Schwarz and summation give the factor $m(m+1)/2$.

This is an actual energy estimate, not a rank count. Its RH use would require the computed losses to be terms in the complete arithmetic form and the actual observation margin to have the right aperture scale. Adding imagined measurements does not add physical energy to the denominator.

## Reflection words constrain possible geometric lifts

The arithmetic full-line reflections $\rho_i f(x)=f(\lambda_i-x)$ satisfy $(\rho_1\rho_2\rho_3)^2=I$. A nonconcurrent triple of planar mirror reflections can instead satisfy $(R_1R_2R_3)^2=\tau_v$ with $v\ne0$.

A bounded simultaneous intertwiner $J$ between these full representations would satisfy $\tau_vJ=J$. A nonzero translation has no nonzero fixed vector in full-plane $L^2$, so $J=0$. This rules out that proposed exact lift. Boundary-enlarged or compressed models are not covered by the same simple conclusion, but must retain their word defects.

The independent public geometry work remains a separate subject. Its internal RH connections are recorded here only to preserve the tested insights and obstructions; no change to the public geometry manuscript is implied.

## Even exact modular symmetry has a counter-control

The stronger clock/cross-field control constructs a positive self-Fourier Gaussian–Hermite seed whose complete theta sum obeys the exact Poisson relation. Its even kernel has positive central coefficients and all odd boundary cancellations. Nevertheless its transform is

$$
 \xi(1/2+z)P_T(1/2+z),
 \qquad
 P_T(1/2+z)=\frac\varepsilon{16}
 \bigl((z-d)^2+T^2\bigr)\bigl((z+d)^2+T^2\bigr),
 \tag{45.2}\label{eq:45.2}
$$

with $d=1/4$ and, in the explicit rational example, $T=1000$. The added zeros occur at $s=1/4\pm1000i$ and $s=3/4\pm1000i$. The source proves positivity of the altered seed and kernel by exact polynomial bounds, rather than sampling.

This does not modify or disprove RH for the genuine Gaussian theta seed. It proves that modular symmetry, positive kernel, and positive coefficients do not by themselves distinguish that seed from a carefully constructed altered one. The negative-heat example of Chapter 22 is a different control: together the two prevent an induction based only on broad analytic shape.

## Selberg amplitudes and a fermionic correction

Another branch compared periodic-orbit trace amplitudes. For length $\ell$ and repetition $k$, the Selberg-type amplitude contains

$$
 \frac{\ell e^{-k\ell/2}}{1-e^{-k\ell}},
$$

whereas the Riemann prime-power amplitude is $\ell e^{-k\ell/2}$. Their ratio is exactly $1-e^{-k\ell}$, which can be expressed as the supertrace of $e^{-k\ell N}$ on an exterior algebra of one complex dimension.

This suggested pairing an orbit-side fermionic correction with a positive Hodge polarization. A generator $\Theta$ satisfying

$$
 \nu\langle f,g\rangle
 =\langle\Theta f,g\rangle+\langle f,\Theta g\rangle
 \tag{45.3}\label{eq:45.3}
$$

on a valid common domain would have $\Theta-\nu/2$ skew-symmetric, and would need the further operator-domain hypotheses for skew-adjointness. At $\nu=1$, an appropriate complete realization would place its spectrum on the critical line.

The arithmetic space, positive polarization, and exact trace identification were not constructed. Equation (45.3) is a design requirement, not a consequence of matching the amplitudes. This orbit-side supersymmetry is also distinct from the Cauer factorization $D_CD_C^{*}$ of Chapter 41.

**Sources:** [CLOCK](#source-clock), [CLOCK-MODULAR](#source-clock-modular), [COMP](#source-comp), and the Selberg/supertrace/Deninger sections of [ATLAS](#source-atlas) and the cumulative masters. Each cross-field mechanism is preserved with the specific additional structure required for arithmetic use.


\part{Connections, chronology, and the continuation of the work}

# 46. The counterexample archive as mathematical information {#ch-obstructions}

## Failures should be stored at the level of the implication

A failed argument need not invalidate the object it studied. The useful archival unit is therefore a precise implication together with its counterexample, domain, or incompatible scale. “The moment route failed” is too coarse; “finite Hankel positivity plus a positive even kernel implies all-rank positivity” is a definite statement that the negative-heat control disproves.

The same distinction applies to the physical programme. The large unweighted norm of a centered old/future operator does not refute a source-specific inverse-energy estimate. It does rule out using that unweighted norm as the small quantity. A scoped same-Gram identity can remain correct after the application to the complete denominator has been rejected.

## The principal physical exclusions

The full unweighted centered cross has recurrent high-frequency witnesses of size $e^{b/2}$ after a fixed old aperture is chosen. Finite pole removal does not remove those witnesses. Their Archimedean energy can be large, so they are not negative tests for the complete Weil form. Their significance is to retire a particular norm estimate, not to settle the form's sign.

The coefficient prime generator $\sum_p(\log p)v_p(n)=\log n$ differs from the physical fibre generator $\sum_{p^k\le t}\log p=\psi(t)$. The exact $N=8$ witness gives $\log420>\log8$. A transfer of a coefficient budget to physical fibres must therefore exhibit a different matched map or retain the compensating positive Hamiltonian.

Pure-Gram shorting and complete-owner shorting also differ. The example $B=(1,1)^T$, $D=BB^*+I$ leaves a nonzero transformed source and debt $1/6$, whereas the corresponding pure-Gram short vanishes. The discrepancy is not a technical pseudoinverse issue; it is the omitted background.

Finally, a common growing shift is not a fixed global shift. The two-dimensional model of Chapter 11 has a logarithmically growing negative direction before shifting, even though the prescribed growing shift gives a positive Schur reserve. A later theorem that consumes the older unshifted premise remains unsupported until that dependency is replaced.

## The geometric and localization exclusions

An unweighted finite-rank capture of the complete arithmetic residual cannot be uniformly small: the preserved essential-norm argument yields a lower bound of exponential aperture size. The energy-relative compression of Chapter 8 is a valid replacement, but it has its own large cutoff and finite-core sign.

Likewise, bounded-diameter positive square partitions can create an adverse arithmetic localization seam of order $e^b$. The proof uses simultaneous recurrence of the finitely many prime phases at each fixed aperture. It first takes frequency to infinity and then increases the aperture, which is permissible for the unrestricted norm. This excludes a universal polynomial scalar seam budget for that class of partitions. Disconnected remote windows, relative-energy estimates, and complete signed reorganizations remain outside that exclusion.

A nonconcurrent planar reflection lift fails a group-word identity, and a gauge change can conceal a negative eigenvalue only by changing the metric. Both are exact structural obstructions. More elaborate geometry is worthwhile only if it preserves or explicitly accounts for the missing relation.

## The coefficient and polynomial exclusions

Positive entries, total positivity of a collocation kernel, and positive semidefiniteness of a raw Hankel matrix are different notions. F42 provides the relevant reverse-Bessel warning. Factorial or Pascal rescaling is not automatically a positive congruence. The Pólya–Schur scouts give further distinctions: a preserving comparison model may fail its actual-coefficient transfer test; additional factors inside a restricted parameter class may be incapable of matching the necessary curvature.

The exact polynomial $1+3x+3x^2+x^3/2$ is useful in several places: it has positive coefficients and normalized log-concavity, yet nonreal zeros and an indefinite direct coefficient matrix. The reciprocal-Laplace example in Chapter 23 is stronger in a different direction: complete monotonicity of $1/F$ does not imply the required Stieltjes logarithmic derivative.

The heat and Gaussian–Hermite controls retain many of the properties one would naturally try to use in an all-rank induction. Their existence does not make an arithmetic proof impossible. It requires the proof to use a feature of the exact arithmetic function that those controls do not share.

## The finite-prime exclusions

The fixed-base criterion cannot be proved by changing $a$ as the rank changes. The endpoint criterion belongs to one function at one fixed base. A whole-cube inward field is false, and the finite trace rules out a fixed positive harmonic lower tube. The mature scale must be summable.

An exact prime hit on a codimension-one wall is not required once the actual mesh is proved sufficiently fine. On the other hand, a small coefficient in an associated or stripped continued fraction is not automatically the next literal Xi seed. The endpoint-Christoffel and absolute-index calculations must be retained. F166.85A resolves a particular forced-wall index ambiguity; it does not supply the missing flight estimate.

## How to reactivate a retired route

Reactivation should name the altered premise. A new source restriction may avoid an unrestricted-norm counterexample. A new complete residual estimate may avoid an adverse localization seam. A different preserving multiplier may escape the Jacobi parameter obstruction. A rigorously growing comparison scale may escape the bounded-Laguerre-parameter obstruction.

The fact that a new proposal uses different terminology is not such a change. The counterexample register accompanying this book records the relevant source and main-chapter location so that future work can test the actual hypotheses before rebuilding an invalid argument.

**Sources:** [II8](#source-ii8), [II9](#source-ii9), [COMP](#source-comp), [HYB](#source-hyb), [ARK](#source-ark), [CLOCK-MODULAR](#source-clock-modular), [F41](#source-f41)/[F42](#source-f42), and the post-Source71 audit. The results are indexed by their scoped inference rather than by a blanket verdict on a whole research family.

# 47. Cross-era connections and the missing identifications {#ch-connections}

## Three levels of connection

The programme contains many recurring shapes. To use them well, distinguish an **exact identification**, a **conditional transfer**, and an **analogy that motivates a calculation**.

An exact identification supplies the map, spaces, normalization, and equality. The all-carry lift and the congruence between the Hankel and direct coefficient matrices are examples. A conditional transfer supplies an implication with hypotheses that must still be checked for the target: projected denominator funding and the local dyadic RESET theorem have this form. An analogy notes a common mechanism, such as cubic centering or transport of a poorly observed direction, without asserting a target-space identity.

These categories should not be confused with usefulness. A precise conditional lemma can remove unnecessary burdens. An analogy can guide discovery. The error is treating either as an already verified arithmetic bridge.

## RESET and complete source funding

The old RESET margin update and the new Schur source debt are literally instances of the same block-inverse formula. This is the strongest algebraic connection across the programme. It suggests organizing the remaining proof around

$$
 \text{new margin}
 =\text{old margin}+\text{new resource}
 -\text{complete innovation energy}.
 \tag{47.1}\label{eq:47.1}
$$

For a physical application, the new resource must be a term in the complete owner; the inverse must use the denominator after every screen; and the innovation must be the source produced by the same elimination. The source orbit may allow a much smaller estimate than a full-space norm. Those are substantive gains in the target one needs to prove, but they still require explicit arithmetic allocation.

The positive-reference method contributes a further exact simplification: pure reference elimination has a single total debt, bounded for a frozen old aperture, rather than a sum of scalar errors charged at each strip. This means a prospective RESET proof should not repeatedly pay the same Archimedean interaction.

## Pole geometry and the finite boundary ledger

The rank-two pole read, the second-order homogeneous equation $(\partial_x^2-1/4)u=0$, and the two Cauchy boundary coordinates all express the same elementary exponential geometry in their respective settings. They support the expectation that a genuinely pole-generated residual can have a small effective boundary representation.

What does not follow is that every first-harmonic source or every prime endpoint lies in one fixed two-dimensional physical range. A low-dimensional state on each tooth may be embedded differently across teeth. The exact common extractor and transverse remainder must be exhibited before the small matrix represents the whole response.

The source quotient of Chapter 7 is the appropriate place to test this. An old-port-supported correction vanishes from the quotient by exact compression. A transverse correction remains visible. That distinction is more reliable than guessing the rank of the entire raw term.

## Three cubic mechanisms, three different meanings

Original Paper III has the exact cocircuit factor $X^2Z\nabla_\alpha^3\nabla_\beta$. Paper IX has a cubic saddle normal form yielding Airy scaling. The mature and neighboring-band calculations use subtraction of common values, first differences, and curvature to expose a higher-order residual.

These are not the same theorem. The first is divisibility in a finite combinatorial kernel; the second is local asymptotic geometry; the third is an arithmetic centering procedure. Their common lesson is that low-order structure should be removed before an absolute bound is taken.

The strongest unproved connection suggested by the record is an identity of the form

$$
 r_{\mathrm{native}}=\nabla^3 g+	ext{explicit boundary remainder}
 \tag{47.2}\label{eq:47.2}
$$

for the complete neighboring-band source after the precise old-port quotient. Equation (47.2) is a research question. It is not an established factorization of primes, and it must not be substituted into an energy estimate before being derived.

## The moment route and the old compact-moment route

The modern unshifted logarithmic moments and the older fixed-$a$ finite-prime moments both lead to Hankel matrices, canonical coordinates, and Schur pivots. But they are expansions of different transforms at different basepoints, with different cutoffs and smoothing conventions.

The modern one-Hankel theorem gains support information from analyticity of the complete entire function. The older F39 criterion gains an exact arithmetic trajectory from a fixed right-half-plane expansion. A theorem about one trajectory cannot be imported into the other by renaming its canonical coordinates. An explicit transform between their functionals, with quantified positivity preservation, would be needed.

A more modest reuse is already justified. Their determinant, continued-fraction, and endpoint-Christoffel algebra can be developed once and applied with the appropriate moment functional. Their all-rank positivity remains owner-specific.

## Divisor covariance and physical synthesis

The GCD inverse estimate and the divisor-logarithm construction both arise from incidence algebra. One controls the inverse of a coefficient covariance; the other creates exact cancellation before squaring. This is a real arithmetic connection and a reason to preserve the explicit Möbius inverse.

The physical synthesis map cannot be discarded. Nearly adjacent logarithmic frequencies have a poorly conditioned physical Gram even when the corresponding two-label GCD matrix is well conditioned. The quotient-first funding theorem preserves the synthesis on both sides, which is the correct way to combine arithmetic preconditioning with a physical inverse energy.

## A ranked research portfolio

The present ordering is a judgment about reusable structure, not a numerical probability of proving RH. The complete physical route has the most direct object-and-detector chain and now explicit local/complement budgets. The actual-coefficient route has the cleanest independent all-rank sign and strong controls against false inductions. The one-sided prime-excess route is unusually explicit arithmetically, while the multiplier and older finite-prime routes provide distinct representations that might supply a new preservation mechanism.

The archive should therefore be used as a portfolio with a primary calculation, not as dozens of equally active proof claims. The important question is whether a proposed import supplies a new estimate for the actual unresolved range.

**Sources:** the principal equations in Chapters 7–10, 14, 18–23, 26, 31, 37–45; [ATLAS](#source-atlas) and [LOST-GEMS](#source-lost-gems) for the historical synthesis. Equation (47.2) remains explicitly exploratory.

# 48. Chronology of the mathematical programme {#ch-chronology}

## How dates are interpreted

The dates below are dates recorded by the surviving research documents and handovers. A document's creation date in a storage system can differ from its internal research date, and neither alone establishes the date of first public disclosure. The chronology is intended to recover mathematical dependencies and corrections.

A later version supersedes an earlier statement only at the affected dependency. It does not erase a valid independent result. Conversely, a historical label such as ACTIVE or PASS is not preserved as an operative premise when the relevant later source gives a counterexample or narrows its scope.

## April and May: from analytic positivity to finite gates

The April 28–30 records explore logarithmic derivatives, Herglotz/Stieltjes representations, a theta/Mellin fold, and Laguerre–Pólya/Pólya-frequency coefficients. A finite-symbol determinant proposal fails a scaling check. The surviving idea is to find an exact positive realization, not merely a favorable numerical spectrum.

The May series then develops finite algebra in stages. Paper I isolates a boundary-absorbed Schur gate. Paper II organizes reciprocal-pair contributions and a flagged reservoir. Paper III supplies cocircuit factorization and forced-root divisibility. Paper IV turns residuals toward positive rising-factorial coefficients. Paper V uses a closed boundary ladder and a Sturm mechanism. These papers have their own definitions and finite hypotheses; they are not preliminary versions of the later Weil operator.

Papers VI–VIII shift toward the Jensen family. VI gives vertical proper position and Wronskian/Gram formulations. VII develops centered heat variables and root separation. VIII introduces variable-curvature saddle transfer and hard-window analysis. Paper IX assembles the asymptotic regions and finite seams. The recovered original TeX files allow the early results to be read in their own notation rather than reconstructed solely from later descriptions.

## June: spectral folds and compact moment support

The F18/F19 development replaces a Bernstein angular norm by a Laguerre square and then an orthogonal Chebyshev sequence. The Joukowski map sharpens sensitivity to nonreal endpoints. F21 converts a once-smoothed logarithmic derivative to compact Hausdorff/Jacobi coordinates; F22 supplies the unitary CMV fold under the support condition.

Gate A/B heat–Turán work investigates kernel curvature and critical-root drift. Several finite branches are later certified, but the all-branch first-contact argument remains a separate task. The finite evidence in F21 reaches degree 255 and compact Jacobi order 64 in its recorded normalization; it is not the same calculation as the September unshifted rank-20 tower.

## August: fixed-base arithmetic and the mature relay

F35–F39 fix the right-half-plane base, eventually $a=30$, and obtain the literal finite-prime Hausdorff-depth criterion. Reverse-Bessel impulses and canonical walls make prime activation explicit. F40 gives protected-coordinate response, F41 supplies the trace obstruction, and F42 rejects total-positivity shortcuts. The two-defect geometry is developed to replace the false whole-cube inward picture.

The mature relay then accumulates exact transport identities. F161 desingularizes the saddle response by integration by parts; F163/F164 supply conditional actual-branch inequalities. F165 corrects the off-resonance coordinate and selected crossing. F166 replaces equilibrium residue language with the physical endpoint-Christoffel and Darboux normalization.

The August 28 sequence .11–.18 is important because short handovers often stopped before it: low-branch packet bounds, amplitude derivatives, effective retention, and the activation residual are all part of the later relay, not optional numerical decorations.

## September 1–9: RESET indexing and global source organization

The later F166 notes pursue the canonical RESET product, Borel-response representation, forward retention, and the next entrance seed. The fixed-section inverse map .78 is followed by the forced-wall two-slot synchronization .85A. Thus “which index?” and “how large after the flight?” must be distinguished. The former is locally resolved at the wall; the latter remains quantitative.

The parallel early-September programme reorganizes around Cofinal Physical Prefix, sparse activation, Haar detail, a rank-two pole, and a terminating Redheffer edge. The source-specific innovation cost becomes the central scalar. First-visibility permanence and one-square Fejér–Riesz closure are rejected. The old long-lead qd strategy also remains outside the cubic-wedge range that motivated it.

Paper IX's historical seven-region activation and threshold $M_\star=671{,}088{,}640$ undergo hostile recertification. The earlier combined owner contract is not accepted. Later v437–v442 packages provide additional regional and finite certificates; their parameter dictionary and remaining low-slope region must be read separately from the earlier threshold.

## September 10–20: native finite sections and complete Weil geometry

The native mesh work progresses from finite source corridors to the terminal $H=6144$ certificate at $D=\log2/2048$. Fixed-mesh Xi capture is numerically contradicted by a persistent cell defect. Dyadic refinement and the complete detail Schur denominator become the next targets.

Source64/67/71 calculations, boundary jets, and MEL/co-Jost approaches then probe the continuum transition. Later audits correct finite entry budgets and reject a zero-gap conclusion from a tiny Rayleigh value. W200 supplies an independent fixed-window engine; exact collar tests block an easy universal induction built from it.

The Euler/shared-prime programme develops identity-normalized products, excitation Hamiltonians, same-gap Poisson transport, Gram–Feshbach birth factorization, and the Boundary–Weyl splice. The broad V13 manuscript preserves much of this structure, but its optimistic assembled status is superseded at the physical collar and continuation interfaces. Its exact identities remain source material.

## September 21–26: candidate chains and their hostile audit

The proof-facing V-series and its B-branch concentrate on Brehmer/current-exponent sources, literal first-Blaschke frames, common-cut inverse energy, and a cofinal shifted floor. The September 23 referee edition assembles these into a candidate chain. The R1/R2 repairs and September 24 Paper II replace an uncentered wide-placement claim by a centered decomposition and a proposed lifetime bound.

II.1 genuinely records a six-gate internal pass. Later II.2–II.7 records contain scoped repairs and replay claims. II.8 identifies specific remaining physical and metric dependencies, retaining the owner and detector while reopening the assembled placement/funding/continuation chain. II.9 reconciles this history and proves weaker alternative repair lemmas. The correct chronology is not that the historical pass never existed; it is that later source-level exceptions changed what could be inherited from it.

## September 27: the physical form becomes the organizing object

The RGPAP sequence tests harmonic displacement, gauge geometry, arithmetic decomposition, probability, and alternative routes. Referee III presents complete local terminal-strip coercivity, sharp cuts, the centered reference, and a carry-preserving representation. The complete-complement note adds total reference-debt control, a fixed-aperture spectral tail certificate, and adverse localization obstructions.

These results make the remaining signed core more explicit. They do not identify a favorable compression with the full expanding form. The day’s path-space and reflection calculations also expose information lost by purely multiplicative or purely geometric simplifications.

## September 28: detector, divisor, multiplier, and moment scouts

The quotient-first scout reduces inverse funding to the old-port complement and introduces arithmetic GCD preconditioning. The second scout gives the fixed two-packet detector and boundary completion. The third derives one-sided signed-mass growth and the ordinary-prime excess target. The fourth supplies exact composite cancellation and the optimal quarter surplus.

The architecture reassessment reopens the original Jensen lineage as an independent challenger. The preserving-multiplier tests find both a Jacobi-class obstruction and a broader admissible family. Prefix-energy work replaces root-by-root transfer by positive analytic approximants. Moment continuation pays a finite missing moment by positive-measure interpolation and obtains higher-order matching.

The all-rank scout reaches actual rank 20 but also supplies the negative-heat control and direct coefficient congruence. Cross-field work strengthens the modular counter-control. The subsequent source audit returns to Referee III and budgets its local inverse-expansion remainder with linear expansion degree. The archive's newest lost-gem synthesis proposes combining exact innovation accounting with higher-order centering; the native cubic identity remains unproved.

**Sources:** [MASTER](#source-master), [ATLAS](#source-atlas), original [P1](#source-p1)–[P8](#source-p8), [IX442](#source-ix442), the F166 sequence, [AUDIT19](#source-audit19), [II8](#source-ii8)/[II9](#source-ii9)/[RIII](#source-riii), and the dated September 27–28 reports. Detailed filenames and hashes appear in the source register and machine-readable catalogue.

# 49. The current working frontier {#ch-frontier}

## The physical target, without unnecessary strengthening

The primary unresolved question remains a lower bound for the complete signed form at cofinal apertures in the physical norm. A successful argument need not create a positive gap at every intermediate step. It may use a growing shift, a source-specific inverse estimate, or a complete residual lower bound, provided the final cumulative allowance has zero exponential rate.

The most concrete reference-relative expression is

$$
 S_H+W-ED^{-1}E^*.
 \tag{49.1}\label{eq:49.1}
$$

The pure reference debt has an exact total treatment. At fixed aperture, the full high-frequency complement can be bounded. For an original terminal strip, the inverse expansion error has an explicit budget. The remaining leading signed arithmetic expression and the actual successive pivots are still the tasks that matter.

An effective continuation theorem must address one of two compatible alternatives: control the complete joint source directly in the final denominator, or retain a full positive block and bound the entire residual after it. Neither alternative requires proving every stronger historical sufficient condition. Both require a literal arithmetic decomposition and compatible domains.

## The independent all-rank target

The coefficient route asks for

$$
 p_{2n+1}-v_n^TH_n^{-1}v_n>0
 \tag{49.2}\label{eq:49.2}
$$

at all stages where the preceding block is positive, or directly for positivity at an unbounded sequence of sizes. The direct coefficient kernel and the positive-measure approximation theorem remove certain assembly and transfer burdens. They do not control the prescribed fresh moment.

A valid induction must distinguish the exact undeformed theta kernel from the negative-heat and self-Fourier altered controls. It must also be relative to the shrinking moment interval: an error tending to zero in absolute size can be too large compared with the next Schur margin.

## The arithmetic target

The one-sided scalar formulation asks for a subexponential accumulated excess of the fixed ordinary-prime window. The divisor-logarithm majorant has only bounded asymptotic overcount, so its centered quadratic is a legitimate alternative object. The leading pole and prime term must still cancel at the required scale. The elementary unconditional smoothed bound retains linear exponential rate $1/2$ and does not meet that target.

A new sieve or incidence-algebra argument must therefore improve the centered arithmetic comparison, not merely make the composite indicator more accurate. The exact complete Gram and rational correction terms in Chapters 17–18 specify where such an improvement would enter.

## What would justify switching the main route

The older routes should be promoted only when a new theorem reaches their actual missing range. In the Jensen family, that means a cofinal unshifted or genuinely low-shift transfer, not another large-shift model. In the fixed-base relay, it means actual seed regeneration and quantitative flight/retention in the literal canonical coordinates, together with a finite entry seam. In a spectral realization, it means the actual positive Hamiltonian or valid limiting identification.

A successful new representation might indeed be decisive. The criterion is whether it supplies a verifiable mathematical mechanism that the present object does not expose. A change in vocabulary, a smaller diagram, or another finite test does not meet that criterion.

## A continuation record for the next calculation

Every next strike should begin by recording the source state, exact input object, target inequality, allowed external inputs, and the counter-controls it must survive. It should end by recording the newly proved statement or explicit failure, the affected descendants, and the remaining quantified claim. This is not administrative overhead: it prevents a local fact from silently becoming a different global premise in the following session.

The most valuable resource in this book is therefore not one favored equation alone. It is the combined record of exact arithmetic, legitimate reductions, finite certificates, and known obstructions. Used together, these make it possible to continue without repeatedly rediscovering either the same identity or the same invalid inference.

# 50. Proof dependencies and the programme's audit discipline {#ch-audit}

## The mathematical unit of certification

The recorded red-team protocol requires a dependency entry for every proof-bearing statement: hypotheses, conclusion, proof location, and dependencies. The basic object is a theorem application, not a page, a package name, or a count of favorable reviews.

For an operator statement, this means explicitly identifying the domain and codomain, the form domain, the norm, the adjoint convention, the shift, the aperture, the quotient or projection, and the complete source. For an asymptotic statement, it means recording which parameters are fixed, which tend to infinity, and whether the chosen horizons satisfy all required estimates simultaneously.

The five protocol layers are minimal-cut falsification, complete theorem coverage, orthogonal global audits, independent end-to-end reconstruction, and targeted counterexample testing. The first layer is designed to stop a long audit when a load-bearing implication already lacks proof.

## Dependency-specific reopening

A repair must be propagated downstream. Replacing an unshifted denominator by a common growing shift changes every theorem that used a fixed positive exterior. Restricting a source norm to a canonical range changes every later application to an unrestricted physical space. Replacing a two-port support equality by a transverse-error estimate creates an inverse-energy term that must be paid.

At the same time, independent statements are not erased. II.9's reconciliation preserves the historical six-gate record and the separately retained owner and detector. It reopens the affected physical implications by named exceptions. This is the proper interpretation of the source history.

## Independent reconstruction

The end-to-end reconstruction should start from the locked explicit formula, not from the last candidate's conclusion. It must recover the finite arithmetic algebra, pole extraction, actual centered source, complete denominator, shifts and cumulative bounds, and finally the detector. Any extra lemma required by that reconstruction becomes a visible missing dependency.

For the coefficient route, the corresponding reconstruction is theta coefficients, logarithmic recurrence, actual Hankel positivity, positive measure, analytic continuation, and zero geometry. A finite moment package is not a substitute for its all-rank arrow.

## Computation as a premise

If a theorem uses a numerical enclosure, the computation belongs inside its proof dependencies. Exact rational tests, outward interval certificates, and floating-point diagnostics have different roles. A small matrix counterexample can disprove a universal algebraic claim. A finite interval certificate can prove the positivity of its enclosed matrix. A high-precision numerical sign without enclosure remains a diagnostic.

The preservation checks associated with this edition concern source identity, recoverability, and the book's mathematical transcription. Historical computational results are recorded with their original scope. Their data and programs are retained so that a subsequent proof-bearing replay can target the exact required version rather than an ambiguous filename.

## The research state as a set of statements

The most reliable summary of the programme is not a single Boolean. It is the collection of established local and conditional statements together with the explicit global obligations in Chapter 49. The book accordingly gives the mathematics its own prose: hypotheses where they are needed, counterexamples where they constrain a route, and open problems where they remain.

**Source:** [PROTOCOL](#source-protocol), [II8](#source-ii8), [II9](#source-ii9), and the source-level dependency ledgers. The protocol's exact original wording remains in the source collection; this chapter develops its operational mathematical content.


\appendix
\part{Reference material}

# Notation and normalization concordance {#app-notation}

## Analytic functions

The lower-case completed function is $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$. The real-axis function is $\Xi(t)=\xi(1/2+it)$. The even entire descent used in Chapters 19–23 is $F(w)=\xi(1/2+\sqrt{w/\kappa})/\gamma_0$, where $\kappa=\gamma_1/\gamma_0$ and $\xi(1/2+z)=\sum\gamma_jz^{2j}/j!$. This normalization makes $F(0)=F'(0)=1$.

The older F21 notation can instead start from $\Xi(\sqrt{-w})/\Xi(0)$ before its scale is imposed. The fixed-$a$ branch uses $Q(y)=\xi'/\xi(1/2+y)$ and $R(x)=Q(\sqrt x)/\sqrt x$. None of these symbols is a physical quadratic form until a separate dictionary is supplied.

A polynomial called $Q$ in the Jensen chapters is a neighboring or derivative polynomial. The $Q$ in a Schur block is often a positive future reference. A projection denoted $Q=I-P$ is yet another object. The chapter definitions take precedence over the letter.

## Parameters that must not be identified

| Symbol or name | Meaning in its declared chapter | Required distinction |
|---|---|---|
| $b$ | Physical logarithmic aperture | Not a prime cutoff or matrix size |
| $N=e^{2b}$ | Faithful arithmetic cutoff | Subpower in $N$ equals subexponential in $b$ |
| $a=30$ | Fixed right-half-plane base of F39 | Not a variable aperture |
| $D$ | Native mesh width in Chapters 39–40 | Elsewhere a denominator block or polynomial degree |
| $d,n$ | Jensen degree and shift | Original P5 uses an offset degree convention |
| $\lambda$ | Paper IX chart parameter | Earlier and later charts reuse the symbol differently |
| $M_\star$ | Historical Paper IX global threshold | Not a presently inherited theorem constant |
| $p_r$ | Logarithmic coefficient of the normalized $F$ | Not the canonical moment $p_j$ in F39 |
| $\chi_k$ | Canonical coordinate of a compact moment prefix | Not a spatial cutoff in other chapters |
| $\epsilon$ | Soft pole reserve or an approximation tolerance | Its local definition is essential |
| $\tau$ | Gaussian concentration or heat time | Different constructions, different signs and scales |

## Physical norms and adjoints

All physical Hilbert spaces are complex. Inner products are conjugate-linear in their first argument. The unnormalized odd extension $J_b$ satisfies $\|J_bu\|^2=2\|u\|^2$, and the full-line Weil form satisfies $Q_W(J_bu)=2q_{\mathrm{comp},b}[u]$. The normalized odd isometry is $J_b/\sqrt2$.

The raw and completed half-line forms differ by $|\ell_b(u)|^2$, with $g_b(x)=2\sinh(x/2)$ and $\ell_b(u)=\langle g_b,u\rangle$. Their equality on $\ker\ell_b$ is a quadratic-form identity. It does not imply that this subspace is invariant under every operator or semigroup used later.

For a nonunitary change $u=Sx$, the coordinate metric is $G=S^*S$. A physical inequality $A\succeq-sI$ becomes $S^*AS\succeq-sG$. An identity with a different right-hand metric is a different statement.

## Four distinct uses of a Gram matrix

A **synthesis Gram** is $BB^*$ for an explicitly declared map. A **complete denominator** includes all background, arithmetic, boundary, and shift terms present at that stage. A **moment Gram** is the Hankel or localizer matrix of a specified functional. An **observation Gram** sums transported measurement energies. These objects can coincide only through a proved identity.

The same-Gram inverse relation $(Bc)^*(BB^*)^\dagger(Bc)\le\|c\|^2$ does not bound the inverse cost in an unrelated complete denominator. The support of a source in a port range is likewise stronger than knowing that each local source has a small number of coordinates.

## Source names and aliases

Original Papers I–IX form the polynomial/Jensen series. Referee Papers I, II and III belong to the later physical proof-facing sequence; the September 23 referee edition is identified in the catalogue by its full title. Decimal referee numbers II.1–II.9 are audit checkpoints, not chapters of Original Paper II.

The F-number system also has collisions across historical branches. “F43” in the fixed-base relay denotes two-defect recruitment; a similarly numbered Paper IX source can denote another spectral reduction. A full source key, family, and content identifier should accompany every such reference.

The terms *owner*, *funding*, *front*, *relay*, *firewall*, and *soft state* are internal vocabulary. In the main exposition they denote, respectively, the exact mathematical object, a positive comparison resource, an active boundary/index, a repeated rank-transition mechanism, a rule preventing an invalid transfer, and a distinguished small-energy direction. They do not add mathematical hypotheses beyond the displayed definitions.

# Result and mechanism locator {#app-results}

## Exact identities with several applications

| Mechanism | Principal treatment | What the identity supplies |
|---|---|---|
| Full/half-line odd normalization | Chapter 4 | The same Rayleigh quotient and pole convention |
| Exact old-block nesting | Chapter 4 | An unchanged old physical form under zero extension |
| Arithmetic-free canonical shell | Chapter 5 | Zero direct arithmetic diagonal in that shell |
| Positive Green completion | Chapter 6 | A single reference retaining the lowest Archimedean cancellation |
| Total reference debt | Chapters 6, 8 | No repeated scalar charge for exact reference elimination |
| Complete block inverse | Chapter 7 | Source and denominator transformed together |
| Quotient equals inverse compression | Chapter 7 | Old-supported corrections removed exactly |
| Compiled boundary graph | Chapter 7 | Positive boundary term retained in the effective denominator |
| Augmented source certificate | Chapter 10 | A source-specific inverse bound, not a full inverse norm |
| Carry-preserving lift | Chapter 9 | The literal physical dilation including every carry |
| Finite Euler inverse | Chapter 13 | Complete divisor algebra before compression |
| Rational three-source routing | Chapter 14 | Exact nondivisible scales after source–operator–source composition |
| Sine displacement identity | Chapter 14 | Structured assembly of the complete finite arithmetic matrix |
| Divisor covariance inversion | Chapter 17 | Explicit Möbius inverse and subpower coefficient conditioning |
| Divisor logarithm | Chapter 18 | Composite cancellation before squaring |
| Logarithmic coefficient recurrence | Chapter 19 | Actual moment data from actual Taylor coefficients |
| Prefix matching | Chapter 20 | Quantitative local uniform convergence of admissible models |
| Moment-preserving parameter flow | Chapter 21 | Exact prior-moment preservation and next-moment budget |
| Direct coefficient congruence | Chapter 23 | The same Hankel signs without logarithmic assembly |
| Schur curvature and boundary reservoir | Chapter 24 | A completed finite gate rather than termwise positivity |
| Reciprocal orbit grouping | Chapter 25 | Exact coefficient counts and their forced reservoirs |
| Cocircuit factorization | Chapter 26 | Higher-order difference structure in the finite gate |
| Polar Wronskian | Chapter 29 | Adjacent proper position from higher-degree hyperbolicity |
| Endpoint-Christoffel map | Chapter 37 | Exact transport of the continued fraction |
| Forced-wall two-slot shift | Chapter 37 | Correct absolute index at the wall |
| Haar RESET budget | Chapter 40 | Fine margin equals coarse margin minus innovation debt |
| Quotient-residual trial identity | Chapter 40 | Self-defect separated from transverse forcing |
| Joukowski fold | Chapter 42 | An orthogonal scalar detector and slit-plane geometry |
| Killed jump representation | Chapter 43 | Complete raw arithmetic as a generator minus a scalar |
| Path occupation concatenation | Chapter 43 | Order-sensitive aperture information |
| Cayley defect | Chapter 44 | Exact preservation of the physical sign in rational coordinates |
| Transport plus genuine damping | Chapter 45 | Quantitative observation-to-loss conversion |

## Conditional statements that reduce unnecessary demands

The cofinal staircase of Chapter 3 permits subexponential negative allowance and remote, nonuniformly spaced horizons. It does not require positivity at every aperture. The single-Hankel implication of Chapter 19 needs positivity at unbounded sizes, not a uniform eigenvalue margin. Positive-prefix transfer does not require a root-by-root separation estimate. The old-port quotient does not require funding already eliminated directions. The source-fitting estimate permits a transverse defect if its inverse cost is explicitly paid. The local RESET criterion permits constants depending on a frozen source set, provided the later schedule handles them.

These are genuine logical reductions. They should not be strengthened again without a reason. Their remaining hypotheses concern actual arithmetic objects, and those hypotheses must not be inferred from an auxiliary model.

## Finite results with particularly reusable content

The native terminal-prefix theorem owns every earlier prefix at its fixed mesh. The actual rank-20 moment certificate owns a finite initial matrix family but not its next extension. W200 owns its declared fixed support window. The Paper IX regional certificates own their explicit rectangles and asymptotic regimes, with their primitive-dependency requirements. Original Papers I–V contain exact symbolic finite-gate and layer results that do not yet transfer to every actual Xi minor.

Finite counterexamples are equally reusable. The source-only first contact of 4 is indefinite. The same-Gram versus complete-Gram example disproves an interchange of shorts. The generalized gauge example disproves an apparent gain from unweighted coordinates. The polynomial averaging, complete-monotonicity, and negative-heat examples identify inadequate hypotheses for global real-rootedness.

## Formula retrieval beyond the principal exposition

The companion display index records recognized literal mathematical blocks from every recovered theory source, with content identity and line locators. It includes alternative forms and historical versions that do not need to be repeated in the principal exposition. The heading index supplies the corresponding theorem, section, or certificate heading when present.

Identical equations can occur under different hypotheses, so equal formula hashes do not identify theorem applications. Conversely, equivalent formulas written differently remain distinct literal entries. The complete original source is the authority for its definitions, inline equations, diagrams, and surrounding proof.

# Computational evidence and its exact scope {#app-computations}

## Four categories

An exact rational or symbolic calculation proves the finite identity it evaluates. An outward interval computation proves the enclosed finite assertion under its arithmetic and error model. A high-precision floating-point calculation is a diagnostic unless a valid enclosure is supplied. A source-integrity check establishes the identity of preserved bytes, not the truth of their mathematical claims.

The following record keeps those categories separate. Counts refer to the source reports' executions unless explicitly described as editorial checks of this edition.

## Older polynomial and finite-prime records

| Record | Preserved coverage | Limitation that travels with it |
|---|---|---|
| Original Papers I–V | Exact coefficient, root-skeleton, endpoint and finite-layer calculations | Full-prefix or all-degree extensions remain separately stated |
| Paper IX | Regional interval certificates, finite Wronskians and later v437–v442 records | A region is not complete coverage of the parameter plane |
| F19 Chebyshev fold | Modes 0 through 255 | No infinite Hardy-tail estimate |
| F21/F22 | Hausdorff degree 255, Jacobi order 64, 127 canonical moments and CMV order 64 in the retained record | Smoothing and scale fixed; all-rank support open |
| F39 | Depth bounds 67, 79 and 85 at the stated finite prime cutoffs | No unbounded actual-depth invariant |
| F163–F168 and later relay | Exact symbolic identities, conditional constants, interval/prefix checks | Mature hypotheses, next entrance and finite seam must be supplied |

## Native and physical records

The $H=6144$ certificate is an augmented-matrix certificate that implies all earlier faithful prefixes at its mesh. The fine RESET calculations separately retain entry enclosures and numerical inverse diagnostics. These should not be combined into an unrecorded continuum certificate.

The Source71 audit preserves corrected coarse and first-refinement bounds together with a much smaller continuum test. The latter is an absolute Rayleigh bound, not a sign or exact-zero result. W200 retains its fixed-window verification suite and any distinct later margin variants as separate sources.

Referee III contains analytical proofs of terminal-strip positivity and exact Schur reductions. The complete-complement source gives a mathematical spectral-cut construction and explicit worst-case dimension bound; it does not claim to have numerically built and certified the enormous resulting matrix. The local inverse note's 96 exact finite tests verify auxiliary inverse-expansion algebra, not the global arithmetic sign.

## September 28 scout record

| Scout family | Recorded calculation | Mathematical reach |
|---|---|---|
| Quotient/GCD | 8,192 exact divisor identities; exact inverse at order 16; rational quotient tests | Auxiliary algebra and conditioning, not native funding |
| Boundary/detector | Twelve exact block cases and synthetic Gaussian diagnostics | Finite identities; detector proved analytically in its source |
| One-sided prime excess | Exact arithmetic covariance and convolution checks | Supports formulas, not the cofinal prime estimate |
| Quarter surplus | 11,999 proper-divisor checks, coefficient identities, matrix logarithms and graph completions | Auxiliary finite checks accompanying an asymptotic argument |
| Hybrid multipliers | Actual theta enclosures, interval parameter fits and an interval degree-eight transfer failure | Exact fitted models; no unbounded-degree transfer |
| Prefix energy | Positive fits through prefixes 3, 6 and 7; selected failed continuation paths | Finite feasibility and local differential identities |
| Moment continuation | Actual coefficients through order 25; size-13 moment data and order-24 fractional matching | Finite positive measures; unbounded feasibility open |
| All-rank scout | Forty coefficient enclosures; rank 20; rank-19 localizers; 38 canonical coordinates | Finite actual positivity and matched altered-function control |
| All-rank control | Negative-heat function passes the same finite tests | Demonstrates why finite positivity does not justify induction |

The complete archived programs and receipts identify their environments and exact inputs. Synthetic spectra and rational matrices are not reported as zeta data. Failed optimization or unfinished eigenvalue computations retain their failed or unfinished status.

## Fresh editorial checks in this edition

The edition independently checks the reassembly hashes of the nine-part vault and the original theory-source manifest, hashes every retained source object, and validates the generated archives. It also performs exact small-case checks of the original Paper I endpoint boundary, the ordered/orbit counting convention in Paper II, several principal algebraic identities used in the unified exposition, and source-preserving transcription consistency.

These editorial calculations are listed with executable code and machine-readable results. They do not replace the historical large numerical suites. The source register makes it possible to perform those suites later against an exact version rather than an inferred substitute.

# Editorial concordance and recoverable coverage {#app-editorial}

## Changes made in the exposition

The original source bytes are retained unchanged. The authored exposition makes the following local changes explicitly.

**The Paper I boundary case.** The source's displayed endpoint product includes $n=2$. Evaluating the defining Schur expression gives $G_2(1^m)=m(m-1)(m+2)/2$. Chapter 24 therefore states the printed uniform product for $n\ge3$ and gives $n=2$ separately. Exact computations of the defining specialization and the product agree at the tested $n=3,\ldots,8$. Those checks support the boundary diagnosis, not an independent proof of the full symbolic theorem.

**Ordered triples versus orbit sums.** Chapter 25 writes the fully mixed coefficient both as an ordered sum and as a sum over one representative of each permutation orbit. It makes the multinomial multiplicity explicit. This prevents an orbit from being summed twice; no coefficient positivity is inferred from the counting repair.

**Multiplicity in the trace obstruction.** Chapter 35 distinguishes the trace of a scalar cyclic multiplication operator, which counts distinct support points, from a zero sum carrying multiplicities. The inequality between them suffices for the finite-trace obstruction. No simplicity of zeta zeros is assumed.

**Hankel index size.** The main convention is $H_n=(p_{i+j+1})_{i,j=0}^{n-1}$, an $n\times n$ matrix, with the displayed next pivot using $p_{2n+1}$. Some cumulative summaries use an upper index $n$ while retaining the same pivot notation. The book fixes the size convention once and does not silently combine the two.

**Paper IX parameters.** Earlier and later uses of $\lambda$ are not identified. The older ratio $d/(n+d/2)$ has range at most two for nonnegative shift; it cannot be the later chart coordinate with threshold 5.52. Chapter 31 records the later region without importing a false numerical dictionary.

**Source vocabulary.** Generic forms, norms, and coordinates are distinguished by their chapter definitions. Original labels remain searchable, but a shared word such as *owner* or *Gram* is not treated as a mathematical map.

## Corpus boundaries

The recoverable corpus combines the original nine-part September 20 vault, its theory-source manifest, later manuscript and verification packages, cumulative master and architecture atlas, the referee and RGPAP sources, and the latest arithmetic and moment scouts. Two late-relay notes were separately recovered from Library in addition to their appearances inside cumulative masters: F166.78 and F166.85A.

The original vault was reassembled as a byte object of 1,538,199,981 bytes with SHA-256 beginning `c81ec61fc1c1e2da`. Its original 1,304 theory-source objects were recovered and checked against their recorded hashes. The expanded exact-text and code collection has 6,687 distinct objects, of which 1,762 are classified as theory/text sources. These are document/object counts, not numbers of discoveries.

The literal index recognizes 194,176 display-block occurrences representing 32,283 distinct blocks, and 117,379 heading occurrences. Cumulative masters repeat predecessors; repetitions are counted as occurrences and kept in their sources. Inline formulas, unusual mathematical delimiters, and graphics need the original source even if the automatic display index does not isolate them.

A complete raw export of every account conversation, deleted file, and inaccessible project was not recovered. Historical chat content survives in the visible conversation and in retained handovers, not necessarily as complete original transcripts. The source catalogue distinguishes an exact standalone file from a cumulative report about another source. No missing standalone original is replaced by invented text.

## A stable way to extend the book

An addition should have an exact source file and hash, a dated statement of its hypotheses and conclusion, a source-to-chapter location, and a dependency-specific supersession note when it changes an earlier result. The authored exposition can then be revised without changing the frozen source.

The core book, source catalogue, and raw evidence have different roles. The core provides a coherent argument and research history. The catalogue provides stable retrieval. The exact sources preserve full proofs, symbolic certificates, code, data, and historical variants. Retaining all three avoids both repeated reinvention and the opposite problem of a large archive with no mathematical guide.


# Primary source register {#app-sources}

The keys used in the chapters resolve below to exact recovered source objects. Titles of cumulative notes are retained as historical titles. A source identifier is derived from its SHA-256 hash; the complete digest, original path, and archive ancestry are in the companion catalogue. Source availability is distinct from a new proof audit.

## P1 — Boundary-Absorbed A2-Curvature Inequalities for Toeplitz–Pólya Frequency Schur Minors {#source-p1}

Exact object: `S-98519678386aa255`. Format: tex. Length: 35,458 bytes.

Original file: Paper I polished boundary absorbed A2.tex.

## P2 — Flagged Reciprocal-Pair Positivity for Boundary-Absorbed Schur-Minor Gates {#source-p2}

Exact object: `S-fa761138fa5fa79a`. Format: tex. Length: 72,434 bytes.

Original file: Paper II polished flagged reciprocal pair.tex.

## P3 — Cocircuit–Brion Factorization and Forced Root Skeletons in Fully Mixed Flagged Determinant Gates {#source-p3}

Exact object: `S-ac3361eaee452ab6`. Format: tex. Length: 59,124 bytes.

Original file: Paper III polished cocircuit brion skeleton.tex.

## P4 — Rising-Factorial Positivity of Prefix Residuals in Jacobi-Chain Endpoint Gates {#source-p4}

Exact object: `S-fcd89aa66551cf9b`. Format: tex. Length: 72,108 bytes.

Original file: Paper IV polished four layers final corrected.tex.

## P5 — A Boundary-Minor Mechanism for Newton–Jensen Hyperbolicity {#source-p5}

Exact object: `S-c3fff90a0513b483`. Format: tex. Length: 86,372 bytes.

Original file: Paper V definitive consolidated.tex.

## P6 — Vertical Proper Position and Wronskian Gram Feasibility for Jensen Polynomials {#source-p6}

Exact object: `S-4c097cbcf1024626`. Format: tex. Length: 55,790 bytes.

Original file: PAPER VI expanded master v2 WITH AUTHOR PAPERS.tex.

## P7 — Centered Heat Root Flows, Robust Jensen Gates, and a Full-Lattice RH Bridge {#source-p7}

Exact object: `S-d197fadcf7984b2d`. Format: tex. Length: 73,806 bytes.

Original file: paper vii centered heat root flows v2 fortified.tex.

## P8 — Saddle-Separation Gates for Jensen Hyperbolicity and the Leading Hard-Window Xi Profile {#source-p8}

Exact object: `S-2c68db16ed6050fe`. Format: tex. Length: 32,209 bytes.

Original file: paper viii saddle separation gates.tex.

## IX442 — Paper IX v442: effective large-parameter region and remaining low-slope range {#source-ix442}

Exact object: `S-896c05cc031f91b4`. Format: md. Length: 1,890 bytes.

Original file: README.md.

## MASTER — Exhaustive recoverable master archive, 28 September 2026 {#source-master}

Exact object: `S-bfad5f7dd1c0c92d`. Format: md. Length: 55,192,718 bytes.

Original file: RH EXHAUSTIVE MASTER ARCHIVE 2026-09-28(1).md.

## ATLAS — Architecture atlas, exotic routes, and lost-gem ledger {#source-atlas}

Exact object: `S-0e30003bfb0c8aaa`. Format: md. Length: 55,710,006 bytes.

Original file: RH EXHAUSTIVE ARCHITECTURE ATLAS AND LOST GEMS 2026-09-28.md.

## RIII — Referee III: Local Coercivity and Exact Schur Reductions for the Odd Weil Form {#source-riii}

Exact object: `S-846753cfc08d5bba`. Format: tex. Length: 39,327 bytes.

Original file: Referee Paper III.tex.

## RII — Referee-facing Paper II, 24 September 2026 {#source-rii}

Exact object: `S-9440035393c0e395`. Format: tex. Length: 38,228 bytes.

Original file: Dumas Referee Facing Paper II RH Proof Candidate 2026-09-24.tex.

## II8 — Referee II.8: terminal audit and local repairs {#source-ii8}

Exact object: `S-a893796e0bb0d24a`. Format: md. Length: 80,255 bytes.

Original file: Dumas Referee Paper II 8 TERMINAL LAYER1 AUDIT 2026-09-26.md.

## II9 — Referee II.9: history reconciliation and constructive repair {#source-ii9}

Exact object: `S-1aeba0e42dc30d75`. Format: md. Length: 15,555 bytes.

Original file: Dumas Referee Paper II 9 HISTORY AND REPAIR 2026-09-26.md.

## II9-DIRECTION — Complete-denominator directional source funding {#source-ii9-direction}

Exact object: `S-99a619b7e3a03f53`. Format: md. Length: 19,918 bytes.

Original file: directional funding.md.

## II9-ADAPTIVE — Adaptive continuation and the replacement physical contract {#source-ii9-adaptive}

Exact object: `S-b9b2e16074b5747f`. Format: md. Length: 23,945 bytes.

Original file: adaptive contract repair.md.

## II9-G2 — Actual unrestricted centered-norm obstruction {#source-ii9-g2}

Exact object: `S-342d50c8c604e1a2`. Format: md. Length: 20,396 bytes.

Original file: G2 actual scope.md.

## COMP-PROOF — Full complement certificate and energy-relative finite reduction {#source-comp-proof}

Exact object: `S-af5d2cd340be052a`. Format: md. Length: 20,814 bytes.

Original file: complement certificate.md.

## INV — Native local inverse remainder with explicit source budget {#source-inv}

Exact object: `S-dcbe5693e878ca4f`. Format: md. Length: 5,887 bytes.

Original file: NATIVE INVERSE REMAINDER NOTE.md.

## SC1 — Cross-project scout: quotient-first funding and GCD covariance {#source-sc1}

Exact object: `S-f86c7fce4f09f4e2`. Format: md. Length: 28,790 bytes.

Original file: RH CROSS PROJECT SCOUT REPORT 2026-09-28.md.

## SC2 — Second scout: complete boundary completion and two-packet detection {#source-sc2}

Exact object: `S-04ce7f19d7f06637`. Format: md. Length: 31,036 bytes.

Original file: SECOND SCOUT REPORT.md.

## SC3 — Third scout: one-sided signed mass and prime excess {#source-sc3}

Exact object: `S-27084fc3d2629940`. Format: md. Length: 28,177 bytes.

Original file: THIRD SCOUT REPORT.md.

## SC4 — Fourth scout: divisor logarithm and optimal quarter surplus {#source-sc4}

Exact object: `S-201f6ed31814cf76`. Format: md. Length: 31,439 bytes.

Original file: RH FOURTH SCOUT REPORT 2026-09-28.md.

## HYB — Actual-coefficient multiplier tests and hybrid obstructions {#source-hyb}

Exact object: `S-10c4e5e5db9e0735`. Format: md. Length: 25,092 bytes.

Original file: REPORT.md.

## PC — Positive-prefix transfer and explicit parameter energy {#source-pc}

Exact object: `S-c028388ec6b92175`. Format: md. Length: 26,426 bytes.

Original file: REPORT.md.

## MC — Moment continuation, canonical coordinates, and positive measures {#source-mc}

Exact object: `S-d9b08492453b9716`. Format: md. Length: 26,354 bytes.

Original file: REPORT.md.

## ARK — All-rank scout: rank-20 certificates, heat control, and direct coefficient kernel {#source-ark}

Exact object: `S-dce1dc227ffaadbf`. Format: md. Length: 21,001 bytes.

Original file: REPORT.md.

## GAP — RGPAP arithmetic progress: exact centered decomposition {#source-gap}

Exact object: `S-7e6a1c0b897cb27a`. Format: md. Length: 11,174 bytes.

Original file: RGPAP Arithmetic Progress 2026-09-27.md.

## HARM — Actual sine displacement structure and complete Schur transport {#source-harm}

Exact object: `S-be73938e72f7c1cd`. Format: md. Length: 9,768 bytes.

Original file: sine displacement.md.

## LOEWNER — Harmonic Loewner/displacement representation {#source-loewner}

Exact object: `S-afbbeddbf1386910`. Format: md. Length: 5,272 bytes.

Original file: loewner displacement replay.md.

## JUMP — Killed jump processes and boundary occupation information {#source-jump}

Exact object: `S-4a36471e93804ae2`. Format: md. Length: 11,353 bytes.

Original file: nonlocal information.md.

## GAUGE — Exact gauge metrics and Crank–Nicolson/Cayley identities {#source-gauge}

Exact object: `S-7236ce8c36563fc8`. Format: md. Length: 10,359 bytes.

Original file: gauge cayley.md.

## WAVE — Neutral wave packets and quantitative prime-phase recurrence {#source-wave}

Exact object: `S-d1fc2f4875b92a32`. Format: md. Length: 11,162 bytes.

Original file: wave uncertainty.md.

## CLOCK — Clock/ghost crossfields: observation, damping, and counter-controls {#source-clock}

Exact object: `S-06bbb0ac3f685d9b`. Format: md. Length: 21,342 bytes.

Original file: REPORT.md.

## CLOCK-MODULAR — Clock crossfield continuation and exact modular counter-control {#source-clock-modular}

Exact object: `S-ec740b67e40ef658`. Format: md. Length: 20,519 bytes.

Original file: REPORT.md.

## PROTOCOL — RH red-team certification audit protocol {#source-protocol}

Exact object: `S-ab6dbf986e412c7e`. Format: txt. Length: 9,305 bytes.

Original file: RH red team audit protocol.txt.

## F21 — Self-layer-cake Jacobi/CMV owner {#source-f21}

Exact object: `S-3727eb9d71b4fab5`. Format: md. Length: 3,903 bytes.

Original file: F21 SELF LAYER CAKE COMPLETE BERNSTEIN JACOBI OWNER v244.md.

## F21-NEAR — Near-exponential complete-Bernstein model {#source-f21-near}

Exact object: `S-6f5e3d5d5aa7c6e4`. Format: md. Length: 11,628 bytes.

Original file: RH EUREKA NEAR EXPONENTIAL F21 AND SAFE CAUCHY 2026-09-05.md.

## F21-CHERNOFF — Canonical-product and Chernoff/Hausdorff comparisons {#source-f21-chernoff}

Exact object: `S-fc1cbe54e32d2624`. Format: md. Length: 8,526 bytes.

Original file: RH F21 CHERNOFF TRANSITION SHELL 2026-09-05.md.

## F36 — Fixed-base Xi-native moment owner {#source-f36}

Exact object: `S-60fb99c6f6c2449c`. Format: md. Length: 25,636 bytes.

Original file: RH F36 Prime Safe Hausdorff Wall Lattice Master Transfer v1 2026-08-21.md.

## F37 — Reverse-Bessel impulse representation {#source-f37}

Exact object: `S-0e662f9c8f6c45b5`. Format: md. Length: 25,703 bytes.

Original file: RH F37 Reverse Bessel Laguerre Prime Front Master Transfer v1 2026-08-21.md.

## F38 — Parity chains and canonical-wall determinants {#source-f38}

Exact object: `S-f61bb4d174c49356`. Format: md. Length: 19,244 bytes.

Original file: RH F38 Canonical Tube Hankel Margin Master Transfer v1 2026-08-21.md.

## F39 — Fixed-parameter strict Hausdorff-depth criterion {#source-f39}

Exact object: `S-d7e2caf259656d9d`. Format: md. Length: 26,131 bytes.

Original file: RH F39 Finite Prime Prefix Closure and Face Polarization Master Transfer v1 2026-08-21-1.md.

## F40 — Protected-coordinate light cones {#source-f40}

Exact object: `S-818fdb132f46b84b`. Format: md. Length: 28,033 bytes.

Original file: RH F40 Logarithmic Light Cone Prime Block Separation Master Transfer v1 2026-08-21.md.

## F41 — Trace obstruction and Schur renewal {#source-f41}

Exact object: `S-ecf54e88c72c20cb`. Format: md. Length: 27,361 bytes.

Original file: RH F41 Trace Class Obstruction and Schur Renewal Master Transfer v1 2026-08-21-1.md.

## F42 — Reverse-Bessel total-positivity obstruction {#source-f42}

Exact object: `S-f7d993d51e11a0bb`. Format: md. Length: 36,226 bytes.

Original file: RH F42 Reverse Bessel TP Obstruction and Frontier Action Master Transfer v1 2026-08-21.md.

## F163 — Actual branch-response inequality under mature hypotheses {#source-f163}

Exact object: `S-27d8a8e604b688ac`. Format: md. Length: 4,124 bytes.

Original file: RH F163 ACTUAL BR RESET FREEZE 2026-08-24.md.

## F164 — Safe-cone sign and retained branch control {#source-f164}

Exact object: `S-47b901032678d20d`. Format: md. Length: 1,590 bytes.

Original file: RH F164 EXPLICIT SAFE CONE SIGN 2026-08-24.md.

## F165-NORM — Corrected off-resonance normalization {#source-f165-norm}

Exact object: `S-19d7642421016721`. Format: md. Length: 11,705 bytes.

Original file: RH F165 NORMALIZATION AND EXACT TRANSPORT 2026-08-26.md.

## F165.2 — Corrected thin-core transport {#source-f165-2}

Exact object: `S-27f70a0d77f11649`. Format: md. Length: 8,190 bytes.

Original file: RH F165 2 FINITE TRANSPORT FREEZE 2026-08-26.md.

## F165.8 — Selected crossing depth and physical-residue continuation {#source-f165-8}

Exact object: `S-7d841f92eae13685`. Format: md. Length: 6,281 bytes.

Original file: RH F165 8 F166 7 INVARIANT MARGIN RECURRENCE 2026-08-26.md.

## F167 — Exceptional-cell Möbius map and cube-only prefix bootstrap {#source-f167}

Exact object: `S-88283427e9f8a7de`. Format: md. Length: 7,578 bytes.

Original file: RH F167 CUBE ONLY PREFIX BOOTSTRAP 2026-08-26.md.

## F168 — Summable-tail amplitude reduction {#source-f168}

Exact object: `S-b0a3a3b1beaff776`. Format: md. Length: 3,468 bytes.

Original file: RH F168 SUMMABLE TAIL AMPLITUDE REDUCTION 2026-08-26.md.

## F166.78 — Exact inverse RESET determinant and same-index owner map {#source-f166-78}

Exact object: `S-d6eb4b7f00daf920`. Format: md. Length: 2,994 bytes.

Original file: F166 78 EXACT INVERSE RESET DETERMINANT MAP 2026-09-02.md.

## F166.85A — Forced-wall two-slot index synchronization {#source-f166-85a}

Exact object: `S-2f7ab9768852fd65`. Format: md. Length: 6,220 bytes.

Original file: F166 85A EXACT FORCED WALL TWO SLOT INDEX SYNCHRONIZATION 2026-09-03.md.

## NATIVE6144 — Fixed-mesh terminal prefix certificate through source 61 {#source-native6144}

Exact object: `S-d507d07459eda77c`. Format: md. Length: 10,010 bytes.

Original file: RH NEXT STRIKE GLOBAL PREFIX TO H6144 AND RESET MINCUT 2026-09-12.md.

## RESET12 — Dyadic RESET/refinement: complete Schur debt and local summability target {#source-reset12}

Exact object: `S-50e5db37c3f0233a`. Format: md. Length: 9,692 bytes.

Original file: RH DYADIC RESET REFINEMENT STRIKE 2026-09-12.md.

## MOVING-MEL — Quotient-residual Xi capture and the moving-corridor estimate {#source-moving-mel}

Exact object: `S-73b6f51525211330`. Format: md. Length: 7,056 bytes.

Original file: RH EUREKA QUOTIENT RESIDUAL XI MOVING MEL 2026-09-12.md.

## AUDIT19 — Consolidated Source71/collar audit and repair {#source-audit19}

Exact object: `S-634bd0708e82c82c`. Format: md. Length: 76,986 bytes.

Original file: RH CONSOLIDATED AUDIT AND REPAIR 2026-09-19.md.

## JOUKOWSKI — Joukowski–Chebyshev orthogonal fold {#source-joukowski}

Exact object: `S-b532ec190a3d5074`. Format: md. Length: 8,424 bytes.

Original file: PaperIX v243 Joukowski Chebyshev Orthogonal Fold.md.

## W200-DIGEST — W200 frozen working digest {#source-w200-digest}

Exact object: `S-b58fbe5de15b6c60`. Format: md. Length: 95,783 bytes.

Original file: W200 FROZEN WORKING DIGEST 2026-09-19(1).md.

## AR — Architecture reassessment and two independent hybrids {#source-ar}

Exact object: `S-a82b16574b501dcc`. Format: md. Length: 22,950 bytes.

Original file: REASSESSMENT.md.

## COMP — Complete complement, mixed terms, and Schur assembly {#source-comp}

Exact object: `S-b17a7c6489522b0a`. Format: md. Length: 16,408 bytes.

Original file: Complete Complement and Schur Assembly 2026-09-27.md.

## V10B — V10-B: complete batch pullback and rational three-source residue {#source-v10b}

Exact object: `S-a0c54e4c1067ec0f`. Format: md. Length: 21,402 bytes.

Original file: RH FACING PAPER V10B CUBD AUDIT 2026-09-22(1).md.

## V12 — V12 candidate manuscript and original physical-placement chain {#source-v12}

Exact object: `S-a4ac54f9990d219b`. Format: tex. Length: 297,659 bytes.

Original file: RH RKSPT ARXIV PREPRINT V12 2026-09-19.tex.

## II5 — Referee II.5: scoped post-short Boundary–Weyl repair {#source-ii5}

Exact object: `S-e15c9f5c14706bfe`. Format: tex. Length: 16,391 bytes.

Original file: Dumas Referee Paper II 5 G5 PostShort Certification 2026-09-26.tex.

## II1 — Referee II.1 and the historical six-gate freeze {#source-ii1}

Exact object: `S-d77aef75c8941a31`. Format: md. Length: 2,100 bytes.

Original file: Dumas Referee Paper II.1 LAYER1 FROZEN 2026-09-24.md.

## W200-CORPUS — W200 frozen research corpus {#source-w200-corpus}

Exact object: `S-ac2e099719c91b44`. Format: md. Length: 4,216,561 bytes.

Original file: W200 FROZEN ARTIFACT RESEARCH CORPUS 2026-09-18(1)(2).md.

## LOST-GEMS — Recovered lost-gem synthesis: RESET, pole modes, cocircuits and co-Poisson {#source-lost-gems}

Exact object: `S-462792155d1226a3`. Format: txt. Length: 15,127 bytes.

Original file: Pasted text(4).txt.

## F166.3 — F166.3 — exact endpoint-Christoffel canonical map and deposit-identification correction {#source-f166-3}

Exact object: `S-3d480b72108141db`. Format: md. Length: 6,819 bytes.

Original file: RH F166 3 ENDPOINT CHRISTOFFEL CANONICAL MAP 2026-08-26.md.

## F166.5 — F166.5 — exact equilibrium-to-actual future-residue barrier transfer {#source-f166-5}

Exact object: `S-60eafc91b7757f51`. Format: md. Length: 5,916 bytes.

Original file: RH F166 5 EQUILIBRIUM TO ACTUAL BARRIER 2026-08-26.md.

## F166.11 — F166.11 — fixed low-branch anchor and exact post-packet canonical bound {#source-f166-11}

Exact object: `S-566c6d92683e0063`. Format: md. Length: 9,361 bytes.

Original file: RH F166 11 LOW BRANCH PACKET BOUND 2026-08-28.md.

## F166.12 — F166.12 — global RESET logarithmic derivative without an unnamed finite head {#source-f166-12}

Exact object: `S-2844783a3e385cea`. Format: md. Length: 4,774 bytes.

Original file: RH F166 12 GLOBAL RESET LOG DERIVATIVE 2026-08-28.md.

## F166.13 — F166.13 — exact endpoint-Darboux amplitude intertwiner and summable switch cost {#source-f166-13}

Exact object: `S-1528a839f8f5461b`. Format: md. Length: 9,804 bytes.

Original file: RH F166 13 ENDPOINT DARBOUX AMPLITUDE INTERTWINER 2026-08-28.md.

## F166.16 — F166.16 — effective selected-excursion RET constants and deposit reserve {#source-f166-16}

Exact object: `S-904a9559c1bf6a99`. Format: md. Length: 5,174 bytes.

Original file: RH F166 16 EFFECTIVE RETENTION CONSTANTS 2026-08-28.md.

## F166.18 — F166.18 — activation-band regeneration reduced to a residual of size 24 {#source-f166-18}

Exact object: `S-67c85b6f142515ca`. Format: md. Length: 3,151 bytes.

Original file: RH F166 18 ACTIVATION RESIDUAL GATE 2026-08-28.md.

## F166.19 — F166.19 — exact RESET width telescope and two-sided post-packet deposit {#source-f166-19}

Exact object: `S-dd6373d84e4ebec4`. Format: md. Length: 5,736 bytes.

Original file: RH F166 19 RESET WIDTH TELESCOPE TWO SIDED PACKET 2026-08-28.md.

## F166.30 — F166.30 — Switch-then-strip seed localization theorem {#source-f166-30}

Exact object: `S-224023084a149f56`. Format: md. Length: 5,599 bytes.

Original file: RH F166 30 SWITCH THEN STRIP SEED LOCALIZATION 2026-08-28.md.

## F166.31 — F166.31 — qd Schur-strip theorem and endpoint-localizer congruence {#source-f166-31}

Exact object: `S-356f9df79bf18d5a`. Format: md. Length: 6,600 bytes.

Original file: RH F166 31 QD SCHUR STRIP ENDPOINT CONGRUENCE 2026-08-28.md.

## F166.32 — F166.32 — Two-parity defect deletion and exact rank-relabel pivot theorem {#source-f166-32}

Exact object: `S-7a5c7b2260d05007`. Format: md. Length: 7,500 bytes.

Original file: RH F166 32 TWO PARITY DEFECT DELETION RANK RELABEL 2026-08-28.md.

## F166.33 — F166.33 — Robust activation residual from a coarse absolute width ledger {#source-f166-33}

Exact object: `S-7788fab6cb56d9c7`. Format: md. Length: 6,118 bytes.

Original file: RH F166 33 ACTIVATION RESIDUAL ROBUST WIDTH LEDGER 2026-08-28.md.

## F166.34 — F166.34 — self-consistent protected-prefix response in the mature high band {#source-f166-34}

Exact object: `S-a72a81a81c9d4dd4`. Format: md. Length: 5,266 bytes.

Original file: RH F166 34 SELF CONSISTENT HIGH BAND RESPONSE 2026-08-28.md.

## F166.35 — F166.35 — normalized unit-block source bracket and same-Xi mature capture {#source-f166-35}

Exact object: `S-a85f87ab4e7d2724`. Format: md. Length: 7,127 bytes.

Original file: RH F166 35 NORMALIZED UNIT BLOCK SOURCE AND SAME XI CAPTURE 2026-08-28.md.

## F166.36 — F166.36 — capture closes the summable width, trace, half-cube, and activation loop {#source-f166-36}

Exact object: `S-3aed81bd36a20fa3`. Format: md. Length: 7,604 bytes.

Original file: RH F166 36 CAPTURE INVARIANT WIDTH TRACE HALFCUBE 2026-08-28.md.

## F166.44 — F166.44 — Elementary adjacent reverse-Bessel recurrence and local matching closure {#source-f166-44}

Exact object: `S-b400efa3cc5d6833`. Format: md. Length: 6,246 bytes.

Original file: RH F166 44 ELEMENTARY LOCAL MATCHING CLOSURE 2026-08-30.md.

## F166.48 — F166.48 — Actual post-pole edge trap {#source-f166-48}

Exact object: `S-2666e672d5576b32`. Format: md. Length: 13,108 bytes.

Original file: RH F166 48 ACTUAL POST POLE EDGE TRAP 2026-08-30.md.

## F166.52C — F166.52C — Literature Import Dossier {#source-f166-52c}

Exact object: `S-e6465d090ebc3593`. Format: md. Length: 40,483 bytes.

Original file: RH F166 52C LITERATURE IMPORT DOSSIER 2026-08-31.md.

## F166.54 — F166.54 — Cross-cycle qd edge return and explicit post-pole Darboux seed {#source-f166-54}

Exact object: `S-776afc817fcec8c1`. Format: md. Length: 3,283 bytes.

Original file: RH F166 54 CROSS CYCLE EDGE RETURN AND RESET SEED 2026-08-31.md.

## F166.55 — F166.55 — Positive bounded-seed selected crossing with widened packet constants {#source-f166-55}

Exact object: `S-39e526f927542af7`. Format: md. Length: 3,958 bytes.

Original file: RH F166 55 POSITIVE SEED WIDENED SELECTED CROSSING 2026-08-31.md.

## F166.56 — F166.56 — Exact parity-pivot reset determinant injection {#source-f166-56}

Exact object: `S-761dd038575f3bf3`. Format: md. Length: 3,624 bytes.

Original file: RH F166 56 PARITY PIVOT RESET DETERMINANT INJECTION 2026-08-31.md.

## F166.57A — F166.57A — Finite seam staircase reconstruction {#source-f166-57a}

Exact object: `S-afcf021b107774d7`. Format: md. Length: 4,765 bytes.

Original file: RH F166 57A FINITE SEAM STAIRCASE RECONSTRUCTION 2026-08-31.md.

## F166.58 — F166.58 — Moderate-band reverse-Bessel response scout {#source-f166-58}

Exact object: `S-efd8b8855483793a`. Format: md. Length: 3,743 bytes.

Original file: RH F166 58 MODERATE BAND REVERSE BESSEL RESPONSE SCOUT 2026-08-31.md.

## F166.59A — F166.59A — Moderate-band endpoint response theorem {#source-f166-59a}

Exact object: `S-ff50c1d80e8e1443`. Format: md. Length: 5,313 bytes.

Original file: F166 59A MODERATE BAND ENDPOINT RESPONSE 2026-09-01.md.

## F166.59BC — F166.59B/C — Moderate exterior response, invariant trace, response-aware capture, and local matching corridor {#source-f166-59bc}

Exact object: `S-afd3c40e63bc0da0`. Format: md. Length: 9,640 bytes.

Original file: F166 59BC MODERATE CAPTURE MATCHING 2026-09-01.md.

## F166.60 — F166.60 — Post-pole edge-trap threshold compression {#source-f166-60}

Exact object: `S-b074ef7f5e9ae0d2`. Format: md. Length: 2,645 bytes.

Original file: F166 60 EDGE TRAP THRESHOLD 1E9 2026-09-01.md.

## F166.62 — F166.62 — Promoted RESET residue monotonicity {#source-f166-62}

Exact object: `S-25efb2c70e7554f7`. Format: md. Length: 2,868 bytes.

Original file: F166 62 PROMOTED RESET RESIDUE MONOTONICITY 2026-09-01.md.

## F166.63 — F166.63 — Exact owner kill tests and reset-determinant transport reduction {#source-f166-63}

Exact object: `S-557f549ca6f9a4b6`. Format: md. Length: 7,698 bytes.

Original file: F166 63 OWNER KILL AND RESET TRANSPORT REDUCTION 2026-09-01.md.

## F166.64A — F166.64A — RESET lower-localizer one-way wall theorem {#source-f166-64a}

Exact object: `S-0adbb8bda5c5658a`. Format: md. Length: 4,957 bytes.

Original file: F166 64A RESET LOWER LOCALIZER ONE WAY WALL 2026-09-01.md.

## F166.64B0 — F166.64B0 — Moderate reset-injection and distortion-budget theorem {#source-f166-64b0}

Exact object: `S-1d7c5e101ca33d04`. Format: md. Length: 1,549 bytes.

Original file: F166 64B0 MODERATE RESET INJECTION BUDGET 2026-09-01.md.

## F166.64B2 — F166.64B2 — F165 determinant-recentering budget {#source-f166-64b2}

Exact object: `S-5140de8152275b9f`. Format: md. Length: 1,451 bytes.

Original file: F166 64B2 F165 RECENTERING BUDGET 2026-09-01.md.

## F22 — F22 — cumulative-source entry {#source-f22}

Exact object: `S-bfad5f7dd1c0c92d`. Format: md. Length: 55,192,718 bytes.

Original file: RH EXHAUSTIVE MASTER ARCHIVE 2026-09-28(1).md.

This key points to the complete master; it is not a claim of separate original-file recovery. Search the heading index for the exact family and number.

## F43 — F43 — cumulative-source entry {#source-f43}

Exact object: `S-bfad5f7dd1c0c92d`. Format: md. Length: 55,192,718 bytes.

Original file: RH EXHAUSTIVE MASTER ARCHIVE 2026-09-28(1).md.

This key points to the complete master; it is not a claim of separate original-file recovery. Search the heading index for the exact family and number.

## F156 — F156 — cumulative-source entry {#source-f156}

Exact object: `S-bfad5f7dd1c0c92d`. Format: md. Length: 55,192,718 bytes.

Original file: RH EXHAUSTIVE MASTER ARCHIVE 2026-09-28(1).md.

This key points to the complete master; it is not a claim of separate original-file recovery. Search the heading index for the exact family and number.

## F161 — F161 — cumulative-source entry {#source-f161}

Exact object: `S-bfad5f7dd1c0c92d`. Format: md. Length: 55,192,718 bytes.

Original file: RH EXHAUSTIVE MASTER ARCHIVE 2026-09-28(1).md.

This key points to the complete master; it is not a claim of separate original-file recovery. Search the heading index for the exact family and number.

## F162 — F162 — cumulative-source entry {#source-f162}

Exact object: `S-bfad5f7dd1c0c92d`. Format: md. Length: 55,192,718 bytes.

Original file: RH EXHAUSTIVE MASTER ARCHIVE 2026-09-28(1).md.

This key points to the complete master; it is not a claim of separate original-file recovery. Search the heading index for the exact family and number.


# Numbered-equation index {#app-equations}

The entries below point to the principal numbered formulas in this exposition. The companion literal display index includes the much larger recovered source collection.

## Chapter 1: One programme, several mathematical objects

| Equation | Context | Page |
|---|---|---:|
| (1.1) | The present order of work | \pageref{eq:1.1} |
| (1.2) | The present order of work | \pageref{eq:1.2} |

## Chapter 2: Functions, transforms, and metrics

| Equation | Context | Page |
|---|---|---:|
| (2.1) | Completed zeta and the two even descents | \pageref{eq:2.1} |
| (2.2) | Completed zeta and the two even descents | \pageref{eq:2.2} |
| (2.3) | Completed zeta and the two even descents | \pageref{eq:2.3} |
| (2.4) | Completed zeta and the two even descents | \pageref{eq:2.4} |
| (2.5) | Completed zeta and the two even descents | \pageref{eq:2.5} |
| (2.6) | Fourier and odd half-line conventions | \pageref{eq:2.6} |
| (2.7) | Fourier and odd half-line conventions | \pageref{eq:2.7} |
| (2.8) | Fourier and odd half-line conventions | \pageref{eq:2.8} |
| (2.9) | The physical logarithmic form domain | \pageref{eq:2.9} |
| (2.10) | The physical logarithmic form domain | \pageref{eq:2.10} |
| (2.11) | A typed estimate | \pageref{eq:2.11} |

## Chapter 3: Cofinality, convergence, and the actual endpoint

| Equation | Context | Page |
|---|---|---:|
| (3.1) | A lower allowance can be enough | \pageref{eq:3.1} |
| (3.2) | The adaptive staircase | \pageref{eq:3.2} |
| (3.3) | The adaptive staircase | \pageref{eq:3.3} |
| (3.4) | The adaptive staircase | \pageref{eq:3.4} |
| (3.5) | The adaptive staircase | \pageref{eq:3.5} |
| (3.6) | The adaptive staircase | \pageref{eq:3.6} |
| (3.7) | The polynomial endpoint | \pageref{eq:3.7} |

## Chapter 4: The odd Weil form and its exact embeddings

| Equation | Context | Page |
|---|---|---:|
| (4.1) | Translation, reflection, and the arithmetic sum | \pageref{eq:4.1} |
| (4.2) | Translation, reflection, and the arithmetic sum | \pageref{eq:4.2} |
| (4.3) | Translation, reflection, and the arithmetic sum | \pageref{eq:4.3} |
| (4.4) | Translation, reflection, and the arithmetic sum | \pageref{eq:4.4} |
| (4.5) | Translation, reflection, and the arithmetic sum | \pageref{eq:4.5} |
| (4.6) | The full-line identity | \pageref{eq:4.6} |
| (4.7) | The full-line identity | \pageref{eq:4.7} |
| (4.8) | The full-line identity | \pageref{eq:4.8} |
| (4.9) | The full-line identity | \pageref{eq:4.9} |
| (4.10) | Closed forms and compact resolvent | \pageref{eq:4.10} |
| (4.11) | Exact old-block nesting | \pageref{eq:4.11} |
| (4.12) | Exact old-block nesting | \pageref{eq:4.12} |
| (4.13) | Why the pole-neutral space is not a direct sum of neutral pieces | \pageref{eq:4.13} |

## Chapter 5: Arithmetic shells and positive terminal strips

| Equation | Context | Page |
|---|---|---:|
| (5.1) | The arithmetic-free canonical diagonal | \pageref{eq:5.1} |
| (5.2) | A support-measure uncertainty bound | \pageref{eq:5.2} |
| (5.3) | A support-measure uncertainty bound | \pageref{eq:5.3} |
| (5.4) | A support-measure uncertainty bound | \pageref{eq:5.4} |
| (5.5) | A support-measure uncertainty bound | \pageref{eq:5.5} |
| (5.6) | The complete terminal-strip theorem | \pageref{eq:5.6} |
| (5.7) | The complete terminal-strip theorem | \pageref{eq:5.7} |
| (5.8) | The complete terminal-strip theorem | \pageref{eq:5.8} |
| (5.9) | The complete terminal-strip theorem | \pageref{eq:5.9} |
| (5.10) | The complete terminal-strip theorem | \pageref{eq:5.10} |
| (5.11) | The complete terminal-strip theorem | \pageref{eq:5.11} |
| (5.12) | The complete terminal-strip theorem | \pageref{eq:5.12} |
| (5.13) | Integer batches and the inverse bound | \pageref{eq:5.13} |
| (5.14) | Integer batches and the inverse bound | \pageref{eq:5.14} |

## Chapter 6: A positive reference with exact boundary cancellation

| Equation | Context | Page |
|---|---|---:|
| (6.1) | The Green compression | \pageref{eq:6.1} |
| (6.2) | The Green compression | \pageref{eq:6.2} |
| (6.3) | The Green compression | \pageref{eq:6.3} |
| (6.4) | The Green compression | \pageref{eq:6.4} |
| (6.5) | The retained perturbation | \pageref{eq:6.5} |
| (6.6) | The retained perturbation | \pageref{eq:6.6} |
| (6.7) | The retained perturbation | \pageref{eq:6.7} |
| (6.8) | The lowest Archimedean exponential cancels exactly | \pageref{eq:6.8} |
| (6.9) | The lowest Archimedean exponential cancels exactly | \pageref{eq:6.9} |
| (6.10) | The lowest Archimedean exponential cancels exactly | \pageref{eq:6.10} |
| (6.11) | Total reference debt is bounded once | \pageref{eq:6.11} |
| (6.12) | Total reference debt is bounded once | \pageref{eq:6.12} |
| (6.13) | The architectural gain | \pageref{eq:6.13} |

## Chapter 7: Schur reduction and the source that actually survives

| Equation | Context | Page |
|---|---|---:|
| (7.1) | The complete block inverse | \pageref{eq:7.1} |
| (7.2) | The complete block inverse | \pageref{eq:7.2} |
| (7.3) | The complete block inverse | \pageref{eq:7.3} |
| (7.4) | The complete block inverse | \pageref{eq:7.4} |
| (7.5) | Reduction relative to a positive reference | \pageref{eq:7.5} |
| (7.6) | Reduction relative to a positive reference | \pageref{eq:7.6} |
| (7.7) | Reduction relative to a positive reference | \pageref{eq:7.7} |
| (7.8) | Reduction relative to a positive reference | \pageref{eq:7.8} |
| (7.9) | Reduction relative to a positive reference | \pageref{eq:7.9} |
| (7.10) | Reduction relative to a positive reference | \pageref{eq:7.10} |
| (7.11) | Quotient first: old ports can be eliminated exactly | \pageref{eq:7.11} |
| (7.12) | Quotient first: old ports can be eliminated exactly | \pageref{eq:7.12} |
| (7.13) | Quotient first: old ports can be eliminated exactly | \pageref{eq:7.13} |
| (7.14) | Quotient first: old ports can be eliminated exactly | \pageref{eq:7.14} |
| (7.15) | Boundary completion in a graph chart | \pageref{eq:7.15} |
| (7.16) | Boundary completion in a graph chart | \pageref{eq:7.16} |
| (7.17) | Boundary completion in a graph chart | \pageref{eq:7.17} |
| (7.18) | Boundary completion in a graph chart | \pageref{eq:7.18} |

## Chapter 8: The infinite complement and the local inverse budget

| Equation | Context | Page |
|---|---|---:|
| (8.1) | A fixed-aperture spectral cut | \pageref{eq:8.1} |
| (8.2) | A fixed-aperture spectral cut | \pageref{eq:8.2} |
| (8.3) | A fixed-aperture spectral cut | \pageref{eq:8.3} |
| (8.4) | A fixed-aperture spectral cut | \pageref{eq:8.4} |
| (8.5) | A fixed-aperture spectral cut | \pageref{eq:8.5} |
| (8.6) | A fixed-aperture spectral cut | \pageref{eq:8.6} |
| (8.7) | A valid but very large finite core | \pageref{eq:8.7} |
| (8.8) | A valid but very large finite core | \pageref{eq:8.8} |
| (8.9) | A valid but very large finite core | \pageref{eq:8.9} |
| (8.10) | Energy-relative finite capture | \pageref{eq:8.10} |
| (8.11) | Energy-relative finite capture | \pageref{eq:8.11} |
| (8.12) | Energy-relative finite capture | \pageref{eq:8.12} |
| (8.13) | Energy-relative finite capture | \pageref{eq:8.13} |
| (8.14) | A local complete inverse has a rapidly convergent expansion | \pageref{eq:8.14} |
| (8.15) | A local complete inverse has a rapidly convergent expansion | \pageref{eq:8.15} |
| (8.16) | A local complete inverse has a rapidly convergent expansion | \pageref{eq:8.16} |
| (8.17) | Paying that source-amplified error | \pageref{eq:8.17} |
| (8.18) | Paying that source-amplified error | \pageref{eq:8.18} |
| (8.19) | Paying that source-amplified error | \pageref{eq:8.19} |
| (8.20) | Paying that source-amplified error | \pageref{eq:8.20} |
| (8.21) | Paying that source-amplified error | \pageref{eq:8.21} |

## Chapter 9: Literal arithmetic: carries, generators, and frames

| Equation | Context | Page |
|---|---|---:|
| (9.1) | Why integer labels alone do not identify a physical map | \pageref{eq:9.1} |
| (9.2) | Why integer labels alone do not identify a physical map | \pageref{eq:9.2} |
| (9.3) | Why integer labels alone do not identify a physical map | \pageref{eq:9.3} |
| (9.4) | Reflection and old support after changing aperture | \pageref{eq:9.4} |
| (9.5) | Reflection and old support after changing aperture | \pageref{eq:9.5} |
| (9.6) | Reflection and old support after changing aperture | \pageref{eq:9.6} |
| (9.7) | Coefficient energy and physical fibre energy differ | \pageref{eq:9.7} |
| (9.8) | Coefficient energy and physical fibre energy differ | \pageref{eq:9.8} |
| (9.9) | A collar frame and its scope | \pageref{eq:9.9} |
| (9.10) | A collar frame and its scope | \pageref{eq:9.10} |
| (9.11) | A collar frame and its scope | \pageref{eq:9.11} |

## Chapter 10: Funding a direction rather than a whole inverse

| Equation | Context | Page |
|---|---|---:|
| (10.1) | The augmented source matrix | \pageref{eq:10.1} |
| (10.2) | Actual source fitting with a residual | \pageref{eq:10.2} |
| (10.3) | Actual source fitting with a residual | \pageref{eq:10.3} |
| (10.4) | Regular and finite-port pieces | \pageref{eq:10.4} |
| (10.5) | Regular and finite-port pieces | \pageref{eq:10.5} |
| (10.6) | Regular and finite-port pieces | \pageref{eq:10.6} |
| (10.7) | Regular and finite-port pieces | \pageref{eq:10.7} |
| (10.8) | A proved gain reduces debt only through its source overlap | \pageref{eq:10.8} |
| (10.9) | Low-energy overlap rather than a global spectral gap | \pageref{eq:10.9} |
| (10.10) | Low-energy overlap rather than a global spectral gap | \pageref{eq:10.10} |
| (10.11) | Low-energy overlap rather than a global spectral gap | \pageref{eq:10.11} |
| (10.12) | A whole-positive-block alternative | \pageref{eq:10.12} |
| (10.13) | A whole-positive-block alternative | \pageref{eq:10.13} |
| (10.14) | A whole-positive-block alternative | \pageref{eq:10.14} |

## Chapter 11: The referee sequence: repairs and the interfaces they leave

| Equation | Context | Page |
|---|---|---:|
| (11.1) | The September 24 pole extraction | \pageref{eq:11.1} |
| (11.2) | The September 24 pole extraction | \pageref{eq:11.2} |
| (11.3) | The historical freeze and the scoped G5 repair | \pageref{eq:11.3} |
| (11.4) | Why finite rank did not prove port support | \pageref{eq:11.4} |
| (11.5) | Why finite rank did not prove port support | \pageref{eq:11.5} |
| (11.6) | Why finite rank did not prove port support | \pageref{eq:11.6} |
| (11.7) | The growing-shift repair and the stale fixed-shift use | \pageref{eq:11.7} |
| (11.8) | The growing-shift repair and the stale fixed-shift use | \pageref{eq:11.8} |
| (11.9) | The growing-shift repair and the stale fixed-shift use | \pageref{eq:11.9} |
| (11.10) | The actual unweighted centered-norm obstruction | \pageref{eq:11.10} |

## Chapter 12: Exponential detection on the full test space

| Equation | Context | Page |
|---|---|---:|
| (12.1) | The spectral pairing must retain conjugation correctly | \pageref{eq:12.1} |
| (12.2) | The spectral pairing must retain conjugation correctly | \pageref{eq:12.2} |
| (12.3) | Selecting a quartet without a rightmost-zero assumption | \pageref{eq:12.3} |
| (12.4) | A sign-controlled spectral test | \pageref{eq:12.4} |
| (12.5) | A sign-controlled spectral test | \pageref{eq:12.5} |
| (12.6) | Compact support and exact pole neutralization | \pageref{eq:12.6} |
| (12.7) | Compact support and exact pole neutralization | \pageref{eq:12.7} |
| (12.8) | Compact support and exact pole neutralization | \pageref{eq:12.8} |
| (12.9) | Compact support and exact pole neutralization | \pageref{eq:12.9} |

## Chapter 13: Finite Euler algebra and the surviving bilinear sum

| Equation | Context | Page |
|---|---|---:|
| (13.1) | Exact finite convolution before compression | \pageref{eq:13.1} |
| (13.2) | Exact finite convolution before compression | \pageref{eq:13.2} |
| (13.3) | Exact finite convolution before compression | \pageref{eq:13.3} |
| (13.4) | Exact finite convolution before compression | \pageref{eq:13.4} |
| (13.5) | One-prime Poisson cancellation and weighted rows | \pageref{eq:13.5} |
| (13.6) | One-prime Poisson cancellation and weighted rows | \pageref{eq:13.6} |
| (13.7) | One-prime Poisson cancellation and weighted rows | \pageref{eq:13.7} |
| (13.8) | One-prime Poisson cancellation and weighted rows | \pageref{eq:13.8} |
| (13.9) | Largest-prime decomposition and its domain | \pageref{eq:13.9} |
| (13.10) | Exact pole neutrality pays the Type I main terms | \pageref{eq:13.10} |
| (13.11) | Exact pole neutrality pays the Type I main terms | \pageref{eq:13.11} |
| (13.12) | Exact pole neutrality pays the Type I main terms | \pageref{eq:13.12} |
| (13.13) | Exact pole neutrality pays the Type I main terms | \pageref{eq:13.13} |
| (13.14) | Exact pole neutrality pays the Type I main terms | \pageref{eq:13.14} |
| (13.15) | Exact pole neutrality pays the Type I main terms | \pageref{eq:13.15} |
| (13.16) | Exact pole neutrality pays the Type I main terms | \pageref{eq:13.16} |
| (13.17) | Young atoms: a separate local budget | \pageref{eq:13.17} |

## Chapter 14: Coherent rational interactions and harmonic boundary data

| Equation | Context | Page |
|---|---|---:|
| (14.1) | A fixed source does not pay a collar-count factor | \pageref{eq:14.1} |
| (14.2) | A fixed source does not pay a collar-count factor | \pageref{eq:14.2} |
| (14.3) | A fixed source does not pay a collar-count factor | \pageref{eq:14.3} |
| (14.4) | A fixed source does not pay a collar-count factor | \pageref{eq:14.4} |
| (14.5) | Exact Blaschke-adapted centering | \pageref{eq:14.5} |
| (14.6) | Exact Blaschke-adapted centering | \pageref{eq:14.6} |
| (14.7) | Exact Blaschke-adapted centering | \pageref{eq:14.7} |
| (14.8) | A compact exact representation of actual sine matrices | \pageref{eq:14.8} |
| (14.9) | A compact exact representation of actual sine matrices | \pageref{eq:14.9} |
| (14.10) | A compact exact representation of actual sine matrices | \pageref{eq:14.10} |
| (14.11) | A compact exact representation of actual sine matrices | \pageref{eq:14.11} |
| (14.12) | Rank-two displacement, not rank-two matrix | \pageref{eq:14.12} |
| (14.13) | Rank-two displacement, not rank-two matrix | \pageref{eq:14.13} |
| (14.14) | Rank-two displacement, not rank-two matrix | \pageref{eq:14.14} |
| (14.15) | Rank-two displacement, not rank-two matrix | \pageref{eq:14.15} |
| (14.16) | The structure survives a complete coordinate Schur step | \pageref{eq:14.16} |
| (14.17) | The structure survives a complete coordinate Schur step | \pageref{eq:14.17} |
| (14.18) | The structure survives a complete coordinate Schur step | \pageref{eq:14.18} |

## Chapter 15: A fixed pair of packets and the complete zero response

| Equation | Context | Page |
|---|---|---:|
| (15.1) | Building one test with no off-axis blind spot | \pageref{eq:15.1} |
| (15.2) | Building one test with no off-axis blind spot | \pageref{eq:15.2} |
| (15.3) | Two packets in the actual physical norm | \pageref{eq:15.3} |
| (15.4) | Two packets in the actual physical norm | \pageref{eq:15.4} |
| (15.5) | Two packets in the actual physical norm | \pageref{eq:15.5} |
| (15.6) | Two packets in the actual physical norm | \pageref{eq:15.6} |
| (15.7) | The spectral exponential series | \pageref{eq:15.7} |
| (15.8) | The spectral exponential series | \pageref{eq:15.8} |
| (15.9) | The spectral exponential series | \pageref{eq:15.9} |
| (15.10) | Gaussian isolation of a dominant contribution | \pageref{eq:15.10} |
| (15.11) | Gaussian isolation of a dominant contribution | \pageref{eq:15.11} |
| (15.12) | One sign and integrated mass also suffice | \pageref{eq:15.12} |
| (15.13) | One sign and integrated mass also suffice | \pageref{eq:15.13} |
| (15.14) | Sparse apertures and the quantitative implication | \pageref{eq:15.14} |

## Chapter 16: Prime excess, square bias, and unconditional smoothing bounds

| Equation | Context | Page |
|---|---|---:|
| (16.1) | The exact centered prime window | \pageref{eq:16.1} |
| (16.2) | The exact centered prime window | \pageref{eq:16.2} |
| (16.3) | The exact centered prime window | \pageref{eq:16.3} |
| (16.4) | Removing higher prime powers without losing the bias | \pageref{eq:16.4} |
| (16.5) | Removing higher prime powers without losing the bias | \pageref{eq:16.5} |
| (16.6) | Removing higher prime powers without losing the bias | \pageref{eq:16.6} |
| (16.7) | Removing higher prime powers without losing the bias | \pageref{eq:16.7} |
| (16.8) | A one-sided averaged endpoint | \pageref{eq:16.8} |
| (16.9) | A one-sided averaged endpoint | \pageref{eq:16.9} |
| (16.10) | What unconditional zero-free information gives for this observable | \pageref{eq:16.10} |
| (16.11) | What unconditional zero-free information gives for this observable | \pageref{eq:16.11} |
| (16.12) | What unconditional zero-free information gives for this observable | \pageref{eq:16.12} |

## Chapter 17: Divisor covariance and the subcritical sieve obstruction

| Equation | Context | Page |
|---|---|---:|
| (17.1) | An arithmetic covariance with a tractable inverse | \pageref{eq:17.1} |
| (17.2) | An arithmetic covariance with a tractable inverse | \pageref{eq:17.2} |
| (17.3) | An arithmetic covariance with a tractable inverse | \pageref{eq:17.3} |
| (17.4) | An arithmetic covariance with a tractable inverse | \pageref{eq:17.4} |
| (17.5) | An arithmetic covariance with a tractable inverse | \pageref{eq:17.5} |
| (17.6) | Keeping synthesis explicit | \pageref{eq:17.6} |
| (17.7) | Keeping synthesis explicit | \pageref{eq:17.7} |
| (17.8) | Keeping synthesis explicit | \pageref{eq:17.8} |
| (17.9) | The standard quadratic majorant | \pageref{eq:17.9} |
| (17.10) | The standard quadratic majorant | \pageref{eq:17.10} |
| (17.11) | The standard quadratic majorant | \pageref{eq:17.11} |
| (17.12) | The standard quadratic majorant | \pageref{eq:17.12} |
| (17.13) | Why more coefficient optimization cannot fix this scale | \pageref{eq:17.13} |
| (17.14) | Why more coefficient optimization cannot fix this scale | \pageref{eq:17.14} |
| (17.15) | Why more coefficient optimization cannot fix this scale | \pageref{eq:17.15} |
| (17.16) | The exact remainder short | \pageref{eq:17.16} |

## Chapter 18: Exact composite cancellation and the quarter-surplus theorem

| Equation | Context | Page |
|---|---|---:|
| (18.1) | A finite logarithm in the divisibility algebra | \pageref{eq:18.1} |
| (18.2) | A finite logarithm in the divisibility algebra | \pageref{eq:18.2} |
| (18.3) | A cutoff that includes every proper divisor | \pageref{eq:18.3} |
| (18.4) | A cutoff that includes every proper divisor | \pageref{eq:18.4} |
| (18.5) | A cutoff that includes every proper divisor | \pageref{eq:18.5} |
| (18.6) | A cutoff that includes every proper divisor | \pageref{eq:18.6} |
| (18.7) | Why the quarter cannot be optimized away | \pageref{eq:18.7} |
| (18.8) | Why the quarter cannot be optimized away | \pageref{eq:18.8} |
| (18.9) | Why the quarter cannot be optimized away | \pageref{eq:18.9} |
| (18.10) | Why the quarter cannot be optimized away | \pageref{eq:18.10} |
| (18.11) | The centered comparison that remains | \pageref{eq:18.11} |
| (18.12) | The centered comparison that remains | \pageref{eq:18.12} |
| (18.13) | The conditional negative margin | \pageref{eq:18.13} |

## Chapter 19: The theta coefficients and the single-Hankel theorem

| Equation | Context | Page |
|---|---|---:|
| (19.1) | The complete theta kernel | \pageref{eq:19.1} |
| (19.2) | The complete theta kernel | \pageref{eq:19.2} |
| (19.3) | The complete theta kernel | \pageref{eq:19.3} |
| (19.4) | The complete theta kernel | \pageref{eq:19.4} |
| (19.5) | The complete theta kernel | \pageref{eq:19.5} |
| (19.6) | One all-rank family suffices | \pageref{eq:19.6} |
| (19.7) | One all-rank family suffices | \pageref{eq:19.7} |
| (19.8) | Integer multiplicities become automatic only at the limit | \pageref{eq:19.8} |
| (19.9) | Integer multiplicities become automatic only at the limit | \pageref{eq:19.9} |
| (19.10) | The next actual pivot | \pageref{eq:19.10} |
| (19.11) | The next actual pivot | \pageref{eq:19.11} |

## Chapter 20: Positive prefixes and uniform analytic transfer

| Equation | Context | Page |
|---|---|---:|
| (20.1) | Entire approximants with prescribed zero geometry | \pageref{eq:20.1} |
| (20.2) | Entire approximants with prescribed zero geometry | \pageref{eq:20.2} |
| (20.3) | Entire approximants with prescribed zero geometry | \pageref{eq:20.3} |
| (20.4) | Finite positive models from actual moments | \pageref{eq:20.4} |
| (20.5) | Finite positive models from actual moments | \pageref{eq:20.5} |
| (20.6) | Polynomial rather than exponential models | \pageref{eq:20.6} |
| (20.7) | Polynomial rather than exponential models | \pageref{eq:20.7} |
| (20.8) | Fractional exponents enlarge the feasible class | \pageref{eq:20.8} |
| (20.9) | Fractional exponents enlarge the feasible class | \pageref{eq:20.9} |
| (20.10) | Fractional exponents enlarge the feasible class | \pageref{eq:20.10} |
| (20.11) | A positive resolvent from finite moments | \pageref{eq:20.11} |
| (20.12) | A positive resolvent from finite moments | \pageref{eq:20.12} |
| (20.13) | A positive resolvent from finite moments | \pageref{eq:20.13} |

## Chapter 21: Moment correction, canonical coordinates, and collision-free paths

| Equation | Context | Page |
|---|---|---:|
| (21.1) | A flow preserving the matched prefix | \pageref{eq:21.1} |
| (21.2) | A flow preserving the matched prefix | \pageref{eq:21.2} |
| (21.3) | A flow preserving the matched prefix | \pageref{eq:21.3} |
| (21.4) | A flow preserving the matched prefix | \pageref{eq:21.4} |
| (21.5) | The next-moment budget | \pageref{eq:21.5} |
| (21.6) | The next-moment budget | \pageref{eq:21.6} |
| (21.7) | Canonical coordinates measure feasibility directly | \pageref{eq:21.7} |
| (21.8) | Canonical coordinates measure feasibility directly | \pageref{eq:21.8} |
| (21.9) | Canonical coordinates measure feasibility directly | \pageref{eq:21.9} |
| (21.10) | Canonical coordinates measure feasibility directly | \pageref{eq:21.10} |
| (21.11) | Canonical coordinates measure feasibility directly | \pageref{eq:21.11} |
| (21.12) | Canonical coordinates measure feasibility directly | \pageref{eq:21.12} |
| (21.13) | Paying the old deficit by moving measures | \pageref{eq:21.13} |
| (21.14) | Paying the old deficit by moving measures | \pageref{eq:21.14} |
| (21.15) | Paying the old deficit by moving measures | \pageref{eq:21.15} |

## Chapter 22: Heat evolution and the controls that defeat naive induction

| Equation | Context | Page |
|---|---|---:|
| (22.1) | Exact evolution of the logarithmic moments | \pageref{eq:22.1} |
| (22.2) | Exact evolution of the logarithmic moments | \pageref{eq:22.2} |
| (22.3) | Exact evolution of the logarithmic moments | \pageref{eq:22.3} |
| (22.4) | Exact evolution of the logarithmic moments | \pageref{eq:22.4} |
| (22.5) | Exact evolution of the logarithmic moments | \pageref{eq:22.5} |
| (22.6) | Exact evolution of the logarithmic moments | \pageref{eq:22.6} |
| (22.7) | The complete negative-heat control | \pageref{eq:22.7} |
| (22.8) | The complete negative-heat control | \pageref{eq:22.8} |
| (22.9) | Finite theta truncations lose a boundary cancellation | \pageref{eq:22.9} |
| (22.10) | Finite theta truncations lose a boundary cancellation | \pageref{eq:22.10} |
| (22.11) | Finite theta truncations lose a boundary cancellation | \pageref{eq:22.11} |

## Chapter 23: A direct coefficient kernel and the limits of probabilistic positivity

| Equation | Context | Page |
|---|---|---:|
| (23.1) | Avoiding the logarithmic recurrence in matrix assembly | \pageref{eq:23.1} |
| (23.2) | Avoiding the logarithmic recurrence in matrix assembly | \pageref{eq:23.2} |
| (23.3) | Avoiding the logarithmic recurrence in matrix assembly | \pageref{eq:23.3} |
| (23.4) | Avoiding the logarithmic recurrence in matrix assembly | \pageref{eq:23.4} |
| (23.5) | Numerical value without a new sign theorem | \pageref{eq:23.5} |
| (23.6) | Numerical value without a new sign theorem | \pageref{eq:23.6} |
| (23.7) | Complete monotonicity of the reciprocal is weaker | \pageref{eq:23.7} |
| (23.8) | Complete monotonicity of the reciprocal is weaker | \pageref{eq:23.8} |

## Chapter 24: Boundary absorption: the first Schur gate

| Equation | Context | Page |
|---|---|---:|
| (24.1) | The three adjacent shapes | \pageref{eq:24.1} |
| (24.2) | The three adjacent shapes | \pageref{eq:24.2} |
| (24.3) | Hook-content evaluation and the forced roots | \pageref{eq:24.3} |
| (24.4) | Hook-content evaluation and the forced roots | \pageref{eq:24.4} |
| (24.5) | Hook-content evaluation and the forced roots | \pageref{eq:24.5} |
| (24.6) | Degree cancellation completes the factorization | \pageref{eq:24.6} |
| (24.7) | Degree cancellation completes the factorization | \pageref{eq:24.7} |
| (24.8) | Degree cancellation completes the factorization | \pageref{eq:24.8} |

## Chapter 25: Reciprocal pairs and the flagged reservoir

| Equation | Context | Page |
|---|---|---:|
| (25.1) | Row entries before determinant expansion | \pageref{eq:25.1} |
| (25.2) | Row entries before determinant expansion | \pageref{eq:25.2} |
| (25.3) | Row entries before determinant expansion | \pageref{eq:25.3} |
| (25.4) | Row entries before determinant expansion | \pageref{eq:25.4} |
| (25.5) | A counting convention that matters | \pageref{eq:25.5} |
| (25.6) | A counting convention that matters | \pageref{eq:25.6} |
| (25.7) | A counting convention that matters | \pageref{eq:25.7} |
| (25.8) | What the finite positivity theorem actually controls | \pageref{eq:25.8} |
| (25.9) | What the finite positivity theorem actually controls | \pageref{eq:25.9} |

## Chapter 26: Cocircuits, finite chains, and forced-root skeletons

| Equation | Context | Page |
|---|---|---:|
| (26.1) | The fourth-order difference hidden in the boundary | \pageref{eq:26.1} |
| (26.2) | The fourth-order difference hidden in the boundary | \pageref{eq:26.2} |
| (26.3) | Coefficient targets and derivative layers | \pageref{eq:26.3} |
| (26.4) | Coefficient targets and derivative layers | \pageref{eq:26.4} |

## Chapter 27: Prefix residuals and rising-factorial positivity

| Equation | Context | Page |
|---|---|---:|
| (27.1) | The residual and the two factorial bases | \pageref{eq:27.1} |
| (27.2) | The residual and the two factorial bases | \pageref{eq:27.2} |
| (27.3) | The residual and the two factorial bases | \pageref{eq:27.3} |
| (27.4) | Four layers, not the whole polynomial | \pageref{eq:27.4} |
| (27.5) | Four layers, not the whole polynomial | \pageref{eq:27.5} |

## Chapter 28: Boundary ladders and a finite Sturm mechanism

| Equation | Context | Page |
|---|---|---:|
| (28.1) | One signed remainder | \pageref{eq:28.1} |
| (28.2) | One signed remainder | \pageref{eq:28.2} |
| (28.3) | Transport to the next pair | \pageref{eq:28.3} |
| (28.4) | Transport to the next pair | \pageref{eq:28.4} |
| (28.5) | The exact third-order minor | \pageref{eq:28.5} |
| (28.6) | The exact third-order minor | \pageref{eq:28.6} |
| (28.7) | From local propagation to vertical interlacing | \pageref{eq:28.7} |

## Chapter 29: Vertical proper position and the Jensen Wronskian

| Equation | Context | Page |
|---|---|---:|
| (29.1) | Three identities with one normalization | \pageref{eq:29.1} |
| (29.2) | The polar-derivative theorem | \pageref{eq:29.2} |
| (29.3) | The polar-derivative theorem | \pageref{eq:29.3} |
| (29.4) | The polar-derivative theorem | \pageref{eq:29.4} |
| (29.5) | The coefficient-side Wronskian | \pageref{eq:29.5} |
| (29.6) | The coefficient-side Wronskian | \pageref{eq:29.6} |

## Chapter 30: The centered heat model and its exact gap barrier

| Equation | Context | Page |
|---|---|---:|
| (30.1) | The finite heat polynomial | \pageref{eq:30.1} |
| (30.2) | The finite heat polynomial | \pageref{eq:30.2} |
| (30.3) | The finite heat polynomial | \pageref{eq:30.3} |
| (30.4) | The hyperbolic root equation | \pageref{eq:30.4} |
| (30.5) | The hyperbolic root equation | \pageref{eq:30.5} |
| (30.6) | The hyperbolic root equation | \pageref{eq:30.6} |
| (30.7) | A quantitative reserve | \pageref{eq:30.7} |
| (30.8) | Which perturbations actually move a gap? | \pageref{eq:30.8} |
| (30.9) | Which perturbations actually move a gap? | \pageref{eq:30.9} |

## Chapter 31: Saddle chambers, Airy edges, and Paper IX

| Equation | Context | Page |
|---|---|---:|
| (31.1) | The saddle-spacing mechanism | \pageref{eq:31.1} |
| (31.2) | The early hard-window profile | \pageref{eq:31.2} |
| (31.3) | Coalescing saddles and the Airy scale | \pageref{eq:31.3} |
| (31.4) | The later v442 frontier is a different record | \pageref{eq:31.4} |

## Chapter 32: Preserving operators and the actual-coefficient transfer tests

| Equation | Context | Page |
|---|---|---:|
| (32.1) | One-sided transfer at critical points | \pageref{eq:32.1} |
| (32.2) | Why arbitrarily many standard Jacobi factors do not fix the fit | \pageref{eq:32.2} |
| (32.3) | An Euler escape and its failure at degree eight | \pageref{eq:32.3} |
| (32.4) | The broader Pólya–Schur symbol | \pageref{eq:32.4} |
| (32.5) | The broader Pólya–Schur symbol | \pageref{eq:32.5} |
| (32.6) | A second obstruction forces the Laguerre scale to grow | \pageref{eq:32.6} |
| (32.7) | A second obstruction forces the Laguerre scale to grow | \pageref{eq:32.7} |

## Chapter 33: The self-layer-cake and Jacobi–CMV route

| Equation | Context | Page |
|---|---|---:|
| (33.1) | Smoothing the logarithmic moments | \pageref{eq:33.1} |
| (33.2) | Smoothing the logarithmic moments | \pageref{eq:33.2} |
| (33.3) | Smoothing the logarithmic moments | \pageref{eq:33.3} |
| (33.4) | Infinite-order smoothing without an artificial heat anchor | \pageref{eq:33.4} |

## Chapter 34: The fixed-base prime-Hausdorff criterion

| Equation | Context | Page |
|---|---|---:|
| (34.1) | Fix the base once | \pageref{eq:34.1} |
| (34.2) | Fix the base once | \pageref{eq:34.2} |
| (34.3) | Literal finite prime-power stages | \pageref{eq:34.3} |
| (34.4) | Literal finite prime-power stages | \pageref{eq:34.4} |
| (34.5) | Reverse-Bessel prime impulses | \pageref{eq:34.5} |
| (34.6) | Why unbounded depth is exactly the missing statement | \pageref{eq:34.6} |

## Chapter 35: Canonical walls, trace constraints, and the two-defect geometry

| Equation | Context | Page |
|---|---|---:|
| (35.1) | The formal Wall lattice and its boundary at infinity | \pageref{eq:35.1} |
| (35.2) | The lower-Hankel quotient | \pageref{eq:35.2} |
| (35.3) | Why the harmonic tube must remain retired | \pageref{eq:35.3} |
| (35.4) | The exceptional pair and resonance | \pageref{eq:35.4} |

## Chapter 36: Exact mature transport and the corrected off-resonance chart

| Equation | Context | Page |
|---|---|---:|
| (36.1) | The width is $x-1$, not the resonance proxy | \pageref{eq:36.1} |
| (36.2) | The width is $x-1$, not the resonance proxy | \pageref{eq:36.2} |
| (36.3) | The width is $x-1$, not the resonance proxy | \pageref{eq:36.3} |
| (36.4) | An exact resonance-defect integral | \pageref{eq:36.4} |
| (36.5) | An exact resonance-defect integral | \pageref{eq:36.5} |
| (36.6) | Saddle desingularization and the BR estimate | \pageref{eq:36.6} |
| (36.7) | PREFIX-51 and the concrete constants | \pageref{eq:36.7} |
| (36.8) | PREFIX-51 and the concrete constants | \pageref{eq:36.8} |

## Chapter 37: Endpoint Christoffel transport and the later RESET sequence

| Equation | Context | Page |
|---|---|---:|
| (37.1) | The endpoint transform and its seed | \pageref{eq:37.1} |
| (37.2) | The endpoint transform and its seed | \pageref{eq:37.2} |
| (37.3) | The endpoint transform and its seed | \pageref{eq:37.3} |
| (37.4) | Equilibrium residue and physical residue are different | \pageref{eq:37.4} |
| (37.5) | The same-index determinant map | \pageref{eq:37.5} |
| (37.6) | The same-index determinant map | \pageref{eq:37.6} |
| (37.7) | What F166.85A actually settles | \pageref{eq:37.7} |

## Chapter 38: Cube-only protection, amplitude control, and the remaining invariant

| Equation | Context | Page |
|---|---|---:|
| (38.1) | A relative light cone from the cube alone | \pageref{eq:38.1} |
| (38.2) | A relative light cone from the cube alone | \pageref{eq:38.2} |
| (38.3) | A summable tail makes the amplitude hypothesis eventual | \pageref{eq:38.3} |
| (38.4) | A summable tail makes the amplitude hypothesis eventual | \pageref{eq:38.4} |

## Chapter 39: Native finite sections: what the mesh really certifies

| Equation | Context | Page |
|---|---|---:|
| (39.1) | The Toeplitz-minus-Hankel core | \pageref{eq:39.1} |
| (39.2) | The Toeplitz-minus-Hankel core | \pageref{eq:39.2} |
| (39.3) | A terminal matrix contains all earlier prefixes | \pageref{eq:39.3} |
| (39.4) | A terminal matrix contains all earlier prefixes | \pageref{eq:39.4} |
| (39.5) | W200 as a local theorem | \pageref{eq:39.5} |

## Chapter 40: RESET, Riccati energy, and the distinguished source

| Equation | Context | Page |
|---|---|---:|
| (40.1) | The fine/coarse identity | \pageref{eq:40.1} |
| (40.2) | The fine/coarse identity | \pageref{eq:40.2} |
| (40.3) | A useful local summability theorem | \pageref{eq:40.3} |
| (40.4) | A useful local summability theorem | \pageref{eq:40.4} |
| (40.5) | Why the residual, not a raw cross norm, matters | \pageref{eq:40.5} |
| (40.6) | A trial image and its exact transverse defect | \pageref{eq:40.6} |
| (40.7) | A trial image and its exact transverse defect | \pageref{eq:40.7} |
| (40.8) | A trial image and its exact transverse defect | \pageref{eq:40.8} |

## Chapter 41: Weyl functions, canonical systems, and positive realizations

| Equation | Context | Page |
|---|---|---:|
| (41.1) | Cauer factorization and discrete supersymmetry | \pageref{eq:41.1} |
| (41.2) | Cauer factorization and discrete supersymmetry | \pageref{eq:41.2} |

## Chapter 42: Orthogonal folds, Hardy norms, and cutoff-free arithmetic

| Equation | Context | Page |
|---|---|---:|
| (42.1) | Bernstein energy and its Laguerre realization | \pageref{eq:42.1} |
| (42.2) | The Joukowski change of geometry | \pageref{eq:42.2} |
| (42.3) | The Joukowski change of geometry | \pageref{eq:42.3} |
| (42.4) | The Joukowski change of geometry | \pageref{eq:42.4} |
| (42.5) | The global Hardy function and its unresolved estimate | \pageref{eq:42.5} |
| (42.6) | The co-Poisson identity preserves a different tail | \pageref{eq:42.6} |

## Chapter 43: A killed jump process and order-sensitive arithmetic paths

| Equation | Context | Page |
|---|---|---:|
| (43.1) | An exact representation of the raw operator | \pageref{eq:43.1} |
| (43.2) | An exact representation of the raw operator | \pageref{eq:43.2} |
| (43.3) | An exact representation of the raw operator | \pageref{eq:43.3} |
| (43.4) | A complete path needs its occupation information | \pageref{eq:43.4} |
| (43.5) | A complete path needs its occupation information | \pageref{eq:43.5} |
| (43.6) | A complete path needs its occupation information | \pageref{eq:43.6} |
| (43.7) | Two identical prime products can have different boundary effects | \pageref{eq:43.7} |
| (43.8) | The completed pole remains a separate perturbation | \pageref{eq:43.8} |

## Chapter 44: Gauges, implicit steps, and what a change of coordinates cannot improve

| Equation | Context | Page |
|---|---|---:|
| (44.1) | The physical metric travels with the coordinates | \pageref{eq:44.1} |
| (44.2) | A moving frame has a connection term | \pageref{eq:44.2} |
| (44.3) | A real Cayley transform records the sign exactly | \pageref{eq:44.3} |
| (44.4) | Displacement structure survives an implicit step | \pageref{eq:44.4} |
| (44.5) | Displacement structure survives an implicit step | \pageref{eq:44.5} |
| (44.6) | Why unrestricted storage existence is not a new estimate | \pageref{eq:44.6} |

## Chapter 45: Transported observations, reflection geometry, and arithmetic polarization

| Equation | Context | Page |
|---|---|---:|
| (45.1) | A genuine damping estimate | \pageref{eq:45.1} |
| (45.2) | Even exact modular symmetry has a counter-control | \pageref{eq:45.2} |
| (45.3) | Selberg amplitudes and a fermionic correction | \pageref{eq:45.3} |

## Chapter 47: Cross-era connections and the missing identifications

| Equation | Context | Page |
|---|---|---:|
| (47.1) | RESET and complete source funding | \pageref{eq:47.1} |
| (47.2) | Three cubic mechanisms, three different meanings | \pageref{eq:47.2} |

## Chapter 49: The current working frontier

| Equation | Context | Page |
|---|---|---:|
| (49.1) | The physical target, without unnecessary strengthening | \pageref{eq:49.1} |
| (49.2) | The independent all-rank target | \pageref{eq:49.2} |

[plate-arithmetic-windows]: figures/plate-arithmetic-windows.png
[plate-detector-phase]: figures/plate-detector-phase.png
[plate-gaussian-envelope]: figures/plate-gaussian-envelope.png
[plate-heat-collision]: figures/plate-heat-collision.png
