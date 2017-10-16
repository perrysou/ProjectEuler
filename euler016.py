def integerdigits(integer):
    total = 0
    while integer:
        total += (integer % 10)
        integer /= 10
    return total


def powerdigit(power, powertodigits):
    if power not in powertodigits:
        powertodigits[power] = integerdigits(2**power)
    return powertodigits[power]


def main():
    powerdigits = {}
    # t = int(raw_input().strip())
    t = 1
    while t:
        # n = long(raw_input().strip())
        n = 1000
        print powerdigit(n, powerdigits)
        t -= 1


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
