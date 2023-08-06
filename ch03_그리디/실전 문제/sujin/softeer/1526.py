# 암기 서열 커버

# 완전탐색으로 풀기에는 4**20 의 조합을 확인해야함
#  자릿수마다 a,c,g,t의 갯수를 구하기
# 배열이 0 이아닌 경우의 갯수가 초 염기서열의 최소개수
import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
acgt = [[False] * 4 for _ in range(m)]

maxCnt = 0
for i in range(n):
    string = list(input())
    cnt = 0
    for idx in range(len(string)):
        if string[idx] == 'a':
            acgt[idx][0] = True
        elif string[idx] == 'c':
            acgt[idx][1] = True
        elif string[idx] == 'g':
            acgt[idx][2] = True
        elif string[idx] == 't':
            acgt[idx][3] = True
        else:
            continue


maxCnt = 0
for i in acgt:
    cnt = 0
    for j in i:
        if j:
            cnt += 1
    if cnt > maxCnt:
        maxCnt = cnt
print(maxCnt)