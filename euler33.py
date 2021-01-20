#!/usr/bin/env python3
#
# euler33 / digit cancelling fractions


##main loop
totalnum,totaldenom=1,1
A=[str(j) for j in range(1,10)]
for i in range(11,100):
    s=str(i)
    for j in range(i+1,100):
        f=i/j
        t=str(j)
        for k in A:
            y=s.replace(k,'')
            z=t.replace(k,'')
            if y!='' and z!='' and int(y)!=0 and int(z)!=0 and int(y)!=int(s) and int(z)!=int(t):
                if f==(int(y)/int(z)):
                    totalnum*=i
                    totaldenom*=j

print(totalnum)
print(totaldenom)




