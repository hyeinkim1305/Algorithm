
# 탐색
def test(A, P):
    start_A = 1
    end_A = P
    A_cnt = 1
    while start_A <= end_A:
        mid_A = int((start_A + end_A) / 2)
        if mid_A == A:
            return A_cnt
        elif mid_A < A:
            start_A = mid_A
            A_cnt += 1
        else:
            end_A = mid_A
            A_cnt += 1
    return 0

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    if test(A, P) > test(B, P):
        print('#{} {}'.format(tc, 'B'))
    elif test(A, P) < test(B, P):
        print('#{} {}'.format(tc, 'A'))
    else:
        print('#{} {}'.format(tc, '0'))

