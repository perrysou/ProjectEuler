"""
"""
import math


dsums = {}
abundant = {}


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
        if n < total + 1:
            abundant[n] = 1
    return dsums[n]


def main():
    total = 0
    for i in range(12, 28123):
        divisorSum(i)
    for j in range(24, 28124):
        for k in abundant:
            if (j - k) in abundant:
                # pass
                # print '%d is the sum of two abundants %d and %d' % (j, k, j - k)
                break
        else:
            total += j
    print total + sum(range(1, 24))
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
