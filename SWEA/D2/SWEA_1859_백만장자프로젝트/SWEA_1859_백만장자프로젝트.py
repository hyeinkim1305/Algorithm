
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))
    bene = 0

    while len(cost) != 0 and len(cost) != 1:

        max_cost = 0
        max_idx = 0
        for i in range(len(cost)):
            if cost[i] > max_cost:
                max_cost = cost[i]  # 최대 가격 선택
                max_idx = i

        if max_idx == 0:
            cost = cost[1:]
            max_cost = 0
            max_idx = 0
            for i in range(len(cost)):
                if cost[i] > max_cost:
                    max_cost = cost[i]  # 최대 가격 선택
                    max_idx = i

        sum_cost = 0  # 매수 전체 가격
        cnt = 0  # 개수
        for j in range(max_idx):
            sum_cost += cost[j]
            cnt += 1

        bene += cost[max_idx] * cnt - sum_cost  # 이익
        if max_idx + 1 >= len(cost):
            break
        cost = cost[max_idx + 1:]

    print('#{} {}'.format(tc, bene))

'''
sol2
뒤집어서 뒤에서부터 풀면 풀이가 훨씬 짧아질듯 !!
'''