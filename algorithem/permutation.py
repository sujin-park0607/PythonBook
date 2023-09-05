# 조합
# itertools로 구현

# from itertools import permutations

# array = [0, 1, 2, 3, 4]
# permutation_list = list(permutations(array,3))
# print(permutation_list)

# yield로 구현
def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield[array[i]]
        else:
            for next in permutations(array[:i] + array[i+1:], r-1):
                yield [array[i]] + next

array = [0, 1, 2, 3, 4]
permutations_list = []
for i in permutations(array, 3):
    permutations_list.append(i)

print(permutations_list)
print("순열 개수:", len(permutations_list))