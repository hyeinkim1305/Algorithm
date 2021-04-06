'''
10 5 2
8 42
9 468
10 335
6 501
7 170

'''

def nodesum(idx):           # 후위방식
    global tree
    if idx <= N:
        nodesum(idx * 2)
        nodesum(idx * 2 + 1)
        if idx * 2 + 1 <= N:        # 자식 노드가 N안에 있으면
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        if idx * 2 == N:            # 자식 노드가 1개이면  (마지막 노드가 자식노드)
            tree[idx] = tree[idx*2]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b         # 넣기
    nodesum(1)
    print('#{} {}'.format(tc, tree[L]))


'''
# sol2
def calc(l):
    if l <= N:
        if l in nodes:
            return nodes[l]
        return calc(2*l) + calc(2*l + 1)
    return 0

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    nodes = {}
    for i in range(M):
        node, value = map(int, input().split())
        nodes[node] = value
    print(f'#{tc} {calc(L)}')
'''