"""
You are given around five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list in sample is sorted into alphabetical order,
PAMELA, which is worth 16 + 1 + 13 + 5 + 12 + 1 = 48, is the 5th name in the list.
So, PAMELA would obtain a score of 5 * 48 = 240.

You are given Q queries, each query is a name, you have to print the score.
"""
import csv
alphabet = {'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26}


def main():
    names = []
    n = int(raw_input().strip())
    while n:
        names.append(raw_input().strip())
        n -= 1
    names.sort()

    q = int(raw_input().strip())
    while q:
        nameQ = raw_input().strip()
        total = 0
        i = names.index(nameQ)
        for letter in nameQ:
            total += alphabet[letter]
        total *= (i + 1)
        print total
        q -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
