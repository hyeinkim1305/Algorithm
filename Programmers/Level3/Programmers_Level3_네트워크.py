'''
이 문제 풀 때 좀 헷갈렸음 !!
나는 2차원 배열의 각각을 시작점으로 생각했는데 이러면 생각이 꼬인다.
보통 4방향 탐색이거나 할 때 그렇게 생각!
이 문제는 노드 기준으로 생각하면 된다!
0, 1, 2 노드를 기준으로 연결되어 있고 방문 안한거 재귀반복하는 것
'''

### 1. dfs 풀이
def dfs(idx, visited, n, computers):
    visited[idx] = 1

    for j in range(n):
        # 대각선 성분이 아니고 연결되어 있을 때
        if idx != j and computers[idx][j] == 1:
            if visited[j] == 0:
                dfs(j, visited, n, computers)


def solution(n, computers):
    visited = [0] * n
    cnt = 0             # 네트워크 수
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, n, computers)
            cnt += 1                # 뭉텅이 개수를 세주면 되니까 여기에 적으면 된다.

    return cnt

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)


### 2. bfs 풀이

def bfs(n, computers, idx, vis):
    q = [idx]
    vis[idx] = 1

    while q:
        cur = q.pop(0)

        for j in range(n):
            if cur != j and vis[j] == 0:
                if computers[cur][j]:
                    q.append(j)
                    vis[j] = 1


def solution(n, computers):
    vis = [0] * n
    answer = 0
    for i in range(n):
        if vis[i] == 0:
            bfs(n, computers, i, vis)
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)