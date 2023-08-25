# # 
## 5-6 인구이동

## Solution

### 문제의 아이디어 생각해낸 포인트
# 
### 시간 복잡도 계산
# A. 

### 소요시간
# 19: 00 ~ 
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    global result, finish
    change = [(x,y)]
    total = graph[x][y]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(graph[x][y] - graph[nx][ny])
                if l <= diff <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True

                    change.append((nx, ny))
                    total += graph[nx][ny]

    # print("change_location: ", change)
    if len(change) > 1:
        change_num = total // len(change)
        for c in change:
            cx, cy = c
            graph[cx][cy] = change_num

        finish = True
        
    # print("finish:", finish)

            

n, l, r = map(int, input().split(" "))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split(" "))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
global result, finish
result = 0

while(True):

    finish = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)
    if finish:
        result += 1
    # for h in graph:
    #     print(h)
    # print("result:", result)
    # print("============")
    
    if not finish:
        break

print(result)
        
    

    

