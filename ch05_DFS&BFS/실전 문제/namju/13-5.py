

"""
연산자 끼워넣기
2
5 6
0 0 1 0
"""

def DFS(v, sum):
    global minv, maxv, plus, minus, double, divid
    if v == n:
        minv = min(minv, sum)
        maxv = max(maxv, sum)
    else:
        if plus>0:
            plus-=1
            DFS(v+1, sum+num[v])
            plus+=1
        if minus>0:
            minus -=1
            DFS(v+1, sum-num[v])
            minus +=1
        if double>0:
            double -=1
            DFS(v+1, sum*num[v])
            double +=1
        if divid>0:
            divid -=1
            DFS(v+1, sum//num[v])
            divid+=1

from itertools import combinations
n = int(input())
num = list(map(int, input().split()))
#tools = list(map(int, input().split()))
plus, minus, double, divid = map(int, input().split())

# 전체탐색으로 모든 경우를 구해야할것 같은디
minv = 1e9
maxv = -1e9
DFS(1, num[0])

print(maxv)
print(minv)