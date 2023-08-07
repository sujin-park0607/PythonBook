'''[만들 수 없는 금액]'''
import sys

# 가장 작은 화폐 단위부터 순서대로 더해, 모든 결과를 리스트에 담는다
# 0부터 (가장 큰 화폐 단위 + 1)까지 확인한다
# 0부터 1씩 늘려가며 리스트에 있는지 확인하다가, 숫자가 리스트에 없으면 해당 숫자 반환

input = sys.stdin.readline

# n = int(input())
n = 5
# c_list = sorted(list(map(int, input().split())))
c_list = [1, 1, 2, 3, 9]

sum = []
for i in range(len(c_list)):
    if i < len(c_list) - 1:
        for j in range(i + 1, len(c_list)):
            sum.append() # 1+2+3, 1+3 등의 다양한 경우를 포함하지 못함.
    elif i >= len(c_list) - 1:
        sum.append(c_list[-1])

### -> 계산의 경우의 수들을 리스트에 전부 저장하는 게 아니라, 1부터 높여가며 가능한지만 확인한다.