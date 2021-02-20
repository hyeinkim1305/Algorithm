
# sol1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    count = []
    cnt = 0
    for i in range(N-M+1):   # 행 수
        for j in range(N-M+1):  # 시작점
            for k in range(M):
                for l in range(M):
                    cnt += table[i+k][j+l]
            count.append(cnt)
            cnt = 0

    max_num = 0
    for i in count:
        if i > max_num:
            max_num = i
    print("#{} {}".format(tc, max_num))


# sol2  # 굳이 계산값들을 배열에 다시 담을 필요는 없음
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N-M+1):   # 행 수
        for j in range(N-M+1):  # 시작점
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += table[i+k][j+l]
            if cnt > max_cnt:
                max_cnt = cnt

    print("#{} {}".format(tc, max_cnt))
