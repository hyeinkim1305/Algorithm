
'''
행 최소, 초대
열 최소, 최대
'''

# 상하좌우
dr = [-1, +1, 0, 0]
dc = [0, 0, -1, +1]

def bfs(r, c):
    q = []
    q.append([r, c])
    arr[r][c] = 0
    max_r = r       # 최대 행
    max_c = c       # 최대 열

    while q:
        cur = q.pop(0)
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1: continue
            if arr[nr][nc] != 0:
                q.append([nr, nc])
                arr[nr][nc] = 0
                if nr >= max_r and nc >= max_c:     # 최대 행 찾기, 최대 열 찾기
                    max_r = nr
                    max_c = nc
    return max_r, max_c     # 최대 행과 열을 리턴

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):      # 시작점 찾기
        for j in range(N):
            if arr[i][j] != 0:
                R = i
                C = j
                answer = bfs(R, C)      # 함수 실행
                ans.append([(answer[0]-R+1) * (answer[1]-C+1), answer[0]-R+1, answer[1]-C+1])       # 최대 행과 열에서 각각 시작점 뺀다 + 1

    ans = sorted(ans, key = lambda x : (x[0], x[1]))        # 정렬

    print('#{} {}'.format(tc, len(ans)), end=' ')
    for i in ans:
        for j in range(1, 3):
            print(i[j], end= ' ')
    print()






