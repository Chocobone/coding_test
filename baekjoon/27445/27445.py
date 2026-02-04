# 고라니의 좌표 : 가장 작은 두 숫자의 index
# 숫자가 ㄴ자로 주어짐 -> for문 통해 n-1까지 진행한 뒤 n번째에 세로를 읽으면 됨
import sys

n, m = map(int, sys.stdin.readline().split())
x = []
for _ in range(n-1):
    x.append(int(sys.stdin.readline()))
y = list(map(int, sys.stdin.readline().split()))
x.append(y[0])  # 마지막에 세로를 추가

print(str(x.index(min(x))+1) + ' ' + str(y.index(min(y))+1))