#https://www.acmicpc.net/problem/2294
#(1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)

# 주어진 동전들을 최소한으로 사용해 k만큼의 가치를 만드는 방법
# sol1 : BFS
# ex) input :
# 3 15 
# 1 
# 5 
# 12
# output : 3

# sol2 : DP
# dp[i] = min(dp[i-1], dp[i-v]+1)

import sys
input = sys.stdin.readline
max_value = sys.maxsize

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins = sorted(list(set(coins)))

dp = [max_value] * (k+1)
dp[0] = 0

for v in coins:
    for i in range(v, k+1):
        if dp[i - v] != max_value:
            dp[i] = min(dp[i], dp[i-v] + 1)

print(dp[k] if dp[k] != max_value else -1)