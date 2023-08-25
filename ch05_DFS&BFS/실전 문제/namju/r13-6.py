
"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
"""

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(input().split()) for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
queue = deque()
check = False

def bfs():
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T': # T를 발견할 경우 Q에 넣기
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            temp_x, temp_y = x,y
            while True:
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n: # 그래프 내에서
                    if graph[nx][ny] == 'X' and visited[nx][ny] == False: # 1. 빈공간X 면서 방문한적이 없으면 = 학생을 찾지 못하면
                        visited[nx][ny] = True # T
                    elif graph[nx][ny] == 'S': # 2. 학생 발견하면
                        return False  # F
                    elif graph[nx][ny] == 'O': # 3. 벽 발견하면
                        break # 멈춤
                    temp_x, temp_y = nx,ny
                else:
                    break
    return True


# 벽 체크
def recursive(index):
    global check
    if index == 3:
        if bfs():
            check = True
        return

    # 그래프의 모든 X에 0(벽)을 3개 생성하여 확인하기
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X': # 빈공간이면
                graph[i][j] = 'O' # 벽생성
                recursive(index + 1) # 벽+=1
                graph[i][j] = 'X' # 다시 초기화

recursive(0)
if check:
    print("YES")
else:
    print("NO")