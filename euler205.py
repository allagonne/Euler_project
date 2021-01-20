#!/usr/bin/env python3
#
#euler205.py/dice game

from itertools import product
pyramidal_dice=['1','2','3','4']
cubic_dice=['1','2','3','4','5','6']

pyramidal_possibilities=[]
cubic_possibilities=[]

def expand_possibilities(list,nb):
    list_string=''
    for i in list:
        list_string+=i
    p = product(list_string,repeat=nb)
    list_return=[i for i in p]
    return list_return

##calcul de toutes les possibilités
pyramidal_possibilities=expand_possibilities(pyramidal_dice,9)
cubic_possibilities=expand_possibilities(cubic_dice,6)

pyramidal_total,cubic_total=[],[]
for i in pyramidal_possibilities:
    total=0
    for j in range(len(i)):
        total+=int(i[j])
    pyramidal_total.append(total)
for i in cubic_possibilities:
    total=0
    for j in range(len(i)):
        total+=int(i[j])
    cubic_total.append(total)

total,p_greater_than_c=0,0
for i in pyramidal_total:
    for j in cubic_total:
        total+=1
        if i>j:
            p_greater_than_c+=1

print(p_greater_than_c,total)
print("ratio=",p_greater_than_c/total)