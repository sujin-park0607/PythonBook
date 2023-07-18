# 모험가 길드
N = int(input())
guild = list(map(int, input().split(" ")))

guild.sort()

idx = 1
cnt = 0

for x in guild:
    if(x == idx):
        cnt += 1
        idx = 1
    else: idx += 1
    

print(cnt)