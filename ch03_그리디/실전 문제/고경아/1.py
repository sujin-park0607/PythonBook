'''
[모험가 길드]
'''
import sys

input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())), reverse=True)

result = 0
index = 0
# 반복 횟수가 정확하지 않으므로 for문이 아닌 while문을 사용
while index < n: # 인덱스가 리스트를 벗어나지 않을 동안, 즉 떠날 모험가가 남아있는 동안 반복.
    if n_list[index] <= (n + 1): # 만약 현재 인덱스의 값만큼 참여자를 모집할 수 있다면 모집.
        result += 1 # 한 팀 모집
        index += (n_list[index]) # 모집된 수만큼 인덱스 넘기기
    else: index += 1 # 현재 인덱스의 값만큼 참여자를 모집할 수 없다면 인덱스 넘기기. *** 이 부분 까먹어서 무한 반복 발생
