import sys
from collections import deque

input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# n, m, k, x = map(int, input().split())
n, m, k, x = 4, 4, 2, 1

# A번 도시에서 B번 도시로 이동하는 단방향 도로 (거리는 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# X 도시로부터 최단 거리가 K인 도시의 개수
result = -1

# X 도시로부터 각 도시까지의 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# DFS
q = deque([x])
while q: # 모든 도시를 방문하여 큐가 빌 때까지 반복
    now = q.popleft() # 현재 도시를 꺼냄
    for next_node in graph[now]:
        if distance[next_node] == -1: # 아직 방문하지 않은 도시일 경우
            distance[next_node] = distance[now] + 1 # 최단 거리 갱신
            q.append(next_node) # 방문한

result = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        result = True
if result == False:
    print(-1)