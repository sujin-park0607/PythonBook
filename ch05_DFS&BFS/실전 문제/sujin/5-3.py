# # 
## 5-2 연구소

## Solution

### 문제의 아이디어 생각해낸 포인트
# 1번째 풀이
# k번까지의 2차원 리스트를 만들어서 바이러스의 좌표 넣기
# 상하좌우로 돌면서 추가된 좌표 2차원 리스트에 넣기
# s초동안 돌리기
# ->시간초과

# 그냥 q에 넣고 처음만 정렬해준다면 바이러스의 우선순위가 지켜질 수 있지 않을까?

### 시간 복잡도 계산
# A. 

### 소요시간
# 1:40  ~  3:32
import sys

input = sys.stdin.readline

def bfs():
    
    q = []

    # graph에 값이 존재하다면 배열에 넣기
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                q.append((graph[i][j], i, j))
    # 바이러스가 작은순서대로 정렬
    q = sorted(q, key = lambda x:x[0])

    # 1초라는 기준이 될 배열의 길이
    # 예를 들어 처음에는 1,2,3이 있는 (0,0), (0,2), (2,0)
    # 이렇게 세개를 다 탐색해야 1초가 지난것!
    length = len(q)

    # 시간 변수
    second = 0

    # 몇개의 좌표를 탐색하고 있는지 확인하는 변수
    cnt = 0


    while q:
        # 바이러스 번호, 좌표 순으로
        # 배열로 큐를 구현할 경우는 pop(0) 해주면 된다
        virus, x, y = q.pop(0)

        #상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 바이러스가 안퍼졌다면
                if graph[nx][ny] == 0:
                    # 바이러스 퍼트리기
                    graph[nx][ny] = virus
                    q.append((virus,nx,ny))
        
        cnt += 1
        
        # 1초 기준인 모든곳을 탐색했다면 1초 더하기
        if length == cnt:
            second += 1
            cnt = 0
            # 새로운 기준으로 초 설정해주기
            length = len(q)
        # 정해진 시간되면 탈출
        if second == s:
            break

# 입력
n, k = map(int, input().split(" "))
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split(" "))))
s, x, y = map(int, input().split(" "))


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# s가 0일 경우 예외처리
if s:
    bfs()
print(graph[x-1][y-1])

