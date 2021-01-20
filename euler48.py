#!/usr/bin/env python3
#
#euler48 / self powers

x=0
total=0
for i in range(1,1000):
    x=i**i
    s=str(x)
    total+=int(s[-10:])

s=str(total)
total=int(s[-10:])
print(total)
