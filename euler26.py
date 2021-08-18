#!/usr/bin/env python3
#
#euler26 / reciprocal cycles
import time

# Debut du decompte du temps
start_time = time.time()

# fonctions
def division(x,y):
    '''gives if the fraction of x/y is a recurring cycle (boolean), the result of the fraction (string) and the remainings of the euclidian division (list)'''
    result = '0.'
    remainings = []
    test = 1
    recur = 0
    while test == 1:
        x *= 10
        while x < y:
            result = result + '0'
            x *= 10
        result = result + str(x//y)
        if str(x%y) not in remainings and x%y != 0:
            remainings.append(str(x%y))
            x = x%y
        else:
            if str(x%y) in remainings :
                recur = 1
            test = 0
    return recur, result, remainings


# main loop
thr = 1
for i in range(2,1000):
    div = division(1,i)
    if div[0] == 1 and len(div[2]) > thr : ## if it is a recurring fraction and the length of the remainings is bigger than the previous result
        thr = len(div[2]) ##update the remaining result threshold
        print(i,div[1], div[2]) ##print the i and the results for which the fraction is bigger

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))