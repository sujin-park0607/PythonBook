# # 
## 11-4 볼링공 고르기

## Solution

### 문제의 아이디어 생각해낸 포인트
# n개중 2개를 뽑아 모든 경우의 수를 리스트로 구함 -> 순열
# 그 중 무게가 같은것은 패쓰 다르면 cnt 올려주기

### 시간 복잡도 계산
# 

### 입력
import sys
import itertools

# input = sys.stdin.readline().rstrip

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
array = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# 순열
# n개중 r개를 뽑는 모든 경우의 수를 itertools형태로 반환
nCr = itertools.combinations(array,2)
# print(nCr)

#조합
# nPr = itertools.permutations(array,2)


cnt = 0
for i in list(nCr):
    # 두가지의 볼링공의 무게가 같은 경우는 패쓰
    if i[0] == i[1]:
        continue
    # 뽑힌 볼링공의 무게가 다른경우는 cnt 올려주기
    cnt += 1

print(cnt)