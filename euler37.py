#!/usr/bin/env python3
#
# euler37 / truncatable primes 
import math
def isprime(x):
    if x==1:
        return False
    squareroot=int(math.sqrt(x))+1
    for i in range(2,squareroot):
        if x%i==0:
            return False
        else:
            continue
    return True

def truncate_left(x,n):
    y=str(x)
    z=int(y[n:])
    return z

def truncate_right(x,n):
    y=str(x)
    z=int(y[:-n])
    return z

#def truncatable(n):
def istruncatableprime(n):
    taille_n=len(str(n))
    A=[j for j in range(1,taille_n)]
    liste=[n]
    for i in A:
        liste.append(truncate_left(n,i))
        liste.append(truncate_right(n,i))
    for j in liste:
        if isprime(j)!=True:
            return False
    return True


answer=[]
x=11
while len(answer) < 11:
    if isprime(x)==True:
        if(istruncatableprime(x))==True:
            answer.append(x)
    x+=2

print(answer,sum(answer))
