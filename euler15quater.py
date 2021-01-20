#!/usr/bin/env python3
#
#euler15quater / lattice paths / by two
#x=gridsize
lattice_paths_list=[0,2,6]
def lattice_paths(x,y):
    total=0
    if x==y and x < len(lattice_paths_list):
        total=lattice_paths_list[x]
    elif x==0 or y==0:
        total=1
    elif x==1 or y==1:
        total=lattice_paths(x,y-1)+lattice_paths(y,x-1)
    elif x>1 and y>1:
        total=2*lattice_paths(x-1,y-1)+lattice_paths(x,y-2)+lattice_paths(x-2,y)
    return total

for i in range(3,21):
    lattice_paths_list.append(lattice_paths(i,i))
print(lattice_paths(20,20))
