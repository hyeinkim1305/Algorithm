#
import sys
from collections import deque
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([Sr-1, Sc-1])
    visited[Sr-1][Sc-1] = 1         # 가장 왼쪽 맨 위 좌표만 방문 배열에 기록

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (nr < 0 or nr > N - H or nc < 0 or nc > M - W) or (visited[nr][nc] != 0) or (arr[nr][nc] == 1):
                continue
            if wall[nr][nc] == 0:                             # 벽이 겹치는 시작점이 아니라면 정사각형 만큼 순회안하고 바로 아래 코드
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1           # 횟수 세기
                if nr == Fr - 1 and nc == Fc - 1:
                    return visited[nr][nc] - 1
    return -1


N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
wall = [[0] * M for _ in range(N)]
# 벽이 겹치는 시작점들을 미리 표시해놓기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            for k in range(H):
                for l in range(W):
                    if i-k >= 0 and i-k <= N-1 and j-l >= 0 and j-l<= M-1:
                        wall[i-k][j-l] = 1
print(bfs())




# 시간 초과 -> 각 시작점마다 정사각형 크기만큼 순회하며 1이 있는지 확인함
# import sys
# from collections import deque
# # 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
#
# def bfs():
#     q = deque()
#     q.append([Sr-1, Sc-1])
#     visited[Sr-1][Sc-1] = 1         # 가장 왼쪽 맨 위 좌표만 방문 배열에 기록
#
#     while q:
#         r, c = q.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if (nr < 0 or nr > N - H or nc < 0 or nc > M - W) or (visited[nr][nc] != 0) or (arr[nr][nc] == 1):
#                 continue
#             sum_arr = 0
#             for j in range(H):
#                 for k in range(W):
#                     sum_arr += arr[nr+j][nc+k]
#             if sum_arr == 0:
#                 q.append([nr, nc])
#                 visited[nr][nc] = visited[r][c] + 1           # 횟수 세기
#                 if nr == Fr - 1 and nc == Fc - 1:
#                     return visited[nr][nc] - 1
#     return -1
#
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
# print(bfs())
