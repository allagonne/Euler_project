#!/usr/bin/env python3
#
#euler17.py / number letter counts
numbers=['','one','two','three','four','five','six','seven','eight','nine']
tens=['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
tentotwenty=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
total=0

#mille
total+=len('onethousand')

#1 à 9
total+=sum(len(numbers[i]) for i in range(10))

#10 à 19
total+=sum(len(tentotwenty[i]) for i in range(10))

#20 à 99
for i in range(20,100):
    k=int(str(i)[0])
    l=int(str(i)[1])
    total+=len(tens[k]+numbers[l])
#100 à 999
for i in range(100,1000):
    j=int(str(i)[0])
    if i%100==0:
        total+=len(numbers[j]+'hundred')
    elif int(str(i)[1])==1:
        l=int(str(i)[2])
        total+=len(numbers[j]+'hundred'+'and'+tentotwenty[l])
    else:
        k=int(str(i)[1])
        l=int(str(i)[2])
        total+=len(numbers[j]+'hundred'+'and'+tens[k]+numbers[l])
print(total)

