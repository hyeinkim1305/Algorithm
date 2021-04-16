
'''
재귀부분 잘 보기!
아래처럼 하면 부분집합처럼 된다.
'''

def dfs(i, cnt, N, B):
    global min_cnt

    if B <= cnt < min_cnt:      # B이상이고 지금까지의 최소값보다 작은 경우
        min_cnt = cnt
        return

    if cnt > min_cnt:
        return

    if i == N:
        return

    dfs(i+1, cnt+H[i], N, B)
    dfs(i+1, cnt, N, B)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())        # 직원수, 높이
    H = list(map(int, input().split()))

    visited = [0] * N
    min_cnt = 987654321
    dfs(0, 0, N, B)
    print(f'#{tc} {min_cnt-B}')

