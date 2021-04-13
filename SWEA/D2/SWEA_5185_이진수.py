
T = int(input())

for tc in range(1, T+1):
    N, num = input().split()
    ans = []

    # 16진수를 2진수로 바꾸기
    for n in num:
        if n.isalpha():     # 알파벳이면
            temp = ord(n) - 65 + 10
        else:
            temp = int(n)

        for i in range(3, -1, -1):
            if temp & (1<<i):
                ans.append('1')
            else:
                ans.append('0')

    print('#{} {}'.format(tc, ''.join(ans)))
