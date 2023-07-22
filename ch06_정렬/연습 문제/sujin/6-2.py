# # 
## 6-2 성적이 낮은 순서로 학생 출력하기

## Solution

### 문제의 아이디어 생각해낸 포인트
# 성적이 낮은순대로 이름을 출력
# 딕셔너리를 사용하여 정렬 후 key값 출력

### 시간 복잡도 계산
# A. O(NlogN), python sort함수인 병합정렬을 사용하기 때문에 

N = int(input())
student = dict()
for _ in range(N):
    name, score = input().split(" ")
    student[name] = int(score)

sort_dict = sorted(student.items(), key = lambda item: item[1])
print(sort_dict)
# print(list(sort_dict.values()))

for score in sort_dict:
    print(score[0], end=' ')

