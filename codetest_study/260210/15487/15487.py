# https://www.acmicpc.net/problem/15487

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
line = list(map(int, input().split()))

minA = line[0]
leftA = -INF
for j in range(1, N-2):
    leftA = max(leftA[j-1])