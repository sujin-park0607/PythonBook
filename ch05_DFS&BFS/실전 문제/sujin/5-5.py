# # 
## 5-5 연산자 끼워넣기

## Solution

### 문제의 아이디어 생각해낸 포인트
# dfs로 4가지 연산자를 다 해보면서 최대값과 최소값 구하기

### 시간 복잡도 계산
# A. 

### 소요시간
# 10:32~
import sys
import copy
input = sys.stdin.readline

def dfs(operate, number_idx, result):
    global max_number, min_number

    if number_idx == n:
        # print("-------")
        # print(result)
        # print("=======")
        if result > max_number:
            max_number = result
        if result < min_number:
            min_number = result
        
        # if
        return
    # 덧셈
    if operate[0]:
        next_operate = copy.deepcopy(operate)
        next_operate[0] -= 1
        # print( " + ", numbers[number_idx])
        result += numbers[number_idx]
        dfs( next_operate, number_idx+1, result)
        result -= numbers[number_idx]
    
    # 뺄셈
    if operate[1]:
        next_operate = copy.deepcopy(operate)
        next_operate[1] -= 1
        # print(" - ", numbers[number_idx])
        result -= numbers[number_idx]
        dfs( next_operate, number_idx+1, result)
        result += numbers[number_idx]

    # 곱셈
    if operate[2]:
        next_operate = copy.deepcopy(operate)
        next_operate[2] -= 1
        # print(" * ", numbers[number_idx])
        result *= numbers[number_idx]
        dfs( next_operate, number_idx+1, result)
        result /= numbers[number_idx]

    # 나눗셈
    if operate[3]:
        next_operate = copy.deepcopy(operate)
        next_operate[3] -= 1
        # print("result", result)
        if result < 0:
            result = (abs(result) // numbers[number_idx]) * -1
        
        # print(" / ", numbers[number_idx])
        else: result //= numbers[number_idx]
        dfs( next_operate, number_idx+1, int(result))
        result *= numbers[number_idx]

    
n = int(input())
numbers = list(map(int, input().split(" ")))
operate = list(map(int, input().split(" ")))

global max_number, min_number

max_number = -1e9
min_number = 1e9
dfs(operate, 1, numbers[0])


print(int(max_number))
print(int(min_number))