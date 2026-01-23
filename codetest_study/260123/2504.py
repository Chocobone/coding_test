# https://www.acmicpc.net/problem/2504
# 1. 중/대괄호가 열려있는지를 알려주는 flag로 열림/닫힘을 구분하기
# 2. 

import sys
input = sys.stdin.readline

txt = input().rstrip()
big_open = 0
small_open = 0
big_close = 0
small_close = 0

result = 0
for i in range(len(txt)):
    if txt[i] == '(':
        small_open += 1
    elif txt[i] == '[':
        big_open += 1
    elif txt[i] == ')':
        
    elif txt[i] == ']':

if big_open == 0 and small_open == 0:
    print(result)
else : print(0)