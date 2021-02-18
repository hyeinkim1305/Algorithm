# 가로 탐색
def row(N, M, table):
    for i in range(N):   # 전체 행 수
        for j in range(N-M+1):   # 한 행안에서 검사 횟수
            cnt = 0
            for k in range(int(M//2)):   # 회문안에서 비교 횟수
                if table[i][j+k] == table[i][j+M-(k+1)]:
                    cnt += 1
            if cnt == int(M//2):
                return ''.join(table[i][j:j+M])

# 세로 탐색
def col(N, M, table):
    for i in range(N):   # 전체 열 수
        for j in range(N-M+1):  # 한 열안에서 검사 횟수
            cnt = 0
            for k in range(int(M//2)):
                if table[j+k][i] == table[j+M-(k+1)][i]:
                    cnt += 1
            col_ans = []
            if cnt == int(M//2):
                for l in range(j, j+M):
                    col_ans.append(table[l][i])
                return ''.join(col_ans)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(input()) for _ in range(N)]

    row_output = row(N, M, table)
    col_output = col(N, M, table)

    if row_output == None:
        print('#{} {}'.format(tc, col_output))
    elif col_output == None:
        print('#{} {}'.format(tc, row_output))

# 헷갈렸던 것
# li = [[1,2,3,5],[3,5,7,8]]
# print(li[1][1:3])

# def li(n):
#     if n == 3:
#         return 0
#
# output = li(2)
# if output == None:
#     output = 3
# print(output)