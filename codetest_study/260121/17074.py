# https://www.acmicpc.net/problem/17074
# dp[i] = i번째 원소 중에서 1개를 뺐을 때 정렬이 되는 경우의 수
# 1. arr[i]가 max보다 크다
# 2. arr[i]가 max보다 작고 max-1보다 크다
# 3. arr[i]가 max-1보다 작다

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
can_pop = 1
max_idx = 1
max_2nd = 0

for i in range(2, n+1):
    if can_pop == 1: # i-1까지는 정렬되어 있음
        if arr[i] >= arr[i-1]: #-> max_idx = i-1 
            dp[i] = dp[i-1] + 1
            max_idx = i
        else: # 정렬이 안됐을 때
            if arr[i] >= arr[i-2]:
                dp[i] = 2
                max_2nd = i
            else:
                dp[i] = 1
                max_2nd = i-2
            can_pop -= 1
    elif can_pop == 0:
        if arr[i] >= arr[max_idx]:
            dp[i] = 2
            max_idx = i
        elif arr[i] >= arr[max_2nd]:
            dp[i] = 1
        else:
            can_pop -= 1
    
    if can_pop < 0:
        break
    

print(dp[n])
# print(can_pop)
# print(dp)