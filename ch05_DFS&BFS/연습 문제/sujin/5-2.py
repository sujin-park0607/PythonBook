# # 
## 5-2 미로 탈출

## Solution

### 문제의 아이디어 생각해낸 포인트
# 최단 경로이기 때문에 bfs로 탐색
# dfs는 한길만 파기때문에 최단경로 문제에서는 사용 불가
# 기존의 거리 +1을 통해서 마지막 N,M의 값을 반환 

### 시간 복잡도 계산
# A. O(N)

from collections import deque

def bfs(x,y):
    queue =  deque([(x,y)])
    miro[x][y] = 1

    while queue:
        q = queue.popleft()
        x = q[0]
        y = q[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if N > nx >=0 and M > ny >=0:
                if miro[nx][ny] == 1:
                    queue.append((nx,ny))
                    miro[nx][ny] = miro[x][y] +1
    return miro[N-1][M-1]

N, M = map(int, input().split(" "))

miro = []
for _ in range(N):
    miro.append(list(map(int, input())))

# print(miro)
# 하, 우, 좌, 상
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

print(bfs(0,0))

