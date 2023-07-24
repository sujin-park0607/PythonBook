n = int(input("학생의 수: "))

student_score = []
for _ in range(n):
    student_score_input = input("학생 이름과 성적을 공백으로 구분하여 입력: ").split()
    student_score.append([student_score_input[0], int(student_score_input[1])])

for i in range(len(student_score)):
    min_index = i
    for j in range(i + 1, len(student_score)):
        if student_score[min_index][1] > student_score[j][1]:
            min_index = j
    student_score[i], student_score[min_index] = student_score[min_index], student_score[i]

for i in range(len(student_score)):
    print(student_score[i][0])