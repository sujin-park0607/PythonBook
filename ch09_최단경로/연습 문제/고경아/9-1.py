'''
[미래 도시]
1번 회사에서 출발하여 K번 회사를 지나 X번 회사로 가는 최단 경로

(READ_ME에도 있는 내용)
### 첫번째 풀이(=마지막 풀이)
1. `input = sys.stdin.readline()`와 같이 두고 `n, m = map(int, input.split())` 이렇게 사용하면, 입력값을 한 번만 받아 'input'이라는 변수에 저장하여 의도한 것과 다르게 작동합니다.
   `input = sys.stdin.readline`, `n, m = map(int, input().split())`와 같이 사용하여야 함수를 저장하여 짧은 이름으로 사용할 수 있습니다.
2. `graph = [] * (len(linked_company) + 1)`는 같은 리스트 여러 개를 참조하여 잘못된 결과로 이어집니다.
   - 올바른 선언은 `graph = [[] for _ in range(len(linked_company) + 1)]`입니다. (틀린 풀이 중 일부라, 이번 문제와 무관합니다.)
   - `graph = [[INF] * (n + 1) for _ in range(n+1)]`는 정상적으로 작동합니다. 두 식에서 파이썬의 객체 참조와 복사 방식이 다르다고 합니다.

회사 연결 정보를 그래프로 만든 후 다익스트라를 두 번 사용하여 해결했습니다.
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