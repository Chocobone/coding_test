# https://www.acmicpc.net/problem/16928
# dp 문제에 dict 사용하기
# dp[n번째 칸] = min(dp[n-6] + 1, dp[key] if key in dict)

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
ladderNsnake = defaultdict(int)

for _ in range(n+m):
    key, value = map(int, input().split())
    ladderNsnake[key] = value


dp = [(5+i)//6 for i in range(100)]
for i in range(100):
    if ladderNsnake[i] != 0:
        #dp[value] = dp[key]
        dp[ladderNsnake[i]] = dp[i]
for i in range(6, 100):
    dp[i] = min( min(dp[i-6:i+1]) + 1, dp[i]) 

print(dp[-1])
