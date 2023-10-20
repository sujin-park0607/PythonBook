# 아기상어 4: 25~ 

# N * N 공간에 물고기 M마리 아기상어 1마리
# 처음 아기상어 크기 2
# 아기상어는 1초에 상하좌우로 이동
# - 자신보다 큰 물고기가 있는 칸 지날 수 없음
# - 자신의 크기보다 작은 물고기만 먹을 수 있음 
#     - 크기 작으면 먹을 수 있음

# 아기상어 이동 결정 방법
# - 더이상 먹을 수 있는 물고기가 없다면 엄마상어에게 동무 요청
# - 먹을 수 있는 물고기 1마리 -> 그 물고기 먹으러감
# - 먹을수있는 물고기가 1마리보다 많다면, 가장 가까운 물고기 먹으러감
# - 거리는 -> 칸으로 이동할때 지나야하는 칸의 개수의 최솟값
# - 상, 좌 먼저
# - 아기상어는 자신의 크기와 같은 수의 물고기를 먹을때마 ㅏ크기가 1 증가
# - 크기가 2인 아기상어는 물고기 2마리를 먹으면 크기 3
# - 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 쳐먹을수있는가?

# 공간의 크기 N 
# N의 공간상태 
# 0 :빈칸/ 1~6 물고기 크기/ 9 아기상어 위치
import sys
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline

def findFish(start):
    
    time = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    minNum = INF
    q = deque([])
    q.append(start)
    visited[start[0]][start[1]] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if array[nx][ny] > sharkSize or visited[nx][ny]:
                continue 

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            if 0 <  array[nx][ny] < sharkSize:
                if minNum > visited[nx][ny]:
                    minNum = visited[nx][ny]
                    
                    
    # print("---------visited")
    # for i in visited:
    #     print(i)
    # print("minNum", minNum)

    guid = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == minNum and array[i][j] > 0:
                guid.append((i,j))
    guid.sort(key = lambda x:(x[0],x[1]))
    print("guid",guid)
    if not guid:
        return -1, -1, -1
                
    return minNum-1, guid[0][0], guid[0][1]
        
    
def eatFish(x, y):
    global eatFishNum, sharkSize, sharkLocation
    finishNum[array[x][y]] -= 1

    eatFishNum += 1 
    if eatFishNum == sharkSize:
        sharkSize += 1
        eatFishNum = 0

    array[sharkLocation[0]][sharkLocation[1]] = 0
    array[x][y] = 9
    sharkLocation = (x,y)


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
finishNum = [0 for _ in range(7)]
sharkSize = 2
sharkLocation = None
eatFishNum = 0
totalTime = 0
# 상어 위치와 물고기 수 초기설정
for i in range(N):
    for j in range(N):
        if array[i][j] == 9:
            sharkLocation = (i,j)
        elif array[i][j] > 0:
            finishNum[array[i][j]] += 1
        
while True:
    # 종료조건
    # isFinish = True 
    # for i in finishNum[:sharkSize+1]:
    #     if i > 0:
    #         isFinish = False
    # if isFinish:
    #     break
# print("sharkLocation",sharkLocation)
    time, x, y = findFish(sharkLocation)
    print("time, x, y//", time,":", x, y,"sharkSize",sharkSize)
    
    if x == -1 and y == -1:
        break
    totalTime += time
    print("totalTime",totalTime)
    eatFish(x, y)
    print("--------array")
    for i in array:
        print(i)
print(totalTime)

# print("finishNum",finishNum)

        
