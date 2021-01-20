#!/usr/bin/env python3
#
# euler29 / Distinct powers 
max=int(input('nombre max?'))
list=[]
for i in range(2,max+1):
    for j in range(2,max+1):
        list.append(i**j)
print('termes distincts', len(set(list)))

