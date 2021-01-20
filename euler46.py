#!/usr/bin/env python3
#
# euler46 / Goldbach's other conjecture 
import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True

listprimes=[2]
i=3
while len(listprimes) < 100:
    if isprime(i)==True:
        listprimes.append(i)
    i+=1
print(listprimes)

A=[2*j**2 for j in range(1,30)]
print(A)
j=3
while True:
    if isprime(j)==True:
        j+=2
    else:
        for i in range(1,j):
            if j-i in A:
                print(i,j)
                break
    j+=2


    
    
    j+=2
