'''
[미래 도시]
1번 회사에서 출발하여 K번 회사를 지나 X번 회사로 가는 최단 경로
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 전체 회사의 개수 N과 경로의 개수 M
n, m = map(int, input().split())

# 연결된 두 회사 A와 B의 번호
linked_company = []
for _ in range(m):
    a, b = map(int, input().split())
    linked_company.append((a, b))

# 연결된 회사 그래프 생성
graph = [[] for _ in range(n + 1)]
for i in range(len(linked_company)):
    graph[linked_company[i][0]].append((linked_company[i][1], 1))
    graph[linked_company[i][1]].append((linked_company[i][0], 1))

# 거쳐갈 회사 K와 마지막 도착지 회사 X
x, k = map(int, input().split())

# 한 노드에서 다른 노드까지의 최단 경로를 구하는 다익스트라
distance = [INF] * (n + 1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 1에서 K까지 가는 최단 경로를 구한다
dijkstra(1)
k_root = distance[k]

# 같은 방법으로 K에서 X까지 가는 최단 경로를 구한다.
dijkstra(k)
x_root = distance[x]

# '1에서 K까지 가는 최단 경로 + K에서 X까지 가는 최단 경로'를 출력한다
if (k_root == INF) or (x_root == INF):
    print(-1)
else:
    print(k_root + x_root)