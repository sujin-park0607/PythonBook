#1이 될때까지
N, K = map(int, input().split(" "))
cnt = 0

while(N >= K):
    if not (N % K):
        N = int(N / K)
    else:
        N -= 1
    cnt += 1

if (N != 1):
    cnt += N - 1

print(cnt)
