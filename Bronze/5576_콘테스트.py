
# 버블 정렬로 해서 높은 점수 3명꺼만 가져오기
for i in range(2):
    number = []
    for j in range(10):
        n = int(input())
        number += [n]

    for k in range(9, 6, -1):
        for t in range(k):
            if number[t] > number[t+1]:
                number[t], number[t+1] = number[t+1], number[t]

    output = number[-1] + number[-2] + number[-3]
    print(output, end=" ")


# 이중 리스트 만들기
# output = []
# for i in range(2):
#     number = []
#     for _ in range(10):
#         n = int(input())
#         number += [n]
#     output += [number]
# print(output)