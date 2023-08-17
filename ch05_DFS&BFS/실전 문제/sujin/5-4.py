# # 
## 5-4 괄호 변환

## Solution

### 문제의 아이디어 생각해낸 포인트
# 
### 시간 복잡도 계산
# A. 

### 소요시간
# 3:40 ~

# 문자열 올바른지 판단 함수 
def is_correct(string):
    cnt = 0
    for i in string:
        if i == '(': cnt += 1
        else: cnt -= 1

        if cnt < 0:
            return False
    return True

def seperate(string):
    cnt = 0
    # 분리하기
    for idx in range(len(string)):
        if string[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = string[:idx+1]
            v = string[idx+1:]
            return u, v
    
def solution(string):
    
    if len(string) == 0:
        return ""
    u, v = seperate(string)
    
    # u 처리
    # 문자가 올바를 경우
    if is_correct(u):
        return u + solution(v)
 
    # 문자가 올바르지 않을 경우
    else:
        update_string = "(" + solution(v) + ")"
        
        u = u[1:-1]
        for c in u:
            if c =='(':
                update_string += ')'
            else:
                update_string += '('
    
    return update_string
    
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
            
    
