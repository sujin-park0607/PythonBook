"""
좌표는 리스트 [row, col]이고 [1, 1]에서 시작
공간의 크기 N, 마지막 좌표는 [N, N]
이동 L - col에서 -1
이동 R - col에서 +1
이동 U - row에서 -1
이동 D - row에서 +1
"""

n = int(input("공간의 크기 N을 입력하세요: "))
location = [1, 1]

plan_array = input("여행 계획을 L, R, U, D와 공백을 이용해 입력하세요: ").split()
for i in range(len(plan_array)):
    if (plan_array[i] == "L") and (location[1] > 1):
        location[1] -= 1
    elif (plan_array[i] == "R") and (location[1] < n):
        location[1] += 1
    elif (plan_array[i] == "U") and (location[0] > 1):
        location[0] -= 1
    elif (plan_array[i] == "D") and (location[0] < n):
        location[0] += 1
print(f"{location[0]} {location[1]}")