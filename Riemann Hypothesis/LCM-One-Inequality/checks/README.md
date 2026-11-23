# Finite arithmetic regressions

Run `python3 integer_regression.py` under Python 3.11+ (standard library only).

The script checks the exact integer values `L_4=12`, `L_8=217728000`, and `L_4^4/L_8=1/10500`; enumerates prime powers and evaluates the ramp `R(N)` for sample values `n=1,...,42`; and checks the reported `n=42` logarithmic ratio. Floating-point inequalities use a small safety tolerance; these are **regression tests and not certified analytic bounds**.

They do not prove any all-`n` result, the Mellin-positivity converse, or the imported arithmetic estimate (W). For more extensive original auxiliary computations consult the archived source package associated with the 23 November 2026 paper.
