'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''

def pre_order(idx):
    global cnt
    if idx:
        pre_order(child1[idx])
        cnt += 1
        pre_order(child2[idx])

T = int(input())

# 입력값 받아서 트리 만들기
for tc in range(1, T+1):
    E, N = map(int, input().split())
    child1 = [0] * (E+2)
    child2 = [0] * (E+2)
    data = list(map(int, input().split()))
    for i in range(E):
        if child1[data[i*2]]:
            child2[data[i*2]] = data[i*2+1]
        else:
            child1[data[i*2]] = data[i*2+1]
    cnt = 0
    pre_order(N)
    print('#{} {}'.format(tc, cnt))



