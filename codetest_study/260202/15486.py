# https://www.acmicpc.net/problem/15486
# 무조건 DP -> n일차의 상담을 받았을 때와 받지 않았을 때의 최댓값 비교
# dp[i] = max(dp[i-1], dp[] + work[n])

import sys
input = sys.stdin.readline

N = int(input())
time = []
work = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append(a)
    work.append(b)

dp= [0] * (N+1)
dp[1] = work[1] if time[1] == 1 else 0

for i in range(2, N+1):
    if i + time[i] <= N+1: #당일의 일을 할 수 있으면
        dp[i+time[i]] = max(dp[i-1]+work[i],)