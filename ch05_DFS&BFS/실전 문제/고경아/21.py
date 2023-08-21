### 인구 이동
import sys
from collections import deque

input = sys.stdin.readline

# N * N 크기의 땅, 인구 차이가 L명 이상 R명 이하라면 국경 개방
n, l, r = map(int, input().split())

area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 연합 체크
def process(x, y, idx):
    united = [] # (x, y)의 연합
    united.append((x, y))
    # BFS를 위한 큐
    q = deque()
    q.append((x, y))
    union[x][y] = idx # 에러가 안 나네? (Unresolved reference 'union')
    summary = area[x][y]
    cnt = 1
    # 큐가 빌 때까지 BFS
    while q:
        x, y = q.popleft()
        # 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[y]
            # 옆나라 확인
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(area[nx][ny] - area[x][y]) <= r:
                    q.append((nx, ny))
                    # 인구 차이가 L 이상 L 이하이면 연합에 추가
                    union[nx][ny] = idx
                    summary += area[nx][ny]
                    cnt += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구 분배
    for i, j in united:
        area[i][j] = summary // cnt

total_cnt = 0

# 인구 이동이 불가능할 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, idx)
                idx += 1
    if idx == n * n: # 인구 이동 완료
        break
    total_cnt += 1

# 인구 이동 횟수 출력
print(total_cnt)

"""
입력값
2 20 50
50 30
20 40
"""