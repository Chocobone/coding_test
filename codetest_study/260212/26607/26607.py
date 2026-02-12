# https://www.acmicpc.net/problem/26607

import sys
from collections import deque
input = sys.stdin.readline

N, K, X = map(int, input().split())

A = [0]
for _ in range(N):
    a, _ = map(int, input().split())
    A.append(a)

dp = [[0] * (X+1) for _ in range(N+1)]

# dp[i+1][w] = max(dp[i][w], dp[i][w+a[i]] + a[i])
for i in range(1, N+1):
    for w in range(1, X+1):
    # knapsack에 넣는다.
        if w + A[i] <= X:
            dp[i][w+A[i]] = max(dp[i-1][w+A[i]], dp[i-1][w]+A[i])
        else:
            dp[i][w] = dp[i][w-1]

print(dp)
