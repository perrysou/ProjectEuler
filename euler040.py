"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""

def champernownes_constant(n, m):
    index = 0
    s = '.'
    for i in range(1, n + 1):
        number_of_digits, int_as_str = int2str(i)
        index_new = index + number_of_digits
        s = '.' + int_as_str
        if 0 < m - index <= number_of_digits:
            print(index, m, index_new, s[m - index], s)
            return s[m - index]
        index = index_new
        # print(index, s)

def int2str(n):
    res = ''
    i = 0
    while n // 10 != n:
        res += str(n % 10)
        n //= 10   
        i += 1
    return i, res[::-1]

if __name__ == '__main__':
    res = 1
    for i in range(7):
        res *= int(champernownes_constant(10 ** i, 10 ** i))
    print(res)
