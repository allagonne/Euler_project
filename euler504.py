#!/usr/bin/env python3
#
# euler504 / Square on the inside

import time
from math import gcd, sqrt

# Debut du decompte du temps
start_time = time.time()
result = 0

m = 100
lp = 0

for a in range(1, m + 1):
    for b in range(1, m + 1):
        for c in range(1, m + 1):
            for d in range(1, m + 1):
                bb = gcd(a, b) + gcd(b, c) + gcd(c, d) + gcd(d, a)
                lp = sqrt((a * b + b * c + c * d + d * a) / 2 + 1 - bb / 2)

                if lp == int(lp): result += 1

print(f'Result: {result}')

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))