#https://www.acmicpc.net/problem/2294
#(1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)

# 주어진 동전들을 최소한으로 사용해 k만큼의 가치를 만드는 방법
# sol1 : BFS
# ex) input :
# 3 15 
# 1 
# 5 
# 12
# output : 3

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

from collections import deque
Q = deque()

def bfs(h, k):
    value = 0
    if len(Q) != 0:
        value += Q.popleft()
    for coin in coins:
        value += coin

        if value < k:
            Q.append(value)

        elif value == k:
            
    

for _ in range(k//min(coins) + 1):
