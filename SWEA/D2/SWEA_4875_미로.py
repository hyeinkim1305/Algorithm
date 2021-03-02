
def find(start_r, start_c):
    if start_r == end_r and start_c == end_c:  # 도착점 찾음
        return 1
    else:
        for i in range(4):  # 4방향 탐색
            if start_r+dr[i] < 0 or start_r+dr[i] > N-1 or start_c+dc[i] < 0 or start_c+dc[i] > N-1:
                continue
            if road[start_r+dr[i]][start_c+dc[i]] == '2':
                return 1
            if road[start_r+dr[i]][start_c+dc[i]] == '0' and visited[start_r+dr[i]][start_c+dc[i]] == 0:
                visited[start_r+dr[i]][start_c+dc[i]] = 1
                if find(start_r+dr[i], start_c+dc[i]) == 1:   # 전에 1로 리턴되었다면
                    return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = []  # 전체 길 2차원 배열
    for i in range(N):
        r = list(input())
        for j in range(N):
            if r[j] == '3':  # 3이 있는 곳 위치 인덱스
                start_r = i
                start_c = j
            if r[j] == '2':  # 2가 있는 곳 위치 인데스
                end_r = i
                end_c = j
        road.append(r)
    visited = [[0 for _ in range(N)] for _ in range(N)]

    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]

    ans = find(start_r, start_c)
    print('#{} {}'.format(tc, ans))
