# 시간초과
# M, N = map(int, input().split())
# number = []
#
# for num in range(M, N+1):
#     count = 1
#     for n in range(2, int(num**0.5)+1):
#         if num % n == 0:
#             count = 0
#             break
#         else:
#             count += 1
#     if count > 0:
#         number.append(num)
# for j in number:
#     print(j)

def test(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True

M, N = map(int, input().split())

for num in range(M, N+1):
    if test(num):
        print(num)




