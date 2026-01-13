# https://www.acmicpc.net/problem/16967
# sol : 
# 겹치는 부분 : (H-X)*(W-Y)만큼 겹친다
# B[X][Y]부터 B[H-X+1][W-Y] 만큼
# 아래 예시의 경우 B[2][1]부터 B[2][2]
# B[X][Y]부터 B[X+H][Y+W]를 출력

# 3 3 2 1

# 1 2 3 0
# 4 5 6 0
# 7 9 11 3
# 0 4 5 6
# 0 7 8 9

import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

Mat_B = []
for _ in range(H+X):
    Mat_B.append(list(map(int, input().split())))
#range(2, 3-2+1), range(1, 3-1+2)
for i in range(X, H):
    for j in range(Y, W):
        Mat_B[i][j] = Mat_B[i][j] - Mat_B[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(Mat_B[i][j], end=' ')
    print()

