'''
1
3 7
***....
*-..#**
#<.****
23
SURSSSSUSLSRSSSURRDSRDS
'''

'''
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>
'''
# UDLR에서 for문으로 돌렸는데 오히려 런타임에러 있었다! 그냥 각각 해주니까 런타임에러 사라짐!

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    battle = []  # 게임 맵
    for i in range(H):
        bat = list(input())
        for j in range(len(bat)):
            if bat[j] == '^' or bat[j] == 'v' or bat[j] == '<' or bat[j] == '>':
                r_idx = i   # 전차 row 인덱스
                c_idx = j   # 전차 col 인덱스
                shape = bat[j]   # 전차 방향
                bat[j] = '.'
        battle.append(bat)
    N = int(input()) # 입력 개수
    order = list(input())  # 입력 종류

    for i in range(len(order)):
        if order[i] == 'S':   # S 명령어일때
            if shape == '^':
                r = r_idx - 1  # Shot의 시작 row 인덱스
                while r >= 0:
                    if battle[r][c_idx] == '#':
                        break
                    elif battle[r][c_idx] == '*':
                        battle[r][c_idx] = '.'
                        break
                    elif battle[r][c_idx] == '.' or battle[r][c_idx] == '-':
                        r -= 1
                        continue
            if shape == 'v':
                r = r_idx + 1  # Shot의 시작 row 인덱스
                while r <= H-1:
                    if battle[r][c_idx] == '#':
                        break
                    elif battle[r][c_idx] == '*':
                        battle[r][c_idx] = '.'
                        break
                    elif battle[r][c_idx] == '.' or battle[r][c_idx] == '-':
                        r += 1
                        continue
            if shape == '<':
                c = c_idx - 1   # shot의 시작 col 인덱스
                while c >= 0:
                    if battle[r_idx][c] == '#':
                        break
                    elif battle[r_idx][c] == '*':
                        battle[r_idx][c] = '.'
                        break
                    elif battle[r_idx][c] == '.' or battle[r_idx][c] == '-':
                        c -= 1
                        continue
            if shape == '>':
                c = c_idx + 1   # shot의 시작 col 인덱스
                while c <= W-1:
                    if battle[r_idx][c] == '#':
                        break
                    elif battle[r_idx][c] == '*':
                        battle[r_idx][c] = '.'
                        break
                    elif battle[r_idx][c] == '.' or battle[r_idx][c] == '-':
                        c += 1
                        continue
        elif order[i] == 'U':
            shape = '^'
            if r_idx != 0 and battle[r_idx-1][c_idx] == '.':
                r_idx -= 1

        elif order[i] == 'D':
            shape = 'v'
            if r_idx != H-1 and battle[r_idx+1][c_idx] == '.':
                r_idx += 1

        elif order[i] == 'L':
            shape = '<'
            if c_idx != 0 and battle[r_idx][c_idx-1] == '.':
                c_idx -= 1

        else:
            shape = '>'
            if c_idx != W-1 and battle[r_idx][c_idx+1] == '.':
                c_idx += 1


    battle[r_idx][c_idx] = shape

    print(f'#{tc}', end = ' ')
    for i in battle:
        print(''.join(i))



























##############################################################################


# T = int(input())
# H, W = map(int, input().split())
#
# table = []
# for i in range(H):
#     row = list(input())
#     for j in range(len(row)):
#         if row[j] == '<' or row[j] == '>' or row[j] == '^' or row[j] == 'v':
#             c = i
#             r = j
#     table.append(row)
#
# # 입력 개수
# N = int(input())
# # 게임 입력
# n = list(input())
#
# direction = ['U', 'D', 'L', 'R']
# sign = ['^', 'v', '<', '>']
# dr = [-1, +1, 0, 0]
# dc = [0, 0, -1, +1]
#
# # 입력값을 돌면서
# for j in n:
#     # UDLR 일 때
#     for d in range(len(direction)):
#         if j == direction[d]:
#             # 평지라면 방향 바꾸고, 그 칸으로 이동, 이전 칸은 .으로 변경
#             if table[r + dr[d]][c + dc[d]] == '.':
#                 table[r][c] = '.'
#                 r += dr[d]
#                 c += dc[d]
#                 table[r][c] = sign[d]
#             else:    # 평지가 아니라면 방향만 바꾼다.
#                 table[r][c] = sign[d]
#             break   #
#     # S 일 때
#     if j == 'S':
#         # 바라보고 있는 방향으로 포탄 발사 / 위치나 방향은 그대로, 다른 블럭들 변경
#         # . 이랑 - 일때는 직진  / continue로 하면 될듯 / 범위를 넘어가면 끝
#         # * 는 뿌시고 .으로 바꾸기
#         # #은 break
#         # sign이랑 dr, dc 이용
#         for s in range(len(sign)):
#             if table[r][c] == sign[s]:
#                 #
#                 if table[r + dr[s]][c + dc[s]] == '*':
#                     table[r + dr[s]][c + dc[s]] = '.'
#                 elif table[r + dr[s]][c + dc[s]] == '.' or table[r + dr[s]][c + dc[s]] == '-':
#                     m = 2
#                     while True:
#
#                         if table[r + dr[s]*m][c + dc[s]*m] == '*':
#                             table[r + dr[s] * m][c + dc[s] * m] = '.'
#
#
#                         m += 1
#
#
#
#
#
#
#
#
#
#
#
#
