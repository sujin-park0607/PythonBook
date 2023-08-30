# # 
## 8-2 정수삼각형

## Solution

### 문제의 아이디어 생각해낸 포인트
# 금광과 비슷한 문제라고 판단
# 1. 주어진 삼각형의 크기에 맞춰 0으로 채워진 2차원 배열 만들기
# 2. 2중반복문으로 돌면서 윗줄의 왼쪽 윗줄의 값중 큰 값 더하기
# array[i][j] = max(array[i-1][j], array[i-1][j-1]) + array[i][j]

### 소요시간
# 19:40~ 19:56

import sys
sys = sys.stdin.readline

n = int(input())
array = []
# 삼각형 입력받기
for _ in range(n):
    numbers = list(map(int, input().split(" ")))
    # 채워야하는 0의 수 = 주어진 삼각형 수 - 입력받은 배열 길이
    zero_num = n - len(numbers)
    # 그만큼의 0을 채우기
    array.append(numbers + [0 for _ in range(zero_num)])

# 2중반복문 
for i in range(1, len(array)):
    for j in range(len(array[i])):
        # 인덱스가 0보다 작아지면 바로 값 더하기
        if j < 0:
            array[i][j] += array[i-1][j]
        # 나머지는 구한 점화식으로 풀기
        else:
            array[i][j] += max(array[i-1][j], array[i-1][j-1])

# 바닥 중 가장 큰값이 최댓값
print(max(array[n-1]))