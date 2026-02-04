import sys

x, y = map(int, sys.stdin.readline().split()) 

dp = [[0]*(y+1) for _ in range(x+1)] # (0~x) * (0~y)

for i in range(1, x+1) : dp[i][1] = 1
for j in range(1, y+1) : dp[1][j] = 1

for i in range(2, x+1) :
    for j in range(2, y+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

print(dp[x][y] % 1000000007)