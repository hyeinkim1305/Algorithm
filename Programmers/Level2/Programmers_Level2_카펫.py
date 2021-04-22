'''
무조건 3이상
가운데 영역 개수 세보기
'''


def solution(brown, yellow):
    total = brown + yellow

    for i in range(3, int(total ** 0.5) + 1):
        if total % i == 0:  # 나누어 떨어지면
            j = total // i
            if (i - 2) * (j - 2) == yellow:
                if i >= j:
                    left, right = i, j
                else:
                    left, right = j, i
                answer = [left, right]

                return answer