
# 연산자 우선순위 경우의 수
def perm(idx, arr, sel, vis, oper):
    if idx == 3:
        arr.append(sel[:])
        return
    for i in range(3):
        if vis[i] == 0:
            vis[i] = 1
            sel[idx] = oper[i]
            perm(idx+1, arr, sel, vis, oper)
            vis[i] = 0


def solution(expression):
    oper = ['*', '-', '+']
    vis = [0] * 3
    sel = [0] * 3
    max_num = -1

    arr = []
    # 1. 연산자, 피연산자 배열 만들기
    number = []
    signs = []
    start_i = 0
    for i in range(len(expression)):
        if expression[i] in oper:
            number.append(int(expression[start_i:i]))
            start_i = i+1
            signs.append(expression[i])
    number.append(int(expression[start_i:]))


    # 2. 경우의 수에 따라 따져보기
    # 연산자 종류가 3가지 일 때
    if len(set(signs)) == 3:
        perm(0, arr, sel, vis, oper)
        for i in range(6):
            num = number[:]
            sign = signs[:]
            for k in range(2, -1, -1):
                j = 0
                while arr[i][k] in sign and j < len(signs):
                    if sign[j] == arr[i][k]:
                        if sign[j] == '*':
                            temp = num[j] * num[j+1]
                            num[j+1] = temp
                            num.pop(j)
                            sign.pop(j)
                            j = 0
                            continue
                        elif sign[j] == '-':
                            temp = num[j] - num[j+1]
                            num[j+1] = temp
                            num.pop(j)
                            sign.pop(j)
                            j = 0
                            continue
                        elif sign[j] == '+':
                            temp = num[j] + num[j+1]
                            num[j+1] = temp
                            num.pop(j)
                            sign.pop(j)
                            j = 0
                            continue
                    else:
                        j += 1

            if num[0] < 0:
                num = num[0] * (-1)
            else:
                num = num[0]
            if num > max_num:
                max_num = num
    # 연산자 종류가 2가지 일 때
    elif len(set(signs)) == 2:
        arr = []
        temp = list(set(signs))
        arr.append(temp[:])
        arr.append(temp[::-1])

        for i in range(2):
            num = number[:]
            sign = signs[:]
            for k in range(1, -1, -1):
                j = 0
                while arr[i][k] in sign and j < len(signs):
                    if sign[j] == arr[i][k]:
                        if sign[j] == '*':
                            temp = num[j] * num[j + 1]
                            num[j + 1] = temp
                            num.pop(j)
                            sign.pop(j)
                            j = 0
                            continue
                        elif sign[j] == '-':
                            temp = num[j] - num[j + 1]
                            num[j + 1] = temp
                            num.pop(j)
                            sign.pop(j)
                            j = 0
                            continue
                        elif sign[j] == '+':
                            temp = num[j] + num[j + 1]
                            num[j + 1] = temp
                            num.pop(j)
                            sign.pop(j)
                            j = 0
                            continue
                    else:
                        j += 1
            if num[0] < 0:
                num = num[0] * (-1)
            else:
                num = num[0]
            if num > max_num:
                max_num = num

    # 연산자 종류가 1가지 일 때
    elif len(set(signs)) == 1:
        num = number[:]
        sign = signs[:]
        for i in range(len(signs)):
            if sign[i] == '*':
                temp = num[i] * num[i+1]
                num[i+1] = temp
                num[i] = 0

            if sign[i] == '-':
                temp = num[i] - num[i+1]
                num[i+1] = temp
                num[i] = 0

            if sign[i] == '+':
                temp = num[i] + num[i+1]
                num[i+1] = temp
                num[i] = 0
        max_num = num[-1]
        if max_num < 0:
            max_num = max_num * (-1)

    return max_num






# expression = "2-990-5+2"
# expression = "50*6-3*2"
# expression = "100-200*300-500+20"
# expression = "100-200-20-5"
# expression = "5-2"
expression = "0*8-5*0"
# expression = "100-200-20-5"

solution(expression)

'''
[['*', '-', '+'], ['*', '+', '-'], ['-', '*', '+'], ['-', '+', '*'], ['+', '*', '-'], ['+', '-', '*']]
[100, 200, 300, 500, 20]
['-', '*', '-', '+']
'''



'''
1) 중위표기법을 후위표기법으로 변경
토큰이 피연산자이면 after에 담는다
토큰이 연산자일 때, 스택이 비어있으면 스택에 push
                스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push
                우선순위가 높지 않다면 스택 top의 연산자의 우선순위가 작아질 때까지 스택에서 pop한 후 push
                top에 연산자가 없으면 push
스택에 남아있는 것들을 다 pop하여 after에 넣는다

2) 후위표기법 계산
피연산자 만나면 스택에 push
연산자를 만나면 스택에서 피연산자를 pop하여 연산. (두번째로 pop한걸 앞에 두고 계산)연산결과를 다시 스택에 push
수식이 끝나면 마지막으로 스택을 pop하여 출력
'''