
T = int(input())

for tc in range(T):
    R, S = input().split()
    word = ''
    for i in S:
        word += int(R) * i
    print(word)
