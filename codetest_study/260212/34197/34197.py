# https://www.acmicpc.net/problem/34197

import sys
input = sys.stdin.readline
output = sys.stdout.write

location = [0, 0]
found = False
na_sun = 0
while not found:
    search = []
    for _ in range(3):
        search.append(list(input().rstrip()))
    
    for i in range(3):
        for j in range(3):
            if search[i][j] == 'G':
                found = True
                break
        if found:
            break
    
    if not found:
        if (na_sun // 3) % 4 == 0:
            output("? L\n")
            location[0] -= 1
        elif (na_sun // 3) % 4 == 1:
            output("? U\n")
            location[1] += 1
        elif (na_sun // 3) % 4 == 2:
            output("? R\n")
            location[0] += 1
        elif (na_sun // 3) % 4 == 3:
            output("? D\n")
            location[1] -= 1
        sys.stdout.flush()
        na_sun += 1
