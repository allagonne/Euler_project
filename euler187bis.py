#!/usr/bin/env python3
#
#euler187.py / semiprimes / solved
#bis car basé sur multiplication de nb premiers
#gain environ *2
from math import sqrt
import time

# Debut du decompte du temps
start_time = time.time()

def isprime(x):
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

#main loop
n = 10**8
total = 0
for i in range(2,int(sqrt(n))+1,2):
    if isprime(i) == True:
        for p in range(i,int(n/i)+1):
            if isprime(p) == True:
                total+=1
print(total)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

