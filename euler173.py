#!/usr/bin/env python3
#
# euler173 / Using up to one million tiles how many different "hollow" square laminae can be formed?
#
import time

# Debut du decompte du temps
start_time = time.time()

def hollow(size, tiles_max):
    return_list = []
    if size > 2:
        sizemin = size -2
        while (sizemin > 0):
            if (size ** 2 - sizemin ** 2) > tiles_max:
                break
            return_list.append(size**2-sizemin**2)
            sizemin = sizemin - 2
    return return_list

def total_hollow(max_size, tiles_max):
    return_list = []
    for i in range(1, max_size+1):
        for j in hollow(i, tiles_max):
            return_list.append(j)
    return return_list

##main loop
print(len(total_hollow(300001, 1000000)))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
