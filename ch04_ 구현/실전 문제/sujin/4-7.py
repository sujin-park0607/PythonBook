# # 
## 4-7 치킨배달 

## Solution

### 문제의 아이디어 생각해낸 포인트
# 1차시도 -> 
# 나올수 있는 치킨집의 모든 경우의 수를 구한 후 bfs로 거리의 최소값을 구하고 더한다 
# 좌표로 문제가 나왔다고해서 다 dfs, bfs가 아니다! 문제를 잘 읽고 홀리지 말기


### 소요시간
# 14:20~ 16:20 답안 참고

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)