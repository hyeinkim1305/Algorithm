
# 동서북남 + order와 대응시키기
dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]

def game():
    global r
    global c

    for i in range(K):
        # 주사위 좌표는 초기에 0, 0
        nr = r + dr[order[i] - 1]  # 인덱스땜에 -1 해줌
        nc = c + dc[order[i] - 1]

        if nr < 0 or nr > N - 1 or nc < 0 or nc > M - 1:
            continue
        if order[i] == 1:  # 동쪽
            dir[1], dir[2], dir[3], dir[5] = dir[5], dir[1], dir[2], dir[3]     # 바뀐 위치 대응시키기
        elif order[i] == 2:
            dir[1], dir[2], dir[3], dir[5] = dir[2], dir[3], dir[5], dir[1]
        elif order[i] == 3:
            dir[0], dir[2], dir[4], dir[5] = dir[2], dir[4], dir[5], dir[0]
        elif order[i] == 4:
            dir[0], dir[2], dir[4], dir[5] = dir[5], dir[0], dir[2], dir[4]

        if arr[nr][nc] == 0:
            arr[nr][nc] = dir[2]
        elif arr[nr][nc] != 0:
            dir[2] = arr[nr][nc]
            arr[nr][nc] = 0
        r, c = nr, nc

        print(dir[5])

# 세로, 가로, x, y, 명령개수
N, M, r, c, K = map(int, input().split())
# 지도
arr = [list(map(int, input().split())) for _ in range(N)]
# 명령 / 동서북남 1234
order = list(map(int, input().split()))
# 주사위
dir = [0] * 6

game()



