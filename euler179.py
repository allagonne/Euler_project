#!/usr/bin/env python3
#
# euler179 / Consecutive positive divisors

import time

# Debut du decompte du temps
start_time = time.time()

def divisors(n):
    divisors_list = [1, n]

    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisors_list.extend([d, int(n / d)])

    return list(sorted(set(divisors_list)))

def consecutive_positive_divisors(num):
    nums = [n for n in range(1, num)]
    count = 0

    for i in range(0, len(nums) - 1):
        if len(divisors(nums[i])) == len(divisors(nums[i + 1])):
            count += 1
            #print(count, nums[i], nums[i + 1])

    return count

print(consecutive_positive_divisors(10000000))


# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))