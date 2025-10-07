import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

def doldol_move(n):
    doldol = (a+c) - d*n
    if doldol > 0:
        return 0
    else:
        return doldol
    
def toka_left_path(n):
    toka
