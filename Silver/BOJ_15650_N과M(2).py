
def perm(idx):
    global k
    if idx == M:
        print(*ans)
    else:
        for i in range(k, N):
            if sel[i] == 0:
                ans[idx] = arr[i]
                sel[i] = 1
                k = i
                perm(idx+1)
                sel[i] = 0

N, M = map(int, input().split())
sel = [0] * N
ans = [0] * M
arr = [i for i in range(1, N+1)]
k = 0
perm(0)

