#https://www.acmicpc.net/problem/15235

#sol : deque or for loop 사용

from sys import stdin

n = int(stdin.readline())
pizza = list(map(int, stdin.readline().split()))
pizza_total = 0

result = [0] * (n)
while(pizza_total < pizza):
    contestant = pizza_total%(sum(pizza))


print((result))