
# D3
# 상하좌우
### 왜 q랑 vis쓰니까 안되지??
### 아 이거 전에 푼 최소 신장 트리는 배열을 다시 탐색하면서 길이가 최소인 지점에서 시작하는데
### 이 문제는 2차원 배열을 다 탐색하니까 너무 오래 걸림! 시간 초과 발생! 그래서 q에 담는대신 visited 배열을 없애줘서
### 중복검사를 가능케하는듯! 아마도?

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def Dijkstra(H, r, c):
    d = [[float("inf")] * N for _ in range(N)]            # 그 지점까지의 최단 경로 길이 합
    # vis = [[0] * N for _ in range(N)]           # 방문 배열
    d[r][c] = 0
    q = [(r, c)]

    while q:
        min_r, min_c = q.pop(0)
        ### 이거 말고 큐로 대체! -> 매번 탐색하면 시간이 오래 걸릴듯!!
        # min_r, min_c = -1, -1
        # min_d = float("inf")
        # for i in range(N):
        #     for j in range(N):
        #         if vis[i][j] == 0 and d[i][j] < min_d:
        #             min_d = d[i][j]
        #             min_r = i
        #             min_c = j

        # vis[min_r][min_c] = 1
        for k in range(4):
            ni = min_r + dr[k]
            nj = min_c + dc[k]
            if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                continue
            # if not vis[ni][nj]:
            temp = H[ni][nj] - H[min_r][min_c]
            if temp > 0:            # 더 높은 곳으로 올라가는 경우
                if d[min_r][min_c] + 1 + temp < d[ni][nj]:
                    d[ni][nj] = d[min_r][min_c] + 1 + temp
                    q.append((ni, nj))
            else:
                if d[min_r][min_c] + 1 < d[ni][nj]:
                    d[ni][nj] = d[min_r][min_c] + 1
                    q.append((ni, nj))
    return d[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, Dijkstra(H, 0, 0)))



'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''