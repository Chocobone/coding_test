# 점화식 dp[n] = min(dp[n-3] + 1, dp[n-5] + 1)
# dp[3] == dp[5] == 1
# prob : -1값 분류시 

import sys

n = int(sys.stdin.readline())

if(n>=6):
    dp = [0] * (n+1)
    dp[1] = dp[2] = dp[4] = -1
    dp[3] = dp[5] = 1
    for i in range(6, n+1):
        if (dp[i-3]==-1 and dp[i-5]==-1):
            dp[i] = -1
        elif(dp[i-3]!=-1 and dp[i-5]==-1):
            dp[i] = dp[i-3] + 1
        else:
            dp[i] = dp[i-5] + 1
else:
    dp = [0,-1,-1,1,-1,1]
print(dp[n])

