
def solution(people, limit):
    p = sorted(people, reverse=True)
    answer = 0

    # 가장 무거운거 인덱스, 가장 가벼운거 인덱스
    i, j = 0, len(p) - 1
    while True:
        # 마지막 하나 남았을 경우
        if i == j:
            answer += 1
            break

        # 끝났을 경우
        if i > j:
            break

        if p[i] + p[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            i += 1
    return answer