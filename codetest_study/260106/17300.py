# https://www.acmicpc.net/problem/17300

# 가로 : 1-3, 4-6, 7-9
# 세로 : 1-7, 2-8, 3-9
# 대각 : 1-9, 3-7
# -> 5와의 거리 같음 : 1-9, 2-8, 3-7, 4,6
#    5와의 거리 다름 : 1-7, 3-9, 1-3, 7-9

import sys
input = sys.stdin.readline

n = int(input())
pattern = list(map(int, input().split()))

result = 'YES'
pattern_check = True
for i in range(1, 10):
    if pattern.count(i) > 1:
        result = 'NO'
        pattern_check = False
        break

if pattern_check:
    # 사잇값 여부를 확인
    between = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(1, 10):
        for j in range(i+1, 10):
            if abs(5-i)==abs(5-j):
                between[i][j] = 5
                between[j][i] = 5
            elif i == 1 and j == 3:
                between[i][j] = 2
                between[j][i] = 2
            elif i == 1 and j == 7:
                between[i][j] = 4
                between[j][i] = 4
            elif i == 3 and j == 9:
                between[i][j] = 6
                between[j][i] = 6
            elif i == 7 and j == 9:
                between[i][j] = 8
                between[j][i] = 8
            
    visited = [False] * 10
    for i in range(n-1):
        now = pattern[i]
        next = pattern[i+1]
        if between[now][next] != 0:
            if not visited[between[now][next]]:
                result = 'NO'
                break
        visited[now] = True

print(result)

# five_already = False
# if pattern_check:
#     for i in range(n-1):
#         now = pattern[i]
#         if now == 5:
#             five_already = True
#         next = pattern[i+1] 
#         # 5와의 거리 같음 : 1-9, 2-8, 3-7, 4-6
#         # 고려 : 5가 먼저 나왔다면 넘어간다(29%)
#         if not five_already and abs(5-now) == abs(5-next):
#             result = 'NO'
#             break
#         # 5와의 거리 다름 : 1-7, 3-9, 1-3, 7-9
#         # 고려 : 사이값이 먼저 나온 경우 pass -> graph 구조가 더 직관적
#         elif now == 1 and (next == 3 or next == 7):
#             result = 'NO'
#             break
#         elif now == 3 and (next == 1 or next == 9):
#             result = 'NO'
#             break
#         elif now == 7 and (next == 1 or next == 9):
#             result = 'NO'
#             break
#         elif now == 9 and (next == 3 or next == 7):
#             result = 'NO'
#             break

# print(result)