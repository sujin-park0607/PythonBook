INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 -> 자기자신 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선 초기화
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    graph[a][b] = c


# 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # if a==b: continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print("=========")
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end =" ")
    print()