
# 감이 안오면 규칙 생각해보기
# 40일때는 11개가 나옴
# 1, 3, 5, 11, 21 .. 이이전꺼에 2배 곱하고 이전꺼를 더하면 개수가 나옴 n=60은 43?

def rec(n):
    if n == 10:
        return 1
    if n == 20:
        return 3
    return rec(n - 10) + rec(n - 20) * 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, rec(N)))