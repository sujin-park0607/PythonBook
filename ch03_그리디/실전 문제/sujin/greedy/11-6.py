# # 
## 11-4 만들 수 없는 금액

## Solution

### 문제의 아이디어 생각해낸 포인트
# 

### 시간 복잡도 계산
# 

### 입력
import copy
def solution(food_times, k):
    answer = 0
    origin_food = copy.deepcopy(food_times)
    
    food_times.sort()
    length = len(food_times)

    num = 0
    for i in range(1, len(food_times)):
        if num >= k:
            print("result:", food_times[i-1])
            break

        itrool = food_times[i] - food_times[i-1]
        print("num:,", num)
        print("length, food_time:", length, itrool,  length * food_times[i-1])
        num += length * itrool
        length -= 1 
    

    return answer

# array = [5,7,7,4,3,3,2,1,1]
# k = 17

# array = [5,1,3,7,2]
# k = 13

array = [3, 1, 2]
k = 5
solution(array, k)