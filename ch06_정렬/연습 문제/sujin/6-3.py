# # 
## 6-3 두 배열의 원소 교체

## Solution

### 문제의 아이디어 생각해낸 포인트
# A배열의 k개의 최소값과 B배열의 k개의 최대값을 교체

### 시간 복잡도 계산
# A. O(NlogN), python sort함수인 병합정렬을 사용하기 때문에 

N, K = map(int,input().split(" "))
A = sorted(list(map(int, input().split(" "))))
B = sorted(list(map(int, input().split(" "))), reverse=True)

result = 0
for i in A[K:] + B[:K]:
    result += i

print(result)
