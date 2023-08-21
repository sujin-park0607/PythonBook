"""
맵의 크기 N * M
캐릭터 좌표 (A, B), 방향 d
방향 d 0북 1동 2남 3서

왼쪽 방향 확인. 가보지 않은 육지이면 이동. 아니면 또 왼쪽.
갈 곳이 없으면 현재 방향에서 뒤로 이동. 뒤쪽이 바다면 종료.
"""

# n, m = list(map(int, input("맵의 크기 N * M을 공백으로 구분하여 입력하세요: ").split()))
n, m = [4, 4]

# a, b, d = list(map(int, input("캐릭터 좌표 (A, B)와 방향 d를 공백으로 구분하여 입력하세요: ").split()))
a, b, d = [1, 1, 0]
location = [a, b]

map_list = []
for i in range(n):
    # map_list.append(list(map(int, input("맵의 상태를 한 줄씩 입력하세요 (0육지, 1바다): ").split())))
    map_list.append([1, 1, 1, 1])

while True:
    if d == 0:
        if location[a] - 1