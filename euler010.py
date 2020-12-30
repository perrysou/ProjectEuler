"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def sieveofSundaram(n):
    nums = list(range(2, n + 1))
    for i in range(2, n - 1, 2):
        nums[i] = 0
    for i in range(1, int((-1 + math.sqrt(n)) / 2) + 1):
        j = i
        while 2 * (i + j + 2 * i * j) + 1 <= n:
            nums[2 * (i + j + 2 * i * j) - 1] = 0
            j += 1
    return [x for x in nums if x != 0]


def sieveofEratosthenes(n):
    nums = list(range(2, n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    return [x for x in nums if x != 0]

def sumOfPrimes(n):
    total = 0
    totals = {}
    nums = sieveofEratosthenes(n)
    for i, num in enumerate(nums):
        total += num
        totals[i + 2] = total
    return total, totals

def main():
    sumList = {}
    t = 1
    # t = int(raw_input().strip())
    for a0 in xrange(t):
        n = 10 ** 6
        # n = int(raw_input().strip())
        # print sieveofSundaram(n) == sieveofEratosthenes(n)
        # return
        if n not in sumList:
            sumFinal, sumList = sumOfPrimes(n)
        print sumFinal, sumList[10]
    # print sumList
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
