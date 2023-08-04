# # 
## 4-2 자물쇠와 열쇠

## Solution

### 문제의 아이디어 생각해낸 포인트
# 

### 시간 복잡도 계산
# A. 평균: O(N)

### 소요시간
# 10M
import itertools
def rotated(array):
    # roatated = [[row[i] for row in array[::-1]] for i in range(len(array[0]))]
    rotated = zip(*array[::-1])
    rotated = [list(x) for x in rotated]
    return rotated   


def left_move(lock, key):
    str_key = []
    for k in key:
        str_key.append('0b' + ''.join(str(x) for x in k))
    print(str_key)
    # for k in key:
    for i in range(n):
        print(">>i==========", i)
        for j in range(len(str_key)):
            shift = int(str_key[j], 2) >> i
            if lock[j] != shift:
                continue 
            print("loc_result & shift calculation: ", lock[j],  shift)
            # print("shift calculation: ", lock[j], int(k, 2) >> j)

def right_move(lock, key):
    str_key = []
    for k in key:
        str_key.append('0b' + ''.join(str(x) for x in k))
    print(str_key)
    # for k in key:
    for i in range(n):
        print("<<i==========", i)
        for j in range(len(str_key)):
            shift = int(str_key[j], 2) << i
            if lock[j] != shift:
                continue 
            print("loc_result & shift calculation: ", lock[j],  shift)
            
            
    # for l, k in zip(lock, key):
    #     print("lock: ",l)
    #     print("key: ",k)
    #     str_number = ''.join(str(x) for x in i)
        # print(int(str_number, 2))
        # print(i >> 1)

lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# for i in lock:
#     print(i)
n = int(input())
print("====")
number = int(('1' * n),2)
# print(int(number,2))

lock_result = []
for l in lock:
    str_number = '0b'+''.join(str(x) for x in l)
    lock_result.append(number - int(str_number,2))
print("lock_result", lock_result)
left_move(lock_result, key)
right_move(lock_result, key)








