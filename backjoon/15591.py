import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

def bfs(K,V):
    cnt = 0
    q = deque([])
    q.append((V,INF))
    visited[V] = True

    while q:
        V, usado = q.popleft()

        for next_v, next_usado in graph[V]:
            next_usado = min(next_usado,usado)
            if visited[next_v]:
                continue
            if next_usado < K:
                continue
            q.append((next_v, next_usado))
            visited[next_v] = True
            cnt +=1 
    print(cnt)

N, Q = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, usado = list(map(int, input().split()))
    graph[a].append((b, usado))
    graph[b].append((a, usado))

for _ in range(Q):
    visited = [False for _ in range(N+1)]
    K, V = list(map(int, input().split()))
    bfs(K, V)
    
