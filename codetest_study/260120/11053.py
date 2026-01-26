# https://www.acmicpc.net/problem/11053
# 각 원소별(N)로 시작해서 binary search(logN)해서 


import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
arr = [lst[i]]

for i in range(1, n):
    if lst[i] > arr[-1]:
        arr.append(lst[i])
    else:
        start, end = 0, n-1
        while start < end:
            mid = (start+end)//2
            if lst[mid] < lst[i]:
                start = mid+1
            else:
                end = mid-1
        arr[start] = lst[i]
        

print(len(arr))