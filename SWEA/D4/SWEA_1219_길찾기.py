
def road(n):
    visited[n] = 1
    for i in range(100):
        if arr[n][i] == 1 and visited[i] == 0:
            road(i)

for tc in range(1, 11):
    tc, E = map(int, input().split())
    edge = list(map(int, input().split()))
    arr = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0] * 100

    for i in range(E):
        n1, n2 = edge[i*2], edge[i*2+1]
        arr[n1][n2] = 1

    road(0)
    if visited[0] == 1 and visited[99] == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')






