# 새로운 게임 5:35 ~ 7:06

# N *N 체스판/ K개의 말
# 흰색, 빨간색, 파란색
# 1. 1~k번 말까지 순서대로 이동
# 이동할때 위에 올려져 있는 말도 함께 이동
# 가자 아래에 있는 말만 이동 가능
# 말이 4개 이상 쌓이는 순간 게임 종료

# 1. A번 말이 이동하려는 칸이 
#     - 흰색인경우: 그 칸으로 이동, 칸에 이미 말이 있는 경우 위에 올려놓기
#         - A번말위에 다른말이 있는경우 모두 이동
#     - 빨간색인 경우: A번 말과 그 위에 모든 말의 순서를 바꿈 
#         - A번 말 기준으로 순서바뀜 
#     - 파란색인 경우:
#         - A번말의 이동방향을 반대로하고 한칸 이동한다. 
#             -방향을 반대로 한 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 방향만 바꾼다.
#             - 체스판을 벗어나려는 경우도 파란색과 마찬가지

# 우 좌 상 하 순서

import sys
input = sys.stdin.readline

def move(idx, d):
    length = 0
    x, y = player_location[idx]
    nx = x + dx[d]
    ny = y + dy[d]

    # 범위 벗어난경우
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        if d % 2 == 0:
            d += 1
        else:
            d -= 1
        # d = (d+2) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        direction[idx] = d

        # 한칸 간게 파란색인 경우
        if ground[nx][ny] == 2:
            # direction[idx] = d
            return False
        # 파란색이 아닌 경우
        else:
            return move(idx, direction[idx])
            # direction[idx] = d
            # player[nx][ny].extend(player[x][y])
            # player[x][y] = []
            # direction[idx] = d
            # for l in player[idx]:
            #     player_location[l] = (nx,ny)

    # 파란색인 경우
    elif ground[nx][ny] == 2:
        if d % 2 == 0:
            d += 1
        else:
            d -= 1
        # d = (d+2) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        direction[idx] = d
        # 범위를 벗어난 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return False
        # 파란색인 경우
        if ground[nx][ny] == 2:
            # direction[idx] = d
            return False
        else:
            return move(idx, direction[idx])

            # player[nx][ny].extend(player[x][y])
            # player[x][y] = []
            # direction[idx] = d
            # for l in player[nx][ny]:
                # player_location[l-1] = (nx,ny)
    # 흰색일때
    elif ground[nx][ny] == 0:
        player[nx][ny].extend(player[x][y])
        player[x][y] = []
        if len(player[nx][ny]) >= 4:
            return True
        for l in player[nx][ny]:
            player_location[l-1] = (nx,ny)
    # 빨강일때
    else:
        player[nx][ny].extend(player[x][y][::-1])
        player[x][y] = []
        if len(player[nx][ny]) >= 4:
            return True
        for l in player[nx][ny]:
            player_location[l-1] = (nx,ny)
    
    return False
        
        
N, K = list(map(int, input().split()))
ground = []
player = [[[] for _ in range(N)] for _ in range(N)]
player_location = []
direction = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(N):
    ground.append(list(map(int, input().split())))

for k in range(K):
    x, y, d = list(map(int, input().split()))
    player[x-1][y-1].append(k+1)
    direction.append(d-1)
    player_location.append((x-1, y-1))

for t in range(1000):
    # print("---------",t+1,"번째--------------")
    for i in range(len(player_location)):
        x, y = player_location[i]
        # 마지막숫자가 현재 번호인가 ?
        if player[x][y][0] == i+1:
            isFinish = move(i, direction[i])
            if isFinish:
                break
            # print("length", isFinish)
            # print("------------map")
            # for i in player:
                # print(i)
    if isFinish:
        break
# print("player_location",player_location)
# print("direction", direction)
# print("------------finalmap")
# for i in player:
    # print(i)
    # turn += 1
if isFinish:
    print(t+1)
else:
    print("-1")
 
    