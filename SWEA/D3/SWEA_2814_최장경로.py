
# D3
# 두 정점 사이에 여러 개의 간선 존재?

def dfs(idx, cnt):
    global max_cnt
    vis[idx] = 1

    if cnt > max_cnt:
        max_cnt = cnt

    for j in range(1, N+1):
        if idx != j and adj[idx][j] == 1:
            if vis[j] == 0:
                dfs(j, cnt+1)
    # 아래 줄이 없으면 한번 씩만 방문함
    # 아래 줄을 쓰게 되면 각 정점들을 시작점으로 돌 수 있음
    vis[idx] = 0            # 두번째 예시에서, 3에서 시작해서 끝까지 가는 경로를 돌게 됨
    #### 느낌에, 출발점이 달라질 수 있는 경우 방문배열을 취소하는 듯


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    vis = [0] * (N+1)               # 각 정점 방문 배열
    max_cnt = -1

    # 인접행렬 구성성
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u][v] = 1
        adj[v][u] = 1

    for i in range(1, N+1):          # 각 정점에서 시작
        if vis[i] == 0:
            dfs(i, 1)               # 1 : 정점 개수수
    print('#{} {}'.format(tc, max_cnt))

'''
2
1 0
3 2
1 2
3 2
'''
'''
1
6 5
1 2
1 3
2 4
2 5
2 6
'''