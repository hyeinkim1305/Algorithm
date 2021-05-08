
def solution(s):
    # 스택
    stack = []
    for i in range(len(s)):
        # 스택이 비어있다면
        if not stack:
            stack.append(s[i])
        # 맨 위에 들어있는거랑 같다면 pop
        elif stack[-1] == s[i]:
            stack.pop(-1)
        elif stack[-1] != s[i]:
            stack.append(s[i])

    if not stack:
        answer = 1
    elif stack:
        answer = 0

    return answer
