#!/usr/bin/env python3
#
# euler82.py/path sum : three ways
import time
import numpy as np

# Debut du decompte du temps
start_time = time.time()

## create matrix
mat = np.loadtxt("euler81_matrix.txt",dtype = int, delimiter=",")
mat_test = np.array([[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]])

## functions
def distance_mat(df):
    '''function used to compute the minimum distance from every point to the top up left'''
    distance = np.full(df.shape, np.inf)
    distance[0,0] = df[0,0]
    ## init : 1st column to fill with its own value
    for i in range(1,df.shape[0]):
        distance[i,0] = df[i,0]
    ## for every column, init the first row, then for every row :
    ## - take the min distance from top or left
    ## - check if every value before is indeed the minimum
    for j in range(1, df.shape[1]):
        distance[0,j] = distance[0,j-1] + df[0,j]
        for i in range(1,df.shape[0]):
            distance[i,j] = min( distance[i,j-1] + df[i,j] , distance[i-1,j] + df[i,j])
            for prev in range(1, j+1):
                if distance[i-prev,j] > distance[i-prev+1,j] + df[i-prev,j]:
                    distance[i-prev, j] = distance[i-prev+1,j] + df[i-prev,j]

    return distance

# main loop
## test with the 5*5 matrix
distance_mat_test = distance_mat(mat_test)
print(mat_test, '\n',distance_mat_test)
print("test best distance : ", np.amin(distance_mat_test[:,-1]))
## idem with the 80*80 matrix
distance_mat_80 = distance_mat(mat)
print("80*80-matrix best distance : ", np.amin(distance_mat_80[:,-1]))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
