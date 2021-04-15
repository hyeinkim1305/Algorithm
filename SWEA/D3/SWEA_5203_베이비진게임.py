
def babygin(n, dic):

    # 해당 숫자가 dict에 들어있는지 확인
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

    # 같은 숫자가 3개이상인지 확인
    if dic[n] >= 3:
        return True

    # 연속된 숫자가 3개 이상인지 확인
    for i in range(3):
        if (n-2+i in dic) and (n-1+i in dic) and (n+i in dic):
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    case = list(map(int, input().split()))
    player1 = {}
    player2 = {}

    for i in range(len(case)):
        if i % 2 == 0:      # 플레이어1
            if babygin(case[i], player1):
                print(f'#{tc} {1}')
                break
        else:       # 플레이어2
            if babygin(case[i], player2):
                print(f'#{tc} {2}')
                break
    else:
        print(f'#{tc} {0}')



