"""
19 is a curious number, as 1! + 9! = 1 + 362880 = 362881 which is divisible by 19.

Find the sum of all numbers below N which divide the sum of the factorial of their digits.

Note: as 1!, 2!, ..., 9! are not sums they are not included.
"""

import math
import random

fdict = {}


def factorial(n):
    if n not in fdict:
        if n <= 1:
            fdict[n] = 1
        else:
            fdict[n] = n * factorial(n - 1)
    return fdict[n]


def curiousQ(n):
    cumsum = 0
    n_old = n
    while n / 10 > 0:
        cumsum += factorial(n % 10)
        n /= 10
    cumsum += factorial(n % 10)
    return cumsum % n_old == 0


def main():
    n = long(input().strip())
    # n = random.randint()
    l = []
    # n = 10**5
    cumsum = 0
    for x in range(10, n):
        if curiousQ(x):
            cumsum += x
        l.append(cumsum)
    print
    cumsum
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print
    'I am being imported from another module'
