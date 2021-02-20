
# 회의가 가장 빨리 끝나는 순서대로 정렬 후 구한 최대 개수 풀이
N = int(input())
me = [list(map(int, input().split())) for _ in range(N)]

me.sort(key=lambda x : (x[1], x[0]))

endtime, ans = 0, 0
for i in range(len(me)):
    if me[i][0] >= endtime:
        endtime = me[i][1]
        ans += 1
print(ans)


# 시간 초과 풀이
# N = int(input())
# me = [list(map(int, input().split())) for _ in range(N)]
#
# ro = []  # 회의실
# for i in range(len(me)):  # 회의실 배정
#     if i == 0:
#         ro.append(me[i])
#         continue
#     min_time = 987654321987
#     min_j = -1
#     for j in range(len(ro)):
#
#         # 회의실 배정을 따로하는 조건 1
#         if (me[i][0] >= ro[j][0] and me[i][0] < ro[j][1]) or (me[i][1] > ro[j][0] and me[i][1] <= ro[j][1]) or (me[i][0] <= ro[j][0] and me[i][1] >= ro[j][1]):
#             continue
#         # 같은 회의실 사용이 가능한 경우
#         else:
#             if abs(me[i][0]-ro[j][-1]) < min_time:
#                 min_time = abs(me[i][0]-ro[j][-1])
#                 min_j = j
#
#     if min_j != -1:  # 같은 회의실 사용이 가능
#         ro[min_j].extend(me[i])
#     else:
#         ro.append(me[i])
#
# # 회의의 최대 개수
# max_len = -1
# for i in range(len(ro)):
#     if len(ro[i]) > max_len:
#         max_len = len(ro[i])
# print(max_len // 2)
#
