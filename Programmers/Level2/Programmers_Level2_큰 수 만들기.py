
# 스택에 넣어서 값을 비교하며 제거한다.
def solution(number, k):
    stack = [number[0]]

    for i in number[1:]:
        while stack and stack[-1] < i and k > 0:
            stack.pop(-1)
            k -= 1
        stack.append(i)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)