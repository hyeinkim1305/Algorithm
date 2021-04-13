

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ans = []
    while M >= 2:
        ans = [M % 2] + ans
        M //= 2
    if M == 2:
        ans = [M // 2] + ans
    else:
        ans = [M] + ans


    result = 'ON'
    if len(ans) < N:
        result = 'OFF'
    else:
        for i in range(len(ans)-1, len(ans)-1-N, -1):
            if ans[i] == 0:
                result = 'OFF'
                break

    print('#{} {}'.format(tc, result))


# 더 간단한 다른 풀이
# T = int(input())
#
# for test_case in range(1,T+1):
#     N, M = map(int,input().split())
#
#     result = 'ON'
#     for i in range(N):
#         if not M & (1 << i):
#             result = 'OFF'
#             break
#
#
#     print('#{} {}'.format(test_case, result))