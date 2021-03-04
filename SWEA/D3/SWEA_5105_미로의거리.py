
'''
출발은 3, 도착은 2로
'''

def bfs(r, c):
    q = []
    q.append([r, c])    # 큐에 추가
    arr[r][c] = '0'   # 시작정점 막아버리기 str 형태로

    while q:
        cur = q.pop(0)
        for i in range(4):  # 네 방향 탐색
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]

            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:    # 범위 못 넘어가게
                continue
            elif arr[nr][nc] == 0:    # 통로라면 큐에 추가하고 막아버리기
                q.append([nr, nc])
                d = str(int(arr[cur[0]][cur[1]])+1)     # str형태로 막기
                arr[nr][nc] = d

            elif arr[nr][nc] == 2:
                d = int(arr[cur[0]][cur[1]])
                return d
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dis = [[0 for _ in range(N)] for _ in range(N)]     # 거리체크
    arr = [[int(x) for x in list(input())] for _ in range(N)]
    for i in range(N):      # 3인곳 찾기
        for j in range(N):
            if arr[i][j] == 3:
                R = i
                C = j
    # 상하좌우
    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]

    print('#{} {}'.format(tc, bfs(R, C)))


