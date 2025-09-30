# https://www.acmicpc.net/problem/7579

# dp[n][W] = max(dp[n-1][W], value + dp[n-1][W-K])
# prob : n * W 행렬의 크기가 최대 1Trillion -> 시간복잡도 신경써야 함
# dp[n] = max

import sys

n, m = map(int, sys.stdin.readline().split())

memory = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))

#dp = dict() # key = memory weight, value = cost

dp = [[sum(cost)]*(m+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, m+1):
