
"""
경쟁적 전염
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""

from collections import deque
n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split()))) # 1 0 2
    for j in range(n):
        if graph[i][j]!=0:
            ## 바이러스 종류, 시간, 위치x, 위치y
            # [(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)]
            data.append((graph[i][j], 0, i, j))

print(data)
data.sort()

q = deque(data)
print(q)
# 지난 시간, 바이러스 좌표 x, y
ts, tx, ty = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    virus, s, x, y = q.popleft()
    if s == ts:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx and nx <n and 0<=ny and ny<n:
            ## 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny]==0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
print(graph[tx-1][ty-1])