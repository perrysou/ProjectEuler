"""
"""
import math


def sieveofEratosthenes(n):
    nums = range(2, n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    while nums.count(0):
        nums.remove(0)
    return nums


def getPrimeFactors(n, primeSet):
    # a dictionary {prime#1 : count1, prime#2: count2, ...}, 2 <= prime#i <= n
    primeCount = {}
    total = 1

    for x in primeSet:
        temp = 0
        while n % x == 0:
            temp += 1
            n /= x
        # keep increasing the counter for i until x is not divisible by i
        if temp != 0:
            total *= (temp + 1)
            primeCount[x] = temp  # update the counter in the dictionary
        if n == 1:
            break
    if n != 1:
        total *= 2
        primeCount[n] = 1
        primeSet.append(n)
    # return primeCount, total, set(primeCount.keys())
    return total, primeSet


def genTriangleNumber(n):
    return n * (n + 1) / 2


def main():
    divisorDict = {}
    primeSet = sieveofEratosthenes(1000)
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = 500
        n = int(raw_input().strip())
        diff = n
        tri = genTriangleNumber(n)
        while True:
            nd, primeSet = getPrimeFactors(tri, primeSet)
            # print primeSet[-1]
            if nd not in divisorDict:
                divisorDict[nd] = tri
            else:
                divisorDict[nd] = min(tri, divisorDict[nd])
                # print nd, tri
            if nd > n:
                print tri
                break
            diff += 1
            tri += diff
    # print divisorDict
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
