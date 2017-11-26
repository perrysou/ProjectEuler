"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:


It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a NxN, (N is odd) spiral formed in the same way?
As the sum will be huge you have to print the result mod (10^9 + 7)
"""

import math
import random


def spiralDiagonals(n):
    return (-9 + n * (8 + n * (3 + 4 * n))) / 6 % (10**9 + 7)


def main():
    # t = int(raw_input().strip())
    t = 1
    while t:
        # n = long(raw_input().strip())
        n = 1
        print spiralDiagonals(n)
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
