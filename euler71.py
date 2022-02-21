#!/usr/bin/env python3
#
#euler71 / Ordered fractions

import time

# Debut du decompte du temps
start_time = time.time()

def gen_fractions(d):
    ''' generate fractions immediately to the left of 3/7, with d being the maximum denominator'''
    return_list = []
    for denom in range(2, d+1):
        for num in range(int(denom*42.85/100), int(denom*42.86/100)):
            frac = num/denom
            if frac>0.42857 and frac < 3/7:
                return_list.append([num/denom, f'{num}/{denom}'])
    return sorted(return_list)

d=10**6
print(gen_fractions(d)[-1])

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))