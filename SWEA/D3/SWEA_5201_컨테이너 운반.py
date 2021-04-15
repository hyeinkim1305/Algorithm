
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)     # 화물 무게
    t = sorted(list(map(int, input().split())), reverse=True)     # 적재용량

    stuff = 0
    idx = 0     # 트럭 인덱스
    i = 0       # 적재용량 인덱스
    while i <= N-1 and idx <= M-1:

        # 화물이 트럭의 적재용량보다 가벼운경우
        if t[idx] >= w[i]:
            stuff += w[i]
            idx += 1
            i += 1
        # 화물이 더 무거운 경우
        elif t[idx] < w[i]:
            i += 1

    print('#{} {}'.format(tc, stuff))



