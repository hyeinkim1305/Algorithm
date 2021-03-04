'''
1
1111111111111111
1210000000100011
1010101110101111
1000100010100011
1111111010101011
1000000010101011
1011111110111011
1010000010001011
1010101111101011
1010100010001011
1010111010111011
1010001000100011
1011101111101011
1000100000001311
1111111111111111
1111111111111111

1
1
12101
10101
10101
10101
10031
'''

def dfs(r, c):
    arr[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
            continue
        if arr[nr][nc] == 3:
            return 1
        elif arr[nr][nc] == 0:
            if dfs(nr, nc) == 1:        # 이 부분 중요 !! 그냥 리턴하면 안됨
                return 1
    return 0

def bfs(r, c):
    q = []
    q.append([r, c])
    arr[r][c] = 1

    while q:
        cur = q.pop(0)
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
                continue
            if arr[nr][nc] == 3:
                return 1
            if arr[nr][nc] == 0:
                q.append([nr, nc])
                arr[nr][nc] = 1
    return 0


for _ in range(1, 10+1):
    tc = int(input())
    N = 16
    arr = [[int(x) for x in list(input())] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                R = i
                C = j

    # 상하좌우
    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]

    print('#{} {}'.format(tc, dfs(R, C)))
    # print('#{} {}'.format(tc, bfs(R, C)))

