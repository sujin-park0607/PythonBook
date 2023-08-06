# # 
## 모험가 길드

## Solution

### 문제의 아이디어 생각해낸 포인트
# 그리디, 오름차순 정렬
# 공포도가 작은 수끼리 묶여야 적게도 그룹이 생성 가능하므로 많은 그룹 생성 가능 

### 시간 복잡도 계산
# O(NlogN)

### 입력
import sys
import random
import math
import time
input = sys.stdin.readline


def solution(array):
    array.sort()
    # 그룹의 인원수와 공포도가 맞아 떨어지면 그룹 수 증가
    # 1/1 2/1 2 
    # 1 2 2 2 3

    cnt = 1
    group = 0
    for i in array:
        if cnt == i:
            group += 1
            cnt = 1
        else: cnt += 1
    return group


n = int(input())
array = list(map(int, input().split(" ")))
print(solution(array))


# 시간초과 확인 방법
# time 라이브러리
# start = time.time()

# #logic
# array = []
# # random 라이브러리
# for i in range(100000):
#     array.append(random.randrange(1,100000))
# solution(array)

# end = time.time()
# print(f"{end - start:.5f} sec")
# print(round(end-start,5))

