#https://www.acmicpc.net/problem/15989

import sys
input = sys.stdin.readline

dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, 10001):
    for j in range(i//3 + 1):
        if i - 3*j >= 0:
            dp[i] += 1

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])