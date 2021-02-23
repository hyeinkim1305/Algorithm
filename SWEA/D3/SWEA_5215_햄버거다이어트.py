'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''
# 굳이 여기서 부분집합들의 조합을 다시 리스트에 추가할 필요 없음. 그러면 런타임에러나옴

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    grad = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0

    for i in range(1<<N):
        sum_g = 0    # 칼로리 합
        score_g = 0   # 점수 합
        for j in range(N):
            if i & (1<<j):
                sum_g += grad[j][1]
                score_g += grad[j][0]
        if sum_g <= L:     # 칼로리 낮은 것만 따로 뽑는다
            if score_g > max_score:
                max_score = score_g

    print('#{} {}'.format(tc, max_score))


