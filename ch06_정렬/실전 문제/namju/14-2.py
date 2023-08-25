

"""
안테나
4
5 1 7 9
"""

n = int(input())
locate = list(map(int, input().split()))
locate.sort()
# save = 0
# answer = []
# for x in locate:
#     for i in range(len(locate)):
#         save+=abs(x-locate[i])
#     answer.append(save)
#     save=0
# print(answer) # [18, 10, 10, 14] 결국 오름차순후 중간값이 정답...

print(locate[(n-1)//2])