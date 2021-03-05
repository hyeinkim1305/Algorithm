
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_cnt = 987654321

    # 반복 돌리고
    for i in range(N-2):        # 하얀깃발 행 범위
        for j in range(i+1, N-1):   # 파란깃발 행 범위
            cnt = 0     # 칠해야하는 칸의 개수

            for k in range(i+1):    # 화이트
                for a in range(M):
                    if arr[k][a] != 'W':
                        cnt += 1
            for w in range(k+1, j+1):   # 블루
                for b in range(M):
                    if arr[w][b] != 'B':
                        cnt += 1
            for l in range(w+1, N):
                for c in range(M):
                    if arr[l][c] != 'R':
                        cnt += 1

            if cnt < min_cnt:
                min_cnt = cnt

    print('#{} {}'.format(tc, min_cnt))



