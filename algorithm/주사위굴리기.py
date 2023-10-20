
import sys 
from collections import deque

input = sys.stdin.readline


def runRoll():
    if direction in (0, 2):
        # 동
        if direction == 0:
            temp = roll[0].pop(-1)
            roll[0] = [temp] + roll[0]
            
        # 서
        elif direction == 2:
            temp = roll[0].pop(0)
            roll[0] = roll[0] + [temp]

        for i in 0,2:
            roll[1][i] = roll[0][i]
    else:
        # 남
        if direction == 3:
            temp = roll[1].pop(-1)
            roll[1] = [temp] + roll[1]
            
        # 북
        elif direction == 1:
            temp = roll[1].pop(0)
            roll[1] = roll[1] + [temp]

        for i in 0,2:
            roll[0][i] = roll[1][i]
        


# 방향 가능한지 확인
def confirm():
    global direction
    nx, ny = current[0] + dx[direction], current[1] + dy[direction] 
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        direction += 2

def updateDir():
    global direction
    if direction >= 4:
        direction -= 4
    elif direction < 0:
        direction += 4

def play():
    global current, score
    # 현재 위치 갱신
    current[0] += dx[direction]
    current[1] += dy[direction]
    
    # 주사위 갱신
    runRoll()
    
    # 점수 계산
    cnt = bfs(current[0], current[1])
    score += array[current[0]][current[1]] * cnt 

def bfs(x,y):
    visited = [[False for i in range(M)]for i in range(N)]
    cnt = 1
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    mid = array[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= N or 0 > ny or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if array[nx][ny] == mid:
                visited[nx][ny] = True 
                q.append((nx, ny))
                cnt += 1
    return cnt

def findDir():
    global direction
    # 주사위 밑변
    A = roll[0][2]
    B = array[current[0]][current[1]]

    if A > B:
        direction += 1
    elif A < B:
        direction -= 1
        
                

global direction, roll, current, score

N, M, K = list(map(int, input().split(" ")))
array = []
for _ in range(N):
    array.append(list(map(int, input().split(" "))))

roll = [[1, 3, 6, 4],
        [1, 2, 6, 5]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
current = [0, 0]
score = 0



# 게임 시작
for k in range(K):

    # 주사위 방향 가능한지 확인
    confirm()


    # 방향 갱신 
    updateDir()

    # 주사위 굴리기
    play()

    #이동방향 결정
    findDir()

    #방향 갱신
    updateDir()


print(score)

    

    