'''[볼링공 고르기]'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
b_list = sorted(list(map(int, input().split())))

count = 0
for i in range(len(b_list)):
    for j in range(i + 1, len(b_list)):
        if i != j:
            count += 1
print(count)

### -> i에 같은 값이 두 번 계산될 경우를 고려하지 않음