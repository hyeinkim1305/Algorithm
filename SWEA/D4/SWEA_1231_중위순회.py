'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''
def in_order(idx):
    global ans
    if idx:
        in_order(tree[idx][0])
        ans += alpha[idx]
        in_order(tree[idx][2])


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]
    alpha = [0] * (N+1)               # 알파벳 넣을거
    for _ in range(N):
        case = list(input().split())
        # i = 0
        # for i in range()
        #     alpha[case[i]] = case[i+1]
        if len(case) == 2:
            alpha[int(case[0])] = case[1]
        elif len(case) == 3:
            alpha[int(case[0])] = case[1]
            tree[int(case[0])][0] = int(case[2])
        elif len(case) == 4:
            alpha[int(case[0])] = case[1]
            tree[int(case[0])][0] = int(case[2])
            tree[int(case[0])][2] = int(case[3])
    ans = ''
    in_order(1)
    print('#{} {}'.format(tc, ans))


'''
for i in range(N):
        tmp = list(input().split())
        if len(tmp) == 2:
            tree[int(tmp[0])] = [0, tmp[1], 0]
        elif len(tmp) == 3:
            tree[int(tmp[0])] = [int(tmp[2]), tmp[1], 0]
        elif len(tmp) == 4:
            tree[int(tmp[0])] = [int(tmp[2]), tmp[1], int(tmp[3])]
'''