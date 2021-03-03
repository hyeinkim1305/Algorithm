
'''
1. BFS (너비우선탐색, 퍼져나가는 식으로 탐색)
시작정점을 큐에 넣고, visited 표시한다
큐가 비어있지 않을때까지 반복
    큐의 앞에 있는거 꺼내고 이 정점의 인접정점 중 방문하지 않은 곳을 다시 큐에 넣고
    방문했다고 표시
'''
def bfs(n):
    visited = {i: 0 for i in range(1, N + 1)}  # 재귀 안해도 되서 visited 안에 넣음
    q = []

    q.append(n)  # 시작정점 방문
    visited[n] = 1

    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for i in arr[cur]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
'''
2. DFS (깊이우선탐색)
정점 방문한 곳 체크
정점에 인접한 정점들 중 방문 안한 곳을 또다시 방문 (재귀)
* 이때 check는 함수 밖에 선언 (재귀 때문에)
'''

def dfs(n):
    check[n] = 1
    print(n, end=' ')

    for i in arr[n]:
        if check[i] == 0:
            dfs(i)

info = list(map(int, input().split()))
N = info[0]
M = info[1]
V = info[2]
arr = {i:[] for i in range(1, N+1)}
check = {i: 0 for i in range(1, N + 1)}  # dfs꺼

for i in range(M):  # 딕셔너리 형태로 인접리스트 정의
    n, m = map(int, input().split())
    arr[n].append(m)
    arr[m].append(n)
for j in range(1, N+1):  # 인접정점들 오름차순 정렬 (정점 번호가 작은 것을 먼저 방문한다고 하였으므로)
    arr[j].sort()

dfs(V)
print()
bfs(V)









