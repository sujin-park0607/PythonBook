### 감시 피하기
import sys
from itertools import combinations

input = sys.stdin.readline

# n * n 크기의 복도
n = int(input().strip())

# 복도의 정보. 학생 S, 선생님 T, 공백 X, 장애물 O
aisle_list = []
for _ in range (n):
    aisle_list.append(input().split())

s_list = []
t_list = []
x_list = []
for i in range (n):
    for j in range (n):
        if aisle_list[i][j] == "S":
            # s_list.append([i + 1, j + 1]) - 이게 더 직관적이라고 생각했는데, 계속 생각해야 해서 번거로움
            s_list.append([i, j])
        elif aisle_list[i][j] == "T":
            t_list.append([i, j])
        elif aisle_list[i][j] == "X":
            x_list.append([i, j])

"""
### 장애물을 따로 저장하지 않고 공백만을 이용해보려 했으나 일단 보류

# 조합을 이용해 모든 경우를 확인한다. 각 경우별로 장애물에 막힐 때까지 상하좌우를 확인한다. - ???
block_comb = list(combinations(x_list, 3)) # 장애물 모든 경우의 수

blocked_x_list = [] # 장애물 설치한 후의 공백 위치
for x in x_list:
    for bc in block_comb: # 각 장애물 경우의 수 확인
        if x not in bc:
            blocked_x_list.append(x)
"""

# 감시 (학생 발견 True, 미발견 False)
def watch(x, y, direction):
    if direction == 0: # 왼쪽
        while y >= 0:
            if aisle_list[x][y] == "S":
                return True
            if aisle_list[x][y] == "O":
                return False
            y -= 1
    if direction == 1: # 오른쪽
        while y < n:
            if aisle_list[x][y] == "S":
                return True
            if aisle_list[x][y] == "O":
                return False
            y += 1
    if direction == 2: # 위쪽
        while x >= 0:
            if aisle_list[x][y] == "S":
                return True
            if aisle_list[x][y] == "O":
                return False
            x -= 1
    if direction == 3: # 아래쪽
        while x < n:
            if aisle_list[x][y] == "S":
                return True
            if aisle_list[x][y] == "O":
                return False
            x += 1
    return False

# 장애물 설치 후 학생 검사
def process():
    for x, y in t_list:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False # for문이 시작되고 끝나는 지점을 이해하기 어려움

find = False

for data in combinations(x_list, 3):
    # 장애물 설치
    for x, y in data:
        aisle_list[x][y] = "O"
    if not process():
        find = True
        break
    for x, y in data:
        aisle_list[x][y] = "X" # 장애물 초기화

if find:
    print("YES")
else:
    print("NO")

"""
입력값
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
"""