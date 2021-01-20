#!/usr/bin/env python3
#
coins=[1,2,5,10,20,50,100,200]
amount=200

def ways(target,avail_coins):
    if avail_coins <=1:
        return 1
    result=0
    while target >= 0:
        result+=ways(target,avail_coins-1)
        target=target-coins[avail_coins-1]
    return result



print('manieres', ways(amount,8))
