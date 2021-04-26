'''
올바른 문자열인지 판단하는 함수, 문자열 나누는 함수 이렇게 2가지 필요
조건 2에서 조건 3, 4로 다시 나뉘는 것!
'''


# 올바른 문자열인지 판단
def right(p):
    stack = []
    for i in p:
        if not stack:
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
        elif i == '(':
            stack.append(i)
    if not stack:
        return True
    else:
        return False


# 문자열 나누기
def divide(p):
    # 조건 1
    if not p:
        return p
    # 조건 2
    opens, closes = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            opens += 1
        else:
            closes += 1
        if opens == closes:
            return p[:i + 1], p[i + 1:]


def solution(p):
    # 조건 1
    if not p:
        return p
    # 조건 2
    u, v = divide(p)

    # 조건 3
    if right(u):
        return u + solution(v)

    # 조건 4
    if not right(u):
        s = '('
        s += solution(v)
        s += ')'
        u = u[1:-1]
        for i in u:
            if i == ')':
                s += '('
            else:
                s += ')'
        return s
