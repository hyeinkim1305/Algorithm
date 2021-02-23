# 대각선 탐색하는 부분 잘 보기!

def Game(table, N):
    # 행 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if table[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    return 'YES'
            else:
                cnt = 0

    # 열 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if table[j][i] == 'o':
                cnt += 1
                if cnt >= 5:
                    return 'YES'
            else:
                cnt = 0


    # 대각선 검사
    # 작은 정사각형에서 각각 대각선 방향으로 나가면서 검사하는 느낌
    for i in range(N-5+1):
        for j in range(N-5+1):
            cnt = 0
            for k in range(5):
                if table[i+k][j+k] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                else:
                    cnt = 0
                    # break 해도 될듯
    for i in range(N-5+1):
        for j in range(5-1, N):
            for k in range(5):
                if table[i+k][j-k] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                else:
                    cnt = 0
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Table = [list(input()) for _ in range(N)]
    print('#{} {}'.format(tc, Game(Table, N)))