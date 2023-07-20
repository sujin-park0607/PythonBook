"""
카드 행의 개수 N
카드 열의 개수 M
N * M의 카드 배열

각 행에서 가장 작은 값을 찾는다.
각 행의 가장 작은 값 중 가장 큰 값을 찾는다.
찾은 값을 반환한다.
"""

N, M = list(map(int,input("카드 행과 열의 개수를 공백으로 구분하여 입력하세요: ").split()))

array = []
min_array = []
for i in range(1, N + 1):
    array_input = list(map(int, input(f"카드 배열 {i}번째 행을 공백으로 구분하여 입력하세요: ").split()))
    array.append(array_input)
    min_array.append(min(array_input))
print(max(min_array))