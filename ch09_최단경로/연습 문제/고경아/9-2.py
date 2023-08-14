# [전보]

import sys
input = sys.stdin.readline
INF = 1e9

# 도시의 개수 N, 통로의 개수 M, 메시지의 개수 C(s)
n, m, s = map(int, input().split())

# X 도시에서 Y 도시까지의 거리 Z
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

# 한 도시에서 같은 도시로 가는 경우 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 연결된 도시의 수
reachable_city = 0
for i in range(1, n + 1):
    if graph[s][i] != INF:
        reachable_city += 1

# 가장 먼 거리
max_distance = 0
for i in range(1, n + 1):
    max_distance = max(max_distance, graph[s][i])

# 연결된 도시의 수와 가장 먼 거리 출력
print(reachable_city - 1, max_distance)