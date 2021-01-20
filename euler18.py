#!/usr/bin/env python3
#
# euler18.py/maximum path sum I
import os, time

# Debut du decompte du temps
start_time = time.time()

# traitement fichier => liste triangle_list
os.chdir('\\Users\\allagonne\\PycharmProjects\\Euler')
f = open("euler18_triangle.txt", 'r')
triangle_str_list = [ligne for ligne in f.read().split("\n")]
f.close()
triangle_list = []
for s in triangle_str_list:
    ma_ligne = [int(i) for i in s.split()]
    triangle_list.append(ma_ligne)
print(triangle_list)

#triangle_list = [[75], [95, 64], [17, 47, 82]]
nb_lines = 15
paths_to_take = nb_lines - 1

##fabrication du dictionnaire des chemins
dic = {}
for i in range(2 ** paths_to_take, 2 ** (paths_to_take + 1)):
    s = bin(i)[3:]
    dic[i - 2 ** paths_to_take] = s


##
max_count = 0
max_path = ''
count_zero = triangle_list[0][0]
for i in range(2 ** paths_to_take):
    count = count_zero
    path=dic[i]
    for j in range(1, nb_lines):
        count += triangle_list[j][path[:j].count('1')]
        if (count + 99 * (nb_lines-j)) < max_count:
            break
    #print(count,path)
    if count > max_count:
        max_count = count
        max_path = path
        print('new_maximum',max_count)

print('max', max_count, max_path)
# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
