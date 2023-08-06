# # 
## 11-2 곱하기 혹은 더하기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 더하기가 필요한 경우 -> 0,1
# 나머지는 곱하기를 해야 최댓값 가능

### 시간 복잡도 계산

### 입력
import sys
input = sys.stdin.readline().rstrip

array = list(map(int, input()))
# 초기값 array[0] 으로 설정
num = array[0]

for i in range(1,len(array)):
    # 만약 계산할 두 숫자가 0,1 중에 있을 때는 더하기 연산
    if num in [0,1] or array[i] in [0,1]:
        num += array[i]
    # 나머지는 곱하기 연산
    else: num *= array[i]

print(num)
