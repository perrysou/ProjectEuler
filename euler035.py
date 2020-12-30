"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math


def sieveofEratosthenes(n):
    nums = list(range(2, n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    return set(x for x in nums if x != 0)


def rotate(n):
    num_of_digits = 1
    n_new = n
    while n_new % 10 != n_new:
        num_of_digits += 1
        n_new /= 10
    i = 1
    rotates = {n}
    while i < num_of_digits:
        right = n % 10
        left = n // 10
        n_rotated = right * 10 ** (num_of_digits - 1) + left
        rotates.add(n_rotated)
        n = n_rotated
        i += 1
    return rotates


if __name__ == "__main__":
    # print "This program is being run by itself"
    n = int(input())
    primes = sieveofEratosthenes(n)
    count = 0
    res = 0
    for p in primes:
        if rotate(p) <= primes:
            print(rotate(p))
            count += 1
            res += p
    print(res)
else:
    print
    'I am being imported from another module'
