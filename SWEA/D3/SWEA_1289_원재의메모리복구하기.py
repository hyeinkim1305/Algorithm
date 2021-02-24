
T = int(input())
for tc in range(1, T+1):
    memo = list(input())
    zero = [str(0) for _ in range(len(memo))]
    cnt = 0   # 수정 횟수

    for i in range(len(zero)):
        if i == 0:
            if memo[i] == '0':
                continue
            if memo[i] == '1':
                for j in range(i, len(zero)):
                    zero[j] = '1'
                cnt += 1

        elif memo[i] != memo[i-1]:
            for j in range(i, len(zero)):
                zero[j] = memo[i]
            cnt += 1
    print(f'#{tc} {cnt}')
