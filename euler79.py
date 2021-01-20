#!/usr/bin/env python3
#
# euler79.py/passcode derivation
import os, time

# Debut du decompte du temps
start_time = time.time()

#combien d'occurences
def occurrences(x,liste):
    count_zero, count_one, count_two = 0, 0, 0
    for i in range(len(liste)-1):
        count_zero+=liste[i][0].count(x)
        count_one+=liste[i][1].count(x)
        count_two+=liste[i][2].count(x)
    return count_zero, count_one, count_two

# traitement fichier => liste triangle_list
os.chdir('\\Users\\allagonne\\PycharmProjects\\Euler')
f = open("euler79_keylog.txt", 'r')
keys_str_list = [ligne for ligne in f.read().split("\n")]
f.close()

reponse_desordre=''
for i in keys_str_list:
    for char in i:
        if char not in reponse_desordre:
            reponse_desordre+=char
print(reponse_desordre)

reponse_ordre=''
while reponse_desordre!='':
    for number in reponse_desordre:
        count_zero, count_one, count_two = occurrences(number,keys_str_list)[0], occurrences(number,keys_str_list)[1], occurrences(number,keys_str_list)[2]
        print(count_zero, count_one, count_two)
        if count_one==0 and count_two==0:
            reponse_ordre+=number
            reponse_desordre=reponse_desordre.replace(number,'')
            for i in range(len(keys_str_list)-1):
                if keys_str_list[i][0]==number:
                    keys_str_list[i]=keys_str_list[i].replace(number,'')
                    keys_str_list[i]+='x'
            print(keys_str_list)
            print(reponse_desordre)
print(reponse_ordre)
