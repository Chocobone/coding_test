# https://www.acmicpc.net/problem/1940

# 이중 for문 -> 시간 초과 확률 높음
# 투 포인터 : sort로 정렬 후 양 끝에서부터 좁혀가며 시작
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
left, right = 0, n - 1
count = 0

while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == m:
        count += 1
        left += 1
        right -= 1
    elif current_sum < m:
        left += 1
    else:
        right -= 1

print(count)