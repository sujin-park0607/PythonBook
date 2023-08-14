def solution(key, lock):
    # 회전하는 경우를 계산한 후, 이동하는 동안 반복.
    key_len = len(key)
    rotated_key = [[0] * len(key[0]) for _ in range(key_len)]

    for i in range(key_len):
        for j in range(key_len):
            rotated_key[j][n - i - 1] = key[i][j]

    answer = True

    return answer
