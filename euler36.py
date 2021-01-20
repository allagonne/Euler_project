#!/usr/bin/env python3
#
list=[]

def palindrome_dec(x):
    y = ''
    for i in str(x):
        y=i+y
    if str(x) == y:
        return True
    else:
        return False

def palindrome_bin(x):
    y=bin(x)
    z=''
    for i in str(y):
        z=i+z
    if str(y[2:])==z[0:-2]:
        return True
    else:
        return False




for i in range(1000000):
    if palindrome_dec(i)==True and palindrome_bin(i)==True:
        list.append(i)
    
print(sum(list))
