#https://www.acmicpc.net/problem/35030
# str로 받아들인다음 N까지 체로 여부 확인하고 걸러내면 될 듯?0

import sys
input = sys.stdin.readline

T = int(input())

is_sosu = [1] * 100001
is_sosu[0] = 0
for i in range(2, 100000):
    if is_sosu[i] == 1:
        for j in range(2*i, 100000//i, i):
            is_sosu[j] = 0

is_special = [1] * 100001
def is_special(num):
    if is_sosu[int(num+1)] == 1:
        for i in range(1, num):
            special = int(N[:i]) * int(N[i:]) + 1
            if is_sosu[special] == 0:
                return False
        return True
    else : return False

special = [0] * 100001
for i in range(1, 100001):
    if is_special(i):
        special[i] = special[i-1] + 1
    else:
        special[i] = special[i-1]

for _ in range(T):
    # N = input().rstrip()
    
            