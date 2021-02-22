'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01
'''


T = int(input())

for tc in range(1, T+1):
    card = input()
    shape = ['S', 'D', 'H', 'C']
    shape_n = [[0 for _ in range(14)] for _ in range(4)]
    for i in range(0, len(card), 3):
        ans = 0
        for j in range(len(shape)):
            if card[i] == shape[j]:
                shape_n[j][int(card[i+1:i+3])] += 1
                if shape_n[j][int(card[i+1:i+3])] >= 2:
                    shape_n[j][0] = 'ERROR'
                    break

    answer = []
    for i in shape_n:
        if i[0] == 'ERROR':
            print('#{} {}'.format(tc, 'ERROR'))
            break
        answer.append(str((13-sum(i))))
    else:
        print('#{} {}'.format(tc, ' '.join(answer)))
