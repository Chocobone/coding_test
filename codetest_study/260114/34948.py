# https://www.acmicpc.net/problem/34948
# defaultdict(int) 사용, 같은 새로 길이를 모두 합쳐 최대값 도출
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

col_len = list(map(int, input().split()))
row_len = list(map(int, input().split()))

choco_sum = defaultdict(int)
result_col = col_len[0]
result_row = row_len[0]
for i in range(n):
    choco_sum[col_len[i]] += row_len[i]
    choco_size = col_len[i] * choco_sum[col_len[i]]

    result = result_col * result_row
    if result < choco_size:
        result_col = col_len[i]
        result_row = choco_sum[col_len[i]]

    elif result < col_len[i] * (result_row + row_len[i]):
        result_row += row_len[i]

print(result)