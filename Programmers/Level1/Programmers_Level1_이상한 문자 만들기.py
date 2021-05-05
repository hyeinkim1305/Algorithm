
'''
split()은 스페이스, 탭, 엔터 등 모든 공백을 기준으로 문자열을 나누는데 반해,
문제에서 스페이스 만을 기준으로 나눈다고 하였으므로 split(" ") 으로 해야한다!
문제를 잘 읽어야한다
'''
def solution(s):
    s = s.split(" ")
    answer = ''

    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '

    return answer[:-1]