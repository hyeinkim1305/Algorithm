'''
* 잊어버릴까봐 적는 *
[효율성은 잘 모르겠음]

전체적인 로직은
(생성)
    2차원 행렬에 인접한 노드와 가중치를 넣고
    최소 가중치 넣어줄 d를 무한대로 초기화하여 만든다
(함수호출)
    출발점 거리는 0
    q 만들고, 힙큐 라이브러리 이용하여 (출발점의 가중치, 출발점) 넣어준다.
    함수 호출
(함수)
    q가 비어있지 않은 동안,
        q에서 하나 꺼내고 (이때 힙큐는 최소힙으로 디폴트 정렬되어있다. 아마도?)
        그 지점에 해당하는 행렬을 한 행 돌면서 가중치 있는 칸이 있으면
            지금의 가중치 + 행렬에 있는 가중치 < 기존 그 가중치 이면
            기존 가중치에 새롭게 넣어주고
            큐에 이 가중치와 새로운 지점을 담은 거를 푸시한다.
(오는거-전치)
행렬만 전치로 넣어주고, 그러면 위랑 똑같아진다
(최종)
여기서 전체 d 2개를 각각 돌며 합을 계산하는데
가장 큰 합을 출력한다.

'''
# D6
import heapq

def sol(q, d, arr):

    while q:
        cur = heapq.heappop(q)
        for i in range(1, N+1):
            if arr[cur[1]][i]:      # 가중치가 있으면
                if d[i] > cur[0] + arr[cur[1]][i]:
                    d[i] = cur[0] + arr[cur[1]][i]
                    heapq.heappush(q,(d[i], i))
    return d


# def sol2(q2):
#
#     while q2:
#         cur = heapq.heappop(q2)
#         for i in range(1, N+1):
#             if at[cur[1]][i]:      # 가중치가 있으면
#                 if dt[i] > cur[0] + at[cur[1]][i]:
#                     dt[i] = cur[0] + at[cur[1]][i]
#                     heapq.heappush(q2,(dt[i], i))
#     return dt


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    arr = [[0]*(N+1) for _ in range(N+1)]
    at = [[0]*(N+1) for _ in range(N+1)]

    d = [float('inf')] * (N+1)
    dt = [float('inf')] * (N+1)

    for _ in range(M):
        x, y, c = map(int, input().split())
        arr[x][y] = c               # x번 집에서 y번 집으로 가는데 걸리는 시간
        at[y][x] = c                # 전치

    d[X] = 0            # 출발점 거리 초기화
    q = []
    heapq.heappush(q, (d[X], X))         # X : 출발점
    d = sol(q, d, arr)

    dt[X] = 0
    q2 = []
    heapq.heappush(q2, (dt[X], X))
    dt = sol(q2, dt, at)

    max_d = -1
    for k in range(1, N+1):
        if d[k] + dt[k] > max_d:
            max_d = d[k] + dt[k]
    print('#{} {}'.format(tc, max_d))
