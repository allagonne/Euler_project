#!/usr/bin/env python3
#
#euler28 / number spiral diagonals

grid=1001
total=1
for j in range(2,grid,2):
    for i in range(1,5):
        total+=(j-1)**2+j*i
print(total)
