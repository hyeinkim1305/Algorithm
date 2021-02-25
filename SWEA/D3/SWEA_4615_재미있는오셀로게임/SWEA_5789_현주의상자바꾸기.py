'''
1
5 2
1 3
2 4
'''
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    pos = [list(map(int, input().split())) for _ in range(Q)]
    box = [0] * (N+1)

    for i in range(Q):
        for j in range(pos[i][0], pos[i][1]+1):
            box[j] = i+1
    box = box[1:]

    print('#{}'.format(tc), end = " ")
    for k in box:
        print(k, end = " ")
    print()    # 이거 넣어줘야함 !!! 또는 box안에 요소들 str 형태로 해서 join 할 수도 있음
