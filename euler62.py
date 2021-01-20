#!/usr/bin/env python3
#
#euler62 / cubic permutations

cubic=[]
sortedcubic=[]
joinsortedcubic=[]


#main loop
i=0
while True:
    cubic.append(i**3)
    sortedcubic.append(sorted(str(i**3)))
    x=''.join(sortedcubic[i])
    joinsortedcubic.append(x)
    compteur=joinsortedcubic.count(joinsortedcubic[i])
    if compteur==5:
        print(joinsortedcubic.index(x),cubic[joinsortedcubic.index(x)])
        break 
    i+=1
