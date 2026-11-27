# 04 — Verification ledger and reproducibility
27 November 2026 · Alexandre Dumas · ORCID 0009-0003-1695-0086

## Archive fidelity
Original 29-page manuscript LaTeX file is preserved in [manuscript/adelic_volume_RH.tex](manuscript/adelic_volume_RH.tex). The retrieved text had 657 lines and 100981 characters, matching the locally generated manuscript; FNV-1a over character code points matched 1053204815. This is a fidelity check, not a cryptographic checksum. The original PDF binary was not uploaded by the UTF-8 GitHub connector; regenerate from the archived LaTeX source. The dossier's later results supersede some working assumptions of the manuscript but preserve the original verbatim. All earlier repository archives remain untouched. Unavailable interrupted Work scratch files were not reconstructed verbatim; only their visible findings and subsequent research are included.

## What was tested
Local Python integer/rational regression script [verification/regression.py](verification/regression.py) ran successfully:
- tied cyclic annihilator/colength identity: 648 finite cases;
- dihedral affine composition (counterexample's cocycle): 68,376 pairs;
- mixed two-packet polynomial and valuations: 2,000 cases;
- exact main-pair multiplicities: 931 parameter pairs;
- Gaussian integer packing in Q(i) for principal rational-integer denominator ideals: 539 cases.

These are regression checks of finite models and formulas, not mathematical proofs of the infinite cases or actual arithmetic hypotheses. GitHub Actions finite-regressions job also returned success in run [45943756130](https://github.com/AlexandreDumasResearch/Riemann-Hypothesis/actions/runs/45943756130).

## Lean / Mathlib
Lean, Lake and Elan absent in the local execution environment; GitHub DNS failed on local download attempt. The candidate [StructuralChecks.lean](verification/StructuralChecks.lean) contains seven small theorems (balanced commutator interface, relation sum, split-kernel projection/retract, two-packet polynomial identity, determinant budget and dropped missing term) and prints axioms. It does not formalize the full tensor construction or arithmetic hypotheses. No sorry or additional axiom declarations have been inserted. Do not call this formally checked until the Lean job succeeds.

Workflow [.github/workflows/rh-structural-checks.yml](../../.github/workflows/rh-structural-checks.yml) was committed and triggered. Corrected pipeline (compiler failures propagate): [run 45943756130](https://github.com/AlexandreDumasResearch/Riemann-Hypothesis/actions/runs/45943756130). At this checkpoint the finite-regressions job completed successfully, Lean job was still in progress. Check the live job outcome and printed axioms; no success is assumed. The workflow uses upstream checkout at 72fead102f663d5c7a407964a13dc0cf9d977207, Lean v4.35.0 and Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679. It checks only the Mathlib-based candidate file, not the entire pinned RH project.

For local verification:
1. Install Elan/Lean.
2. Clone lsernau/grh-lean, check out the exact commit above, enter grh.
3. Run lake exe cache get.
4. Copy verification/StructuralChecks.lean into grh and run lake env lean StructuralChecks.lean.
5. Inspect printed axiom dependencies. Full original upstream build and its axiom audit are separate tasks. No new RH proof is verified by the seven lemmas.

## Source dependency ledger
| Obligation | Current disposition |
|---|---|
| A1 packing, layer cake, convolution, rank deficit | Elementary derivations; finite tests for selected models |
| A2/A3 full local Bessel/Poisson applicability | Source-relative; local Fourier kernels and all depth constants need replay |
| Non-main cells, Siegel class sum, target multiplicity | Remain substantial; no claim of elimination |
| Ramified deficit transfer, saturation and spanning | Elementary conditional inequalities; original theorem interface needed |
| Integral seesaw, common multiplier, actual colength | Source-based, independent supplier open |
| Good compression identity | Established in pinned source; new reachable defect formula elementary |
| Mixed-twist Gram method | Conditional; auxiliary conjugate phase and common height unresolved |
| Weighted clearing and descent | Source-relative; individual-generator theorem retained; early stop needs formal replay |
| Class number favorable factor | Candidate source-derived calculation; audit conjugate and multiplier normalizations before using |
| Rank-one and crystalline exact counts | Source-derived; regression checks on multiplicities; no independent Hodge proof |
| Improved log^3 one-sided total remainder | Conditional source-relative quantitative result; not absolute remainder estimate |
| Augmentation, Tor, conormal, local commutators | Elementary algebra; only basic interface candidate Lean proofs |
| C8/C9 source-local relative crystalline cost | Exact elementary quotient and source interface; actual uniform conductor remains open |
| Full RH endpoint | Existing source endpoint required; no independent proof established |

## Priority next
A. Formalize full C8/C9 finite DVR length/annihilator lemma using Mathlib modules. Check exact source's relLength_add_length_inf and source relation module definitions rather than duplicating their abstraction unnecessarily.
B. Obtain actual finite representation-algebra generators and trace/tame/tied rows for a specified source case. Form the image quotient and compute Smith invariants.
C. Seek algebraic local polynomial or commutator relations above ℓ implying a cheap relative conductor, then prove weighted global sum. Treat main and character blocks separately; a universal trace discriminant is a fallback, not a sufficient asymptotic estimate.
D. Only after C, replace the original local crystalline supplier and replay downstream determinant argument. Compare proof dependencies, not just line count and log exponents.
E. Retain failed and suspended routes in the analytic and determinant files. No priority claim until literature and other distillations are compared.
