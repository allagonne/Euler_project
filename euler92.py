#!/usr/bin/env python3
#
#euler92.py / square digit chains 
maximum=10000000
import math
total=0

for i in range(1,maximum):
    s=str(i)
    sq=sum([int(j)**2 for j in s])
    while sq!=1 and sq!=89:
        s=str(sq)
        sq=sum([int(j)**2 for j in s])
    if sq==89:
        total+=1

print(total)
