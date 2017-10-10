"""
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
"""
action = [[1, 0], [0, 1]]
numRoutes = {}


def getRoutes(n, m, init, goal, routes):
    x = goal[0]
    y = goal[1]
    if x == init[0] and y == init[1]:
        routes[(x, y)] = 1
    else:
        routes[(x, y)] = 0
        for a in action:
            xNew = x - a[0]
            yNew = y - a[1]
            if 0 <= xNew < n and 0 <= yNew < m:
                if (xNew, yNew) in routes:
                    c = routes[(xNew, yNew)]
                else:
                    c = getRoutes(n, m, init, [xNew, yNew], routes)
                routes[(x, y)] += c
    return routes[(x, y)]


def main():
    t = int(raw_input().strip())
    # t = 2
    while t:
        n, m = map(int, raw_input().strip().split())
        # n = 20
        # m = 20

        init = [0, 0]
        goal = [n, m]
        print getRoutes(n + 1, m + 1, init, goal, numRoutes) % (10 ** 9 + 7)
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
