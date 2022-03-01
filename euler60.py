#!/usr/bin/env python3
#
# euler60 / prime pair sets
import time
import math

# Debut du decompte du temps
start_time = time.time()

def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
        else:
            continue
    return True

class primesets:
    def __init__(self, maximum) -> None:
        self.maximum = maximum
        self.primepairs = self.gen_primepairsets()

    def gen_primepairsets(self):
        gen_list = []
        for i in range(2, self.maximum + 1):
            if isprime(i):
                for j in range(i + 1, self.maximum + 1):
                    if isprime(j):
                        if isprime(int(str(i) + str(j))) and isprime(int(str(j) + str(i))):
                            gen_list.append([i, j])
        return gen_list

    def gen_primetriosets(self):
        primepairs = self.primepairs
        gen_list = []
        for i in range(len(primepairs)):
            for j in range(i + 1, len(primepairs)):
                if primepairs[i][0] == primepairs[j][0] and [primepairs[i][1], primepairs[j][1]] in self.primepairs:
                    gen_list.append([primepairs[i][0], primepairs[i][1], primepairs[j][1]])
        return gen_list

    def gen_primequadsets(self):
        primetrios = self.gen_primetriosets()
        gen_list = []
        for i in range(len(primetrios)):
            for j in range(i + 1, len(primetrios)):
                if primetrios[i][:2] == primetrios[j][:2] and [primetrios[i][2], primetrios[j][2]] in self.primepairs:
                    gen_list.append([primetrios[i][0], primetrios[i][1], primetrios[i][2], primetrios[j][2]])
        return gen_list

    def gen_primequintsets(self):
        primequads = self.gen_primequadsets()
        gen_list = []
        for i in range(len(primequads)):
            for j in range(i + 1, len(primequads)):
                if primequads[i][:3] == primequads[j][:3] and [primequads[i][3], primequads[j][3]] in self.primepairs:
                    gen_list.append(
                        [primequads[i][0], primequads[i][1], primequads[i][2], primequads[i][3], primequads[j][3]])
        return gen_list

primesets = primesets(maximum = 10000)
A = primesets.gen_primequintsets()
for i in A:
    print(i, sum(i))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))