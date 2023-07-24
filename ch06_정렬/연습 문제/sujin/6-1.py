# # 
## 6-1 위에서 아래로

## Solution

### 문제의 아이디어 생각해낸 포인트
# 퀵 정렬 사용

### 시간 복잡도 계산
# A. 평균: O(NlogN), 최악: O(N^)

from collections import deque

def quick(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_sort = [x for x in tail if x >= pivot]
    right_sort = [x for x in tail if x < pivot]
    
    return quick(left_sort) + [pivot] + quick(right_sort)


N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

print(quick(array))




