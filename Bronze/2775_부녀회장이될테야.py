
# 테스트케이스
T = int(input())
for tc in range(T):
    K = int(input())
    N = int(input())
    # 1층 사람 수 리스트
    people = [i for i in range(1, N+1)]

    for j in range(K):
        for k in range(1, N):
            people[k] = people[k] + people[k-1]

    output = people[-1]
    print(output)

