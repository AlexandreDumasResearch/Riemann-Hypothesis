# 01 — Analytic and geometric ledger
Alexandre Dumas · ORCID 0009-0003-1695-0086 · 2026-11-27

## 1. Scales and source interfaces (S)
Let E be CM of degree 2f, v one of each conjugate pair; n=ρ+1, K=k−n^7, k=r+1−m, m≈√x, r≈x^5, n^9=O(x^4.5). For depth a=0,…,ρ set
$$s(v,a)=|\kappa_v|^{2(\rho-a)}/N,\quad \mathscr K=\prod_v|\kappa_v|=(M\,rd(E)/(2\pi))^f.$$
Hence $\prod_v s(v,a)=\mathscr K^{2(\rho-a)}/N^f$, adjacent ratio $\mathscr K^{-2}$, head prefix product $C_j=\mathscr K^{j(2\rho-j+1)}/N^{fj}$.
Poisson normalization $P_a=c_E N^{2f}/\mathscr K^{4(\rho-a)}$, $\Pi_j=\prod_{a<j}P_a$. Source: New/Spanning/MainTerm/GlobalSieve.lean, frequency_term_le, sum_frequencies_le, boundsDecay_prod, densitySum_succ_le_mul_densitySum_add. Exact frequency constants and normalization must be checked when transplanting any estimate.

## 2. Adelic norm exclusion and anisotropic ideal packing (A1, E)
Let d be a nonzero integral ideal, $R_v>0$, $V=N\mathfrak d\prod R_v^2$. For nonzero $\nu\in\mathfrak d^{-1}$, $\prod|\nu_v|^2=|N_{E/\mathbf Q}\nu|\ge1/N\mathfrak d$. Thus no nonzero point occurs in $|\nu_v|\le R_v$ if V<1. Rescale by R_v; any distinct points have max-norm separation at least $V^{-1/(2f)}$. Disjoint balls of half that radius fit in an expanded unit ball in real dimension 2f. For V≥1:
$$\#\{\nu\ne0: \nu\in\mathfrak d^{-1},|\nu_v|\le R_v\}\le (1+2V^{1/(2f)})^{2f}\le9^f V.$$
The bound also holds for V<1 (zero). In particular it is ≤$9^fV^{1+\eta}$ for $0\le\eta<1$. No embedding independence or field-dependent lattice basis required. Classical multiplicative lattice separation; see Skriganov, Barroero–Widmer, Widmer for precedent. Specific application to the pinned sieve not claimed unprecedented.

Arithmetic uncertainty interpretation: for $y_v=|\nu_v|/s(v,a)$, $\prod y_v\ge N^f/(\mathscr K^{2(\rho-a)}\sqrt{N\mathfrak d(\nu)})$ and $\sum y_v^2\ge f(\prod y_v)^{2/f}$. Denominator growth defeats an unrestricted exclusion claim (ν=1/L).

## 3. Exact product cancellation and S-unit resonance (E/S)
At admissible frequencies integral outside T, $\nu=(t^{-1}-s^{-1})/M$, define $I_{\rm out}=\prod_{\mathfrak p\notin T}N\mathfrak p^{v_\mathfrak p(\nu)}$. The finite-place genIndex factor and infinite decay cancel:
$$\operatorname{genIndex}_T(\nu)^{K/2}/\prod_v|\nu_v|^K=I_{\rm out}^{-K/2}.$$
The remaining majorant is of form $A Q^K I_{\rm out}^{-K/2}(N\mathfrak d(\nu))^{-3}\prod_v\min(1,(q_v/|\nu_v|)^6)$ with $q_v=s(v,a)/|c_v|$, $Q=\prod q_v$ and A the source normalization. Earlier inverse-height bound uses $H=N\mathfrak d(\nu)\prod\max(1,|\nu_v|)^2$ when the scale bounds justify it; do not assume arbitrary q_v≤1.

When t,s,M are T-units, $I_{\rm out}=1$ iff s−t is a T-unit, so t/s+(s−t)/s=1. Beukers–Schlickewei bound ≤$2^{8(2r_T+1)}$ for the rank-$2r_T$ product group, $r_T=f-1+|T|$. Weighted graph bound $\sum_{t\sim s}W_tW_s\le\Delta_T\sum W_t^2$ follows from 2ab≤a²+b². Nonresonant factor ≤$2^{-K/2}$. Under the uniform height majorant, with $L_T=\sum H(\nu)^{-3}$, $\mathcal O_a\le C_a[\min(\Delta_T,L_T)+2^{-K/2}L_T]\sum W_t^2$. X: T may be large or enlarged, and this graph bound may be weaker than the original height sum. Retain as alternate, not a necessary proof route.

## 4. Packing-integrated Bessel estimate (A2, E conditional on actual majorant)
The exact layer-cake identity $\min(1,r^{-6})=\int_1^\infty6u^{-7}\mathbf1_{r\le u}\,du$ lets us count before integration. At fixed denominator d, Tonelli and A1 give
$$\sum_{\mathfrak d(\nu)=\mathfrak d,\nu\ne0}\prod_v\min(1,(q_v/|\nu_v|)^6)
\le 9^f(N\mathfrak d)^{1+\eta} Q^{2+2\eta}(6/(4-2\eta))^f.$$
Dropping the favorable I_out factor and summing ideals by $\zeta_E(2-\eta)\le\zeta(2-\eta)^{2f}$ yields the star equation
$$\boxed{\sum_{\nu\ne0}\beta_a(\nu)\le A C_\eta^f Q^{K+2+2\eta},\qquad C_\eta={54\over4-2\eta}\zeta(2-\eta)^2.}$$
η=0 gives 37^f; η→1 does not give the endpoint with bounded constant. If Q>1, extra exponent need not improve. Source Bessel decay is NOT independently proved here. The packing method also covers anisotropic embedding scales.

Poisson and reciprocal scale candidates: $Q_a^P=\mathscr K^{2(\rho-a)+1}/(MN)^f$, $Q_a^O=\mathscr K^{2(\rho-a)}/(MN)^f$; provided all actual local factors admit these q_v majorants, $\mathcal E_a^P\le\mathcal E'_0\mathscr K^{-2a(K+2)}$, $\mathcal E_a^O\le\mathcal E'_0\mathscr K^{-(2a+1)(K+2)}$. Exact product does not alone justify replacing individual min factors by these scales.

## 5. Weighted convolution and depth-resolved sieve (A3)
Group actual head weights W_t by last reciprocal coordinate z=t^{-1}/M. Cauchy–Schwarz gives $\sum_z w(z)w(z-\nu)\le\sum_z w(z)^2$ and therefore $\mathcal O_a\le(\sum_{\nu\ne0}F_a(\nu))\sum W_t^2$ for any summable nonnegative uniform frequency majorant. Effective occupancy $(\sum W)^2/\sum W^2$. No independent-head hypothesis.
With q=𝒦^{-K}, earlier conditional normalized recurrence:
$$D_{i+1}/\Pi_{i+1}\le D_i/\Pi_i+\Gamma_i\mathcal E_0(q^{2i}+q^{2i-1})\quad(i\ge1).$$
First coordinate has only Poisson error. If $\Gamma_i\le b^{400n^9 f}$ and $\mathscr K\ge b^{19f}$, then $\Gamma q\le b^{f(400n^9-19K)}=b^{-\Omega(fx^5)}$, and $D_n\le\Pi_n[D_0+\mathcal E_0(1+\Gamma q/(1-q))]$. Earlier EnergyEstimate refinement proposal: replace $b^{2403n^9f}$ decayConst by $b^{2002n^9f}$ decayConst times $(1+b^{-\Omega(fx^5)})$; relative error $b^{-3kf+2003n^9f}(1+o(1))$. C: replay recurrence normalization, support and constants before claiming exact replacement.

Head support: cumulative products $\delta_j=t_0\cdots t_{j-1}$ integral, $|c_{j,v}\delta_{j,v}|\le B=b^{60n^2}$, $c_{j,v}=\prod_{a<j}s(v,a)$. Packing gives ≤$9^fB^{2f}C_j^{-2}$ points and no nonzero prefix if volume <1. Under actual prefix weight bound $B^{mf}C_j^{-m}$ (here m denotes exponent n^6, not chain length), sum heads ≤$\prod_j[9^f B^{(m+2)f} C_j^{-(m+2)}]$. Coordinate recovery by successive ratios; no independence. Check support and weights before using.

## 6. Interference and observability (A4)
For a genuine stationary positive-definite kernel $F(z_t-z_s)=\int e^{2\pi i\langle z_t-z_s,\xi\rangle}d\mu$, quadratic form equals $\int|\sum c_t e^{2\pi i\langle z_t,\xi\rangle}|^2d\mu$. C: actual kernel may not be stationary. Genuine finite character average:
$$|\widehat G|^{-1}\sum_\chi\|\sum_t\chi(r(t))a_t\|^2=\sum_g\|\sum_{r(t)=g}a_t\|^2.$$
Brox zero-Gram compact U(k) branch uses Schur orthogonality; extending to nonzero Gram is open. X: global additive character trivial on diagonal rational E, so arbitrary adelic phase averaging fails. Integral projector averaging costs |G| at dividing primes.

If two actual local kernels are Gram, their entrywise product is Gram of tensor features $u_p\otimes v_p$; normalized coherence equals product of local coherences. C: complementary arithmetic–geometric separation theorem needed; all-one Gram matrices show positivity alone gives rank one. Group conditional heads, integrate within and between classes, seek exact orthogonality before absolute bounds.

For positive Gram G of dimension D, $A=DG/\operatorname{tr}G$, $\|A-I\|_{HS}^2=D^2\operatorname{tr}G^2/(\operatorname{tr}G)^2-D$. If $\operatorname{tr}G^2\le(1+\epsilon)(\operatorname{tr}G)^2/D$, at most εD/τ² eigenvalues differ from 1 by ≥τ. Seek direct centered excess rather than subtracting two independently large estimates.

Ramified direct restriction $B_t=A_t|_{S_{\rm ram}}$, covariance ≤ full covariance; cannot infer proportional trace loss. Saturated $C_t=\min(B_t B_t^*,I)$, range equal B_t, $0\le C_t\le I$, rank(QB_t)≥tr(Q C_t Q). For average C with tr(I−C)=δ, some t recovers ≥r−δ dimensions from rank-r residual Q, provided normalization applies. From earlier manuscript deficit-transfer lemma:
$$\operatorname{tr}(QC)\ge {d_R\over D}r-d_R\sqrt{(2\delta_R+\epsilon_R)r/D}.$$
Conditional on its normalized trace-square and trace hypotheses (see original manuscript); not a generic PSD statement. Greedy choose t with at least average rank gain, iterate; original retained fraction ≥1−4/b², ramified codimension ≤f/(N−1), normalized allowance (1−α)^−2 if trace assumptions hold. ShortAndEnough.lean. Persistent measurement analogy is useful only through these exact inequalities.

## 7. Dormant and rejected routes
- Electrical Schur complement: $\det G=\det D\det(A-BD^{-1}B^*)$. Counterexample $G=[[1,\sqrt\epsilon],[\sqrt\epsilon,\epsilon]]$ gives zero effective block despite small B. Need relative coercivity, not small absolute coupling.
- Free-energy viewpoint $f\log b(19K-400n^9)$ is a useful scale test, not an independent proof.
- Gaussian detector / moving carrier, pole-neutral odd Gaussian, signed first-prime Schur, Mellin heat-trace, Jensen/Appell interlacing, fixed-carrier signed-mass, adjacent shift, cofinal Schur and W10 geometric wall remain in earlier archive. No new proof of those routes. Independent W arithmetic-window supplier remains unproved in this programme.
- Explicit-formula zero mode $x^{\beta-1/2}\cos(\gamma\log x+\phi)$ illustrates instability, not a proof of a one-sided bound for all zeros.
- Future proof obligations: first-coordinate local Fourier/Bessel estimate, global Siegel class sum and remaining Bruhat cells, actual common-scalar seesaw and integral lifts, tied Selmer, selected comparison and false-lift exclusion. Do not replace them by abstract RH equivalences.
