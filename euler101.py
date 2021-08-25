#!/usr/bin/env python3
#
#euler101.py / Optimum polynomial
import time
import numpy as np

# Debut du decompte du temps
start_time = time.time()

def gen_sequence(polynom,k):
    '''generates the sequence of k first terms of the polynom'''
    sequence = []
    for i in range(1,k+1):
        term = 0
        for j in range(len(polynom)):
            term += polynom[j]*(i**j)
        sequence.append(term)
    return sequence

def gen_solved(M, N):
    x = np.linalg.solve(M, N)
    answer = []
    answer2 = []
    for i in x:
        j=round(i, 5)
        answer.append(j)
    for i in range(len(answer)):
        answer2.append(answer[len(answer)-i-1])
    return answer2

def gen_Amatrix(n):
    M = np.ones((n))
    for j in range(2, n+1):
        M = np.vstack([M, [j ** (i-1) for i in range(n, 0, -1)]])
    return M


#main loop
print('\npolynom_test part')
polynom_test = [0,0,0,1]
seq_test = gen_sequence(polynom_test,10)
print(seq_test)

total = 0
for i in range(1,4):
    if i == 1:
        total += seq_test[0]
    else :
        A, B = gen_Amatrix(i), np.array(seq_test[0:i])
        seq = gen_sequence(gen_solved(A, B), 10)
        total += gen_sequence(gen_solved(A,B),10)[i]
print(total)

print('\npolynom_real part')
polynom_real = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
seq_real = gen_sequence(polynom_real,11)
print(seq_real)
total = 0
for i in range(1,11):
    if i == 1:
        total += seq_real[0]
    else :
        A, B = gen_Amatrix(i), np.array(seq_real[0:i])
        seq = gen_sequence(gen_solved(A, B), 11)
        print(seq_real)
        print(seq)
        print('adding', seq[i])
        total += seq[i]
print('total = ', total)


# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

