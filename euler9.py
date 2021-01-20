#!/usr/bin/env python3
#
result=0
for a in range(1,1000):
    for b in range(1,1000):
        csqrd=a**2+b**2
        c=(1000-a-b)**2
#        print(csqrd,a,b,c)
        if csqrd == c:
            result=a*b*(1000-a-b)
            list=[a,b,(1000-a-b)]
print(result)
print(list)
