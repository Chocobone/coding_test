#https://www.acmicpc.net/problem/15989

import sys
input = sys.stdin.readline

# 1. DP 테이블 초기화 (n의 최댓값은 10000)
# 오직 '1'로만 합을 만드는 경우는 어떤 숫자든 무조건 1가지이므로 모두 1로 초기화합니다.
dp = [1] * 10001 

# 2. '2'를 더해서 만드는 경우의 수 추가
# 2부터 10000까지 순회하며, 현재 숫자(i)에서 2를 뺀 숫자를 만드는 경우의 수를 더해줍니다.
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 3. '3'을 더해서 만드는 경우의 수 추가
# 3부터 10000까지 순회하며, 현재 숫자(i)에서 3을 뺀 숫자를 만드는 경우의 수를 더해줍니다.
for i in range(3, 10001):
    dp[i] += dp[i - 3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])