#!/usr/bin/env python3
#
#euler47 / distinct primes factors
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
    checked=[]
    [checked.append(i) for i in factors if not checked.count(i)]
    return checked

test=0
i=2
while True:
    if len(factor_uniq(i)) == 4:
        if len(factor_uniq(i+1)) == 4:
            if len(factor_uniq(i+2)) == 4:
                if len(factor_uniq(i+3)) == 4:
                    print(i,i+1,i+2)
                    break
    i+=1

