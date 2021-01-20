#!/usr/bin/env python3
#
# euler38 / pandigital multiples 

def ispandigital(n):
    if n>=10**9 or n<10**8:
        return False
    else:
        s=str(n)
        if '0' in s:
            return False
        for i in range(1,10):
            if str(i) in s:
                continue
            else:
                return False
        return True

##main loop
#n>1 donc i maximum a verifier:9876 et j maximum à vérifier=9
panmax=123456788

for a in range(9877):
    c=[]
    s=[]
    for b in range(1,10):
        c.append(a*b)
        s.append(str(a*b))
        strsomme=''.join(s)
        intsomme=int(strsomme)
        if ispandigital(intsomme)==True and intsomme>panmax:
            print(a,intsomme)
            panmax=intsomme
