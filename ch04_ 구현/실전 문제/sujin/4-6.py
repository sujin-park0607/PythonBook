# # 
## 4-6 기둥과 보 설치

## Solution

### 문제의 아이디어 생각해낸 포인트
# 그냥 있는대로 구현,,,?

### 시간 복잡도 계산
# A. 

### 소요시간
# 17:00 ~  

# 
def solution(n, build_frame):
    answer = []

    array = [[2 for _ in range(n+1)] for _ in range(n+1)]
    
    for frame in build_frame:
        x, y, a, b = frame

        # 구조물 설치
        if b==1:
            #기둥 
            if a == 0:
                # 만약 바닥에 있거나, 왼쪽에 보가 설치되어있거나, 기둥이 아래에 있거나 할때 기둥 설치
                if y == 0 or array[x-1][y] == 1 or array[x][y-1] == 0:
                    array[x][y] = 0  
                    answer.append([x,y,0])
            #보
            elif a== 1:
                # 왼쪽이 기둥일 경우 , 오른쪽이 기둥일 경우, 양쪽이 보일 경우
                if array[x][y-1] == 0 or array[x+1][y-1]==0 or array[x-1][y] == array[x+1][y] == 1:
                    array[x][y] = 1
                    answer.append([x,y,1])
        # 구조물 제거
        else:
            # 기둥
            if a == 0:
                
            # 보
            
    # for i in array:
    #     print(i)
    answer.sort(key = lambda x:x[0])
    return answer

n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n,build_frame))
