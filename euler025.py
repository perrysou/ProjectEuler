"""
"""
fibos = {}


def fibonacci(n):
    if n not in fibos:
        if n == 1 or n == 2:
            fibos[n] = 1
        else:
            fibos[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibos[n]


def main():
    n = 1
    while len(str(fibonacci(n))) != 1000:
        n += 1
    print n
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
