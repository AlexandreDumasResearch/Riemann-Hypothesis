# 08 — Qualitative Bmax period lift for the fixed local augmentation lattice
Alexandre Dumas · ORCID 0009-0003-1695-0086 · 27 November 2026
Status: human proof from pinned qualitative admissibility/regularity inputs. Not a compiler-checked theorem; no quantitative conductor bound claimed.

## 1. Purpose
C10 in 06 required a qualitative period lift Q. We can derive it directly using the source's Bmax regularity, rather than appeal to a separate comparison of Bcris and Bmax. This does not solve C11/C13; it removes the need for that additional qualitative comparison as an independent assumption in the human argument.

Use the actual local group Γ at w|ℓ and complete family u_x from RibetElement. The source establishes InClass F K U for their local matrix lattices. In particular they are potentially crystalline in the source sense: Bmax⊗_{Z_ℓ} each lattice is spanned by vectors fixed near 1. Write B=Bmax and let H_w and I_w be the O-linear spans of u(g) and u(g)-1, respectively. They are stable for the left action, finite free over O, hence over Z_ℓ. The column embeddings into the finite sum of actual matrix lattices are jointly injective and equivariant.

## 2. Admissibility of H_w
By the same jointly-injective subrepresentation argument used in TateDualBound.lean, comesFromClass_of_mem_ribetCocycles (lines 192–240), H_w is in the source's potentially crystalline class, using the closure of InClass under jointly injective equivariant maps into finitely many lattices of the class. Equivalently apply IsAdmissible.of_retraction in Regularity.lean: a Z_ℓ-linear injection of finite free lattices admits a left inverse after tensoring with B, since ℓ is invertible there. No equivariance of the left inverse is required. Therefore B⊗H_w has a basis fixed near 1, by IsAdmissible.exists_basis (Regularity.lean, around line 214).

## 3. The fixed field argument
Let Q_w=H_w/I_w. It is generated as an O-module by the image of 1, and Γ acts trivially on it. Its torsion vanishes after tensoring with B. Since I_w→H_w→Q_w is exact over Z_ℓ, tensoring is exact: B is a Q_ℓ-algebra and therefore flat over Z_ℓ.

If Q_w is torsion, B⊗H_w=B⊗I_w, and 1⊗1 already gives the required coboundary witness.

Otherwise Q_w≅O, a finite free Z_ℓ-module with trivial action. Choose finitely many fixed-near-1 periods of H_w spanning B⊗H_w. As Γ is profinite (the actual local decomposition group), they are fixed by a common open normal subgroup Γ₀. In a Z_ℓ-basis of Q_w the images of these periods are column vectors with coefficients in B^{Γ₀}.

**Key point:** B^{Γ₀} is a field. To see this using exactly the source regularity, apply Fontaine regularity (Regularity.lean, fontaine_regularity, around line 157) to the scalar b∈B^{Γ₀}, b≠0, and the one-coordinate vector w=1, with the filter given by Γ₀. Its hypothesis b·g(1)=g(b)·1 holds. It supplies 1=b·a with a fixed by Γ₀. Thus every nonzero invariant is a unit with invariant inverse. The filter is coarser than nearOne because Γ₀ is open.

The images of the chosen periods span B⊗Q_w over B because the quotient map is surjective. Their coefficient matrix therefore has full row rank over B (it admits a right inverse). Since the entries belong to the subfield B^{Γ₀}, the matrix also has full row rank over B^{Γ₀}: if its rank were deficient there, a nonzero left-kernel vector over the field would remain nonzero over B and contradict surjectivity. Hence the fixed vector 1⊗[1] has a lift z∈B⊗H_w that is fixed by Γ₀, by solving the system over B^{Γ₀}.

Average z over Γ/Γ₀ using the diagonal semilinear action. Normality and finite index guarantee that the average z̄ is Γ-invariant; the denominator [Γ:Γ₀] is a unit in B. Its image remains 1⊗[1] because that vector is Γ-invariant. Exactness then gives a unique preimage y∈B⊗I_w of 1⊗1−z̄.

Consequently
$$\boxed{g y-y=1\otimes(u(g)-1)\qquad(g\in\Gamma).}\tag{C14}$$

This proves Q directly in the source's Bmax setting, subject to the cited qualitative inputs, without quantitative crystalline cup-product estimates. For any integral equivariant map F:I_w→L, apply 1⊗F to C14. The resulting cocycle is a member of the source's crysCocycles by its definition. Thus the integral annihilator argument of C10 applies.

## 4. What is and is not removed
C14 does not require the quantitative dualDefect bound, Hodge-window factorial estimate, or a comparison Bcris≅Bmax. It does retain the source's qualitative potentially crystalline admissibility and Fontaine regularity. The proof uses the actual complete representation family (not just good lifts), and applies to the trivial Tate character as well as main summands. No global central separator is assumed.

The remaining quantitative task is still
$$\sum_{\ell,j,\rho}w_{\ell,j,\rho}\log\ell\,[v_\ell(d_r(A))-v_\ell(d_r(C))]\ll fa\log b,$$
using actual equivariance and tied/tame relation matrices. This is not implied by C14. The qualitative argument has not been formalized in Lean; the existing 11 checks verify only elementary algebraic interfaces. A new independent RH proof is not established.

## Sources at the pinned commit
- [Crystalline/Basic.lean, IsAdmissible, crysCocycles](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/Basic.lean#L96-L115)
- [Crystalline/Regularity.lean, Fontaine regularity and basis/retraction](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/Regularity.lean#L145-L276)
- [TateDualBound.lean, actual graph lattice and jointly injective closure](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/TateDualBound.lean#L192-L240)
