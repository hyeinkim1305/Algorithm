

def in_order(idx):
    global ans
    if idx:                 # 리프노드에 다다르면 자식 노드의 값들이 0 이므로 재귀가 더이상 진행되지 못하고 돌아오게 됨. 따라서 N보다 작다는 조건을 추가 안해도 됨.
        in_order(tree[idx][0])
        ans += tree[idx][1]
        in_order(tree[idx][2])

for tc in range(1, 10+1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]      # 0부터 N까지
    ans = ""
    # 트리만들기
    for _ in range(N):
        data = list(input().split())
        if len(data) == 2:
            tree[int(data[0])][1] = data[1]
        elif len(data) == 3:
            tree[int(data[0])][1] = data[1]
            tree[int(data[0])][0] = int(data[2])
        elif len(data) == 4:
            tree[int(data[0])][1] = data[1]
            tree[int(data[0])][0] = int(data[2])
            tree[int(data[0])][2] = int(data[3])
    in_order(1)
    print('#{} {}'.format(tc, ans))
