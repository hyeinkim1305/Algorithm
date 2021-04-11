
def in_order(idx):
    global cnt
    if idx <= N:
        in_order(idx*2)
        tree[idx] = cnt
        cnt += 1
        in_order(idx*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    in_order(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))




