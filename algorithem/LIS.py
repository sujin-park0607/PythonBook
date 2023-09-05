# 가장 긴 증가 부분 수열

n = 6
array = [10, 20, 10, 30, 20, 50]
array = [0] + array
dp = [0] * (n+1)
for i in range(1, n+1):
    mx = 0
    for j in range(0, i):
        if array[i] > array[j]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1

# print(max(dp))

# 가장 큰 증가 부분 수열

n = 6
array = [10, 20, 10, 30, 20, 50]
array = [0] + array
dp = array[:]
for i in range(1, n+1):
    mx = 0
    for j in range(0, i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])

# print(dp)

