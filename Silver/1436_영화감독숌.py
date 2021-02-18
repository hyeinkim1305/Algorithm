
N = int(input())
cnt = 0
i = 1
while True:
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break
    i += 1

# 틀린 풀이
# def movie(num, cnt):
#     while True:
#         if num % 10 == 6:
#             for i in range(10):
#                 ans = (num // 10) * 10000 + 666 * 10 + i
#                 cnt += 1
#                 if cnt == N:
#                     return ans
#             num += 1
#         ans = num * 1000 + 666
#         num += 1   # 666 앞에 숫자
#         cnt += 1   # 개수
#         if cnt == N:
#             return ans
#
# N = int(input())
# count = 0
# number = 0
# print(movie(number, count))

