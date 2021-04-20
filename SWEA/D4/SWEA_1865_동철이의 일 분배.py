

def percent(idx, total):
    global max_total

    if idx == N:
        if total > max_total:
            max_total = total
        return

    if total < max_total:           # 앞으로 곱하는 값이 1보다 작기 때문에 가지치기
        return

    for i in range(N):
        if vis[i] == 0 and suc[idx][i]:             # 0이면 곱하면 작으니까 제외가능
            vis[i] = 1
            percent(idx+1, total*(suc[idx][i]/100))
            vis[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    suc = [list(map(int, input().split())) for _ in range(N)]
    vis = [0] * N
    max_total = -1
    percent(0, 1)
    max_total = max_total * 100
    print('#{} {:.6f}'.format(tc, max_total))

'''
** 소수점 자리 표기
num = 1.23456789 
print('#{} {:.6f}'.format(tc, num))

num = 1.23456789 
print('%.10f' % num)
'''