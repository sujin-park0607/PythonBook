'''
[도시 분할 계획]
떠올린 방법. 두 개의 신장 트리로 나눈다 -> 사이클을 만드는 길을 없앤다 (첫번째 단계가 감이 안 잡힘)
수정한 방법. 최소 신장 트리를 찾아 가장 비용이 큰 간선을 제거한다
'''
import sys
input = sys.stdin.readline
INF = 1000

# 집의 개수 N, 길의 개수 M
n, m = map(int, input().split())

# A번 집과 B번 집을 연결하는 길의 유지비 C
### 당연히 그래프부터 만들고 있었는데 (`graph = [...]`) 이건 최단 경로 알고리즘에서만 필요하고, 여기서는 부모 테이블을 만들어야 함.

# 찾기 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return x

# 합치기 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a

# 부모 테이블 초기화
parent = [0] * (v + 1)
for i in range(1, n + 1):
    parent[i] = i

# 간선과 유지비 초기화
edges = []
cost = 0

for _