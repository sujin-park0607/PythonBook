# # 
## 6-2 안테나

## Solution

### 문제의 아이디어 생각해낸 포인트
# 위치중 가운데 접은 곳(첫번째 + 끝)의 중간이 가장 적합한 곳이라고 판단
# 중간과 가장 가까운 집에 안테나 설치
### 시간 복잡도 계산
# A. 

### 소요시간
# 2:40 ~ 
import sys
input = sys.stdin.readline

n = int(input())
home = sorted(list(map(int, input().split(" "))))
mid = (home[0] + home[-1]) // 2

result = 1e9
minNum = 1e9
for h in home:
    if  minNum > abs(h - mid):
        minNum = abs(h - mid)
        result = h
print(result)
    


