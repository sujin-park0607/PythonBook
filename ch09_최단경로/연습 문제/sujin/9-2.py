# # 
## 9-2 전보

## Solution

### 문제의 아이디어 생각해낸 포인트
# 플로이드 워셜로 풀기에는 30,000^3 이므로 시간초과
# 다익스트라 우선순위 큐로 구현
# 어려웠던 점: 그래프와 우선순위 큐에서 시간, 노드의 순서가 달라서 헷갈림

### 시간 복잡도 계산
# A. O()  

# 양방향 그래프로 수정
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split(" "))

distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split(" "))
    graph[x].append((y,z)) #(노드, 시간)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #(시간, 노드)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            time = dist + i[1]
            if time < distance[i[0]]:
                distance[i[0]] = time
                heapq.heappush(q,(time,i[0]))

dijkstra(c)

cnt = 0
maxTime = 0

for i in distance:
    if i >= INF or i==0: continue
    else:
        cnt +=1
        if i > maxTime:
            maxTime = i
print(cnt,maxTime)


    




    


    



