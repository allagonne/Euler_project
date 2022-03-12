#!/usr/bin/env python3
#
#euler323 / Bitwise-OR operations on random integers
import time

# Debut du decompte du temps
start_time = time.time()

# main
E = 0 #expectation
previous_prob = 0 #probability of previous N
for i in range(1, 100):
    E+=i*(((2**i-1)/(2**i))**32-previous_prob)
    previous_prob = ((2**i-1)/(2**i))**32
    if i%10==0:
        print(E) #converges to the answer

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))