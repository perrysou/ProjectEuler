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
nMax = 5 * 10**6
chainDict = [-1] * (nMax + 1)
chainDict[1] = 1
chainMaxDict = [-1] * (nMax + 1)


def collatz(n):
    n_new = n / 2 if n % 2 == 0 else n * 3 + 1
    if n <= nMax:
        if chainDict[n] == -1:
            chainDict[n] = collatz(n_new) + 1
        return chainDict[n]
    else:
        return collatz(n_new) + 1


def main():
    n_old = 1
    k_old = 1
    chainMax = 0
    ii = 1
    t = int(raw_input().strip())
    # t = random.randint(1, 10 ** 4)

    for a in range(t):
        n = long(raw_input().strip())
        # n = random.randint(1, 5 * 10 ** 6)
        if chainMaxDict[n] == -1:
            while ii <= n:
                if collatz(ii) >= chainMax:
                    chainMax = chainDict[ii]
                    k_old = max(ii, k_old)
                chainMaxDict[ii] = k_old
                ii += 1
        print n, chainMaxDict[n]
        n_old = max(n, n_old)


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
