#!/usr/bin/env python3
#
#euler23 / Non-abundant sums

def divisors(n):
    divisors=[1]
    for i in range(2,int(n/2+1)):
        if n%i==0:
            divisors.append(i)
    return divisors

sumfactors=[0,1]
max=28123
for i in range(2,max+1):
    x=divisors(i)
    y=sum(x)
    sumfactors.append(y)

perfect,deficient,abundant=0,0,0
listabundant=[]
for i in range(max):
    if i>1:
        j=sumfactors[i]
        if j<max:
            if j==i:
                print('perfect',i,j)
                perfect+=1
            elif j>i:
                listabundant.append(i)
                abundant+=1
            else:
                deficient+=1
print(deficient,perfect,abundant)

listsumabundant=[]
for i in listabundant:
    for j in listabundant:
        if i+j<max:
            if i+j not in listsumabundant:
                listsumabundant.append(i+j)
notinlistsum=[]
for i in range(1,max+1):
    if i not in listsumabundant:
        notinlistsum.append(i)
print(notinlistsum)
print('somme',sum(notinlistsum))
