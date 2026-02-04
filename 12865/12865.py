import sys

n, K = map(int, sys.stdin.readline().split())

weight = [0] * (n+1)
value = [0] * (n+1)
dp = [[0]*(K+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight[i], value[i] = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    for j in range(1, K+1):
        if(weight[i] <= j):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][K])