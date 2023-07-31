# # 
## 8-3 바닥 공사

## Solution

### 문제의 아이디어 생각해낸 포인트
# i-1의 타일에서 붙일 수 있는 경우의 수 -> 1개
# i-2의 타일에서 붙일 수 있는 경우의 수 -> 2개 

### 시간 복잡도 계산
# A.  

N = int(input())

memo = 1001 * [0]

memo[1] = 1
memo[2] = 3

for i in range(3, N+1):
    memo[i] = memo[i-1] + (2 * memo[i-2])

result = memo[N]%1007
print(result)

    
    