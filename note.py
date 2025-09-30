import sys

t = int(input())

for _ in range(t):
    n = int(input())
    result, average = 0, 0
    for _ in range(n):
        c, g = map(float, sys.stdin.readline().split())
        result += c
        average += c * g
    print(int(result), end=' ')

    print(format(average / result, ".1f"))

