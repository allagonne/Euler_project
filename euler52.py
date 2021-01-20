#!/usr/bin/env python3
#
# euler52 / permuted multiples 
j=1
while True:
    if sorted(str(j))==sorted(str(2*j))==sorted(str(3*j))==sorted(str(4*j))==sorted(str(5*j))==sorted(str(6*j)):
        print(j)
        break
    j+=1
