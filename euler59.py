#!/usr/bin/env python3
#
#euler59 / XOR decryption
import os,time

# Debut du decompte du temps
start_time = time.time()

os.chdir("C:/Users/allag/PycharmProjects/Euler/euler_scripts")
with open("euler59.txt", "r") as txt:
    contenu=txt.read()
print(contenu)
liste=[int(x) for x in contenu.split(",")]
print(liste)

def dectochar_ascii(liste):
    '''convert decimal to ascii characters'''
    answer = []
    for i in liste:
        answer.append(chr(i))
    return answer

def xor_on_list(liste, xor):
    '''apply an xor value to a list of decimal values'''
    answer=[]
    for i in liste:
        answer.append(i^xor)
    return answer

## separate the ciphered text into 3 lists, since the length of the key is 3
liste_0 = [liste[i] for i in range(len(liste)) if i%3 == 0]
liste_1 = [liste[i] for i in range(len(liste)) if i%3 == 1]
liste_2 = [liste[i] for i in range(len(liste)) if i%3 == 2]

## testing the unciphered text with ascii values from 97 to 122 ('a' to 'z')
dec_liste_0 = dectochar_ascii(xor_on_list(liste_0, 101)) ## key#0 = ascii 101 = 'e'
dec_liste_1 = dectochar_ascii(xor_on_list(liste_1, 120)) ## key#1 = ascii 120 = 'x'
dec_liste_2 = dectochar_ascii(xor_on_list(liste_2, 112)) ## key#1 = ascii 112 = 'p'

## re_create the unciphered text
dec_liste = []
for i in range(len(liste)):
    if i%3 == 0:
        dec_liste.append(dec_liste_0.pop(0))
    elif i%3 == 1:
        dec_liste.append(dec_liste_1.pop(0))
    elif i%3 == 2:
        dec_liste.append(dec_liste_2.pop(0))
print(dec_liste)
## plain text
print(''.join(dec_liste))

## total of the ascii values of the unciphered text
total = 0
for i in dec_liste:
    total+=ord(i)
print(total)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))