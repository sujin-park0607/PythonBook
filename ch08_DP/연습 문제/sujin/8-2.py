# # 
## 8-1 1로 만들기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 문제를 작은 문제로 나누게된다면 2가지의 경우의 수가 생긴다
# d[i] + d[i+2]
# # d[i] + d[i+3] 

### 시간 복잡도 계산
# A.  
import sys

N = int(input())
array = list(map(int, input().split(" ")))
maxNum = 0
if N >= 3:
    array[2] += array[0]

if N == 3:
    maxNum = max(array)

for i in range(3, N):
    array[i] = max(array[i] + array[i-2], array[i] + array[i-3])
    if array[i] > maxNum:
        maxNum = array[i]

print(maxNum)
    
    