#!/usr/bin/env python3
#
# euler74 / digit factorial chains

def factoriel(x):
    j=1
    for i in range(2,x+1):
       j*=i
    return j
def sum_factoriel(x):
    sum_factoriel=0
    for i in str(x):
        sum_factoriel+=factoriel(int(i))
    return sum_factoriel

liste_factoriels=[factoriel(i) for i in range(10)]

maximum=1000000
i=2
result=0
while i<maximum:
    nonrep=1
    test=0
    repnumbers=[i]
    s=i
    while test==0:
        s=sum_factoriel(s)
        if s in repnumbers:
            test=1
            if nonrep==60:
                print(i)
                result+=1
        else:
            repnumbers.append(s)
            nonrep+=1
    i+=1
print(result)
