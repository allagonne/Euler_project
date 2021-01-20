#!/usr/bin/env python3
#
#euler2.py / even fibonacci numbers
i=1
j=2
max=4000000
tot=0
tot=tot+j
while i < max or j < max: 
    i=i+j
    j=i+j
    print(i,j)
    if i%2==0:
        tot=tot+i 
    if j%2==0:
        tot=tot+j
print ("total : ", tot)

