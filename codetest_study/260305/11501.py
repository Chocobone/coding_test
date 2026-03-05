import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    value = list(map(int, input().split()))

    day = len(value)
    max_v = value[-1]
    result = 0
    for i in range(day-1, -1, -1):
        if value[i] > max_v:
            max_v = value[i]
            continue
        result += max_v - value[i]
    print(result)

    