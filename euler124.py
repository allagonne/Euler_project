#!/usr/bin/env python3
#
# euler124 / Ordered radicals

import time
# Debut du decompte du temps
start_time = time.time()

##fonctions
def rad(n):
    d=2
    l=3
    factors=[]
    while n%2==0:
        n=n/2
        factors.append(2)
    while l <= n:
        while n%l==0:
            n=n/l
            factors.append(l)
        l=l+2
    rad=1
    for i in list(set(factors)):
        rad*=i
    return rad

##main loop
maximum=100000
list_n_rad_n=[]
for i in range(1,maximum+1):
    rad_value_of_i=rad(i)
    list_n_rad_n.append([rad_value_of_i,i])
print(list_n_rad_n)
list_total_sorted=sorted(list_n_rad_n)
concatenated_list=[]
#for k in range(1,maximum+1):
#    concatenated_list.append([k,list_total_sorted[k-1][0],list_total_sorted[k-1][1]])
k=10000
print(list_total_sorted[k-1][1])
# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))