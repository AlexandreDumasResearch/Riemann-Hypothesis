#!/usr/bin/env python3
"""Finite arithmetic regression for the LCM paper. NOT a proof of RH."""
from math import isqrt, log, lcm

def prime_powers(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = b"\x00" * ((limit-p*p)//p + 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            m = p
            while m <= limit:
                yield m, p
                m *= p

def ramp(n):
    return sum((n-m)*log(p) for m,p in prime_powers(n-1))

def running_lcm_products(indices):
    selected = set(indices)
    current, product = 1, 1
    results = {}
    for j in range(1,max(selected)+1):
        if j in selected:
            results[j] = product
        current = lcm(current, j)
        product *= current
    return results

if __name__ == "__main__":
    L = running_lcm_products([4, 8])
    assert L[4] == 12
    assert L[8] == 217728000
    assert 10500*L[4]**4 == L[8]
    for n in range(1,43):
        x = n*n
        signed_log = 4*ramp(x)-ramp(2*x)
        assert signed_log <= n**3*log(2)+1e-7, (n,signed_log)
    ratio_bits = (4*ramp(42**2)-ramp(2*42**2))/log(2)
    assert 123 < ratio_bits < 124
    print("Finite checks passed: L_4=12, L_8=217728000, 42 sampled inequalities.")
    print(f"n=42: log2( L_(n²)^4 / L_(2n²) ) = {ratio_bits:.10f}")
    print("WARNING: finite regression does not establish the all-n inequality or RH.")
