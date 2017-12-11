"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of Nth powers of their digits.
"""

import math
import random


def main():
    # t = int(raw_input().strip())
    # t = random.randint()
    t = 1
    while t:
        # n = long(raw_input().strip())
        n = random.randint(3, 6)
        grandtotal = 0
        for k in range(2, 10**6):
            darr = map(int, str(k))
            total = 0
            for d in darr:
                total += d**n
                if total > k:
                    break
            if total == k:
                # print k
                grandtotal += k
        print grandtotal
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
