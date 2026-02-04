import sys

n = int(sys.stdin.readline())
wine = list()
wine.append(0)  # dp와 wine 길이 맞추기

for _ in range(n):
    wine.append(int(sys.stdin.readline()))

dp = [0] * (n+1)
dp[1] = wine[1]

if(n >= 2): dp[2] = wine[1] + wine[2]

if(n >= 3):
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3])

print(dp[n])