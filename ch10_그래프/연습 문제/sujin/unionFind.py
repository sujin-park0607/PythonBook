# 루트노드 찾기-> 루트노드는 자기자신을 가르키고 있는 것을 활용
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# union집합 수행 -> 더 작은 노드를 부모로 만들기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선 입력
v, e = map(int, input().split(" "))
parent = [0] * (v+1)

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


# union find 연산 수행
for _ in range(e):
    a, b = map(int, input().split(" "))
    union_parent(parent, a, b)

for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

for i in range(1, v+1):
    print(parent[i], end =' ')
    





        