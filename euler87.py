#!/usr/bin/env python3
#
#euler87.py / Prime power triples

import math,time

# Debut du decompte du temps
start_time = time.time()

prime_numbers_deux,prime_numbers_trois,prime_numbers_quatre=[],[],[]
def isprime(x):
    squareroot=int(math.sqrt(x))+1

    for i in range(2,squareroot):
        if x%i==0:
            return False
        else:
            continue
    return True

max=50000000
##determiner le nb premier maximum
prime_max_deux, prime_max_trois,prime_max_quatre=0,0,0
for i in range(2,math.ceil(math.sqrt(max-2**3-2**4))):
    if isprime(i)==True:
        prime_max_deux=i
for i in range(2,math.ceil((max-2**2-2**4)**(1/3))):
    if isprime(i)==True:
        prime_max_trois=i
for i in range(2,math.ceil(math.sqrt(math.sqrt(max-2**3-2**2)))):
    if isprime(i)==True:
        prime_max_quatre=i
print(prime_max_deux, prime_max_trois,prime_max_quatre)
for i in range(2,prime_max_deux+1):
    if isprime(i)==True:
        prime_numbers_deux.append(i)
for i in range(2,prime_max_deux+1):
    if isprime(i)==True:
        prime_numbers_trois.append(i)
for i in range(2,prime_max_deux+1):
    if isprime(i)==True:
        prime_numbers_quatre.append(i)


answers=[]
for i in prime_numbers_deux:
    for j in prime_numbers_trois:
        if (i**2+j**3)<max:
            for k in prime_numbers_quatre:
                number=i**2+j**3+k**4
                if number<max:
                    answers.append(number)
                    #print(i,j,k,number)

my_set=set(answers)
print(len(my_set))
# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))