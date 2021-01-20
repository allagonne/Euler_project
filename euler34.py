#!/usr/bin/env python3
#
# euler34 / digit factorials
#definition fonctions

def factoriel(n):
    j=1
    for i in range(2,n+1):
       j*=i
    return j
def sum_factoriel(n):
    sum_factoriel=0
    for i in str(n):
        sum_factoriel+=factoriel(int(i))
    return sum_factoriel

sum_all_factoriels=0
for i in range(3,1000000):
    if sum_factoriel(i) == i:
        print(i)
        sum_all_factoriels+=i

print('somme de factoriel=',sum_all_factoriels)
