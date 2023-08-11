# # 
## 4-5 뱀 

## Solution

### 문제의 아이디어 생각해낸 포인트
# 
### 시간 복잡도 계산
# A. 

### 소요시간
# 1:50 ~ 3:30 

# n * n
# 몇몇칸에는 사과
# 뱀의 길이는 1, 처음에는 오른쪽을 향함
# 규칙
# 1. 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다
# 2. 만약 벽이나 자기자신과 몸과 부딪히면 게임이 끝난다
# 3. 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않느다
# 4. 만약 이동한 칸에 사과가 없다면, 몸 길이를 주여서 꼬리가 위치한 칸을 비워준다

# 사과의 위치와 뱀의 이동경로가 주어질때 -> 게임이 끝나는 시간 계산


from collections import deque
n = int(input())
k = int(input())

array = [[0 for i in range(n)]for i in range(n)]
# 사과넣기
for _ in range(k):
    x, y = map(int, input().split(" "))
    array[x-1][y-1] += 1

l = int(input())
direction = []
# 방향 배열 받기
for _ in range(l):
    direction.append(input().split(" "))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
i = 0
cnt = 0
snake = deque()
snake.append((0,0))
while True:
    # print("cnt============",cnt)
    # print(snake)
    # 방향전환
    if direction:
        if int(direction[0][0]) == cnt:
            # print("directions control")
            if direction[0][1] == 'D':
                i += 1
                if i>3: i=0
            else:
                i -= 1
                if i<0: i=3
            direction.pop(0)

    nx = x + dx[i]
    ny = y + dy[i]

    # print("nx, ny:",nx, ny)

    if n <= nx or nx < 0 or n <= ny or ny < 0 or (nx,ny) in snake:
        # print("finish",nx,ny)
        # print("snake",snake)
        # print(cnt)
        break
    # 사과인경우
    if array[nx][ny] == 1:
        # 사과 먹은걸 치우는걸 깜박해서 중간에 에러남
        array[nx][ny] = 0
        snake.append((nx,ny))
    #사과가 아닌 경우
    else:
        snake.append((nx,ny))
        snake.popleft()
    x = nx
    y = ny
    cnt += 1
    
print(cnt+1)


