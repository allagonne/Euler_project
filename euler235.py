#!/usr/bin/env python3
#
# euler235.py / An Arithmetic Geometric sequence
import time
from tqdm import tqdm

# Debut du decompte du temps
start_time = time.time()

def u(k,r):
    return (900-3*k)*r**(k-1)

def s(n,r):
    mysum = 0
    for k in range(1,n+1):
        mysum += u(k,r)
    return mysum

def find_lower_r():
    sum_to_find = -600000000000
    r = 1.002322
    while (True):
        if s(5000, r) <= sum_to_find:
            print(r)
            print(s(5000,r))
            break
        r += 0.000000000001

# main loop
sum_to_find = -600000000000
#find_lower_r()
print(s(5000, 1.002322))
print(s(5000, 1.002323))
print(s(5000, 1.002322108633))


# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

