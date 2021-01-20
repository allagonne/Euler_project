#!/usr/bin/env python3
#
# euler40 / champernowne's constant
s='0'
i=1
while True:
    s+=str(i)
    if len(s)>10**6:
        break
    i+=1
total=1
for i in range(7):
    total*=int(s[10**i])
print(total)
