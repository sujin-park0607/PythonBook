# # 
## 5-1 음료수 얼려 먹기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 이중 for문을 사용해서 모든 맵을 조회, 얼음구명(0) 이면서 방문하지 않은 곳 dfs로 탐색
# bfs로 계속해서 이어져 있는 얼음구멍 탐색하면서 방문처리
# bfs가 끝날때마다 카운트
# 모든 맵을 탐색했을 때 카운트 값 정답값으로 출력

### 시간 복잡도 계산
# A. O(N)

from collections import deque 

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        q = queue.popleft()
        
        x = q[0]
        y = q[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if N > nx >= 0 and M > ny >= 0 and graph[nx][ny] != 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                


### 입력
N, M = map(int, input().split(" "))
graph = []

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input_str = ["00000111100000", "11111101111110", "11011101101110", "11011101100000", "110111111111111", "110111111111100", "11000000011111", "01111111111111","00000000111111","01111111111000","00011111111000","00000001111000","11111111110011","11100011111111","11100011111111"]
# 얼음 틀
for string in input_str:
    graph.append(list(map(int,string)))


# python 컨프리헨션, [False] * N 도 가능하나 2중배열 만들때는 사용하면 안된다.
visited = [[False for i in range(M)] for i in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        # 얼음틀이 0 이고, 방문한적이 없을 경우 dfs 실행
        if not graph[i][j] and not visited[i][j]:
            bfs(i,j)
            cnt += 1

print(cnt)

