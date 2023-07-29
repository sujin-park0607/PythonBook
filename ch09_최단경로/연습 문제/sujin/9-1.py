# # 
## 9-1 미래도시

## Solution

### 문제의 아이디어 생각해낸 포인트
# 100 * 100 * 100 = 1,000,000를 탐색하기때문에 플로이드 워셜 사용 가능하다 판단
# 또한 출발점이 다양함, 1~ k까지, k~x까지의 다양한 출발점에 대한 모든 최단 경로를 구해야하기 때문에
# 출발지가 하나인 다익스트라보다는 플로이드 워셜을 사용하는 것이 좋다고 판다
# 다익스트라도 가능하지만 출발지를 다르게 해서 함수를 두번 호출해야함
# 1~K 까지의 거리, K~X까지의 거리 더하기 

### 시간 복잡도 계산
# A. O(N^3)  

# 양방향 그래프로 수정
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split(" "))

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기자신 0으로 초기화
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 처음에는 단방향으로 구현하는 실수함!
# for _ in range(m):
#     a, b = map(int, input().split(" "))
#     graph[a][b] = 1


for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

x, k = map(int, input().split(" "))

result = graph[1][k] + graph[k][x]

if result >= INF: print(-1)
else: print(result)
    

    



