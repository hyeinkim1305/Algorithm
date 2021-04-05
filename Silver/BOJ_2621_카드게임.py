'''
B 2
B 1
B 3
B 5
B 4

'''
def rule():
    global score
    # 규칙1
    if len(cards) == 1:
        nums = list(cards.values())[0]
        for i in range(4):
            if nums[i+1] != nums[i] + 1:
                score.append(600 + nums[4])           # 규칙4
                break
        else:
            score.append(900 + nums[4])

    if len(number) == 2:
        if 4 in number.values():        # 규칙2
            for i in number.keys():
                if number[i] == 4:
                    score.append(800+i)
        elif 3 in number.values() and 2 in number.values():     # 규칙3
            for i in number.keys():
                if number[i] == 3:
                    sc = i * 10
                if number[i] == 2:
                    sc += i + 700
                    score.append(sc)

    if 3 in number.values():        # 규칙6
        for i in number.keys():
            if number[i] == 3:
                score.append(400+i)

    if 2 in number.values():        # 규칙8
        for i in number.keys():
            if number[i] == 2:
                score.append(200+i)

    # 규칙 5
    if len(number) == 5:
        nums = sorted(list(number.keys()))
        for i in range(4):
            if nums[i+1] != nums[i] + 1:
                break
        else:
            score.append(500+nums[4])


    # 규칙 7
    n = []
    if len(number) == 3:
        for i in number.keys():
            if number[i] == 2:
                n.append(i)
        if len(n) == 2:
            n = sorted(n)
            score.append(n[1]*10+n[0]+300)

    # 규칙9
    if len(score) == 0:
        score.append(sorted(list(number.keys()))[4]+100)

    return max(score)

# 딕셔너리에 담기 + 정렬도 진행
cards = {}
number = {}
for i in range(5):
    alpha, num = input().split()
    if alpha in cards.keys():
        cards[alpha].append(int(num))
        cards[alpha] = sorted(cards[alpha])
    else:
        cards[alpha] = [int(num)]
    if int(num) in number.keys():
        number[int(num)] += 1
    else:
        number[int(num)] = 1
score = []

print(rule())







# dict = {'a':[2,5,7,8,10]}
# print(dict.keys())
# print(list(dict.keys()))
# print(list(dict.keys())[0])
# print(list(dict.values())[0])