# 조합을 계산할 땐 파이썬 조합 라이브러리 혹은 DFS ,BFS 이용할 수 있다.

# 아이디어 
## 1. 비어있는 공간 중 3개를 골라 벽을 설치
## 2. 벽을 설치할 때마다, 각 바이러스가 사방으로 퍼지는 것을 DFS/BFS로 제한

n , m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

# 순회 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

def virus (x,y) :
    for i in range(4) : 
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                virus(nx , ny)

# 현재 맵에서 안전 영역의 크기 계산하는 함수 

def get_score() :
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0 :
                score += 1
    return score

# DFS를 이용해서 울타리 설치하면서 안전 영역 크기 계산 
def dfs(count) : 
    global result
    if count == 3 :
        for i in range(n) :
            for j in range(m) :
                temp[i][j] = map[i][j]
        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 2 : 
                    virus(i,j)
        result = max(result, get_score())
        return 
    
    for i in range(n) :
      for j in range(m) :
          if map[i][j]==0 : 
              map[i][j] = 1
              count += 1
              dfs(count)
              map[i][j] = 0
              count -= 1

dfs(0)
print(result)

