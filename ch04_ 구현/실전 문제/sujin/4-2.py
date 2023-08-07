# # 
## 4-2 문자열 재정렬

## Solution

### 문제의 아이디어 생각해낸 포인트
# 문자열 아스키코드로 변환 후 string 배열에 삽입
# 숫자는 변수에 더하기
# string배열 오름차순

### 시간 복잡도 계산
# A. 평균: O(N)

### 소요시간
# 20M

import sys
input = sys.stdin.readline().rstrip

array = list(input())
number = 0
string = []

for s in array:
    # 모든 문자 아스키코드로 변환
    num = ord(s)
    # 문자인 경우는 문자열 리스트에 더하기
    if 65 <= num <= 90:
        string.append(s)
    # 아닌 경우는 숫자로 변환하여 더하기
    else:
        number += int(s)

# 문자열 오름차순
string.sort()
#출력
for s in string:
    print(s,end='')
print(number)
        
        
        




