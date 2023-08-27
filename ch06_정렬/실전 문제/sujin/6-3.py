# # 
## 6-3 실패율

## Solution

### 문제의 아이디어 생각해낸 포인트
# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 1. 분자 배열 구하기 => 계수 정렬을 통해서 해당 인덱스에 인원수 구함
# 2. 분모 구하기 => 플레이어 수 - 이전의 스테이지 도달한 수
### 소요시간
# 19:20 ~ 20:00

def solution(N, stages):
    answer = []
    result = []

    numerator = [0 for _ in range(N+1)]
    denominator = []
    
    # 현재 진행하는 스테이지에 몇명이 존재하는지 구하기 -> 분자구하기
    for i in stages:
        if i > N:
            continue
        numerator[i] += 1

    length = len(stages)
    before = 0

    # 
    for i in range(1, len(numerator)):
        # 스테이지에 존재하지 않다면 실패율 0
        if numerator[i] == 0:
            result.append((i,0))
        # 스테이지에 인원이 존재하다면 실패율 구하기
        else:
            # 스테이지 인원수 / 전체 - 이전 스테이지 점령자 빼기
            # 현재 인덱스를 알아야하므로 튜플로 묶어서 넣어줌
            result.append((i, numerator[i] / (length - before)))
            before += numerator[i]

    # 튜플중 1번째 인덱스 값으로 정렬
    result = sorted(result, key = lambda x:-x[1])
    # 정렬된 값 중 스테이지만 뽑아서 배열 만듦
    for r in result:
        answer.append(r[0])
    return answer

# solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
solution(4,[4,4,4,4,4])