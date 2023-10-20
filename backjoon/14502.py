# 연구소 

# 연구소의 벽을 세우려고함 
# N * M 의 직사각형
# 빈칸, 벽 
# 일부칸에 바이러스 존재
# 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나감
# 세울 수 있는 벽의 개수 3개 
# 꼭 3개를 세워야함
# 0 빈칸, 1 벽, 2 바이러스

import sys
import copy
from collections import deque

input = sys.stdin.readline

def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations(array[:i], r-1):
                yield [array[i]] + next

def virous(ground):
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for x,y in virus_list:
        if not visited[x][y]:
            bfs(x,y,ground,visited)
    
    # print("ground-------------")
    # for i in ground:
    #     print(i)
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 0:
                cnt += 1
    # print("cnt", cnt)
    return cnt

def bfs(x,y,ground,visited):
    
    q = deque([])
    q.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] or ground[nx][ny] == 1:
                continue

            q.append((nx,ny))
            visited[nx][ny] = True
            ground[nx][ny] = 2
    
    


N, M = list(map(int, input().split()))
ground = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(N):
    ground.append(list(map(int, input().split())))

virus_list = []
# 빈칸, 바이러스칸 찾기
array = []
for i in range(N):
    for j in range(M):
        if ground[i][j] == 0:
            array.append((i,j))
        elif ground[i][j] == 2:
            virus_list.append((i,j))

# 벽세울 조합 구하기
permutationList = []
for i in permutations(array,3):
    permutationList.append(i)

maxSafeNum = -1 
for per in permutationList:
    new_ground = copy.deepcopy(ground)

    # 벽세우기
    for x,y in per:
        new_ground[x][y] = 1
    
    # print("new_ground----------")
    # for i in new_ground:
    #     print(i)
    safeNum = virous(new_ground)


    if maxSafeNum < safeNum:
        maxSafeNum = safeNum
        
print(maxSafeNum)