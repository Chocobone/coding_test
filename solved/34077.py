# https://www.acmicpc.net/problem/34077

# 순서에 따라 순서가 변하는 경우
# -> -a . b 에서 b가 0이 아니면 결과가 바뀐다!
# 1. -a+b -> -(a+b) != -a +b
# 2. -a-b -> -(a-b) != -a -b

# 확장 : -a (+0-0+0) . b 의 경우
# -(a+0-0+0+-b) != (-a+0-0+0-+b)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    line = [c for c in str(input().strip())] # line[0] ~ line[2*n]
    result = 'YES'
    i=1
    for _ in range(n - 1):
        if line[i] == "-": # - 부호가 들어갔을 때
            for j in range(2*n, i+2, -2):
                if int(line[j]) != 0: # 다음 부호 이후에 0이 아닌 값이 있다면
                    result = "NO"
                    break
            break
        i += 2
    print(result)

