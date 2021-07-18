#!/usr/bin/env python3
#
#euler73 / Counting fractions in a range

import time
from math import gcd, ceil, floor

# Debut du decompte du temps
start_time = time.time()



##main loop
## best 30397485 for d_max = 1000 in s
d_max = 12000
answer = 0 ## init with 0 values between 1/3 and 1/2
for i in range(5,d_max+1):
    for j in range(floor(i/3),ceil(i/2)):
        if gcd(j,i) == 1 and (j/i > 1/3):
            #print(j,i)
            answer+=1
    if i%1000==0 :
        print(f'advancement : {i}')

print(answer)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))