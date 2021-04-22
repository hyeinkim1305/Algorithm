
# D4
# 최소 연산이니까 bfs로 푸는게 더 맞을듯!
# 핵심 : 시간초과!
# 이 문제는 deque와 vis와 숫자들의 범위 안지정하면 시간초과가 생긴다! + deque 라이브러리 잘 봐두기
from collections import deque
def bfs(N, M):
    q = deque()
    q.append((N, 0))            # 튜플로 넣고
    vis[N] = 1                  # 이거를 해주는 이유는 같은 숫자 들어가면 또 네번 연산 똑같은거 하니까

    while q:
        num, cnt = q.popleft()

        if num > 1000000:
            continue

        for i in range(4):
            if oper[i][0] == '+':
                u = num + int(oper[i][1:])
            elif oper[i][0] == '-':
                u = num - int(oper[i][1:])
            elif oper[i][0] == '*':
                u = num * int(oper[i][1:])

            # 연산의 중간 결과가 백만 이하의 자연수이니까 0부터 1000000이하여야함!!
            if 0 <= u <= 1000000 and vis[u] == 0:           # 여기서 범위를 지정해줘야해!!
                if u == M:
                    return cnt+1
                vis[u] = 1
                q.append([u, cnt+1])


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    oper = ['+1', '-1', '*2', '-10']
    vis = [0] * 1000001
    print(f'#{tc} {bfs(N, M)}')


# dfs 시간 초과
# def dfs(N, M, cnt):
#     global min_cnt
#
#     if N == M:
#         if cnt < min_cnt:
#             min_cnt = cnt
#         return
#
#     if cnt > min_cnt:
#         return
#
#     if N > 1000000:
#         return
#
#     for i in range(4):
#
#         if oper[i][0] == '+':
#             N = N + int(oper[i][1:])
#         elif oper[i][0] == '-':
#             N = N - int(oper[i][1:])
#         elif oper[i][0] == '*':
#             N = N * int(oper[i][1:])
#         dfs(N, M, cnt+1)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     oper = ['+1', '-1', '*2', '-10']
#     min_cnt = 987654321123212
#     dfs(N, M, 0)
#     print(f'#{tc} {min_cnt}')

'''
3
2 7
3 15
36 1007
'''