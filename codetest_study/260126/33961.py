# https://www.acmicpc.net/problem/33961
# 1. 2*M 모양의 체스판 -> 나이숍이 한 번에 갈 수 있는 경우의 수가 4가지 밖에 없다
# chessboard[0][N] 
# -> chessboard[1][N-2], chessboard[1][N-1],
#    chessboard[1][N+2], chessboard[1][N+1]ㅁㄴㅇㄹ

# sol1) 나이숍 투어가 가능한 경우를 분석
# 3, 4, 5 가능 -> 1, 2 제외하고 %3한 값으로 계산하기

def three(i):# 3 + 0
    print(1, 1+i)
    print(2, 3+i)
    print(1, 2+i)
    print(2, 1+i)
    print(1, 3+i)
    print(2, 2+i)

def four(i): # 3 + 1
    print(1, 1+i)
    print(2, 2+i)
    print(1, 4+i)
    print(2, 3+i)
    print(1, 2+i)
    print(2, 1+i)
    print(1, 3+i)
    print(2, 4+i)

def five(i): # 3 + 2
    print(1, 1+i)
    print(2, 2+i)
    print(1, 4+i)
    print(2, 5+i)
    print(1, 3+i)
    print(2, 1+i)
    print(1, 2+i)
    print(2, 3+i)
    print(1, 5+i)
    print(2, 4+i)

n = int(input())

if n == 1 or n == 2:
    print("NO")

# 3, 6, 9, ...
elif n%3 == 0:
    print("YES")
    for i in range(0, n, 3):
        three(i)
    
# 4, 7, 10, ...
elif n%3 == 1:
    print("YES")
    for i in range(0, n-6, 3):
        three(i)
    four(n-4)

#5, 8, 11, ...
elif n%3 == 2:
    print("YES")
    for i in range(0, n-7, 3):
        three(i)
    five(n-5)
    