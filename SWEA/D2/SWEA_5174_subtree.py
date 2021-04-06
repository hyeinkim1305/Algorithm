'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

'''
def pre_order(idx):         # 전위순회
    global cnt
    if idx:
        cnt += 1
        pre_order(child1[idx])
        pre_order(child2[idx])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    child1 = [0] * (E+2)            #인덱스 0~6
    child2 = [0] * (E+2)
    pair = list(map(int, input().split()))
    for i in range(len(pair)):
        if i % 2 == 0:          # 인덱스가 짝수인게 부모일때
            if not child1[pair[i]]:
                child1[pair[i]] = pair[i+1]
            elif child1[pair[i]]:
                child2[pair[i]] = pair[i+1]
    cnt = 0
    pre_order(N)
    print('#{} {}'.format(tc, cnt))

