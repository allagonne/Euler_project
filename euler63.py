#!/usr/bin/env python3
#
#euler63 / Powerful digit counts
count=0

for i in range(1,50):
    valeur=1
    while len(str(valeur**i))<=i:
        if len(str(valeur**i))==i:
            count+=1
            print(valeur, i , valeur**i)
        valeur+=1

print(count)