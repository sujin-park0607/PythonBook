"""
치킨배달
"""

from itertools import combinations
n, m = map(int, input().split())
chicken = []
house = []
# house, chicken 좌표 저장
for x in range(n):
    data = list(map(int, input().split()))
    for y in range(n):
        if data[y]==1:
            house.append((x,y))
        elif data[y]==2:
            chicken.append((x,y))

comb = list(combinations(chicken, m))

# 각각의 집에 대응되는 치킨거리의 합 구하기
def all_find(comb):
    answer=0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in comb:
            temp = min(temp, abs(hx-cx)+ abs(hy-cy))
        answer +=temp
    return answer

answer = 1e9
#치킨 위치를 하나씩 집어넣어 해당 치킨집에 대응되는 모든 집의 거리중 최소값 저장
for c in comb:
    answer = min(answer, all_find(c))

print(chicken)
print(house)
print(comb)
print(answer)

"""
제출
"""