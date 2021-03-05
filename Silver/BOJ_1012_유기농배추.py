'''
일반적인 미로 문제랑 다른 점
: 이거는 시작점도 계속 찾아줘야 한다.
'''
# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c):      # 배추 찾기
    q = []
    q.append([r, c])
    arr[r][c] = 0       # 0으로 막아주기

    while q:
        cur = q.pop(0)
        for i in range(4):
            nr = cur[0] + dx[i]     # 여기 pop한거로 하는거 주의!
            nc = cur[1] + dy[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
                continue
            if arr[nr][nc] == 1:
                q.append([nr, nc])
                arr[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    cnt = 0         # 지렁이 수
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):     # 인접행렬 만들기
        u, v = map(int, input().split())
        arr[v][u] = 1
    for i in range(N):      # 시작점 찾기
        for j in range(M):
            if arr[i][j] == 1:
                R = i
                C = j
                bfs(R, C)
                cnt += 1

    print(cnt)














