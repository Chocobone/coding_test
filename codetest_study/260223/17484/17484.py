# https://www.acmicpc.net/problem/17484

import sys
input = sys.stdin.readline

INF = sys.maxsize
N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    for d in range(3):
        dp[0][i][d] = road[0][i]
for i in range(1, N):
    for j in range(M):
        # 0: 왼쪽 위에서 옴 (이전 위치: j-1, 이전 방향: 1 or 2)
        if j > 0:
            dp[i][j][0] = road[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2])
        
        # 1: 바로 위에서 옴 (이전 위치: j, 이전 방향: 0 or 2)
        dp[i][j][1] = road[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
        
        # 2: 오른쪽 위에서 옴 (이전 위치: j+1, 이전 방향: 0 or 1)
        if j < M - 1:
            dp[i][j][2] = road[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])

ans = INF
for j in range(M):
    ans = min(ans, min(dp[N-1][j]))

print(ans)