#!/usr/bin/env python3
#
# euler10 / summation of primes 
import math
def isprime(x):
    squareroot=int(math.sqrt(x))+1
    for i in range(2,squareroot):
        if x%i==0:
            return False
        else:
            continue
    return True

somme=2
x=int(input('max number you want'))
i=3
while i < x:
    if isprime(i)==True:
        somme+=i
    i+=2
print(somme)
