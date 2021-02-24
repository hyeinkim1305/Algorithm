def number(n):  # 피연산자인지 확인
    if n not in operator:
        return True
    else:
        return False

def prio(n):  # 우선순위 확인
    if n == '+': return 1
    elif n == '*': return 2

T = 10
for tc in range(1, T+1):
    N = int(input())  # 테스트케이스 길이
    after = []  # 후위로 바꾼거 넣는 리스트
    before = list(input())  # 중위
    stack = []
    operator = ['+','*']

    # 중위 -> 후위로 변환환
    for i in range(len(before)):
        if number(before[i]):  # 피연산자이면
            after.append(before[i])
        elif not number(before[i]):  # 피연산자 아니면
            if len(stack) == 0:  # 만약 스택이 비어있으면
                stack.append(before[i])
                continue
            if prio(before[i]) > prio(stack[-1]):  # 스택에 넣으려는 연산자가 탑에 있는 연산자보다 우선순위 높으면
                stack.append(before[i])
            else:
                while len(stack) != 0 and prio(before[i]) <= prio(stack[-1]):  # 스택이 안 비어있고 우선순위 안높으면
                    after.append(stack.pop(-1))
                stack.append(before[i])
    if len(stack) != 0:   # 스택이 빌 때 까지 after에 추가
        while len(stack) != 0:
            after.append(stack.pop(-1))

    stack = []
    ans = 0
    # 후위표기법 수식을 스택 이용해 계산
    for i in range(len(after)):
        if number(after[i]):  # 피연산자라면 스택에 추가
            stack.append(after[i])
        elif not number(after[i]):  # 연산자라면
            if after[i] == '+':  # +라면 아래와 같이 시행
                first = stack.pop(-2)
                second = stack.pop(-1)
                out = (int(first)+int(second))
                stack.append(out)
            elif after[i] == '*':  # *라면 아래와 같이 시행
                first = stack.pop(-2)
                second = stack.pop(-1)
                out = (int(first) * int(second))
                stack.append(out)
    ans = stack[0]
    print('#{} {}'.format(tc, ans))





