#!/usr/bin/env python3
#
# euler49 / prime permutations
import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True

primes=[]
for i in range(1001,10000):
    if isprime(i)==True:
        primes.append(i)

for i in primes:
    for step in range(1,4500):
        j=i+step
        k=i+2*step
        if j in primes and k in primes:
            if sorted(str(i))==sorted(str(j))==sorted(str(k)):
                print(i,j,k)
                print(int(str(i)+str(j)+str(k)))


