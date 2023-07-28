# # 
## 9-1 미래도시

## Solution

### 문제의 아이디어 생각해낸 포인트
# 100 * 100 * 100 = 1,000,000를 탐색하기때문에 플로이드 워셜 사용 가능하다 판단
# 다익스트라에 우선순위 큐가 필요한가 라는 생각에 다익스트라는 패스
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
    

    



