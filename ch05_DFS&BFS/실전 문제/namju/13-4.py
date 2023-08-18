from collections import deque

# 균형잡힌 괄호인지 확인
def isBalance(p):
    if p.count('(') == p.count(')'):
        return True
    return False

# 올바른 괄호인지 확인
def isRight(p):
    p = list(p)
    deq = deque()
    for c in p:
        if c == ')':
            if len(deq)==0:
                return False
            deq.popleft()
        else:
            deq.append(c)
    print(deq)
    if len(deq)>0:
        return False
    return True
def solution(p):
    answer = ''
    # 균형잡힌 문자열인지 확인
    if isBalance(p):
        if isRight(p):
            return p
        else:
            u = q
    return answer

print(solution("(()())()"))
print(solution(")("))
# print(solution("()))((()"))