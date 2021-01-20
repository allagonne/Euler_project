#!/usr/bin/env python3
#
#euler120.py / square remainders
##optimisable avec la fonction remainder:
#def remainder(a):
#    if a%2==0:
#        r=a*(a-2)
#    else:
#        r=a*(a-1)
#    return r
import time

# Debut du decompte du temps
start_time = time.time()

def remainder(a,n):
    r=((a-1)**n+(a+1)**n) % (a**2)
    return r
somme_maximums=0
for a in range(3,1001):
    maximum=max([remainder(a,n) for n in range(1,1001)])
    print(a,maximum)
    somme_maximums+=maximum

print(somme_maximums)
# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))