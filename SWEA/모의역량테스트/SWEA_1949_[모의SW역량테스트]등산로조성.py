
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, use, dist):
    global max_dist
    dist += 1       # 거리는 dist로 해준다
    if dist > max_dist:
        max_dist = dist

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
            continue
        if visited[nr][nc] == 0 and path[nr][nc] < path[r][c] and use != 0:
            visited[nr][nc] = 1
            dfs(nr, nc, use, dist)
            visited[nr][nc] = 0     # 원상복귀 과정 필요
        elif visited[nr][nc] == 0 and path[nr][nc] - K < path[r][c] and use != 0:
            visited[nr][nc] = 1
            ori = path[nr][nc]      # 원래 값 저장해야해
            path[nr][nc] = path[r][c] - 1       # 한 칸만 다운시켜도 된다
            use -= 1
            dfs(nr, nc, use, dist)
            path[nr][nc] = ori      # 아래는 원상복귀 과정
            visited[nr][nc] = 0
            use = 1
        elif visited[nr][nc] == 0 and path[nr][nc] < path[r][c] and use == 0:
            visited[nr][nc] = 1
            dfs(nr, nc, use, dist)
            visited[nr][nc] = 0



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    path = []
    max_path = []
    max_p = -1
    for i in range(N):      # 최대값 찾기, 위치찾기, 지도 이차원배열 생성
        p = list(map(int, input().split()))
        if max(p) > max_p:
            max_p = max(p)
            max_path = []
            for j in range(N):
                if p[j] == max(p):
                    max_path.append([i, j])
        elif max(p) == max_p:
            for j in range(N):
                if p[j] == max(p):
                    max_path.append([i, j])     # [[0, 1], [1, 0], [1, 2], [2, 1]]
        path.append(p)

    ans = []
    for k in range(len(max_path)):
        dist = 0
        use = 1
        max_dist = -1
        visited = [[0] * N for _ in range(N)]
        visited[max_path[k][0]][max_path[k][1]] = 1
        dfs(max_path[k][0], max_path[k][1], use, dist)
        ans.append(max_dist)

    print('#{} {}'.format(tc, max(ans)))







