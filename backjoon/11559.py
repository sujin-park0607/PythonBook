# puyo puyo 4:30 ~
# 필드에 여러가지 색깔의 뿌요를 놓는다
# 뿌요는 중력의 영향을 받아 -> 바닥이나 다른뿌요 만날때까지 떨어짐
# 이때 1연쇄가 시작
# 같은 색의 뿌요들이 4개 이상 모이게 되면 터짐
# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야함 -> 연쇄는 한번 추가
# 상대방의 필드가 주어졌을때 연쇄가 몇 번 연속으로 일어날까?

# R 빨강/ G 초록/ B 파랑/ P 보라/ Y 노랑
# 입력 ->뿌요 아래에 빈 칸이 있는 경우는 없다


# 한턴 -> 그룹 찾기 
# 중력 작용
from collections import deque

array = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = 12 # 행
M = 6 # 열
for _ in range(N):
    array.append(list(input()))

def find_group():
    isPuyo = False
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if array[i][j] != '.' and not visited[i][j]:
                guid = bfs(i,j, visited)
                if len(guid) >= 4:
                    for x,y in guid:
                        array[x][y] = '.'
                    isPuyo = True
                

    return isPuyo


def bfs(x, y, visited):
    isPuyo = False
    guid = []
    q = deque([])
    q.append((x, y))
    guid.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny>= M:
                continue
            if visited[nx][ny]:
                continue
            if array[nx][ny] == array[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = True 
                guid.append((nx,ny))
    return guid

def down():
    global array
    new_array = []
    for i in range(M):
        new_col = []
        for j in range(N-1,-1,-1):
            
            if array[j][i] != '.':
                new_col.append(array[j][i])
        new_array.append(new_col + ['.' for _ in range(N - len(new_col))])

 
    array = []
    for i in range(N-1, -1, -1):
        new_row = []
        for j in range(M):
            new_row.append(new_array[j][i])
        array.append(new_row)
         
cnt = 0
while True:
    result = find_group()
    if result:
        cnt += 1
    else:
        break
    down()
print(cnt)

