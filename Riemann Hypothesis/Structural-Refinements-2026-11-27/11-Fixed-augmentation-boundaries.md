# 11 — Fixed augmentation boundaries and generic-prime localization
Alexandre Dumas · ORCID 0009-0003-1695-0086 · 28 November 2026
Human proofs and source-relative deductions. Not formally replayed in Lean; no independent RH proof or novelty claim.

## 1. Fixed augmentation pairing as connecting homomorphism (C35–C36)
Fix a finite coefficient DVR O, Γ=G_{E_w}, actual complete representation family u including a trivial Tate character. H_w=span_O u(Γ), I_w=ker ε=span_O(u(g)−1), with left Γ-action. Exact sequence 0→I_w→H_w→O→0, O-split by 1, class c_I(g)=u(g)−1. For selected lattice L and L'=L^∨(1) tensor this sequence with L'. The connecting map ∂_w:H¹(Γ,L')→H²(Γ,I_w⊗L') sends a cocycle z' to the differential of its lift 1⊗z'. Explicitly d(1⊗z')(g,h)=(u(g)−1)⊗gz'(h). Hence
$$\boxed{\partial_w[z']=[c_I\smile z'].}\tag{C35★}$$
For any Γ-equivariant F:I_w→L/ℓ^M L, naturality and evaluation give F_*∂_w[z']=[F(c_I)∪z'] in H²(Γ,(O/ℓ^M)(1)). (C36)

## 2. Exact boundary image (C37–C39)
Finite local Tate duality identifies H²(Γ,V(1)) with V_Γ for finite O-torsion V; by inverse limits the same holds for a finite free lattice V (finite cohomology at each level, Mittag-Leffler). Apply with V=I_w⊗L*. Diagonal coinvariants give precisely P_w=L*⊗_{H_w}I_w, since the relations of coinvariants are equivalent to φρ(g)⊗i=φ⊗u(g)i.

The source's crystalline condition is defined via period coboundaries; to identify it with the standard H_f integral condition use the Bmax/Bcris compatibility noted in chapter 10. In the generic nonlevel branch the representations are crystalline. The lattice Z_f of integral crystalline cocycles is finite free and saturated in all functions Γ→L: if a nonzero scalar times a function is a period coboundary, divide by that scalar in the rational period ring. The span of all coordinate evaluation functionals on Z_f is its full dual: otherwise a vector nonzero mod π would have every evaluation divisible by π, contradicting saturation. Hence the row module annihilating Z_f has, modulo ℓ^M, annihilator exactly the reduction of Z_f, not merely a larger space. This justifies using all finite-support relations as in source crysRels, subject to checking formal definition.

For any M the maps I_w→L/ℓ^M are dual to P_w/ℓ^M P_w. By naturality and perfect finite local Tate pairing the annihilator of the image of ∂_w(H_f¹(Γ,L')) modulo ℓ^M is exactly the cocycles satisfying the finite crystalline condition (after evaluation at c_I). It is also the annihilator of actual crystalline relation rows J_w. Thus the two submodules have the same reductions for every M, and finite generation + Krull intersection gives
$$\boxed{J_w=\operatorname{im}(\partial_w|_{H_f^1(\Gamma,L')})\simeq\frac{H_f^1(\Gamma,L')}{H_f^1(\Gamma,L')\cap\operatorname{im}[H^1(\Gamma,H_w\otimes L')\to H^1(\Gamma,L')]}.}\tag{C37–C38★}$$
This is exact for the fixed local algebra, not merely saturation. Map each P_w to the actual global tied normalized quotient S=K/T (C8/C23), using the split projection. Let J_tied=Σ_w ψ_w(J_w). Then
$$D^{tied}_{\rho,M}=\operatorname{len}_O J_{\rm tied}/(J_{\rm tied}\cap\ell^M S).\tag{C39}$$
The source's uniform bounds imply the reached submodule is torsion. The local module is also torsion by the qualitative period argument C14 + finite lattice duality C10. Do not claim that every element of the larger torsion module is a reached boundary. Source compact BlocksAndCocycles.lean, RowBalanced.lean, Lib/ClassField/LocalDuality/CrystallineDuality.lean, Lib/PadicHodge/BlochKato/BlochKato.lean. Standard references: local Tate duality; Bloch–Kato Prop 3.8 and Cor 3.8.4; https://arxiv.org/abs/1609.07627 (integral structures; not a theorem for these particular weights).

## 3. Stronger actual generic vanishing (C40)
Pinned readable Basic.lean IsMainSummandWeights.card_small_le and low_or_high; CrystallineDefect.lean lines 570–630 selects actual dual jumps U' (not the full dual string); CrystallineCocycles.lean normLength_dualDefect_le_of_noMultipleNear calls dualDefect_eq_zero_and_dualDefect_le; compact Lift/ExponentTheorems.lean few_low_jumps.
Set Q=kT₀, h=r^8, b₀=natB, Vℓ=vℓ(I_crys). Generic nonlevel ℓ>Q, Vℓ<h³, chart unramified and gap hypotheses of source. The zero branch needs U and U' to avoid [-2(Vℓ+1),0) or U' contained in the low negative window. If r'm<k, then floor(r'm/k)=0, no low main jumps at any embedding. Indeed low jumps have |u|≤4mh≤2h² from original sizes, and card_small_le excludes them. High main weights have |u|≥offWeight−T₀ (in fact the source window starts G+δ), exceeding 2h³+1 by G≥99h³ and scale separation. Dual main jumps -u−1 likewise. Original class's Tate jumps are nonnegative; dual U' is filtered to actual selected summand. Thus
$$\boxed{\ell>Q,\ V_\ell<h^3,\ r'm<k\Longrightarrow \mathcal D_\ell(r',t')=0.}\tag{C40★}$$
Tate summands vanish by original low-negative-window branch. In particular every rank-one main pair vanishes throughout this generic branch; C34's conservative rank-one W-term can be removed. Higher-rank blocks with no actual low jump also vanish. More precise local test: if d_w=min{|u|: u<0 in U or U' at a coefficient embedding}, with d_w=∞ for empty set, zero if 2(Vℓ+1)<d_w. This uses the source's existing qualitative/quantitative vanishing supplier, not an independent proof.

## 4. Arithmetic localization (C41–C43)
I_crys=(2b₀)! (product over b₀−30h³<n≤b₀+30h³)^{h³}. If Vℓ<h³, ℓ divides no integer of the short product. Thus Vℓ=vℓ((2b₀)!)≥floor(2b₀/ℓ), implying ℓ>2b₀/h³. Source size conditions imply b₀≥99²h⁶, hence ℓ²>2b₀. By Legendre:
$$V_\ell=\lfloor2b_0/\ell\rfloor.\tag{C41}$$
Nonzero generic main defect requires Vℓ≥h_*:=floor(h/5)>0 by original vanishing. Consequently
$$\boxed{L_0=2b_0/h^3<\ell\le U_0=2b_0/h_*.}\tag{C42★}$$
Also ℓ avoids all factors in the short product; this is a necessary support, not an assertion every prime there contributes.

Elementary Chebyshev θ(X)≤4X (binomial coefficient bounds at dyadic scales). On a doubling interval (Y,2Y] one has Σ log p/p≤8. With H=1+log₂(h³/h_*), the total generic valuation satisfies
$$\sum_{\ell\in\mathcal G}V_\ell\log\ell\le16b_0H,\qquad \sum_{\ell\in\mathcal G}\log\ell\le8b_0/h_*.$$
Only the rank-r main blocks across m lifts can now contribute. Keep original generic bound 22f[μ(2Vℓ+3)+r(W+1)], μ=floor(rm/k), W=4T₀, using local degrees 2f. Then
$$\boxed{\mathfrak A_{\rm generic}\le22fm b_0[32\mu H+8(3\mu+r(W+1))/h_*]=O(fa\log h).}\tag{C43★}$$
Here b₀ asymptotic to nominal b, a=xb, m²=O(x), r∼k, h=r⁸, log h=O(log x). This replaces previous generic allowance O(fa log b); the ratio tends to zero under the source's b superpolynomial scale. Still uses source low-jump length bound. No claim of full global reduction to O(fa log h): exponent branch may dominate.

Additional budget decomposition: short-window logarithmic mass ≤60h⁶ log(2b₀) (b₀≫h³). Small primes ℓ≤Q have factorial logarithmic mass O(b₀(1+log Q)) by Legendre V_fac≤2b₀/(ℓ−1) and dyadic Chebyshev. In exponent branches C27–C34, multiplying these masses by O(fm²) gives O(fa log Q) plus O(fm² h⁶ log b₀), both subleading to fa log b if h⁶=o(b). For ℓ>2b₀/h³ with Vℓ≥h³, the window term is nonzero and ≥h³ while factorial term <h³, so total mass there is at most twice window mass. Thus the potentially dominant exponent budget is factorial primes Q<ℓ≤2b₀/h³. This is an upper-bound decomposition, not proof that actual defect is attained.

## 5. Direct local invariant-lift conductor (C44–C45)
For source ties ρ(τ)=1, Hτ=H/Nτ, Iτ=ker ε, and tied equivariant maps F:Iτ→L/ℓ^M. Let
$$A_w=\{h_0\in H:\ (u(g)-1)h_0\in N_\tau\ \forall g\in G_{E_w}\},\quad \mathfrak a_w=\epsilon(A_w).$$
A_w is a finite free O-module; its equations can use any finite basis of the actual span of u(g)-1 in I_w. If the full rational H is semisimple (source trace nondegenerate), a scalar multiple of the central trivial-factor idempotent belongs to A_w and has nonzero augmentation, so a_w nonzero. No semisimplicity of H_w assumed. Choose h0 with augmentation c generating a_w, and let z=c·1−h0 mod Nτ in Iτ. For all local g, c(u(g)-1)=(u(g)-1)z modulo Nτ. Applying F:
$$\boxed{cF(u(g)-1)=(\rho(g)-1)F(z).}\tag{C44★}$$
Thus c times every actual tied local cocycle is a coboundary, and c kills the reached crystalline image. This is a concrete arithmetic certificate independent of quantitative Hodge theory; it only requires invariant lift in the actual tied algebra. a_w computable via kernel of h↦((u(g_i)-1)h mod Nτ)_i followed by augmentation, retaining torsion in Hτ. A unit generator gives exact vanishing. Not proved small for actual matrices. Rational removal of bad factors alone does not control a_w, by chapter 10 saturation counterexample. This certificate is stronger than necessary because crystalline lifts need not be coboundaries.

Using C33, sum over places ≤4fr times a common normalized conductor exponent Eℓ. On necessary generic support interval C42,
$$\mathfrak A_{\rm generic}\le 4fm r \sum_{\ell\in\mathcal G} E_\ell\log\ell \le32fm r b_0 E_{\max}/h_*.$$
In particular sufficient uniform exponent target
$$\boxed{E_{\max}=O(h_*m/r)\ \Longrightarrow\ \mathfrak A_{\rm generic}=O(fa).}\tag{C45★}$$
This is substantially more permissive than a uniform very small local conductor, since h=r⁸. It only replaces generic nonzero-sector quantitative length if existing support vanishing is retained (or reproved independently); cannot assume C42 when removing its proof. No actual bound Emax established.

## 6. Research verdict
C35–39 give exact fixed boundary image and lift defect. C40–43 are concrete source-relative improvements to generic accounting, and C44–45 give a finite local arithmetic certificate and realistic exponent target. The rank-one generic W-term in C34 is unnecessary. The central remaining task is compute or bound ε(A_w) or the smaller cohomological boundary image for the actual Galois family, without universal low-jump length estimates. The source does not provide explicit numerical matrices. Global reciprocity can kill pairings with global lifts whose other local conditions are orthogonal; surjectivity of the requisite dual localization is not automatic from the already bounded primal finite Selmer group (would risk circularly assuming a bound for the relaxed group). No proof of that surjectivity claimed. No new Lean runs performed.
