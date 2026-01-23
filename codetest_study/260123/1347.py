# https://www.acmicpc.net/problem/1347
# L : 좌회전, R : 우회전, F : 전진
# 처음 바라보는 방향은 남쪽

import sys

n = int(sys.stdin.readline())
route = sys.stdin.readline().rstrip()
x_route = [0]
y_route = [0]

SOUTH = 0
EAST = 1
NORTH = 2
WEST = 3
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
def move(x, y, dirr_now, next, count):
    if next == 'L':
        dirr_now = (dirr_now-1)%4
    elif next == 'R':
        dirr_now = (dirr_now+1)%4
    elif next == 'F':
        x += dx[dirr_now]
        y += dy[dirr_now]
    x_route.append(x)
    y_route.append(y)
    if count < n-1:
        move(x, y, dirr_now, route[count+1], count+1)
    else:
        return

move(0, 0, SOUTH, route[0], 0)

x_min = min(x_route)
y_min = min(y_route)
for i in range(n+1):
    x_route[i] -= x_min
    y_route[i] -= y_min

y_range = max(y_route)+1
x_range = max(x_route)+1

maze = [['#']*x_range for _ in range(y_range)]
for i in range(n+1):
    maze[y_route[i]][x_route[i]] = '.'

for i in range(y_range-1, -1, -1):
    print("".join(maze[i]))