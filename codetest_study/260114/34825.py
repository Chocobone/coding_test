#https://www.acmicpc.net/problem/34825

# x, y 값의 차이의 합이 짝수여야 값이 존재한다
# 

import sys
input = sys.stdin.readline

def sign(x):
    if x > 0 : return 1
    elif x < 0 : return -1
    else : return 0

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())

diff_x = xb - xa
diff_y = yb - ya
diff = abs(diff_x) + abs(diff_y)

if diff%2 != 0:
    print(-1)
else:
    # xa, ya를 옮길 예정
    half = diff // 2

    moveX = min(abs(diff_x), half)
    moveY = half - moveX

    
    xa += sign(diff_x)*moveX
    ya += sign(diff_y)*moveY

    
    print(xa, ya)
            


