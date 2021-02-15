
def prime_list(n):
    # 에라토스테네스의 체 초기화
    # 어짜피 자기자신은 포함안되니까 n까지 해도 됨
    ans = [True] * n

    for i in range(2, int(n**0.5)+1):
        if ans[i] == True:
            for j in range(i+i, n, i):
                ans[j] = False
    return [i for i in range(2, n) if ans[i] == True]


T = int(input())
for tc in range(T):
    N = int(input())
    number = prime_list(N)
    # 가운데부터 시작한다.
    for i in range(N//2, 1, -1):
        if (i in number) and (N-i in number):
            print(i, N-i)
            break

# 시간초과
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     answer = []
#     for k in prime_list(N):
#         if k <= N //2:
#             if (N-k) in prime_list(N):
#                 answer.append([k, N-k])
#         else:
#             break
#     print(answer[-1][0], answer[-1][1])




# 만약 여러가지 인 경우, 더 멀리떨어져 있는 것으로 선정
# 반으로 나눈 값까지는 탐색

