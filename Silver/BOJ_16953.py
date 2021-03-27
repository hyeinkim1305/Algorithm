
def change(a, b):
    q = [[a, 0]]

    while q:
        cur = q.pop(0)
        if cur[0] == b:
            return cur[1] + 1
        if cur[0] * 2 <= b:
            q.append([cur[0] * 2, cur[1] + 1])
        if cur[0] * 10 + 1 <= b:
            q.append([cur[0] * 10 + 1, cur[1] + 1])

    return -1

a, b = map(int, input().split())
print(change(a, b))


# 틀린 풀이 !
# def change(a, b, ans, cnt):
#     global min_cnt
#
#     if ans == b:
#         if cnt < min_cnt:
#             min_cnt = cnt
#
#     elif ans > b:
#         return
#
#     elif ans < b:
#
#         ans *= 2
#         cnt += 1
#         change(a, b, ans, cnt)
#         ans = ans * 10 + 1
#         cnt += 1
#         change(a, b, ans, cnt)
#
#
# a, b = map(int, input().split())
# min_cnt = 987654321
# change(a, b, a, 0)
# if min_cnt == 987654321:
#     print(-1)
# else:
#     print(min_cnt + 1)



