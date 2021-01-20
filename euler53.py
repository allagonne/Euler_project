#!/usr/bin/env python3
#
# euler53 / combinatoric selections 

def factoriel(n):
    j=1
    for i in range(2,n+1):
       j*=i
    return j

total=0
for n in range(101):
    for r in range(100):
        if r <= n:
            nCr=factoriel(n)/factoriel(r)/factoriel(n-r)
            if nCr > 1000000:
                total+=1
                print(r,n,nCr)
print('total=',total)
