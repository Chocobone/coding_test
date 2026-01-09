# https://www.acmicpc.net/problem/16928

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = defaultdict(int)
snake = defaultdict(int)

queue = deque()
def bfs(depth):
    now = queue.popleft()
    if now >= 100:
        return depth
    if ladder[now] != 0:
        now = ladder[now]
    elif snake[now] != 0:
        now = snake[now]
    for i in range(1, 7):
        queue.append(now+i)
    return 0

queue.append(1)
depth = 0
while queue:
    bfs(depth)
    depth += 1


        




# dp 문제에 dict 사용하기
# dp[n번째 칸] = min(dp[n-6] + 1, dp[key] if key in dict)

# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# n, m = map(int, input().split())
# ladderNsnake = defaultdict(int)

# for _ in range(n+m):
#     key, value = map(int, input().split())
#     ladderNsnake[key] = value


# dp = [(4+i)//6 for i in range(101)]
# for i in range(101):
#     if ladderNsnake[i] != 0:
#         #dp[value] = dp[key]
#         dp[ladderNsnake[i]] = dp[i]

# for i in range(6, 100):
#     dp[i] = min( min(dp[i-6:i+1]) + 1, dp[i]) 


# for i in range(1, 100):
#     if dp[i] < dp[i-1]:
#         print(dp[i-1], dp[i], dp[i+1], end=' | ')
#         print(i-1, i, i+1)

# print(dp[-1])
