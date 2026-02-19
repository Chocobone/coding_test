# https://www.acmicpc.net/problem/31801

import sys
input = sys.stdin.readline

is_num = [0] * 1000001
for i in range(100, 1000001):
    num = str(i)
    num_stack = 0
    for j in range(len(num)-1):
        if num[j] > num[j+1] and num_stack == 0:
            num_stack += 1
        elif num[j] <= num[j+1] and num_stack == 1:
            num_stack += 1
            break
    if num_stack < 2:
        is_num[i] += is_num[i-1] + 1
    else:
        is_num[i] = is_num[i-1]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(is_num[b+1] - is_num[a])
    print(is_num[:b+1])