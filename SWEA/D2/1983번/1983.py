
T = int(input())
level = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(T):
    N, K = map(int, input().split())
    scores = []
    for j in range(N):
        a, b, c = map(int, input().split())
        score = (a * 0.35 + b * 0.45 + c * 0.2)
        scores.append(score)

    result = []
    for idx, score in enumerate(scores):
        result.append((score, idx+1))

    result = sorted(result, reverse=True)

    level_position = 0
    for n in range(N):
        if result[n][1] == K:
            level_position = (n // (N//10))
        
    print('#{} {}'.format(i+1, level[level_position]))


    


