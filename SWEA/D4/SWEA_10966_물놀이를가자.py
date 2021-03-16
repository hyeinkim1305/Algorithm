
from collections import deque
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(q):
    global ans
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
                continue
            if visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                ans += visited[nr][nc]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # q에 시작지점 넣어서 함수 돌리면 되는듯
    q = deque()
    ans = 0
    pool = [list(input()) for _ in range(N)]        # 2차원 배열 입력
    visited = [[-1] * M for _ in range(N)]      # 방문 배열
    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                q.append((i, j))        # 시작지점들 넣어주고
                visited[i][j] = 0
    bfs(q)
    print('#{} {}'.format(tc, ans))
