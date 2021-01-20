#!/usr/bin/env python3
#
list=[]
diff = 1000000000
for x in range(1,5000):
    list.append(x*(3*x-1)/2)
print(list)
for i in range(1,4000):
    for j in range(1,4000):
        k=list[j]-list[i]
        l=list[i]+list[j]
        if (k in list) and (l in list) and i<j:
            if list[j]-list[i]<diff:
                print(list[j]-list[i],i,list[i],j,list[j])

