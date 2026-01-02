# https://www.acmicpc.net/problem/14888

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
# numbers.sort()
sig = list(map(int, input().split()))

def divide(num1, num2):
    if num1 > 0:
        return num1 // num2
    else:
        num1 = -num1
        return -(num1//num2)
    
# sol 2 : DFS 백트래킹 -> 가능한 모든 경우의 수 탐색
# max_val, min_val 설정 후 모든 결과를 구해가며 값 갱신
# 더하기, 뺴기, 곱하기, 나누기의 남은 숫자만큼 current_result를 갱신하며 재귀호출
max_val = -10e9
min_val = 10e9
def dfs(index, current_result, add, sub, mul, div):
    global max_val, min_val
    if index == n:
        if max_val < current_result:
            max_val = current_result
        if min_val > current_result:
            min_val = current_result
        return
    if add > 0:
        dfs(index + 1, current_result + numbers[index], add - 1, sub, mul, div)
    if sub > 0:
        dfs(index + 1, current_result - numbers[index], add, sub - 1, mul, div)
    if mul > 0:
        dfs(index + 1, current_result * numbers[index], add, sub, mul - 1, div)
    if div > 0:
        dfs(index + 1, divide(current_result, numbers[index]), add, sub, mul, div - 1)

dfs(1, numbers[0], sig[0], sig[1], sig[2], sig[3])
print(max_val)
print(min_val)

# sol 1: 기본적으로 정렬 후 최대값 최소값 구하면 될듯(그리디)
# 뒤의 숫자를 곱셈으로 최대한 크게 한 뒤 더하기와 빼기를 적절히 배치
# 계산 순서 : 무조건 앞에서부터 진행
# 최대값 : 뺄셈 -> 나누기 -> 더하기 -> 곱하기
# 최소값 : 더하기 -> 나누기 -> 빼기 -> 곱하기

# prob : 그리디로는 해결이 안됨
# ex) 1 2 3 4
#     2 1 0 1
# 최대값 : ((1+2)*3)+4 = 13
# 최소값 : (1-2-3)*4 = -16

# # 최대값 계산
# add, sub, mul, div = map(int, sig)
# max_result = numbers[0]
# # sub(빼기 구호가) 있을 때와 없을 때를 구분해서 계산
# if sub > 0:
#     for i in range(1, n):
#         if sub > 0:
#             max_result -= numbers[i]
#             sub -= 1
#         elif add > 0:
#             max_result += numbers[i]
#             add -= 1
#         elif div > 0:
#             max_result = divide(max_result, numbers[i])
#             div -= 1
#         else:
#             max_result *= numbers[i]
# # 없으면 나누기 -> 더하기 -> 곱하기
# else:
#     for i in range(1, n):
#         if div > 0:
#             max_result = divide(max_result, numbers[i])
#             div -= 1
            
#         elif add > 0:
#             max_result += numbers[i]
#             add -= 1
#         elif mul > 0:
#             max_result *= numbers[i]
#             mul -= 1

# # 최소값 계산
# add, sub, mul, div = map(int, sig)
# min_result = numbers[0]

# # sub(빼기 구호가) 있을 때와 없을 때를 구분해서 계산
# if sub > 0:
#     for i in range(1, n):
#         if add > 0:
#             min_result += numbers[i]
#             add -= 1
#         elif div > 0:
#             min_result = divide(min_result, numbers[i])
#             div -= 1
#         elif sub > 0:
#             min_result -= numbers[i]
#             sub -= 1
#         else:
#             min_result *= numbers[i]
# # 없으면 곱하기 -> 더하기 -> 나누기
# else:
#     for i in range(1, n):
#         if mul > 0:
#             min_result *= numbers[i]
#             mul -= 1
#         elif add > 0:
#             min_result += numbers[i]
#             add -= 1
#         elif div > 0:
#             min_result = divide(min_result, numbers[i])
#             div -= 1

# print(max_result)
# print(min_result)