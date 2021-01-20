#!/usr/bin/env python3
#
# euler24 / lexicographic permutations
import itertools
x=itertools.permutations('0123456789')

liste_permut=[''.join(p) for p in x]
print(liste_permut[1000000-1])
