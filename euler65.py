#!/usr/bin/env python3
#
#euler65 / Convergents of e
import time

# Debut du decompte du temps
start_time = time.time()

def count_digits(n):
    return sum([int(i) for i in str(n)])

def gen_e():
    e = [2, 1]
    for i in range(1, 34):
        e.append(2 * i)
        e.append(1)
        e.append(1)
    return e

# main
e = gen_e()
# construct numerator and denominator list
num_list = [2,3]
denom_list = [1,1]
for i in range(2,100):
    num_list_last = num_list[-1]*e[i]+num_list[-2]
    denom_list_last = denom_list[-1]*e[i]+denom_list[-2]
    num_list.append(num_list_last)
    denom_list.append(denom_list_last)
    print(i+1, e[i], count_digits(num_list[-1]), num_list[-1], denom_list[-1])

print(count_digits(num_list[-1]))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))