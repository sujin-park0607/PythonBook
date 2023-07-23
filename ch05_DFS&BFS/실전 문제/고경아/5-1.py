"""
음료수 얼려 먹기
0으로 붙어있으면 연결되어 있는 것.
얼음 틀 세로 N, 가로 M
얼음 틀 뚫림 0, 막힘 1

노드가 0인지 조회. 주변에 0이 있는지 조회. False이면 방문. (...은 DFS/BFS가 아니지 않나)
"""

from collections import deque

## 데이터 입력
n, m = map(int, input("얼음 틀의 세로 길이 N과 가로 길이 M을 공백으로 구분하여 입력하세요: ").split())

ice_layout = []
for i in range(n):
    ice_layout.append(list(map(int, input("얼음 틀의 모양을 뚫림 0과 막힘 1로 구분하여 한 줄씩 입력하세요: "))))

## DFS 함수 작성
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False # 주어진 범위를 벗어나면 뚫린 공간이 없음(False)을 반환하고 종료한다.
    if ice_layout[x][y] == 0:
        ice_layout[x][y] = 1 # 방문한 곳이 뚫린 곳(0)이면 방문 처리(1)한다.
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1) # 상, 하, 좌, 우를 확인하여 연결된 곳(0)이 있으면 방문 처리(1)한다.
        return True # 음료수를 얼릴 공간, 즉 뚫린 공간(0)이 있음(True)을 반환한다.
    return False # 주어진 범위를 벗어났거나 막힌 공간(1)이므로 뚫린 공간이 없음(False)을 반환한다.

## DFS 함수 실행
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

## 결과 출력
print(result)

"""
예제 입력값
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""