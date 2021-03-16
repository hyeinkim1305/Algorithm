
# n은 시작인덱스, k는 끝 인덱스, r은 지금까지합
def f(n, k, r, op1, op2, op3, op4):
    global min_sum
    global max_sum

    if n == k:
        if r < min_sum:
            min_sum = r
        if r > max_sum:
            max_sum = r
        return
    else:
        if op1 > 0:
            f(n+1, k, r+num[n], op1-1, op2, op3, op4)

        if op2 > 0:
            f(n+1, k, r-num[n], op1, op2-1, op3, op4)

        if op3 > 0:
            f(n+1, k, r*num[n], op1, op2, op3-1, op4)

        if op4 > 0:
            if (r < 0 and num[n] > 0) or (r > 0 and num[n] < 0):
                f(n+1, k, (abs(r)//abs(num[n]))*(-1), op1, op2, op3, op4-1)
            elif r < 0 and num[n] < 0:
                f(n+1, k, (abs(r)//abs(num[n])), op1, op2, op3, op4-1)
            else:
                f(n+1, k, r//num[n], op1, op2, op3, op4-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    si = list(map(int, input().split()))        # 연산자 수
    num = list(map(int, input().split()))   # 숫자
    max_sum = -100000789
    min_sum = 100000789
    f(1, N, num[0], si[0], si[1], si[2], si[3])

    print('#{} {}'.format(tc, max_sum-min_sum))





    # # 부분집합 말고 순열 재귀
    # sel = [0] * (N-1)   # 결과 저장 리스트
    # check = [0] * (N-1)     # 사용했는지 체크
    # max_sum = -100000789
    # min_sum = 100000789
    # perm(0)
    # print('#{} {}'.format(tc, max_sum-min_sum))





# 순열 재귀로 풀었을 떄는 중복되는 경우가 너무 많아 시간초과가 나옴
# def perm(idx):
#     global max_sum
#     global min_sum
#     if idx == N - 1:
#         for i in range(N):
#             if i == 0:
#                 sum = num[i]
#             else:
#                 if sel[i-1] == '+':
#                     sum += num[i]
#                 elif sel[i-1] == '*':
#                     sum *= num[i]
#                 elif sel[i-1] == '-':
#                     sum -= num[i]
#                 elif sel[i-1] == '/':
#                     if (num[i] < 0 and sum > 0) or (num[i] > 0 and sum < 0):
#                         sum = (abs(sum) // abs(num[i])) * (-1)
#                     elif num[i] < 0 and sum < 0:
#                         sum = (abs(sum) // abs(num[i]))
#                     else:
#                         sum //= num[i]
#         if sum < min_sum:
#             min_sum = sum
#         if sum > max_sum:
#             max_sum = sum
#         return
#
#         # print(sel)
#         # return
#     else:
#         for i in range(N - 1):
#             if check[i] == 0:
#                 sel[idx] = sign[i]
#                 check[i] = 1
#                 perm(idx + 1)
#                 check[i] = 0  # 원상복구
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     si = list(map(int, input().split()))
#     num = list(map(int, input().split()))
#     obj = ['+', '-', '*', '/']
#     sign = []
#     for i in range(4):      # 연산자를 리스트에 넣기
#         if si[i] != 0:
#             for j in range(si[i]):
#                 sign.append(obj[i])
#     # ['+', '+', '-', '/']
#     # 부분집합 말고 순열 재귀
#     sel = [0] * (N-1)   # 결과 저장 리스트
#     check = [0] * (N-1)     # 사용했는지 체크
#     max_sum = -100000789
#     min_sum = 100000789
#     perm(0)
#     print('#{} {}'.format(tc, max_sum-min_sum))



