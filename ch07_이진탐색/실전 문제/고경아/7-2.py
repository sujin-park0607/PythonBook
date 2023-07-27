'''
[떡볶이 떡 만들기]
떡의 길이순으로 떡들을 돌면서 절단기 길이(가장 긴 떡의 길이부터 1씩 차감)와의 차를 구한다. 차의 합이 주문 길이 이상인지 확인한다.
'''

import sys

print("떡의 개수 N과 요청한 떡의 길이 M을 공백으로 구분하여 입력하세요.: ")
n, m = map(int, sys.stdin.readline().rstrip().split())

print("떡의 개별 높이를 입력하세요: ")
tteok_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

# start = 0, end = tteok_list[-1], mid = (start + end) // 2
start = 0
end = tteok_list[-1]

while start >= 0 and end <= tteok_list[-1]:
    tteok_height = 0
    mid = (start + end) // 2

    for t in tteok_list:
        if t >= mid: # [문제1] 이걸 안 해서 처음에 떡 길이가 음수가 되는 등 오류가 발생함.
            tteok_height += (t - mid) # 절단기 길이가 H == mid일 때 잘려 나온 떡의 길이를 계산한다

    if tteok_height < m:
        end = mid - 1 # 절단기 높이 H == mid일 때 절단된 떡의 길이가 모자라면 end = mid - 1

    elif tteok_height > m:
        start = mid + 1 # 절단기 높이 H == mid일 때 절단된 떡의 길이가 넘치면 start = mid + 1

    elif tteok_height == m:
        print(mid) # 절단기 높이 H == mid일 때 절단된 떡의 길이가 일치하면 결과값 출력 후 반복문 종료
        break
