#https://www.acmicpc.net/problem/13305

# 그리디로 순간순간 비교하면서 최종값에 더하면 될듯?
import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

min_city = city[0]
result = min_city * road[0]
if n > 2:
    for i in range(1, n-1):
        if min_city > city[i]:
            min_city = city[i]
        result += min_city * road[i]

print(result)