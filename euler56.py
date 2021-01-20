#!/usr/bin/env python3
#
# euler56 / powerful digit sum
amax,bmax,sommemax=0,0,0
for a in range(1,100):
    for b in range(1,100):
        somme=0
        s=str(a**b)
        for i in s:
            somme+=int(i)
        if somme>sommemax:
            sommemax=somme
            amax=a
            bmax=b
print(amax,bmax,sommemax)

