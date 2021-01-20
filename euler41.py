#!/usr/bin/env python3
#
# euler41 / pandigital primes
import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            continue
    return True

def ispandigital(n):
    if n>=10**10:
        return False
    else:
        s=str(n)
        for i in range(1,len(s)+1):
            if str(i) in s:
                continue
            else:
                return False
                break
        return True

##main loop
##since pandigital numbers of 8 and 9 digits like 12345678 and 123456789 are divisible by 3, the test is limited to 7-digit numbers

i=9999999
while True:
    if isprime(i)==True and ispandigital(i)==True:
        print(i)
        break
    i-=2

