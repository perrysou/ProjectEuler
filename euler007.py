"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def main():
    primes = {}
    # t = 1
    count = 1
    i = 2
    t = int(raw_input().strip())
    for a0 in xrange(t):
        # n = 10001
        n = int(raw_input().strip())
        if n <= len(primes):
            print primes[n]
        else:
            while count <= n:
                for p in primes.itervalues():
                    if i % p == 0 and i != p:
                        break
                else:
                    primes[count] = i
                    count += 1
                if i == 2:
                    i += 1
                else:
                    i += 2
            print primes[n]
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
