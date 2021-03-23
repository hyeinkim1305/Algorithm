'''
벽을 하나씩 채우고 3개가 되면
bfs로 바이러스 퍼뜨리기
안전영역 개수 세기
'''
def wall(cnt):  # 이거 생각 좀 걸림
    global max_area
    if cnt == 3:
        ans = virus()
        if ans > max_area:
            max_area = ans
        return
    else:
        for i in range(N):
            for j in range(M):
                if area[i][j] == 0:
                    area[i][j] = 1
                    wall(cnt + 1)
                    area[i][j] = 0

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 방문배열 만드는거 보다는 copy해서 쓰는 것이 나을듯?
def virus():
    # 복사 / 원본변형 안되게
    q = []
    area2 = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            area2[i][j] = area[i][j]
            if area[i][j] == 2:
                q.append([i, j])
    while q:
        if len(q) == 0:
            break
        cur = q.pop(0)

        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N - 1 or nc < 0 or nc > M - 1:
                continue
            if area2[nr][nc] == 0:
                area2[nr][nc] = 2
                q.append([nr, nc])

    safe = 0
    for i in range(N):
        for j in range(M):
            if area2[i][j] == 0:
                safe += 1

    return safe


N, M = map(int, input().split())        # 세로, 가로
area = [list(map(int, input().split())) for _ in range(N)]
max_area = -123456789

wall(0)
print(max_area)







