"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

1
4
3
7 4
2 4 6
8 5 9 3

1
15
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""


def main():
    action = [[1, 0], [1, 1]]
    t = int(raw_input().strip())
    for _ in range(t):
        n = int(raw_input().strip())
        values = []
        for i in range(n):
            lineNext = map(int, raw_input().strip().split())
            if len(lineNext) == 1:
                values.append(lineNext)
            else:
                values.append([0] * len(lineNext))
                for j, last in enumerate(lineLast):
                    for a in action:
                        nodeNext = (i - 1 + a[0], j + a[1])
                        if 0 <= nodeNext[0] <= i and 0 <= nodeNext[1] <= nodeNext[0]:
                            next = lineNext[nodeNext[1]] + last
                            values[nodeNext[0]][nodeNext[1]] = max(values[nodeNext[0]][nodeNext[1]], next)
            lineLast = values[i]
            # if len(maxList) == 2**(len(valueList) - 1):
            #     print 'getting out early!'
            #     break
        # print valueList
        # print maxList
        print max(values[-1])
    return


if __name__ == '__main__':
    main()
