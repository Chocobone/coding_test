import sys
input = sys.stdin.readline

# 스위치 상태를 바꾸는 함수 (0 -> 1, 1 -> 0)
def change_switch(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0

# 1. 입력 받기
n = int(input()) # 스위치 개수
switch = list(map(int, input().split())) # 스위치 상태 리스트
students_count = int(input()) # 학생 수

# 2. 학생들의 동작 처리
for _ in range(students_count):
    gender, num = map(int, input().split())
    
    # 남학생인 경우 (배수 스위치 조작)
    if gender == 1:
        for i in range(num, n + 1, num): # num부터 n까지 num의 배수만큼 증가
            change_switch(i - 1) # 인덱스는 0부터 시작하므로 -1
            
    # 여학생인 경우 (대칭 구간 스위치 조작)
    else:
        idx = num - 1 # 기준 인덱스
        change_switch(idx) # 기준 위치는 무조건 변경
        
        # 좌우로 펼쳐가며 검사
        for k in range(1, n // 2 + 1):
            left = idx - k
            right = idx + k
            
            # 배열 범위를 벗어나거나, 좌우 대칭이 아니면 중단
            if left < 0 or right >= n or switch[left] != switch[right]:
                break
            
            # 대칭이면 상태 변경
            change_switch(left)
            change_switch(right)

# 3. 출력 하기 (한 줄에 20개씩)
for i in range(0, n, 20):
    print(*switch[i : i + 20])