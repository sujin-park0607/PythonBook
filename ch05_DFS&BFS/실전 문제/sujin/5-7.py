# # 
## 5-7 블록 이동하기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 
### 시간 복잡도 계산
# A. 

### 소요시간
# 20:05 ~ 

def make_wall(cnt):
    global result
    if cnt == 3:
        print(dfs())
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] =='X':
                graph[i][j] =='O'
                make_wall(cnt + 1)
                graph[i][j] =='X'

def dfs():
    global teachers

    for t in teachers:
        tx, ty = t
        for i in range(4):
            if not check_wall(tx,ty, dx[i], dy[i]):
                return False
    return True



def check_wall(tx, ty, dx, dy):
    nx, ny = tx, ty
    while(True):
        if (tx < 0 or tx <= n) or (ty < 0 or ty <= n):
            break
        if graph[nx][ny] == 'O':
            break
        if graph[nx][ny] == 'S':
            return False
        nx += dx
        ny += dy
    return True

            
global teachers             
n = int(input())
graph = []
teachers = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    graph.append(input().split(" "))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i,j))
    
make_wall(0)
    

