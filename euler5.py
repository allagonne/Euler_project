#!/usr/bin/env python3
#
#euler5 / smallest multiple

max_factor=20
x=2
A=[j for j in range(2,max_factor+1)]

while True:
    test=0
    for i in A:
        if x%i!=0:
            test+=1
            break
    if test == 0:
        print(x)
        break
    x+=1
