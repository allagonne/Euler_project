#!/usr/bin/env python3
#
# euler116 / Red, green or blue tiles

import time
from math import factorial

# Debut du decompte du temps
start_time = time.time()

def perm(n, k):
    '''gives the number of permutations of k among n'''
    return int(factorial(n)/(factorial(k)*factorial(n-k)))
def nb_blocks(full_len, tile_len):
    '''gives the number of different block configs we can have for a total size of full_len, with tiles of length tile_len'''
    F, T = full_len, tile_len
    if T < F/2:
        count = 0
        for num_blocks in range(1,int(F/T)+1):
            spaces = F-T*num_blocks
            #print(F, T, num_blocks+spaces, num_blocks)
            count += perm(num_blocks+spaces, num_blocks)
    else:
        count = F - T + 1
    return count

def total_comb(full_len):
    '''gives the addition of the number of blocks, considering different tile lengths'''
    return sum([nb_blocks(full_len, i) for i in range(2, 5)])

print(total_comb(50))



# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))