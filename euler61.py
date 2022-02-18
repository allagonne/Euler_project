#!/usr/bin/env python3
#
#euler61 / Cyclical figurate numbers

import time
import math

# Debut du decompte du temps
start_time = time.time()

class gen_polynoms:
    def __init__(self, sizemin, sizemax):
        self.sizemin = sizemin
        self.sizemax = sizemax

    def gen_triangles(self):
        n = 0
        returnlist = []
        P = n*(n+1)/2
        while P < self.sizemax :
            if P>self.sizemin and str(P)[2] != '0':
                returnlist.append(int(P))
            n+=1
            P = n*(n+1)/2
        return returnlist

    def gen_squares(self):
        n = 0
        returnlist = []
        P = n**2
        while P < self.sizemax :
            if P>self.sizemin and str(P)[2] != '0':
                returnlist.append(int(P))
            n+=1
            P = n**2
        return returnlist

    def gen_penta(self):
        n = 0
        returnlist = []
        P = n*(3*n-1)/2
        while P < self.sizemax :
            if P>self.sizemin and str(P)[2] != '0':
                returnlist.append(int(P))
            n+=1
            P = n*(3*n-1)/2
        return returnlist

    def gen_hexa(self):
        n = 0
        returnlist = []
        P = n*(2*n-1)
        while P < self.sizemax :
            if P>self.sizemin and str(P)[2] != '0':
                returnlist.append(int(P))
            n+=1
            P = n*(2*n-1)
        return returnlist

    def gen_hepta(self):
        n = 0
        returnlist = []
        P = n*(5*n-3)/2
        while P < self.sizemax:
            if P>self.sizemin and str(P)[2] != '0':
                returnlist.append(int(P))
            n+=1
            P = n*(5*n-3)/2
        return returnlist

    def gen_octa(self):
        n = 0
        returnlist = []
        P = n*(3*n-2)
        while P < self.sizemax :
            if P>self.sizemin and str(P)[2] != '0':
                returnlist.append(int(P))
            n+=1
            P = n*(3*n-2)
        return returnlist
def gen_next_possibilities(list_previous_possibilities):
    types_list = ['3', '4', '5', '6', '7']
    next_possibilities = []
    for i in list_previous_possibilities:
        previous_types = i[0]
        previous_numbers = i[1]
        if '7' not in previous_types:
            nextlist_hepta = [j for j in hepta if str(j)[0:2] == str(previous_numbers[-1])[-2:]]
            for j in nextlist_hepta :
                next_possibilities.append([previous_types + ['7'], previous_numbers + [j]])
        if '6' not in previous_types:
            nextlist_hexa = [j for j in hexa if str(j)[0:2] == str(previous_numbers[-1])[-2:]]
            for j in nextlist_hexa :
                next_possibilities.append([previous_types + ['6'], previous_numbers + [j]])
        if '5' not in previous_types:
            nextlist_penta = [j for j in penta if str(j)[0:2] == str(previous_numbers[-1])[-2:]]
            for j in nextlist_penta :
                next_possibilities.append([previous_types + ['5'], previous_numbers + [j]])
        if '4' not in previous_types:
            nextlist_squ = [j for j in squ if str(j)[0:2] == str(previous_numbers[-1])[-2:]]
            for j in nextlist_squ :
                next_possibilities.append([previous_types + ['4'], previous_numbers + [j]])
        if '3' not in previous_types:
            nextlist_tri = [j for j in tri if str(j)[0:2] == str(previous_numbers[-1])[-2:]]
            for j in nextlist_tri :
                next_possibilities.append([previous_types + ['3'], previous_numbers + [j]])
    return next_possibilities
#main
# generate all the polygon numbers as lists
gen_poly = gen_polynoms(sizemin = 1000, sizemax = 9999)
tri = gen_poly.gen_triangles()
squ = gen_poly.gen_squares()
penta = gen_poly.gen_penta()
hexa = gen_poly.gen_hexa()
hepta = gen_poly.gen_hepta()
octa = gen_poly.gen_octa()

next_possibilities = [] # start from octa
for i in octa:
    next_possibilities.append([['8'], [i]]) # init the chain
    next_possibilities = gen_next_possibilities(next_possibilities) # 2nd number
    next_possibilities = gen_next_possibilities(next_possibilities) # 3rd number
    next_possibilities = gen_next_possibilities(next_possibilities) # 4th number
    next_possibilities = gen_next_possibilities(next_possibilities) # 5th number
    next_possibilities = gen_next_possibilities(next_possibilities) # 6th number
    for j in next_possibilities:
        if str(j[1][-1])[-2:] == str(j[1][0])[:2]: # which one satisfies the chain loop?
            print(j, sum(j[1]))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))