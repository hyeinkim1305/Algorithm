'''
10 100 200 1060
12 9 11 13 11 8 6 12 8 7 15 6
'''
T = int(input())
for tc in range(1, T+1):
    c = list(map(int, input().split()))  # 이용권 가격
    plan = list(map(int, input().split()))  # 이용 계획

    for i in range(12):
        if plan[i] != 0:
            start = i
            break

    cost = [0] * 12     # 지금까지 금액
    for j in range(start, 12, 1):

        # 1일치 비용과 한달치 비용 비교해서 더하기
        if c[0] * plan[j] > c[1] * 1:
            if j == 0:      # j가 0일때 고려
                cost[j] = c[1] * 1
            cost[j] = cost[j-1] + c[1] * 1
        elif c[0] * plan[j] <= c[1] * 1:
            if j == 0:
                cost[j] = c[0] * plan[j]
            cost[j] = cost[j-1] + c[0] * plan[j]

        # 3달치 비용
        if j >= 2:
            if j == 2:
                three = c[2]
                if three < cost[j]:
                    cost[j] = three
            else:
                three = cost[j - 3] + c[2]
                if three < cost[j]:
                    cost[j] = three

    if c[3] < cost[11]:
        ans = c[3]
    else:
        ans = cost[11]

    print('#{} {}'.format(tc, ans))




