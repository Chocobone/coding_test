# https://www.acmicpc.net/problem/25945

import sys
input = sys.stdin.readline

n = int(input())
port = list(map(int, input().split()))

m = 0
for i in port:
    m += i

average = m//n
move = 0
if m%n == 0:
    for i in port:
        move += abs(average - i)
else:
    # 평균으로 나눴을 때의 나머지들
    one_left = m%n

    for i in port:
        if one_left > 0:
            if average < i:
                move += abs(average - i + 1)
                one_left -= 1
        else:
            move += abs(average - i)
print((move+1)//2)