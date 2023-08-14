import sys

input = sys.stdin.readline

# 도시의 크기 N * N, 도시에서 가장 수익을 많이 낼 수 있는 치킨집은 최대 M개
# n, m = map(int, input().split())
n, m = 5, 3

# 도시의 정보(빈칸 0, 집 1, 치킨집 2)
chicken_map = []
# for _ in range(n):
#     chicken_map.append(list(map(int, input().split())))
chicken_map = [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]

# 도시 치킨 거리의 최솟값
chicken_distance_min = 0