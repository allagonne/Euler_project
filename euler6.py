#!/usr/bin/env python3
#
max=101
list=[j for j in range(max+1)]
print(list)
sumsquare=0
squaresum=0
for i in range(max):
    sumsquare=i**2+sumsquare
    squaresum=i+squaresum
    i=i+1
squaresum=squaresum**2
print(sumsquare)
print(squaresum)

diff = squaresum-sumsquare
print(diff)
