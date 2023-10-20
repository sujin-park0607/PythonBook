
# # 
## 8-5 편집 거리

## Solution

### 문제의 아이디어 생각해낸 포인트
# 

### 소요시간
# 답지
import sys
# input = sys.stdin.readline().rstrip

a_array = list(sys.stdin.readline().rstrip())
b_array = list(sys.stdin.readline().rstrip())

a_len = len(a_array)
b_len = len(b_array)

dp = [[i] + [0 for i in range(a_len)] for i in range(1, b_len+1)]
dp = [[i for i in range(a_len+1)]] + dp[:]

for i in range(1, b_len+1):
    for j in range(1, a_len+1):
        if a_array[j-1] == b_array[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

print(dp[b_len][a_len])