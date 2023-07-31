# # 
## 10-2 도시 분할 계획

## Solution

### 문제의 아이디어 생각해낸 포인트
# 최소비용 경로 
# 크루스칼 알고리즘사용하여 최소 신장트리 구하기
# 이후 최대 비용인 간선 하나 끊기 -> 마을이 두개로 분할됨
# sys.stdin.readline을 사용하지않으면 시간초과남

### 시간 복잡도 계산
# A.   
import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split(" "))
parent = [0] * (n+1)
edges = []
cost = []
result = 0

for i in range(1, n+1):
    parent[i] = i
    
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    edges.append((c, a, b))

edges.sort()


for edge in edges:
    c, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        cost.append(c)
cost.sort(reverse=True)

for i in cost[1:]:
    result += i

print(result)
    


