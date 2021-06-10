'''
직사각형 보드
N, M = 세로, 가로
파란구슬, 빨간구슬 움직이는거 따로
'''
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(rr, rc, br, bc, cnt):
    q = [[rr, rc, br, bc, cnt]]
    visited.append([rr, rc, br, bc])

    while q:
        Rr, Rc, Br, Bc, cnt = q.pop(0)

        if cnt > 10:
            break

        for i in range(4):
            Rnr, Rnc, Rdis = move(Rr, Rc, dr[i], dc[i])
            Bnr, Bnc, Bdis = move(Br, Bc, dr[i], dc[i])
            if board[Bnr][Bnc] != 'O':
                if board[Rnr][Rnc] == 'O':
                    return cnt
                elif Rnr == Bnr and Rnc == Bnc:
                    if Rdis > Bdis:
                        Rnr -= dr[i]
                        Rnc -= dc[i]
                    else:
                        Bnr -= dr[i]
                        Bnc -= dc[i]
                if [Rnr, Rnc, Bnr, Bnc] not in visited:
                    visited.append([Rnr, Rnc, Bnr, Bnc])
                    q.append([Rnr, Rnc, Bnr, Bnc, cnt+1])
    return -1

def move(r, c, dr, dc):
    k = 1
    while True:
        if board[r+ (dr*k)][c+(dc*k)] == '#':
            return r+(dr*(k-1)), c+(dc*(k-1)), k-2
        elif board[r+ (dr*k)][c+(dc*k)] == 'O':
            return r+(dr*k), c+(dc*k), k-1
        k += 1


N, M = map(int, input().split())
board = []
visited = []
for i in range(N):
    b = list(input())
    for j in range(M):
        if b[j] == 'B':
            br, bc = i, j
        elif b[j] == 'R':
            rr, rc = i, j
    board.append(b)

print(bfs(rr, rc, br, bc, 1))

