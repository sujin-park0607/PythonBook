# 에라토스테네스의 체

# 소수를 구하는 알고리즘
# 소수 : 1과 그 수 자신 이외의 자연수로 나눌 수 없는 자연수

# 기본적인 방법: 1부터 100 사이의 소수를 구하는 파이썬 코드
# def isPrime(a):
#     if(a<2):
#         return False
#     for i in range(2,a):
#         if(a % i == 0):
#             return False
#     return True

# for i in range(n+1):
#     if(isPrime(i)):
#         print(i)

# 에라토스테네스의 체 알고리즘
# 1. 2부터 N까지의 모든 자연수를 나열한다.
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다
# 3. 남은 수 중에서 i의 배수를 모두 제거한다
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

import math
n = 1000
# 처음엔 모든 수가 소수(True) 인 것으로 초기화
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘
# 2부터 n의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(n)) + 1):
    # i가 소수인 경우 (남은 수인 경우)
    if array[i]:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
