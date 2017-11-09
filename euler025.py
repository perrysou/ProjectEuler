"""
The Fibonacci sequence is defined by the recurrence relation:
F(n) = F(n-1) + F(n-2), where F(1) = F(2) = 1
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain N digits?
"""

import random
fibos = {}
digits = [-1] * 5001
digits[1] = 1


def fibonacci(n):
    if n not in fibos:
        if n == 1 or n == 2:
            fibos[n] = 1
        else:
            fibos[n] = fibonacci(n - 1) + fibonacci(n - 2)
            num_of_digits = len(str(fibos[n]))
            if digits[num_of_digits] == -1:
                digits[num_of_digits] = n
            # else:
            #     digits[num_of_digits] = min(digits[num_of_digits], n)
    return fibos[n]


def main():
    i = 1
    dl = 1
    t = int(raw_input().strip())
    # t = random.randint(1, 1000)
    while t:
        n = int(raw_input().strip())
        # n = random.randint(2, 5000)
        if digits[n] == -1:
            while dl <= n:
                i += 1
                dl = len(str(fibonacci(i)))
        print digits[n]
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
