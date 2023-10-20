# 조합

# 1. itertools를 활용한 방법
# from itertools import combinations

# arr = [0, 1, 2, 3, 4]
# combination_list = list(combinations(arr, 3))
# print(combination_list)
# print(len(combination_list))

# 2. yield를 사용해서 구현
def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next

# 3. 중복조합
def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i:], r-1):
                yield [array[i]] + next
                
array = [0, 1, 2, 3, 4]
combinations_list = []
for i in combinations(array, 3):
    combinations_list.append(i)

print(combinations_list)
print("조합 개수:",len(combinations_list))


