
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, num, cnt):
    global max_room, room_num

    if cnt > max_room:      # 이동한 게 최대 방 개수보다 크다면
        max_room, room_num = cnt, num
    elif cnt == max_room:       # 같은데
        if num < room_num:      # 시작 방번호가 더 작다면
            room_num = num

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <= N-1 and 0 <= nc <= N-1:
            if arr[nr][nc] == arr[r][c] + 1:        # 1이 더 크다면
                dfs(nr, nc, num, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_room, room_num = -1, -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j], 1)        # 시작r인덱스, c인덱스, 시작방번호, 방이동개수

    print(f'#{tc} {room_num} {max_room}')
