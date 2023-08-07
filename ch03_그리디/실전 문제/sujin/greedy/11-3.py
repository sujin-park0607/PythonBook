# # 
## 11-3 문자열 뒤집기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 0,1중에 작은 그룹의 개수만큼 뒤집으면 된다.
# 그룹을 구한 후 작은 최소그룹 반환

### 시간 복잡도 계산
# O(n)

### 입력
import sys
input = sys.stdin.readline().rstrip

array = list(map(int, (input())))
cnt = [0, 0]

cnt[array[0]] += 1
for i in range(1,len(array)):
    if array[i] != array[i-1]:
        cnt[array[i]] += 1
result = min(cnt[0], cnt[1])
print(result)
    