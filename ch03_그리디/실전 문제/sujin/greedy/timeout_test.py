import random
import time 
# 시작시간
start = time.time()

#11-1 예제
def solution(array):
    array.sort()
    cnt = 1
    group = 0
    for i in array:
        if cnt == i:
            group += 1
            cnt = 1
        else: cnt += 1
    return group

array = []
for _ in range(100000):
    #랜덤 숫자
    array.append(random.randrange(1,100000))
print(solution(array))

# 끝시간
end = time.time()

print(round(end-start, 5))
print(f"{end-start:.5f}sec")

