# 치킨배달
# 0은 빈칸/ 1은 집/ 2는 치킨집
# 치킨집의 최대는 M개 
# 도시에 있는 치킨집 중 최대 M개를 고르고 나머지 치킨집은 모두 폐업
# 도시의 치킨 거리가 가장 작게 될 프로그램 

# 치킨집중 M개의 조합을 모두 구하기
# 치킨거리 구하기 
#최소 치킨 거리 출력 

import sys
input = sys.stdin.readline
INF = sys.maxsize
def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combination(array[:i], r-1):
                yield [array[i]] + next


N, M = list(map(int, input().split()))
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

# 치킨집 위치 확인
checkinList = []
peopleList = []
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            peopleList.append((i,j))
        elif array[i][j] == 2:
            checkinList.append((i,j))
            array[i][j] = 0

# 치킨집 조합
combinationList = []
for i in combination(checkinList, M):
    combinationList.append(i)
# print(combinationList)
# print(len(combinationList))
minDistance = INF
minChickenDistance = INF

for combi in combinationList:
    chickenDistance = 0
    for px, py in peopleList:
        minDistance = INF
        for cx, cy in combi:
            minDistance = min(minDistance, abs(px - cx) + abs(py - cy))
        chickenDistance += minDistance

    minChickenDistance = min(minChickenDistance, chickenDistance)
print(minChickenDistance)
        
    
