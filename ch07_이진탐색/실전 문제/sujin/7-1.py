# # 
## 7-1 정렬된 배열에서 특정 수의 개수 구하기

## Solution

### 문제의 아이디어 생각해낸 포인트
# binary_search로 찾는 숫자의 인덱스 구하기
# 구해진 인덱스 기준으로 좌, 우 숫자가 같으면 count를 다르면 반복문 종료
# 
### 소요시간
# 10:26 ~ 10:49

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binary_search(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
# n, x = map(int, input().split(" "))
# numbers = list(map(int, input().split(" ")))

n,x = 7, 2
# n,x = 7, 4
numbers =  [1, 1, 2, 2, 2, 2, 3]
cnt = 0
idx = binary_search(numbers, x, 0, n-1)

for i in range(idx, 0, -1):
    if numbers[i] != x:
        break
    cnt += 1

for i in range(idx+1, n):
    if numbers[i] != x:
        break
    cnt += 1

print(cnt)


