'''
1
5
14054
44250
02032
51204
52212
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 농장의 크기
    farm = [list(input()) for _ in range(N)]
    value = 0  # 농작물 가치

    k = 0
    for i in range(N):  # 각 행마다 순회
        for j in range(N//2-k, N//2+1+k):
            value += int(farm[i][j])

        if i >= N // 2:
            k -= 1
        else:
            k += 1

    print(f'#{tc} {value}')


