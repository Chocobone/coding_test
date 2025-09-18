# https://www.acmicpc.net/problem/1535

# knapsack prob
# dp[k][W] = max(dp[k-1][W], value[k] + dp[k-1][W-K])

import sys

n = int(sys.stdin.readline())

weight = list(map(int, sys.stdin.readline().split()))
value = list(map(int, sys.stdin.readline().split()))
W = 100
dp = [[0]*W for _ in range(n)] # 100 = 초기 체력

