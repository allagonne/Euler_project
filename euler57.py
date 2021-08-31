#!/usr/bin/env python3
#
#euler57 / Square root convergents
import time
#from fractions import Fraction
#from decimal import Decimal

# Debut du decompte du temps
start_time = time.time()

def approx_frac_of_two(n):
    return_list = [[3,2]]
    if n == 1:
        pass
    elif n > 2:
        return_list.append([7, 5])
        for i in range(3,n+1):
            n_minus_one, n_minus_two = return_list[-1], return_list[-2]
            num = 2*n_minus_one[0] + n_minus_two[0]
            denom = n_minus_one[0] + n_minus_one[1]
            return_list.append([num,denom])
    return return_list

# main
count = 0
frac = approx_frac_of_two(1000)
for i in frac:
    if len(str(i[0])) > len(str(i[1])):
        count+=1
print(count)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))