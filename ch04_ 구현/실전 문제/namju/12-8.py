from itertools import permutations
def solution(n, weak, dist):

    # 0을 넘어가는 순간 길이를 두배로 늘림
    length = len(weak)
    weak = weak + [w + n for w in weak]
    minCnt = 1e9
    for start in range(length):
        for d in permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, length):
                nexPos = start + i
                diff = weak[nexPos] - weak[pos]
                if diff > d[cnt-1]:
                    pos = nexPos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)

    #방문이 안되는 경우
    if minCnt == 1e9:
        return -1
    return minCnt

"""
제출
"""