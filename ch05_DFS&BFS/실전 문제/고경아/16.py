'''[연구소]'''
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# 지도의 세로 크기 N, 가로 크기 M
n, m = map(int, input().split())

# 지도의 모양. 빈칸 0, 벽 1, 바이러스 2 (바이러스는 2개 이상 10개 이하)
lab_map = []
for _ in range(n):
    lab_map.append(list(map(int, input().split())))

# 빈 벽 위치 저장
blank_wall = []
for i in range(n):
    for j in range(m):
        if lab_map[i][j] == 0:
            blank_wall.append([i, j]) # i&j, n&m을 서로 헷갈리지 말자!

# 수의 범위가 작은 것으로 보아, 모든 경우를 확인하며 풀어야 하는 문제로 보임
# 빈칸들 중 세 개를 골라 벽을 세우는 경우의 수를 돈다
# 각 경우마다 바이러스가 퍼지는 영역을 계산하고, 안전 영역 크기의 최댓값을 출력한다
new_wall_coms = list(combinations(blank_wall, 3))

# 벽을 세우고 바이러스 퍼트리기
max_safe_area = 0
for nwc in new_wall_coms:
    temp_map = [row[:] for row in lab_map] # 반복문으로 리스트의 요소를 제거할 경우, 복사본을 따로 만들거나, 인덱스만 모아서 마지막에 처리(indices_to_remove = [])
    for nw in nwc: # 조합 내부를 또 반복해야 함을 잊지 말자!
        temp_map[nw[0]][nw[1]] = 1
        # blank_wall.remove([i, j])
        # lab_map[nw[0]][nw[1]] = 2
        #   pop은 인덱스로 삭제, remove는 값으로 삭제
        #   여기서 갑자기 i, j를 왜 썼지? chatGPT는 어이 없는 오류를 빨리 찾을 수 있게 해줌.

    q = deque()
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                q.append((i, j))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()
        for i in range(4): # 상하좌우로 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_map[nx][ny] == 0:
                temp_map[nx][ny] = 2
                q.append((nx, ny))


    # 안전 영역 크기 계산
    safe_area = sum(row.count(0) for row in temp_map)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
"""
입력값
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
"""
