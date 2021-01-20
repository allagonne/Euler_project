#!/usr/bin/env python3
#
# euler27 / quadratic primes 
import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True
upper=1000
amax,bmax,nmax=0,0,0
listnumberofprimes=[]
for a in range(-upper,upper):
    for b in range(-upper-1,upper+1):
        n=0
        while isprime(abs(n**2+a*n+b)):
            n+=1
        listnumberofprimes.append(n)
        if n>nmax:
            print(a,b,n)
            nmax,amax,bmax=n,a,b

print(listnumberofprimes)
print(len(listnumberofprimes))
print(max(listnumberofprimes))
print(amax,bmax,nmax)
print('product of a*b',amax*bmax)
