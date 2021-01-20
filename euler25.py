#!/usr/bin/env python3
#
i=1
j=1
max=4000000
list=[i,j]
while True: 
    i=i+j
    j=i+j
    list.append(i)
    list.append(j)
    if len(str(i)) == 1000:
        print(list.index(i)+1)
        break
    elif len(str(j)) == 1000:
        print(list.index(j)+1)
        break
