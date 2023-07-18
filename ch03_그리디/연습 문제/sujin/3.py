#숫자 카드 게임
N, M = map(int, input().split(" "))

result = 1
for _ in range(N):
    cards = sorted(list(map(int, input().split(" "))))
    result = max(result, cards[0])

print(result)
