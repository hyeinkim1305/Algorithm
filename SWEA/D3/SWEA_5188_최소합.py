

# 오른쪽, 아래로만 가니까 visited 안 만들어줘도 된다!!
dr = [0, 1]
dc = [1, 0]

def dfs(r, c, ans):
    global min_sum

    if ans >= min_sum:      # 백트래킹! 만약 넘어가버리면 리턴해서 돌려주자.
        return

    if r == M-1 and c == M-1:
        if ans < min_sum:
            min_sum = ans
        return          # 다시 돌아가야해!

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr > M-1 or nc < 0 or nc > M-1:
            continue
        else:
            dfs(nr, nc, ans+arr[nr][nc])


# 도착점에 도착할 때까지 이동
T = int(input())
for tc in range(1, T+1):
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]
    min_sum = 987654321
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(tc, min_sum))














'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''