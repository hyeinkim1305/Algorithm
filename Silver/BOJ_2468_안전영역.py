'''
최소 높이 -1 부터 최대 높이-1까지 잠길때
'''
# 미로처럼 왔던 길을 막는 방식으로 하면 for문 돌릴 때 행렬이 초기 주어진 값과 달라지게 됨.
# 따라서 visited로 방문했었는지 확인!
def bfs(r, c):
    q = []
    q.append([r, c])
    vis[r][c] = 1

    while q:
        cur = q.pop(0)
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
                continue
            if sec[nr][nc] > k and vis[nr][nc] == 0:
                q.append([nr, nc])
                vis[nr][nc] = 1


N = int(input())
min_h = 98654   # 건물 최소 높이
max_h = 0       # 건물 최대 높이
sec = []        # 영역 2차원 배열
cnt = 0         # 안잠기는 안전한 영역
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = []        # 안잠기는 영역 개수
for i in range(N):
    s = list(map(int, input().split()))
    for j in s:
        if j > max_h:
            max_h = j
        if j < min_h:
            min_h = j
    sec.append(s)

for k in range(min_h-1, max_h):     # 최소높이 -1부터 최대높이 -1까지 한다
    vis = [[0 for _ in range(N)] for _ in range(N)]     # 방문 배열 초기화 해줘야함
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 시작점은 안잠기고 방문 안했던 거부터
            if sec[i][j] > k and vis[i][j] == 0:
                bfs(i, j)
                cnt += 1
    ans.append(cnt)

print(max(ans))


