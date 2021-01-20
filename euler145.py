#!/usr/bin/env python3
#
#euler145 / how many reversible numbers are there below one-billion? 
seuil=10**9
rev=0
for i in range(1,seuil):
    notreversible=False
    s=str(i)
    r=s[::-1]
    q=int(s)+int(r)
    for j in str(q):
        if j not in ('1','3','5','7','9'):
            notreversible=True    

    if s[0]!=0 and r[0]!='0':
        if notreversible==False:
            rev+=1

print(rev, i)
    

