#!/usr/bin/env python3
#
# euler67.py/maximum path sum II/no bruteforce
import time
import numpy as np

# Debut du decompte du temps
start_time = time.time()

# traitement fichier => array
f = open("euler67_triangle.txt", 'r')
triangle_str_list = [row for row in f.read().split("\n")]
f.close()
triangle_list = []
for s in triangle_str_list:
    row = [int(i) for i in s.split()]
    triangle_list.append(row)
print(triangle_list)

## main
max_distance_array = np.full((len(triangle_list[-1]), len(triangle_list[-1])), np.inf)
print(max_distance_array)
#init : first and last column = left path + right path
max_distance_array[0,0] = triangle_list[0][0]
for i in range(1, len(max_distance_array)):
    max_distance_array[i,0] = max_distance_array[i-1,0] + triangle_list[i][0]
    max_distance_array[i,i] = max_distance_array[i-1,i-1] + triangle_list[i][i]
##second step, compute the max distance for all other locations
for i in range(2, len(max_distance_array)):
    for j in range(1,i):
        max_distance_array[i,j] = max(max_distance_array[i-1,j-1]+triangle_list[i][j], max_distance_array[i-1,j]+triangle_list[i][j])
print(max(max_distance_array[-1,]))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
