import sys
from itertools import combinations

input = sys.stdin.readline

# 도시의 크기 N * N, 도시에서 가장 수익을 많이 낼 수 있는 치킨집은 최대 M개
# n, m = map(int, input().split())
n, m = 5, 2

# 도시의 정보(빈칸 0, 집 1, 치킨집 2)
chicken_map = []
# for _ in range(n):
#     chicken_map.append(list(map(int, input().split())))
chicken_map = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]

# 전체 치킨 집을 M개씩 조합해보고, 가장 짧은 거리를 출력한다.
# 집과 치킨 집을 정리. 치킨 집을 조합해 집들과의 거리 계산. 더 짧은 값으로 갱신.
home = []
chicken_store = []
for i in range (n):
    for j in range (n):
        if chicken_map[i][j] == 1:
            home.append([i + 1, j + 1])
        elif chicken_map[i][j] == 2:
            chicken_store.append([i + 1, j + 1])

# '조합'이 관건. 그 후에는 집을 돌면서 치킨 집과의 가장 짧은 거리를 구하고 더해 비교하면 된다. -> 모듈 사용
chicken_store_combos = list(combinations(chicken_store, m))
chicken_distance_min = 2 * n # 집과 치킨 거리의 최솟값
city_distance_min = 2 * n * m # 도시 치킨 거리의 최솟값

for combo in chicken_store_combos:
    city_distance = 0
    for h in home:
        for chicken in combo:
            width = abs(h[0] - chicken[0])
            height = abs(h[1] - chicken[1])
            dis = width + height
            if dis < chicken_distance_min:
                chicken_distance_min = dis
        city_distance += chicken_distance_min
    if city_distance < city_distance_min:
        city_distance_min = city_distance

print(city_distance_min)