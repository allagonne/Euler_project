#!/usr/bin/env python3
#
#euler112 / bouncy numbers 

bouncy,propbouncy,i=0,0,0,0,100
while propbouncy < 0.99:
    s=str(i)
    if sorted(s)!=list(s) and sorted(s,reverse=True)!=list(s):
        bouncy+=1    
    propbouncy=bouncy/i
    i+=1
print(bouncy,i-1,propbouncy)

    

