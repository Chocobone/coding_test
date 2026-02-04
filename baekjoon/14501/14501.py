# https://www.acmicpc.net/problem/14501
# dp[i] = i일에 얻을 수 있는 최대 수익
# dp[i+1] = max(dp[i], pay + dp[i + day])
# 점화식 ; n-1 -> 0으로 진행하며 최댓값 계산

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
task = []
for _ in range(n):
    task.append(tuple(map(int, input().split())))

for i in range(n - 1, -1, -1):
    day, pay = task[i]
    if i + day <= n:
        dp[i] = max(dp[i + 1], pay + dp[i + day])
    else:
        dp[i] = dp[i + 1]
print(dp[0])


