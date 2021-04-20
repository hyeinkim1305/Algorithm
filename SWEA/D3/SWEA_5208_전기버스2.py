
# D3

def sol():
    cnt = 0
    idx = 1
    while True:

        if idx + battery[idx] >= stop:                          # 종점 넘어가면
            return cnt

        n = (idx + battery[idx]) + battery[idx + battery[idx]]

        max_n = -1
        for i in range(idx+1, idx + battery[idx]+1):            # 지나가면서 더 큰거 있는지 체크
            if i + battery[i] >= n:                             # 더 큰게 있다면
                if i + battery[i] > max_n:                      # 그게 지금까지 max 로 큰거보다 크다면
                    max_n = i + battery[i]                      # 갈 수 있는 정류장
                    startidx = i                                 # 다음 반복의 시작 인덱스

        idx = startidx
        cnt += 1


T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    stop = data[0]
    battery = [0] + data[1:]        # 인덱스 맞추려고
    print(f'#{tc} {sol()}')

'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''