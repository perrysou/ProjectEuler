"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n.
If d(a) = b and d(b) = a, where a != b,
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under N.
"""

import random
import math

amicables = {}
dsums = {}
sums = [-1] * (100000 + 1)


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
    return dsums[n]


def areAmicable(n1, n2):
    return divisorSum(n2) == n1 and n1 != n2


def main():
    i = 1
    n_old = 0
    total = 0
    # t = int(raw_input().strip())
    t = random.randint(1, 1000)
    while t:
        # n = int(raw_input().strip())
        n = random.randint(1, 100000)
        if sums[n] == -1:
            while i <= n:
                if i in amicables:
                    total += i
                else:
                    j = divisorSum(i)
                    if areAmicable(i, j):
                        amicables[i] = j
                        amicables[j] = i
                        total += i
                sums[i] = total
                i += 1
        print sums[n]
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
