# https://www.acmicpc.net/problem/9881

# 매개 범위 문제? -> cost가 최소가 되는 지점 찾는
# N<1000에 hill < 100이라 대입으로 구해서 풀었다

import sys
input = sys.stdin.readline

n = int(input())
hills = []
for _ in range(n):
    hills.append(int(input()))
hills.sort()

min_cost = float("inf")
for mid in range(1, max(hills)+1):
    cost = 0
    for i in hills:
        if i <= mid-9:
            cost += (mid-9-i)**2
        elif i >= mid+8:
            cost += (i-mid-8)**2
    if cost < min_cost: 
        min_cost = cost

print(min_cost)
    
    

