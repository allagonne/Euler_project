#!/usr/bin/env python3
#
# euler51 / prime digit replacements
# not a very good code, but works

from euler_scripts.utils import isprime
import time

# Debut du decompte du temps
start_time = time.time()

def gen_primes(num_digits=2):
    '''returns all primes with length num_digits'''
    return_list = []
    for i in range(10**(num_digits-1)+1, 10**(num_digits), 2):
        if isprime(i):
            return_list.append(i)
    return_list = [str(i) for i in return_list]
    return return_list

def form(mylist, string):
    '''returns if the string applies to some values of the list'''
    return_list = []
    for i in range(10):
        tested_num = string
        tested_num = tested_num.replace('x', str(i))
        if tested_num in mylist:
            return_list.append(tested_num)
    return return_list

## main
primes_6 = gen_primes(6)
family = 8
for i in ['1', '3', '7', '9']:
    for j in range(1,10):
        for h in range(1,10):
            test_form = form(primes_6, str(j) + str(h) + 'xxx' + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, str(j) + 'x' + str(h) + 'xx' + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, str(j) + 'xx' + str(h) + 'x' + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, str(j) + 'xxx' + str(h) + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, 'x' + str(j) + str(h) + 'xx' + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, 'x' + str(j) + 'x' + str(h) + 'x' + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, 'x' + str(j) + 'xx' + str(h) + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, 'xx' + str(j) + str(h) + 'x' + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, 'xx' + str(j) + 'x' + str(h) + i)
            if len(test_form) >= family:
                print(test_form)
            test_form = form(primes_6, 'xxx' + str(j) + str(h) + i)
            if len(test_form) >= family:
                print(test_form)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))