# https://www.acmicpc.net/problem/2467
# sol1) 정렬 후 더블 포인터
# 문제 : 두 값의 합이 그리디로 나타나지 않는 상황 존재

# sol2) for문 안에서 binary search

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

diff = 10e9 
zero_found = False
for i in range(n-1):
    data = num[i]
    start, end = i+1, n-1
    while start <= end:
        mid = (start+end)//2
        temp = data + num[mid]
        if abs(temp) < diff:
            diff = abs(temp)
            left = i
            right = mid
            if temp == 0:
                zero_found = True
                break
        if temp < 0:
            start = mid+1
        else:
            end = mid-1

print(num[left], num[right])


# start = 0
# end = n-1
# result_small = num[start]
# result_big = num[end]
# while start+1 != end:
#     mid = num[start] + num[end]
#     if mid == 0:
#         break
#     elif mid > 0:
#         end -= 1
#     else:
#         start += 1

# result_small = num[start]
# result_big = num[end]
# print(result_small, result_big)
