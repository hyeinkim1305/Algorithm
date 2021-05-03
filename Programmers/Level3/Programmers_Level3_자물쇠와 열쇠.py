'''
lock의 세배 만큼 배열 만들고 (패딩 배열처럼)
key를 4번 회전할 떄 각각 비교해서 판단
이때, 열쇠가 자물쇠와 맞는지는 lock의 빈 공간 개수로 따져주었다.
Point!
문제 조건 잘 보기! 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다는 조건을 넣지 않아서 계속 틀렸었음.
'''
import copy
def solution(key, lock):
    # lock의 3배 배열 가운데에 lock을 넣는다.
    l = len(lock)
    locks = [[2] * (l * 3) for _ in range(l)]
    cnt = 0
    for i in range(l):
        lo = [2] * l + lock[i] + [2] * l
        locks.append(lo)
        # lock의 빈 곳이 몇 개인지 확인
        cnt += lock[i].count(0)
    locks += [[2] * (l * 3) for _ in range(l)]

    if cnt == 0:
        return True

    # key 회전
    for _ in range(4):
        key = spin(key, locks, cnt, l)
        if check(key, locks, cnt, l):
            return True
        else:
            continue
    return False


def spin(key, locks, cnt, l):
    k = len(key)
    new_key = [[0] * l for _ in range(l)]
    for i in range(k):
        for j in range(k):
            new_key[j][l-1-i] = key[i][j]
    return new_key


def check(key, locks, cnt, l):
    n = len(locks)
    k = len(key)
    s = 0
    # 이차원 배열
    while s <= n - k:
        m = 0
        while m <= n - k:
            cnts = cnt
            no = 0
            for i in range(k):
                for j in range(k):
                    # 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됨
                    if key[i][j] == 1 and locks[i + s][j + m] == 1:
                        no += 1
                    if key[i][j] == 1 and locks[i + s][j + m] == 0:
                        cnts -= 1
                    if cnts == 0 and no == 0:
                        return True
            m += 1
        s += 1
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)