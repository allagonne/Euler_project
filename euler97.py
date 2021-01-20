#!/usr/bin/env python3
#
#euler97.py / large non-mersenne prime
m=1
power_of_two=7830457
for i in range(power_of_two):
    m*=2
    s=str(m)
    if len(s)>10:
        s=s[-10:]
    m=int(s)
    i+=1

print(m)
result=28433*m+1
s=str(result)
s=s[-10:]
result=int(s)
print(result)
