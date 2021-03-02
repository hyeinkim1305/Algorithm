
def dfs(n):
    for i in adj[n]:
        if visited[i] == 0:
            visited[i] = 1  # 이거를 for문 앞에 넣어두, 뒤에 넣어두 상관 없네
            dfs(i)

# 인접리스트 dict로 나타내기
V = int(input())
E = int(input())
visited = {i:0 for i in range(1, V+1)}
adj = {i:[] for i in range(1, V+1)}
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dfs(1)
cnt = 0
for i in range(1, V+1):
    if visited[i] == 1:
        cnt += 1
print(cnt-1)


