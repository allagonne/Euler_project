#!/usr/bin/env python3
#
#euler125.py / palindromic sums
import math
limmax=10**8
limmaxsqrt=int(math.sqrt(limmax))+1
def ispalindrome(x):
    y=str(x)
    if y == y[::-1]:
        return True
    else:
        return False
listsquares=[x**2 for x in range(0,limmaxsqrt)]

#main loop
listanswers=[]
for x in range(1,len(listsquares)):
    for y in range(x+1,len(listsquares)):
        somme=sum(listsquares[x:y+1])
        if somme>=limmax:
            break
        if ispalindrome(somme)==True and somme<limmax:
            print(somme,x,y)
            listanswers.append(somme)
print('total',sum(set(listanswers)))
