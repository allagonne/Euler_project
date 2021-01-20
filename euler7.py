#!/usr/bin/env python3
#
# euler7 / 10001st prime 
import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True

listprimes=[2]
x=int(input('nieme nombre premier?'))
i=3
while len(listprimes) < x:
    if isprime(i)==True:
        listprimes.append(i)
    i+=1

print(listprimes[-1])
