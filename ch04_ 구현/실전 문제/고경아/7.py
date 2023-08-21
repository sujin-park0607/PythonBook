'''[럭키 스트레이트]'''
import sys

input = sys.stdin.readline

num = input().rstrip() # 개행문자를 없애기 위함
left = list(map(int, num[:len(num)//2]))
right = list(map(int, num[(len(num)//2):])) # 인덱스가 소수가 되지 않도록, int로 변환하거나 //를 사용해야 함.

left_sum = 0
right_sum = 0
for s in left:
    left_sum += s
for s in right:
    right_sum += s

lucky = ""
if left_sum == right_sum:
    lucky = "LUCKY"
else: lucky = "READY"

print(lucky)
