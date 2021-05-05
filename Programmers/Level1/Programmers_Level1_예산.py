def solution(d, budget):
    # 오름차순 정렬
    d.sort()

    answer = 0

    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break

    return answer
