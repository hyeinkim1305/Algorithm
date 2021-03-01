'''
만약에 중간에 0이 섞여있다면 돌을 놓지 못한다는 조건이 들어있어야함!
이 부분을 놓쳐서 오래 걸림
'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pos = [list(map(int, input().split())) for _ in range(M)]
    table = [[0 for _ in range(N)] for _ in range(N)]
    table[N // 2 - 1][N // 2 - 1], table[N // 2][N // 2] = 2, 2  # 처음 세팅
    table[N // 2 - 1][N // 2], table[N // 2][N // 2 - 1] = 1, 1
    pass_card = 0  # 돌을 못 놓았을 때 넘어가는거 카운팅

    # 인덱스 넘어갈 경우 생각
    for i in range(M):

        c = pos[i][0] - 1
        r = pos[i][1] - 1
        s = pos[i][2]  # 컬러

        dr = [0, 0, -1, 1, -1, +1, +1, -1]
        dc = [1, -1, 0, 0, +1, -1, +1, -1]
        complete = 0

        # 방향 확인
        for j in range(8):
            cc = c
            rr = r
            while True:
                cc += dc[j]
                rr += dr[j]
                if rr < 0 or rr >= N or cc < 0 or cc >= N:
                    break
                if table[rr][cc] == 0:   # 0이라면 안바뀌는 조건 추가!!
                    break
                if table[rr][cc] == s:
                    while True:
                        if cc == c and rr == r:
                            break
                        cc -= dc[j]
                        rr -= dr[j]
                        if table[rr][cc] != 0 and table[rr][cc] != s:
                            table[rr][cc] = s
                    table[r][c] = s
                    complete += 1
                    break
        if complete == 0:
            pass_card += 1
        if pass_card >= 2:
            break

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                black += 1
            if table[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))