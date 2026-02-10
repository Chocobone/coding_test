import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Mat_A = [list(map(int, input().split)) for _ in range(N)]
Mat_B = [list(map(int, input().split)) for _ in range(M)]

def conv(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
