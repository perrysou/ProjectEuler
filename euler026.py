"""
"""

import math
import random


def getPattern(s):
    d = str('')
    for letter in s:
        if letter not in d:
            d += letter
    return d


def main():
    # t = int(raw_input().strip())
    # t = random.randint(1, 1000)
    t = 1
    while t:
        # n = long(raw_input().strip())
        n = long(random.randint(4, 10000))
        for i in range(4, n):
            f = '%.16f' % (1. / i)
            s = str(f).lstrip('0.')
            print s
            print getPattern(s)
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
