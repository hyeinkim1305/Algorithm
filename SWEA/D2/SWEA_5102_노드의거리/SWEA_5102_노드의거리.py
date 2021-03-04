
# 주의할 점 : cur = q.pop(0)을 할 때마다 d += 1하게 되면 누적되는 듯

def bfs(s, g):
    q = []      # 큐
    q.append(s)     # 시작정점
    visit[s] = 1

    while q:    # 큐가 비어있지 않은 동안 (비어있다는 건 더이상 방문할 정점이 없다는 뜻인듯!)
        cur = q.pop(0)
        for i in arr[cur]:
            if visit[i] == 0:
                if i == g:
                    dis[i] = dis[cur] + 1   # 이전 노드까지 거리에 +1 해야함
                    return dis[i]
                q.append(i)
                visit[i] = 1
                dis[i] = dis[cur] + 1

    return 0    # 다 돌았는데 도착정점 못찾으면 0을 리턴

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visit = {i:0 for i in range(1, V+1)}    # 방문배열
    arr = {i:[] for i in range(1, V+1)}     # 인접 노드 리스트
    dis = {i:0 for i in range(1, V+1)}      # 정점들 거리 표기
    for i in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(S, G)))



# 틀린 이유 : 정점을 꺼낼때마다 거리를 1씩 올려주면 이전 정점꺼의 거리에 누적이 되기 때문인듯!! 주의
# def bfs(s, g):
#     d = 1       # 거리
#     q = []
#     q.append(s)
#     visit[s] = 1
#
#     while q:
#         cur = q.pop(0)
#         d += 1
#         for i in arr[cur]:
#             if visit[i] == 0:
#                 if i == g:
#                     return d
#                 q.append(i)
#                 visit[i] = 1
#
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     visit = {i:0 for i in range(1, V+1)}
#     arr = {i:[] for i in range(1, V+1)}
#     # dis = {i:0 for i in range(1, V+1)}
#     for i in range(E):
#         u, v = map(int, input().split())
#         arr[u].append(v)
#         arr[v].append(u)
#     S, G = map(int, input().split())
#
#     print('#{} {}'.format(tc, bfs(S, G)))



'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''