# https://www.acmicpc.net/problem/20056
import sys
input = sys.stdin.readline

dcol = [-1, -1, 0, 1, 1, 1, 0, -1]
drow = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireballs = []
Mat = [[0] * N for _ in range(N)]

for _ in range(M):
    fireballs.append(list(map(int, input().split())))


def move(fireballs):
    new_fireballs = []
    for x, y, m, s, d in fireballs:
        dx = (x + dcol[d] * s + N) % N
        dy = (y + drow[d] * s + N) % N
        new_fireballs.append(dx, dy, m, 0, 0)
    
    return new_fireballs

def combineNwrite(fireballs):
    same_place = []
    for x, y, m, s, d in fireballs:
        if Mat[x-1][y-1] == 0:
            Mat[x-1][y-1] = M
        else:
            