# 다이나믹_프로그래밍_재활 1일차
# 14494_인쇄_대행_서비스
# https://www.acmicpc.net/problem/14494

# 1. 점화식 세우기
# dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
# 2. 초기값 설정
# dp[1][1] = 1, dp[x][1] = 1, dp[1][y] = 1
# 3. 반복문 세우기(오류 없이)

import sys

x, y = map(int, sys.stdin.readline().split()) 

dp = [[0]*(y+1) for _ in range(x+1)] # (0~x) * (0~y)

for i in range(1, x+1) : dp[i][1] = 1
for j in range(1, y+1) : dp[1][j] = 1

for i in range(2, x+1) :
    for j in range(2, y+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

print(dp[x][y] % 1000000007)