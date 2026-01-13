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


dp = [101] * 101
dp[1] = 0

for _ in range(100):
    for i in range(1, 101):
        if dp[i] == 101:
            continue
        for dice in range(1, 7):
            next_step = i + dice
            if next_step > 100:
                continue

            if ladderNsnake[next_step] != 0:
                target = ladderNsnake[next_step]
            else:
                target = next_step

            if dp[target] > dp[i] + 1:
                dp[target] = dp[i] + 1

print(dp[-1])
