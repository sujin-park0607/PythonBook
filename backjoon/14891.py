# 5:50~

def rotate(array, d):
    if d == 1: #시계
        array = [array[-1]] + array[:-1]
    
    else: # 반시계
        array = array[1:] + [array[0]]
    return array
        

array = []
for _ in range(4):
     array.append(list(map(int, input())))

confirmList = []
N = int(input())

for _ in range(N):
    num, direction =  list(map(int, input().split()))
    num -= 1

    # 회전해야할 리스트 구하기
    confirmList.append((num,direction))
    # 좌측으로 회전 여부 탐색 
    d = direction,
    for i in range(num, 0, -1):
        if array[i][0] != array[i-1][4]:
            d *= -1
            confirmList.append((i-1,d))
        else: break
    # 우측으로 회전 여부 탐색
    d = direction
    for i in range(num, 3):
        if array[i][4] != array[i+1][0]:
            d *= -1
            confirmList.append((i+1,d))
        else:
            break

    # print("confirmList",confirmList)
    # 회전
    for num,dd in confirmList:
        array[num] = rotate(array[num], dd)

# print("--------------")
# for i,d in confirmList:
#     print(i+1, d, end=" //")
# print(confirmList)

# 점수 계산
score = 0
cnt = 1
print("---------")
for i in array:
    print(i)
print("---------")
for idx in range(len(array)):
    # print(array[idx][2])
    if array[idx][2] != 0:
        score += cnt
    cnt *= 2

print(score)
        
        




    
        
        

    

