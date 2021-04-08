
# 벽세우기
def wall(cnt):
    global max_safe
    if cnt == 3:
        safe_cnt = virus_func(board)
        if safe_cnt > max_safe:
            max_safe = safe_cnt
        return
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    wall(cnt+1)
                    board[i][j] = 0


def virus_func(board):       # 바이러스 퍼지느거 dfs
    global new_board

    # virus위치랑 board 복사 (위 함수에서 재귀때문에)
    for i in range(N):
        for j in range(M):
            new_board[i][j] = board[i][j]
    q = []
    for i in range(len(virus)):
        q.append(virus[i])
        
    while q:
        cur = q.pop(0)
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
                continue
            if new_board[nr][nc] == 0:
                new_board[nr][nc] = 2
                q.append([nr, nc])
    # 안전영역 개수 세기
    safe = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                safe += 1
    return safe


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())

# 바이러스 위치 찾고 board 입력 받기
virus = []
board = []
for i in range(N):
    b = list(map(int, input().split()))
    for j in range(M):
        if b[j] == 2:
            virus.append([i, j])
    board.append(b)
new_board = [[0]*M for _ in range(N)]
max_safe = -1
wall(0)
print(max_safe)