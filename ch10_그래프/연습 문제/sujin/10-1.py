# # 
## 10-1 팀 결성

## Solution

### 문제의 아이디어 생각해낸 포인트
# 팀 합치기 -> union
# 같은팀 확인 -> find
# unionFind로 풀 수 있는 문제 

### 시간 복잡도 계산
# A.   

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

n, m = map(int, input().split(" "))

parent = [0] * (n+1)
graph = [0] * (n+1)

#자기자신으로 초기화
for i in range(n):
    parent[i] = i

for _ in range(m):
    cal, a, b = map(int, input().split(" "))

    # a, b 부모찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 팀 합치기
    if cal == 0:
        # 작은 노드를 부모로 만듦
        if a < b:
            graph[b] = a
        else:
            graph[a] = b
    # 팀 여부 확인
    else:
        # 부모가 같으면 Yes, 아니면 No
        if a != b:print("NO")
        else: print("YES")


        

    
    
    
# graph = [[] for i in range(v+1)]

    



