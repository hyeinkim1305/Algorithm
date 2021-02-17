
N, M = map(int, input().split())
card = list(map(int, input().split()))

min_card = M+1
for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            sum_card = card[i] + card[j] + card[k]
            if sum_card <= M:
                if M - sum_card < min_card:
                    output = sum_card
                    min_card = M - sum_card      # 이거 빼먹었었음
            sum_card = 0
print(output)

# 시간초과
# N, M = map(int, input().split())
# card = list(map(int, input().split()))
# n = len(card)
# cards_list = []
# min_c = M + 1
# for i in range(1<<n):
#     cards = []
#     for j in range(n):
#         if i & (1<<j):
#             cards.append(card[j])
#     if len(cards) == 3 and sum(cards) <= M and (M-sum(cards)) <= min_c:
#         min_c = M-sum(cards)
#         output = sum(cards)
# print(output)