# 다시 풀어보기 !!!!
# combinations 라이브러리 안 쓰고도 해보기!
# set에서 discard 사용 가능하다

from itertools import combinations

def solution(relation):
    r = len(relation[0])

    # 경우의 수 조합 구하기
    candidate = []
    for i in range(1, r + 1):
        candidate.extend(combinations(range(r), i))

    # 유일성 판단 - set에 넣어서 중복 제거하고 비교
    mini = []
    for c in candidate:
        valid = set()
        for r in relation:
            temp = ''
            for i in c:
                temp += r[i]
            valid.add(temp)
        if len(valid) == len(relation):
            mini.append(c)

    # 최소성 판단
    ans = set(mini)
    for i in range(len(mini)):
        for j in range(i + 1, len(mini)):
            if len(mini[i]) == len(set(mini[i]) & set(mini[j])):
                ans.discard(mini[j])

    return len(ans)


# 다른 풀이 공부

def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))