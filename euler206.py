#!/usr/bin/env python3
#
#euler206.py/concealed square
import math
maximum=int(math.sqrt(2)*10**9)
i=10**9
while i<maximum:
    s=str(i**2)
    if s[0::2]=='1234567890':
        print(i)
        break
    i+=10
