import sys
input = sys.stdin.readline

N = int(input())
micros = []
line = list(map(int, input().split()))

nodes = [[0, 0, i-1, i+1] for i in range(N + 2)]
# [size, original_index, prev_idx, next_idx]
for i in range(1, N + 1):
    nodes[i][0] = line[i-1] # 크기
    nodes[i][1] = i         # 원래 번호

# 더미 노드 연결 수정
nodes[1][2] = -1
nodes[N][3] = -1

head = 1
total_remaining = N

while total_remaining > 1:
    current = head
    to_remove = set()
    active_this_turn = []
    
    # 이번 턴에 활동할 미생물 순서대로 수집
    curr = head
    while curr != -1:
        active_this_turn.append(curr)
        curr = nodes[curr][3]
    
    changed = False
    for i in active_this_turn:
        if i in to_remove:
            continue
        
        eaten_sum = 0
        # 왼쪽 확인
        prev_idx = nodes[i][2]
        if prev_idx != -1 and nodes[prev_idx][0] <= nodes[i][0]:
            eaten_sum += nodes[prev_idx][0]
            to_remove.add(prev_idx)
            # 연결 끊기
            new_prev = nodes[prev_idx][2]
            nodes[i][2] = new_prev
            if new_prev != -1:
                nodes[new_prev][3] = i
            else:
                head = i # 헤드가 먹혔으면 현재 노드가 새로운 헤드
            changed = True
        
        # 오른쪽 확인
        next_idx = nodes[i][3]
        if next_idx != -1 and nodes[next_idx][0] <= nodes[i][0]:
            eaten_sum += nodes[next_idx][0]
            to_remove.add(next_idx)
            # 연결 끊기
            new_next = nodes[next_idx][3]
            nodes[i][3] = new_next
            if new_next != -1:
                nodes[new_next][2] = i
            changed = True
        
        nodes[i][0] += eaten_sum
    
    total_remaining -= len(to_remove)
    if not changed: # 더 이상 서로 잡아먹을 수 없는 상태
        break

print(nodes[head][0])
print(nodes[head][1])
