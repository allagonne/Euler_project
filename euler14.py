#!/usr/bin/env python3
#
#euler14.py / longest Collatz sequence
max=1000000
maxlen=0
max_x=0
for n in range(2,max):
    suite=[]
    suite.append(n)
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        suite.append(n)
    if len(suite) > maxlen:
        maxlen=len(suite)
        #print(suite)
        #print(len(suite))
        max_x=suite[0]

print(maxlen)
print(max_x)

