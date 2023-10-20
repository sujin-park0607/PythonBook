
# # 
## 8-4 병사 배치하기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 가장 긴 증가하는 부분 수열 적용

### 소요시간
# 11:11 ~ 12:38

import sys
input = sys.stdin.readline

# n = 7
# array = [15, 11, 4, 8, 5, 2, 4]
n = int(input())
array = list(map(int, input().split(" ")))

# 가장 큰 증가하는 부분 수열을 구하기 위해서 배열 뒤집기
array = [0] + array[::-1]
count = [0] * (n+1)

for i in range(1, n+1):
    mx = 0
    for j in range(0, i):
        if array[i] > array[j]:
            mx = max(mx, count[j])
    count[i] = mx + 1

# 전체 숫자 - 가장 큰 증가값 = 열외할 사람 수
print(n - max(count))
