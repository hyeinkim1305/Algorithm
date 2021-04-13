
# D4
# 기존 원소들에 새로운 원소를 더한 값들을 추가해주는 방식 + set활용
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    s = len(score)

    # 기존 값들에 새로운 값을 각각 더해서 추가하느데 중복을 제거
    ans = {0}

    for i in range(s):
        temp = set()
        for j in ans:       # ans에 넣으면 길이가 변하니까 일단 temp에
            if j + score[i] not in ans:
                temp.add(j + score[i])
        for k in temp:
            ans.add(k)

    print('#{} {}'.format(tc, len(ans)))






# 부분집합 -> 시간초과
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     score = list(map(int, input().split()))
#     s = len(score)
#     cnt = []
#
#     for i in range(1<<s):
#         sum_score = 0
#         for j in range(s):
#             if i & (1<<j):
#                 sum_score += score[j]
#         if sum_score in cnt:
#             continue
#         else:
#             cnt.append(sum_score)
#
#
#     print('#{} {}'.format(tc, len(cnt)))

