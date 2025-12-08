# https://www.acmicpc.net/problem/1003

from sys import stdin

t = int(stdin.readline())

n_list = []
for _ in range(t):
    n_list.append(int(stdin.readline()))

n_max = max(n_list)

dp = [[0,0] for _ in range(411)]
dp[0] = [1,0]
dp[1] = [0,1]

if(n_max>=2):
    for i in range(2, n_max+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in n_list:
    print(dp[i][0], end=' ')
    print(dp[i][1])
