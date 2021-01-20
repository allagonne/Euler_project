#!/usr/bin/env python3
#
#euler187.py / semiprimes
#basé sur les facteurs des nb premiers
from math import sqrt
import time

# Debut du decompte du temps
start_time = time.time()

def isprime(x):
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

def issemiprime(n):
    list_obvious_semiprimes=[9,15,21,25]
    if n in list_obvious_semiprimes:
        return True
    elif n%3 == 0:
        if isprime(n/3) == True:
            return True
    else:
        for obvious_semiprime in list_obvious_semiprimes:
            if n%obvious_semiprime == 0:
                return False
        for i in range(3,int(sqrt(n))+1,2):
            if n%i == 0:
                if isprime(i) == True :
                    if isprime(int(n/i)) == True:
                        return True
                    else:
                        return False
        return False


#main loop
n=10**7
total=0
for i in range(5,n,2):
    if issemiprime(i) == True:
        total += 1
total += 1 # cas n=4
for i in range(6,n,2):
    if i%4 != 0: ##6, 10, 14...
        if isprime(i/2) == True:
            total += 1
    #else: ##8, 12, 16...
        #continue
print(total)


# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

