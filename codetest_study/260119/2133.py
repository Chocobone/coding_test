# https://www.acmicpc.net/problem/2133
# 3*n길이에 둘 수 있는 타일 경우의 수 -> dp[n]
# n이 홀수면 3*n도 홀수 -> 타일로 채우기 불가능하다


n = int(input())

if n%2 != 0: print(0)
else:
    dp = [0] * (n+1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3

        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2
    
    print(dp[n])