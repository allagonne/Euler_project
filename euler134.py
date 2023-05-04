# -*- coding: utf-8 -*-
"""euler134.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QuC5zRrSV0g2HTT76nfzX427GeyQ-9NA
"""

from math import sqrt
import time
start_time = time.time()
def isprime(x):
    squareroot=int(sqrt(x))+1
    for i in range(2,squareroot):
        if x%i==0:
            return False
    return True
def getsum(p1,p2):
  k, test = 1, False
  while test != True:
    # p2k = str(p2*k)
    # if len(p2k) == 1:
    #   p2k = '0' + p2k
    if str(p2*k)[-len(str(p1)):] == str(p1):
      test = True
    else: k+=2
  return p2*k
def getallsums(maxi = 1000000):
  s, p1, p2 = 0, 5, 7
  while p1 < maxi:
    s+=getsum(p1, p2)
    p1, p2 = p2, p2+2
    while isprime(p2) == False:
      p2+=2
  return s
#testing
display(getallsums(1000000))
display("Temps d execution : %s secondes ---" % (time.time() - start_time))
