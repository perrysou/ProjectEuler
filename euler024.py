"""
"""

from itertools import permutations
def main():
    l = list(permutations(range(0, 10)))
    print l[10**6 - 1]
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
