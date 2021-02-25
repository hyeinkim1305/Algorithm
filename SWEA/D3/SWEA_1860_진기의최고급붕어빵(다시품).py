
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))

    ans = 'Possible'
    for i in range(N):
        if people[i] < M:
            ans = 'Impossible'
            break
        elif people[i] // M * K - i < 1:  # i+1 아님 !!
            ans = 'Impossible'
            break

    print('#{} {}'.format(tc, ans))
























'''
T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    num = list(map(int, input().split()))

    for j in range(len(num)-1, 0, -1):
        for k in range(j):
            if num[k] > num[k+1]:
                num[k], num[k+1] = num[k+1], num[k]


    impossible = 0
    for s in range(len(num)):

        if num[s] < M:
            impossible += 1
            break
            # print('#{} {}'.format(i+1, 'impossible'))
            # break

        elif (num[s] // M * K) - s >= 1:
            continue

        elif (num[s] // M * K) - s < 1:
            impossible += 1
            break
    
    if impossible > 0:
        print('#{} {}'.format(i+1, 'Impossible'))
    else:

        print('#{} {}'.format(i+1, 'Possible'))
'''