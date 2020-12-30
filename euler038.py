"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def get_limit(k):
    set_limit = set()
    for i in range(1, k + 1):
        set_limit.add(str(i))
    limit = 0
    for i in range(1, k + 1):
        limit += i * 10 ** (i - 1)
    return limit, set_limit


def pandigital(n, k):
    limit, set_limit = get_limit(k)
    print(limit, set_limit)
    multipliers = []
    for multiplier in range(2, n):
        res = ""
        i = 0
        while len(res) < k or int(res) <= limit:
            i += 1
            res += str(multiplier * i)
            if len(res) == k and set(res) == set_limit:
                print(res, multiplier, i)
                multipliers.append(multiplier)
    return multipliers


if __name__ == "__main__":
    n, k = map(int, input().split(" "))
    print(pandigital(n, k))
