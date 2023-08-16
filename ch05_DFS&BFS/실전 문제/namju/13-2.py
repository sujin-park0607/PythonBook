
"""
연구소
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

# 3개 카운트
# 전체탐색하여 2를 기준으로 상하좌우 살피기 1-> 넘어가기 , 0일경우 +=1 k-=1,
## 3개가 한정되어 있기때문에 경우의 수가 생김. 0개 셌을때 갯수가 많으면 다시 탐색...
- 다시 초기화 시키고 count 한다 -> max값 찾아야함...

"""
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# k=3
#
# def count_zero(n, m):
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 cnt += 1
#     return cnt
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j]==2 and k>0:
#             for k in range(4):
#                 nx = i+dx[k]
#                 ny = j+dy[k]
#                 if nx>0 and ny>0 and nx<n and ny<m and graph[nx][ny]==0:
#                     graph[nx][ny]+=1
#                     k-=1
#         elif k==0:
#             count_zero(n, m)
# print()


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)] #벽을 설치한 뒤의 맵 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer=0

def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<n and ny >=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score +=1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global answer
    # 울타리가 3개 설치된 경우
    if count ==3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        answer = max(answer, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                count +=1
                dfs(count)
                graph[i][j]=0
                count -=1
dfs(0)
print(answer)

