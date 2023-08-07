# # 
## 4-3 문자열 압축

## Solution

### 문제의 아이디어 생각해낸 포인트
# 문자열을 1~ n까지 잘라서 중복된 문자열이 있는지 반복문 돌림
# 중복된 문자열이 있다면 cnt를 올려주고 없다면 길이값을 계속 더해짐
# 반복해서 최종으로 길이값 반환

### 시간 복잡도 계산
# A. 평균: O(N)

### 소요시간
# 1h 


def solution(s):
    
    answer = 0
    s = list(s)
    n = len(s)
    length = 0
    minNum = 1000
    cnt = 1

    # n의 개수가 1 이하일때
    if n <= 1:
        answer = n
        return answer


    # print("s:",s[0:1])
    # 1부터 s의 길이까지 문자열을 자를 개수를 반복문으로 돌린다.(1개씩 자르기, 2개씩 자르기 ..)
    for i in range(1,n):
        # print("i----",i)
        # 문자열 반복 횟수를 cnt에 저장
        
        length = 0
        # i만큼 더하기를 해주는 반복문과, 슬라이싱을 통해 문자열을 비교해준다
        for j in range(0, n-i, i):
            # print("i,j", j,j+i, end=' ')
            # print(" current: ", s[j:j+i], end=' ')
            # print("after: ", s[j+i:j+i+i])

            # 현재의 문자열과 다음의 문자열이 같다면 cnt를 올려준다
            if s[j:j+i] == s[j+i:j+i+i]:
                cnt += 1

            # 문자열이 다를때
            else:
                # 길이를 더해준다
                length += len(s[j:j+i])
                # print(len(s[j:j+i]))
                # 문자열 반복이 있었을 경우
                if cnt != 1:
                    # 해당 숫자의 자리수만큼 더해준다
                    length += len(str(cnt))
                    cnt = 1
                    # print(len(str(cnt)))
                # print("length= ", length)

        # 반복문에 나가서도 남아있는 문자열을 더해준다
        length += len(s[j+i:])
        # print("current: ",s[j+i:])
        #남아있는 숫자가 있다면 더해준다 
        if cnt != 1:
            length += len(str(cnt)) 
        # print("====")
        # print("result_length= ", length)
        # 최솟값을 구한다
        if length < minNum:
            minNum = length 

    answer = minNum
    # print(answer)
    # result.append(answer)
    return answer
        
    
s1 = "aabbaccc"
s2 = "ababcdcdababcdcd"
s3 = "abcabcdede"
s4 = "abcabcabcabcdededededede"
s5 = "xababcdcdababcdcd"
s6 = "a"
solution(s1)
solution(s2)
solution(s3)
solution(s4)
solution(s5)
solution(s6)
# print(result)
# print(len(s1))
