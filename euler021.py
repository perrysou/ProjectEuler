"""
"""

import math


def divisorSum(n):
    total = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                total += i
            else:
                total += (i + n / i)
    return total + 1


def areAmicable(n1, n2):
    return divisorSum(n1) == n2 and divisorSum(n2) == n1 and n1 != n2


def main():
    amicables = {}
    total = 0
    for i in range(2, 10000):
        j = divisorSum(i)
        if i not in amicables and j not in amicables and areAmicable(i, j):
            amicables[i] = j
            amicables[j] = i
            total += (i + j)
    print total
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
