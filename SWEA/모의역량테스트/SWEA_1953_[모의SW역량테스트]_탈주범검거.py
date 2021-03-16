# 1포함, 2포함 가능
# 칸 수를 세면 되는듯
# 파이프가 이어져있는지 확인 필요
'''
아이디어
나는 파이프가 연결된 걸 어떻게 확인할 지 고민했는데,
고려할 방향이 x라면 옮겨갈 칸의 파이프가 (x+2)%4 방향을
갖고 있으면 된다는 힌트를 얻음!
(파이프 방향:상우하좌 (1230) 시계방향)
방향이 총 4개이니까
-> bfs 탐색하면서 방문한 곳들의 개수 세주면 될 듯
'''

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs(r, c):
    q = []
    q.append([r, c])
    visited[r][c] = 1
    spot = 1
    while q:
        cur = q.pop(0)
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > M-1: continue
            if tunnel[nr][nc] != 0 and visited[nr][nc] == 0:
                if type[tunnel[cur[0]][cur[1]]][i] != -1:       # 해당 방향꺼가 있으면
                    ori = (type[tunnel[cur[0]][cur[1]]][i] + 2) % 4    # 기존꺼
                    new = type[tunnel[nr][nc]]
                    if ori in new:      # 맞아야 하는 방향이 들어있으면
                        q.append([nr, nc])      # 큐에 추가
                        visited[nr][nc] = visited[cur[0]][cur[1]] + 1

                        if visited[nr][nc] == L + 1:
                            return spot
                        spot += 1
    return spot


T = int(input())
# 구조물 타입 숫자는 인덱스랑 맞춤 + 상우하좌 1230
type = [[], [1,2,3,0], [1,-1,3,-1], [-1,2,-1,0], [1,2,-1,-1], [-1,2,3,-1], [-1,-1,3,0], [1,-1,-1,0]]
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]     # 방문배열(방문했는지 + 거리표기)
    print('#{} {}'.format(tc, bfs(R, C)))

