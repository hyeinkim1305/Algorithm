
def perm(idx):
    if idx == M:
        print(*ans)
    else:
        for i in range(N):
            if vis[i] == 0:
                ans[idx] = arr[i]
                vis[i] = 1
                perm(idx+1)
                vis[i] = 0


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0] * M
vis = [0] * N
perm(0)

