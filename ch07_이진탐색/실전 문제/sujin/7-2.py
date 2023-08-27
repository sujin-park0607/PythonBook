# # 
## 7-2 고정점 찾기 

## Solution

### 문제의 아이디어 생각해낸 포인트
# idx      0   1  2  3  4  5   6
# numbers -15 -4  2  8  9  13 15
#-----------------------------------
# idx-num 15   5  0 -1 -5 -8  -9
# 이렇게 idx - numbers를 해주면서 그 차이가 0인것을 이진탐색을 통해 찾도록 구현
### 소요시간
# 10:49 ~ 11:15

def binary_search(array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    diff_num = mid - array[mid]
    
    if diff_num == 0:
        return mid
    elif diff_num < 0:
        return binary_search(array, start, mid-1)
    else: 
        return binary_search(array, mid + 1, end)

# n = int(input())
# array = list(map(int, input().split(" ")))
# n = 5
# array = [-15, -6, 1, 3, 7]

# n = 7
# array = [-15, -4, 2, 8, 9, 13, 15]

n = 7
array = [-15, -4, 3, 8, 9, 13, 15]

print(binary_search(array, 0, n-1))
