#!/usr/bin/env python3
#
#euler4.py / largest palindrome product
liste=[]

def ispalindrome(x):
    y=str(x)
    if y == y[::-1]:
        return True
    else:
        return False


for i in range(1000):
    for j in range(1000):
        if ispalindrome(i*j)==True:
            liste.append(i*j)
print(max(liste))
