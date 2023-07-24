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
    
    # 절단기 높이 찾기
    height = (start + end) // 2
    

    # 절단한 떡의 길이 합 구하기
    height_sum = 0
    for i in array:
        if i > height:
            height_sum += i - height
    # 요청한 떡의 길이와 절단한 떡의 길이가 같을 경우 반환
    if height_sum == m:
        return height
    # 절단된 떡의 길이 < 요청한 떡의길이 -> 경우 절단기 높이를 줄임
    elif height_sum < m:
        return binary_search(array, m, start, height-1)
    # 절단된 떡의 길이 > 요청한 떡의길이 -> 경우 절단기 높이를 늘림
    else:
        return binary_search(array, m, height+1, end)

                

N, M = map(int,input().split(" "))
array = sorted(list(map(int, input().split(" "))))

# 절단기 길이 1~1000000범위를 모두 탐색
print(binary_search(array, M, 0, max(array)))
        

