
def perm(idx):
    if idx == M:
        print(*ans)
    else:
        for i in range(N):
            if sel[i] == 0:     # 방문 안한거
                ans[idx] = arr[i]
                sel[i] = 1
                perm(idx+1)
                sel[i] = 0

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
sel = [0] * N
ans = [0] * M
perm(0)


