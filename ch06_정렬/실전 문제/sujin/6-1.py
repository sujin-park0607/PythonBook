# # 
## 6-1 국영수

## Solution

### 문제의 아이디어 생각해낸 포인트
# sorted와 lambda로 여러 조건을 주면 됨
### 시간 복잡도 계산
# A. 

### 소요시간
# 2:22 ~ 2:39
import sys

n = int(sys.stdin.readline().rstrip())
student = []
for _ in range(n):
    student.append(list(sys.stdin.readline().rstrip().split(" ")))

student = sorted(student, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in student:
    print(s[0])

