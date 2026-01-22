# https://www.acmicpc.net/problem/12107
# n=1이 아니면 A는 '지우는 약수의 개수'를 정할 수 있다
# 모든 수는 1을 약수로 가진다 -> A는 먼저 지울 수 있으니 최적의 개수를 남길 수 있다
n = int(input())
if n==1: print('B')
else: print('A')