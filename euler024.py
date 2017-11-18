"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
For example, dabc is one possible permutation of the word abcd.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

The lexicographic permutations of abc are:
abc acb bac bca cab cba

What is the nth lexicographic permutation of the word abcdefghijklm?
"""

import math
import random


def getPerm(n, s):
    length = math.factorial(len(s) - 1)
    if len(s) == 1:
        return s
    else:
        this = n / length
        n_new = n % length
        s_new = s[0:this] + s[this + 1:len(s)]
        return s[this] + getPerm(n_new, s_new)


def main():
    target = 'abcdefghijklm'
    t = int(raw_input().strip())
    # t = random.randint(1, 1000)
    while t:
        n = long(raw_input().strip())
        # n = random.randint(1, math.factorial(len(target)))
        t -= 1
        print getPerm(n - 1, target)
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
