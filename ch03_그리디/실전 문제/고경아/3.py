''' [문자열 뒤집기] '''
import sys

input = sys.stdin.readline

s_list = list(map(int, input().strip()))

# 덩어리가 큰 것부터 뒤집을까? - X 0001100은 11을 뒤집어야 함.
# 덩어리가 작은 것부터 뒤집을까? - X 010110은 1과 11을 뒤집어야 함.
# 0을 뒤집기, 1을 뒤집기 각각 비교해서 작은 값 출력할까?!

result = 0
temp = 0
for s in s_list:
    if temp == s:
        continue
    else:
        temp ==

# 0을 뒤집는 경우.
# 리스트를 돌면서
# 0이면 무시한다
# 1이면 result += 1
    # 0이 나오는 인덱스까지 이동

### 접근은 맞지만 횟수 세는 방식은 다시 고려해봐야 함!