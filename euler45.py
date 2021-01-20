#!/usr/bin/env python3
#
T=[]
P=[]
H=[]
for x in range(1,100000):
    T.append(x*(x+1)/2)
for x in range(1,100000):
    P.append(x*(3*x-1)/2)
for x in range(1,100000):
    H.append(x*(2*x-1))

for i in range(1,99999):
    if T[i] in P and T[i] in H:
        print(T[i])

