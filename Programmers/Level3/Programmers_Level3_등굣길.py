'''
모든 경로를 탐색하는 최단거리가 아니라
최단 경로의 개수이기 때문에 DP로 풀어야한다.
문제를 제대로 읽자!
+ 왼쪽과 위쪽에서 오므로 전체 행렬의 좌, 상쪽에 여분의 행렬을 만들어둔다.
'''


def solution(m, n, puddles):
    arr = [[0] * (m + 1) for _ in range(n + 1)]
    arr[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                continue
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    answer = arr[n][m] % 1000000007
    return answer

# # 오른쪽, 아래
# dr = [0, 1]
# dc = [1, 0]


# def bfs(r, c, d, arr, n, m):
#     q = [[r, c, d]]

#     while q:
#         cur = q.pop(0)
#         for i in range(2):
#             nr = cur[0] + dr[i]
#             nc = cur[1] + dc[i]
#             if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1:
#                 continue
#             if arr[nr][nc] == 0:
#                 if nr == n - 1 and nc == m - 1:
#                     answer = (cur[2]) % 1000000007
#                     return answer
#                 else:
#                     q.append([nr, nc, cur[2] + 1])


# def solution(m, n, puddles):
#     # 이차원 배열 만들기
#     arr = [[0] * m for _ in range(n)]
#     # 물웅덩이 표시
#     for p in puddles:
#         arr[p[0] - 1][p[1] - 1] = 1
#     # 시작점 0, 0
#     answer = bfs(0, 0, 0, arr, n, m)

#     return answer