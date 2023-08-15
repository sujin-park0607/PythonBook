# # 
## 5-2 연구소

## Solution

### 문제의 아이디어 생각해낸 포인트
# 지도를 딕셔너리로 구현
# bfs로 탐색
# 처음에 visited[start]를 true로 안해줘서 에러남

### 시간 복잡도 계산
# A. 

### 소요시간
# 3:03  ~ 4:27 / 정답 코드 참고

import itertools
import copy
from collections import deque
import sys

def bfs():
    q = deque()
    graph = copy.deepcopy(origin_graph)
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 2:
                q.append((x,y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = 2
    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    
    result = max(result,cnt)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split(" "))
origin_graph = []

for _ in range(n):
    origin_graph.append(list(map(int, input().split(" "))))

# arr = []
# for i in range(n):
#     for j in range(m):
#         arr.append([i,j])

# 벽이 될 수 있는 3가지의 경우의 수 모두 구하기
# 벽의 순서는 중요하지 않기 때문에 조합으로 구현
# nPr = itertools.permutations(arr,3)

# result = 0
# total_size = n * m
# for wall in nPr:
#     graph = copy.deepcopy(origin_graph)
#     # 벽세우기
#     for x, y in wall:
#         # x, y = w
#         graph[x][y] = 1

#     # 벽, 바이러스의 크기
#     total_cnt = 0

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if origin_graph[i][k] == 0:
                origin_graph[i][k] = 1
                make_wall(count+1)
                origin_graph[i][k] = 0

result = 0
make_wall(0)

print(result)
        
    
        

