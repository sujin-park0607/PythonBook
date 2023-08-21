"""
특정 거리의 도시찾기

4 4 2 1
1 2
1 3
2 3
2 4
"""

from collections import deque
n, m, k, x = map(int, input().split())
# 단방향 그래프 생성
graph = [[] for _ in range(m+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

## 최단거리 초기화
distance = [-1]*(n+1)
distance[x]=0 #[-1, 0, -1, -1, -1]

## BFS
q = deque([x])
while q:
    now = q.popleft() # 현재 노드 꺼내기
    for nxt in graph[now]: # 해당 노드가 갈 수 있는 다음 노드들
        if distance[nxt] == -1: # 방문하지 않았는지 여부 확인
            distance[nxt] = distance[now]+1  # 거리 갱신
            q.append(nxt)


check = False
for i in range(1, n+1): #1번 노드부터 탐색
    if distance[i]==k: #주어진 k와 같은값 찾기
        print(i)
        check = True
if check == False:
    print(-1)


