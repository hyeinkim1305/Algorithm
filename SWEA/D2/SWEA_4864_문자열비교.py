'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''


T = int(input())
for tc in range(1, T+1):
    N = list(input())
    n = len(N)
    M = list(input())
    m = len(M)

    count = 0
    for i in range(m-n+1):   # 검사 횟수 만큼
        cnt = 0
        for j in range(n):   # N 길이만큼
            if N[j] == M[j+i]:
                cnt += 1
        if cnt == n:
            count = 1
            break
    if count == 1:
        print('#{} {}'.format(tc, count))
    else:
        print('#{} {}'.format(tc, count))
