수를 더하거나, 묶어 결과를 추출
-> DP!
- 이전 최댓값에서 다음 수를 곱하여 더하나 vs 다음 수를 그냥 더하냐

## 점화식
line = [0] + list(map(int, input().split()))

dp[1] = line[1]
dp[2] = max(line[1] + line[2], line[1]*line[2])
dp[i] = max(dp[i-1] + line[i], dp[i-2] + line[i-1] * line[i])