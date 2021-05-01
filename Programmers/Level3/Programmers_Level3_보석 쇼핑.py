'''
# 어려웠음! 비슷한 유형 풀어보기!
투 포인터 알고리즘, 시작점과 끝점을 이용해 동시에 증가하면서 순차적으로 탐색하는 것
찾고자하는 구간의 조건을 만족할때까지 끝점을 먼저 증가시키고,
그 뒤에 해당 구간을 최소화하도록 시작점을 증가시켜 최소구간을 찾는다.
'''

def solution(gems):

    gem = {}
    l, r = 0, 0
    g = len(set(gems))
    min_g = len(gems) + 1

    # l과 r이 len(gems) 보다 작을 때 까지
    while l < len(gems) and r < len(gems):
        if gems[r] in gem:
            gem[gems[r]] += 1
        else:
            gem[gems[r]] = 1
        r += 1
        # 모든 보석이 들어갔을 경우
        if len(gem) == g:
            while l < r:
                # 시작점을 늘려나간다.
                if gem[gems[l]] > 1:
                    gem[gems[l]] -= 1
                    l += 1
                # 시작점의 값이 1만큼 있을 때때
               elif min_g > r - l:
                    min_g = r - l
                    answer = [l + 1, r]
                    break
                else:                   # 어느쪽도 아닐 때 break 넣어줘야 무한루프 안 빠짐!
                    break
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)