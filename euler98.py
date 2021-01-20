#!/usr/bin/env python3
#
#euler98.py / anagramic squares
from os import chdir
from math import sqrt,floor
from itertools import permutations
answer=0

chiffres=[i for i in range(10)]

#definition 2 mots anagrammes
def isanagram(mot_1,mot_2):
    if len(mot_1)!=len(mot_2):
        return False
    else:
        for letter in mot_1:
            if mot_1.count(letter)!=mot_2.count(letter):
                return False
        for letter in mot_2:
            if mot_1.count(letter)!=mot_2.count(letter):
                return False
    return True
def issquare(x):
    if sqrt(x)==floor(sqrt(x)):
        return True
    else:
        return False
#


##repertoire et fichier
chdir('\\Users\\allagonne\\PycharmProjects\\Euler')
f = open("euler42_words.txt", 'r')
words_list = [strWord[1: -1] for strWord in f.read().split(",")]
f.close()
words_anagrams=[]

##extraire les anagrammes
for i in words_list:
    for j in words_list:
        if i!=j and isanagram(i,j)==True and [j,i] not in words_anagrams:
            words_anagrams.append([i,j])
print(words_anagrams)

for couple_of_anagrams in words_anagrams:
    for permuts in permutations(chiffres, len(couple_of_anagrams[0])):
        dico=dict()
        incr=0
        for letter in couple_of_anagrams[0]:
            dico[letter] = permuts[incr]
            incr+=1
        s,t='',''
        for letter in couple_of_anagrams[0]:
            s+=str(dico[letter])
        for letter in couple_of_anagrams[1]:
            t+=str(dico[letter])
        couple_in_numbers=[int(s),int(t)]
        if issquare(couple_in_numbers[0])==True and issquare(couple_in_numbers[1])==True:
            if s[0]!='0' and t[0]!='0':
                if couple_in_numbers[0] > answer or couple_in_numbers[1] > answer:
                    print(dico)
                    print(couple_in_numbers)
                    answer=max(couple_in_numbers[0],couple_in_numbers[1])

print('la réponse est', answer)