# https://www.acmicpc.net/problem/27311 

import sys

t = int(sys.stdin.readline())
is_heart = False

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    cup = []
    for _ in range(n):
        cup.append(list(sys.stdin.readline().split()))
    
    for i in range(n):
        for j in range(m):
            for k in range(2, min(n, m)):

