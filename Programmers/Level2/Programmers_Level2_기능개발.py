

def solution(progresses, speeds):
    answer = []
    while progresses:
        # 진행
        for i in range(len(progresses)):
            progresses += speeds[i]
        # 개수세기
        cnt = 0
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        answer.append(cnt)

    print(answer)

solution([93, 30, 55], 	[1, 30, 5])
