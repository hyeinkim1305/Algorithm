
# 버블정렬로 해보기
number = list(map(int, input().split()))

for j in range((len(number)-1), 0, -1):
    for i in range(j):
        if number[i] > number[i+1]:
            number[i], number[i+1] = number[i+1], number[i]   # 순서가 바뀐다

for num in number:
    print(num, end=" ")

