#!/usr/bin/env python3
#
import os
os.chdir('\\Users\\allagonne\\PycharmProjects\\Euler')
f = open("euler22_names.txt", 'r')
names_list = [name[1: -1] for name in f.read().split(",")]
f.close()
names_list.sort()
print(names_list)

letters=dict()
for i in range(65,91):
    letters[chr(i)]=i-64
print(letters)

scores_list=[]
for i in range(len(names_list)):
    print(names_list[i],i+1)
    score_word=0
    name=names_list[i]
    for letter in name:
        score_word+=letters[letter]
    score=(i+1)*score_word
    scores_list.append(score)

scores_list_total=0
for i in scores_list:
    scores_list_total+=i

print(scores_list_total)
