import Mathlib

/-!
Small standalone candidate formalizations of the algebraic interfaces in C6/C8.
No new axioms, sorry, or claim to prove the arithmetic hypotheses.
Compiler status must be read from the CI run, not inferred from this file.
-/

namespace RHStructural

theorem commutator_tensor_interface
    {R A P : Type*} [Ring R] [AddCommGroup P]
    (act : A → R → A) (B : A → R → P) (e : R)
    (hbal : ∀ a x y, B (act a x) y = B a (x * y))
    (hsub : ∀ a x y, B a (x - y) = B a x - B a y)
    (he : ∀ a, act a e = a) (a : A) (i : R) :
    B a (e * i - i * e) = B a i - B (act a i) e := by
  rw [hsub, ← hbal a e i, ← hbal a i e, he]

theorem commutator_relation_sum
    {R A P S : Type*} [Ring R] [AddCommGroup P]
    (act : A → R → A) (B : A → R → P) (e : R)
    (hbal : ∀ a x y, B (act a x) y = B a (x * y))
    (hsub : ∀ a x y, B a (x - y) = B a x - B a y)
    (he : ∀ a, act a e = a) (s : Finset S)
    (a : S → A) (i : S → R)
    (hz : ∑ j ∈ s, B (act (a j) (i j)) e = 0) :
    (∑ j ∈ s, B (a j) (e * i j - i j * e)) =
      ∑ j ∈ s, B (a j) (i j) := by
  simp_rw [commutator_tensor_interface act B e hbal hsub he]
  rw [Finset.sum_sub_distrib, hz, sub_zero]

theorem split_kernel_projection
    {P A : Type*} [AddCommGroup P] [AddCommGroup A]
    (mu : P →+ A) (s : A →+ P) (hs : ∀ a, mu (s a) = a)
    (x : P) : mu (x - s (mu x)) = 0 := by
  rw [map_sub, hs, sub_self]

theorem split_kernel_retract
    {P A : Type*} [AddCommGroup P] [AddCommGroup A]
    (mu : P →+ A) (s : A →+ P) (x : P) (hx : mu x = 0) :
    x - s (mu x) = x := by
  rw [hx, map_zero, sub_zero]

theorem mixed_two_packet_identity {R : Type*} [CommRing R] (a X Y : R) :
    (X + a * Y) * (a * X + Y) =
      a * X^2 + (1 + a^2) * X * Y + a * Y^2 := by ring

theorem determinant_budget
    (alpha C H R Es El delta : ℝ)
    (hshort : C ≤ alpha * (H - R + Es))
    (hlong : H - El ≤ C + 2 * delta) :
    alpha * R ≤ alpha * Es + El + 2 * delta - (1 - alpha) * H := by
  nlinarith [hshort, hlong]

theorem determinant_budget_drop_missing
    (alpha C H R Es El delta : ℝ)
    (ha : alpha ≤ 1) (hH : 0 ≤ H)
    (hshort : C ≤ alpha * (H - R + Es))
    (hlong : H - El ≤ C + 2 * delta) :
    alpha * R ≤ alpha * Es + El + 2 * delta := by
  have h := determinant_budget alpha C H R Es El delta hshort hlong
  have hn : 0 ≤ (1 - alpha) * H := mul_nonneg (sub_nonneg.mpr ha) hH
  linarith

#print axioms commutator_tensor_interface
#print axioms commutator_relation_sum
#print axioms split_kernel_projection
#print axioms split_kernel_retract
#print axioms mixed_two_packet_identity
#print axioms determinant_budget
#print axioms determinant_budget_drop_missing

end RHStructural


namespace RHStructural

/-! C10: algebraic length bounds for images after imposing relations.
These statements formalize the finite-module interface, not the period lift Q. -/

theorem relative_image_length_le
    {R M N : Type*} [Ring R] [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N) (T : Submodule R M) (h : T ≤ LinearMap.ker f) :
    Module.length R (LinearMap.range f) ≤ Module.length R (M ⧸ T) := by
  have hr : T ≤ LinearMap.ker f.rangeRestrict := by
    intro x hx
    have hx0 : f x = 0 := h hx
    exact Subtype.ext hx0
  let g := T.liftQ f.rangeRestrict hr
  apply Module.length_le_of_surjective g
  intro y
  obtain ⟨x, hx⟩ := y.property
  refine ⟨T.mkQ x, ?_⟩
  change T.liftQ f.rangeRestrict hr (Submodule.Quotient.mk x) = y
  rw [Submodule.liftQ_apply]
  exact Subtype.ext hx

theorem image_length_mono
    {R M N : Type*} [Ring R] [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N) {A B : Submodule R M} (h : A ≤ B) :
    Module.length R (A.map f) ≤ Module.length R (B.map f) := by
  rw [Module.length_submodule, Module.length_submodule]
  exact Order.height_mono (Submodule.map_mono h)

theorem conductor_kills_image
    {R M N : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N) (A : Submodule R M) (c : R)
    (h : ∀ x ∈ A, c • x ∈ LinearMap.ker f)
    (y : N) (hy : y ∈ A.map f) : c • y = 0 := by
  obtain ⟨x, hx, rfl⟩ := Submodule.mem_map.mp hy
  rw [← map_smul]
  exact h x hx

theorem relative_image_exact_equiv
    {R M N : Type*} [Ring R] [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N) :
    Module.length R (M ⧸ LinearMap.ker f) =
      Module.length R (LinearMap.range f) :=
  f.quotKerEquivRange.length_eq

#print axioms relative_image_length_le
#print axioms image_length_mono
#print axioms conductor_kills_image
#print axioms relative_image_exact_equiv

end RHStructural
