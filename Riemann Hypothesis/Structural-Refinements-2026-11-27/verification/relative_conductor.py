"""Finite lattice regression for C12; not a test of actual RH Galois matrices."""
from itertools import combinations
from math import gcd
from random import Random

def det(M):
    if not M: return 1
    return sum((-1)**j * M[0][j] * det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(len(M)))

def divisor(cols, n, r):
    if r == 0: return 1
    d = 0
    for ii in combinations(range(n), r):
        for jj in combinations(range(len(cols)), r):
            d = gcd(d, det([[cols[j][i] for j in jj] for i in ii]))
    return abs(d)

def valuation(x, p):
    assert x
    ans = 0
    while x % p == 0:
        x //= p
        ans += 1
    return ans

def group_size(cols, n, q):
    H = {(0,)*n}
    for col in cols:
        H = {tuple((v[i]+a*col[i])%q for i in range(n)) for v in H for a in range(q)}
    return len(H)

def test_relative_conductor():
    rng = Random(271126)
    count = 0
    for p, t, r in ((p,t,r) for p in (2,3) for t in (1,2,3) for r in range(t+1)):
        for _ in range(8):
            n = 3
            q = p**2
            U = [[int(i==j) for i in range(n)] for j in range(n)]
            for _ in range(5):
                j,k = rng.sample(range(n),2)
                a = rng.choice((-2,-1,1,2))
                U[j] = [x+a*y for x,y in zip(U[j],U[k])]
            B = [col[:] for col in U[:t]]
            for j in range(t):
                z = p**rng.randrange(3)
                B[j] = [z*x for x in U[j]]
            C = [[p**rng.randrange(3) if i==j else 0 for i in range(t)] for j in range(r)]
            for _ in range(4):
                if r > 1:
                    j,k = rng.sample(range(r),2)
                    a = rng.choice((-1,1))
                    C[j] = [x+a*y for x,y in zip(C[j],C[k])]
            A = [[sum(B[j][i]*col[j] for j in range(t)) for i in range(n)] for col in C]
            pred = valuation(divisor(A,n,r),p) - valuation(divisor(C,t,r),p)
            # Saturation of span(A) has basis U[:r], because U is unimodular.
            # Independent check: count the image modulo q by finite group enumeration.
            old = group_size(B,n,q)
            new = group_size(B+U[:r],n,q)
            assert new == old*p**pred, (p,t,r,pred,old,new)
            count += 1
    return count

if __name__ == '__main__':
    print(test_relative_conductor(), 'cases passed')
