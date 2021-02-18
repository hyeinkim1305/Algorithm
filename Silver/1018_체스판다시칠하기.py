
N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

# number = (M-8+1) * (N-8+1)  # 실행 횟수
min_cnt = 987654321
for i in range(N-8+1):
    for j in range(M-8+1): # 여기까지 시작지점 설정
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k+l)%2 == 1:
                    if chess[k][l] == 'W':
                        cnt1 += 1
                    elif chess[k][l] == 'B':
                        cnt2 += 1
                else:
                    if chess[k][l] == 'B':
                        cnt1 += 1
                    elif chess[k][l] == 'W':
                        cnt2 += 1
        if cnt1 < min_cnt:
            min_cnt = cnt1
        if cnt2 < min_cnt:
            min_cnt = cnt2

print(min_cnt)

############################################################################
# 첫 시작이 B일 때, W일 때 나눠서 생각 못해서 틀림

# number = (M-8+1) * (N-8+1)  # 실행 횟수
# min_cnt = 987654321
# for i in range(N-8+1):
#     for j in range(M-8+1): # 여기까지 시작지점 설정
#         count = 0
#         for k in range(i, i + 8):
#             cnt = 0     #
#             for l in range(j, j + 8-1):
#                 if chess[k][l] == 'B':
#                     if chess[k][l + 1] == 'B':
#                         cnt += 1
#                 if chess[k][l] == 'W':
#                     if chess[k][l + 1] == 'W':
#                         cnt += 1
#             if cnt % 2 == 0:
#                 count += cnt // 2
#             else:
#                 count += int(cnt // 2) + 1
#         if count < min_cnt:
#             min_cnt = count
# print(min_cnt)