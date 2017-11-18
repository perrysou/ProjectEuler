"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Given N, print YES if it can be expressed as sum of two abundant numbers, else print NO.
"""

import random
import math

dsums = {}
abundant = [False] * (10**5 + 1)
abundantSumQ = ['NO'] * (10**5 + 1)


def divisorSum(n):
    if n not in dsums:
        total = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n / i == i:
                    total += i
                else:
                    total += (i + n / i)
        dsums[n] = total + 1
    if n < dsums[n]:
        abundant[n] = True
    return dsums[n]


def main():
    i = 12
    t = int(raw_input().strip())
    # t = random.randint(1, 100)
    while t:
        n = int(raw_input().strip())
        # n = random.randint(1, 10**5)
        if n <= 28123:
            while i <= n:
                divisorSum(i)
                i += 1
            for k in range(12, min(n / 2 + 1, 28123 / 2 + 1)):
                if abundant[k] and abundant[n - k]:
                    abundantSumQ[n] = 'YES'
                    break
        else:
            abundantSumQ[n] = 'YES'
        print abundantSumQ[n]
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
