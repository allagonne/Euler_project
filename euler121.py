#!/usr/bin/env python3
#
#euler121.py / Disc game prize fund
from math import prod, floor
import time
from itertools import combinations

# Debut du decompte du temps
start_time = time.time()

def chances(B,R):
    basis = 1
    for i in range(2,2+B+R):
        basis *= 1/i
    if R == 0:
        return basis
    else:
        factor = 0
        for i in combinations(list(range(1,1+B+R)), R):
            factor += prod(i)
        return factor*basis


#main loop
turns = 15
blue, red = turns, 0
proba = 0
## add the proba of every event where blue > red
while (blue > red) :
    proba += chances(blue, red)
    blue -= 1
    red +=1
print(proba)
print(floor(1/proba))


# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

