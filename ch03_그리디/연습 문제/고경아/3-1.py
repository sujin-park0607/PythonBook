change = int(input("거스름돈을 입력하세요: "))
"""
1. 500원으로 몇 번 나눌 수 있는지 구한다 -> coin_500
2. 500 * n을 뺀다
3. 100원으로 몇 번 나눌 수 있는지 구한다 -> coin_100
4. 100 * n을 뺀다
5. 50원으로 몇 번 나눌 수 있는지 구한다 -> coin_50
6. 50 * n을 뺀다
7. 10원으로 몇 번 나눌 수 있는지 구한다 -> coin_10
8. coin_500 + coin_100 + coin_50 + coin_10을 구한다
"""

coin_500 = change // 500
change -= 500*coin_500

coin_100 = change // 100
change -= 100*coin_100

coin_50 = change // 50
change -= 50*coin_50

coin_10 = change // 10
change -= 10*coin_10

print(f"거슬러주고 남은 돈 = {change}")
print(f"거슬러줄 때 사용된 동전 개수 = 500원 {coin_500}개, 100원 {coin_100}개, 50원 {coin_50}개, 10원 {coin_10}개. 총 {coin_500 + coin_100 + coin_50 + coin_10}개")
