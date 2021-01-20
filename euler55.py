#!/usr/bin/env python3
#
list=[]
for i in range(10001):
    list.append(i)

def ispalindrome(x):
    y = ''
    for i in str(x):
        y=i+y
    if str(x) == y:
        return True
    else:
        return False

def inverse(x):
    y=''
    for i in str(x):
        y=i+y
    return int(y)


for i in range(10001):
    list_iterations=[i]
    nb_apres_iteration=i
    for j in range(51):
        nb_apres_iteration+=inverse(nb_apres_iteration)
        list_iterations.append(nb_apres_iteration)
    for k in range(1,51):
        if ispalindrome(list_iterations[k])==True:
            list.remove(i)
            break

print(list)        
print(len(list))
