# Structural refinements toward an independently auditable RH proof
**Alexandre Dumas — ORCID [0009-0003-1695-0086](https://orcid.org/0009-0003-1695-0086)**  
Research checkpoint: 27 November 2026. AI-assisted working notes; not a proof announcement.

## Reading order and scope

- [Analytic and geometric ledger](01-Analytic-and-geometric.md): all recent sieve, packing, spanning, frequency and abandoned alternatives.
- [Adelic determinant and arithmetic ledger](02-Determinants-and-Selmer.md): conservation, reachable projection, mixed twists, weighted clearing and all arithmetic star equations.
- [Crystalline and trace algebra](03-Crystalline-and-trace-algebra.md): crystalline block estimates, short/long remainder budget, augmentation, Tor, conormal and separator constructions, new tied-cocycle refinement.
- [Source-local replacement theorem](05-Source-local-replacement.md): exact main and Tate restricted cocycle costs (new C9 star).
- [Local saturation and relative Smith lengths](06-Local-saturation.md): new conditional finite-matrix replacement, C10 and C11.
- [Relative determinantal conductor](07-Relative-determinantal-conductor.md): exact signed determinant ratio C12 and global target C13.
- [Qualitative Bmax period lift](08-Qualitative-period-lift.md): C14 derives the period-lift assumption of C10 from pinned qualitative admissibility and regularity.
- [Integral Peirce reduction and local generator bound](09-Peirce-and-local-generator-bound.md): C15–C20, exact off-diagonal obstruction, rank-one relations and local cohomological cost.
- [Original full LaTeX manuscript](manuscript/adelic_volume_RH.tex): exact original 29-page manuscript source.
- [Verification and dependency ledger](04-Verification.md): status and tests, precise remaining obligations and reproducibility instructions.
- [Lean lemmas](verification/StructuralChecks.lean): 11 kernel-checked algebraic interfaces ([successful run](https://github.com/AlexandreDumasResearch/Riemann-Hypothesis/actions/runs/45948892951)), not a formalization of RH.

The earlier September programme, October signed correlations, November critical atlas and LCM inequality are preserved in the parent repository. This checkpoint consolidates the recent conversation and visible interrupted Work findings; it is not an exhaustive transcription of inaccessible Work scratch files. The earlier 29-page manuscript "Adelic Volume Conservation, Coupled Bessel Sieves, and Mixed-Twist Determinants" is the basis of the analytic and determinant ledger; this checkpoint extends it with subsequent discoveries and corrections.

## Status conventions
**E** = elementary proof supplied here, uncompiled unless stated otherwise. **S** = source-relative: relies on a declaration/estimate of the pinned external source. **C** = conditional bridge or unverified substitution into actual arithmetic maps. **X** = failed or suspended route. **O** = open obligation. No claim of publication priority, completed independent RH proof, or kernel verification of an entire modified proof.

Upstream source pinned to [lsernau/grh-lean at 72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New). Lean v4.35.0; Mathlib revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Compare [JoseBrox/GRH_distillation](https://github.com/JoseBrox/GRH_distillation); do not silently import a changing development into the pinned architecture. The earlier 40e56bab… archive is not an exact full pin in this dossier.

## Main equation index (stable identifiers)
| ID | Equation | Status |
|---|---|---|
| A1 | anisotropic ideal packing | E |
| A2 | packing-integrated Bessel bound, Q^(K+2+2η) | E conditional on majorant |
| A3 | weighted reciprocal convolution and depth dominance | E/S/C |
| A4 | centered Gram / ramified deficit transfer | E |
| D1 | Zθ Δθ=C₀ρθ^d | S |
| D2 | signed reachable congruence index | E |
| D3 | mixed determinant Gauss valuation | E/C |
| D4 | optimal diagonal clearing and integrated rank deficit | E/C |
| D5 | Adelic Arithmetic Deficit Inequality (★,★★) | S/C |
| D6 | weighted witness polynomial and early-stop descent | C/S |
| D7 | explicit rank-dependent budget, class-number compensation | S/C |
| C1 | exact crystalline factorial valuation sum | S |
| C2 | rank-one crystalline exclusion threshold | S |
| C3 | improved short/long and total-remainder star | S/C |
| C4 | reachable crystalline length / Tor star | E/C |
| C5 | good-family separator and conormal reduction | E/S |
| C6 | local commutator identity | E |
| C7 | weighted conductor target | O |
| C8 | tied, normalized reachable commutator quotient (new) | E/C |
| C9 | source-local main/Tate replacement and combined conductor budget (new) | E/S/C |
| C10 | local relation saturation and relative image length | E/C |
| C11 | weighted relative Smith-length target | O |
| C12 | exact signed determinantal divisor formula | E |
| C13 | weighted relative determinant budget | C/O |
| C14 | qualitative Bmax period lift of the local augmentation cocycle | S (human derivation) |
| C15 | integral idempotent via Hensel and CRT | E |
| C16 | right augmentation annihilation | E |
| C17 | exact off-diagonal Peirce quotient | E |
| C18 | rank-one local evaluation relations | S/E/C |
| C19 | local generator count independent of family size | E/S |
| C20 | weighted conductor-exponent target | C/O |

## Research priority
1. Formalize C14 and estimate the actual relative saturation images after C8/C9 ties; no need to bound full global Tor if the smaller image suffices.
2. Establish an effective local conductor for the *image* of local commutators, not a full trace discriminant.
3. Treat the trivial Tate character separately; it cannot be separated from augmentation.
4. Check every source-relative substitution, particularly common height multipliers, normalizations and finite-place sums.
5. Keep prior analytic pathways, including failed attempts, available for future research. An improvement in logarithmic overhead is not by itself a shorter independent proof.

## 28 November continuation: tied conductors

[10 — Tied quotient, exact conductors, and local exponent transfer](10-Tied-conductor-and-dual-transfer.md) records C21–C34: tied ideal and Tor reduction, actual cup-exponent transfer, full tied main-block annihilator, optimal Smith conductor, saturation counterexample, finite-dual generator count and hybrid weighted global budget. Source-relative bounds, not independently Lean-checked. Next target: fixed augmentation pairings in the generic high-rank low-jump branch, without the universal quantitative supplier.
