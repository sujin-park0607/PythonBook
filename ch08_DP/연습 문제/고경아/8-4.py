'''
[효율적인 화폐 구성]
'''

n, m = map(int, input("화폐의 종류 가짓수 n과 가치의 합 m을 공백으로 구분하여 입력: ").split())

coin_list = sorted([int(input("각 화폐의 가치를 하나씩 입력:")) for _ in range(n)])

d = [0] * 10001 # d[i]에 (가치의 합 m == i일 때의 최소한의 화폐 개수)를 저장하는 DP 테이블

for c in coin_list: # 각 화폐 하나로 만들 수 있는 경우의 d[i]를 초기화
    d[c] = 1

divisible = False
for i in range(m): # 각 화폐로 나눠 떨어지는 경우, 마지막에 각 화폐를 사용한 경우의 d[i]를 구하여 가장 작은 값으로 저장. 어떤 화폐와도 나눠 떨어지지 않으면 문제 내 최댓값인 10001로 둠.
    for c in coin_list:
        if m % c == 0:
            d[i] = min(d[i], d[i - c] + 1)
            divisible = True
    if divisible == False:
        d[i] = 1001

for i in range(m): # 앞서 나눠 떨어지지 않아 1001로 두었던 값들을, 문제에서 불가능을 의미하는 -1로 바꿔줌
    if d[i] == 1001:
        d[i] = -1

print(d[i])