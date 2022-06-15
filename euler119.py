#!/usr/bin/env python3
#
#euler119.py / digit power sum

import time
# Debut du decompte du temps
start_time = time.time()

def samesize(i, p):
    if sum([int(i) for i in str(i**p)]) == i:
        return True
    else:
        return False

def digitpowersums(l):
    '''max size of answers = l'''
    answers = []
    i=2
    while len(answers)<l:
        for power in range(2, 20):
            if samesize(i,power):
                #print(i,power)
                answers.append(i**power)
        i+=1
    return sorted(answers)

print(digitpowersums(40)[29])

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
