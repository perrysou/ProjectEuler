"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def sieveofSundaram(n):
    nums = range(2, n + 1)
    for i in range(2, n - 1, 2):
        nums[i] = 0
    for i in range(1, int((-1 + math.sqrt(n)) / 2) + 1):
        j = i
        while 2 * (i + j + 2 * i * j) + 1 <= n:
            nums[2 * (i + j + 2 * i * j) - 1] = 0
            j += 1
    total = 0
    totals = {}
    for i, num in enumerate(nums):
        total += num
        totals[i + 2] = total
    return totals


def sieveofEratosthenes(n):
    nums = range(2, n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    total = 0
    totals = {}
    for i, num in enumerate(nums):
        total += num
        totals[i + 2] = total
    return totals


def main():
    sumList = {}
    t = 1
    # t = int(raw_input().strip())
    for a0 in xrange(t):
        n = 10
        # n = int(raw_input().strip())
        # print sieveofSundaram(n) == sieveofEratosthenes(n)
        # return
        if n not in sumList:
            sumList = sieveofSundaram(n)
        print sumList[n]
    # print sumList
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
