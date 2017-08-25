"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            n /= i
            return isPrime(n)
        i += 1
    else:
        return n


def main():
    t = int(raw_input().strip())
    for _ in xrange(t):
        n = long(raw_input().strip())
        print isPrime(n)

if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
