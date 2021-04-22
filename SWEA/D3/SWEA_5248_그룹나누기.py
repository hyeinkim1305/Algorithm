
# D3
# vis 만들고, dfs

def dfs(idx):
    vis[idx] = 1
    for k in arr[idx]:
        if vis[k] == 0:
            dfs(k)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    arr = [[] for _ in range(N+1)]
    vis = [0] * (N+1)
    for i in range(M):
        arr[number[i*2]].append(number[i*2+1])
        arr[number[i*2+1]].append(number[i*2])

    answer = 0
    for j in range(1, N+1):
        if vis[j] == 0:
            dfs(j)
            answer += 1

    print('#{} {}'.format(tc, answer))


