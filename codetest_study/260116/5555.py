# https://www.acmicpc.net/problem/5555
# 걍 하드코딩을 구현하면 될거같으

import sys
input = sys.stdin.readline

word = input().rstrip()
n = int(input())

result = 0
for _ in range(n):
    ring = input().rstrip()
    for i in range(10):
        has_word = True

        for j in range(len(word)):
            if ring[(i+j)%10] != word[j]:
                has_word = False
                break
        
        if has_word:
            result += 1
            break
print(result)
