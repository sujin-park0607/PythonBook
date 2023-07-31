# # 
## 8-4 효율적인 화폐 구성

## Solution

### 문제의 아이디어 생각해낸 포인트
# i-1의 타일에서 붙일 수 있는 경우의 수 -> 1개
# i-2의 타일에서 붙일 수 있는 경우의 수 -> 2개 

### 시간 복잡도 계산
# A.  
d = 10001 * [0]
n, x = map(int,input().split(" "))

for _ in range(n):
    idx = int(input())
    d[idx] = 1


d[0] = 1001
for i in range(1, x+1):
    if d[i] != 0:
        continue
    if i-3 >= 0:
        d[i] = min(d[i-2], d[i-3]) + 1
    else:
        d[i] = 1001

if d[x] > 1000:print(-1)
else: print(d[x])



