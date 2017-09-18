"""
A palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math


def isPalindrome(number):
    numString = str(number)
    for i in range(len(numString) / 2):
        if numString[i] == numString[len(numString) - 1 - i]:
            continue
        else:
            return False
    return True


def getPalindromes():
    palindromes = set()
    for i in range(100, 1000, 1):
        for j in range(100, 1000, 1):
            if isPalindrome(i * j):
                palindromes.add(i * j)
    return sorted(palindromes)


def main():
    t = int(raw_input().strip())
    sortedPalindromes = getPalindromes()
    for _ in xrange(t):
        n = int(raw_input().strip())
        for p in sortedPalindromes:
            if p < n and p != sortedPalindromes[-1]:
                continue
            elif p == sortedPalindromes[-1] and p != n:
                print p
            else:
                print sortedPalindromes[sortedPalindromes.index(p) - 1]
                break


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
