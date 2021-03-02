'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2

'''

def find(r, c, visit):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
            continue
        if n[nr][nc] - n[r][c] == 1:
            visit += 1
            return find(nr, nc, visit)
    return visit


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]
    max_visit = -1


    for i in range(N):
        for j in range(N):
            visit = 0
            ans = find(i, j, visit)+1
            if ans > max_visit:
                max_visit = ans
                min_node = n[i][j]
            elif ans == max_visit:
                if n[i][j] < min_node:
                    min_node = n[i][j]

    print('#{} {} {}'.format(tc, min_node, max_visit))



