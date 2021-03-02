'''
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
'''
def is_num(n):
    notnum = ['+','*','-','/']
    if n in notnum:
        return False
    elif n not in notnum:
        return True

def cal(s, stack):
    for i in range(len(s)):
        if s[i] == '.':
            if len(stack) != 1:
                return 'error'
            answer = stack[-1]
            return answer
        elif is_num(s[i]):  # 숫자이면
            stack.append(s[i])
            continue
        elif is_num(s[i]) == False:  # 연산자이면
            cnt = 0
            for j in stack:   # 연산자들만 들어있을 수도 있으니
                if is_num(j):
                    cnt += 1
            if cnt < 2:
                return 'error'
            a = stack.pop()
            b = stack.pop()
            if s[i] == '+':
                stack.append(int(b) + int(a))
                continue
            elif s[i] == '*':
                stack.append(int(b) * int(a))
                continue
            elif s[i] == '-':
                stack.append(int(b) - int(a))
                continue
            else:
                stack.append(int(b) // int(a))
                continue



T = int(input())
for tc in range(1, T+1):
    s = input().split()  # 입력
    stack = []  # 스택

    print('#{} {}'.format(tc, cal(s, stack)))


