"""
나누어지는 수 N
나누는 수 M

나눌 수 있을 때 나눈다. 나눌 수 없을 때 1을 뺀다.
"""

N, M = list(map(int, input("나누어지는 수 N과, 나누는 수 M을 공백으로 구분하여 입력하세요: ").split()))
count = 0

while N != 1:
    if N % M == 0:
        N = N // M
    else:
        N -= 1
    count += 1
print(count)