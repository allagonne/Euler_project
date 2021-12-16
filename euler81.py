#!/usr/bin/env python3
#
# euler81.py/path sum : two ways
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
    ## 1st row and 1st column are straightforward
    for i in range(1,df.shape[0]):
        distance[i,0] = distance[i-1,0] + df[i,0]
    for j in range(1,df.shape[1]):
        distance[0, j] = distance[0, j-1] + df[0, j]
    ## other points are the best between the last left and last up, plus the value in the matrix
    for i in range(1, df.shape[0]):
        for j in range(1, df.shape[1]):
            distance[i,j] = min(distance[i-1, j], distance[i, j-1]) + df[i,j]
    return distance


# main loop
## test with the 5*5 matrix
distance_mat_test = distance_mat(mat_test)
print("test best distance : ", distance_mat_test[mat_test.shape[0]-1, mat_test.shape[1]-1])

## idem with the 80*80 matrix
distance_mat_80 = distance_mat(mat)
print("80*80-matrix best distance : ", distance_mat_80[mat.shape[0]-1, mat.shape[1]-1])




# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
