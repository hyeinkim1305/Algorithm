
def dfs(r):
    check[r] = 1

    for i in data[r]:
        if check[i] == 0:
            dfs(i)


import sys
N, M = map(int, sys.stdin.readline().split())

data = {i:[] for i in range(1, N+1)}
check = {i:0 for i in range(1, N+1)}

# 연결요소 개수 초기화
cnt = 0

# 1. 연결된 정점들을 딕셔너리 형태로 넣어준다
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    data[u].append(v)
    data[v].append(u)

# 2. 1번부터 N번까지 딕셔너리를 돌면서 방문 안했을 경우 dfs 탐색해준다.
for j in range(1, N+1):
    if check[j] == 0:
        dfs(j)
        cnt += 1        # 한번의 깊이 탐색이 끝나면 연결 요소 개수를 +1 해준다.
print(cnt)
