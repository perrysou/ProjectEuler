"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def isDoublePalindrome(n, k):
    bits = []
    n_new = n
    while n_new >= 1:
        bit = n_new % k
        n_new //= k
        bits.append(bit)
    for i in range(len(bits) // 2):
        if bits[i] != bits[-i - 1]:
            return False
    # print(bits)
    return True



if __name__ == "__main__":
    n, k = map(int, input().split(" "))
    res = 0
    for i in range(int(n)):
        if isDoublePalindrome(i, 10) and isDoublePalindrome(i, int(k)):
            # print(i)
            res += i
    print(res)