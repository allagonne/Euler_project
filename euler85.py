#!/usr/bin/env python3
#
# euler85 / counting rectangles

def somme(x):
    s=0
    for i in range(x+1):
        s+=i
    return s


def rectangles(x,y):
    if x==1 and y==1:
        return 1
    elif y==1 and x>1:
        return somme(x)
    elif y>1 and x==1:
        return somme(y)
    else:
        reponse=rectangles(x,y-1)+rectangles(x,1)+(y-1)*somme(x)
        return reponse

answer=0
maxi = 2000000
for i in range(1,200):
    for j in range(i,200):
        rect=rectangles(i,j)
        if abs(maxi-rect)<abs(maxi-answer):
            print(rect,i,j)
            answer=rect
            aire=i*j

print("answer=",aire)