
T = int(input())
for tc in range(1, T+1):
    N = float(input())

    ans = []
    idx = 1

    # N이 0이 아닐 때까지 반복
    while N:
        ans.append(str(int((N // (1/(2**idx))))))
        N %= (1/(2**idx))
        idx += 1

    if len(ans) >= 13:
        result = 'overflow'
    else:
        result = ''.join(ans)

    print('#{} {}'.format(tc, result))


# num = 0.625 % 0.5
# print(num)
# number = 0.125 // 0.25
# print(number)
# if number == 0:
#     print('12')
# print(1/(2**3))