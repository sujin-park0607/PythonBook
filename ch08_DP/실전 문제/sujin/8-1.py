# # 
## 8-1 금광

## Solution

### 문제의 아이디어 생각해낸 포인트
# 점화식
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1], dp[j-1])


### 소요시간
# 19:15 ~ 

import sys

for tc in range(int(input)):
    n, m = map(int, input().split(" "))
    array = list(map(int, input().split()))


    dp = []
    idx = 0

    for i in range(n):
        dp.append(array[idx:idx+m])
        idx += m

        for j in range(1, m):
            for i in range(n):
                # 왼쪽 위
                if i==0:
                    left_up = 0
                else:
                    left_up = dp[i-1][j-1]
                
                #왼쪽 아래
                if i==n-1:
                    left_down = 0
                else:
                    left_down = dp[i+1][j-1]
                #왼쪽에서 오는 경우
                left = dp[i][j-1]
                dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
    result = max(result, dp[i][m-1])

print(result)