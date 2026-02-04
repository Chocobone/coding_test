import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

def doldol_move_left(n):
    doldol = (a+c) - d*n
    if doldol > 0:
        return 0
    else:
        return doldol
    
def toka_move_left(n):
    c_ = c-(k*(n-1)) if c_ > 0 else 0
    toka = a - c_*n
    if toka > 0:
        return 0
    else:
        return toka

start = 0
end = 10e9
while(start <= end):
    mid = (start+end)//2

