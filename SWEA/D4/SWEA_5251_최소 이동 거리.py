
# D4
def sol(idx):

    q = [idx]
    d[idx] = 0

    while q:
        cur = q.pop(0)

        for i in range(len(arr[cur])):
            temp = arr[cur][i]
            # 지금 지점 길이에 새로운 지점까지의 거리 더한게 새로운 지점의 기존 거리보다 작으면
            if d[cur] + temp[1] < d[temp[0]]:
                d[temp[0]] = d[cur] + temp[1]           # 갱신
                q.append(temp[0])

    return d


# 일방통행 유방향?
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    d = [float('inf')] * (N+1)
    arr = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s].append([e, w])

    dis = sol(0)
    print('#{} {}'.format(tc, dis[N]))

'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''