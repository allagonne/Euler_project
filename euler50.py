#!/usr/bin/env python3
#
# euler50 / consecutive prime sums 
import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True

#fabrication des nombres premiers
listprimes=[2]
i=3
while i<10**4:
    if isprime(i)==True:
        listprimes.append(i)
    i+=2
print(listprimes)

#main loop
A=[]
maxlongueur=0
for x in range(0,len(listprimes)-1):
    for y in range(x+1,len(listprimes)):
        somme=sum(listprimes[x:y])
        if somme < 1000000 and isprime(somme)==True and y-x>maxlongueur:
            maxlongueur=y-x
            A.append(somme)
print(A)
print(max(A))


