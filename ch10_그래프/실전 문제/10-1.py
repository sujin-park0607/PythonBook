# 팀 결성
import sys
input = sys.stdin.readline

# N+1개의 팀, 연산의 개수 M개
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (n + 1)
for i in range(0, n + 1):
    parent[i] = i

# 찾기 연산
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x # if에서 재귀적으로 호출하므로 else 필요 없음

# 합치기 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 각각의 연산
# 팀 합치기 연산 '0 a b' - a번 학생이 속한 팀과 b번 학생이 속한 팀을 합침
# 같은 팀 여부 확인 연산 '1 a b' - a번 학생과 b번 학생이 같은 팀에 속해있는지 확인
for _ in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        union_parent(parent, a, b)
    elif operation == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        elif find_parent(parent, a) != find_parent(parent, b):
            print("NO")

### 더 궁금한 것 - "YES NO를 리스트에 담아 한 번에 출력하지 않아도 되는 건가?"