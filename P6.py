"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = long(raw_input().strip())
        sqrsum = n * (n + 1) / 2 * n * (n + 1) / 2
        sumsqr = n * (n + 1) * (2 * n + 1) / 6
        print abs(sqrsum - sumsqr)
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
