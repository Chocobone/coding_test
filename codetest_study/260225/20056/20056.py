# https://www.acmicpc.net/problem/21610

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Mat = [list(map(int, input().split())) for _ in range(N)]

dcol = [0, -1, -1, -1, 0, 1, 1, 1]
drow = [-1, -1, 0, 1, 1, 1, 0, -1]

# 1. 초기 구름 위치
def move_clouds(clouds, d, s):
    new_clouds = []
    for x, y in clouds:
        new_x = (x + dcol[d] * s) % N
        new_y = (y + drow[d] * s) % N
        new_clouds.append((new_x, new_y))
    return new_clouds

# 2. 구름이 있는 칸에 물이 1씩 증가 후 3. 구름이 사라짐
def rain(clouds):
    for x, y in clouds:
        Mat[x][y] += 1

# 4. 물복사
def water_copy(clouds):
    for x, y in clouds:
        count = 0
        # 대각선 방면에만 물을 복사
        # 해당 과정에는 격자가 이어지지 않음
        for i in range(1, 8, 2):
            nx = x + dcol[i]
            ny = y + drow[i]
            if 0 <= nx < N and 0 <= ny < N and Mat[nx][ny] > 0:
                if Mat[nx][ny] > 0: count += 1
        Mat[x][y] += count

# 5. 새로운 구름
def new_clouds(clouds):
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if Mat[i][j] >= 2 and (i, j) not in clouds:
                new_clouds.append((i, j))
                Mat[i][j] -= 2
    return new_clouds

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    d, s = map(int, input().split())
    clouds = move_clouds(clouds, d-1, s)
    rain(clouds)
    water_copy(clouds)
    clouds = new_clouds(clouds)

answer = 0
for i in range(N):
    answer += sum(Mat[i])
print(answer)