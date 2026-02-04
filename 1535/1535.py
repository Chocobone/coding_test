import sys

n = int(sys.stdin.readline())

weight = [0] + list(map(int, sys.stdin.readline().split()))
value = [0] + list(map(int, sys.stdin.readline().split()))
W = 101
dp = [[0]*W for _ in range(n+1)] # 100 = 초기 체력

for i in range(1, n+1):
    for j in range(1,W):
        if(weight[i] <= j):
            dp[i][j] = max(dp[i-1][j], value[i]+dp[i-1][j-weight[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])