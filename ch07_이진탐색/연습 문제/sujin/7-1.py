# # 
## 7-1 부품 찾기

## Solution

### 문제의 아이디어 생각해낸 포인트
# N의 범위가 백만개이기 때문에 순차탐색, 이진탐색 모두 가능
# 정렬 후, 이진탐색으로 구현

### 시간 복잡도 계산
# A. O(logN) 

def binary_search(array, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
        

N = int(input())
n_array = sorted(list(map(int, input().split(" "))))

M = int(input())
m_array = list(map(int, input().split(" ")))

for m in m_array:
    if binary_search(n_array, m, 0, len(n_array)-1):
        print("yes", end=' ')
    else: print("no", end=' ')
        

