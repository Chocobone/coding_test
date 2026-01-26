# https://www.acmicpc.net/problem/22983
# 체스판 격자를 dp로 구현, 다른지 여부를 확인하기
# 격자라면 dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input().rstrip()))

total = 0
dp = [[1] * (m) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i>0 and j>0:
            if (board[i][j] == board[i-1][j-1] and
                board[i][j] != board[i-1][j] and
                board[i][j] != board[i][j-1]):
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1      
        total += dp[i][j]

print(total)
        

# def is_chessboard(i, j):
#     if i>0 and board[i][j] == board[i-1][j]:
#         return False
#     if i<n-1 and board[i][j] == board[i-1][j]:
#         return False
#     if j>0 and board[i][j] == board[i][j-1]:
#         return False
#     if j<m-1 and board[i][j] == board[i][j-1]:
#         return False
#     return True