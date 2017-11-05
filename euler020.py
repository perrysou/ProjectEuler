"""
"""


import math
def main():
    total = 0
    for i in map(int, str(math.factorial(100))):
        total += i
    print total
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
