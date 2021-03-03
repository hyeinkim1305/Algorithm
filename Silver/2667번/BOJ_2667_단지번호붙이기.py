
def dfs(n, m):
    global cnt
    apart[n][m] = 0  # 지나온 곳 0으로 바꿔도됨. 중요한건 단지 수 이므로!
    cnt += 1
    for k in range(4):
        nr = n + dr[k]
        nc = m + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if apart[nr][nc] == '1':
            dfs(nr, nc)

N = int(input())
apart = [list(input()) for _ in range(N)]
home = []   # 단지 내 집의 수

# 상하좌우
dr = [-1, +1, 0, 0]
dc = [0, 0, -1, +1]

# 탐색 시작점 찾기
for i in range(N):
    for j in range(N):
        if apart[i][j] == '1':
            cnt = 0
            dfs(i, j)
            home.append(cnt)


print(len(home))  # 총 단지수
home.sort()
for h in home:
    print(h)




