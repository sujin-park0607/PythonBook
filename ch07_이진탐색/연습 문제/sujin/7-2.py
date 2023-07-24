# # 
## 7-1 부품 찾기

## Solution

### 문제의 아이디어 생각해낸 포인트
# M의 길이가 20억이기 때문에 계수정렬 불가
# N의 범위가 백만개이기 때문에 이진탐색으로 절단기의 높이를 찾는것이 유리하다고 생각함

### 시간 복잡도 계산
# A. O(logN) 

def binary_search(array, m, start, end):
    if start > end:
        return None
    
    height = (start + end) // 2
    # print("height: ",height)
    height_sum = 0
    for i in array:
        if i > height:
            height_sum += i - height

    # print("height_sum: ",height_sum)

    if height_sum == m:
        return height
    elif height_sum < m:
        return binary_search(array, m, start, height-1)
    else:
        return binary_search(array, m, height+1, end)

                

N, M = map(int,input().split(" "))
array = sorted(list(map(int, input().split(" "))))

print(binary_search(array, M, 1, 1000000))
        

