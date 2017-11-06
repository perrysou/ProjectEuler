"""
4
1900 1 1
1910 1 1
2000 1 1
2020 1 1
"""

import datetime


def builtinway():
    date1 = datetime.date(1901, 1, 1)
    date2 = datetime.date(2000, 12, 31)
    count = 0
    while date1 <= date2:
        if date1.weekday() == 6 and date1.day == 1:
            count += 1
        date1 += datetime.timedelta(days=1)
    print count


def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True, 366
    return False, 365


def getDays(month, year):
    if month == 9 or month == 4 or month == 6 or month == 11:
        days = 30
    elif month == 2:
            if isLeap(year)[0]:
                days = 29
            else:
                days = 28
    else:
        days = 31
    return days


def md2d(y, m, d):
    return m * getDays(m, y) + d


def y2d(y1, y2):
    total = 0
    for y in range(y1, y2):
        total += isLeap(y)[1]
    return total


def main():
    yr, mr, dr = 1900, 1, 1
    # t = int(raw_input().strip())
    t = 1
    while t:
        y0, m0, d0 = 1901, 1, 1
        # y0, m0, d0 = map(int, raw_input().strip().split())
        yf, mf, df = 2000000, 12, 31
        # yf, mf, df = map(int, raw_input().strip().split())
        print y2d(yr, y0) - md2d(yr, mr, dr) + md2d(y0, m0, d0)
        print y2d(yr, yf) - md2d(yf, mf, df) + md2d(yf, mf, df)
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
