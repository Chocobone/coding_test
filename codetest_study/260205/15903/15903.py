# https://www.acmicpc.net/problem/15903

import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())
card = PriorityQueue()
line = list(map(int, input().split()))
for i in range(N):
    card.put(line[i])

for _ in range(M):
    min_1st = card.get()
    min_2nd = card.get()

    min_1st += min_2nd
    card.put(min_1st)
    card.put(min_1st)

result = 0
for _ in range(N):
    result += card.get()

print(result)
