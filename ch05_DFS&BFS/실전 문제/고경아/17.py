'''[경쟁적 전염]'''
import sys

input = sys.stdin.readline

# 정사각형 시험관 크기 n, 바이러스 종류 가짓수 k
n, k = map(int, input().split())
virus_num = []
for k in range(1, k + 1):
    virus_num.append(k)

# 시험관 정보
test_tube = []
for _ in range (n):
    test_tube.append(list(map(int, input().split())))

# s초 후 (x, y)에 존재하는 바이러스의 종류 출력
s, x, y = map(int, input().split())

# 바이러스 증식
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(s):
    for v in virus_num:
        for t in test_tube:
            if v == t:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if test_tube[nx][ny] == 0:
                            test_tube[nx][ny] = v

print(test_tube[x - 1][y - 1])
"""
입력값
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""