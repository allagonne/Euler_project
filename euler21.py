#!/usr/bin/env python3
#
#euler21 / Amicable numbers

def divisors(n):
    divisors=[1]
    for i in range(2,int(n/2+1)):
        if n%i==0:
            divisors.append(i)
    return divisors

sumfactors=[0,1]
max=10000
for i in range(2,max+1):
    x=divisors(i)
    y=sum(x)
    sumfactors.append(y)

print(sumfactors)
totalsum=0
for i in range(max):
    if i>1:
        j=sumfactors[i]
        if j<max:
            if sumfactors[i]==j and sumfactors[j]==i and i!=j:
                print(i,sumfactors[i])
                totalsum+=i
print(totalsum)

