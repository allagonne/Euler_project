#!/usr/bin/env python3
#
#euler15bis / lattice paths
#x=gridsize
lattice_paths_list=[0,2,6]
def lattice_paths(x,y):
    total=0
    if x==y and x<len(lattice_paths_list):
        total=lattice_paths_list[x]
    elif x==0 or y==0:
        total=1
    elif x>0 and y>0:
        total=lattice_paths(x,y-1)+lattice_paths(y,x-1)
    return total

for i in range(3,21):
    lattice_paths_list.append(lattice_paths(i,i))
print(lattice_paths(20,20))
