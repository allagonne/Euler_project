#!/usr/bin/env python3
#
#euler2.py / even fibonacci numbers
import time

# Debut du decompte du temps
start_time = time.time()

liste = [1,1]
max=4000000
tot=0
while liste[-1] < max:
    liste.append(liste[-1]+liste[-2])
    if liste[-1]%2==0:
        tot+=liste[-1]
print ("total : ", tot)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

