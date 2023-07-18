coins = [500, 100, 50, 10]
result = 0

N = int(input())
for coin in coins:
    result += int(N/coin)
    N %= coin

print(result)
# 시간복잡도 O(n)