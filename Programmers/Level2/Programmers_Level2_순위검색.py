'''
카카오 블로그 문제 해설 참고
-> 지원자들을 분류 후 같은 그룹의 지원자끼리 묶어두고, 해당 그룹에서 점수를 기준으로 오름차순 정렬.
검색조건이 주어질 경우 INFO 배열에서 지원자들을 찾지 않고, 미리 분류해둔 그룹에서 X점 이상 맞은 지원자 수를
세주면 된다. 이는 binary search의 lower bound를 이용하면 된다.
'''
'''
defaultdict : 딕셔너리의 서브 클래스, 디폴트 값을 설정할 수 있다. 
-> 즉, 값을 지정하지 않으면 빈 리스트로 초기화한다. 
remove : 리스트 요소 제거
binary lower bound : 데이터 내에서 특정 값보다 같거나 큰 값이 처음 나오는 위치를 리턴
-> 바로 리턴하는 것이 아니라 처음으로 나오는 값을 찾기 위해 end = mid로 하고 범위를 좁혀간다.
'''
from itertools import combinations
from collections import defaultdict
def solution(info, query):

    inform = defaultdict(list)
    answer = []

    for inf in info:
        inf = inf.split()
        score = inf[-1]
        inf = inf[:-1]

        # 조합으로 경우의 수 만들어서 dict에 키(정보), 밸류(스코어) 넣기
        for i in range(5):
            for c in combinations(inf, i):
                inform[''.join(c)].append(int(score))

    # dict의 밸류값들 오름차순 정렬. 그래야 나중에 X점 이상값 찾을 때 이분탐색 할 수 있음
    for j in inform.keys():
        inform[j].sort()

    # 쿼리도 딕셔너리의 키값처럼 변경
    for q in query:
        q = q.split()
        sco = int(q[-1])
        q = q[:-1]
        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        qu = ''.join(q)

        # binary search. lower bound
        if qu in inform:
            score = inform[qu]
            if len(score) > 0:
                start, end = 0, len(score)
                while start < end:
                    mid = (start + end) // 2
                    if score[mid] >= sco:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(score)-start)
        else:
            answer.append(0)


    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))

