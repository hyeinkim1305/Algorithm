# 다른 풀이도 없는지 고민해보기
# Sol1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))

    cnt = 0
    while cnt < M:
        f = n.pop(0)
        n.append(f)
        cnt += 1
    print('#{} {}'.format(tc, n[0]))


