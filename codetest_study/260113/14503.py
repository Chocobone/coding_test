# https://www.acmicpc.net/problem/14503
# 로봇이 하는 행동을 구현해서 함수로 만들기
# 북:0 동:1 남:2 서:3
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

clean_count = 0
def cleaning(x, y, d):
    global clean_count
    # 1. 로봇 청소기 칸이 0이면 1로 만들어라(청소해라)
    if room[x][y] == 0:
        room[x][y] = 1
        clean_count += 1
        cleaning(x, y, d)

    else:
        # 북 - 동 - 남 -서 순서로 정렬(시계)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        #d = [0, 1, 2, 3]

        #2. 주위 4칸이 청소가 안되어 있다면 반시계 방향으로 회전하며 확인하라
        not_cleaned = False
        # 반시계 방향을 구현
        for i in range(d, d+12, 3):
            # 반시계방향 회전 -> +3을 한뒤 %4하면 구분 가능
            mx = x + dx[i%4]
            my = y + dy[i%4]

            if 0 <= mx < n and 0 <= my < m and room[mx][my] == 0:
                not_cleaned = True
                d = i
                break
        if not_cleaned:
            cleaning(mx, my, d)
        else:
            #바라보는 방향을 유지한 채로 '후진'
            mx = x + dx[(d+2)%4]
            my = y + dy[(d+2)%4]
            if 0 <= mx < n and 0 <= my < m:
                cleaning(mx, my, d)
            else:
                return

cleaning(x, y, d)
print(clean_count)
