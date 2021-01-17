n = int(input())
for i in range(n):
    m = input()
    score = 0
    sumscore = 0
    for j in m:
        if j == 'O':
            score += 1     # score에 1 더해줌
        else:
            score = 0      # score 초기화
        sumscore += score  # if문 끝날 때
    print(sumscore)        # for문 끝날 때 
    
