# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

N = int(input())
line = []
for _ in range(N):
    line.append(int(input()))

if N>1:
    line.sort()
    dp = [0] * (N)
    dp[0] = line[0]
    dp[1] = max(line[0] + line[1], line[0] * line[1])
    for i in range(2, N):
        dp[i] = max(dp[i-1] + line[i], dp[i-2] + line[i-1] * line[i])

print(dp[N-1] if N > 1 else line[0])