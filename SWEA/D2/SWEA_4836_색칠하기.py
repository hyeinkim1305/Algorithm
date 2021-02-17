
T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 칠할 영역 개수
    arr = []
    for _ in range(N):
        rec = list(map(int, input().split()))
        arr.append(rec)

    # 색칠된거 표시할 리스트
    cnt = [[0 for _ in range(10)] for _ in range(10)]

    for a in arr:
        for i in range(a[0], a[2]+1):
            for j in range(a[1], a[3]+1):
                cnt[i][j] += a[4]
    output = 0
    for cn in cnt:
        for c in cn:
            if c >= 3:
                output += 1

    print("#{} {}".format(tc, output))

