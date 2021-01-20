#!/usr/bin/env python3
#
div=500
triangle=[]
x=0
i=0
while True:
    x=x+i+1
    triangle.append(x)
    diviseurs=[1]
    for j in range(2,int(x/2)):
        if x%j==0:
            diviseurs.append(j)
    if len(diviseurs) > div-1:
        break
    i=i+1
print(len(diviseurs),diviseurs)
print(i,triangle[-1])

