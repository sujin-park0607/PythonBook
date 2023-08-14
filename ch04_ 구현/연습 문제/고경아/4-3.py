"""
8 * 8의 좌표 평면
나이트는 L자로만 움직일 수 있음
위치가 주어졌을 때 이동 가능한 경우의 수

1. 좌표 a1 받기
- 방1. 평면을 a1, a2, ..., h8까지의 좌표가 있는 버전으로 만든다. 평면에서 좌표 a1을 찾아 인덱스 [1, 1]을 알아낸다.
- 방2. 좌표 변환 사전을 a-1, b-2, ..., h-8로 만든다. a1을 [1, 1]로 변환한다. (채택)
2. 좌표에서 총 8가지 경우의 수 중 몇 개가 가능한지 확인하기
"""


# location = input("나이트의 위치 좌표를 공백으로 구분하여 입력하세요: ")
location = "a1"
location_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8
}
location_array = [location_dict[f"{location[0]}"], int(location[1])]  #좌표를 리스트로 변환

count = 0
# "가능하다"란, 연산 후 값이 1 이상이고 8 이하인 것.
# 왼쪽으로 두 칸 갈 수 있는지 확인. 위나 아래로 가능한지 확인.
if location_array[0] - 2 >= 1:
    if location_array[1] + 1 <= 8:
        count += 1
    if location_array[1] - 1 >= 1:
        count += 1
# 오른쪽으로 두 칸 갈 수 있는지 확인. 위나 아래로 가능한지 확인.
if location_array[0] + 2 <= 8:
    if location_array[1] + 1 <= 8:
        count += 1
    if location_array[1] - 1 >= 1:
        count += 1
# 위쪽으로 두 칸 갈 수 있는지 확인. 좌나 우로 가능한지 확인.
if location_array[1] - 2 >= 1:
    if location_array[0] - 1 >= 1:
        count += 1
    if location_array[0] + 1 <= 8:
        count += 1
# 아래쪽으로 두 칸 갈 수 있는지 확인. 좌나 우로 가능한지 확인.
if location_array[1] + 2 <= 8:
    if location_array[0] - 1 >= 1:
        count += 1
    if location_array[0] + 1 <= 9:
        count += 1

print(count)