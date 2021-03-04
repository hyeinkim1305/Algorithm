
'''
일단 피자를 화덕 크기 만큼 넣고 [7, 1]
치즈 양 절반으로 바꾸고 꺼내서 뒤로 보내
만약 위치가 0인데 치즈양이 0이면 꺼내고 배열에 남아있는거 넣어(안남아있다면 그냥 패스)

3
3 5
7 2 6 5 3
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    for i in range(M):      # 인덱스를 같이 표기
        C[i] = [C[i], i]    # [[7, 0], [2, 1], [6, 2], [5, 3]] 이런 식

    q = []

    while len(q) < N:
        q.append(C.pop(0))

    while len(q) > 1:
        if q[0][0] == 0:    # 치즈가 다 녹았으면
            if len(C) == 0:     # 더이상 넣을 피자가 없으면
                q.pop(0)    # 꺼내고
            else:
                q[0] = C.pop(0)     # 꺼낼 자리에 새로운 거를 넣어

        else:
            q[0][0] //= 2
            a = q.pop(0)
            q.append(a)
        # 여기까지 하면 한 바퀴 돈 것

    ans = q[0][1] + 1   # 인덱스 + 1

    print('#{} {}'.format(tc, ans))


