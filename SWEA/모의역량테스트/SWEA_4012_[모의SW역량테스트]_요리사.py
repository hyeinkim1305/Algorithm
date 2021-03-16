
def foodsum(arr):
    arr_sum = 0
    for i in arr:
        for j in arr:
            arr_sum += grad[i-1][j-1]
    return arr_sum

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = list(range(1,N+1))
    grad = [list(map(int, input().split())) for _ in range(N)]

    food1 = []      # food1 비트 부분집합으로 구하고
    for i in range(1<<N):
        fo = []
        for j in range(N):
            if i & (1<<j):
                fo.append(n[j])
        if len(fo) == N // 2:
            food1.append(fo)

    min_sub = 987654321654
    for i in range(len(food1)):     # food1 순회하면서 각 경우에 대해 food2 구함
        food2 = list(set(n) - set(food1[i]))
        sub = abs(foodsum(food1[i]) - foodsum(food2))
        if sub < min_sub:
            min_sub = sub

    print('#{} {}'.format(tc, min_sub))



# 헷갈렸던 부분 (아래는 다 가능한 코드)
# arr = {1, 2, 3, 7, 9} - {3, 9}
# print(arr, type(arr))
# a = [4, 6, 8, 9, 10]
# print(set(a))
# b = set(list(range(1, 8)))
# print(b)
# c = {i for i in range(1, 10)}
# print(c)
# d = {5, 7, 8, 9}
# print(list(d))


# 비트로 부분집합구하기
# arr = [3, 5, 6, 8, 3]
# N = len(arr)
# for i in range(1<<N):
#     for j in range(N):
#         if i & (1<<j):
#             print(arr[j], end=' ')
#     print()
# print()