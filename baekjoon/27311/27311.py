# https://www.acmicpc.net/problem/27311 

import sys
input = sys.stdin.readline

t = int(input())
is_heart = False

for _ in range(t):
    n, m = map(int, input().split())
    cup = []
    for _ in range(n):
        cup.append(list(input()))
    
    heart_in_cup = 0
    for i in range(n-1):
        for j in range(m-1):
            is_heart = [cup[i][j], cup[i+1][j], cup[i][j+1], cup[i+1][j+1]]
            if(is_heart.count('#')==3 and is_heart.count('.')==1):
                heart_in_cup += 1
            if(heart_in_cup > 1):
                break
        if(heart_in_cup > 1):
            heart_in_cup = 0
            break
    print(heart_in_cup)


