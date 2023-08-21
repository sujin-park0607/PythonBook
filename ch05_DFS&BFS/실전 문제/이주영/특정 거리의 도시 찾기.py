# 입력 조건
# 출력 조건 
## X부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력합니다.
## 이때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1 출력합니다. 

# 어떤 나라에는 1 ~ n 도시와 M개의 단방향 도로가 존재한다.
# 특정 도시 X로부터 출발해서 도달할 수 있는 모든 도시중, 최단 거리가 정확히 K인
# 모든 도시의 번호를 출력하는 프로그램

# 아이디어
## 1. 서로 다른 간선의 비용이 동일할때는 BFS가 더 효율적이다.
## 2. visited를 distance를 계산하는 방식으로 체크할 수 있게 했다.


from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q :
    now = q.popleft()
    for next_node in graph[now] :
        if distance[next_node] == -1 :
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1) :
    if distance[i] == k :
        print(i)
        check = True
if check == False :
    print(-1)
    
