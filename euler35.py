#!/usr/bin/env python3
#
# euler35.py / circular primes

import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True

circular=[2,3,5,7]
for i in range(10,1000000):
    s=str(i)
    permut=[i]
    test=1
    ##exclure les nombres non-circulaires évidents
    if '0' in s or '2' in s or '4' in s or '5' in s or '6' in s or '8' in s:
        test=0
    else:
        for j in range(1,len(s)):
            permut.append(int(s[-j:]+s[:-j]))
        print(permut)
    for j in range(len(permut)):
        if isprime(permut[j])==False:
            test=0
    if test==1:
        circular.append(i)
print(circular)
print(len(circular))            
