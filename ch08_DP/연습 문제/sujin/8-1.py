# # 
## 8-1 1로 만들기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 재귀로 3으로 나눌때, 2로 나눌때, -1 할때 모두 탐색
# 대신 중간에 cnt가 minCnt보다 커지게 될 경우 탐색 안하는 조건 설정

### 시간 복잡도 계산
# A.  
import sys
sys.setrecursionlimit()

def calculate(x, cnt):
    global minCnt
    # print("x,cnt : ",x, cnt)
    # 기존에 최소연산횟수를 안넘어갈 경우
    if cnt <= minCnt:

        # 종료 조건: 1이 될 때
        if x == 1:
            # print("cnt========",cnt, minCnt)
            # cnt 최솟값 저장
            if minCnt > cnt:
                minCnt = cnt
        # 3으로 나눠질 때
        if x % 3 == 0:
            calculate(x//3, cnt+1)
        # 2로 나눠질 때
        if x % 2 == 0:
            calculate(x//2, cnt+1)
        # 1을 뺄 때
        calculate(x-1, cnt+1)
    # print("back")
    return minCnt
    
N = int(input())

# 전역변수 선언, 최댓값으로 설정
global minCnt
minCnt = sys.maxsize
print(calculate(N, 0))


    
