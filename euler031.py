"""
In England the currency is made up of pound, pp, and pence, p,
and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, pp1 (100p) and pp2 (200p).
It is possible to make pp2 in the following way:
1*pp1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can N p be made using any number of coins?
As the result can be large print answer mod (10^9 + 7)
Note: N is given as p and not pp
"""

p = [1, 2, 5, 10, 20, 50, 100, 200]
combos = {(0, 0): 1, (1, 1): 1}


def getCombos(n, coins):
    coins_allowed = [_ for _ in coins if n >= _]
    if (n, len(coins)) not in combos:
        counts = 0
        while len(coins_allowed) >= 3:
            n_new = n
            n_new -= coins_allowed[-1]
            counts += getCombos(n_new, coins_allowed)
            coins_allowed.pop()
        combos[(n, len(coins))] = counts + n / 2 + 1
    return combos[(n, len(coins))]


def main():
    t = int(raw_input().strip())
    # t = 10**4
    # t = 1
    while t:
        n = long(raw_input().strip())
        # n = 10**5
        print getCombos(n, p) % (10**9 + 7)
        t -= 1


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
