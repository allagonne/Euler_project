#!/usr/bin/env python3
#
#euler89 / Roman numerals

import time

# Debut du decompte du temps
start_time = time.time()

def convert_roman_to_minimal(s):
    s = s.replace('IIIII', 'V')
    s = s.replace('IIII', 'IV')
    s = s.replace('VIV', 'IX')
    s = s.replace('VV', 'X')
    s = s.replace('LXXXXX', 'C')
    s = s.replace('LXXXX', 'XC')
    s = s.replace('XXXXX', 'L')
    s = s.replace('XXXX', 'XL')
    s = s.replace('LL', 'C')
    s = s.replace('DCCCCC', 'M')
    s = s.replace('DCCCC', 'CM')
    s = s.replace('CCCCC', 'D')
    s = s.replace('CCCC', 'CD')
    s = s.replace('DD', 'M')
    return s

def count_char(s):
    return sum(map(s.count, ['M','D', 'C', 'L', 'X', 'V', 'I']))

file = open("p089_roman.txt",'r')
count = 0
wrong_list = []
while True:
    next_line = file.readline()

    if not next_line:
        break;
    #print(next_line, convert_roman_to_minimal(next_line), count_char(convert_roman_to_minimal(next_line)))
    count+= count_char(next_line) - count_char(convert_roman_to_minimal(next_line))

file.close()
print(count)