#!/usr/bin/env python3
#
#multiples of 3 and 5
i=1
maximum=1000
tot=0
while i < maximum: 
    if i%15==0:
        tot=tot+i
    elif i%5==0:
        tot=tot+i
    elif i%3==0:
        tot=tot+i
    i = i+1

print ("total : ", tot)

