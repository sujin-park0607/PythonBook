# 조합
# def combinations(array, r):
#     for i in range(len(array)):
#         if r == 1:
#             yield [array[i]]
#         else:
#             for next in combinations(array[:i], r-1):
#                 yield [array[i]] + next
# array = [1,2,3,4,5]
# combinationList = []
# for i in combinations(array, 3):
#     combinationList.append(i)

# def permutation(array, r):
#     for i in range(len(array)):
#         if r == 1:
#             yield [array[i]]
#         else:
#             for next in permutation(array[:i] + array[i+1:], r-1):
#                 yield [array[i]] + next
# array = [1,2,3,4,5]
# permutationList = []
# for i in permutation(array, 3):
#     permutationList.append(i)
# print(permutationList)
# print(len(permutationList))


# 소수찾기
# import math

# n = 10
# isPrime = [True for _ in range(n+1)]

# for i in range(2, int(math.sqrt(n))+1):
#     if isPrime[i]:
#         j = 2
#         while i * j <= n:
#             isPrime[i*j] = False
#             j += 1
# prime = []
# for i in range(2,len(isPrime)):
#     if isPrime[i]:
#         prime.append(i)
# print(prime)

# 가장 긴 증가하는 부분수열
# array = [10, 20, 10, 30, 40, 50, 70]
# n = 7

# array = [0] + array
# dp = [0 for _ in range(n+1)]

# for i in range(1, n+1):
#     mx = 0
#     for j in range(0, i):
#         if array[j] < array[i]:
#             mx = max(mx, dp[j])
#     dp[i] = mx + 1

# array = [10, 20, 10, 30, 40, 50, 70]
# n = 7
# array = [0] + array
# dp = array[:]

# for i in range(1, n+1):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], array[i] + dp[j])

# print(dp)

# union find

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_find(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b 

