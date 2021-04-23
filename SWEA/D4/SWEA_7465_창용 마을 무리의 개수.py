
# D4
def find_set(x):            # 부모 찾는 것
    while p[x] != x:
        x = p[x]
    return x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]                 # 미리 세팅

    for j in range(M):
        u, v = map(int, input().split())
        p[find_set(v)] = find_set(u)            # 합치기
    cnt = 0

    for k in range(1, N+1):
        if k == p[k]:
            cnt += 1                # 자기자신이 대표인 무리 세어주기
    print('#{} {}'.format(tc, cnt))
