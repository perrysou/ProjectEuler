"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


import random


def main():
    table = {}
    t = random.randint(1, 3000)
    # t = 1
    # t = int(raw_input().strip())
    for a0 in xrange(t):
        n = random.randint(1, 3000)
        # n = 3000
        # n = int(raw_input().strip())
        # if n in table and n <= max(table.keys()):
        #     print table[n]
        table[n] = -1
        if n % 2 == 0:
            for i in range(1, n / 3):
                j = (n ** 2 - 2 * i * n) / 2.0 / (n - i)
                if j.is_integer():
                    table[n] = max(i * j * (n - i - j), table[n])
                    # print i, j, k, i + j + k, i * j * k
            # else:
            #     print -1
        # if n not in table and n <= max(table.keys()):
        #     print -1
        print int(table[n])
    # print table.keys()
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
