'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65
'''


def post_order(idx):        # 후위방식
    global num
    if idx:         # 인덱스가 0이 아닐 때
        post_order(tree[idx][0])        # 자식 왼쪽 노드가 있으면 거기로 간다
        post_order(tree[idx][2])

        if tree[idx][1] in ['+', '-', '/', '*']:
            a = num.pop()
            b = num.pop()
            oper = tree[idx][1]
            if oper == '+':
                num.append(b+a)     # 뒤에서부터 꺼냈기때무네 b먼저 다음 a
            elif oper == '-':
                num.append(b-a)
            elif oper == '/':
                num.append(b/a)
            elif oper == '*':
                num.append(b*a)
        else:
            num.append(tree[idx][1])


for tc in range(1, 10+1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]

    # 트리만들기
    for i in range(1, N+1):
        temp = input().split()
        if len(temp) == 4:
            tree[int(temp[0])][1] = temp[1]
            tree[int(temp[0])][2] = int(temp[3])
            tree[int(temp[0])][0] = int(temp[2])
        elif len(temp) == 2:
            tree[int(temp[0])][1] = int(temp[1])

    num = []
    post_order(1)

    print('#{} {}'.format(tc, int(num[0])))

