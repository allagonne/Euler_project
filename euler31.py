#!/usr/bin/env python3
#
list=[1,2,5,10,20,50,100,200]
total=200
ways=0

for a in range(200):
    for b in range(100):
        for c in range(40):
            for d in range(20):
                for e in range(10):
                    for f in range(4):
                        for g in range(2):
                            h=0
                            if a*list[0]+b*list[1]+c*list[2]+d*list[3]+e*list[4]+f*list[5]+g*list[6] == total:
                                ways=ways+1
                                print(a,b,c,d,e,f,g,h)
ways=ways+len(list)
print('manieres', ways)
