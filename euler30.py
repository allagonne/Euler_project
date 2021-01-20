#!/usr/bin/env python3
#
# euler30 / Digit fifth powers
list=[]
for i in range(2,999999):
    j=str(i)
    x=0
    for k in range(len(j)):
        x+=int(j[k])**5
    if x==i:
        list.append(i)
print(list)
print(sum(list))

