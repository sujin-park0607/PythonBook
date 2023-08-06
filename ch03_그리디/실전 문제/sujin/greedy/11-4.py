# # 
## 11-4 만들 수 없는 금액

## Solution

### 문제의 아이디어 생각해낸 포인트
# 

### 시간 복잡도 계산
# 

### 입력
import sys
import random
# input = sys.stdin.readline().rstrip

n = int(sys.stdin.readline().rstrip())
coins = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# n = 1000
# coins = []
# for i in range(1000):
#     coins.append(random.randrange(1,1000000))
# print(coins)
# idx = 0
for i in range(1, 1000):
    num = i
    for coin in coins:
        # idx += 1

        if num >= coin:
            num -= coin
            if num == 0: break
        
    if num:
        print(i)
        break

# print("idx:====",idx)
