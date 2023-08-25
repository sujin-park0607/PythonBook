
"""
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""

# n = int(input())
# save = [input().split() for _ in range(n)] # ['Junkyu', '50', '60', '100']
# score = dict() # [name: 'Junkyu', korean: '50', english: '60', math: '100']
#
# print(save)

n = int(input())
score_list = []

for i in range(n):
    [name, kor, eng, math] = map(str, input().split())
    score_list.append([name, int(kor), int(eng), int(math)])
    print(score_list)
sorted_score_list = sorted(score_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))
                                                # 1: 국어가 감소 2: 영어 점수가 증가 3: 수학점수가 감소 4: 이름순서 증가
for score in sorted_score_list:
    print(score[0])