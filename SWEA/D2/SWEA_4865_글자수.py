
T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    max_cnt = -987654321
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt))
