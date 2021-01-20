#!/usr/bin/env python3
#
#euler111.py / primes with runs
from math import sqrt
import time

# Debut du decompte du temps
start_time = time.time()

def isprime(x):
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

liste_chiffres = [i for i in range(10)]
liste_chiffres_sans_zero = [i for i in range(1,10)]
liste_impair = [2*i+1 for i in range(5)]

def calcul(n,d):
    nb_premiers=0
    liste_premiers=[]
    if d == 0 : ## cas d = 0 : tests x00...00x
        for i in liste_chiffres_sans_zero:
            for j in liste_impair:
                my_string=str(i)+'0'*(n-2)+str(j)
                if isprime(int(my_string)) == True:
                    liste_premiers.append(int(my_string))
                    nb_premiers = n-2
    elif d%2 == 0: ## cas d = pair : tests dd...ddx
        for i in liste_impair:
            if isprime(int(str(d)*(n-1)+str(i))) == True: ## type 1113/1115/1117/1119
                liste_premiers.append(int(str(d)*(n-1)+str(i)))
                nb_premiers = n-1
        if nb_premiers == 0: ##pas de nb premier de type dd...ddx
            nb_premiers = n-2
            for shift in range(n-1):
                for impair in liste_impair:
                    liste_test = [int(str(d) * shift + str(i) + str(d) * (n - shift - 2) + str(impair)) for i in range(10)]
                    for test in liste_test:
                        if isprime(test) == True and len(str(test)) == n:
                            liste_premiers.append(test)
    else : ## cas d = impair : tests dd...ddx
        for i in liste_impair:
            if isprime(int(str(d)*(n-1)+str(i))) == True: ## type 1113/1115/1117/1119
                liste_premiers.append(int(str(d)*(n-1)+str(i)))
                nb_premiers = n-1
        for shift in range(n-1):
            liste_test = [int(str(d)*shift + str(i) + str(d) * (n-shift-1)) for i in range(10)] #type 1011/1111/1211/1311...
            for test in liste_test:
                if isprime(test) == True :
                    liste_premiers.append(test)
                    nb_premiers = n - 1
    return nb_premiers,liste_premiers

#main loop
n=10
total_sum=0
for d in range(10):
    M,liste = calcul(n,d)[0],calcul(n,d)[1]
    N=len(liste)
    S=0
    for i in liste:
        S+=i
    print(d,M,N,S,liste)
    total_sum+=S
print(total_sum)



# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

