"""
The nth term of the sequence of triangle numbers is given by, t_n = 1 / 2 * n * ( n + 1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import math
def letter2number(letter):
    return ord(letter) - ord('A') + 1

with open("p042_words.txt") as f:
    words = f.read().strip('"').split('","')
    numbers = [sum(letter2number(l) for l in w) for w in words]
    print(numbers)

    count = 0
    for n in numbers:
        if math.sqrt(1 + 8 * n) % 2 == 1:
            count += 1
    print(count)
    
