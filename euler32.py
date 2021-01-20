#!/usr/bin/env python3
#
# euler32 / pandigital products

def ispandigital(n):
    if n>=10**9 or n<10**8:
        return False
    else:
        s=str(n)
        if '0' in s:
            return False
        for i in range(1,10):
            if str(i) in s:
                continue
            else:
                return False
        return True

##main loop
##max 10 digits : si a=2 (meilleur cas), b<10000)
liste=[]
total=0
for a in range(1000):
    for b in range(a,10000):
        c=a*b
        s=str(a)+str(b)+str(c)
        if ispandigital(int(s))==True:
            print(a,b,c)
            if c not in liste:
                liste.append(c)
print(liste)
total=sum(liste)
print(total)

