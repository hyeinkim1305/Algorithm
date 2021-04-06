'''
5 5
#####
#..B#
#.#.#
#RO.#
#####

'''

from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():

    while q:
        Rr, Rc, Br, Bc, cnt = q.popleft()
        if cnt > 10:
            break
        for i in range(4):
            Rnr, Rnc, Rdis = move(Rr, dr[i], Rc, dc[i])
            Bnr, Bnc, Bdis = move(Br, dr[i], Bc, dc[i])


            if board[Bnr][Bnc] != 'O':          # 파란구슬이 구멍에 빠지면 실패
                if board[Rnr][Rnc] == 'O':      # 빨간구슬이 구멍에 있으면
                    return cnt
                if Rnr == Bnr and Rnc == Bnc:   # 둘이 위치가 같으면 하나는 뒤로 옮겨야함
                    if Rdis > Bdis:
                        Rnr -= dr[i]
                        Rnc -= dc[i]
                    else:
                        Bnr -= dr[i]
                        Bnc -= dc[i]
                if [Rnr, Rnc, Bnr, Bnc] not in visited:     # 방문했던 곳들인지 확인
                    visited.append([Rnr, Rnc, Bnr, Bnc])
                    q.append([Rnr, Rnc, Bnr, Bnc, cnt+1])
    return -1


def move(r, dr, c, dc):     # 장애물이나 구멍있을 때까지 직진
    dis = 0     # 이동거리-> 만약에 구슬이 겹칠 때 판단 위함
    while True:

        r += dr
        c += dc
        dis += 1
        if board[r][c] == '.':
            continue
        if board[r][c] == '#':
            return r-dr, c-dc, dis-1
        if board[r][c] == 'O':
            return r, c, dis

N, M = map(int, input().split())
board = []
visited = []

# 빨간구슬, 파란구슬 위치찾기
for i in range(N):
    b = list(input())

    for j in range(M):
        if b[j] == 'R':
            Rrow = i
            Rcol = j
        if b[j] == 'B':
            Brow = i
            Bcol = j
    board.append(b)
q = deque()
q.append([Rrow, Rcol, Brow, Bcol, 1])
visited.append([Rrow, Rcol, Brow, Bcol])
print(bfs())



