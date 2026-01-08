#https://www.acmicpc.net/problem/20437

# 특정 문자열이 n만큼 반복되는 문장 중 가장 짧은거 하나 긴거 하나
# defaultdict 사용해서 넣으면 되나
import sys
from collections import defaultdict
input = sys.stdin.readline
max_value = sys.maxsize

t = int(input())
for _ in range(t):
    count_dict = defaultdict(list)
    string = list(map(str, input().rstrip()))
    k = int(input())

    min_count = max_value
    max_count = 0
    result = False
    for i in range(len(string)):
        spell_loc = count_dict[string[i]]
        spell_loc += [i+1]
        if len(spell_loc) >= k:
            result = True
            spell_count = spell_loc[-1] - spell_loc[-k]
            if spell_count < min_count : min_count = spell_count
            if spell_count > max_count : max_count = spell_count
        
    if result:
        print(min_count+1, end=' ')
        print(max_count+1)
    else:
        print(-1)
