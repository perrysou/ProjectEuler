"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def maxPrimeFactor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            n /= i
            # print '{} is a prime factor of {}'.format(i, n)
            return maxPrimeFactor(n)
        i += 1
    else:
        # print '{} is the largest prime factor'.format(n)
        return n


def main():
    t = int(raw_input().strip())
    for _ in xrange(t):
        n = long(raw_input().strip())
        print maxPrimeFactor(n)

if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
