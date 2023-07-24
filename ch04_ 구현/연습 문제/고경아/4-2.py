"""
00시 00분 00초부터 N시 00분 00초까지. (N<=23)
3이 하나라도 포함되는 경우의 수.
"""

# N = int(input("시간을 입력하세요: "))
N = 5

hour_min_sec_list = [0, 0, 0]
count = 0
# 분, 초는 59 이하이다.
# 초가 59를 넘으면 분을 1 올리고, 초는 0이 된다.
# 분이 59를 넘으면 시를 1 올리고, 분은 0이 된다.
# (분 또는 초)의 (1의 자리 숫자나 10의 자리 숫자)가 3이면 count++
# 시가 N이 되면 프로그램이 끝난다.

def is_duplicated(hms_list):
    hms_list = hms_list
    three_val = False
    for num in hms_list:
        if ((num // 10) == 3) or (((num - (num // 10) * 10)) == 3):
            three_val = True
    print(three_val)
    return three_val

while hour_min_sec_list[0] <= N:  # 시가 N이 되면 프로그램이 끝난다.
    while hour_min_sec_list[1] < 60:  ## for문 활용해보기.
        while hour_min_sec_list[2] < 60: # 분, 초는 59 이하이다.
            ## (1)초 올리고 카운트 올리기 vs (2)카운트 올리고 초 올리기.
            print(hour_min_sec_list)
            # print(f"{hour_min_sec_list[1] // 10} {hour_min_sec_list[1] - (hour_min_sec_list[1] // 10 * 10)}")
            # print(f"{hour_min_sec_list[2] // 10} {hour_min_sec_list[2] - (hour_min_sec_list[2] // 10 * 10)}")
            if (is_duplicated(hour_min_sec_list)):
                count += 1  # (시 또는 분 또는 초)의 (1의 자리 숫자나 10의 자리 숫자)가 3이면 count++
            hour_min_sec_list[2] += 1

        hour_min_sec_list[1] += 1
        hour_min_sec_list[2] = 0  # 초가 59를 넘으면 분을 1 올리고, 초는 0이 된다.
    hour_min_sec_list[0] += 1
    hour_min_sec_list[1] = 0  # 분이 59를 넘으면 시를 1 올리고, 분은 0이 된다.
print(count)

