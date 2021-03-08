"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""

import math
import itertools
import bisect

max_pandigital_prime = [-1]
for d in range(1, 7 + 1):
    for num_tuple in itertools.permutations(range(1, d + 1)):
        if num_tuple[-1] % 2 == 0 or sum(num_tuple) % 3 == 0:
            continue
        num = int("".join(map(str, num_tuple)))
        if num == 1:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(float(num)))):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            max_pandigital_prime.append(num)

print(max_pandigital_prime)
t = int(input())
while t:
    n = int(input())
    t -= 1
    print(max_pandigital_prime[bisect.bisect_right(max_pandigital_prime, n) - 1])
    # print(max_pandigital_prime[bisect.bisect_left(max_pandigital_prime, n)])
