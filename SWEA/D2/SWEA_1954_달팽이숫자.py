'''
(방향 변경)
조건 - 행렬의 끝, 이미 채워져 있으면
(끝)
N*N 만큼만 반복
(상하좌우)
-1, 0
1, 0
0, -1
0, 1
여기서 우하좌상 반복
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 0 으로 2차 배열 초기화, 첫번째 시작점은 1로
    table = [[0 for _ in range(N)] for _ in range(N)]
    x, y = 0, 0
    cnt = 2
    table[x][y] = 1

    # 우하좌상 순서
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]


    while cnt < N**2+1:
        for i in range(4):
            while True:
                # 우
                if i == 0:
                    if y + dc[i] > N-1 or table[x+dr[i]][y+dc[i]] != 0:
                        break
                # 하
                if i == 1:
                    if x + dr[i] > N-1 or table[x+dr[i]][y + dc[i]] != 0:
                        break
                # 좌
                if i == 2:
                    if y + dc[i] < 0 or table[x+dr[i]][y+ dc[i]] != 0:
                        break
                # 상
                if i == 3:
                    if x+ dr[i] < 0 or table[x+dr[i]][y + dc[i]] != 0:
                        break
                table[x + dr[i]][y + dc[i]] = cnt
                x, y = x + dr[i], y + dc[i]
                cnt += 1



    print("#{}".format(tc))
    for i in table:
        for j in i:
            print(j, end = " ")
        print()






#
# cnt = 0
# while cnt <= N*N:
#
# # 우하좌상 순서
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# while :
# for i in range()
#     table[]
#     if 끝점에 만나면:
#         break
