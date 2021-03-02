
def is_num(n):
    oper = ['+', '*', '(', ')']
    if n in oper:
        return False
    else:
        return True

def prior(n):  # 스택의 top에 있는거 우선순위
    if n == '+': return 1
    elif n == '*': return 2
    elif n == '(': return 0

def inprior(n):  # 스택에 들어갈 연산자 우선순위
    if n == '+': return 1
    elif n == '*': return 2
    elif n == '(': return 3

T = 10
for tc in range(1, T+1):
    N = int(input())
    be = list(input())  # 중위
    af = []  # 후위로 바꾼거 들어갈 리스트
    stack = []  # 스택

    # 후위 표기법으로 변환
    for i in range(len(be)):
        if is_num(be[i]):  # 피연산자이면
            af.append(be[i])
        elif not is_num(be[i]):  # 연산자이면
            if be[i] == ')':  # 오른쪽괄호이면
                while stack[-1] != '(':  # 스택에서 pop한다
                    af.append(stack.pop(-1))
                if stack[-1] == '(':
                    stack.pop(-1)
            else:
                if len(stack) == 0:
                    stack.append(be[i])
                    continue
                if inprior(be[i]) > prior(stack[-1]):
                    stack.append(be[i])
                else:
                    while inprior(be[i]) <= prior(stack[-1]) and len(stack) != 0:
                        af.append(stack.pop(-1))
                        if len(stack) == 0:
                            break
                    stack.append(be[i])
    if len(stack) != 0:
        while len(stack) != 0:
            af.append(stack.pop(-1))


    # 계산
    for j in range(len(af)):
        if is_num(af[j]):  # 피연산자이면
            stack.append(af[j])
        elif not is_num(af[j]):  # 연산자이면
            a = stack.pop()
            b = stack.pop()
            if af[j] == '+':
                stack.append(int(b)+int(a))
            elif af[j] == '*':
                stack.append(int(b)*int(a))
    print('#{} {}'.format(tc, stack[-1]))



