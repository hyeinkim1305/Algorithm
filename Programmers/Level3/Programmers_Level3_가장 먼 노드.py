from collections import deque

def bfs(s, cnt, adj, vis):
    q = deque()
    q.append((s, cnt))
    vis[s] = 0

    while q:
        cur, count = q.popleft()
        cnt = count + 1
        for i in adj[cur]:
            if vis[i] == -1:  # 방문하지 않았다면
                vis[i] = cnt
                q.append((i, cnt))
    return vis


def solution(n, edge):
    # n개인데 0포함
    adj = [[] for _ in range(n + 1)]

    # 방문배열 생성
    vis = [-1] * (n + 1)

    # 인접리스트 생성
    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    ans = bfs(1, 0, adj, vis)
    max_ans = max(ans)
    return ans.count(max_ans)