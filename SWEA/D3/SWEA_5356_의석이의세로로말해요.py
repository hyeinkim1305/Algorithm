
T = int(input())
for tc in range(1, T+1):
    words = [list(input()) for _ in range(5)]
    ans = ''

    for i in range(15):
        for j in range(5):
            if len(words[j]) < i+1:
                continue
            ans += words[j][i]
    print("#{} {}".format(tc, ans))