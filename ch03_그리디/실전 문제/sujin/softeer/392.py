# 강의실 배정
import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    s, f = map(int, input().split(" "))
    heapq.heappush(q, (f,s))
    # array.append((s, f))
# array = sorted(array, key = lambda x: x[1])

# i = (finish, start)
cnt = 1
# print(array)

b_f = 0
cnt = 0
while q:
    f,s = heapq.heappop(q)
    if s >= b_f:
        cnt += 1
        b_f = f
print(cnt)

    