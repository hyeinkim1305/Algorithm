
# 끝나는 시간 기준으로 오름차순하고 앞에서 부터 하면서 그리디

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    # 끝나는 시간 기준 오름차순, 시작하는 시간도 오름차순(간격이 짧을수록 유리)
    time = sorted(time, key = lambda x: (x[1], x[0]))

    t = time[0][1]      # 제일 첫번째 끝나는 시간
    cnt = 1
    for i in range(1, len(time)):

        # 시작 시간이 끝나는 시간 보다 크보다 같다면 가능
        if time[i][0] >= t:
            cnt += 1
            t = time[i][1]

    print('#{} {}'.format(tc, cnt))
