"""
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

    with open('p022_names.txt', mode='r') as f:
        it = csv.reader(f, delimiter=',', quotechar='"')
        names = it.next()
        names.sort()
        grandtotal = 0
        for i, name in enumerate(names):
            total = 0
            for letter in name:
                total += alphabet[letter]
            grandtotal += total * (i + 1)
        print grandtotal
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
