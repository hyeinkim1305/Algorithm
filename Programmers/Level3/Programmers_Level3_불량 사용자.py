'''
처음에는 조합으로 생각하고 풀었으나 문자열 비교하는 과정에서 (순서에 따라 결과값이 달라질 수 있어서?) 해결하지 못 했다
따라서 순열로 하고 점검해주었다!
+ 프로그래머스 다른 사람 풀이를 보니 조합으로도 풀 수 있다!
'''

# 순열로 경우의 수 구한 코드
def check(id, banned_id):
    for i in range(len(id)):
        if len(id[i]) != len(banned_id[i]):         # 길이 자체가 다르다면 False
            return False
        else:
            for j in range(len(id[i])):             # 글자 하나하나 비교
                if banned_id[i][j] == '*':
                    continue
                elif id[i][j] == banned_id[i][j]:
                    continue
                else:
                    return False
    return True

def perm(idx, u, b, sel, vis):
    global id_list
    if idx == b:
        id_list.append(sel[:])
        return
    else:
        for i in range(u):
            if vis[i] == 0:
                sel[idx] = user_id[i]
                vis[i] = 1
                perm(idx+1, u, b, sel, vis)
                vis[i] = 0


def solution(user_id, banned_id):
    global id_list
    u = len(user_id)
    b = len(banned_id)
    sel = [0] * b
    vis = [0] * u
    id_list = []

    perm(0, u, b, sel, vis)

    answer = []
    for id in id_list:
        if check(id, banned_id):
            if set(id) not in answer:
                answer.append(set(id))
    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
solution(user_id, banned_id)


# 조합으로 경우의 수 구한 틀린 코드 / 점검할 때 조금씩 오차가 생김
def combi(i, j, temp, user_id, u, b):
    global id_list
    if i == b:
        id_list.append(temp[:])
    else:
        for k in range(j, u - b + i + 1):
            temp[i] = user_id[k]
            combi(i + 1, k + 1, temp, user_id,  u, b)

def check(id, banned_id):
    for i in range(len(id)):
        if len(id[i]) != len(banned_id[i]):         # 길이 자체가 다르다면 False
            return False
        else:
            for j in range(len(id[i])):             # 글자 하나하나 비교
                if banned_id[i][j] == '*':
                    continue
                elif id[i][j] == banned_id[i][j]:
                    continue
                else:
                    return False
    return True


def solution(user_id, banned_id):
    global id_list
    u = len(user_id)
    b = len(banned_id)
    temp = [0] * b
    id_list = []

    combi(0, 0, temp, user_id, u, b)

    answer = 0
    for id in id_list:
        if check(id, banned_id):
            answer += 1
    print(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
solution(user_id, banned_id)