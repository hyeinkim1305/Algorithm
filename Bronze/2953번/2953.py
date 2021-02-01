scores = []
for i in range(5):
    score = list(map(int,input().split()))
    scores.append((i+1, sum(score)))       # 튜플로 넣기

# 튜플로 내림차순 정렬
scores = sorted(scores, key = lambda x : -x[1])

print(scores[0][0], scores[0][1])
