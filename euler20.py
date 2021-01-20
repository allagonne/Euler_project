#!/usr/bin/env python3
#
# euler20 / factorial digit sum

print('quel nombre?')
x=int(input())
def factoriel(n):
    j=1
    for i in range(2,n+1):
       j*=i
    return j
y=str(factoriel(x))
print('factoriel=',factoriel(x))

sum_factoriel=0
for i in y:
    sum_factoriel+=int(i)

print('somme de factoriel=',sum_factoriel)
