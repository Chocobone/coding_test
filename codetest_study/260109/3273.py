import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
x = int(input())

i = 0
j = n-1

result = 0
while (i < j):
    numsum = num[i] + num[j]
    if numsum < x:
        i += 1
    elif numsum > x:
        j -= 1
    else:
        result += 1
        i += 1
        j -= 1

print(result)

