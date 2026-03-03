# https://www.acmicpc.net/problem/4811
import sys
import math
input = sys.stdin.readline

dp = [0] * 31
dp[1] = 1
dp[2] = 2
for i in range(3, 31):
    dp[i] = dp[i-1] + math.comb(2*(i-1)-1, 2)
while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(dp[N])