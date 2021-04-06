
'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''

def f(idx):
    global cnt
    while idx <= N:
        tree[idx] = num[cnt]                # 주어진 수를 루트노드부터 차례로 넣는다
        if tree[idx] < tree[idx//2]:        # 만약 부모노드 수가 더 크다면,
            n = idx
            while True:                     # 부모 노드가 더 작아질 때까지 바꾼다
                if tree[n] > tree[n//2]:
                    break
                tree[n], tree[n // 2] = tree[n // 2], tree[n]
                n //= 2
        cnt += 1
        idx += 1
    return tree

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    tree = [0] * (N+1)
    cnt = 0
    f(1)

    # 조상 노드에 저장된 정수 합 구하기
    ans = 0
    while N//2:
        ans += tree[N//2]
        N //= 2

    print('#{} {}'.format(tc, ans))



