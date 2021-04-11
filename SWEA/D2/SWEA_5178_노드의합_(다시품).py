
# sol1
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    idx = N
    while idx:
        if idx % 2:
            tree[idx//2] = tree[idx] + tree[idx-1]
        if idx % 2 == 0 and idx == N:
            tree[idx//2] = tree[idx]
        idx -= 1

    print(f'#{tc} {tree[L]}')



# sol2
def post_order(idx):
    if idx <= N:
        left_sum = post_order(idx*2)
        right_sum = post_order(idx*2+1)
        tree[idx] = tree[idx] + left_sum + right_sum
        return tree[idx]
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        index, value = map(int, input().split())
        tree[index] = value

    post_order(1)
    print('#{} {}'.format(tc, tree[L]))