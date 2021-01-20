#!/usr/bin/env python3
#
#euler39 / Integer right triangles
result_max=0
p_max=0
for p in range(1,1001):
    result=0
    for a in range(1,p):
        for b in range(a,p):
            if a**2+b**2==(p-a-b)**2:
                result+=1
                print(a,b,p-a-b,p)
            if result > result_max:
                result_max=result
                p_max=p
print(p_max,result_max)
