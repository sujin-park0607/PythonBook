
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


# dp로 푼 못생긴 수

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0

next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])
    
    