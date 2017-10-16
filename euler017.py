"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

num2str = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion', 1000000000000: 'Trillion'}


def getstrlen(num):
    string = ''
    for power in [12, 9, 6, 3, 2]:
        if num % 10**power >= 0 and num >= 10**power:
            string += getstrlen(num / 10 ** power) + ' ' + num2str[10 ** power] + ' '
            num -= num / 10**power * 10**power
    if 20 < num < 100:
        string += num2str[num / 10 * 10] + ' '
        num -= num / 10 * 10
    if 0 <= num <= 20:
        string += num2str[num]
    return string.strip()


def main():
    t = int(raw_input().strip())
    while t:
        n = long(raw_input().strip())
        total = 0
        # for n in range(1, 1001):
        #     print n, '->', getstrlen(n)
        #     total += len(getstrlen(n))
        # print total
        print getstrlen(n)
        t -= 1


if __name__ == '__main__':
    main()