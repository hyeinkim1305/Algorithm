
# D4
# MST, PRIM 알고리즘

def MST_PRIM(adj, s):               # s 시작

    dis[s] = 0                      # 시작지점 가중치 0

    for _ in range(V+1):            # 전체 정점 돌면서
        min_i = -1
        min = 11
        for j in range(V+1):        # 인접한 정점 중 방문 안했고, 최소 가중치 정점 찾기
            if vis[j] == 0:
                if dis[j] < min:
                    min = dis[j]
                    min_i = j
        vis[min_i] = 1              # 최소 가중치 정점 방문

        for a, b in adj[min_i]:     # 인접 정점과 가중치 가져와서
            if not vis[a]:          # 방문 안 한 정점인데
                if b < dis[a]:      # 가중치 갱신 가능
                    dis[a] = b
                    p[a] = min_i

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())            # 노드번호, 간선개수
    vis = [0] * (V+1)                           # 방문 배열
    dis = [11] * (V+1)                          # 가중치 초기화, 최대 11
    adj = [[] for _ in range(V+1)]
    p = [False] * (V + 1)                       # 부모배열
    for _ in range(E):                          # 리스트 구성
        u, v, d = map(int, input().split())
        adj[u].append([v, d])
        adj[v].append([u, d])

    MST_PRIM(adj, 0)
    print('#{} {}'.format(tc, sum(dis)))



# 이거 가능하다!
# adj = [[1, 2], [3, 4]]
# for v, val in adj:
#     print(v, val)
# 1 2
# 3 4



# 잘못 구현한듯
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())        # 노드번호, 간선개수
#     arr = []
#     for i in range(E):
#         data = list(map(int, input().split()))
#         arr.append(data)
#     arr = sorted(arr, key=lambda x : x[2])          # 가중치가 낮은 순서대로 정렬
#     ans = [[] for _ in range(V+1)]            # 최종적으로 정답 담을 리스트
#
#     for i in range(len(arr)):
#         cycle = False
#         if not ans:             # ans 비어있을 때
#             ans[arr[i][0]].append(arr[i])
#         else:
#             # 사이클 : 각각 가리키는 것이 동일하거나 서로 이어져있거나
#             now = arr[i]
#             left = now[0]
#             right = now[1]
#             # 사이클 확인 -> 서로 가리키는게 같을 때
#             for i in range(len(ans[left])):
#                 for j in range(len(ans[right])):
#                     if ans[left][i][1] == ans[right][j][1]:
#                         cycle = True
#                         break
#                 if cycle == True:
#                     break
#             for i in range(len(ans[left])):
#                 temp = ans[left][i][1]
#                 for j in ans[temp]:
#                     if ans[temp][j][1] == right:
#                         cycle = True
#                         break
#                 if cycle == True:
#                     break
#
#             if cycle == False:
#                 ans[left].append(arr[i])
#     result = 0
#     for k in range(len(ans)):
#         for l in range(len(ans[k])):
#             result += ans[k][l][2]
#     print(result)

'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''