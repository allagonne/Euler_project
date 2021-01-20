#!/usr/bin/env python3
#
#euler58 / spiral primes

import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True

listspiral=[1]
listspiralprimes=[]
j=2
desired_ratio=0.1
while 1:
    for i in range(1,5):
        k=(j-1)**2+j*i
        listspiral.append(k)
        if isprime(k)==True:
            listspiralprimes.append(k)
    ratio=len(listspiralprimes)/len(listspiral)
    if ratio<desired_ratio:
        print('grid=',j+1)
        break
    j+=2
