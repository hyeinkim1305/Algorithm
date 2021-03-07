
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, +1]

def dfs(r, c):
    dist = 1
    q = []
    q.append([r, c])
    arr[r][c] = dist

    while q:
        cur = q.pop(0)

        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
                continue
            if nr == N-1 and nc == M-1:
                dist = arr[cur[0]][cur[1]] + 1
                return dist

            if arr[nr][nc] == '1':
                dist = arr[cur[0]][cur[1]] + 1
                q.append([nr, nc])
                arr[nr][nc] = dist



N, M = map(int, input().split())
arr = []
for i in range(N):
    a = list(input())
    arr.append(a)

# 도착점 N * M
print(dfs(0, 0))












