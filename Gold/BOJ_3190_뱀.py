from collections import deque

def bfs():
    time = 0
    tail = deque()
    tail.append((0, 0))
    k = 0       # 방향
    r, c = 0, 0     # 뱀 처음 위치

    while True:
        nr = r + dr[k]
        nc = c + dc[k]

        if (nr < 0 or nr > N - 1 or nc < 0 or nc > N - 1) or (game[nr][nc] == 1):
            time += 1
            return time

        if game[nr][nc] == 2:  # 이동한 칸에 사과가 있다면
            game[nr][nc] = 1
            tail.append([nr, nc])
            time += 1

        elif game[nr][nc] != 2:  # 이동한 칸에 사과가 없다면
            game[nr][nc] = 1  # 머리가 이동
            tail.append((nr, nc))  # 지나온 경로 보관      ### 지워도 되는듯
            cur = tail.popleft()  # 꼬리자르기
            game[cur[0]][cur[1]] = 0  # 꼬리 잘린거 표시
            time += 1

        if time in snake.keys():
            r = nr
            c = nc
            if snake[time] == 'D':
                if k + 1 >= 4:
                    k = (k+1)%4
                else:
                    k = k + 1
            elif snake[time] == 'L':
                if k - 1 < 0:
                    k = (k-1)+4
                else:
                    k = k -1
        else:
            r = nr
            c = nc



N = int(input())        # 보드 크기
K = int(input())        # 사과 개수
apple = []              # 사과 위치
game = [[0] * N for _ in range(N)]
game[0][0] = 1          # game의 맨위 맨좌측은 1
for _ in range(K):
    a, b = map(int, input().split())
    game[a-1][b-1] = 2      # 사과 자리는 2로 표시
L = int(input())         # 뱀의 방향 변환 횟수
snake = {}
for _ in range(L):
    X, C = input().split()
    snake[int(X)] = C


# 시계(D), 반시계(L)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


print(bfs())








