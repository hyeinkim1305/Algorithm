def solution(N, stages):
    answer = []

    s = len(stages)
    for i in range(1, N + 1):
        # 아직 클리어하지 못한 플레이어 수
        if s:
            cnt = stages.count(i)
            fail = cnt / s
            answer.append([fail, i])
            s -= cnt
        # else를 처음에 안 넣어서 런타임에러가 있었다
        else:
            answer.append([0, i])

    answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    ans = [i[1] for i in answer]
    return ans