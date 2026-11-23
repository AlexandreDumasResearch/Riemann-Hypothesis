# The Riemann Hypothesis in One Inequality for Least Common Multiples

**Alexandre Dumas** · [ORCID 0009-0003-1695-0086](https://orcid.org/0009-0003-1695-0086) · Revised 23 November 2026

## Manuscript

[Read the revised LaTeX source](main.tex) · [Original source](history/original_main_2026-11-23.tex) · [External-review response](reviews/REVIEW_RESPONSE.md)

The article studies the sequence

\[
L_N=\prod_{j=1}^{N-1}\operatorname{lcm}(1,\dots,j)
\]

and proposes an equivalence between the Riemann hypothesis and

\[
L_{n^2}^{4}\le 2^{n^3}L_{2n^2}\qquad(n\ge1).
\]

The paper also treats a prime-power window and Gaussian/zero-expansion growth criteria.

### Mathematical status — read before citing

The LCM equivalence and growth theorem are **claims with supplied proofs undergoing independent specialist scrutiny**, not externally certified mathematical results. The separate implication from the Alpöge–Claude programme depends on a **specific uniform arithmetic-window estimate (W)**. The authors of this repository have **not verified that the precise quantifiers of (W) follow from a named theorem in a pinned Lean revision**. Under the stated analytic argument, (W) is itself RH-equivalent, and this article **does not independently prove RH**.

Finite numerical and algebraic tests may check particular identities, but do not validate claims quantified over all positive integers or all nontrivial zeros.

### Reviewer-driven changes

The reviewed edition:
- Distinguishes own analytic arguments from external arithmetic hypothesis (W).
- Adds the exact running-LCM/ramp calculation and the numerical constant calculation.
- Expands the Mellin and squared-sample steps.
- Defines the Gaussian maximizing zero and its score gap.
- Separates text-extraction issues from actual formula typos.
- Preserves the earlier original source in `history/`.

See [the review response](reviews/REVIEW_RESPONSE.md) and [Gemini's supplied review](reviews/Gemini_review_user_supplied.md). The Claude file is an **attributed summary of recoverable critique**, not a verbatim transcript.

### Building the manuscript

Compile using a reasonably complete TeX Live distribution:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

GitHub Actions is configured to create the PDF from this source. The release/readable PDF is produced from `main.tex`; the historical original source remains unmodified.

### Rights and attribution

© 2026 Alexandre Dumas. The manuscript text and equations-as-presented are released under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), to the extent copyright applies. Mathematical facts and theorems are not owned by this license. Third-party texts retain their respective rights.
