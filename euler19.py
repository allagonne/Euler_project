#!/usr/bin/env python3
#
#euler19 / counting sundays

#daysperyear starts at 1900 for daysperyear[0]
daysperyear=[]
for i in range(101):
    j=i+1900
    if j%4==0:
        if j%400==0:
            daysperyear.append(365)
        else:
            daysperyear.append(366)
    else:
        daysperyear.append(365)

dayspermonth_leapyear=[31,29,31,30,31,30,31,31,30,31,30,31]
dayspermonth_noleapyear=[31,28,31,30,31,30,31,31,30,31,30,31]
strday=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day=[j for j in range(1,32)]
month=[j for j in range(1,13)]
year=[j for j in range(1900,2001)]
currentday=[strday[0],day[0],month[0],year[0]]
while True:
    if currentday=[day[31],month[12],year[2000]]:
        break
    #new year
    if currentday[1]==day[31] and currentday[2]==month[12]:
        currentday[3]=year[+1]
        currentday[1]=day[1]
        currentday[2]=month[1]
        if currentday[0]==strday[6]:
            currentday[0]=strday[0]
        else:
            currentday[0]=strday[+1]
    #new month
    elif currentday[1]==day[31]:
        currentday[2]=month(+1)
    




