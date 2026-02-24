#https://www.acmicpc.net/problem/15989

import sys
input = sys.stdin.readline

dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
def solution(n):
    if dp[n] != 0:
        return dp[n]
    for i in range(4, n+1):
        for j in range(1, (i//3)+1):
            dp[i] += ((i-3*j) // 2 + 1 ) * 3
    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))