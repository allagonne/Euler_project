#!/usr/bin/env python3
#
# euler108 / Diophantine reciprocals I
import time

# Debut du decompte du temps
start_time = time.time()

def frac(x):
    if x==0:
        return 0
    else:
        y=float(1/x)
        return y

i=4
counter=0
while counter<1000:
    #epsilon=frac(i)/100000000
    i+=1
    counter=0
    ##determiner frac_max pour i
    test, frac_max = 0, 1
    while frac(i) - frac(i + 1) < frac(frac_max):
        frac_max += 1
    #print("pour i=", i, "et frac_max=", frac_max)
    for j in range(i,i*2+1):
        for k in range(j,frac_max):
            if frac(j)+frac(k)==frac(i):
                counter+=1
                #print(i,j,k)

print(i)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))