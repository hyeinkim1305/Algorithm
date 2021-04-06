
# 루트노드부터 시작
def f(idx):
    global cnt
    if idx <= N:
        f(idx*2)        # 왼쪽 노드 들어가기
        tree[idx][1] = cnt      # 숫자 넣기
        cnt += 1
        f(idx*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]          # 0 하나만 해도 될듯
    cnt = 1         # 시작하는 수
    f(1)
    print('#{} {} {}'.format(tc, tree[1][1], tree[N//2][1]))


