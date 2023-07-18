#큰 수의 법칙

N, M, K = map(int, input().split(" "))
number = list(map(int, input().split(" ")))

number = sorted(number, reverse=True)

cnt = 0
result = 0
for _ in range(M):
    if(cnt == K):
        result += number[1]
        cnt = 0
        continue

    result += number[0]
    cnt += 1
print(result)