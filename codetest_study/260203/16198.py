# https://www.acmicpc.net/problem/16918
# 채웠을 때 터질 칸/안터질 칸을 구분할 수 있도록 구현
# %4를 했을 때 반복된다!

import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
board = []
for _ in range(R):
    line = list(input().rstrip())
    board.append(line)

if N == 1:
    for i in range(R):
        print("".join(board[i]))    
elif N%4 == 2 or N%4 == 0:
    for i in range(R):
        print("".join(["O"] * C))
else:
    result = [["O"] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                result[i][j] = '.'
                if i-1 >= 0: result[i-1][j] = '.'
                if i+1 < R: result[i+1][j] = '.'
                if j-1 >= 0: result[i][j-1] = '.'
                if j+1 < C: result[i][j+1] = '.'
    if N%4 == 3:
        for i in range(R):
            print("".join(result[i]))
    else: #N > 1 and N%4 == 1
        board = [["O"] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if result[i][j] == 'O':
                    board[i][j] = '.'
                    if i-1 >= 0: board[i-1][j] = '.'
                    if i+1 < R: board[i+1][j] = '.'
                    if j-1 >= 0: board[i][j-1] = '.'
                    if j+1 < C: board[i][j+1] = '.'
        
        for i in range(R):
            print("".join(board[i]))
