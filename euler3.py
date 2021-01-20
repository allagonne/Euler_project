#!/usr/bin/env python3
#
#euler3 / Largest prime factor
number=600851475143
def factor(n):
    d=2
    l=3
    factors=[]
    while n%2==0:
        n=n/2
        factors.append(2)
    while l <= n:
        while n%l==0:
            n=n/l
            factors.append(l)
        l=l+2
    return factors

def factor_uniq(n):
    factors=factor(n)
    noDupes=[]
    [noDupes.append(i) for i in factors if not noDupes.count(i)]
    return noDupes

print(factor(number))
print(factor_uniq(number))
