
# # 
## 8-5 못생긴 수

## Solution

### 문제의 아이디어 생각해낸 포인트
# q에 담아 2,3,5를 곱한 모든 값을 set에 담는다 (중복을 제거하기 위함)
# sorted함수로 정렬한다

### 소요시간
# 12:45 ~ 1:26
from collections import deque

n = int(input())
numbers = set()
numbers.add(1)
q = deque([])
q.append(1)

while q:
    num = q.popleft()
    multi_2 = num * 2
    multi_3 = num * 3
    multi_5 = num * 5

    if multi_2 <= 1000:
        numbers.add(multi_2)
        q.append(multi_2)
    if multi_3 <= 1000:
        numbers.add(multi_3)
        q.append(multi_3)
    if multi_5 <= 1000:
        numbers.add(multi_5)
        q.append(multi_5)
        
numbers = sorted(numbers)
print(numbers[n-1])
    
    