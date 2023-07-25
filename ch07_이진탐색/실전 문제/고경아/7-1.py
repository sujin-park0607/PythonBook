'''
시작점과 끝점의 몫으로 중간점을 구한다.
리스트의 중간점과 찾고자 하는 값이 같은지 본다.
중간점보다 값이 작으면 끝점을 중간점 왼쪽으로, 크면 오른쪽으로 정한다.
반복.
'''

n = int(input("가게의 부품 개수 N을 입력하세요: "))
store_list = sorted(list(map(int, input("가게의 부품 종류를 공백으로 구분하여 입력하세요: ").split())))

m = int(input("손님의 주문 수량 M을 입력하세요: "))
customer_list = list(map(int, input("손님이 주문한 부품 종류를 공백으로 구분하여 입력하세요: ").split()))

def binary_search(product, start, end):
    mid = (start + end) // 2
    if (start < 0) or (end >= n) or (start > end):
        return "no"
    if store_list[mid] == product:
        return "yes"
    elif store_list[mid] > product:
        return binary_search(product, start, mid - 1) # 수정: 재귀 호출 결과를 반환하게 해야 함
    elif store_list[mid] < product:
        return binary_search(product, mid + 1, end) # 수정: 재귀 호출 결과를 반환하게 해야 함

result = []

for c in customer_list:
    result.append(binary_search(c, 0, n - 1))

print(result)