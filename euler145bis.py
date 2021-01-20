#!/usr/bin/env python3
#
#euler145 / how many reversible numbers are there below one-billion? 
def isnotreversible(n):
    s=str(n)
    r=s[::-1]
    q=int(s)+int(r)
    for j in str(q):
        if j not in ('1','3','5','7','9'):
            return True
    if s[0]!='0'and r[0]!='0':
        return False
    else:
        return True

seuil=10**9
rev=0
for i in range(1,seuil):
    if isnotreversible(i)==False:
        rev+=1

print(rev, i)
    

