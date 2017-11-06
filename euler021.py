"""
"""

import math

amicables = {}
dsums = {}


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
    sums = {}
    # t = int(raw_input().strip())
    t = 1
    while t:
        # n = int(raw_input().strip())
        n = 100000
        total = 0
        for i in range(2, n):
            if i in amicables:
                total += i
                sums[i + 1] = total
            else:
                j = divisorSum(i)
                if areAmicable(i, j):
                    amicables[i] = j
                    amicables[j] = i
                    total += i
                    sums[i + 1] = total
        sums[n] = total
        print total
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
