# 02 — Adelic determinant and Selmer ledger
Alexandre Dumas · ORCID 0009-0003-1695-0086 · 27 November 2026

## 1. Integral theta realization
Pinned New/Reduction/IntegralTargetForms.lean, Lattices/TwistedLattice.lean, Determinant/Twist/LongForms.lean, Determinant/Chain/NormOfChain.lean, OneLift/LiftVolumeHeight.lean. Integral target lattice is simultaneous pullback $L_\iota=\bigcap_\vartheta\Theta_\vartheta^{-1}M_{\vartheta,\iota}$ over allowed twists. Analytic metric supplied by untwisted lift. Common-scalar seesaw $\Theta_\vartheta \mathcal P\phi=c\mathcal T_{\vartheta,\Psi_\vartheta}\phi$ (c independent of twist/source), controlled finite chains and local gauges from SeesawIdentity and exists_err_gaugeLe_compositeLift. Need actual local divisibilities and simultaneous colength; do not replace them by independent per-vector denominators. For a lattice L with common integral sublattice L_int, determinant cost is exactly length(L/L_int) at a DVR. This principle already partly occurs in the pinned source; novelty not claimed.

## 2. Conservation and reachable defect (D1–D2)
Good lift u, gluing g, common period J, $c_\vartheta g_\vartheta^*u_\vartheta=J$. Comparison $U=Cgg^*$ integral at allowed primes, U on good lifts orthogonal to false lifts. Set A=ran u, P orthogonal projection onto A, T=P U|_A, $Z=\det(u^*u)$, $\Delta=\det T$. Source exact identity:
$$\boxed{Z_\vartheta\Delta_\vartheta=C_0\rho_\vartheta^d.}\tag{D1}$$
$\rho_\vartheta$ is the source Hecke-value ratio; C₀ common. This is not a new result. The inverse ratio is $\Delta_\vartheta/\Delta_1\cdot\rho_\vartheta^{-d}$.

At a DVR take M₀ ambient permitted lattice, $L=M_0\cap A$, $L_B=M_0\cap A^\perp$. Full projection module $\mathcal C=PM_0/L\simeq M_0/(L+L_B)$. Reachable module $\mathcal C_U=(L+TL)/L\subseteq\mathcal C$. For invertible T, comparing L and TL through their intersection gives
$$\boxed{-v(\det T)=\operatorname{length}\mathcal C_U-\operatorname{length}(L/(L\cap TL)).}\tag{D2}$$
Thus need only bound reached defects and can retain favorable signed term. From period identity $UL=(C/c_\vartheta)gJ(u^{-1}L)$. Sufficient zero loss if this image is in $L+L_B$. C: actual containment unproved. Counterexample: at ℓ=5 choose integer a with v₅(1+a²)=h by Hensel; u=(1,a)^t, g=(1,0)^t, U=gg*, Z=1+a², Δ=(1+a²)^−1. ZΔ=1 but negative projection valuation h arbitrarily large. Positivity cannot replace arithmetic.

## 3. Mixed twists and Gauss valuation (D3)
Source chain norm Gram $G_\theta=c_\theta c_{Q,\theta}^m\prod_{j=1}^m R_{j,\theta^j}$ with spherical Hecke operators. Suppose relative operators $G_1^{-1}G_\theta$ have a common spectral packet decomposition V=⊕Vπ with dim dπ and eigenvalues λπθ. Form $\mathscr D(X)=\det(\sum_\theta X_\theta G_\theta)$; this is a polynomial, not a new automorphic twist. Then
$$\mathscr D(X)=\det G_1\prod_\pi(\sum_\theta X_\theta\lambda_{\pi,\theta})^{d_\pi}.$$
Gauss valuation = minimum coefficient valuation. It is multiplicative by reducing unit-normalized polynomials modulo the maximal ideal in a domain. Hence
$$\boxed{v_G(\mathscr D)=v(\det G_1)+\sum_\pi d_\pi\min_\theta v(\lambda_{\pi,\theta}).}\tag{D3}$$
If all Gθ integral in a common basis, $v(\det G_1)\ge-\sum d_\pi\min v\lambda_{\pi,\theta}$, potentially much stronger than $-\min_\theta\sum d_\pi v\lambda_{\pi,\theta}$. Example $G_1=p^h I_2$, $G_\alpha=\operatorname{diag}(1,p^h)$, $G_\beta=\operatorname{diag}(p^h,1)$: mixed XY coefficient 1+p^{2h} unit, both pure determinants valuation h. No integral spectral projectors needed; use decomposition only to evaluate polynomial.

With common conjugate-side clearing matrices $C_{\bar\iota}^* G_\theta C_\iota$, cost $e_\iota=v(\det C_{\bar\iota}^*\det C_\iota)$, add e to D3. For d=h+c, c missing auxiliary forms, choose c_+,c_- attaining max valuations of γθ on their respective sides, cost $c(v_\iota(c_+)+v_{\bar\iota}(c_-))$, c≤4d/b². C: separate phase imbalance not controlled by $|\gamma|^2$; example γ=((2+i)/(2−i))^L has γγbar=1 but opposite valuations ±L. Common multiplier and global height of locally mixed ratios unproved; spectral compatibility must be checked on actual chain. Suspend mixed route in favor of single-twist weighted clearing. Determinant ideal redundancy example (2,3) generates ℤ although neither alone is a unit; compatible determinant lines essential.

## 4. Weighted clearing and rank deficit (D4, E/S)
Source DenominatorBound.lean, exists_linearMap_eq_smul_mem_integralForms: individual admissible good-lift generator v_i with Selmer length s_i produces diagonal clearing operator G_i with eigenvalue μ_ii satisfying $v_\ell(\mu_{ii})\le s_i+B_\ell$, $B_\ell=2t'\operatorname{ram}+r'\operatorname{loc}+\operatorname{err}$. Operators are closed under integral linear combinations. Over infinite residue field (or after permissible unramified extension), choose coefficients avoiding all leading-term cancellation hyperplanes. Then Λ diagonal, eigenvalue valuation on v_j is min_i v(μ_ij)≤s_j+B. Thus $v_\ell(\det\Lambda)\le\sum_i s_i+dB_\ell$. Add stabilizer only where integral pairings require it. No new proof of individual theorem.

For finite spanning family weighted by s(v)≥0, r(u)=dim span{v:s(v)≤u}. For any independent basis, total cost = integral of number of vectors of cost >u; this is ≥ integral(d−r(u)). Greedy retain generators by increasing cost when increasing span, achieving equality at every threshold. Thus
$$\boxed{\min_{\mathcal B}\sum_{v\in\mathcal B}s(v)=\int_0^\infty(d-r(u))du,\quad v_\ell(\det\Lambda)\le dB_\ell+\int_0^\infty(d-r_\ell(u))du.}\tag{D4}$$
Classical weighted matroid basis; application conditional on candidate family and all operators sharing the required simultaneous diagonalization. Cannot ignore infinite-cost missing direction.

Exact diagonal optimization: $a_i=\inf_{\Lambda\in\mathscr C}v(\lambda_i(\Lambda))$ finite, same integral clearing module, common diagonal basis and infinite residue field. Choose approximate individual minima and a generic linear combination; then
$$\inf_{\det\Lambda\ne0}v(\det\Lambda)=\sum_i a_i=\int_0^\infty(d-r_\ell^*(u))du$$
with last identity only for nonnegative a_i and $r^*(u)=\#\{i:a_i\le u\}$. Under arbitrary finite residue field need extension or allowance; do not assume a generic integral combination exists.

## 5. Adelic Arithmetic Deficit Inequality (D5)
Let d target dim, m lifts, C squared-covolume log, δ index, r_{ℓ,j}(u) recoverable rank, ℳ_j actual k/2 main pairs, L_{ℓ,j,p} clearing cost including needed stabilizer, B_{ℓ,j} common loss. All valuations normalized to vℓ(ℓ)=1, uniform over necessary coefficient embeddings. Proposed star:
$$\boxed{\mathfrak A(\theta)=\sum_\ell\log\ell\sum_{j=1}^m[B_{\ell,j}+d^{-1}\int_0^\infty(d-r_{\ell,j}(u))du+2\sum_{p\in\mathcal M_j}L_{\ell,j,p}].}\tag{D5★}$$
$$\boxed{(C+2\delta)/d+\mathfrak A(\theta)+E_{\rm fixed}\ge mk\,\operatorname{directionAmount}.}\tag{D5★★}$$
Actual Hecke product factorization $\rho_j=N(Q)^e(\prod_{\mathcal M_j}R_p\prod_{\mathcal R_j}R_q)^2$, |ℳ_j|=k/2, |ℛ_j|=5m. Source TwistedValueHeights.lean. Let B=fa log³b/(mk), A=fmb log²b. Earlier conservative fixed cost $2b+3mA+10m^2x_1+mk(3B+2x_1)$. Rank-one inverse height prior to finer norm bound: ≤3B+2x₁−directionAmount+Σℓ Lℓp logℓ. Target $\mathfrak A\le3fa\log^4 b-E_{\rm fixed}$ suffices for original integral_forms_long. Need common height witness; not an unconditional RH proof.

## 6. Finite Selmer witnesses and weighted descent (D6)
For finite residue DVR extension O, continuous representation mod ℓ^M, finite order twist characters, intersect kernels to obtain common open normal subgroup. Cocycles on trivial-action subgroup factor through finite exponent abelian quotient unramified outside finite S (class field theory). Polynomial entries in twist coordinates (1+X_j)^{h_j(g)} define actual representation only at admissible torsion specializations. Finite quotient and finite polynomial local relations give a matrix of normalized cocycles; not automatically general crystalline local conditions or cohomology quotients. For A(x) with u columns, append ℓ^M I_u. Smith normal form: normalized length kernel modulo ℓ^M = min maximal-minor valuation of appended matrix. At a witness choose sharp minor P, giving an upper bound at any other admissible point. Bound strictly below M excludes elements of order ℓ^M in divisible-coefficient group when the source truncation lemma applies.
Source GeneralTheorem, OneSystem, Line, Descent, TwistingTheorem; actual assumptions scalar inertia ζ_*²−1 unit, integral matrix span, local conditions and global terms. Tied line X_q0=Y, X_q=s_qY; tie polynomial valuation cost ≤s₀r₀. Brox torsion-specialization supplies common point with controlled shared valuation increase, subject to exact hypotheses. Weighted polynomial
$$\mathscr P_{\mathcal B}(X)=\prod_j[\prod_{i\in\mathcal B_j}P_{\ell,j,i}(X)\prod_{p\in\mathcal M_j}Q_{\ell,j,p}(X)^{2d}]$$
after actual twist-power substitutions. Multiplication alone does not produce cheap witnesses.

Proposed early stopping: b_i=globalTerm+placesTerm, h_i(J)=tied Selmer length, $\Phi(J)=\sum_i w_i[h_i(J)-b_i]_+$. Source descent nonincreases all retained truncated lengths, strict decrease of integer total over levels for an offending datum. Stop at Φ≤τ instead of every excess zero. Let q_i=[h_i−b_i]_+; first tie release gives sharp constant term length ≤β_i+q_i, tie cost s₀r₀ and specialization tolerance ε yield s_i(θ)≤β_i+q_i+ε. Hence
$$\boxed{\sum_i w_i s_i(\theta)\le\sum_iw_i\beta_i+\tau+\varepsilon\sum_i w_i.}\tag{D6}$$
Choose M>max_i(β_i+τ/w_i)+1, ε<1, all weights positive, to ensure actual finiteness. C: replay source descent at every truncation, witness construction with early stop, Stickelberger conditions and normalization. Strict savings in primes not guaranteed.

## 7. Rank-dependent arithmetic and class-number cancellation (D7)
MainSummands.lean, GeneralTheorem, FitTwistsExist: β_R≤(4f+3)n_R gℓ with gℓ=vℓ(G), G=chosenGroupOrder; separate ramℓ≤εℓ and s_R≤β_R+εℓ at common twist. Do not inflate rank-one terms to r. Put a₀=4f+3, λℓ=localDefectBound, eℓ=denominatorError.
Good compression allowance $P_{\ell,j}/d\le r\lambda_\ell+e_\ell+a_0rg_\ell+(1+2t)\varepsilon_\ell$; rank-one pair at z, rankDiff 2z−1, allowance $L_{\ell,j,z}\le\lambda_\ell+e_\ell+(a_0+1)g_\ell+(4z-1)\varepsilon_\ell$ (before separate class number, including stabilizer). z=7m/2+1,…,7m/2+k/2, $2\sum_z(4z-1)=k(14m+k+1)$.
$$\boxed{\mathfrak A_{\rm core}\le m[(r+k)\mathcal L+(k+1)\mathcal E+((4f+3)(r+k)+k)\log G+(1+2t+k(14m+k+1))\eta].}\tag{D7a}$$
$\mathcal L=\sum\lambda_\ell\log\ell,\mathcal E=\sum e_\ell\log\ell$; choose εℓ=min(2^−ℓ,η2^−ℓ/logℓ). This does not assert a fixed twist realizes zero tolerance. Source-relative \mathcal L ≤4·10^6 e^180 f(m/k)b log b, \mathcal E≤x^4000; original uniform clearing theorem supplies larger admissible budget.

Class-number proposal: N₁=#StdClasses(U(1),K_chosen). Source CentralAction norm_card_mul_inner_starProjection_le and TwistedValueHeights test pairings: $|N_1\langle P_\phi\Xi,P_\phi\Xi'\rangle|_\ell\le\ell^{L_\ell}$ and each $|N_1^2\langle\Xi,\phi\rangle|_\ell\ge|c_0\rho|_\ell\ell^{-S_\ell}$ with conjugate counterpart. Exact line projection identity therefore gives
$$|c_0\bar c_0\rho^2/\|\phi\|^2|_\ell\le\ell^{L_\ell+2S_\ell}|N_1|_\ell^3.$$
Use common multiplier $H_p c_0\bar c_0/N_1^3$, arch cost −3 log N₁, rather than dropping factors. Proposed rank-one height ≤B+2C₀+2x₁−directionAmount+ΣL logℓ−3logN₁, $C_0=f(m/k)b+3x^{34}$; net difference vs +log N₁ is 4mk log N₁ across chain. Need audit exact conjugate norms, H multiplier and which L includes stabilizer. Do not count compensation twice.
$$\boxed{mk\,\operatorname{directionAmount}\le (C+2\delta)/d+\mathfrak A_{\rm core}+2b+3fm^2b\log^2 b+10m^2x_1+mk(B+2C_0+2x_1)-3mk\log N_1.}\tag{D7★}$$
Earlier derived source-relative proposed $C+2\delta\ge d[mk\,\operatorname{directionAmount}-3fa\log^4 b+3mk\log N_1]$. No formal replay. All exact source interfaces should be audited before publication as theorem.

## 8. Remaining determinant work
Integral theta/selected short image colength, false-lift orthogonality, actual Hecke ratios, tied normalization, global Selmer arithmetic and local crystalline comparison. Corrected determinant bookkeeping: if C≤h(H−mR+E_A) and product formula implies 0≤C+2δ+Q+B with B≤−DH+E_B, then hmR≤−(D−h)H+hE_A+E_B+2δ+Q. Sign favorable only if H≥0. Never interpret signed smoothed prime remainder as an unweighted prime-counting remainder. See file 03 for latest endpoint.
