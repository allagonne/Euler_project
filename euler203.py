#!/usr/bin/env python3
#
# euler203.py/Squarefree Binomial Coefficients

import time, math
import numpy as np

# Debut du decompte du temps
start_time = time.time()

## fonctions
def pascal_triangle(n):
    '''creates a pascal triangle of size n in the form of a matrix'''
    M = np.zeros([n,n]) ## init the matrix
    M[0,0] = 1
    for row in range(1,M.shape[0]):
        M[row, 0] = 1
        for col in range(1, M.shape[0]):
            M[row, col] = M[row-1, col-1] + M[row-1, col]
    return M

def is_squarefree(n):
    '''determinates if a number is square-free, i.e not divisible by any square number'''
    for i in range(2, int(n**(1/2))+1):
        if n%(i**2) == 0:
            return False
        else:
            continue
    return True

def sum_coeffs(n):
    ''' generates a unique list of numbers of euler triangle in the first n rows'''
    M = pascal_triangle(n)
    L = list(set(M.reshape(n**2)))
    newL = []
    for i in L:
        if is_squarefree(i) == True:
            newL.append(int(i))
    return sum(newL)

## main loop
n=51 # nb of rows
print(sum_coeffs(n))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
