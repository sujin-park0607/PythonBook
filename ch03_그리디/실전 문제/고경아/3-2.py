"""
배열의 크기 N
숫자가 더해지는 횟수 M
특정 인덱스가 연속으로 더해질 수 있는 최대 횟수 K
배열의 숫자들을 더하여 가장 큰 값을 만들어야 함
"""

# N, M, K를 입력받아 저장한다
input_value = input("N, M, K를 공백으로 구분하여 작성하세요: ")
value_list = list(map(int, input_value.split()))
N, M, K = value_list

# 배열을 받아 저장한다
input_list = input("배열을 공백으로 구분하여 입력하세요: ")
obj_list = list(map(int, input_list.split()))  #입력받은 문자열을 리스트로 바꾸고, 각 값을 정수형으로 바꾸고, 다시 리스트로 묶는다.

firstBiggestNum = 0
secondBiggestNum = 0
amount = 0
count = 0

# 가장 큰 값인 firstBiggestNum을 찾는다.
for num in obj_list:
    if num > firstBiggestNum:
        firstBiggestNum = num

# 두번째로 가장 큰 값인 secondBiggestNum을 찾는다.
temp_list = [num for num in obj_list if num != firstBiggestNum]  # firstBiggestNum을 제외한 임시 리스트
for num in temp_list:
    if num > secondBiggestNum:
        secondBiggestNum = num

# firstBiggestNum을 K번 만큼 더하고 secondBiggestNum을 한 번 더하는 과정을 반복한다.
# 총 더한 횟수가 M이 되면 위 과정을 멈춘다.

for _ in range (M):
    if count == K:
        amount += secondBiggestNum
        count = 0
    else:
        amount += firstBiggestNum
        count += 1

print(amount)