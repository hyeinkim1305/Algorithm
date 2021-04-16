

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, ans):
    global result

    if len(ans) == 7:
        if ans not in result:
            result.add(ans)
        return          # 이부분 꼭 넣어줘야함! 안하면 재귀깊이 깊어져서 오류 나온다

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <= 3 and 0 <= nc <= 3:           # 여기에 다시 한번 해보기
            dfs(nr, nc, ans + str(arr[nr][nc]))


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    result = set()          # 일곱자리들을 넣을 set
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')
    print('#{} {}'.format(tc, len(result)))