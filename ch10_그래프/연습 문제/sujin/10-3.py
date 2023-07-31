# # 
## 10-3 커리큘럼

## Solution

### 문제의 아이디어 생각해낸 포인트
# 인접한 경로를 찾을 때 더 큰 시간의 값만 더해줌

### 시간 복잡도 계산
# A.   
from collections import deque
import copy
n = int(input())
indegree = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for i in range(n+1)]

# 입력받는 값 강의시간, 선수강의번호
for i in range(1, n+1):
    input_list = list(map(int, input().split()))
    time[i] = input_list[0]
    idx = 1
    while(input_list[idx] != -1):
        graph[input_list[idx]].append(i)
        indegree[i] += 1
        idx += 1    
# print("time: ", time)
# print("indegree: ", indegree)
# print("graph: ", graph)
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 진입차수 0인것 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            # print(result)
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()




