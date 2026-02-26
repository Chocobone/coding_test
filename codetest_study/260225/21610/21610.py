# https://www.acmicpc.net/problem/20056
import sys
input = sys.stdin.readline

dcol = [-1, -1, 0, 1, 1, 1, 0, -1]
drow = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
Mat = [[0] * N for _ in range(N)]

def move(fireballs, s, d):
    for x, y, m in fireballs:
        dx = (x + dcol[d] * s + N) % N
        dy = (y + drow[d] * s + N) % N
        Mat[x][y] = 0
        Mat[dx][dy] += M

def combine()