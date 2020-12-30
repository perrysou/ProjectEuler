"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import math


def sieveofEratosthenes(n):
    nums = list(range(2, n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    return [x for x in nums if x != 0]


def get_left_and_right(n, primes):
    n_left = n
    n_right = 0
    # left_and_rights = [n]
    i = 0
    while n_left % 10 != n_left:
        n_right += (n_left % 10) * (10 ** i)
        n_left //= 10
        i += 1
        # left_and_rights.append(n_right)
        # left_and_rights.append(n_left)
        if not n_right in primes or not n_left in primes:
            return False
    # print(left_and_rights)
    return True


if __name__ == "__main__":
    n = int(input())
    # n = 10**6
    primes = set(sieveofEratosthenes(n))
    # print(max(primes))
    res = 0
    for i in primes:
        if i > 7 and get_left_and_right(i, primes):
            print(i)
            res += i
    print(res)
