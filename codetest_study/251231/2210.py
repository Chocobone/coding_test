# https://www.acmicpc.net/problem/2210

# 1. 숫자판에 어떤 숫자가 있는지 분류
# 2. 있는 숫자들을 차례로 나열해 
#    "가능한 다음 숫자의 경우의 수" 계산
# 3. 각 경우의 수 계산 -> dp? bfs? 

import sys
input = sys.stdin.readline

# num_pad = []
# for _ in range(5):
#     num_pad.append(list(map(int, input().split())))

# 0-9의 "가능한 다음 숫자"를 set 사용해 구한다

# prob : defaultdict를 이용해 다음 숫자를 저장하면 
#       '좌표상에서 가능한 이동'보다 경우의 수가 많아짐

# from collections import defaultdict
# available_num = defaultdict(set)
# for i in range(5):
#     for j in range(5):
#         num = num_pad[i][j]
#         if i > 0:
#             available_num[num].add(num_pad[i-1][j])
#         if i < 4:
#             available_num[num].add(num_pad[i+1][j])
#         if j > 0:
#             available_num[num].add(num_pad[i][j-1])
#         if j < 4:
#             available_num[num].add(num_pad[i][j+1])

# # 경우의 수 구하기 -> dfs
# # 1을 골랐을 때 가능한 경우의 수 (1, 2)
# # 2를 골랐을 때 가능한 경우의 수 (1)
# count = 0
# TARGET_DEPTH = 6 # 6자리 숫자

# def dfs(current_depth, num_now):
#     global count

#     # 목표 깊이에 도달하면 카운트 증가 후 종료
#     if current_depth == TARGET_DEPTH:
#         count += 1
#         return
    
#     # 다음 깊이로 탐색 (가지 수만큼 반복)
#     for num_next in available_num[num_now]:
#         dfs(current_depth + 1, num_next)

# for i in available_num.keys():
#     dfs(1, i)

# -------------------------------------------------------------------------

# sol : 좌표를 기준으로 dfs를 박아버리기

num_pad = []
for _ in range(5):
    num_pad.append(list(map(str, input().split())))

result = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, number):
    if(len(number) == 6):
        result.add(number)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number + num_pad[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, num_pad[i][j])

print(len(result))