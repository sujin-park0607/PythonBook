# # 
## 8-1 1로 만들기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 재귀로 3으로 나눌때, 2로 나눌때, -1 할때 모두 탐색
# 대신 중간에 cnt가 minCnt보다 커지게 될 경우 탐색 안하는 조건 설정

### 시간 복잡도 계산
# A.  
import sys
# sys.setrecursionlimit()

def calculate(x, cnt):
    global minCnt
    print("x,cnt : ",x, cnt)
    # 기존에 최소연산횟수를 안넘어갈 경우
    if cnt <= minCnt:

        # 종료 조건: 1이 될 때
        if x == 1:
            # print("cnt========",cnt, minCnt)
            # cnt 최솟값 저장
            if minCnt > cnt:
                minCnt = cnt
        # 5으로 나눠질 때
        if x % 5 == 0:
            calculate(x//5, cnt+1)
        # 3로 나눠질 때
        if x % 3 == 0:
            calculate(x//3, cnt+1)
        # 2로 나눠질 때
        if x % 2 == 0:
            calculate(x//2, cnt+1)
        # 1을 뺄 때
        calculate(x-1, cnt+1)
    print("back")
    return minCnt
    
N = int(input())

# 전역변수 선언, 최댓값으로 설정
global minCnt
minCnt = sys.maxsize
print(calculate(N, 0))


#==============================
# 보텀업 방식 

x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
    
