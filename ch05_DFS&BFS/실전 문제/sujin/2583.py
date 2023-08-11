import sys

# input = sys.stdin.readline().rstrip

m, n, k = map(int, input().split(" "))

graph = [[0 for i in range(n)] for j in range(m)]

for _ in range(k):
    y, x, ny, nx = map(int, input().split(" "))
    ny -= 1
    nx -= 1

    x = m-1-x
    nx = m - 1- nx
    print("x,y",x, y)
    print("nx,ny",nx, ny)
    for i in range(nx, nx + x):
        for j in range(y, ny + y + 1):
            graph[i][j] += 1

for i in graph:
    print(i)
