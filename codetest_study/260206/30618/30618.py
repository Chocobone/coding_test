# https://www.acmicpc.net/problem/30618

import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()


for i in range(n, 0, -1):
    if (n - i) % 2 == 0:
        dq.appendleft(i)
    else:
        dq.append(i)
print(*dq)