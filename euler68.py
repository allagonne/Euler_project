#!/usr/bin/env python3
#
#euler68.py / Magic 5-gon ring
import time

# Debut du decompte du temps
start_time = time.time()

from itertools import permutations


def str2int(mylist):
    return [int(i) for i in mylist]

def solutions_5gon():
    return_list = []
    perm = permutations('0123456789', 10)
    for i in perm:
        (A, B, C, D, E, F, G, H, I, J) = i
        [A, B, C, D, E, F, G, H, I, J] = str2int([A, B, C, D, E, F, G, H, I, J])
        [A, B, C, D, E, F, G, H, I, J] = [i + 1 for i in
                                          [A, B, C, D, E, F, G, H, I, J]]  # shift by 1 to have nb from 1 to 10
        if A + B + C == D + C + E and D + C + E == F + E + G and F + E + G == H + G + I and H + G + I == J + I + B:
            # print(A,B,C, ' ',D, C, E, ' ', F, E, B, A+B+C)
            if A == min(A, D, F, H, J):
                min_tri = [A, B, C]
                sec_tri, thi_tri, fou_tri, fif_tri = [D, C, E], [F, E, G], [H, G, I], [J, I, B]
            elif D == min(A, D, F, H, J):
                min_tri = [D, C, E]
                sec_tri, thi_tri, fou_tri, fif_tri = [F, E, G], [H, G, I], [J, I, B], [A, B, C]
            elif F == min(A, D, F, H, J):
                min_tri = [F, E, G]
                sec_tri, thi_tri, fou_tri, fif_tri = [H, G, I], [J, I, B], [A, B, C], [D, C, E]
            elif H == min(A, D, F, H, J):
                min_tri = [H, G, I]
                sec_tri, thi_tri, fou_tri, fif_tri = [J, I, B], [A, B, C], [D, C, E], [F, E, G]
            elif J == min(A, D, F, H, J):
                min_tri = [J, I, B]
                sec_tri, thi_tri, fou_tri, fif_tri = [A, B, C], [D, C, E], [F, E, G], [H, G, I]
            chain = [A + B + C, min_tri, sec_tri, thi_tri, fou_tri, fif_tri]
            if chain not in return_list:
                return_list.append(chain)
    return return_list

def get_max_answer(mylist, len_nb=0):
    a = [i[1] + i[2] + i[3] + i[4] + i[5] for i in mylist]
    concat_a = [int(''.join([str(i) for i in elmt])) for elmt in a]
    if len_nb == 0:
        pass
    else:
        concat_a = [i for i in concat_a if len(str(i)) == len_nb]
    return max(concat_a)

#main loop
print(get_max_answer(solutions_5gon(), 16))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

