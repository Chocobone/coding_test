# https://www.acmicpc.net/problem/15486
# 무조건 DP -> n일차의 상담을 받았을 때와 받지 않았을 때의 최댓값 비교
# dp[i] = max(dp[i-1], dp[] + work[n])

import sys
input = sys.stdin.readline

N = int(input())
time = [0] * (N+1)
work = [0] * (N+1)
for i in range(1, N+1):
    time[i], work[i] = map(int, input().split())

dp= [0] * (N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    if i + time[i] - 1 <= N: #당일의 일을 할 수 있으면
        dp[i+time[i]-1] = max(dp[i-1]+work[i], dp[i+time[i]-1])

print(dp[N])