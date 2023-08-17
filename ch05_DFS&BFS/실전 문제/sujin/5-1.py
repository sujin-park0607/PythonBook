# # 
## 5-1 특정 거리의 도시 찾기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 지도를 딕셔너리로 구현
# bfs로 탐색
# 처음에 visited[start]를 true로 안해줘서 에러남

### 시간 복잡도 계산
# A. 

### 소요시간
# 2:00 ~ 3:01
import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start):
    cnt = 0
    q = deque()
    q.append(start)
    visited[start] = True 
    

    while q:
        node = q.popleft()
        # print("node===",node)
        for next_node in graph[node]:
            if not visited[next_node]:
            # if distance[next_node] <= distance[node] + 1:
                visited[next_node] = True
                distance[next_node] = distance[node] + 1
                q.append(next_node)
                # print("q:",q)
        # print(distance)
    return distance

n, m, k, x = map(int, input().split(" "))
visited = [False] * (n+1)
distance = [0] * (n+1)
graph = dict()
result = []

for i in range(1,n+1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, input().split(" "))
    # 딕셔너리에 없으면 리스트를 만들고 있으면 리스트에 b를 추가해라
    graph[a] += [b]

distance = bfs(graph, x)
check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)
# 반례
# 4 5 3 1
# 1 2
# 1 3
# 2 3
# 2 4
# 4 1
        

