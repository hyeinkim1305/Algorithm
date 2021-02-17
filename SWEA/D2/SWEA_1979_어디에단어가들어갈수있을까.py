
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로 검사
    count = 0   # 모든 행에서 가능한 공간 합
    for ar in arr:
        cnt = 0
        for a in ar:
            if a == 0:
                if cnt == K:
                    count += 1
                    cnt = 0
                cnt = 0
            if a == 1:
                cnt += 1  # 각 경우 수
        if cnt == K:
            count += 1

    # 세로 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 0:
                if cnt == K:
                    count += 1
                    cnt = 0
                cnt = 0
            if arr[j][i] == 1:
                cnt += 1
        if cnt == K:
            count += 1

    print('#{} {}'.format(tc, count))
