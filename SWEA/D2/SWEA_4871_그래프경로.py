'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6

7 4
1 6
2 3
2 6
3 5
2 5

'''

def dfs(n):
    visited[n] = 1
    for i in range(1, V+1):
        if arr[n][i] == 1 and visited[i] == 0:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1
    S, G = map(int, input().split())
    visited = [0] * (V+1)

    dfs(S)
    if visited[S] == 1 and visited[G] == 1:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))





