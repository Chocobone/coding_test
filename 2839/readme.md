# dp 풀이
- 5kg 설탕과 3kg 설탕으로 무게를 맞출 수 있는지와 봉지 몇개가 최소로 필요한지 여부를 dp로 측정

- 점화식: dp[n] = min(dp[n-3] + 1, dp[n-5] + 1)
```        
if (dp[i-3]==-1 and dp[i-5]==-1):
    dp[i] = -1
elif(dp[i-3]!=-1 and dp[i-5]==-1):
    dp[i] = dp[i-3] + 1
else:
    dp[i] = dp[i-5] + 1
```
- dp[3] == dp[5] == 1

prob : -1값 분류시 
