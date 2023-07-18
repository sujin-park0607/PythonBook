# 곱하기 혹은 더하기
S = list(map(int, input()))
result = 0

num = S[0]
for i in range(1, len(S)):
    if(num == 0 or S[i] == 0 or S[i] == 1):
        num += S[i]
    else:
        num *= S[i]

print(num)
