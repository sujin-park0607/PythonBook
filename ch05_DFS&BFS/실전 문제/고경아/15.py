import sys

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