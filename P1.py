"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# input number of test cases
t = int(raw_input().strip())
# for each case, compute the sum
for _ in range(t):
    # input of n as a long integer to deal with big numbers
    n = long(raw_input().strip())
    # find the number of multiples within [0, n)
    m3 = (n - 1) / 3
    m5 = (n - 1) / 5
    m15 = (n - 1) / 15
    # compute directly the sum of these multiples
    print (3 * m3 * (m3 + 1) + 5 * m5 * (m5 + 1) - 15 * m15 * (m15 + 1)) / 2
