# # 
## 6-4 카드 정렬하기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 1. 정렬 후 제일 작은 것 두개를 묶고 계속 더하기할려고 함
# 틀림
# 최소힙을 사용
# 
### 소요시간
# 19:20 ~ 20:00

import sys
import heapq

input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    heapq.heappush(numbers, int(input()))

numbers = sorted(numbers)
result = 0
# n이 1인경우는 비교 없음
if n == 1:
    result = 0
# n의 값이 2 이하일 때
elif n == 2:
    result = sum(numbers)
# n의 값이 3이상일 때
else:
    # heap의 값이 1개가 남았을때 종료
    while len(numbers) > 1:
        # 제일 작은것 두번째 작은것 꺼내서 더하기
        min_num1 = heapq.heappop(numbers)
        min_num2 = heapq.heappop(numbers) 
        # 더한값을 result 값에 더함
        result += (min_num1 + min_num2)
        # 더한값을 heap에 다시 넣기
        heapq.heappush(numbers, min_num1 + min_num2)

print(result)
         
    