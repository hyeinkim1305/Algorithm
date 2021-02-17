

planet = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
p = len(planet)

T = int(input())
for tc in range(1, T+1):
    test = input()
    words = input().split()

    planet_cnt = [0 for _ in range(p)]  # 카운트

    for w in words:
        for i in range(p):
            if w == planet[i]:
                planet_cnt[i] += 1
                break
            else:
                continue
    output = []
    for j in range(p):
        output += [planet[j]] * planet_cnt[j]

    print('#{}'.format(tc))
    print(' '.join(output))


    # print(f"#{tc}")
    # for i in range(p):
    #     for j in range(planet_cnt[i]):
    #         print(planet[i], end=" ")   # 이런식으로 할 수도 있다.