

def perm(idx):
    global j

    if idx == M:
        print(*ans)
    else:
        for i in range(j, N):
            j = i
            ans[idx] = n[i]
            perm(idx + 1)


N, M = map(int, input().split())
n = [i for i in range(1, N+1)]
ans = [0] * M
j = 0
perm(0)

