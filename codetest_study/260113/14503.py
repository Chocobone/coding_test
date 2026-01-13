import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def cleaning(x, y, d):
    clean_count = 0
    
    while True:
        # 1. 현재 위치 청소
        if room[x][y] == 0:
            room[x][y] = 2 # 청소를 했고 벽이 아님
            clean_count += 1

        # 2. 주변 4칸 탐색
        cleaned_something = False # 이번 턴에 청소를 했는지 체크하는 깃발
        
        for _ in range(4):
            # 2-a. 반시계 방향 회전 (0->3->2->1)
            d = (d + 3) % 4
            
            mx = x + dx[d]
            my = y + dy[d]

            # 2-b. 앞쪽이 청소하지 않은 빈 칸이면 전진
            if 0 <= mx < n and 0 <= my < m and room[mx][my] == 0:
                x, y = mx, my
                cleaned_something = True
                break # for문을 탈출하고 다시 1번 단계(while 처음)로 돌아감

        # 3. 4칸 중 청소할 곳이 없었던 경우 (후진 로직)
        if cleaned_something == False: # 
            # 바라보는 방향 유지한 채로 후진 (빼기 연산)
            bx = x - dx[d]
            by = y - dy[d]
            
            # 뒤쪽이 벽이라 후진할 수 없으면 작동 멈춤
            if room[bx][by] == 1:
                break
            else:
                x, y = bx, by
                
    return clean_count

print(cleaning(x, y, d))