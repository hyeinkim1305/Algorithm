
T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())

    # 집합 A 
    # 13까지 인거 주의
    number = list(range(1, 13))
    n = len(number)
    cnt = 0
    # 부분집합 개수
    for i in range(1<<n):
        ans = []
        sum_ans = 0
        for j in range(n):
            if i & (1<<j):
                ans.append(number[j])
        # 문제에서 주어진 조건
        if len(ans) == N:
            for a in ans:
                sum_ans += a
            # 조건에 다 맞으면 cnt +1 한다
            if sum_ans == K:
                cnt += 1

    # print("#{} {}".format(tc, cnt))
