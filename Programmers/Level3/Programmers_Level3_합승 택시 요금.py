import heapq
def adj(n, s, a, b, fares):
    # 인접리스트 만들기
    adj = [[] for _ in range(n + 1)]
    for fare in fares:
        u, v, d = fare[0], fare[1], fare[2]
        adj[u].append([v, d])
        adj[v].append([u, d])
    return adj


def dijkstra(start, end, n, adjs):
    # 비용
    cost = [float('inf') for _ in range(n + 1)]
    cost[start] = 0
    q = [[0, start]]

    while q:
        dist, node = heapq.heappop(q)
        if cost[node] < dist:           # 이 코드가 들어가야 시간 초과가 안됨
            continue
        for i in adjs[node]:
            if dist + i[1] < cost[i[0]]:
                heapq.heappush(q, [dist + i[1], i[0]])
                cost[i[0]] = dist + i[1]

    return cost[end]


# 다익스트라
def solution(n, s, a, b, fares):
    # 인접리스트
    adjs = adj(n, s, a, b, fares)
    ans = float('inf')
    for i in range(1, n + 1):
        ans = min(ans, dijkstra(s, i, n, adjs) + dijkstra(i, a, n, adjs) + dijkstra(i, b, n, adjs))

    return ans

# solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
# solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])