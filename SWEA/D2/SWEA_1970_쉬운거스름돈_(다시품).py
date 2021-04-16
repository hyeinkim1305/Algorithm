

T = int(input())
money =[50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    N = int(input())
    count = [0] * 8

    for i in range(8):
        if N // money[i]:       # 몫이 있으면
            count[i] = N//money[i]
            N %= money[i]

    print(f'#{tc}')
    for j in count:
        print(j, end=" ")
    print()

