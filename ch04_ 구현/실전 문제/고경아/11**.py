'''[뱀]'''
import sys

input = sys.stdin.readline

# 보드 크기와 사과 개수 초기화
board_size = int(input().rstrip())
apple_count = int(input().rstrip())

# 빈 보드 생성
board = [[0] * board_size for _ in range(board_size)]

# 보드에 사과 정보 표시
for _ in range(apple_count):
    row, column = map(int, input().split())
    board[row][column] = 1

# 뱀의 방향 변환 저장
rotate_count = int(input().rstrip())
rotate_plan = []
for _ in range(rotate_count):
    rotate_plan.append(list(input().split())) # [time ,direction(왼L, 오D)]

# 시뮬레이션 시작
# r_plan의 숫자가 될 때까지 오른쪽으로 이동.
time = 0
direction_list = ["R", "D", "L", "U"]
direction_index = 0
direction = direction_list[direction_index]
head = [1, 1]
while 1 <= head[0] and head[0] <= board_size and 1 <= head[1] and head[1] <= board_size:
    for i in range(rotate_count):
        for _ in range(int(rotate_plan[i][0]) - time, int(rotate_plan[i][0]) + 1):
            time += 1
            print(direction)
            if direction == "R":
                head[0] += 1
            elif direction == "D":
                head[1] += 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "U":
                head[1] -= 1
        if rotate_plan[i][1] == "L":
            if direction == "R":
                direction = "U"
            else:
                direction_index -= 1
                direction = direction_list[direction_index]
        elif rotate_plan[i][1] == "D":
            if direction == "U":
                direction = "R"
            else:
                direction_index += 1
                direction = direction_list[direction_index]

print(rotate_plan)
"""
입력값
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""