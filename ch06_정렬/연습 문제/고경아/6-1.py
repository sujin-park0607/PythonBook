"""
수열 내림차순 정렬
"""
n = int(input("수열에 속해있는 수의 개수: "))

num_seq = [] # 수열 생성
for _ in range(n):
    num_seq.append(int(input("수열 숫자: ")))

num_seq.sort() # 정렬
num_seq.reverse() # 뒤집기
로
print(num_seq) # 결과 출력