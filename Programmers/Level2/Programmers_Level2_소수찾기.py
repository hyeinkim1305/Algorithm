
# 경우의 수 구하기
def perm(idx, n, N, sel, vis, numbers):
    global ans
    if idx == N:
        ans.append(sel[:])
    else:
        for i in range(n):
            if vis[i] == 0:
                vis[i] = 1
                sel[idx] = numbers[i]
                perm(idx+1, n, N, sel, vis, numbers)
                vis[i] = 0

# 소수인지 판단
def primary(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    global ans

    numbers = list(numbers)
    n = len(numbers)
    ans = []

    # 경우의수 따지기
    for i in range(1, len(numbers)+1):
        sel = [0] * i
        vis = [0] * n
        perm(0, n, i, sel, vis, numbers)

    # 경우의 수 집합
    pos = set()
    for j in ans:
        temp = ''.join(j).lstrip('0')
        if temp != '':
            pos.add(temp)

    # 소수인것 추리기
    answer = []
    for p in pos:
        if primary(int(p)):
            answer.append(int(p))
        else:
            continue

    return len(answer)

numbers = "17"
solution(numbers)
