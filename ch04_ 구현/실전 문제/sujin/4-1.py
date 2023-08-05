# # 
## 4-1 럭키 스트레이트

## Solution

### 문제의 아이디어 생각해낸 포인트
# 문자열을 하나씩 배열에 넣기
# 배열의 길이의 반을 나눈 후 왼쪽, 오른쪽 반복문으로 더하기

### 시간 복잡도 계산
# A. 평균: O(N)

### 소요시간
# 10M


n = list(map(int, input()))
length = len(n) // 2
left_sum = 0
right_sum = 0

for l in n[:length]:
    left_sum += l

for r in n[length:]:
    right_sum += r    

if left_sum == right_sum: print("LUCKY")
else: print("READY")





