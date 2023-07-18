# 문자열 뒤집기
S = list(map(int, input()))
cnt = [0, 0]
for i in range(1, len(S)):
    if(S[i-1] != S[i]):
        cnt[S[i-1]] += 1
cnt[S[i]] += 1
print(min(cnt))