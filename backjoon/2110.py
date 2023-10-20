# 1:24~
# 공유기 설치
# 도현이네 집 N개가 수직선 위에 있음
# 여러개가 같은 좌표를 가지는 일이 없음
# 공유기 C개 설치
# 최대한 많은 곳에서 와이파이를 사용하려고 할때 한집에는 공유기 하나만 설치 가능
# 인접한 두 공유기 사이의 거리를 가능한 크게 설치

# C개의 공유기를 N개의 집에 적당히 설치해서 가장 인접한 두 공유기 사이의 거리를 최대로

# 첫째 줄에 집의 개수, 공유기의 개수
# N개의 줄에는 집의 좌표
import random

import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()
# binary_search()
start = 1
end = array[-1]
result = 1
while True:
    if start > end:
        break 

    mid = (start + end) // 2 #두 공유기 사이의 최대값
    cnt = 1
    before = array[0]
    house = [array[0]]
    for i in range(1, len(array)):
        if array[i] - before >= mid:

            cnt += 1 
            before = array[i]

    if cnt == C:
        result = mid
        start = mid+1
    # 공유기의 개수가 많을 경우 -> 최대값이 작은경우
    elif cnt > C:
        result = mid
        start = mid+1
    # 공유기의 개수가 적은 경우 -> 최대값이 큰 경우
    else:
        # result = mid
        end = mid-1

print(result)



        