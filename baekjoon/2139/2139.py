import sys

day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day, month, year = map(int, sys.stdin.readline().split())

while day != 0 and month !=0 and year != 0:
    result = day + sum(day_of_month[:month])

    if(month > 2):
        if year%400 == 0:
            result+=1
        elif year%100 == 0:
            pass
        elif year%4 == 0:
            result+=1

    print(result)
    day, month, year = map(int, sys.stdin.readline().split())
