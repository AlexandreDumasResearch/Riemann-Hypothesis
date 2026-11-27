# 03 — Crystalline and trace-algebra research
Alexandre Dumas · ORCID 0009-0003-1695-0086 · 27 November 2026

## 1. Exact crystalline valuation sum (C1, S)
Pinned Basic.lean (LocalLoss), CrystallineDefect.lean, CrystallineCocycles.lean, TraceRelations.lean. Set h=r^8=halfGap, b₀=natB, T₀=5r, Q=kT₀. Let
$$I_{\rm crys}=(2b_0)!(\prod_{b_0-30h^3<n\le b_0+30h^3,\ n>0}n)^{h^3},\quad V_\ell=v_\ell(I_{\rm crys}).$$
$D_\ell=10^6(m/k)(b_0v_\ell(M)+V_\ell)$, $\lambda_\ell=4fD_\ell$. Hence
$$\boxed{\sum_\ell\lambda_\ell\log\ell=4\cdot10^6 f(m/k)\log(M^{b_0}I_{\rm crys}).}\tag{C1}$$
This is the allowance, not the actual crystalline torsion. Source separates main rank r′ from t′ Tate characters: local bounds [E_w:Qℓ]r′Dℓ and [E_w:Qℓ]Dℓ/T₀ per character. Sum gives 2f(r′+t′/T₀)Dℓ instead of 4fr′Dℓ. The factor 2f is sum of local degrees; keep it.

## 2. Integer thresholds and generic vanishing (C2, S)
For ℓ away from the two tame level primes let Fℓ=floor(2Vℓ/Q), μ=floor(r′m/k). The actual crystalline theorem bounds each local normalized dual defect by [E_w:Qℓ]10^5(ρ mFℓ+μ Vℓ). For Tate rank one μ_char=floor(m/(kT₀))=0. Summing:
$$\mathcal D_\ell(r',t')\le2f10^5[(r'+t')mF_\ell+\lfloor r'm/k\rfloor V_\ell].$$
Rank-one main pair has μ=0 since m<k:
$$\boxed{2V_\ell<kT_0\ \Longrightarrow\ \mathcal D_\ell(1,t')=0.}\tag{C2}$$
Source-specific hypotheses of adapted crystalline class, weights, Kummer chart and low jumps required. Not a theorem for arbitrary crystalline reps. In branch ℓ>Q and Vℓ<h³, source noMultipleNear theorem gives zero Tate-character defects and zero main if Vℓ<floor(h/5), otherwise ≤22f[μ(2Vℓ+3)+r′(W+1)], W=4T₀. Need audit the source's exact branch hypotheses for each representation, not infer vanishing from μ=0 alone unless Fℓ=0.
For z=7m/2+1,…,7m/2+k/2, $2\sum_z(1+t'_z)=k(7m+k/2+1)$ with t′_z=2z−1. Set Kcal=r+T₀+k(7m+k/2+1). Weighted normalized allowance across m lifts:
$$\mathfrak A_{\rm crys}\le 2\cdot10^5 fm[m\mathcal K\sum_{\ell\nmid M}F_\ell\log\ell+\lfloor rm/k\rfloor\sum_{\ell\nmid M}V_\ell\log\ell]+E_{\rm tame}.$$
Bound ≤$2\cdot10^5fm[2m\mathcal K/(kT_0)+\lfloor rm/k\rfloor]\log I_{\rm crys}+E_{\rm tame}$. Tame level primes use separate tame bound. No independent proof of p-adic Hodge theorem.

## 3. Interrupted Work findings and improved remainder (C3)
Short index distinct from valuation loss: ordinary primes zero index, exceptional small nonsplit p allowance 14fa/p+1/m per source dimension before rounding, special N ≤mfb. Source LocalDivisibility.lean, IsMarked.isOntoUpToColength_prod_scaledHeckeOperator_pow and ShortAndEnough.lean indexLe_of_mem_image_normalizedPoincare. Keep original normalization but sharpen colength:
$$J_{\rm short}=\sum_{p\in\mathcal P_{\rm exc}}(14fa/p+1/m)\log p+mfb\log N.$$
Prior bound $2\delta/d\le20\log(1+2b^2)J_{\rm short}$ conditional on exact number of selected translates and full/ramified dimension comparison. Elementary $\sum_{p\le X}\log p/p\le2\log X$ via log X! and floor(X/p)≥X/(2p). With log N≤30m log b, m²≤4x, a=xb, gives Jshort=O(fa log b), index/d=O(fa log²b).
Untwisted norm reaches U₀=x³³+8f; test form C₀=f(m/k)b+3x³⁴ before rounding to B. Original uniform simultaneous Selmer sufficient with earlier clearing allowance S=O(f(m/k)b log b)+poly(x). Proposed long error
$$E_{\rm long}=2b+3fm^2b\log^2b+10m^2x_1+mk(U_0+2C_0+2x_1)+m(r+k)S=O(fa\log^2b).$$
Check all uniform constants and common height witnesses; do not rely on class-number cancellation to obtain this estimate.
For retained α=n/d≥1−4/b², H=mainAmount≥0, R=totalRemainder, C≤n(H−mR+Eshort), C+2δ≥d(H−Elong). Subtract:
$$\alpha mR\le\alpha E_{\rm short}+E_{\rm long}+2\delta/d-(1-\alpha)H.$$
Thus $mR\le E_{\rm short}+(E_{\rm long}+20\log(1+2b^2)J_{\rm short})/(1-4/b^2)$. Earlier short error $x^{99}+4fa\log^3b+2b$. Proposed source-relative endpoint
$$\boxed{m\,\operatorname{totalRemainder}=O(fa\log^3 b).}\tag{C3★}$$
Here "=" in big-O notation is ONE-SIDED upper bound, not absolute bound. Original star log^5; source's OneSidedBound.lean converts to
$$R_{q_0,d}(x)\le O(\varphi(q_0)\log^4 b/m)+|R_{q_0,d}(x_1)|+\log b|R_{1,d}(x_1)|.$$
R is the source's smoothed weighted prime remainder. Original normalized log^6; this does not change square-root exponent. No Lean replay yet; status S/C. No claim of independent RH proof.

## 4. Actual relation module and two relaxations (C4)
TateDualBound.lean relLength_ribetCocycles_le defines N=local restrictions of actual Ribet cocycles, A=reduction of integral crystalline cocycles, B=obeying all crystalline relations; A⊂B. Source bounds len N/(N∩B)≤len N/(N∩A)≤universal dualDefect(Q,L∨(1)). Two losses. For finite cohomology modules with perfect Tate pairing, $(A+B)/A$ dual is $A^\perp/(A^\perp\cap B^\perp)$; this is classical and is not automatically the exact source relation module (source uses cocycles, not cohomology classes). Do not confuse the letters B in the two constructions.

Let O DVR, H=O-span u(G) inside product of matrix rings for the finite **complete** representation family u_x; I=span(u(g)−1). Both finitely generated; I two-sided ideal, H=O1+I. Selected lattice L has H-action through block evaluation. For q=ℓ^M, actual Ribet cocycles (obeying all O-linear relations among u(g)−1) identify with Hom_H(I,L/qL): F(u(g)−1)=w(g); equivariance follows from u(h)(u(g)−1)=u(hg)−u(h). Conversely F gives cocycle. Let
$$P_\rho=L^*\otimes_H I,\quad \mu:P_\rho\to L^*,\quad\varphi\otimes i\mapsto\varphi i.$$
Tensor-Hom gives Hom_O(Pρ,O/q). For each finite crystalline relation row j=Σφ_i⊗(u(g_i)−1), define Jcrys generated by all such rows at all crystalline places. Exact DVR duality:
$$\operatorname{crystallineColength}_M=\operatorname{len}(J_{\rm crys}/(J_{\rm crys}\cap qP_\rho))=\operatorname{len}(P_\rho/qP_\rho)-\operatorname{len}(P_\rho/(J_{\rm crys}+qP_\rho)).$$
All coboundaries crystalline, hence Jcrys⊂ker μ. Long exact Tor sequence identifies ker μ with Tor₁^H(L*,H/I). If original uniform colength bound holds for all M with fixed data, Jcrys torsion; since P finite over DVR, for large M intersection with qP zero. Thus
$$\boxed{\sup_M\operatorname{crystallineColength}_M=\operatorname{len}J_{\rm crys}\le\operatorname{len}\operatorname{Tor}_1^H(L^*,H/I).}\tag{C4★}$$
Last bound useful only if Tor finite. This formulation includes dependencies between places without summing universal defects. Need exact source identification of relation rows and normLength. All statements over a finite coefficient DVR; extension must preserve source lattices and normalized lengths.

## 5. Central separation, character cases and counterexamples
If a∈Z(H), a−c∈I and ρ(a)−cI invertible integrally, s(φ)=φ⊗(a−c) gives sμ acting as ρ(a)−cI on tensor; hence ker μ=0. If invertible only rationally, characteristic polynomial/adjugate of the induced central action annihilates ker μ by det(ρ(a)−cI). Length≤minimal generator count×valuation determinant. For rank-one χ with mχ=kerχ, Pχ=I/mχ I and ker μ=(I∩mχ)/(mχ I). Commutative comaximal ideals imply zero; noncommutative not automatic. Trivial Tate χ cannot be separated from augmentation.

Dihedral counterexample: G=C_{ℓ^h}⋊C₂, a rotation, s inversion, χ(a)=1,χ(s)=−1, ℓ odd. χ(s)−1 unit but w(a^is^ε)=i mod ℓ^h noncoboundary, so scalar action on a single group element is not enough. Other example good u(s)=diag(−1,1), u(a)=u(b)=1, bad u(s)=same, u(a)=1+E12, u(b)=1+ℓ^hE21. Bad rational rep irreducible, upper-right coefficient mod ℓ^h is normalized χ-cocycle (lower-left ≡0 and diagonal right ≡1), giving length ≥h in algebraic kernel. Not an actual RH crystalline counterexample.

## 6. Good-family separator, conormal reduction (C5)
RibetLemma.lean exists_character_projector: good ρ_x(γ_x)=y_x Id, y_x−1 unit, all Tate χ_e(γ_x)=1. Ordered product q=∏(y_x−γ_x)/(y_x−1) acts as 0 on each good main and 1 on characters. Exact
$$e=1-\prod_x(y_x-\gamma_x)/(y_x-1)\in I.$$
It is central idempotent on good algebra H_g, not necessarily complete H. Let K_bad=ker(H→H_g). Trivial character in good family ensures K_bad⊂I. [e,h],e²−e∈K_bad. Tensor exact I→I_g with kernel K_bad, and μ_g iso via e. Therefore ker μ=image(L*⊗_H K_bad→P). K_bad acts trivially on L*, so K_bad² dies in tensor; hence
$$\boxed{\operatorname{len}J_{\rm crys}\le\operatorname{len}(L^*\otimes_H K_{\rm bad}/K_{\rm bad}^2).}\tag{C5}$$
All tensors parenthesized as L*⊗_H(K_bad/K_bad²). No bound yet.

## 7. Local commutator identity (C6)
For any e∈I with ρ(e)=Id (centrality NOT assumed), and j=Σφ_i⊗i_i∈kerμ, balancing gives Σφ_i⊗e i_i=j, and Σφ_i⊗i_i e=μ(j)⊗e=0. Thus
$$\boxed{j=\sum_i\varphi_i\otimes[e,u(g_i)].}\tag{C6★}$$
For local rows at w, H_w=span u(G_{E_w}), image C_w generated by these commutators in P lies in ker μ. Jcrys⊂Σ_w C_w. Local centrality suffices for zero defect; exact global centrality unnecessary.

## 8. Trace discriminant witness (C7)
If H_F semisimple, K_bad,F is a direct factor with central identity p_bad. If c p_bad∈K_bad then cK_bad⊂K_bad²; len conormal≤rank_O(K_bad)v_O(c), yielding bound r′ rank(K_bad)v_O(c) for Jcrys. Faithful direct sum trace pairing T_ij=Tr(h_i h_j) in basis of H nondegenerate in characteristic 0 under semisimplicity. Tr(p_bad h_i) integral by invariant rational summand and stable lattice. Cramer's rule gives c=det T as possible scalar. But entire discriminant may be prohibitively large and data vary with ℓ; no global bound from this alone.
$$\boxed{\sum_\ell\log\ell\sum_\rho w_\rho\operatorname{normLength}\operatorname{Tor}_1^{H_\ell}(L_\rho^*,H_\ell/I_\ell)\ll fa\log b.}\tag{C7★}$$
Sufficient target, NOT established. Better target is actual reachable commutator image, not all Tor or full trace discriminant. Include true determinant multiplicities and treat Tate trivial separately.

## 9. NEW: exact normalized tied quotient (C8, E)
This is a further refinement beyond the prior conversation. For the selected **main** summand, one source element γ already has ρ(γ)=y Id with y−1 a unit (RibetMatrices.lean coboundary_eq_zero_of_apply_eq_zero, exists_tiedRows_addVal_det_le). Set e=(u(γ)−1)/(y−1)∈I; no product over the good family needed. The map s:L*→P, s(φ)=φ⊗e satisfies μs=Id, so P=s(L*)⊕K, K=ker μ. Define projection π_K=Id−sμ. For every i∈I,
$$\pi_K(\varphi\otimes i)=\varphi\otimes[e,i].$$
Proof: φ⊗ei=φe⊗i=φ⊗i, φ⊗ie=φi⊗e=sμ(φ⊗i). Consequently K is **exactly** the global commutator image, not just bounded by it. The normalized condition w(γ)=0 is equivalent to annihilating s(L*), i.e. Hom_O(K,O/q).

The actual source main block additionally requires w(τ)=0 for all tied evaluation points τ (including conjugate inverses). Let T⊂K be generated by π_K(φ⊗(u(τ)−1)). Then normalized tied Ribet cocycles are exactly Hom_O(K/T,O/q). Crystalline relation module J⊂K projects to Jbar=(J+T)/T. The colength among the **tied normalized** family is therefore
$$\boxed{D_{\rho,M}^{\rm tied}=\operatorname{len}\frac{J+T}{(J+T)\cap(T+qK)}.}\tag{C8★}$$
Indeed finite module Q=K/(T+qK), the extra conditions kill image of J; exact DVR duality. If J torsion, eventual value is len((J+T)/T)=len J−len(J∩T); exact favorable overlap, not a heuristic. Source main-block lossT previously bounds all Ribet restrictions prior to imposing ties. Replacing it by C8 requires checking the inequality in TraceRelations and RibetElement for **that** tied module and keeping all other unramified/tame/Selmer conditions. For the tied module even fewer rows may be reachable after these further conditions; one can include them as additional finite relation rows where justified.

Define local image C=Σ_w C_w⊂K. Then D_tied≤len(image(C) in K/(T+qK)); if C⊂T, zero at every M even when C and K themselves nonzero. More generally if cC⊂T and the image (C+T)/T requires s generators, D_tied≤s v_O(c). This is the **relative local conductor** target. No global discriminant or global central separator needed. It is strictly weaker than centrality and can allow commutator costs canceled by ties. For example abstract K=O/ℓ^h, T=K, J=K gives zero tied loss though original loss h. This example is illustrative only.

Potential actual supplier: source exists_tame_relations provides polynomial annihilators o(δ)(δ−1) for tame generators and controlled o(1) valuations, but these concern primes away from ℓ. They do NOT establish cC⊂T for local groups above ℓ. Need use actual relations at ℓ, perhaps commutator image in the row span of tied normalizer; no claim this is established. Since the auxiliary primes are chosen by Selmer descent, do not freely add tie rows merely to kill C unless source arithmetic hypotheses and costs permit it.

## 10. Next exact proof obligation
For selected main blocks show
$$\sum_\ell\log\ell\sum_\rho w_\rho \operatorname{normLength}((C_{\rho,\ell}+T_{\rho,\ell})/T_{\rho,\ell})\ll fa\log b$$
or an analogous bound only on Jbar. Use existing source's crystalline theorem as fallback. Tate-character sectors need separate analysis (including trivial character); do not claim C8 removes full crystalline machinery. Need establish actual reduction of the tied bound, estimate conductor uniformly over coefficient embeddings, then replay complete determinant calculation. This is a concrete structural target rather than an RH equivalence.
