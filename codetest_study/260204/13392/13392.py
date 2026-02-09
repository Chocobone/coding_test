# https://www.acmicpc.net/problem/13392

import sys
INF = sys.maxsize

n = int(sys.stdin.readline())
start_str = sys.stdin.readline().strip()
target_str = sys.stdin.readline().strip()

dp = [INF] * 10

dp[0] = 0

for i in range(n):
    next_dp = [INF] * 10
    
    start_digit = int(start_str[i])
    target_digit = int(target_str[i])

    for j in range(10):
        if dp[j] == INF:
            continue
        
        current_val = (start_digit + j) % 10
        
        left_moves = (target_digit - current_val + 10) % 10
        new_offset_left = (j + left_moves) % 10
        
        if dp[j] + left_moves < next_dp[new_offset_left]:
            next_dp[new_offset_left] = dp[j] + left_moves
        
        right_moves = (current_val - target_digit + 10) % 10
        new_offset_right = j 
        
        if dp[j] + right_moves < next_dp[new_offset_right]:
            next_dp[new_offset_right] = dp[j] + right_moves

    dp = next_dp

print(min(dp))
