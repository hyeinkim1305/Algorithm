
def perm(idx):
    if idx == M:
        print(*ans)
    else:
        for i in range(N):
            ans[idx] = n[i]
            perm(idx+1)


N, M = map(int, input().split())
ans = [0] * M
n = [i for i in range(1, N+1)]
perm(0)
