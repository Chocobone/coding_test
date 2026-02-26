## 접근 방식

- "연쇄 여부 확인 -> 연쇄 적용(puyo 없애기) -> 중력 적용" 의 사이클 반복

### 연쇄 여부
- 연결된 puyo들을 하나의 뭉탱이로 구분해야 함
- bfs : 같은 색인지 여부확인 + queue에 넣을 때 puyo 개수 갱신
- 별도의 puyopuyo_queue에 (puyo 개수, [각 puyo 좌표])로 넣어 연쇄 작용에 사용

### 연쇄 작용
- puyopuyo_queue에서 pop할 때 마다 result += 1
- 해당 과정 후 puyopuyo_queue는 empty

### 중력 작용
- 바닥과 puyo간 높이 H를 구한 뒤 '.'이 아니면 덮어씌운다