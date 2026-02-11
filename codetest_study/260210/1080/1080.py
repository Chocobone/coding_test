# # https://www.acmicpc.net/problem/1080

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Mat_A = [list(map(int, input().split)) for _ in range(N)]
Mat_B = [list(map(int, input().split)) for _ in range(N)]

result = 0
for i in range(N-2):
    for j in range(M-2):
        if (Mat_A[i][j] + Mat_B[i][j]) % 2 == 1:
            for k in range(3):
                for l in range(3):
                    Mat_A[i+k][j+l] = (Mat_A[i+k][j+l] + 1) % 2
                    result += 1

is_flipable = True
for i in range(N):
    for j in range(M):
        if Mat_A[i][j] != Mat_B[i][j]:
            is_flipable = False
            break
    if not is_flipable:
        break

if is_flipable:
    print(result)
    