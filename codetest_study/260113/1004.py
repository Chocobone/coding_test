# https://www.acmicpc.net/problem/1004
# (x-a)^2 + (y-b)^2과 r^2의 크기 비교를 통해 행성계 접근/이탈 최소화 가능

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    result = 0
    for _ in range(n):
        inNout = 0
        cx, cy, r = map(int, input().split())

        if (x1-cx)**2 + (y1-cy)**2 < r**2: inNout += 1
            
        if (x2-cx)**2 + (y2-cy)**2 < r**2: inNout += 1
        
        if inNout == 1: result += 1
        
    print(result)
        



