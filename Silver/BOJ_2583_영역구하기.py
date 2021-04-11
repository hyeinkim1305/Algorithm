
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global cnt
    global ans

    q = [[r, c]]
    board[r][c] = 1
    cnts = 1

    while q:
        cur = q.pop(0)
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > M-1 or nc < 0 or nc > N-1:
                continue
            if board[nr][nc] == 0:
                q.append([nr, nc])
                board[nr][nc] = 1
                cnts += 1
    cnt += 1
    ans.append(cnts)



M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(M-y2, M-y1):
        for k in range(x1, x2):
            board[j][k] = 1             # 정사각형 자리는 1로 채우기

cnt = 0       # 분리된 영역 개수
ans = []        # 분리된 영역들의 넓이 리스트

# bfs
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            bfs(i, j)

print(cnt)
ans = sorted(ans)
print(*ans)
