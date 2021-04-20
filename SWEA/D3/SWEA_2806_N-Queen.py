# D3

def queen(idx, col_vis, dia1_vis, dia2_vis):
    global count

    if idx == N:
        count += 1
    else:
        for i in range(N):
            if col_vis[i] == 0:                         # 방문 안 한 열이고
                if idx+i not in dia1_vis:               # 방문 안 한 대각선
                    if idx-i not in dia2_vis:      		# 방문 안한 대각선
                        col_vis[i] = 1
                        dia1_vis.append(idx+i)
                        dia2_vis.append(idx-i)
                        queen(idx+1, col_vis, dia1_vis, dia2_vis)
                        col_vis[i] = 0
                        dia1_vis.pop(-1)
                        dia2_vis.pop(-1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    col_vis = [0] * N
    dia1_vis = []           # 우상, 좌하 (행,열 합)
    dia2_vis = []           # 좌상, 우하 (행,열 차)
    count = 0
    queen(0, col_vis, dia1_vis, dia2_vis)
    print(f'#{tc} {count}')

'''
2
1
2
'''