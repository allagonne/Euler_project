#!/usr/bin/env python3
#
#euler123.py / prime square remainders

import math,time

# Debut du decompte du temps
start_time = time.time()

def isprime(x):
    squareroot=int(math.sqrt(x))+1
    for i in range(2,squareroot):
        if x%i==0:
            return False
        else:
            continue
    return True

def remainder(p_n,n):
    r = ((p_n - 1) ** n + (p_n + 1) ** n) % (p_n ** 2)
    return r

a=2
prime_count=0
while True:
    if isprime(a)==True:
        prime_count+=1
        if remainder(a,prime_count)>10**10:
            print(a,prime_count)
            break
        else:
            a+=1
    else:
        a+=1
# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))