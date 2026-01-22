# https://www.acmicpc.net/problem/11909
# 문제 : 칸을 건너는 데의 비용을 최소화하는 문제
# dp[x][y] = (x,y)까지 가는데의 최소 비용
# (x,y)는 (x-1, y) 혹은 (x, y-1)에서밖에 오지 못한다.

# dp[x][y] = max(dp[x-1][y] + (arr[x][y] - arr[x-1][y]))

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def move2x(y, x):
    return max(0, arr[y][x] - arr[y][x-1] + 1)
def move2y(y, x):
    return max(0, arr[y][x] - arr[y-1][x] + 1)

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + move2x(0, i)
    dp[i][0] = dp[i-1][0] + move2y(i, 0)

for y in range(1, n):
    for x in range(1, n):
        dp[y][x] = min(dp[y-1][x] + move2y(y, x),
                       dp[y][x-1] + move2x(y, x))

print(dp[n-1][n-1])