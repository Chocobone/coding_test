https://www.acmicpc.net/problem/2156

# 1. 점화식을 세울 수 있는가?
case 1: i-1, i 번째 포도주를 먹는 경우
`dp[i] = wine[i] + wine[i-1] + dp[i-3]`
case 2: i-2, i 번째 포도주를 먹는 경우
`dp[i] = wine[i] + wine[i-2] + dp[i-3] = wine[i] + dp[i-2]`
case 3: i-2, i-1번째 포도주를 먹는 경우
`dp[i] = wine[i-1] + wine[i-2] + dp[i-3] = dp[i-1]`

# 2. 초기값 설정
`dp[0] = 0, dp[1] = wine[1], dp[2] = wine[1]+wine[2]`
`dp[3] = max(dp[2], dp[1]+wine[3], dp[0]+wine[1]+wine[2])`
