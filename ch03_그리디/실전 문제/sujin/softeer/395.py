# 금고털이

##  구현방법
# 1. 시간초과 해결을 위해 우선순위 큐 구현 heaqp
# 2. max heaqp를 구현하기 위해서 p값을 음수화해서 정렬 후 다시 -1을 곱해준다

import sys
import heapq
input = sys.stdin.readline

w, n = map(int, input().split(" "))

array = []
for _ in range(n):
    m, p = map(int, input().split(" "))
    heapq.heappush(array,(p * -1,m))

result = 0
for i in range(len(array)):
    p , m = heapq.heappop(array)
    p *= -1 
    if w < m:
        result += w * p
        break
    w -= m
    result += (m * p)

print(result)    