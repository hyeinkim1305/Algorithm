

def solution(answers):
    n = len(answers)
    a_cnt, b_cnt, c_cnt = 0, 0, 0
    # 1번 수포자
    first = [i for i in range(1, 6)] * (n // 5) + [i for i in range(1, (n % 5)+1)]
    for j in range(n):
        if answers[j] == first[j]:
            a_cnt += 1

    # 2번 수포자
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    second = sec * (n // 8) + sec[:(n % 8)]
    for j in range(n):
        if answers[j] == second[j]:
            b_cnt += 1

    # 3번 수포자
    th = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    third = [i for i in th] * (n // 10) + th[:(n % 10)]
    for j in range(n):
        if answers[j] == third[j]:
            c_cnt += 1

    answer = []
    cnt = [a_cnt, b_cnt, c_cnt]
    max_cnt = max(cnt)
    for i in range(3):
        if cnt[i] == max_cnt:
            answer.append(i+1)

    return answer

answers = [1,3,2,4,2]
print(solution(answers))

'''
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
'''
n = 20
th = [3, 3, 1, 1, 2, 2, 4, 4]
third = [i for i in th] * (n // 8) + th[:(n % 8)]
print(third)


'''
추가로 공부한 다른사람풀이
--> enumerate를 활용해서 answer의 인덱스값과 pattern의 길이를 나눠준 나머지로 해도 가능하다.
for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
'''