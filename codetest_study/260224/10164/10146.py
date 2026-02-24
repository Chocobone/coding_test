#https://www.acmicpc.net/problem/10164

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

if K == 0:
    Mat = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        Mat[i][1] = 1
    for j in range(1, M+1):
        Mat[1][j] = 1
    for i in range(2, N+1):
        for j in range(2, M+1):
            Mat[i][j] = Mat[i-1][j] + Mat[i][j-1]
    print(Mat[N][M])

else:
    point_x = (K-1) // M + 1
    point_y = (K-1) % M + 1
    # print(point_x, point_y)
    Mat = [[0] * (M+2) for _ in range(N+2)]
    for i in range(1, point_x+1):
        Mat[i][1] = 1
    for j in range(1, point_y+1):
        Mat[1][j] = 1
    for i in range(2, point_x+1):
        for j in range(2, point_y+1):
            Mat[i][j] = Mat[i-1][j] + Mat[i][j-1]
    
    for i in range(point_x+1, N+2):
        Mat[i][point_y+1] = 1
    for j in range(point_y+1, M+2):
        Mat[point_x+1][j] = 1
    for i in range(point_x+2, N+2):
        for j in range(point_y+2, M+2):
            Mat[i][j] = Mat[i-1][j] + Mat[i][j-1]
    
    # print(Mat)
    print(Mat[point_x][point_y] * Mat[N+1][M+1])