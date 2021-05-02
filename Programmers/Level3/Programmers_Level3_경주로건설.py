'''
Point!
초기 시작이 우측방향이냐, 아래방향이냐에 따라 최소비용이 달라짐.
만약 한번에 q에 넣고 하면 나중에 최소비용을 선택했으나 답이 아닌 경우가 생김.
함수를 2번 돌리기 때문에 각각 cost를 새로 정의해주어야함. 처음에 풀 때 이 부분을 놓쳤었음.
또한, 처음에 풀 때는 cost를 같이 q에 담지 않았었는데 방문했던 곳을 다시 방문할 수 있으니 그때  cost를 같이 q에 담아야할듯
'''
# bfs(board, 최소비용배열, 배열길이, 최초시작방향)
def bfs(board, N, k):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 최소비용 초기설정
    cost = [[float('inf')] * N for _ in range(N)]
    cost[0][0] = 0

    # q : 행인덱스, 열인덱스, 현재 cost, k
    q = []
    q.append([0, 0, 0, k])

    while q:
        r, c, co, d = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
                continue
            if board[nr][nc] == 0:
                #방향이 다르다면
                if i != d:
                    # 기존 비용보다 작다면
                    if co + 500 + 100 < cost[nr][nc]:
                        cost[nr][nc] = co + 600
                        q.append([nr, nc, co+600, i])
                # 방향이 같다면
                else:
                    if co + 100 < cost[nr][nc]:
                        cost[nr][nc] = co + 100
                        q.append([nr, nc, co+100, i])

    return cost[N-1][N-1]


def solution(board):

    N = len(board)
    # 초기 시작이 우측방향, 아래방향이 가능함.
    answer = min(bfs(board, N, 1), bfs(board, N, 3))
    return answer


# solution([[0,0,0],[0,0,0],[0,0,0]])
# solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
# solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]])
# solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])