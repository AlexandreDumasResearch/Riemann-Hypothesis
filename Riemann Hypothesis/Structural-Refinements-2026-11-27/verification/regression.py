"""Finite regression checks, not a proof of arithmetic suppliers or RH."""
from itertools import product
from fractions import Fraction
from math import isqrt

def valuation(n, p):
    assert n != 0
    n = abs(n)
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def log_p(n, p):
    assert n > 0
    e = valuation(n, p)
    assert n == p**e
    return e

def test_tied_cyclic():
    count = 0
    for p, h, M in product((2, 3, 5), range(1, 5), range(1, 5)):
        q = p**M
        for t, j in product(range(h+1), repeat=2):
            tied = sum((p**h*x) % q == 0 and (p**t*x) % q == 0 for x in range(q))
            both = sum((p**h*x) % q == 0 and (p**t*x) % q == 0 and (p**j*x) % q == 0 for x in range(q))
            expected = min(h, t, M) - min(h, t, M, j)
            assert tied == both * p**expected
            assert expected == max(0, min(h, t, M)-min(h, t, j))
            count += 1
    return count

def test_dihedral():
    count = 0
    for p, h in product((3, 5), range(1, 4)):
        q = p**h
        elems = list(product(range(q), range(2)))
        for (a,e),(b,f) in product(elems, repeat=2):
            def g(z): return (a + (-1)**e*z) % q
            def t(z): return (b + (-1)**f*z) % q
            assert g(t(0)) == (a + (-1)**e*b) % q
            assert (g(t(1))-g(t(0))) % q == (-1)**(e+f) % q
            count += 1
        assert 1 % q != 0
    return count

def test_mixed():
    count = 0
    for p,h in product((2,3,5,7),range(1,21)):
        a=p**h
        assert min(valuation(a,p),valuation(1+a*a,p))==0
        for X,Y in product(range(-2,3),repeat=2):
            assert (X+a*Y)*(a*X+Y)==a*X**2+(1+a*a)*X*Y+a*Y**2
            count += 1
    return count

def test_pair_sums():
    count=0
    for m,k in product(range(2,40,2),range(2,100,2)):
        z=range(7*m//2+1,7*m//2+k//2+1)
        assert 2*sum(4*i-1 for i in z)==k*(14*m+k+1)
        assert 4*sum(z)==k*(7*m+k//2+1)
        count+=1
    return count

def test_gaussian_packing():
    count=0
    for d,num,den in product(range(1,8),range(1,12),range(1,8)):
        R=Fraction(num,den)
        V=(d*R)**2
        bound=isqrt(V.numerator//V.denominator)
        n=sum(0<a*a+b*b<=V for a,b in product(range(-bound,bound+1),repeat=2))
        assert n<=9*V
        if V<1: assert n==0
        count+=1
    return count

if __name__ == '__main__':
    for f in (test_tied_cyclic,test_dihedral,test_mixed,test_pair_sums,test_gaussian_packing):
        print(f.__name__, f(), 'cases passed')
