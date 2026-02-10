# https://www.acmicpc.net/problem/16936

# 왼쪽으로 갈 수록 3이 많고 오른쪽으로 갈 수록 2가 많아짐
# 2, 3이 곱해진 개수를 각각 list로 나타내면 될듯?

import sys
input = sys.stdin.readline

N = int(input())

two_many = [0] * N
three_many = [0] * N

line = list(map(int, input().split()))

for i in range(N):
    num = line[i]
    while(num % 3 == 0):
        three_many[i] += 1
        num = num // 3
    num = line[i]
    while(num % 2 == 0):
        two_many[i] += 1
        num = num // 2

result = [0] * N
for i in range(N):
    front_idx = i
    for j in range(i+1, N):
        if three_many[front_idx] < three_many[j]:
            front_idx = j
        elif (three_many[front_idx] == three_many[j] and 
              two_many[front_idx] > two_many[j]):
            front_idx = j
    result[i] = line[front_idx]

    temp = line[i]
    line[i] = line[front_idx]
    line[front_idx] = temp
    temp = three_many[i]
    three_many[i] = three_many[front_idx]
    three_many[front_idx] = temp
    temp = two_many[i]
    two_many[i] = two_many[front_idx]
    two_many[front_idx] = temp

print(" ".join(str(x) for x in result))