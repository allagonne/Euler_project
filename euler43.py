#!/usr/bin/env python3
#
# euler43 / Sub-string divisibility
import itertools
liste_pandigital=[]
for i in itertools.permutations('0123456789'):
    liste_pandigital.append(''.join(i))

#main loop
somme=0
for i in range(len(liste_pandigital)):
    s=liste_pandigital[i]
    if len(s)!=9:
        if int(s[7:10])%17==0:
            if int(s[6:9])%13==0:
                if int(s[5:8])%11==0:
                    if int(s[4:7])%7==0:
                        if int(s[5]) in [0,5]:
                            if int(s[2:5])%3==0:
                                if int(s[3]) in [0,2,4,6,8]:
                                    print(int(s))
                                    somme+=int(s)
print(somme)
