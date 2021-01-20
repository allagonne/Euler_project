#!/usr/bin/env python3
#
#euler102.py / triangle containment
import os
os.chdir("/home/arnaud/scripts/euler")
with open("files/euler102_triangles.txt", "r") as txt:
    contenu=txt.readlines()
triangles=[]
for i in contenu:
    triangles.append(i)
triangles2=[]
for i in triangles:
    triangles2.append(i.replace("\n",",0,0"))
print(triangles2)
trianglesint=[]
for i in triangles2:
    ts=eval(i)
    trianglesint.append(ts)

def whereispoint(xA,yA,xB,yB,xM,yM):
    diffx=xB-xA
    diffy=yB-yA
    if diffx!=0:
        a=diffy/diffx
        b=yA-a*xA
        if yM>=a*xM+b:
            return '+'
        elif yM==a*xM+b:
            return '='
        elif yM<=a*xM+b:
            return '-'
        else:
            return 'Problem'
    else:
        if xA>xM:
            return '-'
        elif xA==xM:
            return '='
        elif xA<xM:
            return '+'
        else:
            return 'Problem'

def isMinABC(xA,yA,xB,yB,xC,yC,xM,yM):
    if whereispoint(xA,yA,xB,yB,xM,yM)==whereispoint(xA,yA,xB,yB,xC,yC) and whereispoint(xA,yA,xC,yC,xM,yM)==whereispoint(xA,yA,xC,yC,xB,yB) and whereispoint(xB,yB,xC,yC,xM,yM)==whereispoint(xB,yB,xC,yC,xA,yA):
        return True
    else:
        return False
total=0
for i in range(len(trianglesint)):
    if isMinABC(trianglesint[i][0],trianglesint[i][1],trianglesint[i][2],trianglesint[i][3],trianglesint[i][4],trianglesint[i][5],trianglesint[i][6],trianglesint[i][7])==True:
        print(trianglesint[i])
        total+=1
print(total)
