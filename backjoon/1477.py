# 2:51~ 4:22
# 유료 고속도로 
# 휴게소 N개 
# 휴게소의 위치는 고속도로 시작으로부터 얼만큼 떨어져있는지 주어짐
# 추가로 M개의 휴게소 세우려고함
# 휴게서 이미 존재하는 곳 x, 고속도로 끝 x 
# 휴게소가 없는 구간의 길이의 최댓값을 -> 최소로하려고함
# 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로 길이 L
#   
import sys
# import random
input = sys.stdin.readline

N, M, L = list(map(int, input().split()))
input_array = list(map(int, input().split()))
input_array.sort()

# N, M, L = 50, 100, 151
# input_array = []
# for i in range(N):
#     input_array.append(random.randrange(1,L-1))
# input_array.sort()
input_array = [0] + input_array[:] + [L]

array = []
for i in range(1, len(input_array)):
    array.append(input_array[i] - input_array[i-1])

start = 1
end = L
result = 0
while True:
    if start > end:
        break 
    mid = (start + end) // 2
    cnt = 0
    for i in array:
        cnt += i // mid
        if i % mid == 0:
            cnt -= 1
    # print("최대거리값", mid, "cnt", cnt)
    
    if cnt > M: #휴게소가 더 많아졌을때 -> 최대값을 늘림 
        start = mid + 1
    else: # 휴게소가 더 적거나 같을 때 -> 최대값을 줄임
        result = mid
        end = mid - 1
print(result)