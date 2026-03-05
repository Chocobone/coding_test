import sys
input = sys.stdin.readline

dp = [0] * 100001

N = int(input())

dp[0] = 1
dp[1] = 3
for i in range(2, N+1):
    