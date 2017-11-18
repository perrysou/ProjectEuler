"""
n! means n x (n - 1) x .... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number N!
"""


import math


def main():
    t = int(raw_input().strip())
    while t:
        n = int(raw_input().strip())
        print sum(map(int, str(math.factorial(n))))
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
