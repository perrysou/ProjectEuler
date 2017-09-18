"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import random


def collatz(n, chainDict):
    if n not in chainDict:
        chainDict[n] = 1
        if n != 1:
            if n % 2 == 0:
                n_new = n / 2
            else:
                n_new = n * 3 + 1
            chainDict[n] = collatz(n_new, chainDict) + 1
    return chainDict[n]


def main():
    # t = int(raw_input().strip())
    t = random.randint(1, 10 ** 4)
    chainDict = {}
    chainMaxDict = {}
    n_old = 0
    chainMax = 0
    k_old = 1
    for a in range(t):
        # n = long(raw_input().strip())
        n = random.randint(1, 5 * 10 ** 5)
        if n > n_old:
            step = -1
        elif n < n_old:
            step = 1
            chainMax = 0
            k_old = 1
        else:
            print chainMaxDict[n]
            break

        for nn in range(n, max(n_old, n / 2), step):
            collatz(nn, chainDict)
        for k in chainDict:
            if k <= n:
                if chainDict[k] >= chainMax:
                    chainMax = chainDict[k]
                    k_old = max(k, k_old)
        chainMaxDict[n] = k_old
        print n, k_old
        n_old = n


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
