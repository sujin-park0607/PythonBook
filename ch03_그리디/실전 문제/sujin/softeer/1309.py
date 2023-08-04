# 성적 평가

# 1. 처음에는 2중 for문으로 구현 -> 시간초과
# 2. 정렬된 배열, 그렇지 않은 배열로 이진탐색으로 몇번째존재하는지 구현
# 3. 만약 같은 숫자일경우 while문을 통해서 앞자리 수를 가르키도록 함
import sys
input = sys.stdin.readline

n = int(input())
result = []
global total_score
total_score = [0] * n

# 이진탐색
def binary_search(array, target, start, end):
    if start > end: return None
    mid = (start + end) // 2
    if target == array[mid]:
        while(array[mid] == array[mid-1] and mid > 0):
            mid -= 1
        return mid
            
        return mid
    elif target < array[mid]:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)



def find_grade(sort_array, array):
    grade = []
    for i in range(len(array)):
        total_score[i] += array[i]
        result = binary_search(sort_array, array[i], 0, n)
        grade.append(result+1)
    return grade
    

for k in range(3):
    array = list(map(int, input().split(" ")))
    sort_array = sorted(array.copy(), reverse=True)
    result.append(find_grade(sort_array, array))

grade = []
total_array = sorted(total_score.copy(), reverse=True)

for num in total_score:
    grade.append(binary_search(total_array, num, 0, n) + 1)
result.append(grade)

for i in result:
    print(" ".join(list(map(str,i))))

