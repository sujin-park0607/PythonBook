'''[곱하기 혹은 더하기]'''
import sys

input = sys.stdin.readline

s_list = list(map(int, input().strip())) # split을 사용하지 않아서 개행 문제를 제거하기 위해 strip 필요

result = 0
for s in s_list:
    if result == 0 or s == 0:
        result += s
    else:
        result *= s

print(s_list)
print(result)

### -> 1은 곱하는 것보다 더하는 게 이득이라는 점을 고려하지 않음!