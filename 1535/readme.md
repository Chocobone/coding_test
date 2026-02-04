https://www.acmicpc.net/problem/1535

# knapsack prob
### dp[k][W] = max(dp[k-1][W], value[k] + dp[k-1][W-K])

# 1. 초기값 설정
- dp[0][W] = 0
- dp[1][W] = 0

# 2. 조건 분류
- 가방에 물건을 담을 수 있다면, 즉 `weight[i] <= j`라면 `dp[k][W] = max(dp[k-1][W], value[k] + dp[k-1][W-K])`
- 물건을 담을 수 없다면 이전값(`dp[i-1][j]`)를 유지