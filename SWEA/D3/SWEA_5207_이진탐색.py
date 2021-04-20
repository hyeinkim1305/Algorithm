
# D3

# 번갈아라고 했으므로 개수 세주는 것 보다 조건 걸어주는게 나은듯!
def binary(l, r, key, choice):
    global count
    mid = (l + r) // 2

    if n[mid] == key:
        count += 1
        return

    # 왼쪽
    if n[mid] > key:
        if choice == 'rchoice' or choice == '':
            binary(l, mid-1, key, 'lchoice')
    # 오른쪽
    elif n[mid] < key:
        if choice == 'lchoice' or choice == '':
            binary(mid+1, r, key, 'rchoice')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = sorted(list(map(int, input().split())))
    m = list(map(int, input().split()))
    count = 0

    for i in range(len(m)):
        if m[i] not in n:
            continue
        else:
            binary(0, len(n)-1, m[i], '')
    print('#{} {}'.format(tc, count))


'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''