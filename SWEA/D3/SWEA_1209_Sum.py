
T = 10
N = 100
for tc in range(1, T+1):
    testcase = int(input())
    arr = []
    for s in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    max_sum = -1
    for i in range(N):  # 행
        row_sum = 0
        for j in range(N):  # 열
            row_sum += arr[i][j]
        if row_sum > max_sum:
            max_sum = row_sum


    for i in range(N):  # 열
        col_sum = 0
        for j in range(N):  # 행
            col_sum += arr[j][i]
        if col_sum > max_sum:
            max_sum = col_sum

    sum_m = 0
    for k in range(N):
        sum_m += arr[k][k]

    if sum_m > max_sum:
        max_sum = sum_m

    sum_n = 0
    for t in range(N):
        sum_n += arr[t][N-1-t]

    if sum_n > max_sum:
        max_sum = sum_n

    print('#{} {}'.format(testcase, max_sum))