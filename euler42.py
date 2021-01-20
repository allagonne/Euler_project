#!/usr/bin/env python3
#
#euler42.py / coded triangle numbers
triangle=[]
for n in range(1,30):
    value=n*(n+1)/2
    triangle.append(value)
def istriangle(x):
    if x in triangle:
        return True
    else:
        return False

f=open("euler42_words.txt","rb")
contenu=f.readline()
f.close()
words=[]
compteur,valeur_mot = 0, 0
for i in contenu:
    if i==34:
        if istriangle(valeur_mot)==True:
            compteur+=1
    elif i==44:
        valeur_mot=0
    else:
        valeur_mot+=i-64
print(compteur)

